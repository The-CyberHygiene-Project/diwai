"""Fixed rules: failed checks -> finding codes (= runbook card names). No model involved."""
import tomllib
from dataclasses import dataclass, field


@dataclass
class Finding:
    code: str
    host: str
    check_ids: list = field(default_factory=list)
    severity: str = "warn"
    details: list = field(default_factory=list)


def load_map(path):
    with open(path, "rb") as fh:
        rows = tomllib.load(fh).get("map", [])
    return {(r["host"], str(r["check"])): (r["finding"], r.get("severity", "warn")) for r in rows}


def evaluate(reports, mapping, card_ids):
    """(findings, gaps): one Finding per (host, code); failures without a card are gaps."""
    found, gaps = {}, []
    for rep in reports:
        if not rep.ok:
            code = "MONITOR_REPORT_STALE" if rep.problem.startswith("stale") else "MONITOR_REPORT_UNREADABLE"
            if code not in card_ids:
                gaps.append(f"no runbook card yet: {code} ({rep.host}): {rep.problem}")
                continue
            found[(rep.host, code)] = Finding(code, rep.host, [], "fail", [rep.problem])
            continue
        for c in rep.checks:
            if c.status == "ok":
                continue
            hit = mapping.get((rep.host, c.id))
            if hit is None:
                gaps.append(f"no runbook card yet: {rep.host} check {c.id} ({c.name}) is {c.status}: {c.detail}")
                continue
            code, sev = hit
            if code not in card_ids:
                gaps.append(f"no runbook card yet: {code} ({rep.host} check {c.id}) is {c.status}")
                continue
            f = found.setdefault((rep.host, code), Finding(code, rep.host, [], sev, []))
            if c.id not in f.check_ids:
                f.check_ids.append(c.id)
            f.details.append(f"{c.name}: {c.detail}" if c.detail else c.name)
            if c.status == "fail":
                f.severity = "fail"
    return list(found.values()), gaps
