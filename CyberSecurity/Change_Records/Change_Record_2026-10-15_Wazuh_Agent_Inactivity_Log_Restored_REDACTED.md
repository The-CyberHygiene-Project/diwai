> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — WAZUH AGENT INACTIVITY-LOG COLLECTION RESTORED; VM NETWORK OUTAGE RECORDED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-15** |
| **Date opened** | October 18, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§6, Addenda A and B); owner approved 2026-10-18. One item open (§5.2, cause of the missing entry); the archive gap of §5.4 is recorded as a permanent gap, not an open fault** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host (Wazuh agent configuration); services VM (observed only, not changed) |
| **Addresses** | **3.5.6** (inactivity enforcement: evidence of its runs reaches the monitor); **3.3.1 / 3.14.6** (audit and monitoring data delivered to the manager); **3.4.3** (change control) |
| **Authority** | Owner approved the script after review, and ran it with `sudo` |
| **Related** | `DIWAI-CR-2026-10-14` (same day); the inactivity job's setup of 2026-09-13 (log `~/diwai/logs/setup-mac-inactivity-job-20260913-151755.log`) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

The services VM control-health monitor reported five failing checks at 13:15 on 2026-10-18, including **#13** (Mac inactivity enforcement job has not reported in 26 h) and **#15** (Mac TOTP check has not reported in 2.5 h). Investigation found two separate causes:

1. **A network outage between the Mac and the VM** (§5.1). The Mac's Wazuh agent could not reach the VM's manager from the outage until 13:17:13.
2. **A missing log-collection entry** on the Mac agent. `/var/log/diwai-inactivity.log` is not in the agent's `ossec.conf`, although the 2026-09-13 setup log records "agent monitoring the log". The inactivity job kept running and writing its log (daily 04:20, last run 2026-10-18 04:20:04), but the log was not being collected. This record fixes that.

## 2. Scope

1. **Changed:** `/Library/Ossec/etc/ossec.conf` on the Mac host. One `<localfile>` block (`log_format` syslog, location `/var/log/diwai-inactivity.log`) was added directly after the existing `diwai-mfa-pam.log` block. The agent was restarted.
2. **Tool:** `~/diwai/scripts/add-inactivity-localfile.sh`, reviewed by the owner and run with `sudo`. It backs up first, makes one edit, checks the XML (restoring the backup on failure) and restarts the agent. It does nothing if the entry already exists.
3. **Backup:** `/Library/Ossec/etc/ossec.conf.bak.20261018-inactivity`.
4. **Not changed:** the VM, the monitor, the inactivity job itself, the mfa-pam collection entry, any Wazuh rules.

## 3. Rollback

`sudo cp -p /Library/Ossec/etc/ossec.conf.bak.20261018-inactivity /Library/Ossec/etc/ossec.conf`, then restart the agent. The inactivity log would then stop being collected again.

## 4. Execution log (2026-10-18)

1. Read the monitor result on the VM (`/var/lib/diwai-control-health/latest.json`): checks 2, 4, 5b, 13, 15 failing at 13:15.
2. Confirmed on the Mac that both jobs were running: inactivity daily at 04:20 (last 04:20:04 today) and the TOTP check hourly through 14:54, all OK.
3. Owner ran `sudo grep` on the Mac agent log and config (output to the owner's home folder, read by Claude). The agent log shows `Unable to connect to '[[LAN-IP-REDACTED]]:1514/tcp'` repeating until `Connected to the server` at 13:17:13. The config lists three collected sources (a `netstat` command, a macOS log query, `/var/log/diwai-mfa-pam.log`) and has no entry containing "inactivity".
4. Claude wrote the script; the owner reviewed and ran it with `sudo`; the agent restarted.
5. Checked from the Mac: the new agent process (PID 66562) holds an established connection to `[LAN-IP-REDACTED]:1514`.

## 5. Observations

1. **VM network outage.** After UTM's restart the Mac could not reach the services VM (no ping; ports 22 and 3306 closed; ARP incomplete). The VM itself was up, with `[LAN-IP-REDACTED]/24` on `enp0s1`. UTM's bridge `bridge100` contained only the VM's virtual NIC `vmenet0`, and not the physical `en6`. After the owner restarted UTM, `en6` was a member again and the VM answered. **The cause is not known.** The Mac agent could not reach the manager during this time (agent log errors through 13:17:13; the start of the errors was not captured here).
2. **Open: why the inactivity entry is missing.** The likeliest cause is the agent restart on 2026-10-09 11:48 (the running agent process had started then), possibly rewriting the config. This is a **hypothesis**; the config file's change time and any agent-upgrade record were not read. Until confirmed, the same loss could recur.
3. **Resolved (Addendum A): check #15 stayed red.** The mfa-pam log *is* collected, and the Mac reported at 13:54 and 14:54, after the agent reconnected at 13:17. The monitor still showed #15 failing at 15:01. The cause is not found and is probably on the VM side (the monitor reads the VM's data; its script is root-only and was not read).
4. **Pipeline resumed (Addendum B); the gap remains.** **Archive gap (check #5b).** The VM's `wazuh-archive` job logged runs on 2026-10-12 and 2026-10-13 (both delivered), no runs for 2026-10-14 to 2026-10-17, and a run at 08:19 on 2026-10-18 that skipped ("No alert files found for 2026-10-17"). The timer is `Persistent=false`, so a missed 02:00 is never made up. Whether the VM was off or suspended on those nights is **not known**; the VM keeps its journal in memory only, so the reboot erased it. The Mac's 03:00 push job ran and correctly found nothing to push. **No log archive exists for 2026-10-13 to 2026-10-17.**
5. **Evidence gap for 3.5.6.** From the missing entry until this change, runs of the inactivity job were not visible to the monitor. The job's own log on the Mac is complete for those days (04:20 runs on 2026-10-13 to 2026-10-18).

## 6. Verification

| # | Check | Result |
|--:|:---|:---|
| 1 | Script made the backup and the XML check passed | **Pass** (owner ran it; agent restarted without a restore) |
| 2 | Agent restarted and holds a connection to `[LAN-IP-REDACTED]:1514` | **Pass** (PID 66562, ESTABLISHED) |
| 3 | The new `<localfile>` block is in `ossec.conf` | **Not independently read back by Claude** (the file is root-only; the script prints the edited lines to the owner's terminal) |
| 4 | Checks #2 and #4 clear after the outage | **Pass** (cleared at the 13:30 run) |
| 5 | Check #13 clears after the next inactivity run | **Pass** — the job ran at 04:20:02 on 2026-10-19 and the monitor run at 08:15:21 showed #13 `ok` (Addendum B) |
| 6 | Check #15 clears | **Pass** at the 16:00 run on 2026-10-18 (Addendum A) |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-18)* |
| **Date** | 10-18-2026 |

## Addendum A — check #15 cleared (entered 2026-10-19; observations of 2026-10-18)

| | |
|:---|:---|
| **What was found** | The Mac's `diwai-mfa-pam-check` ran hourly and logged `OK` lines (13:54, 14:54 included), and the agent config collects `/var/log/diwai-mfa-pam.log`. On the VM, rule 100226 (a plain heartbeat, no suppression) had produced **one** alert that day, at 08:54:13; the 13:54 and 14:54 lines produced none. Mac events did reach the VM in general: a rootcheck alert from the Mac arrived at 15:09:30, and agent 004 was listed Active. |
| **What changed** | Nothing beyond the agent restart already recorded in §2 (about 15:08). No change was made to the VM, the rule or the monitor. |
| **Result** | The Mac logged its next TOTP line at 15:54:14. The monitor run at 16:00:43 no longer listed check #15; the only failing checks were #5b and #13. |
| **Cause** | **Not confirmed.** The evidence fits the agent having stopped reading the mfa-pam log after the network outage, and the restart resetting it. The agent's internal state was not read, and the alternative (the 13:54 and 14:54 lines were read but dropped) was not excluded. If #15 goes red again without an outage, this should be investigated as a standing fault. |
| **Evidence** | VM `alerts.json` extracts (read by the owner with `sudo`, copied to the owner's home); VM `ossec.log` tail (agent 004 Active; no manager errors about it; unrelated `InventoryHarvesterFacade: Missing enabled field` at 13:17:15, not investigated); monitor result file `/var/lib/diwai-control-health/latest.json` at 15:30:10 and 16:00:43. |
| **Still open** | §5.2 (why the inactivity entry was missing) and §5.4 (no archive for 2026-10-13 to 2026-10-17). Checks #13 and #5b were still failing at 16:00 on 2026-10-18. |

## Addendum B — checks #13 and #5b cleared (entered 2026-10-19)

| | |
|:---|:---|
| **#13 (inactivity, 3.5.6)** | The Mac job ran at 04:20:02 on 2026-10-19 (`/var/log/diwai-inactivity.log`). The monitor run at 08:15:21 listed #13 as `ok`. This confirms the new `<localfile>` entry (§2) is delivering the log to the VM. The alert itself was not read on the VM; the evidence is the monitor result. |
| **#5b (archive)** | The VM's `wazuh-archive` job ran on schedule at 02:00:00 on 2026-10-19 (archive for 2026-10-18, 24K, delivered to Mac staging). The Mac's 03:00:03 push copied it to the NAS (`/Volumes/home/Backup/SecureMac/wazuh-alerts`), verified its SHA-256 and moved it (1 file, 0 failures). The monitor showed #5b `ok` ("shipped 0d ago"). |
| **Monitor overall** | At 08:15:21 on 2026-10-19: **0 of 32 result rows not `ok`** (25 checks, some with more than one row). The VM had been up since the 13:15 restart on 2026-10-18 and ran through the night. |
| **Not resolved** | **No archive exists for 2026-10-13 to 2026-10-17** (five days of alert logs; §5.4). The VM stayed up through the night of 2026-10-18, so the missed 02:00 runs on 2026-10-14 to 2026-10-17 are **still unexplained**; whether the VM was stopped or suspended on those nights is not known. The timer remains `Persistent=false`, so a missed run is never made up. The cause of the missing inactivity entry (§5.2) is still a hypothesis. |
| **A limit of the monitor** | One #5b row reads "Mac staging not checkable (ssh unavailable) — not treated as failure". The monitor cannot look at the Mac's staging folder, so that half of the check is blind; the Mac push log above is the evidence for delivery. |
| **Suggested follow-ups (not done)** | Set `Persistent=true` on `wazuh-archive.timer` so a missed 02:00 is made up; keep the VM journal persistent so a reboot does not erase it; separate change record for each. |

---

**Distribution:** Limited to authorized personnel
