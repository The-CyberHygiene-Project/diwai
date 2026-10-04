"""ISSO and installer commands. Both need the administrator password (sudo);
approve also needs the YubiKey (PIN + touch)."""
import hashlib
import subprocess
import tempfile
from pathlib import Path

from repairkit import signing

SOURCE = Path.home() / "diwai-rag"
APPROVER_DIR = Path.home() / ".config" / "diwai"
FIDO_TOKEN = "/opt/homebrew/bin/fido2-token"
# Spoken in the order the key asks: PIN first, then touch (owner, 2026-10-04:
# the earlier wording asked for the touch before the PIN prompt appeared).
SPOKEN_PROMPT = "Type your YubiKey PIN, then touch the key when it blinks."


def fido_pins_text(paths):
    """SHA-256 of the signing tool and the library it loads. Both live in
    Homebrew's folder, which the owner's account can change, so approve
    refuses if either differs from what was recorded at install."""
    import os
    lines = []
    for f in (paths.fido_assert, paths.fido_lib):
        real = os.path.realpath(f)
        with open(real, "rb") as fh:
            lines.append(f"{hashlib.sha256(fh.read()).hexdigest()}  {real}\n")
    return "".join(lines)


def _sudo(shell, argv):
    r = shell.mac(argv, sudo=True)
    if r.returncode != 0:
        raise OSError(f"{' '.join(argv)}: {r.stderr or r.stdout}")


def _owner(shell, mode):
    return ["-m", mode] + (["-o", "root", "-g", "wheel"] if shell.sudo_prefix else [])


def _prove_with_yubikey(pem, credid):
    """The approver key is trusted only after the YubiKey signs a fresh random
    challenge (PIN + touch) that checks out against it."""
    import os
    import secrets
    from repairkit.paths import PRODUCTION
    device = _device()
    if not device:
        return False
    challenge = secrets.token_bytes(32)
    with tempfile.TemporaryDirectory() as tmp:
        i, a = Path(tmp) / "in", Path(tmp) / "out"
        i.write_text(signing.assert_input(PRODUCTION, challenge, credid))
        print("Proving the approver key: enter your YubiKey PIN when asked, then touch the YubiKey.")
        subprocess.run(["/usr/bin/say", SPOKEN_PROMPT], capture_output=True)
        if subprocess.run(signing.sign_command(PRODUCTION, device, i, a)).returncode != 0 or not a.is_file():
            return False
        return signing.check_assertion(PRODUCTION, challenge, a.read_text(), pem=pem)[0]


def _export(src_root, dest):
    """The committed tree only (git archive HEAD): uncommitted edits are never
    installed, and what is installed has a commit id to review."""
    commit = subprocess.run(["git", "-C", str(src_root), "rev-parse", "HEAD"],
                            capture_output=True, text=True, check=True).stdout.strip()
    subject = subprocess.run(["git", "-C", str(src_root), "log", "-1", "--format=%cs %s"],
                             capture_output=True, text=True, check=True).stdout.strip()
    tar = subprocess.run(["git", "-C", str(src_root), "archive", commit, "repairkit", "repairs", "bin"],
                         capture_output=True, check=True).stdout
    subprocess.run(["/usr/bin/tar", "-x", "-C", str(dest)], input=tar, check=True)
    return commit, subject


def install(src_root, paths, shell, approver_dir=None, out=print, prove_approver=None):
    """Copy the committed, reviewed source into the root-owned library. The
    approver's public key is set on first install only, after it proves it is
    the YubiKey; replacing it later is a deliberate, manual act."""
    approver_dir = APPROVER_DIR if approver_dir is None else approver_dir
    prove_approver = prove_approver or _prove_with_yubikey
    pem, credid = approver_dir / "repair-approver.pem", approver_dir / "repair-approver.credid"
    new_approver = not paths.approver_pem.exists() and pem.is_file() and credid.is_file()
    if new_approver:
        if not prove_approver(pem, credid.read_text()):
            out("Not installed: the approver key did not prove it belongs to the YubiKey. Nothing was changed.")
            return 1
    with tempfile.TemporaryDirectory() as tmp:
        tree = Path(tmp)
        commit, subject = _export(src_root, tree)
        links = [p for p in tree.rglob("*") if p.is_symlink()]
        if links:
            out("Not installed: the source contains links to other files "
                f"({', '.join(str(p.relative_to(tree)) for p in links)}). Nothing was changed.")
            return 1
        files = sorted((tree / "repairkit").glob("*.py")) + sorted(
            p for p in (tree / "repairs").rglob("*")
            if p.is_file() and "__pycache__" not in p.parts and not p.name.endswith(".pyc"))
        for d in (paths.lib, paths.kit, paths.repairs, paths.approvals, paths.lib / "bin"):
            _sudo(shell, ["/usr/bin/install", "-d"] + _owner(shell, "755") + [str(d)])
        _sudo(shell, ["/usr/bin/install", "-d"] + _owner(shell, "700") + [str(paths.runs)])
        for f in files:
            dest = paths.lib / f.relative_to(tree)
            _sudo(shell, ["/usr/bin/install", "-d"] + _owner(shell, "755") + [str(dest.parent)])
            _sudo(shell, ["/usr/bin/install"] + _owner(shell, "644") + [str(f), str(dest)])
        _sudo(shell, ["/usr/bin/install"] + _owner(shell, "755") +
              [str(tree / "bin" / "diwai-repair"), str(paths.lib / "bin" / "diwai-repair")])
        pins = tree / "fido-tools.sha256"
        pins.write_text(fido_pins_text(paths))
        _sudo(shell, ["/usr/bin/install"] + _owner(shell, "644") + [str(pins), str(paths.fido_pins)])
        stamp = tree / "INSTALLED_FROM"
        stamp.write_text(f"{commit} {subject}\n")
        _sudo(shell, ["/usr/bin/install"] + _owner(shell, "644") + [str(stamp), str(paths.lib / "INSTALLED_FROM")])
    if new_approver:
        for src, dest in ((pem, paths.approver_pem), (credid, paths.approver_credid)):
            _sudo(shell, ["/usr/bin/install"] + _owner(shell, "644") + [str(src), str(dest)])
        digest = hashlib.sha256(pem.read_bytes()).hexdigest()
        out(f"Approver key installed. Record its SHA-256 in the change record: {digest}")
    if shell.sudo_prefix:
        _sudo(shell, ["/bin/ln", "-sf", str(paths.lib / "bin" / "diwai-repair"), "/usr/local/bin/diwai-repair"])
    out(f"Installed from commit {commit[:12]} ({subject}).")
    for p in sorted(paths.repairs.glob("*.py")):
        rid = p.stem.replace("_", "-")
        ok, why = signing.verify(paths, rid)
        out(f"{rid:28s} {'approved' if ok else why}")
    return 0


def _device():
    r = subprocess.run([FIDO_TOKEN, "-L"], capture_output=True, text=True)
    first = r.stdout.splitlines()[0] if r.stdout.strip() else ""
    return first.split(": ", 1)[0]


def approve(repair_id, paths, shell, device=None, out=print):
    if not signing.valid_id(repair_id):
        out(f"Not approved: '{repair_id}' is not a valid repair name.")
        return 1
    if not (paths.repairs / f"{signing.module_name(repair_id)}.py").is_file():
        out(f"Not approved: repair '{repair_id}' is not installed.")
        return 1
    try:
        pinned_ok = paths.fido_pins.read_text() == fido_pins_text(paths)
    except OSError:
        pinned_ok = False
    if not pinned_ok:
        out("Not approved: the YubiKey signing tool (or its library) has changed since install, or was "
            "never recorded. If you updated it with Homebrew, check the update, then run: diwai-repair install")
        return 1
    device = _device() if device is None else device
    if not device:
        out("Not approved: no YubiKey found. Is it plugged in?")
        return 1
    data = signing.manifest(paths, repair_id)
    stamp = paths.lib / "INSTALLED_FROM"
    origin = stamp.read_text().strip() if stamp.is_file() else "unknown (no install record)"
    out(f"Approving '{repair_id}', installed from commit {origin}.\n"
        f"Approve only if that commit is the one you reviewed. Files and fingerprints:\n{data.decode()}")
    with tempfile.TemporaryDirectory() as tmp:
        m, i, a = Path(tmp) / f"{repair_id}.manifest", Path(tmp) / "in", Path(tmp) / f"{repair_id}.assertion"
        m.write_bytes(data)
        i.write_text(signing.assert_input(paths, data, paths.approver_credid.read_text()))
        out("Enter your YubiKey PIN when asked. Then touch the YubiKey.")
        shell.say(SPOKEN_PROMPT)
        r = subprocess.run(signing.sign_command(paths, device, i, a))
        if r.returncode != 0 or not a.is_file():
            out("Not approved: the YubiKey did not sign (wrong PIN, no touch within 30 seconds, "
                "or key unplugged). Nothing was changed. You can try again.")
            return 1
        ok, why = signing.check_assertion(paths, data, a.read_text())
        if not ok:
            out(f"Not approved: {why} Nothing was changed.")
            return 1
        for f in (m, a):
            _sudo(shell, ["/usr/bin/install"] + _owner(shell, "644") + [str(f), str(paths.approvals / f.name)])
    ok, why = signing.verify(paths, repair_id)
    out(f"'{repair_id}': {'approved' if ok else why}")
    return 0 if ok else 1


def main(cmd, args, paths):
    from repairkit.shell import Shell
    shell = Shell(speaker=lambda text: subprocess.run(["/usr/bin/say", text], capture_output=True))
    if cmd == "install" and not args:
        return install(SOURCE, paths, shell)
    if cmd == "approve" and len(args) == 1:
        return approve(args[0], paths, shell)
    print("usage: diwai-repair approve <repair> | install")
    return 2
