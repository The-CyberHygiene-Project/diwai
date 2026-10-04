import hashlib
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config  # noqa: E402
import rag_utils  # noqa: E402

DIM = 64


def fake_vector(text):
    """Deterministic hash-derived unit vector (spec §5 fake embedder)."""
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    raw = [(digest[i % len(digest)] - 127.5) for i in range(DIM)]
    norm = math.sqrt(sum(x * x for x in raw))
    return [x / norm for x in raw]


def strip_task_prefix(text):
    """The fake embedder ignores nomic task labels so a query can match its
    document; tests that care about the labels inspect embed_calls instead."""
    for prefix in ("search_document: ", "search_query: "):
        if text.startswith(prefix):
            return text[len(prefix):]
    return text


@pytest.fixture
def embed_calls():
    return []


@pytest.fixture
def temp_store(tmp_path, monkeypatch, embed_calls):
    """Real ChromaDB in a temp dir; only the LM Studio embedder is faked."""
    monkeypatch.setattr(config, "DB_PATH", str(tmp_path / "chroma_db"))
    monkeypatch.setattr(config, "DOCS_DIR", str(tmp_path / "documents"))
    monkeypatch.setattr(config, "COLLECTION_NAME", "test_collection")

    def fake_embed(texts):
        embed_calls.extend(texts)
        return [fake_vector(strip_task_prefix(t)) for t in texts]

    monkeypatch.setattr(rag_utils, "embed_texts", fake_embed)
    return tmp_path
