"""Every card in runbooks/ is in the approved shape (idm-assistant format,
approved 2026-10-03, plus diwai's one extension: the objectives line)."""
import cards
from pathlib import Path

DIR = cards.DEFAULT_DIR


def test_there_are_cards():
    assert cards.ids(DIR)


def test_every_card_has_every_field():
    for fid in cards.ids(DIR):
        c = cards.load(fid, DIR)
        missing = [f for f in cards.FIELDS if not getattr(c, f).strip()]
        assert not missing, f"{fid} lacks {missing}"
        assert c.excerpt, f"{fid} has no text after ---"


def test_every_card_names_valid_objectives():
    for fid in cards.ids(DIR):
        c = cards.load(fid, DIR)
        assert c.objectives, f"{fid} names no objectives"
        bad = [o for o in c.objectives if not cards.valid_objective(o)]
        assert not bad, f"{fid}: {bad}"


def test_every_cited_decision_is_in_the_register():
    known = cards.decision_numbers(DIR / "DECISIONS.md")
    for fid in cards.ids(DIR):
        unknown = set(cards.load(fid, DIR).decisions) - known
        assert not unknown, f"{fid} cites unknown decisions {unknown}"


def test_readme_and_register_are_not_cards():
    assert (DIR / "README.md").is_file() and (DIR / "DECISIONS.md").is_file()
    assert not {"README", "DECISIONS"} & set(cards.ids(DIR))


def test_every_card_is_in_plain_words():
    for fid in cards.ids(DIR):
        problems = cards.plain_language_problems(cards.load(fid, DIR))
        assert not problems, f"{fid}: {problems}"


def test_every_card_objective_exists_in_800_171a():
    import objectives
    known = objectives.load()["objectives"]
    for fid in cards.ids(DIR):
        unknown = [o for o in cards.load(fid, DIR).objectives if o not in known]
        assert not unknown, f"{fid} names objectives not in 800-171A: {unknown}"


def test_every_default_repair_exists():
    repairs = Path(__file__).resolve().parents[1] / "repairs"
    for fid in cards.ids(DIR):
        rid = cards.load(fid, DIR).default_repair
        if rid is not None:
            assert (repairs / (rid.replace("-", "_") + ".py")).is_file(), f"{fid}: unknown repair {rid}"
