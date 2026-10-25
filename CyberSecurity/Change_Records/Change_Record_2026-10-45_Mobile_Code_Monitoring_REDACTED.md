> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MOBILE-CODE MONITORING: WEEKLY REVIEW STEP AND MAC FILE INTEGRITY
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-45** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§3). Owner approved Parts A and B 2026-10-24.** |
| **System** | Mac host (Wazuh agent configuration); `DIWAI-SCH-001`; `DIWAI-MCP-001` |
| **Addresses** | **3.13.13** [b] (use of mobile code is monitored) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Part A: weekly review step (procedure)

`DIWAI-SCH-001` v1.2, row W1: a mobile-code step. It reads the week's file-integrity alerts (VM `/var/www`; Mac Nextcloud `apps`, `core`, `themes`), compares `occ app:list` with the previous week's saved list (Evidence `DIWAI-EV-MC-<date>`), checks the editors' versions against the SBOM, and records the result in the ledger. The dashboard files that change by design (`backup-status.json`, `index.html`, `compliance.html`, `morning-digest.json`) are skipped. `DIWAI-MCP-001` §4 now describes this monitoring and keeps the browser-side limit.

**First run (baseline), 2026-10-24:** 123 integrity alerts on `/var/www` in 7 days: 122 modifications of the generated files and one added backup copy (covered by `DIWAI-CR-2026-10-41`); 57 Nextcloud apps listed (52 enabled, 5 disabled) as `DIWAI-EV-MC-2026-10-24`; `richdocuments` 9.1.0 and ONLYOFFICE Desktop 10.0.0 match the SBOM. Logged in the ledger as W1.

## 2. Part B: Mac file integrity (configuration)

`/Library/Ossec/etc/ossec.conf` (Mac agent): added `/opt/local/nextcloud/apps`, `/opt/local/nextcloud/core`, `/opt/local/nextcloud/themes` (about 35,000 files) to the checked paths. Backup `/Library/Ossec/etc/ossec.conf.bak-20261024-1049-cr45`. The agent also already checks Nextcloud's `config` and the group-folder data (set by the manager's shared agent settings), so the application's code, configuration and data are all covered. The scan frequency in force is hourly (the manager's shared setting), not the local file's twelve hours.

## 3. Verification

- The agent restarted cleanly, connected, and the baseline of the new paths completed in 20 seconds.
- **First test (marker created, agent restarted):** no alert. A scan started by a restart does not report to the manager. Recorded, not hidden.
- **Second test (marker created, left to the scheduled hourly scan):** the manager raised **rule 554, "File added to the system", for agent `[USERNAME]s-Mac-mini.local`, at 11:51:00**, about 52 minutes after the file was created. The marker was then removed; a "deleted" alert is expected at the next scan and matches this record.
- Scripts: `scripts/fim/mac-fim-nextcloud.sh`, `scripts/fim/mac-fim-proof2.sh`; outputs kept beside them.

## 4. Limits and a finding

- Detection is hourly, not instant. A change is flagged at the next hourly scan.
- Scripts that run inside the browser, and content-security-policy violations, remain unmonitored (stated in MCP-001 §4).
- **Found, not changed:** the manager's log shows `custom-virustotal` integration errors ("Unable to run integration", exit status 4) at 10:14 today, on the file-added and file-changed alerts. The VirusTotal lookups on those events may not be running. Needs the owner's attention; it is separate from this change.

## 5. Rollback

`sudo cp -p /Library/Ossec/etc/ossec.conf.bak-20261024-1049-cr45 /Library/Ossec/etc/ossec.conf && sudo /Library/Ossec/bin/wazuh-control restart`. Part A: revert `DIWAI-SCH-001` to v1.1 and `DIWAI-MCP-001` §4 from `.bak-20261024-cr45`.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
