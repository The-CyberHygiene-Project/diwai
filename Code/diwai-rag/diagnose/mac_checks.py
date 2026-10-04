"""The read-only Mac collector: things the VM's monitor cannot see. Never sudo.
Each check is one small function returning a Check; collect() runs them all."""
import re
import subprocess
from datetime import datetime, timedelta, timezone

from diagnose.report import Check, Report

TM_MAX_AGE = timedelta(hours=26)
CERT_MIN_LEFT = timedelta(days=14)
CERT = "/etc/ssl/diwai/[DOMAIN.ORG].crt"
AUDIT_WARN = "/etc/security/audit_warn"
FORWARD_LINE = "/var/log/diwai-audit-warn.log"      # the 3.3.4 line macOS updates drop (DIWAI-CR-2026-09-07)


def _run(runner, argv):
    try:
        return runner(argv, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return subprocess.CompletedProcess(argv, 1, "", str(exc))


def owui_cors(runner, now):
    r = _run(runner, ["/usr/bin/curl", "-s", "-m", "10", "-o", "/dev/null", "-D", "-",
                      "-H", "Origin: http://evil.example", "http://127.0.0.1:3000/api/version"])
    allowed = [ln.split(":", 1)[1].strip() for ln in r.stdout.replace("\r", "").splitlines()
               if ln.lower().startswith("access-control-allow-origin:")]
    bad = any(v in ("*", "http://evil.example") for v in allowed)
    if r.returncode != 0 or not r.stdout.strip():     # no answer is not an all-clear
        return Check("owui-cors", "Open WebUI lets only its own web address read its answers", "warn",
                     "Open WebUI did not answer, so this could not be checked")
    return Check("owui-cors", "Open WebUI lets only its own web address read its answers",
                 "fail" if bad else "ok", "another web site is allowed to read its answers" if bad else "")


def lmstudio(runner, now):
    r = _run(runner, ["/usr/bin/curl", "-s", "-m", "5", "http://127.0.0.1:1234/v1/models"])
    up = r.returncode == 0 and '"data"' in r.stdout
    return Check("lmstudio", "LM Studio (the local AI models) answers", "ok" if up else "fail",
                 "" if up else "no answer on this Mac's port 1234")


def library(runner, now):
    r = _run(runner, ["/usr/bin/curl", "-s", "-m", "5", "-o", "/dev/null", "-w", "%{http_code}",
                      "-X", "POST", "http://127.0.0.1:8767/mcp"])
    code = r.stdout.strip()
    up = code in ("200", "400", "406")       # any of these means the server is there and answering
    return Check("library", "The document library's search server answers", "ok" if up else "fail",
                 "" if up else f"no answer (HTTP {code or 'none'})")


def pf(runner, now):
    """pf's rules need root to read; its launcher's last run is visible. Never a silent pass."""
    r = _run(runner, ["/bin/launchctl", "print", "system/org.diwai.pf"])
    m = re.search(r"last exit code = (\S+)", r.stdout)
    if r.returncode != 0 or not r.stdout.strip():
        return Check("pf", "The firewall's loader ran", "fail", "the firewall loader is not installed")
    if not m:
        return Check("pf", "The firewall's loader ran", "warn",
                     "could not be confirmed without administrator rights")
    ok = m.group(1) == "0"
    return Check("pf", "The firewall's loader ran", "ok" if ok else "fail",
                 "" if ok else f"the loader's last run failed (exit code {m.group(1)})")


def tm_age(runner, now):
    r = _run(runner, ["/usr/bin/tmutil", "latestbackup"])
    m = re.search(r"(\d{4}-\d{2}-\d{2}-\d{6})\.backup", r.stdout)
    if not m:
        return Check("tm-age", "Time Machine backed up within the last day", "fail", "no backup found")
    taken = datetime.strptime(m.group(1), "%Y-%m-%d-%H%M%S").replace(tzinfo=now.tzinfo)
    old = now - taken > TM_MAX_AGE
    return Check("tm-age", "Time Machine backed up within the last day", "fail" if old else "ok",
                 f"last backup {taken:%Y-%m-%d %H:%M}")


def tm_volume(runner, now):
    ok = _run(runner, ["/bin/test", "-d", "/Volumes/SecureMac"]).returncode == 0
    return Check("tm-volume", "The backup disk is unlocked and mounted", "ok" if ok else "fail",
                 "" if ok else "the SecureMac backup disk is not mounted: backups stop until it is unlocked")


def mscp_audit_warn(runner, now):
    text = _run(runner, ["/bin/cat", AUDIT_WARN]).stdout
    has_s, has_fwd = "logger -s -p" in text, FORWARD_LINE in text
    ok = has_s and has_fwd
    missing = [w for w, h in (("the stderr warning", has_s), ("the forwarding to the security monitor", has_fwd))
               if not h]
    return Check("mscp-audit-warn", "Audit-failure warnings still reach a person (reset by macOS updates)",
                 "ok" if ok else "fail", "" if ok else "missing: " + " and ".join(missing))


def mscp_screensaver(runner, now):
    text = _run(runner, ["/usr/bin/security", "-q", "authorizationdb", "read", "system.login.screensaver"]).stdout
    ok = "<string>authenticate-session-owner</string>" in text
    return Check("mscp-screensaver", "Only the signed-in person can unlock their locked screen (reset by macOS updates)",
                 "ok" if ok else "fail", "" if ok else "any administrator can unlock another person's screen")


def cert_expiry(runner, now):
    r = _run(runner, ["/usr/bin/openssl", "x509", "-enddate", "-noout", "-in", CERT])
    m = re.search(r"notAfter=(.+)", r.stdout)
    if not m:
        return Check("cert-expiry", "The web certificate is valid for 14 more days", "fail", "could not be read")
    try:
        end = datetime.strptime(" ".join(m.group(1).split()), "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
    except ValueError:
        return Check("cert-expiry", "The web certificate is valid for 14 more days", "fail",
                     "could not be read (unexpected date format)")
    short = end - now < CERT_MIN_LEFT
    return Check("cert-expiry", "The web certificate is valid for 14 more days", "fail" if short else "ok",
                 f"expires {end:%Y-%m-%d}")


CHECKS = (owui_cors, lmstudio, library, pf, tm_age, tm_volume, mscp_audit_warn, mscp_screensaver, cert_expiry)


def collect(runner=subprocess.run, now=None):
    now = now or datetime.now().astimezone().isoformat(timespec="seconds")
    now_t = datetime.fromisoformat(now)
    return Report("mac", now, [_safe(check, runner, now_t) for check in CHECKS], True, "")


def _safe(check, runner, now_t):
    """One check that breaks fails alone; it never takes the whole diagnosis down."""
    try:
        return check(runner, now_t)
    except Exception as exc:
        return Check(check.__name__.replace("_", "-"), check.__name__, "fail",
                     f"the check itself failed ({type(exc).__name__})")
