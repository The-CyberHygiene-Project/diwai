import pytest

import config
import rag_utils
from conftest import fake_vector


class FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        pass

    def json(self):
        return self._payload


# ---- chunking -------------------------------------------------------------

def test_short_text_is_one_chunk():
    assert rag_utils.chunk_text("hello world") == ["hello world"]


def test_empty_and_whitespace_give_no_chunks():
    assert rag_utils.chunk_text("") == []
    assert rag_utils.chunk_text(" \n\n\n  ") == []


def test_three_or_more_newlines_collapse_to_two():
    assert rag_utils.chunk_text("a\n\n\n\n\nb") == ["a\n\nb"]


def test_chunks_respect_size_and_overlap():
    text = " ".join(f"word{i}" for i in range(2000))
    chunks = rag_utils.chunk_text(text)
    assert len(chunks) > 1
    assert all(len(c) <= config.CHUNK_SIZE for c in chunks)
    # consecutive chunks overlap
    assert chunks[0][-50:] in chunks[0] and chunks[0][-100:].split()[-1] in chunks[1]


def test_prefers_paragraph_break():
    para1 = "A" * 1000
    para2 = "B" * 1000
    chunks = rag_utils.chunk_text(para1 + "\n\n" + para2)
    assert chunks[0] == para1


def test_falls_back_to_sentence_break():
    first = ("x" * 99 + ". ") * 9  # sentence ends well past the overlap
    chunks = rag_utils.chunk_text(first + "y" * 2000)
    assert chunks[0].endswith(".")


def test_break_inside_overlap_is_ignored():
    # the only paragraph break is 100 chars in (< overlap 250): hard cut instead
    text = "a" * 100 + "\n\n" + "b" * 3000
    chunks = rag_utils.chunk_text(text)
    assert len(chunks[0]) == config.CHUNK_SIZE


def test_all_text_is_covered():
    text = " ".join(f"w{i}" for i in range(3000))
    joined = " ".join(rag_utils.chunk_text(text))
    for token in ("w0", "w1500", "w2999"):
        assert token in joined.split()


# ---- embedding ------------------------------------------------------------

def test_embed_texts_sorts_by_index(monkeypatch):
    calls = {}

    def fake_post(url, json, timeout):
        calls["url"], calls["json"] = url, json
        return FakeResponse({"data": [
            {"index": 1, "embedding": [1.0]},
            {"index": 0, "embedding": [0.0]},
        ]})

    monkeypatch.setattr(rag_utils.requests, "post", fake_post)
    assert rag_utils.embed_texts(["a", "b"]) == [[0.0], [1.0]]
    assert calls["url"] == "http://127.0.0.1:1234/v1/embeddings"
    assert calls["json"]["model"] == config.EMBED_MODEL
    assert calls["json"]["input"] == ["a", "b"]


# ---- collection and retrieval ---------------------------------------------

def test_collection_is_cosine_and_persistent(temp_store):
    col = rag_utils.get_collection()
    assert col.name == "test_collection"
    assert col.metadata.get("hnsw:space") == "cosine"
    assert (temp_store / "chroma_db").exists()


def test_retrieve_returns_source_and_relevance(temp_store):
    col = rag_utils.get_collection()
    col.add(ids=["1"], documents=["chrony makestep"],
            embeddings=[fake_vector("chrony makestep")],
            metadatas=[{"source": "/docs/chrony.md"}])
    hits = rag_utils.retrieve("chrony makestep")
    assert hits[0]["source"] == "/docs/chrony.md"
    assert hits[0]["text"] == "chrony makestep"
    assert hits[0]["relevance"] == pytest.approx(1.0, abs=1e-4)


def test_retrieve_drops_hits_below_threshold(temp_store, monkeypatch):
    col = rag_utils.get_collection()
    col.add(ids=["1"], documents=["unrelated"],
            embeddings=[fake_vector("unrelated")],
            metadatas=[{"source": "/docs/x.md"}])
    monkeypatch.setattr(config, "RELEVANCE_THRESHOLD", 1.01)
    assert rag_utils.retrieve("unrelated") == []


def test_retrieve_on_empty_library_is_empty(temp_store):
    assert rag_utils.retrieve("anything") == []


# ---- model auto-detection -------------------------------------------------

V0_MODELS = {"data": [
    {"id": "openai/gpt-oss-20b", "type": "llm", "state": "loaded"},
    {"id": "text-embedding-nomic-embed-text-v1.5@f16", "type": "embeddings", "state": "loaded"},
    {"id": "other/not-loaded", "type": "llm", "state": "not-loaded"},
    {"id": "mistralai/devstral-small-2-2512", "type": "vlm", "state": "loaded"},
]}


def test_configured_model_wins(monkeypatch):
    monkeypatch.setattr(config, "LLM_MODEL", "x/y")
    assert rag_utils.get_llm_model() == "x/y"


def test_autodetect_picks_loaded_chat_model_skipping_barred(monkeypatch):
    monkeypatch.setattr(rag_utils.requests, "get",
                        lambda url, timeout: FakeResponse(V0_MODELS))
    assert rag_utils.get_llm_model() == "mistralai/devstral-small-2-2512"


def test_autodetect_with_nothing_loaded_uses_a_downloaded_chat_model(monkeypatch):
    # LM Studio's JIT eviction unloads the chat model whenever the embedder loads
    # (observed 2026-10-03), so "nothing loaded" is the normal state after a search.
    models = {"data": [
        {"id": "openai/gpt-oss-20b", "type": "llm", "state": "not-loaded"},
        {"id": "text-embedding-nomic-embed-text-v1.5@f16", "type": "embeddings", "state": "loaded"},
        {"id": "mistralai/devstral-small-2-2512", "type": "vlm", "state": "not-loaded"},
    ]}
    monkeypatch.setattr(rag_utils.requests, "get",
                        lambda url, timeout: FakeResponse(models))
    assert rag_utils.get_llm_model() == "mistralai/devstral-small-2-2512"


def test_autodetect_with_no_usable_chat_model_says_so(monkeypatch):
    models = {"data": [
        {"id": "openai/gpt-oss-20b", "type": "llm", "state": "loaded"},
        {"id": "text-embedding-nomic-embed-text-v1.5@f16", "type": "embeddings", "state": "loaded"},
    ]}
    monkeypatch.setattr(rag_utils.requests, "get",
                        lambda url, timeout: FakeResponse(models))
    with pytest.raises(RuntimeError, match="No usable chat model"):
        rag_utils.get_llm_model()


# ---- ask_llm --------------------------------------------------------------

def _chat(content, finish):
    return FakeResponse({"choices": [{
        "message": {"content": content, "reasoning_content": "thinking..."},
        "finish_reason": finish}]})


def test_ask_llm_returns_text_when_not_streaming(monkeypatch):
    monkeypatch.setattr(config, "LLM_MODEL", "m")
    sent = {}

    def fake_post(url, json, timeout):
        sent.update(json)
        return _chat("The answer.", "stop")

    monkeypatch.setattr(rag_utils.requests, "post", fake_post)
    assert rag_utils.ask_llm("q", stream=False) == "The answer."
    assert sent["messages"][0] == {"role": "system", "content": config.RAG_SYSTEM_PROMPT}
    assert sent["temperature"] == config.LLM_TEMPERATURE
    assert sent["max_tokens"] == config.LLM_MAX_TOKENS


def test_ask_llm_empty_content_at_length_limit_is_explained(monkeypatch):
    monkeypatch.setattr(config, "LLM_MODEL", "m")
    monkeypatch.setattr(rag_utils.requests, "post",
                        lambda url, json, timeout: _chat("", "length"))
    answer = rag_utils.ask_llm("q", stream=False)
    assert answer.strip()
    assert "token limit" in answer


def test_ask_llm_empty_content_otherwise_is_explained(monkeypatch):
    monkeypatch.setattr(config, "LLM_MODEL", "m")
    monkeypatch.setattr(rag_utils.requests, "post",
                        lambda url, json, timeout: _chat(None, "stop"))
    assert "empty answer" in rag_utils.ask_llm("q", stream=False)


class FakeStream:
    def __init__(self, lines):
        self.lines = lines

    def raise_for_status(self):
        pass

    def iter_lines(self, decode_unicode=True):
        return iter(self.lines)


def test_ask_llm_streaming_yields_text(monkeypatch):
    monkeypatch.setattr(config, "LLM_MODEL", "m")
    lines = [
        'data: {"choices":[{"delta":{"content":"Hel"},"finish_reason":null}]}',
        "",
        'data: {"choices":[{"delta":{"content":"lo"},"finish_reason":"stop"}]}',
        "data: [DONE]",
    ]
    monkeypatch.setattr(rag_utils.requests, "post",
                        lambda url, json, timeout, stream: FakeStream(lines))
    assert "".join(rag_utils.ask_llm("q", stream=True)) == "Hello"


def test_ask_llm_streaming_empty_at_length_is_explained(monkeypatch):
    monkeypatch.setattr(config, "LLM_MODEL", "m")
    lines = [
        'data: {"choices":[{"delta":{"reasoning_content":"hmm"},"finish_reason":null}]}',
        'data: {"choices":[{"delta":{},"finish_reason":"length"}]}',
        "data: [DONE]",
    ]
    monkeypatch.setattr(rag_utils.requests, "post",
                        lambda url, json, timeout, stream: FakeStream(lines))
    assert "token limit" in "".join(rag_utils.ask_llm("q", stream=True))


# ---- nomic task labels (owner approved 2026-10-03) ------------------------

def test_task_labels_are_configured():
    assert config.DOC_PREFIX == "search_document: "
    assert config.QUERY_PREFIX == "search_query: "


def test_embed_documents_labels_each_text(temp_store, embed_calls):
    rag_utils.embed_documents(["a", "b"])
    assert embed_calls == ["search_document: a", "search_document: b"]


def test_retrieve_labels_the_question(temp_store, embed_calls):
    rag_utils.retrieve("how do I step the clock?")
    rag_utils.get_collection().add(ids=["1"], documents=["x"],
                                   embeddings=[fake_vector("x")],
                                   metadatas=[{"source": "s"}])
    rag_utils.retrieve("how do I step the clock?")
    assert embed_calls == ["search_query: how do I step the clock?"]


# ---- Devstral is the preferred model (owner, 2026-10-03) -------------------

def test_devstral_is_preferred():
    assert config.PREFERRED_MODELS == ("devstral",)


def test_preferred_model_wins_over_another_loaded_model(monkeypatch):
    models = {"data": [
        {"id": "google/gemma-4-e4b", "type": "vlm", "state": "loaded"},
        {"id": "mistralai/devstral-small-2-2512", "type": "vlm", "state": "not-loaded"},
    ]}
    monkeypatch.setattr(rag_utils.requests, "get", lambda url, timeout: FakeResponse(models))
    assert rag_utils.get_llm_model() == "mistralai/devstral-small-2-2512"


def test_falls_back_when_preferred_model_is_absent(monkeypatch):
    models = {"data": [
        {"id": "openai/gpt-oss-20b", "type": "llm", "state": "loaded"},
        {"id": "google/gemma-4-e4b", "type": "vlm", "state": "not-loaded"},
    ]}
    monkeypatch.setattr(rag_utils.requests, "get", lambda url, timeout: FakeResponse(models))
    assert rag_utils.get_llm_model() == "google/gemma-4-e4b"
