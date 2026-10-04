"""An approval is the ISSO's YubiKey assertion (PIN + touch) over a manifest:
the SHA-256 of every file the repair runs (its module, its data, and the shared
kit). Checked with root-owned tools only: this module, /usr/bin/python3 and
/usr/bin/openssl. The signing tool (fido2-assert) is never trusted to check.

What fido2-assert -G writes (one value per line): client data hash (base64),
relying party id, authenticator data (base64 of a CBOR byte string),
signature (base64, DER). The signature covers authenticator data || client
data hash. Authenticator data = SHA-256(rp id) | flags | counter."""
import base64
import binascii
import hashlib
import re
import subprocess
import tempfile
from pathlib import Path

FLAG_UP = 0x01   # user present: the key was touched
FLAG_UV = 0x04   # user verified: the PIN was given
VALID_ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")   # plain names only: no paths, no dots


def valid_id(repair_id):
    return bool(VALID_ID.match(repair_id or ""))


def module_name(repair_id):
    return repair_id.replace("-", "_")


def _files(paths, repair_id):
    mod = module_name(repair_id)
    files = sorted(paths.kit.glob("*.py"))
    command = paths.lib / "bin" / "diwai-repair"
    if command.is_file():
        files.append(command)       # the approval covers the command itself too
    files.append(paths.repairs / f"{mod}.py")
    data = paths.repairs / f"{mod}.data"
    if data.is_dir():
        files += sorted(p for p in data.rglob("*") if p.is_file())
    return files


def manifest(paths, repair_id):
    lines = []
    for f in sorted(_files(paths, repair_id), key=lambda p: str(p.relative_to(paths.lib))):
        digest = hashlib.sha256(f.read_bytes()).hexdigest()
        lines.append(f"{digest}  {f.relative_to(paths.lib)}\n")
    return "".join(lines).encode()


def assert_input(paths, manifest_bytes, credid):
    """The input file fido2-assert -G reads."""
    cdh = base64.b64encode(hashlib.sha256(manifest_bytes).digest()).decode()
    return f"{cdh}\n{paths.rp_id}\n{credid.strip()}\n"


def sign_command(paths, device, in_file, out_file):
    """-p: the key must be touched. -v: the PIN must be given."""
    return [paths.fido_assert, "-G", "-p", "-v", "-i", str(in_file), "-o", str(out_file), device]


def _cbor_bytes(data):
    head = data[0]
    if 0x40 <= head <= 0x57:
        return data[1:1 + head - 0x40]
    if head == 0x58:
        return data[2:2 + data[1]]
    if head == 0x59:
        return data[3:3 + int.from_bytes(data[1:3], "big")]
    raise ValueError("authenticator data is not a CBOR byte string")


def check_assertion(paths, manifest_bytes, assertion_text, pem=None):
    """(ok, reason) for one assertion over MANIFEST_BYTES, checked against PEM
    (default: the installed approver key)."""
    bad = (False, "The approval signature is not valid.")
    try:
        lines = assertion_text.split("\n")
        cdh = base64.b64decode(lines[0], validate=True)
        rp = lines[1]
        auth = _cbor_bytes(base64.b64decode(lines[2], validate=True))
        sig = base64.b64decode(lines[3], validate=True)
    except (IndexError, ValueError, binascii.Error):
        return bad
    if len(auth) < 37:
        return bad
    if rp != paths.rp_id or auth[:32] != hashlib.sha256(paths.rp_id.encode()).digest():
        return False, "The approval signature was not made for repair approvals."
    if cdh != hashlib.sha256(manifest_bytes).digest():
        return bad
    flags = auth[32]
    if not flags & FLAG_UP:
        return False, "The approval was signed without a touch on the YubiKey."
    if not flags & FLAG_UV:
        return False, "The approval was signed without the YubiKey PIN."
    with tempfile.TemporaryDirectory() as tmp:
        sig_file = Path(tmp) / "sig"
        sig_file.write_bytes(sig)
        r = subprocess.run([paths.openssl, "dgst", "-sha256", "-verify", str(pem or paths.approver_pem),
                            "-signature", str(sig_file)], input=auth + cdh, capture_output=True,
                           env={"PATH": "/usr/bin:/bin"})
    if r.returncode != 0:
        return bad
    return True, "approved"


def verify(paths, repair_id):
    if not valid_id(repair_id):
        return False, f"'{repair_id}' is not a valid repair name."
    if not (paths.repairs / f"{module_name(repair_id)}.py").is_file():
        return False, f"Repair '{repair_id}' is not installed."
    if not paths.approver_pem.is_file():
        return False, "The approver's public key file is missing, so no approval can be checked."
    m = paths.approvals / f"{repair_id}.manifest"
    a = paths.approvals / f"{repair_id}.assertion"
    if not (m.is_file() and a.is_file()):
        return False, f"Repair '{repair_id}' has not been approved."
    current = manifest(paths, repair_id)
    if m.read_bytes() != current:
        return False, f"Repair '{repair_id}' has changed since it was approved. It must be approved again."
    ok, why = check_assertion(paths, current, a.read_text())
    if not ok:
        return False, f"Repair '{repair_id}': {why}"
    return True, "approved"
