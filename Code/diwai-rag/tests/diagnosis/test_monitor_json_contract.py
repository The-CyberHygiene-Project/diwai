import json
import pytest
from diagnose.report import load_report

GOOD = {"host": "services", "time": "2026-10-04T11:00:33-06:00", "monitor_version": "abc123def456",
        "checks": [{"id": "11", "name": "Audit warning path", "status": "ok", "detail": ""}]}


def test_contract_accepts_the_spec_shape():
    r = load_report(json.dumps(GOOD), expect_host="services", now="2026-10-04T11:05:00-06:00")
    assert r.ok and r.checks[0].status == "ok"


@pytest.mark.parametrize("bad", [
    {**GOOD, "checks": [{"id": "11", "name": "x", "status": "maybe", "detail": ""}]},
    {k: v for k, v in GOOD.items() if k != "time"},
    {**GOOD, "checks": "not a list"},
])
def test_contract_rejects_other_shapes(bad):
    r = load_report(json.dumps(bad), expect_host="services", now="2026-10-04T11:05:00-06:00")
    assert not r.ok
