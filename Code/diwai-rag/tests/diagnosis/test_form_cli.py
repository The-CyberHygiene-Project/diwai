import json
import subprocess

import cards
from diagnose import cli
from diagnose.findings import Finding
from diagnose.form import render
from diagnose.report import Check, Report

F = Finding("OPEN_WEBUI_ACCEPTS_ANY_ORIGIN", "mac", ["owui-cors"], "warn", ["Open WebUI CORS: echoes evil.example"])


def test_form_ends_with_the_exact_command_when_a_repair_fits():
    out = render(F, cards.load(F.code), {"analysis": "x", "confidence": "HIGH", "repair": "owui-cors-any-origin",
                                         "source": "model", "note": ""})
    assert out.rstrip().endswith("To fix: diwai-repair run owui-cors-any-origin")
    assert "Found on mac: Open WebUI CORS" in out and "from the local model" in out


def test_form_without_repair_gives_person_steps():
    card = cards.load(F.code)
    out = render(F, card, {"analysis": None, "confidence": "UNKNOWN", "repair": None,
                           "source": "none", "note": "the model was unavailable"})
    flat = " ".join(out.split())          # the form wraps lines; compare the words, not the layout
    assert "To fix:" not in out and card.repair.split(".")[0] in flat and "the model was unavailable" in flat


def model_down(payload):
    raise ConnectionError("no model in unit tests")


def deps(tmp_path, mac_status="fail", vm=None, transport=model_down):
    return {"now": "2026-10-04T11:10:00-06:00",
            "mac": lambda: Report("mac", "2026-10-04T11:09:00-06:00",
                                  [Check("owui-cors", "Open WebUI accepts only its own site", mac_status, "d")]),
            "vm": lambda: vm or (None, "the VM was not checked: log in with ssh services"),
            "repair_list": "owui-cors-any-origin approved\n",
            "installed": tmp_path, "transport": transport, "cases": tmp_path / "cases", "out": []}


def test_nothing_found(tmp_path):
    d = deps(tmp_path, mac_status="ok")
    assert cli.main([], d) == 0 and any("Nothing found" in o for o in d["out"])


def test_no_vm_session_is_said_plainly(tmp_path):
    d = deps(tmp_path)
    cli.main([], d)
    assert any("the VM was not checked" in o for o in d["out"])


def test_offers_the_approved_repair_meant_for_the_finding(tmp_path):
    (tmp_path / "owui_cors_any_origin.py").write_text('ID = "owui-cors-any-origin"\nCARD = "OPEN_WEBUI_ACCEPTS_ANY_ORIGIN"\n')
    d = deps(tmp_path)
    cli.main([], d)
    assert any("To fix: diwai-repair run owui-cors-any-origin" in o for o in d["out"])


def test_case_folder_holds_reports_findings_and_forms(tmp_path):
    d = deps(tmp_path)
    cli.main([], d)
    case = next((tmp_path / "cases").iterdir())
    data = json.loads((case / "case.json").read_text())
    assert data["findings"][0]["code"] == F.code and (case / "forms.txt").read_text()


def test_stale_vm_report_becomes_a_finding(tmp_path):
    old = json.dumps({"host": "services", "time": "2026-10-04T09:00:00-0600", "monitor_version": "x",
                      "checks": []})
    d = deps(tmp_path, mac_status="ok", vm=(old, ""))
    cli.main([], d)
    assert any("MONITOR_REPORT_STALE" in o for o in d["out"])


def test_diagnose_never_calls_sudo(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr(subprocess, "run",
                        lambda argv, **kw: calls.append(argv) or subprocess.CompletedProcess(argv, 0, "", ""))
    cli.main([], deps(tmp_path))
    assert not any("sudo" in " ".join(map(str, a)) for a in calls)
