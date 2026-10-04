"""diwai-diagnose: read-only diagnosis. Collect -> findings -> explanation -> forms -> case record.
Never uses sudo, never runs a repair; writes only ~/diwai-rag/cases/."""
import subprocess
import sys
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

import cards
from diagnose import case, findings as fnd, form, interpret, repairs_index, vm_fetch
from diagnose.report import load_report

ROOT = Path(__file__).resolve().parents[1]
INSTALLED = Path("/usr/local/lib/diwai-repair/repairs")


def _real_deps():
    from diagnose import mac_checks   # imported here so the rest of the tool loads without it
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    try:
        lst = subprocess.run(["/usr/local/bin/diwai-repair", "list"], capture_output=True, text=True, timeout=60)
        repair_list = lst.stdout if lst.returncode == 0 else ""
    except (OSError, subprocess.TimeoutExpired):
        repair_list = ""
    return {"now": now, "mac": lambda: mac_checks.collect(now=now), "vm": vm_fetch.fetch_vm_report,
            "repair_list": repair_list, "installed": INSTALLED, "transport": None,
            "cases": ROOT / "cases", "out": None}


def main(argv=None, deps=None):
    d = deps or _real_deps()
    raw = d["out"].append if d.get("out") is not None else print

    def say(text):
        raw(form.clean(text))
    reports, notes = [d["mac"]()], []
    vm_text, vm_note = d["vm"]()
    if vm_text is None:
        notes.append(vm_note)
    else:
        reports.append(load_report(vm_text, "services", d["now"]))
    mapping = fnd.load_map(ROOT / "diagnose" / "findings_map.toml")
    found, gaps = fnd.evaluate(reports, mapping, set(cards.ids()))
    for n in notes:
        say(n)
    if not found and not gaps:
        say("Nothing found. " + "; ".join(f"{r.host} report from {r.time}" for r in reports))
        case.write_case(d["cases"], {"reports": [asdict(r) for r in reports], "findings": [], "gaps": [],
                                     "notes": notes}, "Nothing found.\n")
        return 0
    card_objs = {f.code: cards.load(f.code) for f in found}
    gaps += [f"no runbook card could be read: {c}" for c, k in card_objs.items() if k is None]
    found = [f for f in found if card_objs[f.code] is not None]
    allowed = repairs_index.allowed_repairs(d["installed"], d["repair_list"])
    res = interpret.interpret(found, card_objs, allowed, transport=d.get("transport"))
    if res["note"]:
        say(res["note"])
    text = "".join(form.render(f, card_objs[f.code], res["per_finding"][f.code]) for f in found)
    if gaps:
        text += "\nCHECKS WITH NO RUNBOOK CARD YET\n" + "".join(f"  - {g}\n" for g in gaps)
    say(text)
    case.write_case(d["cases"], {"reports": [asdict(r) for r in reports], "findings": [asdict(f) for f in found],
                                 "gaps": gaps, "notes": notes, "model": res}, text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
