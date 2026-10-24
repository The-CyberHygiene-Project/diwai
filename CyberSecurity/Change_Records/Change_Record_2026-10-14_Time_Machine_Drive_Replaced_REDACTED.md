> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — TIME MACHINE DRIVE REPLACED; USB GUARD ALLOWLIST UPDATED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-14** |
| **Date opened** | October 18, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§6); owner approved 2026-10-18. Two items open (§5.1, §5.2)** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host only |
| **Addresses** | **3.8.9** (backup confidentiality: the new drive is FileVault-encrypted); **3.1.20** (portable storage allowlist); **3.4.3** (change control); **3.4.1** (inventory: SBOM v3.15) |
| **Authority** | Owner: the Time Machine drive failed; the owner replaced it and asked that the USB guard be told about the new volume |
| **Related** | `DIWAI-CR-2026-10-13` (same day; the guard was off for that transfer), `DIWAI-CR-2026-09-09` (attached storage encrypted) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

The Time Machine destination (`SecureMac`, USB SSD, allowlist UUID `[TM-UUID-REDACTED]`) **failed** (reported by the owner; the date of failure and the last good backup on it were not captured in this record, §5.1). The owner replaced it with a new 500 GB SSD. The USB guard force-ejects any USB storage whose partition UUID is not on its allowlist, so the new drive would have been ejected the moment the guard was switched back on.

## 2. Scope

1. **New drive:** USB SSD, APFS **case-sensitive**, volume `SecureMac`, **FileVault: Yes** (read back as *Yes, Unlocked* after mounting). Capacity 499.9 GB.
   - Physical partition (`disk6s2`) UUID: **`[HW-UUID-REDACTED]`** (the value the guard compares)
   - Volume UUID: `[HW-UUID-REDACTED]`
   - Time Machine destination ID: `[HW-UUID-REDACTED]`
2. **Allowlist updated.** The old UUID was replaced by the new one in three root-owned scripts, by `~/diwai/scripts/install-new-tm-uuid.sh` run with `sudo` by the owner: `/usr/local/sbin/usb-guard`, `/usr/local/sbin/usb-guard-monitor`, `/usr/local/sbin/mount-tm-drive.sh`. Each was backed up first as `<name>.bak.20261018-newtm`; the edited copies differ only in the UUID line and its comment (copies kept in `~/diwai/backups/20261018-usb-guard-edits/`). The monitor daemon was restarted because it reads the allowlist only at start.
3. **Guard switched back on** by the owner at 10:48:57.
4. **Not changed:** the `CyberHygiene Project` drive's allowlist entries (`[HW-UUID-REDACTED]` volume, `[HW-UUID-REDACTED]` container), the VM's USB guard, the Time Machine schedule (hourly), `org.diwai.mount-tm-drive`.

## 3. Rollback

Restore each `*.bak.20261018-newtm` over its script and run `sudo launchctl kickstart -k system/org.diwai.usb-guard`. The old drive's UUID would then be allowlisted again and the new drive would be ejected.

## 4. Execution log (2026-10-18)

1. Read the new disk's identifiers with `diskutil info` (partition `disk6s2`, volume `disk7s2`).
2. Searched `/usr/local/sbin`, the LaunchDaemons and `~/diwai/scripts` for the old UUID: three live scripts (and their older backups) referenced it.
3. Prepared edited copies and a short installer; the owner read and ran it with `sudo`; then ran `sudo /usr/local/sbin/usb-guard on`.
4. Read the guard log, the file contents and the daemon state; checked Time Machine (§6).

## 5. Observations

1. **Open: the old drive's failure is not recorded.** The date it failed, the last good backup on it, and whether any backups were missed in between are unknown to this record. The SSP last recorded a backup of **2026-09-15 16:50**. The owner is asked to state the failure date and the last good backup so the gap can be stated (backup RPO: hourly).
2. **Open: mount-point name.** The new volume mounted as **`/Volumes/SecureMac 1`**, not `/Volumes/SecureMac`. `mount-tm-drive.sh` tests for `/Volumes/SecureMac`; at the next login it may report a mount failure although the drive is mounted. To be checked at the next restart; not changed today.
3. **Guard window.** The guard was off 09:10:04 → 10:48:57 (`DIWAI-CR-2026-10-13` §5.1). The new drive was attached during that window, so its first appearance in the log is the allow event at 10:49:00–10:49:01 after the guard came back on.
4. **`usb-guard status` run without `sudo` prints "Monitor daemon: stopped"** because `launchctl list` cannot see a system daemon from a user account. The daemon was running (PID 50254; `launchctl print` state *running*). The wording of that message is a small defect in the script.

## 6. Verification

| # | Check | Result |
|--:|:---|:---|
| 1 | New UUID present in all three scripts; old UUID absent from them | **Pass** (`grep -c` = 1 each; old UUID 0) |
| 2 | Guard mode file reads `on`; monitor daemon running | **Pass** (`/var/lib/usb-guard/mode` = on; PID 50254) |
| 3 | Guard log: `AI-TRANSFER` blocked and ejected; new Time Machine drive **allowed** by partition UUID `[HW-UUID-REDACTED]` at 10:49:00 | **Pass** |
| 4 | New drive is encrypted | **Pass** (`diskutil`: FileVault Yes; `apfs list`: Yes, Unlocked) |
| 5 | A Time Machine backup completed to the new drive | **Pass** — snapshot **2026-10-18 10:47:15**, `RESULT = 0`; backup folder 229 GB against 221 GB used on the source volume; hourly schedule on |
| 6 | The backup restores | **Not yet tested** (one-file restore test proposed) |
| 7 | Allowlist behaviour for the `CyberHygiene Project` drive unchanged | **Pass** (allowed at 10:49:34) |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-18)* |
| **Date** | 10-18-2026 |

---

**Distribution:** Limited to authorized personnel
