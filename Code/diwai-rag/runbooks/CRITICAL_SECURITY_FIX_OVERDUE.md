default_repair: none
decisions: 3
objectives: 3.11.3[a], 3.11.3[b]
user_sees: A critical security fix has been waiting more than three days since it was found.
means: Critical flaws are the ones attackers use first. Every day the fix waits, that way in stays open.
evidence: The weekly flaw scan lists a critical fix that is not installed yet, and it was first found more than three days ago.
repair: No automatic repair. The owner installs the fix, or writes down why it must wait and what protects the system in the meantime.
if_wrong: An update can occasionally break a service, and without a fresh backup that service may stay down.
rollback: Nothing is changed by this card. Before installing, the owner confirms a fresh backup exists, which is the way back.
say_no_if: Someone proposes switching on fully automatic updates to keep up. The owner chose to review each update before it is installed.
---
Status as of 2026-09-15 (owner decision 3; DIWAI-PR-001 v1.2 §6/§6.1). Critical: 72 hours from detection, the clock start defined in §6.1 (F-2026-09-04). Routine patching is monthly. `dnf-automatic` on the VM is download-only (`apply_updates = no`), an accepted deviation in SSP Appendix E.3; updates are operator-applied and logged in DIWAI-PR-LOG. Note for the owner: SSP v2.18 rows 3.7.1 and 3.11.3 still say "weekly review" and give IMPORTANT a 7-day window; reconcile with decision 3.
