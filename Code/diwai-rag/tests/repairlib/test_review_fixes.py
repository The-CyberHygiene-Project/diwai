"""Final-review findings (2026-10-04). Each test failed before its fix."""
import subprocess
from pathlib import Path

import pytest

from repairkit import admin, runner, signing
from repairkit.runner import Runner
from repairkit.shell import Shell
from repairlib.helpers import approve_with
from repairlib.test_runner import make
from repairlib.test_admin import fake_signer


# ---- C1: undo must only act on a real run of the repair it names ----------

def _fake_run_dir(tmp_path, repair="demo-fix", content=b"ATTACKER CONTENT"):
    d = tmp_path / "attacker"
    d.mkdir()
    (d / "record.json").write_text('{"repair": "%s", "run": "x", "state": "done"}' % repair)
    (d / "backup-demo.txt").write_bytes(content)
    return d


def test_C1_undo_refuses_absolute_path(lib_paths, soft_key, tmp_path):
    approve_with(lib_paths, "demo-fix", soft_key)
    r, target, out = make(lib_paths, tmp_path, answers=("yes",))
    d = _fake_run_dir(tmp_path)
    assert r.cmd_undo(str(d)) == 2
    assert target.read_text() == "bad"


def test_C1_undo_refuses_parent_traversal(lib_paths, soft_key, tmp_path):
    approve_with(lib_paths, "demo-fix", soft_key)
    r, target, out = make(lib_paths, tmp_path, answers=("yes",))
    _fake_run_dir(tmp_path)
    assert r.cmd_undo("../attacker") == 2
    assert target.read_text() == "bad"


def test_C1_undo_refuses_record_naming_another_repair(lib_paths, soft_key, tmp_path):
    approve_with(lib_paths, "demo-fix", soft_key)
    r, target, out = make(lib_paths, tmp_path)
    r.cmd_run("demo-fix")
    run = r.store.runs()[0]
    rec = r.store.load(run); rec["repair"] = "other-fix"; r.store.save(run, rec)
    r2, _, _ = make(lib_paths, tmp_path, answers=("yes",))
    assert r2.cmd_undo(run.name) == 2


def test_C1_undo_asks_for_exact_yes(lib_paths, soft_key, tmp_path):
    approve_with(lib_paths, "demo-fix", soft_key)
    r, target, out = make(lib_paths, tmp_path)
    r.cmd_run("demo-fix")
    run = r.store.runs()[0].name
    r2, target2, _ = make(lib_paths, tmp_path, text="good", answers=("y",))
    assert r2.cmd_undo(run) == 2 and target2.read_text() == "good"


# ---- I1: repair ids are plain names --------------------------------------

@pytest.mark.parametrize("rid", ["../../x", "/etc/x", "Demo-Fix", "demo_fix", "-x", "a b", ""])
def test_I1_bad_repair_ids_refused(lib_paths, soft_key, rid):
    ok, why = signing.verify(lib_paths, rid)
    assert not ok and "not a valid repair name" in why


def test_I1_approve_refuses_bad_id(tmp_path, lib_paths, soft_key):
    paths = fake_signer(tmp_path, soft_key, lib_paths)
    out = []
    assert admin.approve("../demo_fix", paths, Shell(sudo_prefix=[], speaker=lambda t: None),
                         device="fake", out=out.append) == 1


# ---- I2: sudo is signed out when the runner finishes ----------------------

def test_I2_main_signs_sudo_out(monkeypatch, lib_paths):
    calls = []
    monkeypatch.setattr(runner, "_sudo_sign_out", lambda: calls.append(True))
    runner.main(["list"], lib_paths)
    runner.main(["nonsense"], lib_paths)
    assert len(calls) == 2


# ---- I3: the yes must come from a person at a terminal --------------------

def test_I3_yes_from_a_pipe_is_refused(monkeypatch):
    class NotTty:
        def isatty(self):
            return False
    monkeypatch.setattr(runner.sys, "stdin", NotTty())
    with pytest.raises(EOFError):
        runner.terminal_ask("Type yes: ")


# ---- I4: the approver key must prove it is the YubiKey ---------------------

def _src(tmp_path):
    from repairlib.test_admin import source_tree
    return source_tree(tmp_path)


def test_I4_first_install_requires_proof_from_the_key(tmp_path, lib_paths):
    src = _src(tmp_path)
    appr = tmp_path / "appr"; appr.mkdir()
    (appr / "repair-approver.pem").write_text("PEM"); (appr / "repair-approver.credid").write_text("id")
    out = []
    rc = admin.install(src, lib_paths, Shell(sudo_prefix=[]), approver_dir=appr, out=out.append,
                       prove_approver=lambda pem, credid: False)
    assert rc == 1 and not lib_paths.approver_pem.exists()


def test_I4_proven_approver_is_installed_and_fingerprint_shown(tmp_path, lib_paths):
    src = _src(tmp_path)
    appr = tmp_path / "appr"; appr.mkdir()
    (appr / "repair-approver.pem").write_text("PEM"); (appr / "repair-approver.credid").write_text("id")
    out = []
    rc = admin.install(src, lib_paths, Shell(sudo_prefix=[]), approver_dir=appr, out=out.append,
                       prove_approver=lambda pem, credid: True)
    assert rc == 0 and lib_paths.approver_pem.read_text() == "PEM"
    assert any("SHA-256" in o for o in out)


# ---- I5: install only committed, reviewable code ---------------------------

def test_I5_uncommitted_edits_are_not_installed(tmp_path, lib_paths):
    src = _src(tmp_path)
    f = src / "repairs" / "demo_fix.py"
    f.write_text("ID = 'demo-fix'  # uncommitted edit\n")
    admin.install(src, lib_paths, Shell(sudo_prefix=[]), out=lambda s: None)
    assert (lib_paths.repairs / "demo_fix.py").read_text() == "ID = 'demo-fix'\n"


def test_I5_approve_shows_the_installed_commit(tmp_path, lib_paths, soft_key):
    src = _src(tmp_path)
    admin.install(src, lib_paths, Shell(sudo_prefix=[]), out=lambda s: None)
    commit = subprocess.run(["git", "-C", str(src), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    (lib_paths.repairs / "demo_fix.py").write_text((tmp_path / "lib" / "repairs" / "demo_fix.py").read_text())
    paths = fake_signer(tmp_path, soft_key, lib_paths)
    out = []
    admin.approve("demo-fix", paths, Shell(sudo_prefix=[], speaker=lambda t: None), device="fake", out=out.append)
    assert any(commit[:12] in o for o in out)


# ---- I7: nothing changed means no undo ------------------------------------

def test_I7_backup_failure_is_not_undone(lib_paths, soft_key, tmp_path):
    approve_with(lib_paths, "demo-fix", soft_key)
    r, target, out = make(lib_paths, tmp_path)
    mod = r.load("demo-fix")
    undone = []
    def bad_backup(ctx):
        raise OSError("disk full")
    mod.backup = bad_backup
    mod.undo = lambda ctx: undone.append(True)
    assert r.cmd_run("demo-fix") == 1
    assert undone == [] and any("Nothing was changed" in o for o in out)


# ---- M8 (graded Important): no symlinks published -------------------------

def test_M8_install_refuses_symlinks(tmp_path, lib_paths):
    src = _src(tmp_path)
    secret = tmp_path / "secret"; secret.write_text("KEY")
    (src / "repairs" / "demo_fix.data").mkdir()
    (src / "repairs" / "demo_fix.data" / "link").symlink_to(secret)
    subprocess.run(["git", "-C", str(src), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(src), "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "link"], check=True)
    out = []
    assert admin.install(src, lib_paths, Shell(sudo_prefix=[]), out=out.append) == 1
    assert not (lib_paths.repairs / "demo_fix.data" / "link").exists()
