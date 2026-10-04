# Runbook card format

Adopted 2026-10-03 from The CyberHygiene Project's idm-assistant runbook format (approved by its ISSO the same day),
with **one diwai extension: the `objectives:` line** (owner approved 2026-10-03). Only the format is shared; no
technical content crosses between the two projects.

One short card per finding (`<FINDING_ID>.md`, upper case, words joined by `_`). The header fills the reader's view
**by code** (`cards.py`); no model writes any line of it. The text after `---` is the technical note the model reads.
`tests/test_runbook_shape.py` enforces this format for every card.

## Who reads a card

**Cards are written for people who are not trained system administrators.** The seven plain fields say what the
person notices, why it matters, and what to do, in everyday words. Paths, commands, product names and protocol
names belong in the technical note, which is labelled "for the administrator" and folded away in the HTML view.

## Layout

```
default_repair: <repair id, or none>
decisions: <owner decision numbers from DECISIONS.md this card depends on, or empty>
objectives: <NIST SP 800-171A objectives this card concerns, e.g. 3.5.6[a], 3.5.6[b]>
user_sees: <PROBLEM DETECTED: what the person notices>
means: <why it matters: who loses what>
evidence: <LIKELY CAUSE: what the check found, in plain words>
repair: <PROPOSED ACTION; for none: "No automatic repair." + what a person does instead>
if_wrong: <POTENTIAL DOWNSIDE: what happens if this is the wrong call>
rollback: <Undo: how it is undone, or "Cannot be undone" and why>
say_no_if: <SAY NO IF: the one situation where the right answer is no>
---
<technical note: a few sentences; technical terms, paths and commands allowed>
```

## How a card is shown

The same card has two views, built by `cards.py`; the sections come in the order of the decision form.

| View | Command | Designed for |
| --- | --- | --- |
| Terminal | `venv/bin/python cards.py show <ID>` | A quick look. Wraps to the window width (40–72 columns), one label per line, blank line between sections, "SAY NO IF" marked `!!` as well as bold (never colour alone; `NO_COLOR` respected). |
| HTML page | `venv/bin/python cards.py show <ID> --html out.html` | Reading at length. Self-contained (no network), 22 px base type, high contrast in light and dark, lines about 36 em, "Say no if" in a heavy bordered box, technical note folded away. |

| Field | Shown as |
| --- | --- |
| `user_sees` + `means` | PROBLEM DETECTED (What you may notice), then "Why it matters" |
| `evidence` | LIKELY CAUSE (What the check found) |
| `repair` | PROPOSED ACTION (What to do); a `none` card adds "Nothing on the system is changed by this card." |
| `if_wrong` + `rollback` | POTENTIAL DOWNSIDE (What could go wrong): "If it is wrong", then "Undo" |
| `say_no_if` | SAY NO IF (Stop and say no if this is true) |
| `objectives`, `decisions` | REFERENCE: "Requirement checked (NIST SP 800-171A)", "Follows owner decision N." |
| text after `---` | TECHNICAL NOTE (for the administrator) |

## Rules

1. **Plain words.** Write for a person who is not a system administrator. Every line must be something they can act
   on. The format test rejects paths, commands, listed jargon and fields over 35 words in the seven plain fields.
2. **Written from the repair's code, not from memory.** Read the repair's precheck, backup, apply and undo before
   writing `repair`, `if_wrong` and `rollback`. Claim nothing the code does not do.
3. **Say when a repair cannot be undone, and why.**
4. **No-repair cards** (`default_repair: none`) say what a person does instead, and when not to.
5. **Follow the owner's decisions.** A card whose advice depends on one names it in `decisions`, and its text must
   agree with it. Every cited number must exist in `DECISIONS.md`.
6. **Name the objectives.** Every card names at least one SP 800-171A objective (`3.x.y` or `3.x.y[z]`).
7. **Use the live values.** Numbers from a host's configuration must match what is configured there. A card states
   the date its facts were last checked.
8. **Every new repair ships with two tests:** a case where the right answer is no repair (the model must decline or
   the code must refuse), and a case where the evidence carries an injected instruction that must be ignored.
9. **Wording is reviewed by the ISSO before it is published.**

## Review record

| Date | Reviewer | Cards | Result |
|:---|:---|:---|:---|
| 2026-10-03 | [SYSTEM-OWNER], ISSO | All 13 cards in this folder | **Approved without change** (rule 9). `DECISIONS.md` was not part of this review. |
| 2026-10-03 | [SYSTEM-OWNER], owner | `DECISIONS.md`, rows 1-12 | **Confirmed, agreed without change** |
| 2026-10-03 | [SYSTEM-OWNER], owner | `DECISIONS.md`, rows 9, 10, 11, 12 | **Signed 2026-10-03** (at the owner's direction; row 10's memo DIWAI-MFR-2026-09-24 signed the same day) |
| 2026-10-04 | [SYSTEM-OWNER], ISSO | `OPEN_WEBUI_ACCEPTS_ANY_ORIGIN`, `WAZUH_CUSTOM_RULES_NOT_LOADED` (first cards naming a real repair) | **Approved without change** (rule 9) |
