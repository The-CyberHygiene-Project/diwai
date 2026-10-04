import unicodedata

from webapp import library


def test_apfs_key_ignores_case_and_unicode_form():
    nfd = unicodedata.normalize("NFD", "Résumé.txt")
    nfc = unicodedata.normalize("NFC", "résumé.TXT")
    assert library.apfs_key(nfd) == library.apfs_key(nfc)
    assert library.apfs_key("Report.PDF") == library.apfs_key("report.pdf")


def test_safe_name_strips_directories_and_control_characters():
    assert library.safe_name("../../x.txt") == "x.txt"
    assert library.safe_name("a\\b\\c.txt") == "c.txt"
    assert library.safe_name("bad\x00na\x1fme.md") == "badname.md"
    assert library.safe_name("..") == "unnamed"
    assert library.safe_name("") == "unnamed"


def test_choose_name_counts_up_until_free():
    taken = {library.apfs_key(n) for n in ("notes.txt", "Notes (2).txt")}
    assert library.choose_name("NOTES.txt", taken) == "NOTES (3).txt"
    assert library.choose_name("fresh.txt", taken) == "fresh.txt"


def test_choose_name_keeps_long_names_within_the_filesystem_limit():
    long = "x" * 260 + ".txt"
    name = library.choose_name(long, set())
    assert len(name.encode("utf-8")) <= 255 and name.endswith(".txt")
    taken = {library.apfs_key(name)}
    second = library.choose_name(long, taken)
    assert second != name and len(second.encode("utf-8")) <= 255 and "(2)" in second


def test_supported_extension_is_case_insensitive():
    assert library.supported("A.TXT") and library.supported("b.Pdf")
    assert not library.supported("c.exe") and not library.supported("noext")


def test_filter_is_literal_and_case_insensitive():
    rows = [{"source": n} for n in ("Plan [current].txt", "Plan (2).txt", "Plan.txt", "other.md")]
    got = lambda q: [r["source"] for r in library.filter_rows(rows, q)]
    assert got("[current]") == ["Plan [current].txt"]
    assert got("(2)") == ["Plan (2).txt"]
    assert got("PLAN") == ["Plan [current].txt", "Plan (2).txt", "Plan.txt"]
    assert got("") == [r["source"] for r in rows]
