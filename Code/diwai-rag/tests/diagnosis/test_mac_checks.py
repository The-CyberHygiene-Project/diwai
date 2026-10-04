import subprocess

import pytest

from diagnose import mac_checks

NOW = "2026-10-04T13:30:00-06:00"
AW_GOOD = "logger -s -p security.warning \"audit warning: $1\" ; echo x >> /var/log/diwai-audit-warn.log\n"
SS_GOOD = "<dict><key>rule</key><array><string>authenticate-session-owner</string></array></dict>"


def fake(**over):
    """A runner that answers each command like a healthy Mac, unless overridden by key."""
    good = {
        "cors": "HTTP/1.1 200 OK\r\n",
        "lmstudio": '{"data":[{"id":"x"}]}',
        "library": "406",
        "pf": "\tstate = not running\n\tlast exit code = 0\n",
        "tm": "/Volumes/.timemachine/X/2026-10-04-130721.backup/2026-10-04-130721.backup\n",
        "volume": "",
        "audit_warn": AW_GOOD,
        "screensaver": SS_GOOD,
        "cert": "notAfter=Nov  8 17:52:41 2026 GMT\n",
    }
    good.update(over)
    rc = {"volume": over.pop("volume_rc", 0)}

    def run(argv, **kw):
        a = " ".join(map(str, argv))
        key = ("cors" if "evil.example" in a else "lmstudio" if ":1234" in a else "library" if ":8767" in a
               else "pf" if "org.diwai.pf" in a else "tm" if "tmutil" in a else "volume" if "SecureMac" in a
               else "audit_warn" if "audit_warn" in a else "screensaver" if "screensaver" in a
               else "cert" if "x509" in a else None)
        assert key, f"unexpected command {a}"
        return subprocess.CompletedProcess(argv, rc.get(key, 0), good[key], "")
    return run


def statuses(**over):
    return {c.id: c.status for c in mac_checks.collect(runner=fake(**over), now=NOW).checks}


def test_healthy_mac_is_all_ok():
    s = statuses()
    assert set(s) == {"owui-cors", "lmstudio", "library", "pf", "tm-age", "tm-volume",
                      "mscp-audit-warn", "mscp-screensaver", "cert-expiry"}
    assert set(s.values()) == {"ok"}


@pytest.mark.parametrize("over,check", [
    ({"cors": "HTTP/1.1 200 OK\r\naccess-control-allow-origin: http://evil.example\r\n"}, "owui-cors"),
    ({"cors": "HTTP/1.1 200 OK\r\naccess-control-allow-origin: *\r\n"}, "owui-cors"),
    ({"lmstudio": ""}, "lmstudio"),
    ({"library": "000"}, "library"),
    ({"pf": "\tlast exit code = 1\n"}, "pf"),
    ({"tm": "/Volumes/.timemachine/X/2026-10-02-130721.backup/2026-10-02-130721.backup\n"}, "tm-age"),
    ({"tm": ""}, "tm-age"),
    ({"volume_rc": 1}, "tm-volume"),
    ({"audit_warn": "logger -p security.warning x\n"}, "mscp-audit-warn"),
    ({"audit_warn": "logger -s -p security.warning x\n"}, "mscp-audit-warn"),
    ({"screensaver": SS_GOOD.replace("authenticate-session-owner", "use-login-window-ui")}, "mscp-screensaver"),
    ({"cert": "notAfter=Oct 10 17:52:41 2026 GMT\n"}, "cert-expiry"),
])
def test_each_bad_condition_fails_its_own_check(over, check):
    s = statuses(**over)
    assert s[check] == "fail" and sum(v != "ok" for v in s.values()) == 1


def test_pf_without_a_last_exit_is_a_warning_not_a_silent_pass():
    assert statuses(pf="\tstate = not running\n")["pf"] == "warn"


def test_collector_never_uses_sudo():
    calls = []
    base = fake()

    def run(argv, **kw):
        calls.append(argv)
        return base(argv, **kw)
    mac_checks.collect(runner=run, now=NOW)
    assert not any("sudo" in " ".join(map(str, a)) for a in calls)


def test_report_shape():
    r = mac_checks.collect(runner=fake(), now=NOW)
    assert r.host == "mac" and r.ok and r.time == NOW
