import json
from diagnose.report import load_report


def doc(**kw):
    d = {"host": "services", "time": "2026-10-04T11:00:00-0600", "monitor_version": "x",
         "checks": [{"id": "1", "name": "a", "status": "fail", "detail": "d"}]}
    d.update(kw)
    return json.dumps(d)


def test_fresh_report_loads():
    r = load_report(doc(), "services", "2026-10-04T11:10:00-06:00")
    assert r.ok and r.checks[0].status == "fail"


def test_old_report_is_stale():
    r = load_report(doc(), "services", "2026-10-04T11:31:00-06:00")
    assert not r.ok and r.problem.startswith("stale")


def test_report_from_wrong_host_or_future_is_not_trusted():
    assert not load_report(doc(host="other"), "services", "2026-10-04T11:05:00-06:00").ok
    r = load_report(doc(time="2026-10-04T12:00:00-0600"), "services", "2026-10-04T11:05:00-06:00")
    assert not r.ok and "future" in r.problem


def test_garbage_is_unreadable_not_a_crash():
    r = load_report("not json {", "services", "2026-10-04T11:05:00-06:00")
    assert not r.ok and "unreadable" in r.problem


def test_both_time_formats_are_read():
    assert load_report(doc(time="2026-10-04T11:00:00-06:00"), "services", "2026-10-04T11:05:00-0600").ok
