default_repair: wazuh-ruleset-missing
decisions: 13
objectives: 3.14.6[b], 3.3.5[a]
user_sees: Usually nothing. The security monitor runs, but some of its own alerts never arrive.
means: Warnings this system was set up to raise (malware found, audit logging failing, an incident report) would stay silent, so a real problem could go unnoticed.
evidence: The security monitor's settings do not list the folder that holds this system's own alert rules, so it never reads them.
repair: Put back the approved rules section in the security monitor's settings, test the settings, restart the monitor, then send one labelled test message and check that its alert appears.
if_wrong: The security monitor stops for about a minute while it restarts. If the settings test fails, nothing is restarted and the change is put back.
rollback: The repair's undo puts the previous settings file back from the backup (kept on the virtual server and on the Mac) and restarts the monitor.
say_no_if: Someone is changing the security monitor's settings by hand right now.
---
Status as of 2026-10-04. Before 2026-09-13 `/var/ossec/etc/ossec.conf` on the VM had no `<ruleset>` block, so only the stock ruleset loaded: `etc/rules` and `etc/decoders` were never read and the YARA (100200-209), audit (100220-225), inactivity (100222-224) and incident (100230) rules could not fire. The block was restored that day and is present now (`diwai-repair check wazuh-ruleset-missing` → nothing to do). Repair `wazuh-ruleset-missing` restores the approved 15-line block, runs `wazuh-analysisd -t`, restarts `wazuh-manager` only if that passes, then sends `logger -t diwai-incident` with a unique marker and requires rule 100230 in `alerts.json` within 60 s (proven live 2026-10-04: 2 s; level 10, mail false). The config test alone is not proof (lesson of 2026-09-13). Note: VM sudo is passwordless for [USERNAME] (`/etc/sudoers.d/[USERNAME]`), so this repair's VM steps do not prompt.
