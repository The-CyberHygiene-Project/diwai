"""Regression tests for the 2026-10-03 code review (findings 1-10).

Each test names its finding. Every one failed before its fix."""
import os
import sys
import threading
import time

import pytest
from fastapi.testclient import TestClient

import identifiers
import ingest
import mcp_server
import objectives
import rag_utils
from test_ingest import chunks_of, long_text, write
from test_webapp import TEXT, Switch, jobs, stored_files, upload, wait_done
from webapp import library, main


def make_app(temp_store, **kw):
    kw.setdefault("collection", rag_utils.get_collection())
    kw.setdefault("documents_dir", str(temp_store / "documents"))
    kw.setdefault("activity_path", str(temp_store / "activity.db"))
    kw.setdefault("ready", Switch(True))
    kw.setdefault("retry_seconds", 0.05)
    kw.setdefault("allowed_hosts", {"testserver"})
    return main.create_app(**kw)


@pytest.fixture
def app_env(temp_store, embed_calls):
    shutdowns = []
    app = make_app(temp_store, on_quit=lambda: shutdowns.append(True))
    with TestClient(app) as client:
        yield {"client": client, "docs": temp_store / "documents", "shutdowns": shutdowns}


# ---- 1. other web pages must not drive the manager --------------------------

EVIL = {"Origin": "http://evil.example"}


def test_1_cross_site_upload_is_refused(app_env):
    c = app_env["client"]
    r = c.post("/upload", files=[("files", ("planted.txt", TEXT))], headers=EVIL)
    assert r.status_code == 403
    assert jobs(c) == [] and stored_files(app_env["docs"]) == []


def test_1_cross_site_remove_and_quit_are_refused(app_env):
    c = app_env["client"]
    assert c.post("/remove", data={"doc_id": "x"}, headers=EVIL).status_code == 403
    assert c.post("/quit", headers=EVIL).status_code == 403
    assert jobs(c) == [] and app_env["shutdowns"] == []


def test_1_cross_site_fetch_metadata_without_origin_is_refused(app_env):
    r = app_env["client"].post("/quit", headers={"Sec-Fetch-Site": "cross-site"})
    assert r.status_code == 403 and app_env["shutdowns"] == []


def test_1_same_origin_post_is_allowed(app_env):
    r = app_env["client"].post("/quit", headers={"Origin": "http://testserver",
                                                 "Sec-Fetch-Site": "same-origin"})
    assert r.status_code == 200 and app_env["shutdowns"] == [True]


def test_1_foreign_host_header_is_refused_dns_rebinding(app_env):
    r = app_env["client"].get("/api/library", headers={"Host": "evil.example"})
    assert r.status_code == 400


def test_1_production_default_allows_only_loopback_names(temp_store, embed_calls):
    app = make_app(temp_store, allowed_hosts=None)
    with TestClient(app, base_url="http://127.0.0.1:8766") as c:
        assert c.get("/healthz").status_code == 200
        assert c.get("/healthz", headers={"Host": "localhost:8766"}).status_code == 200
        assert c.get("/healthz", headers={"Host": "testserver"}).status_code == 400


# ---- 2. a damaged index must not hang the manager ---------------------------

class FlakyCollection:
    """The real collection, except every read fails while BROKEN is on."""

    def __init__(self, col):
        self._col, self.broken = col, True

    def get(self, *a, **kw):
        if self.broken:
            raise RuntimeError("Error loading hnsw index")
        return self._col.get(*a, **kw)

    def __getattr__(self, name):
        return getattr(self._col, name)


def test_2_damaged_index_fails_jobs_clearly_and_quit_still_works(temp_store, embed_calls):
    col = FlakyCollection(rag_utils.get_collection())
    shutdowns = []
    app = make_app(temp_store, collection=col, on_quit=lambda: shutdowns.append(True))
    with TestClient(app) as c:
        upload(c, ("a.txt", TEXT))
        job = wait_done(c, 1)[0]
        assert job["outcome"] == "library_error" and "repair" in job["message"]
        assert "could not be opened" in c.get("/status").text
        assert c.post("/quit").status_code == 200 and shutdowns == [True]
        assert stored_files(temp_store / "documents") == []


def test_2_index_recovers_once_repaired_without_restart(temp_store, embed_calls):
    col = FlakyCollection(rag_utils.get_collection())
    app = make_app(temp_store, collection=col)
    with TestClient(app) as c:
        upload(c, ("a.txt", TEXT))
        wait_done(c, 1)
        col.broken = False
        upload(c, ("b.txt", TEXT))
        assert wait_done(c, 2)[0]["outcome"] == "added"


# ---- 3. an embedder hiccup is not "Couldn't read" ---------------------------

def test_3_brief_embedder_failure_is_retried_and_file_added(app_env, monkeypatch):
    real, calls = rag_utils.embed_texts, []

    def flaky(texts):
        calls.append(1)
        if len(calls) <= 2:
            raise ConnectionError("model still loading")
        return real(texts)
    monkeypatch.setattr(rag_utils, "embed_texts", flaky)
    upload(app_env["client"], ("a.txt", TEXT))
    assert wait_done(app_env["client"], 1)[0]["outcome"] == "added"


def test_3_lasting_embedder_failure_names_lm_studio_not_the_file(app_env, monkeypatch):
    def down(texts):
        raise ConnectionError("HTTP 500")
    monkeypatch.setattr(rag_utils, "embed_texts", down)
    upload(app_env["client"], ("a.txt", TEXT))
    job = wait_done(app_env["client"], 1, timeout=15)[0]
    assert job["outcome"] == "embed_failed"
    assert "LM Studio" in job["message"] and "Couldn't read" not in job["message"]


# ---- 4. replacing a document never loses the old copy -----------------------

def test_4_failed_replacement_keeps_the_old_chunks(temp_store, monkeypatch):
    col = rag_utils.get_collection()
    f = write(temp_store / "r.txt", long_text("old", 2000))
    first = ingest.ingest_file(str(f), col)
    write(f, long_text("new", 2000))

    def broken_upsert(*a, **kw):
        raise RuntimeError("disk full")
    monkeypatch.setattr(type(col), "upsert", broken_upsert)
    assert ingest.ingest_file(str(f), col).status == "error"
    monkeypatch.undo()
    got = chunks_of(col, ingest.doc_id_for(str(f)))
    assert len(got["ids"]) == first.chunks


# ---- 5. the document list is safe to read while the worker writes ------------

def test_5_index_reads_survive_concurrent_writes():
    idx = library.DocIndex()
    idx.docs = {f"d{i}": {"doc_id": f"d{i}", "source": f"s{i}", "chunks": 1,
                          "file_path": "", "added_at": ""} for i in range(20000)}
    idx.ready = True

    class Col:
        n = 0

        def get(self, where, include):
            Col.n += 1
            if Col.n % 2:
                return {"ids": [], "metadatas": []}
            return {"ids": ["c"], "metadatas": [{"source": "x"}]}

    stop, errors = threading.Event(), []

    def writer():
        while not stop.is_set():
            idx.refresh_doc(Col(), "churn")

    old = sys.getswitchinterval()
    sys.setswitchinterval(1e-6)
    t = threading.Thread(target=writer)
    t.start()
    try:
        for _ in range(200):
            try:
                idx.totals(), idx.rows(), idx.source_keys(), idx.by_path("/nope")
            except RuntimeError as exc:
                errors.append(exc)
                break
    finally:
        stop.set()
        t.join()
        sys.setswitchinterval(old)
    assert errors == []


# ---- 6. a second copy of the manager must not touch the first one's jobs -----

def test_6_second_instance_refuses_and_leaves_live_jobs_alone(temp_store, embed_calls):
    first = make_app(temp_store, ready=Switch(False))
    with TestClient(first) as c:
        upload(c, ("a.txt", TEXT))
        end = time.time() + 5
        while jobs(c)[0]["outcome"] != "paused" and time.time() < end:
            time.sleep(0.02)
        second = make_app(temp_store)
        with pytest.raises(RuntimeError, match="already running"):
            with TestClient(second):
                pass
        assert jobs(c)[0]["outcome"] == "paused"


# ---- 7. search errors say what actually failed; top_k is bounded -------------

@pytest.fixture
def lib(temp_store):
    col = rag_utils.get_collection()

    def add(name, text):
        ingest.ingest_file(str(write(temp_store / "docs" / name, text)), col)
    return add


def test_7_damaged_index_is_not_blamed_on_lm_studio(lib, monkeypatch):
    def broken(*a, **kw):
        raise RuntimeError("Error loading hnsw index")
    monkeypatch.setattr(identifiers, "retrieve_with_ids", broken)
    out = mcp_server.search_documents("chrony")
    assert "Start LM Studio" not in out and "repair" in out


def test_7_top_k_is_clamped(lib, monkeypatch):
    asked = []
    monkeypatch.setattr(identifiers, "retrieve_with_ids",
                        lambda q, k: asked.append(k) or [])
    for k in (-1, 0, 5, 100000):
        mcp_server.search_documents("chrony", top_k=k)
    assert asked == [1, 1, 5, mcp_server.MAX_TOP_K]


# ---- 8. every article on a page is kept -------------------------------------

def test_8_all_articles_kept_when_page_has_no_main(temp_store):
    f = write(temp_store / "kb.html", "<html><body><nav>Menu</nav>"
              "<article><h2>Advisory one</h2><p>First fix.</p></article>"
              "<article><h2>Advisory two</h2><p>Second fix.</p></article>"
              "<footer>Foot</footer></body></html>")
    text = ingest.read_file(str(f))
    assert "First fix." in text and "Second fix." in text
    assert "Menu" not in text and "Foot" not in text


# ---- 9. no orphaned files ---------------------------------------------------

def test_9_leftover_incoming_files_are_cleared_at_startup(temp_store, embed_calls):
    incoming = temp_store / "documents" / ".incoming"
    incoming.mkdir(parents=True)
    (incoming / "stale.txt").write_bytes(b"x" * 100)
    with TestClient(make_app(temp_store)):
        assert list(incoming.iterdir()) == []


def test_9_unexpected_error_leaves_no_files_behind(temp_store, embed_calls, monkeypatch):
    def boom(*a, **kw):
        raise RuntimeError("unexpected")
    monkeypatch.setattr(ingest, "ingest_file", boom)
    with TestClient(make_app(temp_store)) as c:
        upload(c, ("a.txt", TEXT))
        assert wait_done(c, 1)[0]["state"] == "done"
    docs = temp_store / "documents"
    assert stored_files(docs) == [] and list((docs / ".incoming").iterdir()) == []


def test_9_shutdown_mid_job_leaves_no_stored_copy(temp_store, embed_calls):
    with TestClient(make_app(temp_store, ready=Switch(False))) as c:
        upload(c, ("a.txt", TEXT))
        end = time.time() + 5
        while jobs(c)[0]["outcome"] != "paused" and time.time() < end:
            time.sleep(0.02)
    assert stored_files(temp_store / "documents") == []


# ---- 10. one scan of the library per question --------------------------------

def test_10_one_document_scan_per_question(lib, monkeypatch):
    lib("RB-04_clock.md", "RB-04 clock runbook. " * 20)
    real, scans = ingest.list_documents, []
    monkeypatch.setattr(ingest, "list_documents",
                        lambda col: scans.append(1) or real(col))
    identifiers.retrieve_with_ids("RB-04, RB-05, POA&M-076 and CVE-2024-6387?")
    assert len(scans) == 1


def test_10_control_list_is_read_once(monkeypatch):
    real, loads = objectives.load, []
    monkeypatch.setattr(objectives, "load", lambda *a: loads.append(1) or real(*a))
    identifiers._known_controls.cache_clear()
    identifiers.find("3.5.6 and 3.1.1")
    identifiers.find("3.13.8")
    assert len(loads) == 1
