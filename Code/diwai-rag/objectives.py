"""NIST SP 800-171A assessment objectives, parsed from the NIST PDF.

The list is committed as runbooks/objectives_171a.json (with the PDF's sha256)
so cards can be checked against real objectives and coverage can be reported.

CLI:  objectives.py build <NIST_SP_800-171A.pdf>   rebuild the JSON
      objectives.py coverage                        objectives with / without cards
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import cards

DEFAULT_PATH = cards.DEFAULT_DIR / "objectives_171a.json"
SOURCE_TITLE = "NIST SP 800-171A (June 2018), Assessing Security Requirements for CUI"

CONTROL_RE = re.compile(r"(3\.\d{1,2}\.\d{1,2})\s+SECURITY REQUIREMENT")
# Some headings put the number on the next line, after margin noise.
HEADING_ONLY_RE = re.compile(r"\s(SECURITY REQUIREMENT)\s*$")
BARE_NUMBER_RE = re.compile(r"\s(3\.\d{1,2}\.\d{1,2})\s*$")
MAX_MARGIN_NOISE = 6


def _alone(regex, line):
    """regex's match if it is the only thing on the line apart from the
    few characters of rotated margin text to its left."""
    m = regex.search(line)
    if m and len(line[:m.start(1)].strip()) <= MAX_MARGIN_NOISE:
        return m
    return None
LETTERED_RE = re.compile(r"(3\.\d{1,2}\.\d{1,2}\[[a-z]\])\s+(\S.*)")
SINGLE_RE = re.compile(r"Determine if\s+(?!:)(\S.*)")
PAGE_CHROME_RE = re.compile(r"PAGE \d+\s*$|ASSESSING SECURITY REQUIREMENTS FOR|^_{10,}")
END_MARKERS = ("POTENTIAL ASSESSMENT", "ASSESSMENT OBJECTIVE", "SECURITY REQUIREMENT")


def _tidy(text):
    return " ".join(re.sub(r"_{5,}", " ", text).split())


def parse(text):
    requirements, objs = {}, {}
    control = None
    target = None    # (dict, key) receiving continuation lines
    col = 0          # text column of the current entry; margin noise sits left of it
    heading_col = 0
    awaiting_number = False
    pending = ""     # lines after a finished objective: the next ID's opening words

    def finish():
        nonlocal pending
        if pending and target:
            d, k = target
            d[k] += " " + pending
        pending = ""

    for line in text.splitlines():
        if PAGE_CHROME_RE.search(line):
            continue
        m = CONTROL_RE.search(line)
        if m:
            finish()
            control = m.group(1)
            requirements[control] = ""
            target, col, awaiting_number = (requirements, control), m.start(1), False
            continue
        m = _alone(HEADING_ONLY_RE, line)
        if m:
            finish()
            awaiting_number, target, heading_col = True, None, m.start(1)
            continue
        if awaiting_number:
            m = _alone(BARE_NUMBER_RE, line)
            if m:
                control = m.group(1)
                requirements[control] = ""
                target, col, awaiting_number = (requirements, control), heading_col, False
                continue
            if len(line.strip()) > MAX_MARGIN_NOISE:
                raise ValueError(f"SECURITY REQUIREMENT heading without a number near: {line.strip()!r}")
            continue
        m = LETTERED_RE.search(line)
        if m:
            objs[m.group(1)] = (pending + " " + m.group(2)).strip()
            pending = ""
            target, col = (objs, m.group(1)), m.start(2)
            continue
        m = SINGLE_RE.search(line)
        if m and control:
            finish()
            objs[control] = m.group(1)
            target, col = (objs, control), m.start()
            continue
        if any(k in line for k in END_MARKERS) or "Determine if:" in line:
            finish()
            target = None
            continue
        if target:
            rest = _tidy(line[col:])
            if not rest:
                continue
            d, k = target
            if d is objs and "[" in k and _tidy(d[k]).endswith("."):
                # An ID can sit beside the 2nd line of its own text (vertically
                # centred), so words after a finished objective open the next one.
                pending = (pending + " " + rest).strip()
            else:
                d[k] = (d[k] + " " + rest).strip()
    finish()
    return {
        "requirements": {k: _tidy(v) for k, v in requirements.items()},
        "objectives": {k: _tidy(v) for k, v in objs.items()},
    }


def build(pdf_path, out_path=DEFAULT_PATH):
    text = subprocess.run(
        ["gs", "-q", "-dSAFER", "-dNOPAUSE", "-dBATCH", "-sDEVICE=txtwrite",
         "-sOutputFile=-", str(pdf_path)],
        capture_output=True, check=True, timeout=600,
    ).stdout.decode("utf-8", errors="replace")
    data = parse(text)
    data["source"] = {
        "title": SOURCE_TITLE,
        "file": Path(pdf_path).name,
        "sha256": hashlib.sha256(Path(pdf_path).read_bytes()).hexdigest(),
    }
    Path(out_path).write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    return data


def load(path=DEFAULT_PATH):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def coverage(cards_dir=None):
    covered = {}
    for fid in cards.ids(cards_dir):
        for oid in cards.load(fid, cards_dir).objectives:
            covered.setdefault(oid, []).append(fid)
    known = load()["objectives"]
    return {
        "covered": {k: v for k, v in covered.items() if k in known},
        "uncovered": [k for k in known if k not in covered],
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("pdf")
    sub.add_parser("coverage")
    args = ap.parse_args(argv)
    if args.cmd == "build":
        data = build(args.pdf)
        print(f"{len(data['requirements'])} requirements, "
              f"{len(data['objectives'])} objectives -> {DEFAULT_PATH}")
        return 0
    cov = coverage()
    total = len(cov["uncovered"]) + len(cov["covered"])
    print(f"{len(cov['covered'])} of {total} objectives have a card")
    for oid, fids in cov["covered"].items():
        print(f"  {oid:12} {', '.join(fids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
