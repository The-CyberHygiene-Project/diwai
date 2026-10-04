"""Monitor reports: one shape for the VM's latest.json and the Mac collector."""
import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta

STALE = timedelta(minutes=30)
FUTURE = timedelta(minutes=5)
STATUSES = {"ok", "warn", "fail"}


@dataclass
class Check:
    id: str
    name: str
    status: str
    detail: str = ""


@dataclass
class Report:
    host: str
    time: str
    checks: list = field(default_factory=list)
    ok: bool = True
    problem: str = ""


def _t(text):
    """ISO time with offset, either -06:00 or -0600 (the monitor writes the latter)."""
    try:
        t = datetime.fromisoformat(text)
    except ValueError:
        t = datetime.strptime(text, "%Y-%m-%dT%H:%M:%S%z")
    if t.tzinfo is None:                 # no offset: cannot be compared, so it is unreadable
        raise ValueError("time without an offset")
    return t


def load_report(text, expect_host, now):
    try:
        d = json.loads(text)
        checks = [Check(str(c["id"]), str(c["name"]), c["status"], str(c.get("detail", "")))
                  for c in d["checks"]]
        if any(c.status not in STATUSES for c in checks):
            raise ValueError("bad status")
        when, now_t = _t(d["time"]), _t(now)
    except (ValueError, KeyError, TypeError, IndexError, AttributeError):
        return Report(expect_host, "", [], False, "the report is unreadable")
    if d.get("host") != expect_host:
        return Report(expect_host, d.get("time", ""), [], False,
                      f"the report is unreadable: it is from {d.get('host')!r}, not {expect_host!r}")
    if when - now_t > FUTURE:
        return Report(expect_host, d["time"], checks, False, "the report's time is in the future")
    if now_t - when > STALE:
        return Report(expect_host, d["time"], checks, False,
                      f"stale: the report is from {d['time']} (the monitor may have stopped)")
    return Report(expect_host, d["time"], checks, True, "")
