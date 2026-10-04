import pytest


@pytest.fixture(autouse=True)
def never_reach_real_services(monkeypatch):
    """No diagnose unit test may reach the real LM Studio, the VM or diwai-repair
    (lesson of 2026-10-04: a test reached the real YubiKey)."""
    import requests

    def forbidden(*a, **kw):
        raise AssertionError("unit test reached a real service")
    monkeypatch.setattr(requests, "post", forbidden)
    monkeypatch.setattr(requests, "get", forbidden)
