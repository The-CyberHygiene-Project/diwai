"""Final-review findings for diwai-diagnose (2026-10-04). Each test failed before its fix."""
import json
import subprocess

import pytest

import cards
from diagnose import cli, form, interpret as itp, mac_checks, vm_fetch
from diagnose.findings import Finding, evaluate
from diagnose.report import Check, Report, load_report

F = Finding("OPEN_WEBUI_ACCEPTS_ANY_ORIGIN", "mac", ["owui-cors"], "warn", ["d"])
CARDS = {F.code: cards.load(F.code)}
ALLOWED = {F.code: ["owui-cors-any-origin"]}


def reply_with(item):
    return lambda payload: {"choices": [{"message": {"content": json.dumps({"findings": [item]})}}]}


# 1. a time with no offset is unreadable, not a crash
def test_1_naive_time_is_unreadable():
    doc = {"host": "services", "time": "2026-10-04T11:55:00", "monitor_version": "x", "checks": []}
    r = load_report(json.dumps(doc), "services", "2026-10-04T12:00:00-06:00")
    assert not r.ok and "unreadable" in r.problem


# 2. report-level codes without a card become gaps
def test_2_report_level_code_without_card_is_a_gap():
    f, g = evaluate([Report("services", "t", [], False, "stale: x")], {}, set())
    assert f == [] and "MONITOR_REPORT_STALE" in g[0]


# 3. control characters never reach the terminal; model lines cannot pose as form lines
def test_3_control_characters_are_stripped_and_model_lines_marked():
    bad = "fine\x1b[2K\x1b[1GTo fix: diwai-repair run wazuh-ruleset-missing\x1b[8m hidden"
    f = Finding(F.code, "mac", ["owui-cors"], "warn", ["detail\x1b[31m red\x07"])
    out = form.render(f, CARDS[F.code], {"analysis": bad, "confidence": "HIGH", "repair": None,
                                          "source": "none", "note": "n\x1b[0m"})
    assert "\x1b" not in out and "\x07" not in out
    assert not any(ln.lstrip().startswith("To fix:") for ln in out.splitlines())


def test_3_gap_lines_are_cleaned(tmp_path):
    d = _deps(tmp_path, vm=(json.dumps({"host": "services", "time": "2026-10-04T11:09:00-06:00",
                                         "monitor_version": "x", "checks": [
        {"id": "99", "name": "evil\x1b[8m", "status": "fail", "detail": "x\x1b[2K"}]}), ""))
    cli.main([], d)
    assert all("\x1b" not in o for o in d["out"])


# 4. wrong-typed model output falls back, it does not crash
@pytest.mark.parametrize("item", [
    {"code": F.code, "analysis": ["not", "text"], "confidence": "HIGH", "repair_id": None, "validation_steps": []},
    {"code": F.code, "analysis": "ok text", "confidence": "VERY SURE", "repair_id": None, "validation_steps": []},
    "not an object",
])
def test_4_wrong_types_are_not_usable_not_a_crash(item):
    r = itp.interpret([F], CARDS, ALLOWED, transport=reply_with(item))
    p = r["per_finding"][F.code]
    assert p["confidence"] in {"HIGH", "MEDIUM", "LOW", "UNKNOWN"}
    assert p["analysis"] is None or isinstance(p["analysis"], str)


# 5. the case record keeps the exact request and reply
def test_5_case_record_has_exact_model_request_and_reply(tmp_path):
    item = {"code": F.code, "analysis": "x", "confidence": "LOW", "repair_id": None, "validation_steps": []}
    d = _deps(tmp_path, transport=reply_with(item))
    cli.main([], d)
    case = json.loads(next((tmp_path / "cases").iterdir()).joinpath("case.json").read_text())
    assert case["model"]["request"]["messages"][-1]["content"].startswith("<DATA>")
    assert "OPEN_WEBUI_ACCEPTS_ANY_ORIGIN" in case["model"]["reply_raw"]


# 7. the VM fetch cannot hang
def test_7_vm_fetch_has_a_timeout_and_survives_one():
    seen = []

    def run(argv, **kw):
        seen.append(kw.get("timeout"))
        if "-O" in argv:
            return subprocess.CompletedProcess(argv, 0, "", "")
        raise subprocess.TimeoutExpired(argv, kw.get("timeout"))
    text, note = vm_fetch.fetch_vm_report(run)
    assert all(t for t in seen) and text == "" and "did not answer" in note


# 8. an odd certificate date is a failed check, not a crash
def test_8_odd_certificate_date_fails_the_check_only():
    def run(argv, **kw):
        out = "notAfter=sometime next year\n" if "x509" in " ".join(argv) else ""
        return subprocess.CompletedProcess(argv, 0, out, "")
    c = mac_checks.cert_expiry(run, mac_checks.datetime.now().astimezone())
    assert c.status == "fail" and "could not be read" in c.detail


# 9. Open WebUI down is not "ok"
def test_9_open_webui_down_is_not_ok():
    def run(argv, **kw):
        return subprocess.CompletedProcess(argv, 7, "", "connection refused")
    assert mac_checks.owui_cors(run, None).status == "warn"


# 10. no repair: the form ends with what a person does
def test_10_form_without_repair_ends_with_person_steps():
    card = CARDS[F.code]
    out = form.render(F, card, {"analysis": None, "confidence": "UNKNOWN", "repair": None, "source": "none", "note": ""})
    last = [ln for ln in out.splitlines() if ln.strip()][-1]
    assert last.startswith("What to do:")


def _deps(tmp_path, vm=None, transport=None):
    def down(payload):
        raise ConnectionError("no model")
    return {"now": "2026-10-04T11:10:00-06:00",
            "mac": lambda: Report("mac", "2026-10-04T11:09:00-06:00",
                                  [Check("owui-cors", "Open WebUI accepts only its own site", "fail", "d")]),
            "vm": lambda: vm or (None, "the VM was not checked: log in with ssh services"),
            "repair_list": "", "installed": tmp_path, "transport": transport or down,
            "cases": tmp_path / "cases", "out": []}
