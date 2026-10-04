"""Exact identifier lookup (the spec's clause lookup, generalised).

Meaning-based search is poor at exact identifiers: it hands back a
neighbouring control or CVE. Questions that name an identifier get that
identifier's own file and its exact mentions first, then the semantic hits.

Sysadmin identifiers: CVE-YYYY-N, RLSA-YYYY:N, NIST SP 800-171 controls and
objectives (3.x.y, 3.x.y[z]; only the 110 real controls), DIWAI document IDs,
POA&M items, RB-xx runbooks, systemd unit names.
"""
import functools
import os
import re

import ingest
import objectives
import rag_utils

MAX_IDS = 4
EXACT_BUDGET = 8          # exact chunks shared by all identifiers in a question
CONTAINS_LIMIT = 1000     # common identifiers are cited hundreds of times
TOC_HEADING_LINES = 5

_UNIT_SUFFIXES = "service|timer|socket|target|path|mount"
PATTERNS = [
    (re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.I), str.upper),
    (re.compile(r"\bRL[SBE]A-\d{4}:\d+\b", re.I), str.upper),
    (re.compile(r"(?<![\w.])3\.(?:1[0-4]|[1-9])\.\d{1,2}(?:\[[a-z]\])?(?!\d)(?!\.\d)"), None),
    (re.compile(r"\bDIWAI-[A-Z]+(?:-[A-Z0-9]+)*\b"), None),
    (re.compile(r"\bPOA&M-\d{3}\b"), None),
    (re.compile(r"\bRB-\d{2}\b"), None),
    (re.compile(rf"(?<![\w@.:-])[A-Za-z0-9][\w@.:-]*\.(?:{_UNIT_SUFFIXES})\b"), None),
]
_CONTROL_RE = re.compile(r"3\.\d{1,2}\.\d{1,2}")
_HEADING_RE = re.compile(r"^\s*(#+\s|\d+(\.\d+)+\s|[A-Z][\w&]*-\d+\s)")


@functools.lru_cache(maxsize=1)
def _known_controls():
    return set(objectives.load()["requirements"])


def find(text):
    """Identifiers in TEXT, in order of appearance, without repeats."""
    controls = _known_controls()
    found = []
    for regex, norm in PATTERNS:
        for m in regex.finditer(text):
            value = norm(m.group(0)) if norm else m.group(0)
            if _CONTROL_RE.fullmatch(value.split("[")[0]) and value.split("[")[0] not in controls:
                continue
            found.append((m.start(), value))
    out = []
    for _, value in sorted(found):
        if value not in out:
            out.append(value)
    return out


def _hit(chunk_id, text, meta):
    return {"id": chunk_id, "text": text, "source": meta.get("source", "unknown"),
            "relevance": 1.0, "metadata": meta, "exact": True}


def _owns(source, ident):
    stem = os.path.splitext(source)[0].lower()
    ident = ident.lower()
    return stem == ident or any(stem.startswith(ident + sep) for sep in "_- .")


def _rank(text, ident):
    lines = text.splitlines()
    if sum(1 for l in lines if _HEADING_RE.match(l)) > TOC_HEADING_LINES:
        return 1  # table of contents
    for line in lines:
        body = line.strip().lstrip("#*>- ").strip()
        if body.startswith(ident) and re.match(r"[\s:.]+\S", body[len(ident):] or ""):
            return 0  # a line that starts with the identifier and a title
    return 2  # a mere citation


def exact_hits(ident, collection, limit, docs=None):
    """DOCS is the library listing; pass it in so a question naming several
    identifiers scans the library once, not once per identifier (finding 10)."""
    if docs is None:
        docs = ingest.list_documents(collection)
    own_ids = [d["doc_id"] for d in docs if _owns(d["source"], ident)]
    hits, seen = [], set()
    if own_ids:
        got = collection.get(where={"doc_id": {"$in": own_ids}},
                             include=["documents", "metadatas"])
        own = sorted(zip(got["ids"], got["documents"], got["metadatas"]),
                     key=lambda r: (own_ids.index(r[2]["doc_id"]), r[2].get("chunk_index", 0)))
        for cid, text, meta in own:
            hits.append(_hit(cid, text, meta))
            seen.add(cid)
    got = collection.get(where_document={"$contains": ident}, limit=CONTAINS_LIMIT,
                         include=["documents", "metadatas"])
    rest = [(cid, text, meta) for cid, text, meta in
            zip(got["ids"], got["documents"], got["metadatas"]) if cid not in seen]
    rest.sort(key=lambda r: (_rank(r[1], ident), r[2].get("source", ""),
                             r[2].get("chunk_index", 0)))
    hits += [_hit(*r) for r in rest]
    return hits[:limit]


def retrieve_with_ids(question, top_k=None):
    """Exact identifier hits (relevance 1.0) first, then semantic hits,
    de-duplicated, up to max(top_k, exact + 3). A question with no
    identifier behaves exactly like rag_utils.retrieve()."""
    import config
    top_k = top_k or config.TOP_K
    idents = find(question)[:MAX_IDS]
    if not idents:
        return rag_utils.retrieve(question, top_k)
    col = rag_utils.get_collection()
    docs = ingest.list_documents(col)
    per = max(1, EXACT_BUDGET // len(idents))
    exact, seen = [], set()
    for ident in idents:
        for h in exact_hits(ident, col, per, docs):
            if h["id"] not in seen:
                seen.add(h["id"])
                exact.append(h)
    limit = max(top_k, len(exact) + 3)
    semantic = [h for h in rag_utils.retrieve(question, limit + len(exact)) if h["id"] not in seen]
    return (exact + semantic)[:limit]
