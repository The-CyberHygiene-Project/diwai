import os

import pytest

import config


def test_default_profile_is_sysadmin():
    p = config.load_profile(None)
    assert p["name"] == "sysadmin"
    assert p["collection"] == "diwai_sysadmin"


def test_unknown_profile_is_refused():
    with pytest.raises(ValueError, match="nosuch"):
        config.load_profile("nosuch")


def test_profiles_do_not_share_store_collection_docs_or_ports():
    a = config.load_profile("sysadmin")
    b = config.load_profile("compliance")
    for key in ("db_path", "docs_dir", "collection", "web_port", "mcp_port"):
        assert a[key] != b[key], key


def test_paths_are_inside_the_project_folder():
    project = os.path.dirname(os.path.abspath(config.__file__))
    for name in config.PROFILES:
        p = config.load_profile(name)
        for key in ("db_path", "docs_dir"):
            assert os.path.commonpath([project, p[key]]) == project, (name, key)


def test_no_hardcoded_chat_model():
    assert config.LLM_MODEL == ""


def test_spec_tuning_values():
    assert (config.CHUNK_SIZE, config.CHUNK_OVERLAP) == (1400, 250)
    assert config.TOP_K == 8
    # Tuned on real content 2026-10-03 (evals/): answerable best hits 0.74-0.84,
    # unanswerable 0.56-0.63 with nomic task labels on.
    assert config.RELEVANCE_THRESHOLD == 0.65
    assert config.LLM_TEMPERATURE == 0.05
    assert config.LLM_MAX_TOKENS == 3000


def test_lmstudio_is_loopback_and_embedder_is_f16():
    assert config.LMSTUDIO_BASE_URL == "http://127.0.0.1:1234"
    assert config.EMBED_MODEL == "text-embedding-nomic-embed-text-v1.5@f16"


def test_system_prompt_forbids_fabrication_and_requires_citation():
    prompt = config.RAG_SYSTEM_PROMPT.lower()
    assert "only" in prompt
    assert "cite" in prompt
    assert "not found in the library" in prompt
    assert "never fabricate" in prompt
