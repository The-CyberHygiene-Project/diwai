> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — 90-DAY PASSWORD EXPIRY EXTENDED TO THE VM LOCAL `[USERNAME]` ACCOUNT; CLOSING ITEMS FROM DIWAI-CR-2026-10-11
## [DOMAIN.ORG] SecureMac Reference System


| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-12** |
| **Date** | October 9, 2026 |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Rocky Linux VM — local account `[USERNAME]` (`/etc/shadow`) |
| **Addresses** | Password expiration (IA-5 / 3.5.7), continuing C10 to C12 of `DIWAI-CR-2026-10-11` |
| **Authority** | Owner direction 2026-10-09: "set the VM expiry to 90 days". Applied with the owner present; sudo unlocked by the owner. |
| **Status** | **IMPLEMENTED AND APPROVED — owner signature 9 October 2026 (§8). Post-signature additions record the document edits, the `root` decision and the refusal test (above §7).** |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Condition addressed

`DIWAI-CR-2026-10-11` enforced the 90-day password expiry stated in the Identification and Authentication, Acceptable Use
and Configuration Management policies on the Mac (`[USERNAME]`) and in the directory (all interactive user accounts). It did
not look at the VM's **local** accounts. The VM `[USERNAME]` account is a local account (`nsswitch` uses files, `pam_unix`
authenticates it, `sssd` is inactive), so it uses a password separate from the directory and Mac passwords, and
nothing governed its age.

| Item | Before | After |
|:---|:---|:---|
| VM `[USERNAME]`, maximum password age | 99999 days (never expires) | **90 days**, warning 7 days |
| VM `[USERNAME]`, last password change | not read | 2026-10-09 (changed by the owner today) |
| VM `[USERNAME]`, password expires | never | **2027-01-07** |

The policy wording ("90 days for interactive user accounts") already covers this account. The change brings the VM into line
with it; no policy value changes.

## 2. Changes

| # | Host | Change | Rollback |
|---|---|---|---|
| C1 | VM | `chage -M 90 [USERNAME]` (maximum age 99999 → 90). `/etc/shadow` copied first, preserving mode and owner, to `/root/shadow.bak-20261009-vmexpiry`. | `sudo chage -M 99999 [USERNAME]`, or restore the backed-up `/etc/shadow` |

The owner changed the account's password earlier the same day (`passwd`, through `ssh -t services`), so the first 90-day
period runs from 2026-10-09 and nothing was backdated.

## 3. Verification

| Test | Result |
|:---|:---|
| `chage -l [USERNAME]` before | last change 2026-10-09; expires never; maximum 99999; warning 7 |
| `chage -l [USERNAME]` after | last change 2026-10-09; **expires 2027-01-07**; maximum **90**; warning 7 |
| `sudo` with the new password | accepted (owner entered it once; no failure recorded) |
| `faillock --user [USERNAME]` after the change | empty |
| Local accounts with a usable password (`/etc/shadow`) | `root` and `[USERNAME]` only; see finding 2 |

**Not yet done: a refusal test.** The setting is proven by read-back only. The earlier expiry changes were each proven by
refusal on a disposable account. The equivalent here is a disposable local account with an already-expired password,
which must be refused for the right reason. Run it before signing, or record that read-back is accepted for this
setting. See §6.

## 4. Findings

1. **Three failed password attempts locked the owner out of the VM for about 15 minutes.** At 13:29:49, 13:31:53 and
   13:32:03 on 2026-10-09 the owner typed a password that the VM did not accept; the third failure triggered `faillock`
   (`deny = 3`, `fail_interval = 300`, `unlock_time = 900`). The lock cleared by itself and nothing was bypassed. The cause was
   that the VM `sudo` password is the local VM password, which today's directory and Mac changes did not touch. This is the
   lockout control working as designed, and it is the first time the 3-in-5-minutes, 15-minute lock configured by
   `DIWAI-CR-2026-10-11` was seen to act on the owner. The directory and Mac accounts were not locked.
2. **VM `root` has a usable password hash that never expires.** `passwd -S root` reports "Password set, SHA512 crypt" with
   no maximum age. Remote root login is off (`PermitRootLogin no`), and the owner has noted before that the root password is
   rejected, so it may be unusable in practice. It is not an interactive user account, and this record does not change it.
   The owner is asked to decide whether `root` is exempt like the break-glass account (state the exemption in the policy)
   or is to be locked (`passwd -l root`; this would also need the recovery path checked, because the ISO rescue procedure
   was used on 2026-09-25).
3. **A `passwd` run on the Mac, not the VM, was refused** ("authentication token failure"). It changed nothing and the
   Mac failed-login count stayed 0. The cause was not established: the Mac gave no reason, and the likely ones are an
   old password typed for the current one, a new password under 16 characters, or one within the last 6.

## 5. Documents (proposed; none changed)

| Document | Proposed edit |
|:---|:---|
| Identification and Authentication Policy, expiration bullet | add "the VM local account `[USERNAME]` (`chage -M 90`)" to the list of enforcement points; state the decision on `root` (finding 2) |
| SSP Appendix E.4, password expiration row | the same two additions; the VM local account is listed beside the directory and Mac enforcement |
| SSP revision row | a new amendment (20) if the SSP is edited; the version number is left to the owner |
| Retired Identifiers Register (`DIWAI-IA-REG-001`) | no change; the account `[USERNAME]` is already listed for the VM |

## 6. Open items

- **Refusal test** for the VM local expiry (§3), or an owner decision to accept read-back.
- **Decision on `root`** (finding 2).
- **Directory `[USERNAME]` password: confirmed changed.** `passwordExpirationTime` is 2027-01-07 18:08:18Z, i.e. changed
  2026-10-09 about 18:08Z; `passwordExpWarned` 0; the account is not locked. This closes the open item in
  `DIWAI-CR-2026-10-11` §6 that the directory password "begins its first period at its next change". That record is signed
  and is not edited; this record supersedes the item.
- **Mac `[USERNAME]` password** also set 2026-10-09 (expiry rule present). Both it and the directory password expire about
  **2027-01-07**, the same date as the VM account.
- **Calendar reminders** created 2026-10-09 for 2026-12-24 (two weeks before) and 2027-01-07 (the day). Their text names the
  directory and Mac passwords; adding the VM password to the wording is optional.
- **`svc-nas` bind** (err=0 after the C1 policy change in the earlier record) and the **`sysadmin` 16-character check** remain open
  from `DIWAI-CR-2026-10-11` §6.

**Added after signature, 9 October 2026, at the owner's direction (the signed text above is unchanged):** the §5 document edits and the `root` decision were completed the same day. The owner chose to exempt `root` (option 1). Diff 19 added the VM local `[USERNAME]` account and the `root` exemption to the Identification and Authentication Policy, expiration bullet; diff 20 made the same additions to SSP Appendix E.4 and added the revision row **2.18 (amended 20)**, dated 10/09/2026. Backups: `~/diwai/backups/20261009-doc-corrections-10/`. Still open: the refusal test (§3, §6).

**Added after signature, 9 October 2026, at the owner's direction (the signed text above is unchanged): refusal test run and passed.** On a disposable local account `fltest` (random password, never written to a file): with the password current, `su - fltest` was accepted (control); with the last change set 130 days back and a 90-day maximum (expired 2026-08-30), the same login with the correct password was refused: "You are required to change your password immediately (password expired)", and the command did not run. `faillock` for `fltest` stayed empty. The account and its home directory were removed and confirmed gone. The VM expiry is therefore proven by refusal, not by read-back alone. With the document edits made and the `root` decision taken (the paragraph above), no item remains open in this record.

## 7. SPRS effect

**None.** The expiry is a stricter choice than DoD's value ("never for passwords where MFA is employed"), so no
requirement is added or removed, and the figure of record (100/110, Rev 2, evidence-strict) is unchanged.

---

## 8. Sign-off

|                |                                                |
|:---------------|:-----------------------------------------------|
| **Name**           | [SYSTEM-OWNER]                              |
| **Roles**          | System Owner; ISSO; System Administrator       |
| **Signature**      | \_\_\_\_[SYSTEM-OWNER]_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| **Date**           | \_\_\_\_9 October 2026\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

---

**Distribution:** Limited to authorized personnel
