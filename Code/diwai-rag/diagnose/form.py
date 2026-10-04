"""The decision form, built by code from the runbook card. The model's text is labelled as the model's."""
import re
import textwrap

# Terminal escape sequences, then any other control character (C0, DEL, C1). Text from the model
# or the VM could otherwise hide lines, move the cursor or forge a "To fix:" line.
_ESC = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]|\x1b[@-_]")
_CTRL = re.compile(r"[\x00-\x08\x0b-\x1f\x7f-\x9f]")
MODEL = "   model| "          # every line of the model's words carries this, so none can pose as a form line
FOUND = "   found| "          # the same for what the checks reported


def clean(text):
    """Text safe for the terminal: escape sequences and control characters removed, newlines and tabs kept."""
    return _CTRL.sub("", _ESC.sub("", str(text)))


def _w(text, indent="   "):
    return textwrap.fill(" ".join(clean(text).split()), 76, initial_indent=indent, subsequent_indent=indent)


def render(finding, card, choice):
    bar = "=" * 76
    lines = ["", bar, f" {finding.code} on {finding.host}", bar,
             " PROBLEM", _w(card.user_sees), _w("Why it matters: " + card.means), "",
             " LIKELY CAUSE", _w(card.evidence)]
    if finding.details:
        lines.append(_w(f"Found on {finding.host}: " + "; ".join(finding.details), FOUND))
    if choice.get("analysis"):
        lines += ["", f" EXPLANATION (from the local model, confidence {choice['confidence']})",
                  _w(choice["analysis"], MODEL)]
    if choice.get("note"):
        lines += ["", _w("Note: " + choice["note"])]
    lines += ["", " PROPOSED ACTION", _w(card.repair), "", " POTENTIAL DOWNSIDE",
              _w("If it is wrong: " + card.if_wrong), _w("Undo: " + card.rollback), "",
              " SAY NO IF", _w(card.say_no_if), "-" * 76]
    if choice.get("repair"):
        lines.append(f"To fix: diwai-repair run {clean(choice['repair'])}")
    else:
        lines.append("What to do: no approved repair fits. Follow PROPOSED ACTION or ask the ISSO.")
    return "\n".join(lines) + "\n"
