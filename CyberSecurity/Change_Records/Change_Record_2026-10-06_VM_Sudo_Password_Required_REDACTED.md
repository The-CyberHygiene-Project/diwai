> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — VM SUDO NOW ASKS FOR THE PASSWORD
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-06** |
| **Date opened** | October 4, 2026 |
| **Status** | **APPROVED 10-04-2026** — implemented and verified, all checks pass (§6); signed by the System Owner / ISSO (typed at the owner's direction) |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | services.[DOMAIN.ORG] (VM): `/etc/sudoers.d/[USERNAME]`. Mac: two owner scripts adapted |
| **Addresses** | **3.1.5** (least privilege); **3.1.6** (non-privileged access for non-security functions); **3.5.3** (privileged access needs more than an open session) |
| **Authority** | Owner decision 2026-10-04 (option A: require the password; then option A: remember it at most 2 minutes, so a repair asks once) |
| **Found by** | Repair library build, 2026-10-04 (`~/diwai-rag` plan Task 8; final review finding I6) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

`/etc/sudoers.d/[USERNAME]` (dated 2026-04-08) granted `[USERNAME] ALL=(ALL) NOPASSWD: ALL`. While the owner's SSH session to the VM was open (a shared ControlMaster connection), any program running as the owner on the Mac could become root on the VM without being asked. That included the Aider coding tool after a single typed yes. This was not recorded in the SSP or POA&M.

## 2. Scope

1. `/etc/sudoers.d/[USERNAME]` replaced with:
   ```
   Defaults:[USERNAME] timestamp_type=global, timestamp_timeout=2
   [USERNAME] ALL=(ALL) ALL
   ```
   `sudo` asks for the owner's VM password. A password typed once is remembered across the owner's sessions for at most 2 minutes, not the default 5 minutes per terminal. That lets a repair ask once, after which the repair runner makes the VM forget it (`sudo -K`).
2. `~/diwai/scripts/change-directory-password.sh` asks for the VM password once at the start (`ssh -tt services sudo -v`) and makes the VM forget it at the end. `negative-test-directory-policy.sh`'s usage note was updated the same way. Backups: `~/diwai/backups/*.bak-20261004-sudo`.
3. The repair library's VM steps do the same: one prompt per repair, quiet steps use `sudo -n`, and `sudo -K` runs at the end (`~/diwai-rag` commit `2dbfb54`).

## 3. Before the change

- **Nothing scheduled relies on passwordless sudo:**
  - no `[USERNAME]` crontab;
  - only the two stock user timers;
  - no unattended (`TTY=unknown`) sudo use by `[USERNAME]` in 45 days of the journal.
- **Only two owner-run scripts used `sudo -n`.** Both were adapted (§2).
- **No lockout through the directory:** `sudo` authenticates through `system-auth` → `pam_unix` against the **local** `/etc/shadow` hash for `[USERNAME]` (the same password as SSH). It does not depend on the 389-DS directory.
- **Lockout counter:** wrong passwords count toward `pam_faillock`. The owner was warned not to retry repeatedly.

## 4. Rollback

The original file was saved to `/root/sudoers.d-[USERNAME].bak-20261004` on the VM and `~/diwai/backups/vm-sudoers.d-[USERNAME].bak-20261004` on the Mac. To roll back, from a root shell on the VM: `cp -p /root/sudoers.d-[USERNAME].bak-20261004 /etc/sudoers.d/[USERNAME] && visudo -c`.

## 5. Execution log (2026-10-04)

1. The owner opened a safety root shell (`sudo -i`) in the existing SSH window and kept it open until the end.
2. The new content was staged as `/etc/sudoers.d/[USERNAME].new` (inactive: sudoers ignores names containing a dot), set to mode 0440, and checked with `visudo -cf`: parsed OK. The old file was backed up (§4).
3. 08:29: `mv` into place. Passwordless sudo was refused immediately.
4. The owner ran `sudo -v` in a second session and the password was accepted.
5. Verification (§6). The owner was then asked to close the safety root shell (`exit`).

## 6. Verification

| Check | Result |
|:---|:---|
| Passwordless sudo refused | **Pass**: "a password is required" |
| Owner's password accepted | **Pass** |
| Remembered across sessions (a quiet session used it right after) | **Pass** |
| `visudo -c`: `/etc/sudoers`, `sudoers.d/[USERNAME]`, `sudoers.d/secure_path` | **Pass**: all parsed OK |
| `faillock --user [USERNAME]` | **Pass**: no failures recorded |
| `sudo -K` makes the VM forget it | **Pass**: password required again |

## 7. Observations

1. **Residual window.** For up to 2 minutes after the owner types the password, any program running as the owner can use `sudo` on the VM through the open session. The repair runner and the password script close that window early with `sudo -K`.
2. **3.5.3.** VM SSH already requires TOTP for the owner's login. Privileged use now also requires the password at the time of use.

## 7a. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — \_[SYSTEM-OWNER] *(typed at the owner's direction, 2026-10-04)* |
| **Date** | 10-04-2026 |

---

**Distribution:** Limited to authorized personnel
