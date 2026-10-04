import subprocess
from diagnose.vm_fetch import fetch_vm_report


def test_no_session_means_vm_not_checked():
    def run(argv, **kw):
        return subprocess.CompletedProcess(argv, 255, "", "")
    rep, note = fetch_vm_report(run)
    assert rep is None and "ssh services" in note


def test_session_reads_the_report_without_sudo():
    seen = []

    def run(argv, **kw):
        seen.append(argv)
        return subprocess.CompletedProcess(argv, 0, '{"host":"services"}', "")
    text, note = fetch_vm_report(run)
    assert all("sudo" not in " ".join(a) for a in seen) and "services" in text and note == ""


def test_unreadable_report_on_the_vm_is_said():
    def run(argv, **kw):
        return subprocess.CompletedProcess(argv, 0 if "-O" in argv else 1, "", "No such file")
    text, note = fetch_vm_report(run)
    assert text == "" and "could not be read" in note
