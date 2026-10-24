> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MAC INACTIVITY JOB RECORDED AND RETESTED; DOCUMENTS CORRECTED; 3.5.6 POINT STAYS WITHHELD UNTIL THE VM IS COVERED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-17** |
| **Date opened** | October 19, 2026 |
| **Status** | **DOCUMENTS CORRECTED; DISABLE PATH RETESTED; THE JOB'S VERIFICATION CHECK FIXED, REINSTALLED AND RETESTED (§3A). Owner approved 2026-10-23. Two items open (§5). Addendum §3B (warning path) 2026-10-23** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host (test only; no setting changed). The services VM was not changed |
| **Addresses** | **3.5.6** (Rev 2: disable identifiers after a defined period of inactivity; **withdrawn in Rev 3**, whose item 03.01.01 f.02 covers accounts inactive for an organization-defined time); **3.4.3** (change control); **3.3.1** (the job's log) |
| **Authority** | Owner decisions of 2026-10-19: approve the corrected wording; retest the disable path; keep the 3.5.6 point withheld until the VM's local accounts are covered; approve re-approval of the runbook card |
| **Related** | `DIWAI-CR-2026-09-08` (directory half), `DIWAI-CR-2026-10-15` (the job's log reaches Wazuh again), POA&M-076 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

On 2026-10-19 the local AI models, asked how diwai disables inactive accounts, answered that the Mac has no enforcement. They were repeating the SSP, the POA&M and a runbook card. A read-only audit found those documents out of date: a daily Mac job has enforced the 90-day limit on local accounts since 2026-09-13. The job also had no change record of its own (its header cites `DIWAI-CR-2026-09-09`, which is the attached-storage record), and its 2026-09-13 proof had logged an unexplained `verified=NO`. This record fixes the documents, records the job, and explains the anomaly.

## 2. The job (recorded here for the first time)

1. **Installed** 2026-09-13 by `~/diwai/scripts/mac-inactivity-356.sh` under POA&M-076: `/usr/local/sbin/diwai-inactivity-enforce` (root:wheel, 755; source of record `~/diwai/scripts/diwai-inactivity-enforce`), run daily at 04:20 by `/Library/LaunchDaemons/org.diwai.inactivity-enforce.plist`; log `/var/log/diwai-inactivity.log`, forwarded by the Wazuh agent (rules 100222 to 100224; control-health check 13).
2. **Covers** every local account with UID 500 or higher and a real login shell, except `sysadmin`, the break-glass account, which is exempt by owner direction (2026-09-13). Today only `[USERNAME]` is covered.
3. **Acts:** an account idle 90 days or more is disabled with `pwpolicy -disableuser`; a warning is logged from 80 days. An open session (`who`) or a recorded login (`last`) resets the clock; a logged-in account is never disabled; an account first seen starts its clock that day.
4. **Why a job and not a policy:** macOS records no last-login time on this host, so a `pwpolicy` inactivity rule always passes (tested 2026-09-13).
5. **Record of runs:** an unbroken daily run from 2026-09-13 to 2026-10-19 04:20; every run logged `disabled=0`.

## 3. Retest of the disable path (2026-10-19)

Script `~/diwai/scripts/retest-inactivity-disable.sh`, reviewed and run with `sudo` by the owner. It created one disposable account with a random password (never displayed), let the job see it, backdated it 100 days, ran the real job, then deleted the account. Transcript: `~/diwai/logs/retest-inactivity-disable-20261019-114218.log`.

| Step | Result |
|:---|:---|
| Account authenticates before the test | Yes |
| Job run on the backdated account | `DISABLED ... idle_days=100 limit=90 verified=NO` |
| Login with the correct password afterwards | **Refused**; `pwpolicy` itself reported "account is disabled" |
| The record the job checks (`AuthenticationAuthority`) before and after | Identical: only `;ShadowHash;`, no disabled marker |
| Third run | Disabled the same account again and logged `verified=NO` again |
| `[USERNAME]`, `sysadmin` afterwards | Both still enabled |

**Conclusion.** The disable works. The job's way of confirming it does not: it looks for a `;DisabledUser;` marker that macOS on this host does not write there. This reproduces the unexplained `verified=NO` of 2026-09-13 and explains it. **Recorded as a limitation of the job's verification step, not of the enforcement.** Consequences: the "verified" field in the log cannot be relied on, and an account that really is disabled is disabled again, and logged again, on every run (so Wazuh rule 100222 would fire nightly after a real disable). **The job was not changed by this first retest.** It was corrected afterwards, with the owner's approval, as recorded in §3A.

## 3A. Verification check fixed, reinstalled and retested (2026-10-19, later)

1. **What was found.** The source of record (`~/diwai/scripts/diwai-inactivity-enforce`, edited 2026-09-13 15:20) already contained a corrected check that was never installed (the installed copy dated 15:17 was older). Reading that source, the corrected check had its own flaw: one of its signals treated "the policy command's answer lacks the words 'allows user'" as proof of disabled. An empty, failed or unexpected answer would have made an **enabled** account look disabled, and the job would have skipped it forever, switching the control off without a sign.
2. **What was changed.** The check now needs positive evidence only: the system's own words "account is disabled" (as printed by `pwpolicy`, captured in the first retest), the legacy `isDisabled=1` marker, or the `;DisabledUser;` tag. The job's header now says the control was recorded in this change record and that `DIWAI-CR-2026-09-09`, first cited there, is a different record. The log line gains `signals=...`.
3. **Tests.** 15 new unit tests (the Mac job had none). Putting the old negative check back makes four of them fail, so they do detect the flaw. Source hash `11d00de41fcfa814...`.
4. **Install.** `install-mac-inactivity-fix.sh` (owner ran it with `sudo`; checks the hash, backs the old copy up as `/usr/local/sbin/diwai-inactivity-enforce.bak-20261019`, installs root:wheel 755). The installed hash matches the source. The LaunchDaemon and schedule were not touched.
5. **Retest.** First attempt (14:11) failed four checks because the disposable account reused the name `diwaiidletest` and **was disabled from the moment it was created**: macOS appears to keep a disabled state by account name, so a new account with the name of one the job had disabled and deleted starts out disabled (a likely cause; the fresh-name run did not reproduce it). The retest was changed to use a new name each run, to re-enable the account before deleting it, and to stop at once if the account does not start enabled. Second attempt (14:12, transcript `retest-inactivity-disable-20261019-141257.log`): **all five checks passed**: the corrected check reads an enabled account (the test account and `[USERNAME]`, read-only) as enabled; the job disables the backdated account and its own confirmation says `verified=yes` (`signals=aa:0,isDisabled:0,policy_denies:1`: only the system's own words detect the state); `pwpolicy` says the account is disabled; the correct password is refused; a third run does not disable it again.
6. **A consequence worth knowing.** If an account that the job disabled is deleted and a new account is later created with the same name, the new one may start disabled. Recovery: `sudo pwpolicy -u <name> -enableuser`.

## 3B. Addendum, 2026-10-23: the 80-day warning path proven to the Wazuh alert

**Test.** `scripts/warn-test-mac.sh` (owner ran it with `sudo`, 2026-10-23 10:19; transcript `warn-test-mac.log` saved in `assessment-2026-08/evidence-CR-2026-10-19-partC/`) on a disposable account (`diwaiwarn101931`, random password never printed): first sight (no warning), clock backdated **85 days**, one real run of the installed job with `DIWAI_INACTIVITY_TEST=1`. Then, on the VM, `vm-check-warning-alert.sh` (read-only) looked for the alert.
**Results.** (1) The job logged `WARNING user=diwaiwarn101931 idle_days=85 disable_in=5 test=1` at 10:19:35. (2) The account was **not** disabled: the correct password was still accepted and `pwpolicy` did not say disabled. (3) **The Wazuh manager raised alert rule 100223 one second later** (10:19:36, level 10, "Mac local account approaching the 90-day inactivity disable (3.5.6)", agent `[USERNAME]s-Mac-mini.local`, exactly one alert). (4) The account and its state entry were removed; `[USERNAME]` and `sysadmin` were untouched.
**Limits.** **The alert is not set to send mail** (`mail` flag false on the alert): the owner sees a Mac warning only by looking at the Wazuh alerts, or through the control-health monitor, which fails check 13 when a real (untagged) WARNING appears in the last day, and whose own alerts go to the owner's VM mailbox. The test line carried `test=1`, so the monitor ignored it; the monitor's reaction to a real warning was shown earlier by its own test script, not by this run. A backdated disposable account stands in for an account that really aged 80 days. The owner's Gmail could not be searched (the connector lacks read permission). **No control determination, no SPRS change.**

**Live proof to the owner's Gmail (same day, after the owner approved it).** The test was repeated at 10:33:10 as `scripts/warn-test-mac-live.sh`, **without** the `test=1` tag (disposable account `diwaiwarn103306`, backdated 85 days, not disabled, then deleted). The control-health monitor's next run (10:45:41) **failed check 13**: "Mac account nearing inactivity disable: WARNING user=diwaiwarn103306 idle_days=85 disable_in=5 (3.5.6) - log in to reset", mailed the owner's Gmail ("new failure(s)"), and the relay accepted it at 10:45:44 (`status=sent`, 250 OK). **The owner confirmed receipt in the Gmail inbox** (sender `root <[EMAIL-REDACTED]>`, 10:45 AM, subject "[diwai] CONTROL HEALTH FAILURE on services.[DOMAIN.ORG] — new failure(s)", naming the account). The route is the monitor's, by design (Wazuh's own email is disabled, `DIWAI-CR-2026-09-07`): job log line, Wazuh alert 100223, monitor check 13, Gmail. Side effect, expected: the monitor reads 32 of 33 until the warning is older than its 26-hour window, then recovers on its own (recovery notice to the local root mailbox).

## 4. Documents corrected (working copies, then published)

1. **SSP v2.18, amendment 23:** §1.4 Key Findings (the 3.5.6 item), the open-deductions table, and Appendix E.4. They now say: directory enforced; Mac enforced by the daily job; **VM local accounts not yet covered; the 3.5.6 point stays withheld.** The 2026-09-13 amendment rows are history and were left as written.
2. **POA&M v1.32, amended 6:** the POA&M-076 status cell, and a new dated paragraph. The 2026-09-13 finding paragraphs were left as written.
3. **Runbook card `INACTIVE_ACCOUNT_NOT_DISABLED`:** evidence, repair and status lines. The card is ISSO-approved and the owner approved re-approval (2026-10-19).
4. **Change record `DIWAI-CR-2026-09-08`:** one pointer line added (body unchanged): the Mac statement is correct only as of that morning.
5. The corrected SSP, POA&M, card and the new records were re-ingested into the local libraries so the models read the current wording.

## 5. Open items

1. **Resolved by `DIWAI-CR-2026-10-18`: VM local accounts.** The VM job is built, proven and enabled; its first scheduled run is 2026-10-20 04:25. The documents still say "VM not covered" until the owner decides what they should say about the 3.5.6 point.
2. **The job has never disabled a real account.** Only disposable test accounts. (The 80-day warning path was proven to the Wazuh alert on 2026-10-23, §3B; the alert sends no mail.) A real account has to age 90 days for that to happen. An overnight test of the 04:20 schedule on an aged disposable account is available if the owner wants it.
3. **Resolved (§3A): the verification check.**
4. **Resolved (§3A): the script header's citation.**
5. **Open: the 3.5.6 point and the document wording** (SSP, POA&M, runbook card) now that both hosts are covered: the owner's decision.

## 6. Verification

| # | Check | Result |
|--:|:---|:---|
| 1 | Retest: disable works (login refused, `pwpolicy` agrees) | **Pass** |
| 2 | Retest: `verified=NO` reproduced and explained | **Pass** |
| 3 | `[USERNAME]` and `sysadmin` untouched; test account removed | **Pass** |
| 4 | SSP (amendment 23), POA&M (amended 6), runbook card, CR-09-08 pointer corrected; no score change | **Pass** (card tests pass; SSP, POA&M and CR-09-08 published and in sync) |
| 5 | Corrected text read by the local AI | **Partly tested** (three later test runs quoted the new wording; a clean rerun is still to do) |
| 6 | Mac job tests (15) and the deliberate-break check | **Pass** |
| 7 | Corrected job installed; hash equals the reviewed source; backup kept | **Pass** |
| 8 | Second retest: five of five checks | **Pass** (§3A) |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
