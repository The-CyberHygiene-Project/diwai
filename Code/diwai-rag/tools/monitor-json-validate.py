#!/usr/bin/env python3
"""Validate the VM monitor's latest.json against the diagnose report contract.
Usage: ssh services cat /var/lib/diwai-control-health/latest.json | venv/bin/python tools/monitor-json-validate.py"""
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from diagnose.report import load_report  # noqa: E402

r = load_report(sys.stdin.read(), "services", datetime.now().astimezone().isoformat(timespec="seconds"))
print(("VALID" if r.ok else f"NOT VALID: {r.problem}") + f" — {len(r.checks)} check results, time {r.time}")
for c in r.checks:
    print(f"  {c.status:4s} {c.id:3s} {c.name}: {c.detail[:70]}")
sys.exit(0 if r.ok else 1)
