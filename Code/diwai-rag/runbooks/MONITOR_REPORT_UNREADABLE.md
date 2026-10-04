default_repair: none
decisions: 13
objectives: 3.14.6[b]
user_sees: The diagnosis says it could not read the security self-check's latest report.
means: Without that report, the diagnosis cannot tell whether the virtual server's protections are working.
evidence: The report was missing, damaged, from another computer, or dated in the future.
repair: No automatic repair. Note what the diagnosis said, check the virtual server's clock and the self-check, then run the diagnosis again.
if_wrong: Looking does no harm. Deleting the report by hand hides the evidence of what went wrong.
rollback: Looking changes nothing. The next self-check run writes a fresh report.
say_no_if: Someone proposes trusting the old report anyway. A report that cannot be read must not be treated as good news.
---
Status as of 2026-10-04 (DIWAI-CR-2026-10-09). `load_report` marks the report unreadable when the JSON is invalid, a status is unknown, the host is not `services`, or the time is more than 5 minutes in the future (clock drift: see the VM clock-guard history). The file is `/var/lib/diwai-control-health/latest.json`, written atomically by the monitor.
