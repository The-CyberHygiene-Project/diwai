import pytest

import config
import identifiers
import ingest
import rag_utils


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


# ---- finding identifiers ----------------------------------------------------

def test_finds_each_kind_in_order_without_repeats():
    text = ("Fix CVE-2024-6387 (RLSA-2024:4312) for 3.14.1 and 3.5.6[b]; see "
            "DIWAI-CR-2026-09-08, POA&M-076, RB-04 and chronyd.service. Again CVE-2024-6387.")
    assert identifiers.find(text) == [
        "CVE-2024-6387", "RLSA-2024:4312", "3.14.1", "3.5.6[b]",
        "DIWAI-CR-2026-09-08", "POA&M-076", "RB-04", "chronyd.service"]


def test_case_is_normalised_for_advisories():
    assert identifiers.find("is cve-2024-6387 fixed?") == ["CVE-2024-6387"]


def test_version_numbers_that_are_not_controls_are_ignored():
    assert identifiers.find("Python 3.12.15 and OpenSSL 3.5") == []


def test_plain_prose_has_no_identifiers():
    assert identifiers.find("How do I step the clock after the VM sleeps?") == []


def test_unit_names_with_instances():
    assert identifiers.find("restart [EMAIL-REDACTED] now") == \
        ["[EMAIL-REDACTED]"]


# ---- exact lookup -----------------------------------------------------------

@pytest.fixture
def lib(temp_store):
    col = rag_utils.get_collection()
    docs = temp_store / "docs"

    def add(name, text):
        ingest.ingest_file(str(write(docs / name, text)), col)
    return col, add


def test_identifier_own_file_comes_first_in_chunk_order(lib):
    col, add = lib
    add("notes.md", "Clock trouble? RB-04 covers it. " + "filler " * 50)
    add("RB-04_VM_Clock_Drift.md",
        "# RB-04 VM clock drift\n\n" + "\n\n".join(f"Step {i}. " + "x" * 900 for i in range(4)))
    hits = identifiers.exact_hits("RB-04", col, limit=8)
    own = [h for h in hits if h["source"] == "RB-04_VM_Clock_Drift.md"]
    assert hits[0]["source"] == "RB-04_VM_Clock_Drift.md"
    # later chunks don't contain "RB-04" at all: only the own-file rule finds them
    assert any("RB-04" not in h["text"] for h in own)
    assert len(own) == len(col.get(where={"source": "RB-04_VM_Clock_Drift.md"})["ids"])
    assert [h["metadata"]["chunk_index"] for h in own] == sorted(h["metadata"]["chunk_index"] for h in own)
    assert all(h["relevance"] == 1.0 for h in hits)


def test_heading_beats_table_of_contents_beats_citation(lib):
    col, add = lib
    # names sort the opposite way to the expected ranking, so only the rank decides
    add("a_cites.md", "As required by 3.5.6 we review accounts. " + "words " * 40)
    toc = "\n".join(f"## {n} Something" for n in ("3.5.1", "3.5.2", "3.5.3", "3.5.4", "3.5.5", "3.5.6"))
    add("b_toc.md", toc)
    add("c_defines.md", "3.5.6 Disable identifiers after a defined period of inactivity.\n\nBody text.")
    order = [h["source"] for h in identifiers.exact_hits("3.5.6", col, limit=8)]
    assert order[:3] == ["c_defines.md", "b_toc.md", "a_cites.md"]


def test_no_match_gives_no_exact_hits(lib):
    col, add = lib
    add("a.md", "nothing relevant here")
    assert identifiers.exact_hits("CVE-2099-0001", col, limit=8) == []


# ---- retrieve_with_ids ------------------------------------------------------

def test_question_without_identifiers_behaves_like_retrieve(lib):
    col, add = lib
    add("chrony.md", "chrony makestep steps the clock")
    q = "chrony makestep steps the clock"
    assert identifiers.retrieve_with_ids(q) == rag_utils.retrieve(q)


def test_exact_hits_lead_and_are_not_repeated(lib):
    col, add = lib
    add("a.md", "Patch CVE-2024-6387 in openssh now.")
    add("b.md", "Unrelated text about mail.")
    hits = identifiers.retrieve_with_ids("Patch CVE-2024-6387 in openssh now.")
    assert hits[0]["source"] == "a.md" and hits[0]["relevance"] == 1.0
    ids = [h["id"] for h in hits]
    assert len(ids) == len(set(ids))


def test_result_size_is_max_of_top_k_and_exact_plus_three(lib, monkeypatch):
    col, add = lib
    for i in range(12):
        add(f"d{i}.md", f"Document {i} mentions POA&M-076 once. " + f"unique{i} " * 30)
    monkeypatch.setattr(config, "RELEVANCE_THRESHOLD", -1.0)
    hits = identifiers.retrieve_with_ids("What is POA&M-076?", top_k=2)
    exact = [h for h in hits if h["relevance"] == 1.0]
    assert len(exact) == identifiers.EXACT_BUDGET
    assert len(hits) == max(2, len(exact) + 3)


def test_at_most_four_identifiers_are_looked_up(lib, monkeypatch):
    col, add = lib
    seen = []
    real = identifiers.exact_hits
    monkeypatch.setattr(identifiers, "exact_hits",
                        lambda ident, c, limit, *docs: seen.append(ident) or real(ident, c, limit, *docs))
    identifiers.retrieve_with_ids("RB-01 RB-02 RB-03 RB-04 RB-05 RB-06")
    assert seen == ["RB-01", "RB-02", "RB-03", "RB-04"]


def test_retrieve_hits_carry_chunk_ids(lib):
    col, add = lib
    add("a.md", "some text")
    assert rag_utils.retrieve("some text")[0]["id"].endswith("::chunk::0")
