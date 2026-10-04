"""Chroma collection, LM Studio embed/chat calls, chunking and retrieval.

Settings are read from `config` at call time (config.X, not `from config import X`)
so a profile switch or a test override takes effect everywhere.
"""
import json
import re

import chromadb
import requests
from chromadb.config import Settings

import config

EMBED_TIMEOUT = 120
CHAT_TIMEOUT = 600


def get_collection():
    client = chromadb.PersistentClient(
        path=config.DB_PATH, settings=Settings(anonymized_telemetry=False)
    )
    return client.get_or_create_collection(
        name=config.COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
    )


def embed_texts(texts):
    resp = requests.post(
        f"{config.LMSTUDIO_BASE_URL}/v1/embeddings",
        json={"model": config.EMBED_MODEL, "input": list(texts)},
        timeout=EMBED_TIMEOUT,
    )
    resp.raise_for_status()
    data = sorted(resp.json()["data"], key=lambda d: d["index"])
    return [d["embedding"] for d in data]


def embed_documents(texts):
    return embed_texts([config.DOC_PREFIX + t for t in texts])


def embed_query(text):
    return embed_texts([config.QUERY_PREFIX + text])[0]


def chunk_text(text, size=None, overlap=None):
    size = size or config.CHUNK_SIZE
    overlap = config.CHUNK_OVERLAP if overlap is None else overlap
    text = re.sub(r"\n{3,}", "\n\n", text)
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        if end < len(text):
            window = text[start:end]
            cut = window.rfind("\n\n")
            if cut <= overlap:
                cut = max(window.rfind(". "), window.rfind(".\n"))
                cut = cut + 1 if cut > overlap else -1  # keep the full stop
            if cut > overlap:
                end = start + cut
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        start = max(end - overlap, start + 1)
    return chunks


def retrieve(question, top_k=None):
    top_k = top_k or config.TOP_K
    col = get_collection()
    count = col.count()
    if count == 0:
        return []
    res = col.query(
        query_embeddings=[embed_query(question)],
        n_results=min(top_k, count),
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    for chunk_id, text, meta, dist in zip(
        res["ids"][0], res["documents"][0], res["metadatas"][0], res["distances"][0]
    ):
        relevance = 1 - dist
        if relevance < config.RELEVANCE_THRESHOLD:
            continue
        meta = meta or {}
        hits.append({
            "id": chunk_id,
            "text": text,
            "source": meta.get("source", "unknown"),
            "relevance": relevance,
            "metadata": meta,
        })
    return hits


def get_llm_model():
    """config.LLM_MODEL if set; else a preferred model if downloaded; else the
    chat model LM Studio has loaded; else the first downloaded one (LM Studio
    loads it on demand). Barred models are never chosen."""
    if config.LLM_MODEL:
        return config.LLM_MODEL
    resp = requests.get(f"{config.LMSTUDIO_BASE_URL}/api/v0/models", timeout=10)
    resp.raise_for_status()
    usable = [
        m for m in resp.json()["data"]
        if m.get("type") in ("llm", "vlm")
        and not any(b in m["id"] for b in config.BARRED_MODELS)
    ]
    for pref in config.PREFERRED_MODELS:
        for m in usable:
            if pref in m["id"]:
                return m["id"]
    loaded = [m for m in usable if m.get("state") == "loaded"]
    if loaded or usable:
        return (loaded or usable)[0]["id"]
    raise RuntimeError(
        "No usable chat model in LM Studio. Download one (for example Devstral) "
        "or set LLM_MODEL in config.py."
    )


def _empty_answer_message(finish_reason):
    if finish_reason == "length":
        return (
            f"[No answer: the model reached its token limit ({config.LLM_MAX_TOKENS}) "
            "before writing any answer, probably while reasoning. Ask a narrower "
            "question or raise LLM_MAX_TOKENS.]"
        )
    return f"[The model returned an empty answer (finish_reason={finish_reason}).]"


def ask_llm(prompt, stream=False, system=None):
    """Non-streaming: return the answer text (callers must print it).
    Streaming: return a generator of text pieces."""
    payload = {
        "model": get_llm_model(),
        "messages": [
            {"role": "system", "content": system or config.RAG_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": config.LLM_TEMPERATURE,
        "max_tokens": config.LLM_MAX_TOKENS,
        "stream": stream,
    }
    url = f"{config.LMSTUDIO_BASE_URL}/v1/chat/completions"
    if stream:
        return _stream(url, payload)
    resp = requests.post(url, json=payload, timeout=CHAT_TIMEOUT)
    resp.raise_for_status()
    choice = resp.json()["choices"][0]
    content = (choice.get("message") or {}).get("content") or ""
    if not content.strip():
        return _empty_answer_message(choice.get("finish_reason"))
    return content


def _stream(url, payload):
    resp = requests.post(url, json=payload, timeout=CHAT_TIMEOUT, stream=True)
    resp.raise_for_status()
    produced = False
    finish = None
    for line in resp.iter_lines(decode_unicode=True):
        if not line or not line.startswith("data:"):
            continue
        data = line[len("data:"):].strip()
        if data == "[DONE]":
            break
        choice = json.loads(data)["choices"][0]
        finish = choice.get("finish_reason") or finish
        piece = (choice.get("delta") or {}).get("content")
        if piece:
            produced = True
            yield piece
    if not produced:
        yield _empty_answer_message(finish)
