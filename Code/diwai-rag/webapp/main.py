"""DIWAI Library browser manager: add documents by drag-and-drop, see what
happened to each, find and remove documents. Low-vision layout.

    venv/bin/python -m uvicorn --factory webapp.main:create_app --host 127.0.0.1 --port 8766
"""
import fcntl
import os
import shutil
import signal
import threading
import uuid
from contextlib import asynccontextmanager
from pathlib import Path
from typing import List

import requests
from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import config
import rag_utils
from webapp import library
from webapp.activity import ActivityLog
from webapp.worker import Worker

HERE = Path(__file__).resolve().parent
MAX_UPLOAD_BYTES = 500 * 1024 * 1024
SHOW_ROWS = 100
# Only these Host names reach the app. A web page that DNS-rebinds its own name
# to 127.0.0.1 still sends its own name, so it is refused (finding 1).
LOOPBACK_HOSTS = {"127.0.0.1", "localhost"}
SAFE_METHODS = {"GET", "HEAD", "OPTIONS"}
SORT_KEYS = {"name": lambda d: d["source"].casefold(),
             "chunks": lambda d: d["chunks"],
             "added": lambda d: d["added_at"] or ""}


def lmstudio_ready():
    """LM Studio is usable when /v1/models lists the embedding model."""
    try:
        r = requests.get(f"{config.LMSTUDIO_BASE_URL}/v1/models", timeout=3)
        return r.ok and any(m.get("id") == config.EMBED_MODEL for m in r.json().get("data", []))
    except Exception:
        return False


def _default_quit():
    # SIGINT gives uvicorn a graceful shutdown, which stops the worker after
    # its current job (a Chroma write killed half-way can damage the store).
    threading.Timer(0.5, os.kill, (os.getpid(), signal.SIGINT)).start()


def create_app(collection=None, documents_dir=None, activity_path=None, ready=None,
               retry_seconds=15, on_quit=None, allowed_hosts=None):
    collection = collection if collection is not None else rag_utils.get_collection()
    documents_dir = documents_dir or config.DOCS_DIR
    activity_path = activity_path or str(HERE / f"activity-{config.PROFILE['name']}.db")
    ready = ready or lmstudio_ready
    on_quit = on_quit or _default_quit
    incoming_dir = os.path.join(documents_dir, ".incoming")
    os.makedirs(incoming_dir, exist_ok=True)

    allowed = set(allowed_hosts) if allowed_hosts else LOOPBACK_HOSTS
    log = ActivityLog(activity_path)
    index = library.DocIndex()
    worker = Worker(collection, documents_dir, log, index, ready, retry_seconds)

    @asynccontextmanager
    async def lifespan(app):
        # One manager per library. uvicorn runs this before it binds the port,
        # so a second copy must stop here, before it touches the job list
        # (finding 6).
        lock = open(activity_path + ".lock", "w")
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            lock.close()
            raise RuntimeError("Another library manager is already running.")
        try:
            log.mark_interrupted()
            # Every job is finished or interrupted now, so nothing in
            # .incoming belongs to a live job (finding 9).
            for name in os.listdir(incoming_dir):
                path = os.path.join(incoming_dir, name)
                if os.path.isfile(path):
                    os.remove(path)
            worker.start()
            yield
            worker.stop()
        finally:
            lock.close()

    app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None, openapi_url=None)
    app.state.log, app.state.index, app.state.worker = log, index, worker

    @app.middleware("http")
    async def same_origin_only(request: Request, call_next):
        """Refuse foreign Host names (DNS rebinding) and cross-site writes:
        another web page must never add, remove or quit (finding 1)."""
        host = (request.headers.get("host") or "").rsplit(":", 1)[0].strip("[]")
        if host not in allowed:
            return PlainTextResponse("Unknown host", status_code=400)
        if request.method not in SAFE_METHODS:
            origin = request.headers.get("origin")
            if origin is not None:
                o_host = origin.split("://", 1)[-1].split("/", 1)[0].rsplit(":", 1)[0].strip("[]")
                if o_host not in allowed:
                    return PlainTextResponse("Cross-site request refused", status_code=403)
            if request.headers.get("sec-fetch-site") == "cross-site":
                return PlainTextResponse("Cross-site request refused", status_code=403)
        return await call_next(request)
    app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
    templates = Jinja2Templates(directory=HERE / "templates")

    def render(request, name, **ctx):
        return templates.TemplateResponse(request, name, ctx)

    def header_ctx():
        docs, chunks = index.totals()
        return {"lm_up": ready(), "docs": docs, "chunks": chunks, "index_ready": index.ready,
                "index_error": index.error,
                "app_name": config.APP_NAME, "profile": config.PROFILE["name"]}

    # ---- pages and fragments ---------------------------------------------

    @app.get("/", response_class=HTMLResponse)
    def home(request: Request):
        return render(request, "page.html", **header_ctx(), jobs=log.recent(),
                      active=log.active_count(), max_bytes=MAX_UPLOAD_BYTES)

    @app.get("/healthz")
    def healthz():
        return {"ok": True}

    @app.get("/status", response_class=HTMLResponse)
    def status(request: Request):
        return render(request, "_status.html", **header_ctx())

    @app.get("/activity", response_class=HTMLResponse)
    def activity(request: Request):
        return render(request, "_activity.html", jobs=log.recent(), active=log.active_count())

    @app.get("/api/jobs")
    def api_jobs():
        return log.recent()

    @app.get("/api/library")
    def api_library():
        return {"rows": index.rows()}

    # ---- adding ----------------------------------------------------------

    @app.post("/upload", response_class=HTMLResponse)
    def upload(request: Request, files: List[UploadFile] = File(...)):  # plain def: copies run in a thread
        for f in files:
            name = library.safe_name(f.filename)
            if not library.supported(name):
                log.add(name, "add", state="done", outcome="refused",
                        message="❌ Can't add (unsupported type)",
                        detail="Supported: " + ", ".join(sorted(ingest_types())))
                continue
            dest = os.path.join(incoming_dir, uuid.uuid4().hex + os.path.splitext(name)[1].lower())
            size = 0
            too_big = False
            with open(dest, "wb") as out:
                while block := f.file.read(1 << 20):
                    size += len(block)
                    if size > MAX_UPLOAD_BYTES:
                        too_big = True
                        break
                    out.write(block)
            if too_big:
                os.remove(dest)
                log.add(name, "add", state="done", outcome="refused",
                        message="❌ Can't add (too large)",
                        detail=f"Limit {MAX_UPLOAD_BYTES // (1024 * 1024)} MB")
                continue
            worker.submit(log.add(name, "add", payload=dest))
        return render(request, "_activity.html", jobs=log.recent(), active=log.active_count())

    # ---- library tab -----------------------------------------------------

    @app.get("/library", response_class=HTMLResponse)
    def library_tab(request: Request, q: str = "", sort: str = "name", dir: str = "asc"):
        all_rows = index.rows()
        rows = library.filter_rows(all_rows, q)
        key = SORT_KEYS.get(sort, SORT_KEYS["name"])
        rows = sorted(rows, key=key, reverse=(dir == "desc"))
        return render(request, "_library.html", rows=rows[:SHOW_ROWS], shown=min(len(rows), SHOW_ROWS),
                      matched=len(rows), total=len(all_rows), q=q, sort=sort, dir=dir, index_ready=index.ready)

    @app.get("/library/detail", response_class=HTMLResponse)
    def detail(request: Request, doc_id: str):
        doc = index.get(doc_id)
        got = collection.get(where={"$and": [{"doc_id": doc_id}, {"chunk_index": 0}]},
                             include=["documents"]) if doc else {"documents": []}
        opening = (got["documents"][0][:200] if got["documents"] else "")
        return render(request, "_detail.html", doc=doc, opening=opening)

    @app.get("/library/confirm", response_class=HTMLResponse)
    def confirm(request: Request, doc_id: str):
        return render(request, "_confirm.html", doc=index.get(doc_id), doc_id=doc_id)

    @app.post("/remove", response_class=HTMLResponse)
    def remove(request: Request, doc_id: str = Form(...)):
        doc = index.get(doc_id)
        worker.submit(log.add(doc["source"] if doc else doc_id, "remove", payload=doc_id))
        return HTMLResponse('<p class="note" role="status">Removal queued. '
                            "The list refreshes when it finishes.</p>")

    # ---- quit ------------------------------------------------------------

    @app.post("/quit", response_class=HTMLResponse)
    def quit_(request: Request):
        busy = log.active_count()
        if busy:
            return HTMLResponse(f'<p class="note warn" role="alert">Busy: {busy} job(s) waiting '
                                "or working. Quit when they finish.</p>")
        on_quit()
        return HTMLResponse('<p class="note" role="status">Closing the library manager. '
                            "You can close this tab.</p>")

    return app


def ingest_types():
    import ingest
    return ingest.SUPPORTED
