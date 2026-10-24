> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — VM PASSWORD MINIMUM 16 AND PASSWORD HISTORY ENFORCED; MAC WI-FI RADIO OFF; FIRST AUDIT-EVENT REVIEW
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-25** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§5). Owner approved 2026-10-23** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Services VM (`/etc/security/pwquality.conf`, `/etc/security/pwhistory.conf`, the `custom/hardening` authselect profile); Mac host (the Wi-Fi radio) |
| **Addresses** | **3.5.7**, **3.5.8** (password complexity and reuse), **3.1.16** (wireless), **3.3.3** (review of logged events) |
| **Authority** | Owner approval in chat, 2026-10-23 ("approve all"), items 13, 14 and 15 of the re-walk definitions sheet |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

The objective-level re-walk found three gaps between the SSP and the systems: (1) Appendix E.4 said the minimum password length is 16 "on both", but the **VM's own accounts required 15**; (2) **no password history** was enforced for the VM's own accounts (`pam_pwhistory` was not in the stack; `remember` was commented out), so 3.5.8 was proven only for the directory and the Mac; (3) the Mac's **Wi-Fi radio was On** (not associated) although the wireless path is meant to be off except as a break-glass uplink.

## 2. Change

| # | Host | Change | Rollback |
|--:|:---|:---|:---|
| 1 | VM | `pwquality.conf`: `minlen` 15 → **16** | `/etc/security/pwquality.conf.bak-20261023-134129` |
| 2 | VM | `pwhistory.conf`: `remember = 6`, `enforce_for_root`; the authselect feature **`with-pwhistory`** enabled on `custom/hardening` (adds `pam_pwhistory` to `system-auth` and `password-auth`) | `authselect backup-restore pre-pwhistory-20261023-134129`; `/etc/security/pwhistory.conf.bak-20261023-134129` |
| 3 | Mac | Wi-Fi radio off: `networksetup -setairportpower en1 off` | `networksetup -setairportpower en1 on` |

## 3. First audit-event review (`DIWAI-PR-001` v1.5 §4.8)

Performed the same day and recorded in `DIWAI-PR-LOG`. Finding: **successful writes to configuration files are not logged by `auditd`** (the hardened baseline records privileged commands, authentication and unsuccessful access); they **are** caught in real time by Wazuh file-integrity monitoring (a probe file raised alerts 554, 550 and 553), and `sudo` logs who ran them. No audit-rule change made. Deferred: `auditd` path watches on `/etc/sudoers.d`, `/etc/pam.d`, `/usr/local/sbin`.

## 4. Security analysis

All three changes **tighten** a control and none opens a path. Risk: a mistake in the sign-in stack could lock a login out. Mitigation: the supported authselect feature was used (not a hand edit), a named backup was taken, two sessions stayed open, and a fresh SSH login was proven to work immediately after. Password history for `root` is also enforced (`enforce_for_root`), so an administrator reset cannot reuse a recent password; this applies only to future changes.

## 5. Verification

| Test (disposable account, changed as a user through `passwd`) | Result |
|:---|:---|
| A different valid password | **accepted** |
| The previous password again | **refused**: "Password has been already used" |
| A 14-character password | **refused**: "The password is shorter than 16 characters" |
| Live stack | `pam_pwhistory` present in both `system-auth` and `password-auth`; `authselect current` lists `with-pwhistory` |
| SSH login after the change | works (the whole review session ran over new logins) |
| Mac Wi-Fi | `networksetup -getairportpower en1` → Off |

The first attempt used `chpasswd` as root, which skips both checks, so its "accepted" result proved nothing; the test was redone through the user's own `passwd`.

## 6. Open items

1. `passwordMustChange` in the directory remains off by decision: the account `uid=[USERNAME]` is the bind account for four services, so a forced change would break them. Splitting those identities comes first (3.5.9).
2. Owner signature: done 2026-10-23.

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
