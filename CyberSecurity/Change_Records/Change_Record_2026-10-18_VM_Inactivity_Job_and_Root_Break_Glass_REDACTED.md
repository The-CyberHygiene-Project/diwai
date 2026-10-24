> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — VM INACTIVITY JOB BUILT, PROVEN AND ENABLED; VM ROOT PASSWORD RESET AND BREAK-GLASS CONFIRMED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-18** |
| **Date opened** | October 19, 2026 |
| **Status** | **IMPLEMENTED AND PROVEN (§6), INCLUDING THE CONTROL-HEALTH MONITOR. Owner approved 2026-10-23. Four items open (§5). Addenda §6A (monitor check 15 regression) §6B (warning mail proven) and §6C (also to Gmail) 2026-10-23** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Services VM (job, timer, Wazuh manager configuration, `root` password). The Mac host was not changed |
| **Addresses** | **3.5.6** (Rev 2: disable identifiers after a defined period of inactivity; withdrawn in Rev 3, whose 03.01.01 item f.02 covers accounts inactive for an organization-defined time); **3.4.3** (change control); **3.3.1** (the job's log); **3.5.10 / 03.05.12** (the `root` credential) |
| **Authority** | Owner decisions of 2026-10-19: same 90 days and 80-day warning on the VM; build the job, its timer and the log collection; `root` is exempt from the inactivity rule and its password does not expire on a schedule; the owner reset the `root` password |
| **Related** | `DIWAI-CR-2026-10-17` (the Mac job and the corrected documents), `DIWAI-CR-2026-10-12` (VM password expiry; its item 2 on `root`), POA&M-076 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

After `DIWAI-CR-2026-10-17` the Mac's local accounts were covered by an inactivity job; the VM's local accounts were not, and that is the half that kept the 3.5.6 point withheld (owner decision 2026-10-19). Only two accounts can log in on the VM, `root` and `[USERNAME]`. The directory's 90-day limit does not reach them, because the VM resolves users from local files only (`sssd` is off). A second finding made the VM job unsafe to build at first: **the owner no longer knew the `root` password**, so the VM had no working break-glass login. A job that can expire `[USERNAME]` is only acceptable if a tested way back in exists.

## 2. Scope

**A. `root` password reset and break-glass confirmed.** The owner reset the `root` password with `sudo passwd root` from `[USERNAME]` and tested a `root` login at the VM console. The password was chosen and typed by the owner and was never seen by the assistant. SSH root login is off: `sshd -T` reports `permitrootlogin no`, so `root` is console-only. Owner decisions recorded here: `root` is **exempt from the inactivity job**, and its password **does not expire on a schedule** (maximum age 99999 days, confirmed). Under the DoD Rev 3 values the owner adopted for this system (03.05.12.e: at least every three years for an authenticator with no second factor), the `root` password is due for change **by 2029-10-19** and after any incident or evidence of compromise; that date belongs in the credential register (§5.5).

**B. The VM job.** New files, all on the VM: `/usr/local/sbin/diwai-inactivity-enforce-vm` (root:root 755, `bin_t`; source of record `~/diwai/scripts/diwai-inactivity-enforce-vm`), `/etc/systemd/system/diwai-inactivity-enforce.service` and `.timer`, `/var/lib/diwai-inactivity/` (mode 700, first-seen state) and `/var/log/diwai-inactivity.log` (644). The timer runs daily at **04:25** with `Persistent=true` (it catches up after an outage). Rules:
1. Covers every local account with UID 1000 or higher and a real login shell. Today that is only `[USERNAME]`.
2. The idle clock is the later of the last login in the login record and any open session; an account never seen to log in starts its clock the day it is first seen.
3. Warning line and a mail to `[USERNAME]` at 80 days idle; at 90 days the account is set to expired (`chage -E 0`), which PAM refuses for every login method including SSH keys.
4. **Safeguards:** at most one account is disabled per run; nothing is done unless the clock is synchronized (a skipped run logs a SKIPPED line and no heartbeat); an account that is already expired is skipped, never disabled again; an account with an open session is never disabled.
5. **Confirmation:** the job reads the expiry date back with `chage -l`, the system's own report. It does not look for a marker the system may not write (the cause of the Mac job's `verified=NO`, `DIWAI-CR-2026-10-17`).
6. Log format and program name match the Mac job's, so Wazuh rules 100222 (DISABLED), 100223 (WARNING) and 100224 (RUN) apply unchanged. Recovery after a disable: `chage -E -1 <user>`, as `root` at the console.

**C. Wazuh manager.** One `<localfile>` block (syslog format) for `/var/log/diwai-inactivity.log` was added to `/var/ossec/etc/ossec.conf` (backup `ossec.conf.bak.20261019-vm-inactivity`, XML checked) and `wazuh-manager` was restarted. Alerting paused briefly during the restart.

**E. Control-health monitor (found and fixed the same day).** Check 13 (Mac inactivity) finds the Mac's heartbeat by log path alone (`/var/log/diwai-inactivity.log`), and the VM job writes to the **same path** on the Wazuh manager. From 14:04, when the VM log went live, check 13 was reading the VM's heartbeat as the Mac's: replaying it with the Mac silent for 30 hours and the VM reporting gave **"OK" for the Mac**, so a stopped Mac job would have been masked until the VM's heartbeat also stopped, and a VM warning or disable would have been reported as a Mac one. Fix: the check became one shared function, `inactivity_check`, that tells the two apart by the host name inside each log line (`[USERNAME]s-Mac-mini` against `services`). Check 13 uses it for the Mac with its wording unchanged, and a new **check 16** uses it for the VM (same rules: a disable or a warning in the last 26 h, or no heartbeat in 26 h, turns it red; test-tagged lines are ignored). Backup `/usr/local/sbin/diwai-control-health.bak-20261019-vminact`; 16 lines added; everything before check 13 and from the report onward is unchanged. Source: `~/diwai/scripts/vm-monitor/`.

**D. Not changed:** the Mac, the directory, the `fapolicyd` rules and trust list, every other VM service, any account other than the temporary test account, the 3.5.6 score.

## 3. Rollback

`systemctl disable --now diwai-inactivity-enforce.timer`; remove the two unit files and the job file and run `systemctl daemon-reload`; put `/var/ossec/etc/ossec.conf.bak.20261019-vm-inactivity` back over `ossec.conf` and restart `wazuh-manager`; put `/usr/local/sbin/diwai-control-health.bak-20261019-vminact` back over the monitor (check 16 goes away, check 13 returns to path-only matching, which re-opens the masking problem). The `root` password cannot be rolled back; it can be changed again with `sudo passwd root`.

## 4. Execution log (2026-10-19)

1. The build was written and tested first: 27 unit tests against a fake system (also checked by deliberately breaking four rules, each of which made a test fail) and a parse check under the VM's Python 3.9.25.
2. 13:45 Staged the files on the VM. **The staged job could not be read by `[USERNAME]`** ("Operation not permitted"): the VM's file-access allowlist (`fapolicyd`) refuses untrusted Python files to non-root users. A read-only diagnostic (13:49) showed the rules: root running a trusted program may open and run anything, so the job, run as root from systemd, needs no trust-list entry. Nothing was added to the trust list and nothing was worked around.
3. 13:52 Step 1 installed the job and units without enabling the timer (file hashes checked first).
4. **Proof, three attempts.** 13:54: everything passed except the independent refusal test, which was **inconclusive** (`runuser` lets `root` bypass the account check). 13:58: the control login failed before the expiry (`su` answered "Permission denied" to an ordinary test user; the reason was not confirmed, a wheel-only `su` restriction is the likely one), so the later refusal proved nothing; the script's verdict flagged it, although it still printed a pass line for the refusal itself. 14:01: the test now asks PAM's account stack (the one `sshd` uses) directly; **all checks passed.**
5. 14:04 Step 3: Wazuh log collection added, manager restarted, timer enabled, one real run, alert seen.
6. 14:08 to 14:40 Monitor: found the collision (§2.E), wrote the shared function, tested it with 13 crafted cases on the VM and replayed the old logic to show the masking, rehearsed the patch on a copy (which caught a bug in my first patch: it would have placed the new check at the top of the file because my search for the section marker also matched the same words inside a comment), then applied it at 14:25. The manual run of the monitor then waited about 15 minutes on its probe of the Mac's staging folder, because run from a terminal its standard input was the terminal, which the remote end waited on; it finished when the owner pressed Ctrl-D. Under the timer the same probe returns at once. The patch script now closes input and limits the run to five minutes.

## 5. Observations and open items

1. **The first two proof attempts did not pass,** for reasons in the test, not the job (§4.4). They are recorded so the evidence is not read as a clean first run.
2. **Open: the `fapolicyd` rule** `allow perm=any uid=0 trust=1 : all` means the allowlist restricts non-root users and untrusted programs but not scripts run as root by a trusted program. If the SSP describes the allowlist as permit-by-exception for every process, that wording may be broader than the configuration. Not changed; the SSP text is to be checked.
3. **Resolved (§2.E): the monitor.** It now checks the VM job's heartbeat (check 16) and no longer lets one host's heartbeat stand for the other's. This record's earlier statement that the existing rules "apply unchanged" was true of Wazuh's rules and false of the monitor; it was corrected the same afternoon.
4. **Open: the job has not yet disabled a real account.** `[USERNAME]` is the only covered account and is in regular use, so a real disable is not expected soon. The 80-day warning mail was exercised on 2026-10-23 on a disposable account (§6B); the Mac job's warning path (Wazuh rule 100223) was proven to the alert on 2026-10-23 (`DIWAI-CR-2026-10-17` §3B); that alert sends no mail.
5. **Open: credential register.** The `root` password's three-year due date (2029-10-19) and the other no-second-factor authenticators are not yet recorded anywhere (see the password-expiry change package, a draft).
6. **Resolved: the Mac job's verification check** (`DIWAI-CR-2026-10-17` §3A).
7. **Open: small leftovers** on the VM, in `[USERNAME]`'s home folder: the staging folder, the diagnostic, proof and monitor transcripts, `sshd-root.txt`, `control-health.b64`. Twelve test-tagged lines (three proof runs) are in the VM job's log; they were written before Wazuh collected the log.

## 6. Verification

| # | Check | Result |
|--:|:---|:---|
| 1 | Unit tests (27) and deliberate-break check | **Pass** |
| 2 | Proof: account accepted by PAM before; first run does not disable | **Pass** (14:01) |
| 3 | Proof: backdated 100 days, disabled, the job's own read-back `verified=yes`, `chage -l` shows the expiry | **Pass** |
| 4 | Proof: PAM (the `sshd` stack) then **refuses** the same account (rc=13, "User account has expired") | **Pass** |
| 5 | Proof: third run does not disable it again; exactly one new DISABLED line | **Pass** |
| 6 | Proof: `root` and `[USERNAME]` unchanged; test account deleted | **Pass** |
| 7 | Timer enabled, next run Tue 2026-10-20 04:25 | **Pass** |
| 8 | Real run logged; Wazuh alert raised within one second (rule 100224, level 5) | **Pass** |
| 9 | `root`: console login works; SSH root login off; password age setting 99999 | **Pass** (login tested by the owner; the other two read back) |
| 10 | Control-health monitor clean after the Wazuh restart | **Pass** (run at 14:16: 32 rows, 0 not OK) |
| 12 | Shared check: 13 crafted-alert cases on the VM, including "Mac stale, VM fresh: the Mac must fail" | **Pass** (13 of 13) |
| 13 | Old logic replayed with the Mac silent 30 h and the VM reporting | **Showed the fault** (old: OK; new: FAIL) |
| 14 | Patched monitor run once: checks 13 and 16 both OK | **Pass** (33 of 33, 0 not OK) |
| 15 | Patched monitor run by its own timer | **Pass** (14:45 run: 33 rows, 0 not OK, checks 13 and 16 OK) |
| 16 | SSP (amendment 24), POA&M (amended 7) and the runbook card updated to say both hosts are covered; no score change | **Pass** (card tests 51 and full suite 427 pass; documents published and in sync) |
| 11 | A real 04:25 scheduled run | **Pending** (2026-10-20 04:25) |

Transcripts (on the VM, `~[USERNAME]`): `vm-inactivity-proof-20261019-140154.log` (passing proof), `vm-inactivity-enable-20261019-140444.log`.

## 6A. Addendum, 2026-10-23: monitor regression found and fixed (check 15)

**What was wrong.** The monitor patch of 2026-10-19 14:25 (§6) rewrote section 13 and renamed its helper `age_of` to `ia_age_of`. **Check 15 (Mac SSH still demands TOTP, 3.5.3 / 3.7.5) still called `age_of`**, which no longer existed. From 14:25 on 2026-10-19 every run logged `line 415: age_of: command not found` and `line 415: [: : integer expression expected` (576 log lines in the three days to 2026-10-23). The error made the comparison false, so **check 15 could report OK when the Mac's hourly TOTP report was stale, and a newer "TOTP no longer demanded" line could be missed.** The check read OK on every run in that period; whether those OKs were genuine cannot now be shown. The cause was my own patch; the §6 verification looked only at checks 13 and 16 and the total count (33 of 33), not at the monitor's error output.
**Tested before the fix** on a rebuilt copy of the installed script (the patch re-applied to the 2026-10-19 copy gave exactly the installed size, 30,130 bytes), with a stand-in for GNU `date`: stale report gave **OK** (wrong) with two errors; fresh gave OK; missing gave FAIL. After the fix: stale **FAIL**, fresh OK, missing FAIL, no errors.
**The fix (owner ran it with `sudo`, 2026-10-23 09:32):** `scripts/vm-monitor/vm-monitor-fix-ageof.sh` backs the monitor up to `/usr/local/sbin/diwai-control-health.bak-20261023-ageof`, inserts the original one-line `age_of` definition before section 15, checks the file with `bash -n`, and runs the monitor once. Result: file 30,442 bytes; **33 rows, 0 not OK; check 15 OK; 0 errors**; transcript `~/vm-monitor-fix-ageof-20261023-093221.log` on the VM. Rollback: copy the backup over the monitor.
**Limits.** The OK status of check 15 from 2026-10-19 to 2026-10-23 is unproven. The fix was shown with a stand-in test and one live run, not by making the real Mac's TOTP report go stale. **Lesson:** after patching the monitor, read its error output as well as its results. **No control determination, no SPRS change.**

## 6B. Addendum, 2026-10-23: the 80-day warning and its mail proven on the VM

**Test.** `scripts/vm-inactivity/vm-inactivity-4-warnmail.sh` (owner read it and ran it with `sudo` on the VM, 2026-10-23 09:37; transcript `~/vm-warnmail-20261023-093713.log` on the VM). It created one disposable account (`diwaiwarntest`, random password never printed), let the job see it (first sight: no warning), backdated its clock **85 days** (inside the 80 to 89 day warning window), and ran the job once more with `DIWAI_INACTIVITY_TEST=1`.
**Results (all passed).** (1) The job logged `WARNING user=diwaiwarntest idle_days=85 disable_in=5`, tagged `test=1` so the control-health monitor ignores it. (2) The account was **not** disabled: the sshd account-management stack (`pamacct.py`) still accepted it and `chage -l` showed "Account expires: never". (3) The warning mail was handed to postfix and **delivered** (`status=sent`, queue empty) to `[EMAIL-REDACTED]`, subject "diwai VM: account diwaiwarntest will be disabled in 5 day(s)", with the job's recovery sentence. (4) The test account and its state entry were removed; `root` and `[USERNAME]` were untouched. One test message remains in the owner's VM mailbox as evidence.
**Limits.** The mail reaches the owner's **local VM mailbox only**: there is no forwarding to an outside address, so the owner sees it only by reading that mailbox (the same mailbox the control-health monitor's alerts use). The Mac job sends **no mail**; its warning is a log line that Wazuh rule 100223 turns into an alert (proven separately, `DIWAI-CR-2026-10-17` §3B; the alert is not set to send mail). The test used a backdated disposable account, not an account that actually aged 80 days. **No control determination, no SPRS change.**

## 6C. Addendum, 2026-10-23: the VM warning mail now also goes to the owner's Gmail (proven by receipt)

**Why.** §6B showed the 80-day warning mail reached only the owner's local VM mailbox, which the owner reads only through webmail. A warning that is not seen does not protect against a lockout.
**Change (owner decision 2026-10-23, run with `sudo` at 10:28:56).** One line of the installed job `/usr/local/sbin/diwai-inactivity-enforce-vm` (source of record `scripts/diwai-inactivity-enforce-vm`; installed by `scripts/vm-inactivity/vm-inactivity-5-mailto.sh`, which checks the file against `SHA256SUMS`, parses it, backs up the installed job and shows the difference): `MAIL_TO = "[USERNAME]"` became `MAIL_TO = "[USERNAME], [EMAIL-REDACTED]"`. Nothing else in the job changed (9,057 to 9,152 bytes; new SHA-256 `09b45138c97e5ca76f8d4c9a29d78ff9a74fc5d468e59d3c40424d7ceada53f3`; root:root 755). The timer, the schedule (next run 04:25 on 2026-10-24) and every account are unchanged. Backup: `/usr/local/sbin/diwai-inactivity-enforce-vm.bak-20261023-mailto`; rollback is a copy back.
**Proof (the owner's rule: claim only if the mail arrives).** Test `vm-inactivity-4-warnmail.sh` rerun on a disposable account at 10:30:50: WARNING logged, the account not disabled, local delivery `status=sent` at 10:30:50, and **the relay `smtp.gmail.com:587` accepted the Gmail copy at 10:30:52 (`status=sent`, 250 2.0.0 OK). The owner confirmed receipt in the Gmail inbox** (sender `root <[EMAIL-REDACTED]>`, 10:30 AM, subject "diwai VM: account diwaiwarntest will be disabled in 5 day(s)", the job's full text).
**Notes.** The test script's own Gmail check reported "no relay line" on that run because the relay takes about two seconds after the local delivery and the script looked too early; it now waits up to 20 s. The two earlier runs of the warning test (09:37 to 10:28) were on the old job and left three harmless test messages in the local mailbox. **Not covered:** the Mac job's warning to Gmail, which goes through the control-health monitor (Wazuh's own email is disabled by design, `DIWAI-CR-2026-09-07`), and is to be shown separately. **No control determination, no SPRS change.**

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
