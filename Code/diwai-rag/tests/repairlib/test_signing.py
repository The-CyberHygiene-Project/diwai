import subprocess
from repairkit import signing
from repairlib.helpers import approve_with, UP, UV


def test_manifest_lists_kit_and_repair_with_hashes(lib_paths):
    text = signing.manifest(lib_paths, "demo-fix").decode()
    assert "  repairs/demo_fix.py\n" in text and "  repairkit/paths.py\n" in text
    assert all(len(line.split("  ")[0]) == 64 for line in text.splitlines())


def test_approved_repair_verifies(lib_paths, soft_key):
    approve_with(lib_paths, "demo-fix", soft_key)
    assert signing.verify(lib_paths, "demo-fix") == (True, "approved")


def test_missing_approval_is_refused(lib_paths, soft_key):
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "not been approved" in why


def test_not_installed_is_refused(lib_paths, soft_key):
    ok, why = signing.verify(lib_paths, "no-such-fix")
    assert not ok and "not installed" in why


def test_repair_edited_after_approval_is_refused(lib_paths, soft_key):
    approve_with(lib_paths, "demo-fix", soft_key)
    f = lib_paths.repairs / "demo_fix.py"
    f.write_text(f.read_text() + "\n# edited\n")
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "changed since it was approved" in why


def test_shared_helper_edited_after_approval_is_refused(lib_paths, soft_key):
    approve_with(lib_paths, "demo-fix", soft_key)
    (lib_paths.kit / "paths.py").write_text((lib_paths.kit / "paths.py").read_text() + "# tampered\n")
    assert signing.verify(lib_paths, "demo-fix")[0] is False


def test_manifest_and_signature_both_swapped_is_refused(lib_paths, soft_key, tmp_path):
    """An attacker rewrites the stored manifest to match edited files: the signature no longer fits."""
    approve_with(lib_paths, "demo-fix", soft_key)
    sig = (lib_paths.approvals / "demo-fix.assertion").read_text()
    f = lib_paths.repairs / "demo_fix.py"; f.write_text(f.read_text() + "# edited\n")
    (lib_paths.approvals / "demo-fix.manifest").write_bytes(signing.manifest(lib_paths, "demo-fix"))
    (lib_paths.approvals / "demo-fix.assertion").write_text(sig)
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "signature" in why


def test_wrong_signer_is_refused(lib_paths, soft_key, tmp_path):
    other = tmp_path / "other.key"
    subprocess.run(["/usr/bin/openssl", "ecparam", "-name", "prime256v1", "-genkey", "-noout",
                    "-out", str(other)], check=True, capture_output=True)
    approve_with(lib_paths, "demo-fix", other)
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "signature" in why


def test_approval_without_pin_is_refused(lib_paths, soft_key):
    approve_with(lib_paths, "demo-fix", soft_key, flags=UP)
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "PIN" in why


def test_approval_without_touch_is_refused(lib_paths, soft_key):
    approve_with(lib_paths, "demo-fix", soft_key, flags=UV)
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "touch" in why


def test_approval_for_another_purpose_is_refused(lib_paths, soft_key):
    approve_with(lib_paths, "demo-fix", soft_key, rp="ssh:")
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "not made for repair approvals" in why


def test_missing_approver_key_is_refused(lib_paths, soft_key):
    approve_with(lib_paths, "demo-fix", soft_key)
    lib_paths.approver_pem.unlink()
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "approver's public key" in why


def test_garbled_assertion_is_refused_not_crashing(lib_paths, soft_key):
    approve_with(lib_paths, "demo-fix", soft_key)
    (lib_paths.approvals / "demo-fix.assertion").write_text("not base64 at all\n!!\n")
    ok, why = signing.verify(lib_paths, "demo-fix")
    assert not ok and "not valid" in why
