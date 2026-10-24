> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — PASSWORD CHANGE INTERVAL 90 DAYS → THREE YEARS ON ALL THREE PASSWORD STORES; CREDENTIAL REGISTER; MONITOR CHECK 18
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-26** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§5). Owner approved 2026-10-23** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac host (per-user account policy), services VM (`chage`, 389-DS global policy and one entry, monitor, register copy) |
| **Addresses** | **3.5.7**, **3.5.8**, **3.5.9** (password management, Rev 2); Rev 3 **03.05.12.e** (change interval), **03.05.07** (screening, not yet installed) |
| **Supersedes** | the 90-day interval of `DIWAI-CR-2026-10-11` and `-10-12` (left as written; this record points back) |
| **Authority** | Owner decisions 2026-10-23 on the five points of the 2026-10-19 package; the owner ran the Mac step |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

On 2026-10-19 the owner preferred the Rev 3 approach to password expiry: **never** for a password protected by a second factor on every login path, **at least every three years** for any authenticator that can be used without one. Neither Rev 2 nor Rev 3 requires periodic expiry; the 90 days came from this system's own policy text. A five-point decision package was drafted and held.

## 2. Decisions taken (2026-10-23)

| # | Decision |
|--:|:---|
| 1 | **No password qualifies for "never".** The Mac and VM consoles and webmail and mail are password-only paths. The three-year rule applies to **every** password, **enforced by an expiry** of 3 years (not by turning expiry off), which does not depend on a register or on memory |
| 2 | Last-change dates were read from the systems, not asked for (§4) |
| 3 | Part B approved: documents and three settings in one change |
| 4 | Part C (offline password-screening list) approved as a **separate later change**; opened as **POA&M-077**; the policy states it is not yet in effect |
| 5 | Effective on the day the settings changed: 2026-10-23 |

## 3. Change

| # | Host | Change | Rollback |
|--:|:---|:---|:---|
| 1 | VM | `chage -M 90 [USERNAME]` → `-M 1095` (expires 2029-10-08) | `chage -M 90 [USERNAME]` (backup of `/etc/shadow` in `/root`) |
| 2 | VM (389-DS) | Global `passwordMaxAge` 7,776,000 s → **94,608,000 s**; the stored `passwordExpirationTime` on `uid=[USERNAME]` moved from 2027-01-07 to **2029-10-08** (last change + 1095 days). `svc-nas` and `demo_user` keep their own policy entries | `dsconf diwai pwpolicy set --pwdmaxage 7776000`; set the entry back to 20270107180818Z |
| 3 | Mac | Per-user rule `diwai.password.expiry` **90 → 1095 days** (run by the owner with `mac-expiry-1095.sh`, which saves the old policy and read it back) | `pwpolicy -u [USERNAME] -setaccountpolicies ~/diwai/backups/20261023-password-expiry/mac-[USERNAME]-policy-before.plist` |
| 4 | Documents | `DIWAI-IAP-001` §3.3 (change interval and screening bullets), `DIWAI-AUP-001` §2.2, `DIWAI-CMP-001` §3.5 table, SSP Appendix E.4, POA&M-077 | the `.bak-20261023-pwexp` copies |
| 5 | New | Credential register **`DIWAI-CRR-001`** (Evidence folder) and its copy `/etc/diwai/credential-register.json` on the VM | delete both |
| 6 | VM | **Monitor check 18** "credential register: no password is past its change date" (backup `diwai-control-health.bak-20261023-chk18`): fails on an overdue entry or an unreadable register | restore the backup |

## 4. Dates read from the systems (2026-10-23)

| Credential | Last changed | Next due (+1095 days) | Enforced by |
|:---|:---|:---|:---|
| Mac `[USERNAME]` | 2026-10-09 | 2029-10-08 | the system |
| VM local `[USERNAME]` | 2026-10-09 | 2029-10-08 | the system |
| Directory `uid=[USERNAME]` | 2026-10-09 | 2029-10-08 | the system |
| VM `root` | 2026-10-19 | 2029-10-18 | the register |
| Mac `sysadmin` | 2026-08-07 | 2029-08-06 | the register |
| `svc-nas` | 2026-08-02 | 2029-08-01 | the register |

## 5. Verification

| Check | Result |
|:---|:---|
| VM `chage -l [USERNAME]` | maximum 1095 days, expires 2029-10-08 |
| Directory | `passwordmaxage: 94608000`; `[USERNAME]` expiry 20291008180818Z; `dirsrv@diwai` active; `svc-nas` and `demo_user` still carry their own policy entry |
| Mac | read-back `diwai.password.expiry` = **1095**; the account still authenticates |
| **Negative and positive proof on the VM (disposable accounts, removed)** | account last changed **1,000 days ago**: expires 2027-01-26, **accepted** by the sshd account stack; last changed **1,100 days ago**: expired 2026-10-18, **refused** ("Authentication token is no longer valid") |
| Monitor check 18, every branch (stand-in harness) | healthy → OK; one overdue → FAIL naming it; due within 90 days → OK with a warning list; file missing, malformed, or no register entries → FAIL |
| Monitor live | **35 rows**, checks 17 and 18 OK; the only failure is the 2026-10-23 Mac warning test |

**Not proven by test:** the Mac expiry (read back only; a disposable Mac account was not aged), and the directory's own refusal at the new age (the stored expiry and policy were read back).

## 6. Security analysis

This **lengthens** an interval and so removes a scheduled change, which is the intent of Rev 3 (long, unique passwords, changed on events, not on a clock). Compensations: length 16 (all three stores, the VM raised from 15 today), history 6 (all three), lockout, screening **to be installed (POA&M-077)**, a second factor on every remote path, and the change-on-event rule (`DIWAI-IAP-001`). The accounts the system cannot expire are tracked and monitored. **Residual:** until the screening list exists, a long password that is on a breach list is not refused (the same position as before this change). **SPRS:** no change expected; the DoD items for passwords concern complexity, reuse, temporary passwords and protection, not expiry.

## 7. Open items

1. **Part C, the password screening list** (POA&M-077): build the offline list, a VM `pam_pwquality` dictionary, the directory dictionary check, and a Mac helper by procedure.
2. 389-DS `passwordMustChange` stays off (3.5.9): the account `uid=[USERNAME]` is the bind account for four services, so forcing a change would break them. Splitting those identities comes first.
3. Owner signature: done 2026-10-23.

## 8. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
