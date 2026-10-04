"""Recovery tool: rebuild the vector index from Chroma's SQLite file.

Chroma keeps vectors only in the HNSW segment folders, but chunk text and
metadata live in chroma.sqlite3. If the index folders are lost, every Chroma
call fails ("Error loading hnsw index"), yet the corpus survives. This reads
the chunks straight from sqlite (read-only, bypassing the Chroma API),
re-embeds them, and writes a FRESH store. Non-destructive and resumable: it
flushes every FLUSH_EVERY chunks and skips ids already written.

    rebuild_index.py [--source DIR] [--dest DIR]

Defaults: the profile's store and <store>_rebuild. Swap it in by hand after
checking it. Note: `pragma quick_check` reports "malformed inverted index for
FTS5" on healthy Chroma stores; that is a false alarm.
"""
import argparse
import os
import sqlite3
import sys
from pathlib import Path

import chromadb
from chromadb.config import Settings

import config
import rag_utils

FLUSH_EVERY = 5000
DOCUMENT_KEY = "chroma:document"


def _value(string_value, int_value, float_value, bool_value):
    if bool_value is not None:
        return bool(bool_value)
    if int_value is not None:
        return int_value
    if float_value is not None:
        return float_value
    return string_value


def read_chunks(db_dir, collection_name, page=FLUSH_EVERY):
    """Yield {id, document, metadata} for every chunk, from sqlite only."""
    uri = Path(db_dir, "chroma.sqlite3").resolve().as_uri() + "?mode=ro"
    db = sqlite3.connect(uri, uri=True)
    try:
        row = db.execute(
            "SELECT s.id FROM segments s JOIN collections c ON s.collection = c.id "
            "WHERE c.name = ? AND s.scope = 'METADATA'", (collection_name,)).fetchone()
        if row is None:
            raise ValueError(f"No collection named {collection_name!r} in {db_dir}")
        segment = row[0]
        last = 0
        while True:
            batch = db.execute(
                "SELECT id, embedding_id FROM embeddings WHERE segment_id = ? AND id > ? "
                "ORDER BY id LIMIT ?", (segment, last, page)).fetchall()
            if not batch:
                return
            ids = [r[0] for r in batch]
            marks = ",".join("?" * len(ids))
            meta = {i: {} for i in ids}
            for rid, key, s, n, f, b in db.execute(
                    f"SELECT id, key, string_value, int_value, float_value, bool_value "
                    f"FROM embedding_metadata WHERE id IN ({marks})", ids):
                meta[rid][key] = _value(s, n, f, b)
            for rid, chunk_id in batch:
                m = meta[rid]
                document = m.pop(DOCUMENT_KEY, None)
                yield {"id": chunk_id, "document": document, "metadata": m}
            last = ids[-1]
    finally:
        db.close()


def _existing_ids(col):
    ids, offset = set(), 0
    while True:
        got = col.get(include=[], limit=FLUSH_EVERY, offset=offset)
        if not got["ids"]:
            return ids
        ids.update(got["ids"])
        offset += len(got["ids"])


def _inside(path, parent):
    path, parent = os.path.realpath(path), os.path.realpath(parent)
    return path == parent or path.startswith(parent + os.sep)


def rebuild(source_dir, dest_dir, collection_name, progress=None):
    if _inside(dest_dir, source_dir):
        raise ValueError("The destination must not be the source store or inside it.")
    client = chromadb.PersistentClient(path=dest_dir, settings=Settings(anonymized_telemetry=False))
    col = client.get_or_create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})
    done = _existing_ids(col)
    counts = {"read": 0, "written": 0, "skipped": 0}
    page = []

    def flush():
        todo = [r for r in page if r["id"] not in done]
        counts["skipped"] += len(page) - len(todo)
        if todo:
            vectors = []
            for i in range(0, len(todo), config.EMBED_BATCH):
                vectors += rag_utils.embed_documents(
                    [r["document"] or "" for r in todo[i:i + config.EMBED_BATCH]])
            col.upsert(ids=[r["id"] for r in todo], documents=[r["document"] for r in todo],
                       metadatas=[r["metadata"] or None for r in todo], embeddings=vectors)
            done.update(r["id"] for r in todo)
            counts["written"] += len(todo)
        page.clear()
        if progress:
            progress(counts)

    for row in read_chunks(source_dir, collection_name):
        counts["read"] += 1
        page.append(row)
        if len(page) >= FLUSH_EVERY:
            flush()
    flush()
    return counts


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default=config.DB_PATH)
    ap.add_argument("--dest", default=config.DB_PATH + "_rebuild")
    args = ap.parse_args(argv)
    counts = rebuild(args.source, args.dest, config.COLLECTION_NAME,
                     progress=lambda c: print(f"  read {c['read']}, written {c['written']}, "
                                              f"already there {c['skipped']}", flush=True))
    print(f"Rebuilt {config.COLLECTION_NAME} into {args.dest}: {counts['read']} chunks read, "
          f"{counts['written']} written, {counts['skipped']} already there.")
    print("Nothing was changed in the source. To swap it in by hand: stop the browser manager "
          "and the MCP server, move the old store aside, move the rebuilt folder into its "
          f"place ({args.source}), then start them again.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
