> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# EVIDENCE RECORD — PERSONNEL ACTION (SEPARATION) DRILL
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-EV-PS-2026-10-23** |
| **Date** | October 23, 2026 (drill ran 14:14–14:28 local) |
| **Supports** | **3.9.2** (objective [c]); exercises `DIWAI-PS-001` PS-4 |
| **Run by** | Claude (AI assistant), under the owner's approval of the maintenance round and the temporary sudo window (`DIWAI-CR-2026-10-23`) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Why this record exists

`DIWAI-PS-001` defines a termination procedure (PS-4), but no personnel action has ever occurred, so the procedure had never been run. This drill runs it on a disposable account that stands in for an assistant, so that the steps, the timing and the refusals are on record. The account `drillassist63c4` existed only for this drill and has been deleted.

## 2. What was done and what was observed

All steps ran on the VM (`services.[DOMAIN.ORG]`).

| Step | Action | Observed |
|------|--------|----------|
| Onboard | Directory entry and VM local account created; added to `cui-users` only | Member of `cui-users`: yes. In `wheel` (sudo): no. |
| Before separation | Directory bind with its password; VM account check through the PAM account stack (`sshd`) | Bind succeeded; account stack `ok`. |
| Separation | `dsidm account lock`; removal from `cui-users`; `usermod -L -e 1970-01-02` | All completed in **1 second** (policy allows 1 hour). Directory reported the entry locked. |
| After separation | Same directory bind with the CORRECT password; same PAM check; group membership | Directory: "Account inactivated. Contact system administrator." PAM: refused, "User account has expired". Group membership: none. |
| Audit (24 h step) | `ausearch -ua` for the account | 0 records (the account never logged in). The search took about 13 minutes on today's audit logs. |
| Post-termination monitoring | Two further bind attempts after separation | The directory access log recorded both as **err=53** (unwilling to perform). The only successful bind (err=0) is the one before separation. |
| Clean-up | Directory entry and VM account deleted | Both confirmed gone. |

## 3. What this shows and what it does not

**Shown:** the PS-4 steps work as written for the directory, the VM and the Mac host's local accounts; access ends within seconds, the refusals are enforced by the systems and not by trust, further attempts leave a log record, and a new account added under least privilege has no administrative rights.

## 3a. Mac host local account (run by the owner at 14:40)

Script `mac-lockout-drill.sh`; raw output retained as `evidence-PS-mac-drill-20261023-1440.txt`. A disposable standard (non-admin) local account was created, and the Mac's own credential check (`dscl . -authonly`) was used as the test. Before the lock the correct password was ACCEPTED and a wrong one REFUSED (positive and negative control). `pwpolicy -disableuser` took 0 seconds; afterwards the correct password was REFUSED and `pwpolicy` reported "not allowed to authenticate". The account was then deleted and confirmed gone.

## 3b. Nextcloud (attempted, inconclusive)

Five attempts with disposable directory accounts could not obtain a positive control: Nextcloud refused the correct password before the lock, and no bind to the directory for the account was logged, so the later refusal proves nothing and is **not** claimed. Findings that are true: Nextcloud's LDAP backend finds a new directory account, and after the account is locked Nextcloud still lists it as enabled (the lock takes effect at the next login, when the directory refuses the password, as shown in section 2). Two-factor authentication is enforced for all users, which prevents a simple scripted login. A browser login by the owner as a throwaway directory user would supply the missing control.

**Not shown (still open):**
- Nextcloud sessions or app passwords: the refusal at Nextcloud's own login was not demonstrated (section 3b). Existing Nextcloud sessions and app passwords were not examined.
- Return of physical items and revocation of any delegated privileges are not exercised by a disposable account.
- Transfers (PS-5) are not applicable to a single-owner system and were not tested.
- The audit search is slow; PS-4's 24-hour audit step should be started promptly and allowed to run.

## 4. Reproduction

The drill script is retained at `~/diwai/scripts/personnel-drill/ps-drill.sh` on the Mac. It creates and removes its own account, so it can be re-run for any later personnel action rehearsal.
