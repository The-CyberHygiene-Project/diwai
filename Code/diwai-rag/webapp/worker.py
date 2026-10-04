"""The single background worker: every library write (add or remove) happens
here, one job at a time. Page requests never write to Chroma."""
import hashlib
import os
import queue
import threading
import time

import ingest
from webapp import library

EMBED_ATTEMPTS = 3  # a model still loading, or one 5xx, is not the file's fault
LIBRARY_ERROR = ("❌ The library could not be opened. "
                 "Ask the administrator to run the repair tool.")


class Worker(threading.Thread):
    def __init__(self, collection, documents_dir, log, index, ready, retry_seconds):
        super().__init__(name="library-worker", daemon=True)
        self.col = collection
        self.docs = documents_dir
        self.log = log
        self.index = index
        self.ready = ready
        self.retry = retry_seconds
        self.jobs = queue.Queue()
        self._stopping = threading.Event()
        self._hashes = {}  # path -> (size, mtime, sha256)
        self._incoming = self._new_dest = None  # files the current job created

    # ---- control --------------------------------------------------------

    def submit(self, job_id):
        self.jobs.put(job_id)

    def stop(self):
        """Stop taking jobs; a job already running finishes first."""
        self._stopping.set()
        if self.is_alive():
            self.join()

    def _build_index(self):
        """Naming depends on the index: no job runs before it exists. A store
        that cannot be read is reported, never left to hang (finding 2)."""
        try:
            self.index.build(self.col)
        except Exception as exc:
            self.index.error = f"{type(exc).__name__}: {exc}"
        return self.index.ready

    def run(self):
        self._build_index()
        while not self._stopping.is_set():
            try:
                job_id = self.jobs.get(timeout=0.05)
            except queue.Empty:
                continue
            job = self.log.get(job_id)
            self._incoming = job["payload"] if job["kind"] == "add" else None
            self._new_dest = None
            try:
                if not self.index.ready and not self._build_index():
                    self._discard_new_files()
                    self._done(job, "library_error", LIBRARY_ERROR, self.index.error)
                elif job["kind"] == "add":
                    self._add(job)
                else:
                    self._remove(job)
            except Exception as exc:  # never let one job kill the worker
                self._discard_new_files()
                self._done(job, "unreadable", "❌ Couldn't read", f"{type(exc).__name__}: {exc}")

    def _discard_new_files(self):
        """Remove what this job created and the library does not use (finding 9).
        A stored copy that predates the job is never touched."""
        if self._incoming and os.path.exists(self._incoming):
            os.remove(self._incoming)
        dest = self._new_dest
        if dest and os.path.exists(dest) and not self.col.get(
                where={"doc_id": ingest.doc_id_for(dest)}, limit=1)["ids"]:
            os.remove(dest)
            self._hashes.pop(dest, None)

    # ---- helpers --------------------------------------------------------

    def _done(self, job, outcome, message, detail=""):
        self.log.update(job["id"], state="done", outcome=outcome, message=message,
                        detail=detail, progress=100 if outcome in ("added", "restored") else 0)

    def _wait_ready(self, job):
        """Block while LM Studio is down. False if the worker is stopping."""
        while not self.ready():
            self.log.update(job["id"], state="waiting", outcome="paused",
                            message="⏸️ Paused (LM Studio not running)")
            if self._stopping.wait(self.retry):
                return False
        self.log.update(job["id"], state="working", outcome="working", message="⏳ Working")
        return True

    def _stored_files(self):
        for root, dirs, files in os.walk(self.docs):
            dirs[:] = [d for d in dirs if d != ".incoming"]
            for f in files:
                yield os.path.join(root, f)

    def _sha(self, path):
        st = os.stat(path)
        cached = self._hashes.get(path)
        if cached and cached[:2] == (st.st_size, st.st_mtime):
            return cached[2]
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for block in iter(lambda: fh.read(1 << 20), b""):
                h.update(block)
        self._hashes[path] = (st.st_size, st.st_mtime, h.hexdigest())
        return h.hexdigest()

    def _identical_stored(self, sha, size):
        for path in self._stored_files():
            if os.path.getsize(path) == size and self._sha(path) == sha:
                return path
        return None

    def _taken(self):
        keys = self.index.source_keys()
        keys |= {library.apfs_key(os.path.basename(p)) for p in self._stored_files()}
        return keys

    def _ingest(self, job, path):
        """Ingest PATH, pausing (never failing) while LM Studio is down."""
        def progress(done, total):
            self.log.update(job["id"], progress=int(100 * done / max(total, 1)),
                            message=f"⏳ Working {int(100 * done / max(total, 1))}%")
        attempts = 0
        while True:
            if not self._wait_ready(job):
                return None
            result = ingest.ingest_file(path, self.col, progress=progress)
            if result.status == "error" and not self.ready():
                continue  # the embedder went away mid-job: wait and retry
            if result.stage == "embed":
                attempts += 1
                if attempts < EMBED_ATTEMPTS:  # finding 3: retry, don't blame the file
                    if self._stopping.wait(self.retry):
                        return None
                    continue
            self.index.refresh_doc(self.col, ingest.doc_id_for(path))
            return result

    # ---- jobs -----------------------------------------------------------

    def _add(self, job):
        incoming = job["payload"]
        self.log.update(job["id"], state="working", outcome="working", message="⏳ Working")
        sha = self._sha(incoming)
        match = self._identical_stored(sha, os.path.getsize(incoming))
        if match:
            doc = self.index.by_path(match)
            if doc:
                os.remove(incoming)
                return self._done(job, "skipped", f"⏭️ Already in library as {doc['source']}")
            result = self._ingest(job, match)  # removed earlier: restore the stored copy
            if result is None:
                return self._discard_new_files()
            os.remove(incoming)
            if result.status == "ingested":
                return self._done(job, "restored", f"✅ Restored {result.source}",
                                  f"{result.chunks} chunks")
            return self._finish_failed(job, result, None)

        name = library.choose_name(library.safe_name(job["filename"]), self._taken())
        folder = os.path.join(self.docs, time.strftime("%Y-%m"))
        os.makedirs(folder, exist_ok=True)
        dest = os.path.join(folder, name)
        if os.path.exists(dest):  # never overwrite
            os.remove(incoming)
            return self._done(job, "refused", "❌ Can't add (name already in use)", dest)
        os.rename(incoming, dest)
        self._hashes.pop(incoming, None)
        self._incoming, self._new_dest = None, dest
        result = self._ingest(job, dest)
        if result is None:  # stopping: the job is marked interrupted at next start
            return self._discard_new_files()
        if result.status == "ingested":
            return self._done(job, "added", f"✅ Added {name}", f"{result.chunks} chunks")
        return self._finish_failed(job, result, dest)

    def _finish_failed(self, job, result, dest):
        if dest and os.path.exists(dest):  # documents/ holds only what the library uses
            os.remove(dest)
            self._hashes.pop(dest, None)
        if result.status == "skipped_duplicate":
            return self._done(job, "skipped", f"⏭️ Already in library (same text as {result.duplicate_of})")
        if result.status == "empty":
            return self._done(job, "no_text", f"❌ {result.detail}")
        if result.stage == "embed":
            return self._done(job, "embed_failed", "❌ Couldn't add: LM Studio did not answer. "
                              "Drop the file again later.", result.detail)
        return self._done(job, "unreadable", "❌ Couldn't read", result.detail)

    def _remove(self, job):
        doc_id = job["payload"]
        self.log.update(job["id"], state="working", outcome="working", message="⏳ Working")
        if not self.col.get(where={"doc_id": doc_id}, limit=1)["ids"]:
            self.index.refresh_doc(self.col, doc_id)
            return self._done(job, "not_found", "❌ Not found (already removed?)")
        self.col.delete(where={"doc_id": doc_id})
        self.index.refresh_doc(self.col, doc_id)
        self._done(job, "removed", f"🗑️ Removed {job['filename']}",
                   "The stored copy is kept; dropping the file again restores it.")
