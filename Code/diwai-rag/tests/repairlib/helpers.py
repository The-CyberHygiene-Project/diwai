"""Shared test helpers for the repair library (fixtures live in conftest.py)."""
import base64, hashlib, shutil, subprocess
from pathlib import Path
from repairkit.paths import Paths

ROOT = Path(__file__).resolve().parents[2]
UP, UV = 0x01, 0x04


def lib_paths(tmp_path):
    """An installed-looking library in a temp folder, with one trivial repair."""
    lib = tmp_path / "lib"
    shutil.copytree(ROOT / "repairkit", lib / "repairkit", ignore=shutil.ignore_patterns("__pycache__"))
    (lib / "repairs").mkdir()
    (lib / "approvals").mkdir()
    (tmp_path / "runs").mkdir()
    (lib / "repairs" / "demo_fix.py").write_text(DEMO)
    return Paths(lib=lib, runs=tmp_path / "runs")


def soft_key(tmp_path, lib_paths):
    """A throwaway software P-256 key standing in for the YubiKey; its public half is the approver."""
    key = tmp_path / "isso.key"
    subprocess.run(["/usr/bin/openssl", "ecparam", "-name", "prime256v1", "-genkey", "-noout",
                    "-out", str(key)], check=True, capture_output=True)
    subprocess.run(["/usr/bin/openssl", "ec", "-in", str(key), "-pubout", "-out",
                    str(lib_paths.approver_pem)], check=True, capture_output=True)
    return key


def fake_assertion(key, manifest_bytes, rp="diwai-repair", flags=UP | UV, cdh=None):
    """The four lines fido2-assert -G writes, made with a software key."""
    cdh = cdh or hashlib.sha256(manifest_bytes).digest()
    auth = hashlib.sha256(rp.encode()).digest() + bytes([flags]) + (7).to_bytes(4, "big")
    sig = subprocess.run(["/usr/bin/openssl", "dgst", "-sha256", "-sign", str(key)],
                         input=auth + cdh, capture_output=True, check=True).stdout
    b64 = lambda b: base64.b64encode(b).decode()
    return f"{b64(cdh)}\n{rp}\n{b64(bytes([0x58, len(auth)]) + auth)}\n{b64(sig)}\n"


def approve_with(paths, repair_id, key, **kw):
    from repairkit import signing
    m = signing.manifest(paths, repair_id)
    (paths.approvals / f"{repair_id}.manifest").write_bytes(m)
    (paths.approvals / f"{repair_id}.assertion").write_text(fake_assertion(key, m, **kw))


DEMO = '''
ID = "demo-fix"; TITLE = "Demo fix"; HOST = "mac"; CARD = "DEMO"
SAY_NO_IF = "never"; MANUAL_RESTORE = "copy demo.bak back to demo.txt"
def check(ctx):
    return "change demo.txt" if ctx.target.read_text() == "bad" else None
def backup(ctx):
    ctx.save_backup("demo.txt", ctx.target.read_bytes())
def apply(ctx):
    ctx.target.write_text(ctx.options.get("apply_text", "good"))
def verify(ctx):
    from repairkit.context import RepairFailed
    if ctx.target.read_text() != "good":
        raise RepairFailed("demo.txt is not good")
def undo(ctx):
    ctx.target.write_bytes(ctx.load_backup("demo.txt"))
'''
