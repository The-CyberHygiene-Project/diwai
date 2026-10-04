"""The 8 deferred minor review points (2026-10-04). Each test failed before its fix."""
import importlib.util
import subprocess
from pathlib import Path

from repairkit import admin, signing
from repairkit.records import RunStore
from repairkit.shell import Shell
from repairlib.helpers import approve_with
from repairlib.test_runner import make
from repairlib.test_admin import fake_signer, source_tree

ROOT = Path(__file__).resolve().parents[2]


# 1. undo re-checks afterwards
def test_1_undo_rechecks_and_says_the_problem_is_back(lib_paths, soft_key, tmp_path):
    approve_with(lib_paths, "demo-fix", soft_key)
    r, target, out = make(lib_paths, tmp_path, answers=("yes", "yes"))
    r.cmd_run("demo-fix")
    run = r.store.runs()[0]
    assert r.cmd_undo(run.name) == 0
    assert any("problem is back" in o for o in out)
    assert "present" in r.store.load(run)["after_undo"]


# 2. Ctrl-C at the yes prompt is a cancel
def test_2_ctrl_c_at_the_prompt_cancels(lib_paths, soft_key, tmp_path):
    approve_with(lib_paths, "demo-fix", soft_key)
    r, target, out = make(lib_paths, tmp_path)
    def interrupt(prompt):
        raise KeyboardInterrupt
    r.ask = interrupt
    assert r.cmd_run("demo-fix") == 2
    assert target.read_text() == "bad" and r.store.runs() == []
    assert any("Cancelled" in o for o in out)


# 3. lock: refused sudo is not "another repair"; status shows a stale lock
def test_3_lock_states_are_told_apart(lib_paths):
    s = RunStore(lib_paths, Shell(sudo_prefix=[]))
    assert s.lock() is True
    assert s.lock() == "held"
    s.unlock()
    broken = RunStore(lib_paths, Shell(sudo_prefix=["/usr/bin/false"]))
    assert broken.lock() == "error"


def test_3_refused_sudo_on_the_lock_is_reported_as_such(lib_paths, soft_key, tmp_path):
    approve_with(lib_paths, "demo-fix", soft_key)
    r, target, out = make(lib_paths, tmp_path)
    r.store.lock = lambda: "error"
    assert r.cmd_run("demo-fix") == 2
    assert any("Could not take the lock" in o for o in out)
    assert not any("Another repair is running" in o for o in out)


def test_3_status_shows_a_left_over_lock_and_how_to_clear_it(lib_paths, soft_key, tmp_path):
    r, target, out = make(lib_paths, tmp_path)
    r.store.lock()
    r.cmd_status()
    assert any("lock" in o.lower() and "rmdir" in o for o in out)


# 4. the command file itself is approved
def test_4_manifest_includes_the_command_file(lib_paths):
    (lib_paths.lib / "bin").mkdir()
    (lib_paths.lib / "bin" / "diwai-repair").write_text("#!x\n")
    assert "  bin/diwai-repair\n" in signing.manifest(lib_paths, "demo-fix").decode()


# 5. VM writes are atomic and keep the file's mode
def test_5_vm_write_goes_through_a_copy_and_keeps_mode(tmp_path):
    from repairlib.test_repair_wazuh_ruleset import setup, wz, STOCK_ONLY
    ctx, conf = setup(tmp_path, STOCK_ONLY)
    conf.chmod(0o640)
    wz.backup(ctx); wz.apply(ctx)
    assert oct(conf.stat().st_mode & 0o777) == "0o640"
    assert not list(conf.parent.glob("*.diwai-tmp"))
    script = []
    real = ctx.shell.vm
    ctx.shell.vm = lambda s, **kw: script.append(s) or real(s, **kw)
    wz.undo(ctx)
    assert any("mv -f" in s for s in script)


# 6. the FIDO2 tools are pinned at install
def _pinned(tmp_path, lib_paths, soft_key):
    paths = fake_signer(tmp_path, soft_key, lib_paths)
    src = source_tree(tmp_path)
    admin.install(src, paths, Shell(sudo_prefix=[]), out=lambda s: None)
    (paths.repairs / "demo_fix.py").write_text((ROOT / "tests" / "repairlib" / "helpers.py").read_text().split("DEMO = '''")[1].split("'''")[0])
    return paths


def test_6_approve_refuses_a_changed_signing_tool(tmp_path, lib_paths, soft_key):
    paths = _pinned(tmp_path, lib_paths, soft_key)
    Path(paths.fido_assert).write_text(Path(paths.fido_assert).read_text() + "# changed\n")
    out = []
    assert admin.approve("demo-fix", paths, Shell(sudo_prefix=[], speaker=lambda t: None),
                         device="fake", out=out.append) == 1
    assert any("changed since" in o for o in out)


def test_6_approve_works_with_the_pinned_tools(tmp_path, lib_paths, soft_key):
    paths = _pinned(tmp_path, lib_paths, soft_key)
    assert admin.approve("demo-fix", paths, Shell(sudo_prefix=[], speaker=lambda t: None),
                         device="fake", out=lambda s: None) == 0


# 7. the command runs the real interpreter, not the redirectable shim
def test_7_entry_points_use_the_real_interpreter():
    real = "/Library/Developer/CommandLineTools/usr/bin/python3"
    assert (ROOT / "bin" / "diwai-repair").read_text().startswith(f"#!{real} -I\n")
    assert real in (ROOT / "tools" / "repair-install").read_text()
    import re
    assert not re.search(r"(?<![\w/])/usr/bin/python3", (ROOT / "tools" / "repair-install").read_text())


# 8. a literal "*" means any site is allowed
def test_8_star_answer_counts_as_any_site_allowed(tmp_path):
    from repairlib.test_repair_owui_cors import setup, cors
    ctx, launcher, fake = setup(tmp_path)
    ctx.shell.runner = lambda argv, **kw: subprocess.CompletedProcess(
        argv, 0, "HTTP/1.1 200 OK\r\naccess-control-allow-origin: *\r\n", "")
    assert cors.check(ctx) is not None
