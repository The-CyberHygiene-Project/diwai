default_repair: none
decisions: 13
objectives: 3.14.6[b]
user_sees: The diagnosis says the security self-check's latest report is more than half an hour old.
means: The self-check normally runs every 15 minutes. An old report means it may have stopped, so problems it watches for could go unnoticed.
evidence: The newest report from the self-check on the virtual server is older than 30 minutes.
repair: No automatic repair. Check that the virtual server is running and that its self-check timer is active, then run the diagnosis again.
if_wrong: Looking does no harm. Restarting the virtual server to clear this can interrupt mail and the directory for a few minutes.
rollback: Looking changes nothing. A restart of the virtual server cannot be undone, but it puts back what was running before.
say_no_if: Someone proposes switching the self-check off because its reports are late. Find out why it stopped instead.
---
Status as of 2026-10-04 (diagnosis loop design, DIWAI-CR-2026-10-09). `diwai-control-health.timer` runs the monitor every 15 minutes; each run writes `/var/lib/diwai-control-health/latest.json`. `diwai-diagnose` treats a report older than 30 minutes as stale. Check with `systemctl list-timers diwai-control-health.timer` and `journalctl -u diwai-control-health.service` on the VM. Remember the VM halts at its LUKS prompt after any reboot (it cannot recover unattended).
