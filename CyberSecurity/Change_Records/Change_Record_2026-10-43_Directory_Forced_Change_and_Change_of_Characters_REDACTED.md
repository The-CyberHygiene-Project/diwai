> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — FORCED PASSWORD CHANGE ON; RULE FOR CHANGE OF CHARACTERS STATED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-43** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§2). Owner approved 2026-10-24.** |
| **System** | services VM: 389-DS global password policy; Identification and Authentication policy; SSP Appendix E.4 |
| **Addresses** | **3.5.9** (temporary passwords); **3.5.7** [b] (change of characters); Rev 3 03.05.07, 03.05.12 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Changes

1. **Directory:** `dsconf diwai pwpolicy set --pwdmustchange on` (`passwordMustChange` was off). A password set by an administrator now has to be changed by the user before anything else is allowed.
2. **IA policy and SSP Appendix E.4:** one rule added: a new password must differ from each of the previous six. The directory (`passwordInHistory: 6`) and the Mac policy (`diwai.password.history`) already enforce it. The IA policy's temporary-password line now says the change is enforced.

## 2. Verification (`scripts/pwpolicy/vm-mustchange.sh`, output `mustchange-20261024.out`)

- A disposable account (made-up name) was created by the administrator with a temporary password. Its password-expiry time was set to the epoch (expired).
- First login: refused, "Server is unwilling to perform (53)" with the PasswordExpired control, for both a bind check and an ordinary search.
- The user changed the password with the old one; the new password then worked and an ordinary search succeeded; the expiry became three years ahead (2029-10-23).
- The account was removed.
- Service accounts: after the change, `svc-nextcloud` (43 binds), `svc-nas` (3), `svc-apache` (3) and `svc-dovecot` (2) showed no failed binds in the directory log. The script's own failure counter was mis-parsing the log (a script defect, noted); the check above was redone separately with correct parsing.

## 3. Limits

- An administrator reset of any real account now forces that user to change the password at the next login. For the owner's account this affects only a break-glass reset (his own change script sets the password as himself, with the old password, and is not affected).
- The service accounts have their own password policy and were unaffected here. **When a service-account password is next rotated, check the bind afterwards** (the same check this record used).
- The Mac and the VM's local accounts are separate stores. This change is the directory only; whether their temporary passwords are forced to change was not assessed here, and 3.5.9 rests on the directory, where the owner's CUI accounts live.

## 4. Rollback

`sudo dsconf diwai pwpolicy set --pwdmustchange off`

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
