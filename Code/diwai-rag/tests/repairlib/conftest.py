import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import pytest
from repairlib.helpers import lib_paths as _lib_paths, soft_key as _soft_key


@pytest.fixture
def lib_paths(tmp_path):
    return _lib_paths(tmp_path)


@pytest.fixture
def soft_key(tmp_path, lib_paths):
    return _soft_key(tmp_path, lib_paths)


@pytest.fixture(autouse=True)
def never_touch_real_hardware(tmp_path, monkeypatch):
    """No repair-library test may reach the real YubiKey, the owner's real key
    files, or the speaker. (2026-10-04: two install tests did, and the Mac asked
    the owner out loud to touch the key.)"""
    from repairkit import admin, shell

    def forbidden(*a, **kw):
        raise AssertionError("test reached the real YubiKey or speaker")
    empty = tmp_path / "no-approver"
    empty.mkdir()
    monkeypatch.setattr(admin, "APPROVER_DIR", empty)
    monkeypatch.setattr(admin, "_prove_with_yubikey", forbidden)
    monkeypatch.setattr(admin, "_device", forbidden)
    real_say = shell.Shell.say

    def guarded_say(self, text):
        if self.speaker is None:
            forbidden()
        return real_say(self, text)
    monkeypatch.setattr(shell.Shell, "say", guarded_say)
