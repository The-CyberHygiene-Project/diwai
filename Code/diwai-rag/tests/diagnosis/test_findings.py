from diagnose.findings import evaluate, load_map
from diagnose.report import Check, Report
from pathlib import Path

M = {("mac", "owui-cors"): ("OPEN_WEBUI_ACCEPTS_ANY_ORIGIN", "warn"),
     ("services", "7"): ("HEALTH_CHECK_WARNINGS_UNREAD", "warn"),
     ("services", "8"): ("HEALTH_CHECK_WARNINGS_UNREAD", "warn"),
     ("services", "9"): ("NO_SUCH_CARD", "fail")}
CARDS = {"OPEN_WEBUI_ACCEPTS_ANY_ORIGIN", "HEALTH_CHECK_WARNINGS_UNREAD", "MONITOR_REPORT_STALE",
         "MONITOR_REPORT_UNREADABLE"}


def rep(host, *checks, ok=True, problem=""):
    return Report(host, "t", [Check(i, f"check {i}", s, f"detail {i}") for i, s in checks], ok, problem)


def test_failed_mapped_check_is_a_finding():
    f, g = evaluate([rep("mac", ("owui-cors", "fail"))], M, CARDS)
    assert [x.code for x in f] == ["OPEN_WEBUI_ACCEPTS_ANY_ORIGIN"] and g == []


def test_ok_checks_give_nothing():
    assert evaluate([rep("mac", ("owui-cors", "ok"))], M, CARDS) == ([], [])


def test_unmapped_failure_is_a_gap():
    f, g = evaluate([rep("services", ("42", "fail"))], M, CARDS)
    assert f == [] and "services" in g[0] and "42" in g[0]


def test_mapped_finding_without_card_file_is_a_gap():
    f, g = evaluate([rep("services", ("9", "fail"))], M, CARDS)
    assert f == [] and "NO_SUCH_CARD" in g[0]


def test_one_form_per_host_and_finding():
    f, g = evaluate([rep("services", ("7", "fail"), ("8", "warn"))], M, CARDS)
    assert len(f) == 1 and f[0].check_ids == ["7", "8"] and f[0].severity == "fail"


def test_same_check_reported_twice_counts_once_per_finding():
    f, g = evaluate([rep("services", ("7", "fail"), ("7", "fail"))], M, CARDS)
    assert len(f) == 1 and f[0].check_ids == ["7"] and len(f[0].details) == 2


def test_stale_report_is_its_own_finding():
    f, g = evaluate([rep("services", ok=False, problem="stale: …")], M, CARDS)
    assert f[0].code == "MONITOR_REPORT_STALE"


def test_unreadable_report_is_its_own_finding():
    f, g = evaluate([rep("services", ok=False, problem="the report is unreadable")], M, CARDS)
    assert f[0].code == "MONITOR_REPORT_UNREADABLE"


def test_shipped_map_only_names_existing_cards():
    import cards
    m = load_map(Path(__file__).resolve().parents[2] / "diagnose" / "findings_map.toml")
    have = set(cards.ids())
    assert m and all(code in have for code, _ in m.values())
