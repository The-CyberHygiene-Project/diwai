"""Runbook cards: one short page per finding, in the idm-assistant format
(approved 2026-10-03) plus diwai's one extension, the `objectives:` line.

The header fills the reader's view by code; no model writes any of it. Two
views of the same card: wrapped terminal text and a low-vision HTML page.
Cards are written for people who are not trained system administrators:
the seven plain fields carry no paths, commands or product jargon; those
belong in the technical note after `---`.

CLI:  cards.py show <CARD_ID> [--html OUT.html]
      cards.py book OUT.html          every card on one page, for review
"""
import argparse
import html
import os
import re
import shutil
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_DIR = Path(__file__).resolve().parent / "runbooks"
FIELDS = ("user_sees", "means", "evidence", "repair", "if_wrong", "rollback", "say_no_if")
ID_RE = re.compile(r"[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+")
OBJECTIVE_RE = re.compile(r"3\.(?:1[0-4]|[1-9])\.\d{1,2}(?:\[[a-z]\])?")

MIN_WIDTH, MAX_WIDTH = 40, 72
MAX_PLAIN_WORDS = 35
# Words a non-administrator can't act on. Extend as cards are written.
JARGON = (
    "389-ds", "ldap", "ldaps", "selinux", "fapolicyd", "chrony", "chronyd",
    "systemd", "systemctl", "sshd", "pam", "faillock", "nginx", "apache",
    "wazuh", "suricata", "luks", "totp", "fips", "aci", "lastlogintime",
    "sudo", "uid", "gid", "daemon", "launchd", "launchagent", "launchdaemon",
    "plist", "utm", "occ", "certbot", "openssl", "pf",
)
COMMAND_RE = re.compile(r"`|\$\s|^\s*(sudo|systemctl|chmod|chown|rm|kill)\b", re.I | re.M)
PATH_RE = re.compile(r"(?:^|\s)~?/[\w.@-]+/")


@dataclass(frozen=True)
class Card:
    finding: str
    default_repair: object  # str | None
    excerpt: str
    decisions: list = field(default_factory=list)
    objectives: list = field(default_factory=list)
    user_sees: str = ""
    means: str = ""
    evidence: str = ""
    repair: str = ""
    if_wrong: str = ""
    rollback: str = ""
    say_no_if: str = ""

    @property
    def complete(self):
        return all(getattr(self, f).strip() for f in FIELDS)

    @property
    def title(self):
        return self.finding.replace("_", " ").capitalize()


def _list(value):
    return [v.strip() for v in value.split(",") if v.strip()]


def ids(directory=None):
    d = Path(directory or DEFAULT_DIR)
    return sorted(p.stem for p in d.glob("*.md") if ID_RE.fullmatch(p.stem))


def load(finding_id, directory=None):
    p = Path(directory or DEFAULT_DIR) / f"{finding_id}.md"
    if not p.is_file():
        return None
    text = p.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        text = text[4:]
    head, _, body = text.partition("\n---\n")
    meta = {k.strip(): v.strip() for k, v in
            (line.split(":", 1) for line in head.splitlines() if ":" in line)}
    d = meta.get("default_repair", "")
    return Card(
        finding=finding_id,
        default_repair=None if d in ("", "none") else d,
        excerpt=body.strip(),
        decisions=_list(meta.get("decisions", "")),
        objectives=_list(meta.get("objectives", "")),
        **{f: meta.get(f, "") for f in FIELDS},
    )


def valid_objective(text):
    return bool(OBJECTIVE_RE.fullmatch(text))


def decision_numbers(register_path):
    nums = set()
    for line in Path(register_path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|", line)
        if m:
            nums.add(m.group(1))
    return nums


def plain_language_problems(card):
    """Expert language in the seven plain fields (not the technical note)."""
    problems = []
    for f in FIELDS:
        text = getattr(card, f)
        words = re.findall(r"[\w@.-]+", text.lower())
        if PATH_RE.search(text):
            problems.append(f"{f}: file path")
        if COMMAND_RE.search(text):
            problems.append(f"{f}: command")
        hits = sorted({w.strip(".") for w in words} & set(JARGON))
        if hits:
            problems.append(f"{f}: jargon ({', '.join(hits)})")
        if len(text.split()) > MAX_PLAIN_WORDS:
            problems.append(f"{f}: too long ({len(text.split())} words)")
    return problems


# ---- shared wording -----------------------------------------------------------

SECTIONS = (
    ("PROBLEM DETECTED", "What you may notice"),
    ("LIKELY CAUSE", "What the check found"),
    ("PROPOSED ACTION", "What to do"),
    ("POTENTIAL DOWNSIDE", "What could go wrong"),
    ("SAY NO IF", "Stop and say no if this is true"),
)
NO_CHANGE = "Nothing on the system is changed by this card."
OBJECTIVES_LABEL = "Requirement checked (NIST SP 800-171A)"
TECH_LABEL = "Technical note (for the administrator)"


def _decisions_line(card):
    if not card.decisions:
        return ""
    noun = "decision" if len(card.decisions) == 1 else "decisions"
    return f"Follows owner {noun} {', '.join(card.decisions)}."


def _section_bodies(card):
    action = [card.repair] + ([NO_CHANGE] if card.default_repair is None else [])
    return [
        [card.user_sees, "Why it matters: " + card.means],
        [card.evidence],
        action,
        ["If it is wrong: " + card.if_wrong, "Undo: " + card.rollback],
        [card.say_no_if],
    ]


# ---- terminal view ------------------------------------------------------------

def render_text(card, width=None, color=False):
    if width is None:
        width = shutil.get_terminal_size((MAX_WIDTH, 24)).columns - 1
    width = max(MIN_WIDTH, min(MAX_WIDTH, width))
    bold = (lambda s: f"\x1b[1m{s}\x1b[0m") if color else (lambda s: s)

    def para(text, indent="   "):
        return textwrap.fill(" ".join(str(text).split()), width,
                             initial_indent=indent, subsequent_indent=indent)

    def heading(text):
        return [bold(line) for line in textwrap.wrap(text, width)]

    out = ["", "=" * width, *heading(card.title.upper()), "=" * width]
    for (name, hint), body in zip(SECTIONS, _section_bodies(card)):
        mark = "!! " if name == "SAY NO IF" else ""
        out += ["", *heading(f"{mark}{name} - {hint}")]
        out += [para(b) for b in body]
    out += ["", *heading("REFERENCE")]
    out.append(para(f"{OBJECTIVES_LABEL}: {', '.join(card.objectives) or 'none'}"))
    if card.decisions:
        out.append(para(_decisions_line(card)))
    out.append(para(f"Card: {card.finding}"))
    out += ["", "-" * width, *heading("TECHNICAL NOTE (for the administrator)")]
    out.append(para(card.excerpt))
    out.append("")
    return "\n".join(out)


# ---- HTML view ----------------------------------------------------------------

CSS = """
:root { --bg:#ffffff; --fg:#111111; --muted:#3d3d3d; --rule:#767676;
        --stop-bg:#fff4e5; --stop-edge:#8a3b00; --card:#f4f4f4; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#121212; --fg:#f2f2f2; --muted:#cfcfcf; --rule:#9a9a9a;
          --stop-bg:#2e1f0f; --stop-edge:#ffb066; --card:#1e1e1e; }
}
html { font-size: 22px; }
body { background:var(--bg); color:var(--fg); margin:0; padding:1rem 16px 3rem;
       font-family:-apple-system, "Helvetica Neue", Arial, sans-serif; line-height:1.6; }
main { max-width:36em; margin:0 auto; }
h1 { font-size:1.6rem; line-height:1.25; margin:.5rem 0 1.5rem; }
h2 { font-size:1.1rem; margin:0 0 .4rem; letter-spacing:.02em; }
h2 .hint { display:block; font-weight:normal; color:var(--muted); font-size:.95rem; letter-spacing:0; }
section { border-left:6px solid var(--rule); padding:.2rem 0 .2rem 1rem; margin:0 0 1.6rem; }
section p { margin:.3rem 0; }
section.stop { border:4px solid var(--stop-edge); background:var(--stop-bg);
               padding:.8rem 1rem; border-radius:6px; }
section.stop h2::before { content:"\\26D4\\FE0E  "; }
section.ref { border-left-style:dotted; color:var(--muted); }
.label { font-weight:bold; }
details { background:var(--card); border-radius:6px; padding:.6rem 1rem; }
summary { cursor:pointer; font-weight:bold; min-height:44px; display:flex; align-items:center; }
code { font-size:.95em; }
a { color:inherit; text-underline-offset:.2em; }
ol.toc li { margin:.5rem 0; }
.hint { color:var(--muted); }
article { border-top:4px solid var(--rule); margin-top:3rem; padding-top:1rem; }
@media print { body { padding:0; } details { display:block; } }
"""


def _p(text):
    e = html.escape(text)
    for label in ("Why it matters:", "If it is wrong:", "Undo:"):
        if e.startswith(label):
            e = f'<span class="label">{label}</span>{e[len(label):]}'
    return f"<p>{e}</p>"


def _card_sections(card):
    parts = []
    for (name, hint), body in zip(SECTIONS, _section_bodies(card)):
        cls = ' class="stop"' if name == "SAY NO IF" else ""
        parts.append(
            f'<section{cls}><h2>{name.capitalize()}<span class="hint">{html.escape(hint)}</span></h2>'
            + "".join(_p(b) for b in body) + "</section>")
    ref = [f'<p><span class="label">{OBJECTIVES_LABEL}:</span> '
           f'{html.escape(", ".join(card.objectives) or "none")}</p>']
    if card.decisions:
        ref.append(_p(_decisions_line(card)))
    ref.append(f"<p>Card: <code>{html.escape(card.finding)}</code></p>")
    parts.append('<section class="ref"><h2>Reference</h2>' + "".join(ref) + "</section>")
    parts.append(f"<details><summary>{TECH_LABEL}</summary>"
                 f"<p>{html.escape(card.excerpt)}</p></details>")
    return "\n".join(parts)


def _page(title, body):
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{html.escape(title)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n<main>\n"
        + body + "\n</main>\n</body>\n</html>\n"
    )


def render_html(card):
    return _page(card.title, f"<h1>{html.escape(card.title)}</h1>\n" + _card_sections(card))


def render_book_html(card_list, title="Runbook cards"):
    """Every card on one page, with a contents list, for review."""
    toc = "".join(
        f'<li><a href="#{html.escape(c.finding)}">{html.escape(c.title)}</a>'
        f' <span class="hint">({html.escape(", ".join(c.objectives))})</span></li>'
        for c in card_list)
    articles = "".join(
        f'<article id="{html.escape(c.finding)}"><h1>{html.escape(c.title)}</h1>\n'
        f"{_card_sections(c)}\n<p><a href=\"#contents\">Back to contents</a></p></article>"
        for c in card_list)
    body = (f'<h1 id="contents">{html.escape(title)}</h1>\n'
            f'<p>{len(card_list)} cards.</p><nav><ol class="toc">{toc}</ol></nav>\n{articles}')
    return _page(title, body)


# ---- CLI ----------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    show = sub.add_parser("show")
    show.add_argument("card_id")
    show.add_argument("--html", metavar="OUT")
    book = sub.add_parser("book", help="every card on one HTML page")
    book.add_argument("out")
    args = ap.parse_args(argv)

    if args.cmd == "book":
        cards_ = [load(i, DEFAULT_DIR) for i in ids(DEFAULT_DIR)]
        Path(args.out).write_text(render_book_html(cards_), encoding="utf-8")
        print(f"Wrote {args.out} ({len(cards_)} cards)")
        return 0

    card = load(args.card_id, DEFAULT_DIR)
    if card is None:
        print(f"No card named {args.card_id} in {DEFAULT_DIR}", file=sys.stderr)
        return 1
    if args.html:
        Path(args.html).write_text(render_html(card), encoding="utf-8")
        print(f"Wrote {args.html}")
        return 0
    color = sys.stdout.isatty() and "NO_COLOR" not in os.environ
    print(render_text(card, color=color))
    return 0


if __name__ == "__main__":
    sys.exit(main())
