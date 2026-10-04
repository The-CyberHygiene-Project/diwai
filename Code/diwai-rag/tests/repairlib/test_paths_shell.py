import os, subprocess, sys
from pathlib import Path
from repairkit import paths, shell


def test_production_paths_are_the_root_owned_locations():
    p = paths.PRODUCTION
    assert p.lib == Path("/usr/local/lib/diwai-repair")
    assert p.runs == Path("/var/db/diwai-repair/runs")
    assert p.approvals == p.lib / "approvals"
    assert p.approver_pem == p.lib / "approver.pem"
    assert p.openssl == "/usr/bin/openssl"
    assert p.rp_id == "diwai-repair"


def test_production_paths_ignore_environment():
    code = "from repairkit import paths; print(paths.PRODUCTION.lib)"
    env = dict(os.environ, DIWAI_REPAIR_ROOT="/tmp/evil", DIWAI_REPAIR_LIB="/tmp/evil")
    out = subprocess.run([sys.executable, "-c", code], env=env, capture_output=True,
                         text=True, cwd=Path(__file__).resolve().parents[2]).stdout.strip()
    assert out == "/usr/local/lib/diwai-repair"


def test_mac_runs_with_sudo_prefix_only_when_asked():
    seen = []
    sh = shell.Shell(sudo_prefix=["SUDO"], vm_prefix=["SSH"],
                     runner=lambda argv, **kw: seen.append(argv) or subprocess.CompletedProcess(argv, 0, "", ""))
    sh.mac(["cat", "x"]); sh.mac(["cp", "a", "b"], sudo=True)
    assert seen == [["cat", "x"], ["SUDO", "cp", "a", "b"]]


def test_vm_wraps_script_and_uses_sudo_bash_when_asked():
    seen = []
    sh = shell.Shell(sudo_prefix=[], vm_prefix=["SSH"],
                     runner=lambda argv, **kw: seen.append(argv) or subprocess.CompletedProcess(argv, 0, "ok\r\n", ""))
    r = sh.vm("echo hi", sudo=True)
    assert seen == [["SSH", "sudo -n bash -c 'echo hi'"]]   # ssh joins its arguments; quiet steps never wait for a password
    assert r.stdout == "ok\n"      # carriage returns from the remote terminal removed


def test_local_vm_mode_never_calls_real_sudo():
    seen = []
    sh = shell.Shell(sudo_prefix=[], vm_prefix=[],
                     runner=lambda argv, **kw: seen.append(argv) or subprocess.CompletedProcess(argv, 0, "", ""))
    sh.vm("echo hi", sudo=True)
    assert seen == [["bash", "-c", "echo hi"]]


def test_vm_ready_uses_the_session_check():
    assert shell.Shell(vm_check=lambda: True).vm_ready() is True
    assert shell.Shell(vm_check=lambda: False).vm_ready() is False


def test_runtime_code_compiles_under_system_python():
    root = Path(__file__).resolve().parents[2]
    files = [str(p) for p in (root / "repairkit").glob("*.py")] + [str(p) for p in (root / "repairs").glob("*.py")]
    r = subprocess.run(["/usr/bin/python3", "-m", "py_compile", *files], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_vm_output_is_captured_quietly_unless_shown():
    quiet, shown = [], []
    sh = shell.Shell(sudo_prefix=[], vm_prefix=["SSH"],
                     runner=lambda argv, **kw: quiet.append(argv) or subprocess.CompletedProcess(argv, 0, "data", "noise"),
                     vm_runner=lambda argv, **kw: shown.append(argv) or subprocess.CompletedProcess(argv, 0, "", ""))
    r = sh.vm("cat secret")
    assert quiet and not shown and r.stdout == "data"      # nothing echoed; stderr kept apart
    sh.vm("restart", show=True)
    assert shown


def test_quiet_vm_reads_do_not_force_a_terminal():
    seen = []
    sh = shell.Shell(sudo_prefix=[], vm_prefix=["SSH", "-tt", "host"],
                     runner=lambda argv, **kw: seen.append(argv) or subprocess.CompletedProcess(argv, 0, "", ""),
                     vm_runner=lambda argv, **kw: seen.append(argv) or subprocess.CompletedProcess(argv, 0, "", ""))
    sh.vm("cat x"); sh.vm("restart", show=True)
    assert "-tt" not in seen[0] and "-tt" in seen[1]


def test_quiet_vm_sudo_never_waits_for_a_password():
    seen = []
    sh = shell.Shell(sudo_prefix=[], vm_prefix=["SSH"],
                     runner=lambda argv, **kw: seen.append(argv) or subprocess.CompletedProcess(argv, 0, "", ""))
    sh.vm("cat x", sudo=True)
    assert seen[-1][-1].startswith("sudo -n bash -c ")


def test_vm_sudo_start_prompts_once_in_a_terminal_and_end_forgets():
    """The VM's password prompt has no line break, so it must reach the terminal
    directly: no capture, no line-by-line copying (2026-10-04: it stayed invisible)."""
    shown, quiet = [], []
    def interactive(argv, **kw):
        assert "capture_output" not in kw and "stdout" not in kw   # the terminal itself
        shown.append(argv); return subprocess.CompletedProcess(argv, 0)
    sh = shell.Shell(sudo_prefix=[], vm_prefix=["SSH", "-tt", "host"],
                     runner=lambda argv, **kw: quiet.append(argv) or subprocess.CompletedProcess(argv, 0, "", ""),
                     interactive=interactive)
    assert sh.vm_sudo_start() is True
    assert shown == [["SSH", "-tt", "host", "sudo -v"]]
    sh.vm_sudo_end()
    assert quiet[-1] == ["SSH", "host", "sudo -K"]


def test_vm_sudo_start_reports_a_refused_password():
    sh = shell.Shell(sudo_prefix=[], vm_prefix=["SSH", "-tt", "host"],
                     interactive=lambda argv, **kw: subprocess.CompletedProcess(argv, 1))
    assert sh.vm_sudo_start() is False
