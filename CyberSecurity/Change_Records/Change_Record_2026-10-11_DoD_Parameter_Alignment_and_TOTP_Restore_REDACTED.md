> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — PASSWORD LENGTH 16 AND LOCKOUT ALIGNED TO THE DoD Rev 3 PARAMETERS; MAC TOTP RESTORED AND MONITORED
## [DOMAIN.ORG] SecureMac Reference System


| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-11** |
| **Date** | October 9, 2026 |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Rocky Linux VM — PAM `faillock` configuration and 389-DS instance `diwai` (`cn=config`); Mac mini host — `pwpolicy` global account policy; control-health monitor on the VM (`/usr/local/sbin/diwai-control-health`); Mac `sshd` PAM (`/etc/pam.d/sshd`) |
| **Addresses** | **3.5.7** (password length), **3.1.8** (unsuccessful logon attempts), **3.12.3** and **3.5.6** (monitoring of the inactivity-enforcement control; control-health check 13), **3.5.3** and **3.7.5** (TOTP on the Mac host restored), password expiration (IA-5 / 3.5.7) |
| **Authority** | Owner direction 2026-10-09, adopting the DoD organization-defined parameter values for NIST SP 800-171 Rev 3 (DoD memo signed 2025-04-10, Attachment A) for these two parameters; owner direction 2026-10-09 to restore the Mac TOTP and to monitor it (C6 to C9); owner decision 2026-10-09 to enforce the 90-day password expiry stated in three policies, for interactive user accounts only (C10 to C12). Changes applied one at a time with the owner present; sudo unlocked by the owner for each VM step. |
| **Status** | **IMPLEMENTED, VERIFIED AND APPROVED — owner signature 9 October 2026 (§8)** |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Condition addressed

A comparison of the organization's documents against the DoD Rev 3 parameter values
(`ODP looser than DoD - flagged`, 2026-10-09) found two parameters where the configured
control was looser than DoD's value, and one place where the documents disagreed with the
configuration. While correcting the related SSP rows, the Mac's SSH multifactor configuration
was read and found to have lost its TOTP line to a macOS update on 2026-09-03 (finding 7).

| Parameter | DoD value | Before this record | After |
|:---|:---|:---|:---|
| 3.5.7 minimum password length | 16 characters | VM directory 14; Mac 14 | **16 on both** |
| 3.1.8 failed attempts allowed | at most 5 | VM `deny = 3`; Mac **10** | VM 3 (unchanged); Mac **5** |
| 3.1.8 counting window | 5 minutes | VM `fail_interval = 900` (15 minutes); Mac has no separate window | VM **300**; Mac see §4 |
| 3.1.8 lock duration | at least 15 minutes | VM `unlock_time = 900`; Mac 900 s | unchanged (meets) |

DoD values bind under Rev 3. Under Rev 2 (the current DoW basis) they are guidance; the
organization adopts them early.

## 2. Changes

| # | Host | Change | Rollback |
|:---|:---|:---|:---|
| C3 | VM | `/etc/security/faillock.conf`: `fail_interval` 900 → **300** | `faillock.conf.bak-20261009-CR-2026-10-11` (same directory) |
| C1 | VM | 389-DS `cn=config`: `passwordMinLength` 14 → **16**, applied over the local `ldapi` socket (`ldapmodify`, SASL EXTERNAL). `passwordCheckSyntax: on` and `passwordMinCategories: 3` unchanged. | set `passwordMinLength` back to 14; `dse.ldif.bak-20261009-CR-2026-10-11` in `/etc/dirsrv/slapd-diwai/` |
| C2 | Mac | `diwai.minimum.length`: rule text `policyAttributePassword matches '.{14,}+'` → `'.{16,}+'`, and `minimumLength` 14 → 16 | `pwpolicy -setaccountpolicies ~/diwai/staging/mac-account-policy.live-BEFORE-ORIGINAL-14.plist` |
| C4 | Mac | `diwai.authentication.lockout`: `policyAttributeMaximumFailedAuthentications` 10 → **5**; `autoEnableInSeconds` unchanged at 900 | same file as C2 |
| C5 | VM | `diwai-control-health` check 13 (Mac inactivity enforcement heartbeat): the heartbeat is now also read from the previous day's rotated Wazuh alerts file (`/var/ossec/logs/alerts/YYYY/Mon/ossec-alerts-DD.json.gz`), in addition to the live `alerts.json`. The 26-hour limit is unchanged. | `/usr/local/sbin/diwai-control-health.bak-20261009-chk13` |
| C6 | Mac | `/etc/pam.d/sshd`: the TOTP line `auth required /opt/homebrew/lib/security/pam_google_authenticator.so` restored after `pam_opendirectory` (line 12; mode 444 root:wheel), by `scripts/restore-mac-ssh-totp.sh` from the staged known-good file `~/diwai/staging/sshd.pam.new`. The script refuses unless the staged file only adds lines, requires a typed confirmation that a second session is open, and restores the backup if its read-back fails. | `sudo cp -p /etc/pam.d/sshd.bak.20261009-CR-2026-10-11 /etc/pam.d/sshd` (also under `~/diwai/backups/`) |
| C7 | Mac | `diwai-mfa-pam-check` installed at `/usr/local/sbin` and run by launchd (`org.diwai.mfa-pam-check`) **hourly and at every boot**: reads `/etc/pam.d/sshd` and reports FAIL if the TOTP line is missing or commented out, sits before `pam_opendirectory`, the module is missing, or `sshd` no longer requires a key then keyboard-interactive. Changes nothing; logs to `/var/log/diwai-mfa-pam.log`, which the Wazuh agent now forwards (agent config edited; backup `ossec.conf.bak-20261009-CR-2026-10-11`). Installed by `scripts/install-mfa-pam-check.sh`. | `launchctl bootout system/org.diwai.mfa-pam-check`; remove the plist and the script; restore the agent config backup and restart the agent |
| C8 | VM | Wazuh decoder `diwai-mfa-pam` and rules **100226** (OK, level 5, heartbeat) and **100227** (FAIL, level 12) added to `local_decoder.xml` and `local_rules.xml`; manager restarted | restore `*.bak-20261009-mfa-pam`; restart the manager |
| C9 | VM | `diwai-control-health` check **15**, "Mac SSH still demands TOTP": fails on a FAIL newer than the last OK, or when no OK has arrived for 2.5 h; also reads the previous day's rotated alerts. The monitor now runs 32 checks. | `diwai-control-health.bak-20261009-chk15` |
| C10 | VM | 389-DS `cn=config` password policy: `passwordExp` off → **on**, `passwordMaxAge` 8640000 → **7776000** (90 days), `passwordWarning` 86400 → **1209600** (14 days); `nsslapd-pwpolicy-local` off → **on** and `nsslapd-pwpolicy-inherit-global` off → **on** (so a local policy changes only what it states) | `dse.ldif.bak-20261009-pwexpiry` in `/etc/dirsrv/slapd-diwai/`; or set the five values back to those shown |
| C11 | VM | Local password policies on `svc-nas` (service account) and `demo_user` (locked reserved identity), each with expiry off, created by `dsconf slapd-diwai localpwp adduser … --pwdexpire off` | `dsconf slapd-diwai localpwp removeuser <dn>` |
| C12 | Mac | Per-user account policy `diwai.password.expiry` on `[USERNAME]` only: password expires every 90 days (`policyAttributeCurrentTime > policyAttributeLastPasswordChangeTime + policyAttributeExpiresEveryNDays * DAYS_TO_SECONDS`), applied by `scripts/apply-mac-password-expiry.sh`, which first proves the rule on a disposable account and refuses to apply while the password is more than 80 days old. `sysadmin` carries no rule (break-glass). | `sudo pwpolicy -u [USERNAME] -clearaccountpolicies` |

C2 and C4 were applied together by `scripts/apply-mac-policy-cr-2026-10-11.sh`, which
requires every rule to parse, saves the live policy first, and restores it if the read-back
does not verify. Staged policy: `~/diwai/staging/mac-account-policy.cr-2026-10-11.plist`.

Existing passwords are unaffected on both hosts: the length rules apply when a password is
next changed. The `[USERNAME]` directory password was not touched and was not changed through
this record; it has its own script and monitor check.

## 3. Verification — by refusal, through the path the control governs

| Test | Host | Result |
|:---|:---|:---|
| Throwaway local account: three wrong passwords, then the correct one | VM | refused (locked); control password accepted before the failures |
| Two wrong passwords, a 310-second pause, one more wrong password, then the correct one | VM | **accepted** — the first two failures had left the 300-second window |
| 6-character, 15-character, and 16-character password changes by a disposable directory user | VM directory | 6 and 15 refused ("must be at least 16 characters long"); 16 accepted |
| Reuse of a previous password; four wrong binds then the correct one | VM directory | both refused for the right reason (history; retry limit) |
| 6-character and 15-character password changes | Mac | both refused |
| Reuse of the previous password | Mac | refused (history enforced) |
| Seven wrong passwords (more than 5, fewer than the old 10), then the correct one | Mac | refused while locked |
| Check 13 with the live alerts file empty (as just after midnight) at a simulated 02:00 | VM | old logic: no heartbeat found, would FAIL; new logic: heartbeat 21.7 h old, PASS |
| Full monitor run after C5 | VM | `RESULT: all 31 checks passed`, including check 13 |
| `ssh -i id_ecdsa_[USERNAME] [USERNAME]@localhost`: password, then a wrong verification code | Mac | refused; the module's accepted-code list unchanged (no code accepted) |
| The same, then a fresh correct code | Mac | accepted: login at 11:43 from 127.0.0.1; the accepted-code list advanced to the current 30-second step |
| `wazuh-logtest` on a sample OK line and a sample FAIL line, before the manager restart | VM | OK fires rule 100226 (level 5); FAIL fires rule 100227 (level 12) |
| A real hourly line from the Mac (11:53:57) | VM | arrived as an alert, rule 100226, two seconds later: the whole path from the Mac file to the VM is proven |
| Check 15 against five synthetic alert histories | VM | OK recently passes; OK 4 h old, FAIL newer than OK, and no lines at all each fail; a FAIL followed by a later OK passes |
| Full monitor run after C9 | VM | `RESULT: all 32 checks passed` |
| Disposable directory entry whose password is marked already expired | VM directory | refused for the right reason: `password expired!` |
| The same entry with the exempt local policy attached | VM directory | still binds: the exemption works |
| Full monitor run after the directory change (C10, C11) | VM | `RESULT: all 32 checks passed` |
| Disposable Mac account with a "expires every 0 days" rule, then the correct password | Mac | refused with `eDSAuthNewPasswordRequired` (-14161), macOS's answer for an expired password (the script's first wording of the test missed this and was corrected) |
| The same account with a 90-day rule | Mac | the fresh password authenticates |
| `sysadmin` rule count after applying to `[USERNAME]` | Mac | 0 (exempt by design); read-back shows `diwai.password.expiry` with 90 days on `[USERNAME]` |

Evidence generators retained as re-runnable scripts: the VM directory test
(`scripts/negative-test-directory-policy.sh`, updated to 15/16 characters; original kept as
`.bak-20261009-14`), the Mac credential test (`scripts/negative-test-credential-policy.sh`,
adds a 15-character boundary and a lockout test that discriminates 5 from 10; original kept
as `.bak-20261009-14`), and the VM lockout driver (a `su`/`expect` script run from the Mac over the
existing SSH session, so no script is written to the VM and `fapolicyd` is not involved).
All throwaway accounts were removed. The failed logins appear in the Wazuh alert stream, as
expected.

## 4. Findings made during this work

1. **The Mac length rule is enforced by its rule text, not by the `minimumLength`
   parameter beside it.** The first run changed only the parameter. The read-back reported
   16, but the new boundary test showed a 15-character password accepted. The staged policy
   now changes the rule text (`.{16,}+`), and the apply script verifies the rule text, not
   only the parameter. A check that read back the parameter alone would have recorded a
   control that was not enforced — the same pattern as DIWAI-CR-2026-09-03.
2. **The documents were wrong about the VM lockout.** The SSP and the Identification and
   Authentication Policy state "5 attempts / 30-minute lockout"; the VM is configured for 3
   attempts and a 15-minute lock. Both configured values meet DoD (at most 5; at least 15
   minutes), so this is a documentation error, not a control gap. It was first noted in
   DIWAI-CR-2026-09-03 and is corrected here (§5).
3. **The Mac allowed 10 failed attempts**, looser than DoD's 5; corrected by C4.
4. **macOS has no separate counting window.** The Mac policy counts consecutive failed
   attempts and releases the lock 900 seconds after the last failure. DoD's value is a limit
   of failed attempts within a 5-minute period. The Mac rule is at least as strict (it does not let
   failures expire), so this is recorded as a documented difference in mechanism, not a gap.
5. **A false start with a test script.** A test script written to `/tmp` on the VM was
   refused by `fapolicyd` ("Operation not permitted"); no attempt was made to bypass the
   control. The test was redone with the driver on the Mac, using the trusted `su` binary
   over the existing session.
6. **The inactivity-heartbeat alert was a nightly false alarm, and the cause was not the 26-hour limit.** The control-health monitor reported "Mac inactivity enforcement job has not reported in 26 h" and recovered the next morning (eight unread recovery notices from 2026-09-26 to 2026-10-09). The Mac job (`diwai-inactivity-enforce`, launchd 04:20) ran daily and exited 0 throughout. Check 13 reads the heartbeat from Wazuh's live `alerts.json`, which restarts at midnight; between 00:00 and the 04:20 run the file held no heartbeat, so the check failed at about 00:15 every night and recovered at 04:30. Failure notices go to the offsite action channel, so this produced a false alarm each night. Raising the threshold would not have helped. C5 fixes the cause. No control was non-functional; this was a monitoring false positive.
7. **TOTP on the Mac host had been silently removed by a macOS update, and was found by reading the configuration, not by an alert.** DIWAI-CR-2026-08-17 (closing POA&M-007) added the TOTP line to `/etc/pam.d/sshd` on 2026-08-06 to 07. Every file in `/etc/pam.d` carries the modification time **2026-09-03 00:29**, consistent with a macOS update rewriting the directory, and the live file had no TOTP line. `sshd` still required a public key and then keyboard-interactive through PAM, which by then checked only the account password. The TOTP module, the secret file and the `sshd` setting were intact; only the PAM line was gone. Nothing detected it: this is the same class of regression as the mSCP rules that macOS updates reset. **The line was missing from 2026-09-03 00:29 until 2026-10-09 11:34, about 36 days.** The 3.7.5 credit (+5, `DIWAI-CR-2026-08-18`) and the 3.5.3 partial credit (+2) rested on that TOTP, and the owner's determinations of 2026-09-13 (101, then 100) were made inside that interval. The control is restored and proven by refusal and by a correct code (C6). A check that reports the line's absence has now been added (C7 to C9): the Mac verifies the line hourly and at every boot, and the control-health monitor fails on a FAIL or on a missing heartbeat. A FAIL cannot be produced on the live system without removing the line again, so the failure paths were tested against synthetic alert histories rather than induced.
8. **The 90-day password expiry stated in three policies was enforced nowhere.** The Identification and Authentication, Acceptable Use and Configuration Management policies all said passwords expire after 90 days. The directory had `passwordExp: off` (`passwordMaxAge` 8640000 was only the stock default) and the Mac had no expiry rule. DoD's value is "never for passwords where MFA is employed", so no rule was required; the owner chose to enforce it, for interactive user accounts only, and to exempt `svc-nas` (cannot change a password interactively), `demo_user` (locked reserved identity) and `sysadmin` (break-glass). Two effects are recorded plainly. The owner's Mac password was 130 days old, so the script refused to apply the rule until the owner had changed it; the first 90-day period began on 2026-10-09. The owner's directory password has not changed since about 2026-05-13 and is stored by four services, so it was **not** backdated (that would have refused their binds): its first 90-day period begins at its next change through `scripts/change-directory-password.sh`.
9. **The Acceptable Use Policy repeated the same stale values** as the Identification and Authentication Policy (14 characters, 24 passwords of history, "5 attempts = 30-minute lockout") and was corrected in the same way.

## 5. Documents corrected or created

Each change was proposed as a diff, approved by the owner, applied through the freshness tool or written to the
canonical store with a verified backup, and the groupfolder rescanned. Backups: `~/diwai/backups/20261009-doc-corrections*`
(nine directories; five reconstructed by reversing the approved diffs, because one backup step failed to run and was
replaced). Revision row **SSP 2.18 (amended 19)**, dated 10/09/2026.

| Document | Applied 2026-10-09 |
|:---|:---|
| SSP (`CUI_System_Security_Plan_v2.18.md`) | §3.1.8 and Appendix E.4: real lockout values and length 16; "weekly patch review" corrected to monthly in 3.7.1, 3.11.3, 3.14.1, 3.14.3 and E.3; 3.6.3 (tabletop conducted and signed 2026-08-03) in the known-gaps list, the control row and the deficit table; the §11 deductions ledger rebuilt to 100/110 (four open deductions, 45 points shown as recovered, a score history); 3.5.3 and 3.7.5 control rows and the §3.2 Mac MFA paragraph; revision row amended 19 |
| Identification and Authentication Policy (DIWAI-IAP-001) | length 16, history 6 (it said 24), real lockout values, FreeIPA examples replaced by a table of the real settings; account types allowed (including reserved identities) and prohibited; intended system usage and the circumstances for disabling accounts (3.1.1 d.02, f.04, f.05); notification periods (24 hours each); identifier reuse (never), naming the register |
| System and Information Integrity Policy (DIWAI-SI-001) | flaw remediation (SI-2) aligned to SSP E.3 and DIWAI-PR-001 (monthly review; 72 hours from detection for PATCH-class CRITICAL; `dnf-automatic` download-only); alert processing; Procedure 2 replaced by a pointer to the procedure; components no longer supported by their publisher (3.16.02) |
| Patch Review Procedure (DIWAI-PR-001) | remaining "weekly" wording corrected to match the monthly cadence |
| Risk Management Policy (DIWAI-RA-001) | supply chain plan, lifecycle coverage (3.17.01), under section 7 |
| Acceptable Use Policy (DIWAI-AUP-001) | section 10.1, use of external systems (3.1.20) |
| Audit and Accountability Policy (DIWAI-AAP-001) | event-type review frequency; time stamp granularity |
| Acceptable Use Policy, section 2.2; Configuration Management Policy, baseline table; Identification and Authentication Policy, expiration; SSP Appendix E.4 (new row) | password requirements brought to the values in force: length 16, expiration scope and the three exemptions, history 6, real lockout values; SSP revision row amended 19 gains the expiration item |
| Retired Identifiers Register (**new**, `DIWAI-IA-REG-001`, Evidence folder) | rule, reserved test and demo identities, review log, baseline of identifiers in use on the Mac, the VM and the directory |

## 6. Open items

- **Certificate renewal.** The certificate in service expires 2026-11-08 17:52 GMT; renewal opens about 2026-10-09 11:52 MDT. Confirm both legs (Mac nginx, 389-DS) took the new certificate after the first renewal run. Not part of this record's changes.
- **`svc-nas`** (the NAS's directory bind account, hourly) has not yet been seen to bind after C1. No password change is involved, so no failure is expected; confirm an `err=0` bind in the directory access log. Its next rotation must meet 16 characters.
- **`sysadmin` break-glass account** (Mac): confirm its password meets 16 characters at its next change. Succession access depends on it.
- **`[USERNAME]` directory and Mac passwords** meet 16 only when next changed; the directory change continues to go through `scripts/change-directory-password.sh`.
- **Password expiration, remaining.** The owner's Mac password expires about **2027-01-07** (90 days from 2026-10-09); nothing warns beyond the macOS prompt, so a calendar reminder is advisable. The owner's directory password begins its first period at its next change, which should be soon: use 16 or more characters and `scripts/change-directory-password.sh`.
- **Post-macOS-update routine.** Add a line next to the mSCP fix so a person reads the TOTP check's result after each update, and does not wait for the next hourly run.
- **Tabletop record `DIWAI-IR-TTX-001`:** the header date, the end time, the policy-usability checkboxes and the duplicated section numbers are incomplete (the exercise was held and signed 2026-08-03).
- **Remaining DoD comparison items** (`ODP looser than DoD - flagged`): quarterly reviews of the authorized software list and the component inventory; removable media; audit event list; re-authentication circumstances; audit-failure response actions; and the wording items.

## 7. SPRS effect

**None to the score of record by this record.** This record aligns two parameters with the DoD Rev 3 values, corrects
documentation and restores the Mac TOTP; no requirement is added, removed or re-weighted, and the figure of record
(100/110 under the evidence-strict basis, Rev 2) is unchanged. **For the owner's determination:** the 3.7.5 and 3.5.3 credit rested on a control that was absent from 2026-09-03 to 2026-10-09 (finding 7), an interval that includes the 2026-09-13 determinations. The control is now restored and proven. This record states the interval; it does not decide whether any recorded figure is adjusted.

---

## 8. Sign-off

|                |                                                |
|:---------------|:-----------------------------------------------|
| **Name**           | [SYSTEM-OWNER]                              |
| **Roles**          | System Owner; ISSO; System Administrator       |
| **Signature**      | \_[SYSTEM-OWNER] _____________________________\_ |
| **Date**           | \____9 October 2026__________________\_          |

---

**Distribution:** Limited to authorized personnel
