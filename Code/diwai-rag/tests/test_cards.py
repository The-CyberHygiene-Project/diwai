import re

import pytest

import cards

GOOD = """default_repair: none
decisions: 2
objectives: 3.5.6[a], 3.5.6[b]
user_sees: Usually nothing; an idle account still works.
means: A forgotten account stays usable.
evidence: Local accounts have no inactivity limit.
repair: No automatic repair. Review local accounts by hand.
if_wrong: Disabling the break-glass account removes the way back in.
rollback: An administrator can re-enable a disabled account.
say_no_if: Someone proposes disabling accounts with no recorded login.
---
SSP E.4 defines 90 days. 389-DS enforces it.
"""


@pytest.fixture
def card_dir(tmp_path):
    (tmp_path / "INACTIVE_ACCOUNT_NOT_DISABLED.md").write_text(GOOD)
    (tmp_path / "README.md").write_text("# format")
    (tmp_path / "DECISIONS.md").write_text(
        "| No. | Date | Decision | Source |\n|---|---|---|---|\n"
        "| 1 | 2026-09-13 | Lower value | memo |\n| 2 | 2026-09-13 | Evidence strict | memo |\n")
    return tmp_path


def card(card_dir):
    return cards.load("INACTIVE_ACCOUNT_NOT_DISABLED", card_dir)


# ---- loading --------------------------------------------------------------

def test_load_reads_every_field(card_dir):
    c = card(card_dir)
    assert c.finding == "INACTIVE_ACCOUNT_NOT_DISABLED"
    assert c.default_repair is None
    assert c.decisions == ["2"]
    assert c.objectives == ["3.5.6[a]", "3.5.6[b]"]
    assert c.say_no_if.startswith("Someone proposes")
    assert c.excerpt == "SSP E.4 defines 90 days. 389-DS enforces it."
    assert c.complete


def test_missing_field_is_incomplete(card_dir):
    (card_dir / "PART_CARD.md").write_text("default_repair: none\nuser_sees: x\n---\nbody\n")
    assert not cards.load("PART_CARD", card_dir).complete


def test_unknown_card_is_none(card_dir):
    assert cards.load("NO_SUCH_CARD", card_dir) is None


def test_ids_are_upper_snake_files_only(card_dir):
    assert cards.ids(card_dir) == ["INACTIVE_ACCOUNT_NOT_DISABLED"]


def test_objective_syntax():
    assert cards.valid_objective("3.5.6[a]")
    assert cards.valid_objective("3.13.11[b]")
    assert cards.valid_objective("3.1.1")
    for bad in ("3.15.1[a]", "3.5", "AC-2", "3.5.6[A]", "3.5.6a"):
        assert not cards.valid_objective(bad), bad


def test_decision_numbers_come_from_the_register(card_dir):
    assert cards.decision_numbers(card_dir / "DECISIONS.md") == {"1", "2"}


# ---- terminal view --------------------------------------------------------

HEADINGS = ["PROBLEM DETECTED", "LIKELY CAUSE", "PROPOSED ACTION",
            "POTENTIAL DOWNSIDE", "SAY NO IF", "REFERENCE"]


def test_text_sections_in_decision_form_order(card_dir):
    out = cards.render_text(card(card_dir), width=72)
    assert [out.index(h) for h in HEADINGS] == sorted(out.index(h) for h in HEADINGS)


def test_text_carries_every_field_and_reference(card_dir):
    c = card(card_dir)
    flat = " ".join(cards.render_text(c, width=72).split())
    for f in cards.FIELDS:
        assert " ".join(getattr(c, f).split()) in flat, f
    assert "3.5.6[a], 3.5.6[b]" in flat
    assert "decision 2" in flat
    assert c.excerpt in flat


def test_text_wraps_to_narrow_window(card_dir):
    out = cards.render_text(card(card_dir), width=44)
    assert max(len(line) for line in out.splitlines()) <= 44


def test_text_width_has_a_floor(card_dir):
    out = cards.render_text(card(card_dir), width=10)
    assert max(len(line) for line in out.splitlines()) <= 40


def test_text_is_plain_unless_colour_asked(card_dir):
    assert "\x1b[" not in cards.render_text(card(card_dir), width=72)
    assert "\x1b[1m" in cards.render_text(card(card_dir), width=72, color=True)


def test_say_no_if_is_marked_without_relying_on_colour(card_dir):
    out = cards.render_text(card(card_dir), width=72)
    line = next(l for l in out.splitlines() if "SAY NO IF" in l)
    assert line.strip().startswith("!!")


def test_no_repair_card_says_nothing_changes(card_dir):
    assert "Nothing on the system is changed by this card" in cards.render_text(card(card_dir), width=72)


# ---- HTML view ------------------------------------------------------------

def test_html_sections_in_order_and_low_vision_basics(card_dir):
    page = cards.render_html(card(card_dir))
    labels = ["Problem detected", "Likely cause", "Proposed action",
              "Potential downside", "Say no if", "Reference"]
    assert [page.index(h) for h in labels] == sorted(page.index(h) for h in labels)
    assert '<html lang="en">' in page
    assert 'name="viewport"' in page
    assert "prefers-color-scheme: dark" in page
    assert re.search(r"font-size:\s*22px", page)


def test_html_is_self_contained(card_dir):
    page = cards.render_html(card(card_dir))
    assert not re.search(r'(src|href)\s*=\s*"https?:', page)
    assert "<script" not in page


def test_html_escapes_card_text(card_dir):
    (card_dir / "EVIL_CARD.md").write_text(GOOD.replace(
        "Usually nothing;", '<script>alert(1)</script> Usually nothing;'))
    page = cards.render_html(cards.load("EVIL_CARD", card_dir))
    assert "<script>alert(1)</script>" not in page
    assert "&lt;script&gt;" in page


def test_html_title_is_readable_words(card_dir):
    page = cards.render_html(card(card_dir))
    assert "<h1>Inactive account not disabled</h1>" in page


# ---- CLI ------------------------------------------------------------------

def test_cli_show_prints_card(card_dir, monkeypatch, capsys):
    monkeypatch.setattr(cards, "DEFAULT_DIR", card_dir)
    assert cards.main(["show", "INACTIVE_ACCOUNT_NOT_DISABLED"]) == 0
    assert "PROBLEM DETECTED" in capsys.readouterr().out


def test_cli_html_writes_page(card_dir, monkeypatch, tmp_path):
    monkeypatch.setattr(cards, "DEFAULT_DIR", card_dir)
    out = tmp_path / "card.html"
    assert cards.main(["show", "INACTIVE_ACCOUNT_NOT_DISABLED", "--html", str(out)]) == 0
    assert "Say no if" in out.read_text()


def test_cli_unknown_card_fails(card_dir, monkeypatch, capsys):
    monkeypatch.setattr(cards, "DEFAULT_DIR", card_dir)
    assert cards.main(["show", "NOPE_CARD"]) == 1
    assert "No card named NOPE_CARD" in capsys.readouterr().err


# ---- written for people who are not trained administrators ----------------

def test_text_headings_explain_themselves(card_dir):
    out = cards.render_text(card(card_dir), width=72)
    for phrase in ("What you may notice", "What the check found", "What to do",
                   "What could go wrong", "Stop and say no"):
        assert phrase in out, phrase


def test_technical_note_is_labelled_for_the_administrator(card_dir):
    out = cards.render_text(card(card_dir), width=72)
    assert "TECHNICAL NOTE (for the administrator)" in out
    assert out.index("SAY NO IF") < out.index("TECHNICAL NOTE")


def test_html_folds_the_technical_note_away(card_dir):
    page = cards.render_html(card(card_dir))
    assert "<details>" in page
    assert "<summary>Technical note (for the administrator)</summary>" in page


def test_plain_card_passes_the_plain_words_check(card_dir):
    assert cards.plain_language_problems(card(card_dir)) == []


@pytest.mark.parametrize("text, why", [
    ("Edit /etc/chrony.conf and restart.", "file path"),
    ("Run `systemctl restart chronyd`.", "command"),
    ("The 389-DS lastLoginTime attribute is stale.", "jargon"),
    (" ".join(["word"] * 36), "too long"),
])
def test_plain_words_check_catches_expert_language(card_dir, text, why):
    (card_dir / "HARD_CARD.md").write_text(GOOD.replace(
        "Local accounts have no inactivity limit.", text))
    problems = cards.plain_language_problems(cards.load("HARD_CARD", card_dir))
    assert any(why in p for p in problems), problems


def test_technical_note_may_use_expert_language(card_dir):
    (card_dir / "TECH_CARD.md").write_text(GOOD.replace(
        "SSP E.4 defines 90 days.", "Check /etc/dirsrv and `lastLoginTime` in 389-DS."))
    assert cards.plain_language_problems(cards.load("TECH_CARD", card_dir)) == []


# ---- all cards on one page (for review) ------------------------------------

def test_book_has_contents_linking_every_card(card_dir):
    (card_dir / "SECOND_CARD.md").write_text(GOOD)
    page = cards.render_book_html([cards.load(i, card_dir) for i in cards.ids(card_dir)])
    for fid in ("INACTIVE_ACCOUNT_NOT_DISABLED", "SECOND_CARD"):
        assert f'href="#{fid}"' in page and f'id="{fid}"' in page
    assert page.count("<h2>Problem detected") == 2
    assert page.index('href="#INACTIVE') < page.index('id="INACTIVE')


def test_book_is_self_contained_and_escaped(card_dir):
    (card_dir / "EVIL_CARD.md").write_text(GOOD.replace("Usually nothing;", "<b>x</b>"))
    page = cards.render_book_html([cards.load(i, card_dir) for i in cards.ids(card_dir)])
    assert "<b>x</b>" not in page and "<script" not in page
    assert '<html lang="en">' in page


def test_cli_book_writes_page(card_dir, monkeypatch, tmp_path):
    monkeypatch.setattr(cards, "DEFAULT_DIR", card_dir)
    out = tmp_path / "book.html"
    assert cards.main(["book", str(out)]) == 0
    assert 'href="#INACTIVE_ACCOUNT_NOT_DISABLED"' in out.read_text()
