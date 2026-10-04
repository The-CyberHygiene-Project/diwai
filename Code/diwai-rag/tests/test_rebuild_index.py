import hashlib
import os
import shutil

import pytest

import config
import ingest
import rag_utils
import rebuild_index


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


@pytest.fixture
def src(temp_store):
    col = rag_utils.get_collection()
    for i in range(3):
        ingest.ingest_file(str(write(temp_store / "docs" / f"d{i}.md",
                                     " ".join(f"doc{i}word{n}" for n in range(600)))), col)
    col.upsert(ids=["typed::chunk::0"], documents=["typed values"],
               embeddings=[rag_utils.embed_texts(["typed values"])[0]],
               metadatas=[{"source": "typed.md", "doc_id": "typed", "chunk_index": 0,
                           "flag": True, "off": False, "score": 0.5}])
    return col


def as_map(got):
    return {i: (d, m) for i, d, m in zip(got["ids"], got["documents"], got["metadatas"])}


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def test_reads_every_chunk_with_typed_metadata_straight_from_sqlite(src):
    rows = list(rebuild_index.read_chunks(config.DB_PATH, config.COLLECTION_NAME))
    got = {r["id"]: (r["document"], r["metadata"]) for r in rows}
    assert got == as_map(src.get(include=["documents", "metadatas"]))
    typed = got["typed::chunk::0"][1]
    assert typed["flag"] is True and typed["off"] is False
    assert typed["score"] == 0.5 and typed["chunk_index"] == 0


def test_rebuild_works_after_the_vector_index_is_lost(src, temp_store):
    expected = as_map(src.get(include=["documents", "metadatas"]))
    for entry in os.listdir(config.DB_PATH):  # the HNSW segment folders
        p = os.path.join(config.DB_PATH, entry)
        if os.path.isdir(p):
            shutil.rmtree(p)
    dest = str(temp_store / "rebuilt")
    result = rebuild_index.rebuild(config.DB_PATH, dest, config.COLLECTION_NAME)
    assert result == {"read": len(expected), "written": len(expected), "skipped": 0}
    import chromadb
    from chromadb.config import Settings
    new = chromadb.PersistentClient(path=dest, settings=Settings(anonymized_telemetry=False)) \
        .get_collection(config.COLLECTION_NAME)
    assert as_map(new.get(include=["documents", "metadatas"])) == expected
    assert new.metadata.get("hnsw:space") == "cosine"
    assert new.query(query_embeddings=[rag_utils.embed_texts(["typed values"])[0]],
                     n_results=1)["ids"][0] == ["typed::chunk::0"]


def test_rebuild_embeds_with_the_document_label(src, temp_store, embed_calls):
    embed_calls.clear()
    rebuild_index.rebuild(config.DB_PATH, str(temp_store / "rebuilt"), config.COLLECTION_NAME)
    assert embed_calls and all(t.startswith("search_document: ") for t in embed_calls)


def test_rebuild_is_resumable_and_skips_ids_already_written(src, temp_store, monkeypatch, embed_calls):
    total = src.count()
    dest = str(temp_store / "rebuilt")
    real = rag_utils.embed_texts
    calls = {"n": 0}

    def crash_on_second_flush(texts):
        calls["n"] += 1
        if calls["n"] > 1:
            raise ConnectionError("power cut")
        return real(texts)

    monkeypatch.setattr(rebuild_index, "FLUSH_EVERY", 2)
    monkeypatch.setattr(config, "EMBED_BATCH", 2)
    monkeypatch.setattr(rag_utils, "embed_texts", crash_on_second_flush)
    with pytest.raises(ConnectionError):
        rebuild_index.rebuild(config.DB_PATH, dest, config.COLLECTION_NAME)
    monkeypatch.setattr(rag_utils, "embed_texts", real)
    embed_calls.clear()
    result = rebuild_index.rebuild(config.DB_PATH, dest, config.COLLECTION_NAME)
    assert result == {"read": total, "written": total - 2, "skipped": 2}
    assert len(embed_calls) == total - 2


def test_source_is_never_modified(src, temp_store):
    before = sha(os.path.join(config.DB_PATH, "chroma.sqlite3"))
    rebuild_index.rebuild(config.DB_PATH, str(temp_store / "rebuilt"), config.COLLECTION_NAME)
    assert sha(os.path.join(config.DB_PATH, "chroma.sqlite3")) == before


def test_refuses_to_write_over_the_source(src):
    with pytest.raises(ValueError, match="source"):
        rebuild_index.rebuild(config.DB_PATH, config.DB_PATH, config.COLLECTION_NAME)
    with pytest.raises(ValueError, match="source"):
        rebuild_index.rebuild(config.DB_PATH, os.path.join(config.DB_PATH, "inside"),
                              config.COLLECTION_NAME)


def test_unknown_collection_is_reported(src, temp_store):
    with pytest.raises(ValueError, match="nosuch"):
        list(rebuild_index.read_chunks(config.DB_PATH, "nosuch"))


def test_cli_defaults_to_the_profile_store_and_a_rebuild_folder(src, capsys):
    assert rebuild_index.main([]) == 0
    out = capsys.readouterr().out
    assert config.DB_PATH + "_rebuild" in out and "swap" in out.lower()
