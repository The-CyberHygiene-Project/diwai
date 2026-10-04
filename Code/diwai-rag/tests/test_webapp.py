import os
import threading
import time
import unicodedata

import pytest
from fastapi.testclient import TestClient

import rag_utils
from webapp import library, main


class Switch:
    def __init__(self, on=True):
        self.on = on

    def __call__(self):
        return self.on


@pytest.fixture
def env(temp_store, embed_calls):
    col = rag_utils.get_collection()
    docs = temp_store / "documents"
    lm = Switch(True)
    shutdowns = []
    app = main.create_app(collection=col, documents_dir=str(docs),
                          activity_path=str(temp_store / "activity.db"),
                          ready=lm, retry_seconds=0.05,
                          on_quit=lambda: shutdowns.append(True),
                          allowed_hosts={"testserver"})
    with TestClient(app) as client:
        yield {"client": client, "col": col, "docs": docs, "lm": lm, "app": app,
               "embed_calls": embed_calls, "shutdowns": shutdowns, "tmp": temp_store}


def upload(client, *files):
    return client.post("/upload", files=[("files", (n, data)) for n, data in files])


def jobs(client):
    return client.get("/api/jobs").json()


def wait_done(client, n=None, timeout=10):
    end = time.time() + timeout
    while time.time() < end:
        js = jobs(client)
        if js and all(j["state"] == "done" for j in js) and (n is None or len(js) >= n):
            return js
        time.sleep(0.02)
    raise AssertionError(f"jobs not done: {jobs(client)}")


def latest(client):
    return wait_done(client)[0]


def stored_files(docs):
    return sorted(p.relative_to(docs).as_posix() for p in docs.rglob("*")
                  if p.is_file() and ".incoming" not in p.parts)


TEXT = b"chrony makestep steps the clock on the first updates. " * 20


# ---- pages ------------------------------------------------------------------

def test_home_page_is_local_only_assets(env):
    page = env["client"].get("/").text
    assert '<script src="/static/htmx.min.js"' in page
    assert "https://" not in page and "http://" not in page
    assert "font-size: 20px" in page


def test_api_docs_are_disabled(env):
    assert env["client"].get("/docs").status_code == 404
    assert env["client"].get("/openapi.json").status_code == 404


def test_healthz(env):
    assert env["client"].get("/healthz").json() == {"ok": True}


def test_header_shows_lm_studio_state_in_words_and_counts(env):
    c = env["client"]
    upload(c, ("a.txt", TEXT))
    latest(c)
    h = c.get("/status").text
    assert "LM Studio running" in h and "1 document" in h and "chunk" in h
    env["lm"].on = False
    assert "LM Studio not running" in c.get("/status").text


# ---- adding -----------------------------------------------------------------

def test_add_stores_under_year_month_and_reports_added(env):
    upload(env["client"], ("notes.txt", TEXT))
    job = latest(env["client"])
    assert job["outcome"] == "added" and job["message"].startswith("✅")
    month = time.strftime("%Y-%m")
    assert stored_files(env["docs"]) == [f"{month}/notes.txt"]
    assert env["col"].count() > 0


def test_byte_identical_drop_is_skipped_without_embedding(env):
    c = env["client"]
    upload(c, ("notes.txt", TEXT))
    latest(c)
    before = len(env["embed_calls"])
    upload(c, ("copy.txt", TEXT))
    job = wait_done(c, 2)[0]
    assert job["outcome"] == "skipped" and job["message"].startswith("⏭️")
    assert len(env["embed_calls"]) == before
    assert len(stored_files(env["docs"])) == 1


def test_same_text_different_bytes_is_skipped_and_copy_removed(env):
    c = env["client"]
    upload(c, ("a.txt", TEXT))
    latest(c)
    upload(c, ("b.txt", TEXT + b"\n\n   "))
    assert wait_done(c, 2)[0]["outcome"] == "skipped"
    assert len(stored_files(env["docs"])) == 1


def test_name_clash_gets_a_number(env):
    c = env["client"]
    upload(c, ("plan.txt", TEXT))
    latest(c)
    upload(c, ("plan.txt", b"entirely different words " * 30))
    wait_done(c, 2)
    names = [os.path.basename(p) for p in stored_files(env["docs"])]
    assert sorted(names) == ["plan (2).txt", "plan.txt"]


def test_upper_and_lower_case_names_clash_like_apfs(env):
    c = env["client"]
    upload(c, ("report.txt", TEXT))
    latest(c)
    upload(c, ("Report.TXT", b"other content here " * 30))
    wait_done(c, 2)
    names = sorted(os.path.basename(p) for p in stored_files(env["docs"]))
    assert names == ["Report (2).TXT", "report.txt"]


def test_nfd_and_nfc_names_clash(env):
    c = env["client"]
    upload(c, (unicodedata.normalize("NFC", "résumé.txt"), TEXT))
    latest(c)
    upload(c, (unicodedata.normalize("NFD", "résumé.txt"), b"other content " * 40))
    wait_done(c, 2)
    names = [unicodedata.normalize("NFC", os.path.basename(p)) for p in stored_files(env["docs"])]
    assert sorted(names) == ["résumé (2).txt", "résumé.txt"]


def test_empty_file_reports_no_text_and_keeps_nothing(env):
    upload(env["client"], ("empty.txt", b"   \n"))
    job = latest(env["client"])
    assert job["outcome"] == "no_text" and job["message"].startswith("❌")
    assert stored_files(env["docs"]) == []


def test_unsupported_type_is_refused_at_once(env):
    upload(env["client"], ("tool.exe", b"MZ"))
    job = latest(env["client"])
    assert job["outcome"] == "refused" and "Can't add" in job["message"]
    assert stored_files(env["docs"]) == []
    assert not list((env["docs"] / ".incoming").glob("*"))


def test_too_large_is_refused(env, monkeypatch):
    monkeypatch.setattr(main, "MAX_UPLOAD_BYTES", 100)
    upload(env["client"], ("big.txt", b"x" * 500))
    job = latest(env["client"])
    assert job["outcome"] == "refused" and "too large" in job["message"]
    assert not list((env["docs"] / ".incoming").glob("*"))


def test_path_in_name_stays_inside_documents(env):
    upload(env["client"], ("../../escape.txt", TEXT))
    latest(env["client"])
    assert not (env["tmp"] / "escape.txt").exists()
    assert [os.path.basename(p) for p in stored_files(env["docs"])] == ["escape.txt"]


def test_long_name_is_added(env):
    name = "a" * 226 + ".txt"
    upload(env["client"], (name, TEXT))
    assert latest(env["client"])["outcome"] == "added"


def test_upper_case_extension_is_accepted(env):
    upload(env["client"], ("NOTES.TXT", TEXT))
    assert latest(env["client"])["outcome"] == "added"


def test_batch_upload_queues_each_file(env):
    upload(env["client"], ("a.txt", TEXT), ("b.txt", b"different text " * 40))
    js = wait_done(env["client"], 2)
    assert sorted(j["outcome"] for j in js) == ["added", "added"]


# ---- LM Studio down ---------------------------------------------------------

def test_add_waits_while_lm_studio_is_down_then_resumes(env):
    c = env["client"]
    env["lm"].on = False
    upload(c, ("w.txt", TEXT))
    end = time.time() + 5
    while time.time() < end and jobs(c)[0]["outcome"] != "paused":
        time.sleep(0.02)
    job = jobs(c)[0]
    assert job["state"] == "waiting" and job["message"].startswith("⏸️")
    env["lm"].on = True
    assert latest(c)["outcome"] == "added"


def test_embedder_failure_mid_job_pauses_instead_of_failing(env, monkeypatch):
    c = env["client"]
    real = rag_utils.embed_texts
    state = {"fail": True}

    def flaky(texts):
        if state["fail"]:
            env["lm"].on = False
            raise ConnectionError("LM Studio went away")
        return real(texts)

    monkeypatch.setattr(rag_utils, "embed_texts", flaky)
    upload(c, ("f.txt", TEXT))
    end = time.time() + 5
    while time.time() < end and jobs(c)[0]["outcome"] != "paused":
        time.sleep(0.02)
    state["fail"] = False
    env["lm"].on = True
    assert latest(c)["outcome"] == "added"


# ---- removing ---------------------------------------------------------------

def _doc_id(client):
    return client.get("/api/library").json()["rows"][0]["doc_id"]


def test_remove_deletes_chunks_but_keeps_the_stored_file(env):
    c = env["client"]
    upload(c, ("r.txt", TEXT))
    latest(c)
    c.post("/remove", data={"doc_id": _doc_id(c)})
    job = wait_done(c, 2)[0]
    assert job["outcome"] == "removed" and env["col"].count() == 0
    assert len(stored_files(env["docs"])) == 1


def test_second_remove_says_not_found(env):
    c = env["client"]
    upload(c, ("r.txt", TEXT))
    latest(c)
    doc_id = _doc_id(c)
    c.post("/remove", data={"doc_id": doc_id})
    wait_done(c, 2)
    c.post("/remove", data={"doc_id": doc_id})
    assert wait_done(c, 3)[0]["outcome"] == "not_found"


def test_remove_then_redrop_restores_the_stored_copy(env):
    c = env["client"]
    upload(c, ("r.txt", TEXT))
    latest(c)
    c.post("/remove", data={"doc_id": _doc_id(c)})
    wait_done(c, 2)
    upload(c, ("r-again.txt", TEXT))
    job = wait_done(c, 3)[0]
    assert job["outcome"] == "restored" and env["col"].count() > 0
    assert [os.path.basename(p) for p in stored_files(env["docs"])] == ["r.txt"]


# ---- library tab ------------------------------------------------------------

def test_library_filter_is_literal_and_counts(env):
    c = env["client"]
    upload(c, ("Plan [current].txt", TEXT), ("other.txt", b"something else " * 40))
    wait_done(c, 2)
    html = c.get("/library", params={"q": "[current]"}).text
    assert "Plan [current].txt" in html and "other.txt" not in html
    assert "Showing 1 of 1 matches" in html and "2 documents in the library" in html


def test_library_shows_at_most_100(env, monkeypatch):
    rows = [{"doc_id": str(i), "source": f"d{i:03}.txt", "chunks": 1, "added_at": "",
             "file_path": ""} for i in range(150)]
    monkeypatch.setattr(env["app"].state.index, "rows", lambda: rows)
    html = env["client"].get("/library").text
    assert "Showing 100 of 150 matches" in html and "d099.txt" in html and "d100.txt" not in html


def test_library_sorts_by_chunks(env):
    c = env["client"]
    upload(c, ("small.txt", b"tiny text"), ("large.txt", TEXT * 5))
    wait_done(c, 2)
    html = c.get("/library", params={"sort": "chunks", "dir": "desc"}).text
    assert html.index("large.txt") < html.index("small.txt")


def test_missing_date_shows_earlier(env):
    rows = [{"doc_id": "1", "source": "old.txt", "chunks": 1, "added_at": "", "file_path": ""}]
    env["app"].state.index.rows = lambda: rows
    assert "earlier" in env["client"].get("/library").text


def test_detail_shows_path_and_opening_text(env):
    c = env["client"]
    upload(c, ("d.txt", TEXT))
    latest(c)
    html = c.get("/library/detail", params={"doc_id": _doc_id(c)}).text
    assert "chrony makestep" in html and "d.txt" in html


# ---- quit and shutdown ------------------------------------------------------

def test_quit_is_refused_while_a_job_is_waiting(env):
    env["lm"].on = False
    upload(env["client"], ("q.txt", TEXT))
    r = env["client"].post("/quit")
    assert "busy" in r.text.lower() and env["shutdowns"] == []
    env["lm"].on = True
    latest(env["client"])


def test_quit_when_idle_shuts_down(env):
    r = env["client"].post("/quit")
    assert "Closing" in r.text and env["shutdowns"] == [True]


def test_stop_lets_the_running_job_finish(env, monkeypatch):
    c = env["client"]
    gate = threading.Event()
    real = rag_utils.embed_texts

    def slow(texts):
        gate.wait(5)
        return real(texts)

    monkeypatch.setattr(rag_utils, "embed_texts", slow)
    upload(c, ("s.txt", TEXT))
    end = time.time() + 5
    while time.time() < end and jobs(c)[0]["state"] != "working":
        time.sleep(0.02)
    stopper = threading.Thread(target=env["app"].state.worker.stop)
    stopper.start()
    time.sleep(0.1)
    gate.set()
    stopper.join(5)
    assert jobs(c)[0]["outcome"] == "added"


# ---- startup ----------------------------------------------------------------

def test_unfinished_jobs_are_marked_interrupted_on_restart(temp_store):
    from webapp.activity import ActivityLog
    log = ActivityLog(str(temp_store / "a.db"))
    jid = log.add("x.txt", "add")
    log.update(jid, state="working")
    log2 = ActivityLog(str(temp_store / "a.db"))
    log2.mark_interrupted()
    job = log2.recent()[0]
    assert job["state"] == "done" and "Interrupted" in job["message"]


def test_jobs_wait_for_the_index(temp_store, monkeypatch):
    gate = threading.Event()
    real = library.DocIndex.build

    def slow_build(self, col):
        gate.wait(5)
        real(self, col)

    monkeypatch.setattr(library.DocIndex, "build", slow_build)
    app = main.create_app(collection=rag_utils.get_collection(),
                          documents_dir=str(temp_store / "documents"),
                          activity_path=str(temp_store / "activity.db"),
                          ready=lambda: True, retry_seconds=0.05, on_quit=lambda: None,
                          allowed_hosts={"testserver"})
    with TestClient(app) as c:
        upload(c, ("i.txt", TEXT))
        time.sleep(0.3)
        assert jobs(c)[0]["state"] == "waiting"
        gate.set()
        assert latest(c)["outcome"] == "added"
