"""Naming, filtering and the in-memory document index for the browser manager."""
import os
import re
import threading
import unicodedata

import config
import ingest

MAX_NAME_BYTES = 255  # APFS file-name limit
_CONTROL = re.compile(r"[\x00-\x1f\x7f]")


def apfs_key(name):
    """Compare names the way APFS does: case-insensitive, Unicode NFC."""
    return unicodedata.normalize("NFC", name).casefold()


def safe_name(uploaded):
    """Strip directory parts and control characters from an uploaded name."""
    name = _CONTROL.sub("", uploaded or "")
    name = name.replace("\\", "/").rsplit("/", 1)[-1].strip()
    if name in ("", ".", ".."):
        return "unnamed"
    return unicodedata.normalize("NFC", name)


def supported(name):
    return os.path.splitext(name)[1].lower() in ingest.SUPPORTED


def _fit(stem, suffix, ext):
    """Trim STEM so stem+suffix+ext fits the file-name limit in UTF-8."""
    room = MAX_NAME_BYTES - len((suffix + ext).encode("utf-8"))
    raw = stem.encode("utf-8")[:room]
    return raw.decode("utf-8", errors="ignore") + suffix + ext


def choose_name(name, taken_keys):
    """NAME, or 'stem (2).ext', '(3)' … until its APFS key is not taken."""
    stem, ext = os.path.splitext(name)
    candidate = _fit(stem, "", ext)
    n = 2
    while apfs_key(candidate) in taken_keys:
        candidate = _fit(stem, f" ({n})", ext)
        n += 1
    return candidate


def filter_rows(rows, query):
    """Case-insensitive LITERAL substring match on the document name."""
    q = (query or "").casefold()
    return [r for r in rows if q in r["source"].casefold()]


class DocIndex:
    """doc_id -> {doc_id, source, chunks, file_path, added_at}; built once by
    paging the collection, then updated by the worker after each job."""

    def __init__(self):
        self.docs = {}
        self.ready = False
        self.error = ""  # set when the store cannot be read (finding 2)
        # The worker writes while page requests read (finding 5).
        self._lock = threading.Lock()

    def build(self, collection):
        docs = {d["doc_id"]: d for d in ingest.list_documents(collection)}
        with self._lock:
            self.docs = docs
            self.ready, self.error = True, ""

    def refresh_doc(self, collection, doc_id):
        got = collection.get(where={"doc_id": doc_id}, include=["metadatas"])
        with self._lock:
            if not got["ids"]:
                self.docs.pop(doc_id, None)
                return
            m = got["metadatas"][0]
            self.docs[doc_id] = {"doc_id": doc_id, "source": m.get("source", "?"),
                                 "file_path": m.get("file_path", ""),
                                 "added_at": m.get("added_at", ""), "chunks": len(got["ids"])}

    def get(self, doc_id):
        with self._lock:
            return self.docs.get(doc_id)

    def _values(self):
        with self._lock:
            return list(self.docs.values())

    def source_keys(self):
        return {apfs_key(d["source"]) for d in self._values()}

    def by_path(self, path):
        real = os.path.realpath(path)
        return next((d for d in self._values() if d["file_path"] == real), None)

    def rows(self):
        return sorted(self._values(), key=lambda d: d["source"].casefold())

    def totals(self):
        values = self._values()
        return len(values), sum(d["chunks"] for d in values)
