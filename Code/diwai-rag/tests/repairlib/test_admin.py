import shutil
import subprocess
from pathlib import Path
from repairkit import admin, signing
from repairkit.paths import Paths
from repairkit.shell import Shell
from repairlib.helpers import approve_with

ROOT = Path(__file__).resolve().parents[2]

FAKE_ASSERT = '''#!/usr/bin/python3
# Stand-in for fido2-assert -G -p -v: signs the given client data hash with a software key.
import base64, hashlib, subprocess, sys
args = sys.argv[1:]
inp = open(args[args.index("-i") + 1]).read().split("\\n")
cdh = base64.b64decode(inp[0]); rp = inp[1]
auth = hashlib.sha256(rp.encode()).digest() + bytes([0x05]) + (9).to_bytes(4, "big")
sig = subprocess.run(["/usr/bin/openssl", "dgst", "-sha256", "-sign", "KEY"], input=auth + cdh,
                     capture_output=True, check=True).stdout
b = lambda x: base64.b64encode(x).decode()
open(args[args.index("-o") + 1], "w").write(f"{b(cdh)}\\n{rp}\\n{b(bytes([0x58, len(auth)]) + auth)}\\n{b(sig)}\\n")
'''


def fake_signer(tmp_path, key, lib_paths):
    f = tmp_path / "fake-fido2-assert"
    f.write_text(FAKE_ASSERT.replace("KEY", str(key)))
    f.chmod(0o755)
    lib_paths.approver_credid.write_text("Y3JlZGlk\n")
    lib = tmp_path / "fake-libfido2.dylib"; lib.write_text("lib")
    paths = Paths(lib=lib_paths.lib, runs=lib_paths.runs, fido_assert=str(f), fido_lib=str(lib))
    paths.fido_pins.write_text(admin.fido_pins_text(paths))     # as install records them
    return paths


def source_tree(tmp_path, approver=None):
    src = tmp_path / "src"
    shutil.copytree(ROOT / "repairkit", src / "repairkit", ignore=shutil.ignore_patterns("__pycache__"))
    (src / "repairs").mkdir()
    (src / "repairs" / "demo_fix.py").write_text("ID = 'demo-fix'\n")
    (src / "bin").mkdir()
    (src / "bin" / "diwai-repair").write_text("#!/usr/bin/python3 -I\n")
    git = ["git", "-C", str(src), "-c", "user.name=t", "-c", "user.email=t@t"]
    subprocess.run(["git", "init", "-q", str(src)], check=True)
    subprocess.run(git + ["add", "-A"], check=True)
    subprocess.run(git + ["commit", "-qm", "reviewed"], check=True)
    return src


def test_install_copies_kit_repairs_and_entry_point(tmp_path, lib_paths):
    src = source_tree(tmp_path)
    assert admin.install(src, lib_paths, Shell(sudo_prefix=[]), out=lambda s: None) == 0
    assert (lib_paths.repairs / "demo_fix.py").read_text() == "ID = 'demo-fix'\n"
    assert (lib_paths.lib / "bin" / "diwai-repair").exists()


def test_install_sets_approver_once_and_never_replaces_it(tmp_path, lib_paths):
    src = source_tree(tmp_path)
    first, second = tmp_path / "a", tmp_path / "b"
    for d, text in ((first, "KEY-ONE"), (second, "KEY-TWO")):
        d.mkdir(); (d / "repair-approver.pem").write_text(text); (d / "repair-approver.credid").write_text("id")
    admin.install(src, lib_paths, Shell(sudo_prefix=[]), approver_dir=first, out=lambda s: None, prove_approver=lambda pem, credid: True)
    admin.install(src, lib_paths, Shell(sudo_prefix=[]), approver_dir=second, out=lambda s: None, prove_approver=lambda pem, credid: True)
    assert lib_paths.approver_pem.read_text() == "KEY-ONE"


def test_reinstall_changed_repair_invalidates_approval(tmp_path, lib_paths, soft_key):
    src = tmp_path / "src"
    shutil.copytree(lib_paths.lib, src)
    (src / "bin").mkdir(); (src / "bin" / "diwai-repair").write_text("#!/usr/bin/python3 -I\n")
    approve_with(lib_paths, "demo-fix", soft_key)
    assert signing.verify(lib_paths, "demo-fix")[0]
    git = ["git", "-C", str(src), "-c", "user.name=t", "-c", "user.email=t@t"]
    subprocess.run(["git", "init", "-q", str(src)], check=True)
    f = src / "repairs" / "demo_fix.py"; f.write_text(f.read_text() + "# new\n")
    subprocess.run(git + ["add", "-A"], check=True); subprocess.run(git + ["commit", "-qm", "edit"], check=True)
    admin.install(src, lib_paths, Shell(sudo_prefix=[]), out=lambda s: None)
    assert signing.verify(lib_paths, "demo-fix")[0] is False


def test_approve_signs_speaks_and_installs_approval(tmp_path, lib_paths, soft_key):
    paths = fake_signer(tmp_path, soft_key, lib_paths)
    said, out = [], []
    sh = Shell(sudo_prefix=[], speaker=said.append)
    assert admin.approve("demo-fix", paths, sh, device="fake", out=out.append) == 0
    assert signing.verify(paths, "demo-fix") == (True, "approved")
    assert said == [admin.SPOKEN_PROMPT]
    assert admin.SPOKEN_PROMPT.index("PIN") < admin.SPOKEN_PROMPT.index("touch")   # the order the key asks
    assert any("PIN" in o for o in out)


def test_failed_signing_installs_nothing(tmp_path, lib_paths, soft_key):
    paths = fake_signer(tmp_path, soft_key, lib_paths)
    Path(paths.fido_assert).write_text("#!/bin/bash\nexit 1\n")
    paths.fido_pins.write_text(admin.fido_pins_text(paths))   # a pinned tool that fails to sign
    out = []
    assert admin.approve("demo-fix", paths, Shell(sudo_prefix=[], speaker=lambda t: None),
                         device="fake", out=out.append) == 1
    assert not (paths.approvals / "demo-fix.assertion").exists()
    assert any("try again" in o for o in out)


def test_approve_without_yubikey_says_so(tmp_path, lib_paths, soft_key):
    paths = fake_signer(tmp_path, soft_key, lib_paths)
    out = []
    assert admin.approve("demo-fix", paths, Shell(sudo_prefix=[], speaker=lambda t: None),
                         device="", out=out.append) == 1
    assert any("plugged in" in o for o in out)


def test_entry_point_uses_production_paths_and_isolation():
    text = (ROOT / "bin" / "diwai-repair").read_text()
    assert text.startswith("#!/Library/Developer/CommandLineTools/usr/bin/python3 -I\n")   # real interpreter; -I isolation
    assert "PRODUCTION" in text and "os.environ" not in text and "getenv" not in text
