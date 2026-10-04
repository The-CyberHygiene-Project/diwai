> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# PLAN OF ACTION AND MILESTONES (POA&M)

## [DOMAIN.ORG] SecureMac Reference System

**Document Control:**

| Field                | Value                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------|
| **System Name**          | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2)                                             |
| **System Owner**         | [SYSTEM-OWNER]                                                                              |
| **Organization**         | [DOMAIN.ORG] (Do It With AI)                                                                   |
| **Classification**       | Controlled Unclassified Information (CUI)                                                   |
| **Version**              | 1.32                                                                                         |
| **Date**                 | September 13, 2026                                                                              |
| **SSP Reference**        | CUI_System_Security_Plan_v2.18.md (§10, Appendix D) — reissued 2026-08-12. **The SSP↔POA&M pin is mutual:** v2.18 cites this document and this document cites v2.18. Bumping either without the other breaks the pair — the defect `DIWAI-MFR-2026-08-12` records |
| **SPRS Score**           | **100/110 — 3.5.6 WITHHELD 2026-09-13 under the evidence-strict basis** (inactivity disable defined but not enforced; POA&M-076). Earlier the same day: **101/110 — RECOMPUTED 2026-09-13 on tested recoveries** (evidence-strict basis, owner determination 2026-09-13; strict 800-171A objectives met 35/110 reported separately) — 3.14.1 +5 (`DIWAI-CR-2026-09-04`), 3.3.4 +1 (`DIWAI-CR-2026-09-07`), 3.10.3 +1 (`DIWAI-PE-LOG-001` §6); revision 1.32 amended 2. Earlier the same day: **94/110 — RE-DETERMINED 2026-09-13 on negative-test evidence** (revision 1.32 amended; `DIWAI-CR-2026-09-03`). Earlier the same day: **93/110 — DETERMINED 2026-09-13.** Owner determination on the `DIWAI-VS-001` §4 dispute (3.1.8 / 3.5.7 / 3.5.8 credential policy), outstanding since 2026-08-07. **Standing rule applied: where a figure is in dispute, the lower — more conservative — value is reported.** The register's open-deduction arithmetic yields 94/110; the determination withholds one further point. Weights VERIFIED against DoD Assessment Methodology v1.2.1. Closes `DIWAI-VS-001` Recommendation 1 |
| **Compliance Framework** | NIST SP 800-171 Rev 2 / FIPS 140-2                                                          |
| **Supersedes**           | CUI_[DOMAIN.ORG]_Unified_POAM_v1.31.md (Version 1.31, 2026-09-13). Earlier: CUI_[DOMAIN.ORG]_Unified_POAM_v1.30.md (Version 1.30, 2026-08-08). **Filename and internal version remain aligned**, as realigned at v1.30 — the earlier v1.7 file had absorbed revisions 1.7–1.29 without the filename moving. Revision-history rows 1.7–1.29 are unchanged and remain valid cross-reference targets |
| **Source Assessment**    | DIWAI-ASMT-2026-08 — full SP 800-171A objective-level self-assessment                       |
| **Change Record**        | DIWAI-EV-AU-2026-08-08 (this revision, POA&M-010 closure evidence); DIWAI-CR-2026-08-28; DIWAI-PR-LOG (2026-08-07 disposition) (the field previously read `-08-12` through revisions 1.8–1.12)                                                                        |

---

## DOCUMENT REVISION HISTORY

| Version         | Date       | Author     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------|------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1             | 2026-06-11 | [SYSTEM-OWNER] | Initial standalone document consolidating POA&M-001–008.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 1.1 (corrected) | 2026-06-11 | [SYSTEM-OWNER] | Added POA&M-008 per independence determination.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 1.2             | 2026-06-12 | [SYSTEM-OWNER] | Independent gap assessment; POA&M-002 closed via SI-3 substitution; added closed 009, 010.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **1.32 (amended 5)** | **2026-09-13** | **[SYSTEM-OWNER]** | **POA&M-075 CLOSED — YARA PROVEN ON BOTH HOSTS; POA&M-076 DIRECTORY HALF ENFORCED.** **(a)** YARA detection exercised end to end with EICAR: VM alert in 2 s, Mac on its hourly scan — the first YARA alerts ever raised; SSP 3.14.2 corrected (`DIWAI-CR-2026-09-06` §3a). **(b)** 389-DS now disables accounts after 90 days' inactivity, proven by refusal; a creation-date lockout trap for the owner's account was avoided by phasing (`DIWAI-CR-2026-09-08`). The 3.5.6 point stays withheld: Mac and VM local accounts remain, and never-logged-in entries need a creation-date fallback. No SPRS change. |
| **1.32 (amended 4)** | **2026-09-13** | **[SYSTEM-OWNER]** | **3.5.6 WITHHELD; SPRS 101 → 100/110; POA&M-076 OPENED.** The newly recorded evidence-strict basis was applied at once: the SSP defines a 90-day inactivity disable, but no host enforces it. The point is withheld until every identifier class is enforced, or formally excepted with evidence. Enforcement is constrained by the `sysadmin` break-glass account (see POA&M-073). |
| **1.32 (amended 3)** | **2026-09-13** | **[SYSTEM-OWNER]** | **SCORING BASIS RECORDED: EVIDENCE-STRICT.** Owner determination: SPRS points are earned only by controls implemented and proven working by evidence, including negative testing, per `DIWAI-VS-001`. The strict 800-171A objective count (35/110) is the documentation gap under POA&M-027 and is reported alongside, not as the score. First answer on the record to `CUI_SPRS_Recomputation_and_Punchlist_2026-08` §1. No figure changed. |
| **1.32 (amended 2)** | **2026-09-13** | **[SYSTEM-OWNER]** | **SPRS 94 → 101/110 ON THREE TESTED RECOVERIES; POA&M-051 CLOSED; POA&M-075 OPENED.** **(a) 3.14.1 +5:** the Wazuh pin's SIGILL diagnosed offline to an SVE2 virtual-CPU quirk crashing OpenSSL 3.5, fixed with `OPENSSL_armcap`; manager upgraded to 4.14.7 and verified; **POA&M-051 closed** (`DIWAI-CR-2026-09-04`). **(b) 3.3.4 +1:** a Mac audit-failure warning proven end to end to the owner's inbox; **POA&M-029** advanced (`DIWAI-CR-2026-09-07`). **(c) 3.10.3 +1:** visitor nil attestation; 3.10.4 withheld by owner decision (`DIWAI-PE-LOG-001` §6; **POA&M-027**). **(d) Found and fixed on the way:** `ossec.conf` had no `<ruleset>` block, so no custom Wazuh rule had ever loaded (`DIWAI-CR-2026-09-06`). The **YARA** detection path had therefore never alerted; that part survives the session as **POA&M-075**. **(e)** Dashboard figures restored (`DIWAI-CR-2026-09-05`). |
| **1.32 (amended)** | **2026-09-13** | **[SYSTEM-OWNER]** | **SPRS RE-DETERMINED 93 → 94/110; CREDENTIAL POLICY PROVEN BY REFUSAL ON BOTH HOSTS, AFTER TWO SILENT FAILURES WERE REPAIRED.** **(a)** Revision 1.32's basis for withholding the point — Mac policies *configured but not negatively tested* — was incomplete, and `DIWAI-VS-002` row 013 had marked 3.5.8 HOLDS from a policy dump. **(b) Negative tests on disposable accounts** (owner-approved) found the **Mac `diwai.password.history` rule malformed** — `opendirectoryd` logged *"Unable to parse the format string"* and skipped it on every change since 2026-08-07, reproducing the `DIWAI-VS-001` §6.1 FAIL — and the **389-DS minimum length not enforced** (`passwordCheckSyntax: off`; a 6-character password accepted). **(c) Repaired in session:** Mac rule → `none policyAttributePasswordHashes in policyAttributePasswordHistory`; 389-DS `passwordCheckSyntax on`, `passwordMinLength` 8 → **14** at the owner's direction. Two wrong fixes on the Mac (category move; an unsourced predicate that parsed but never matched) are recorded in the change record. **(d) Proven by refusal, both hosts:** 3.1.8, 3.5.7, 3.5.8 — each rejection checked for the right reason in `opendirectoryd` or the 389-DS response. **(e) Effect:** owner re-determination **93 → 94/110**, the arithmetic figure. Corrected in session, so a change record (`DIWAI-CR-2026-09-03`), not a POA&M item. **(f)** `svc-nas` (NAS DSM LDAP client) confirmed binding after the change — 12:08:59, `err=0`. **Not verified:** Wazuh receipt of the deliberate failures. |
| **1.32** | **2026-09-13** | **[SYSTEM-OWNER]** | **SPRS DETERMINED AT 93/110; THE 08-07 DISPUTE IS CLOSED.** **(a) Owner determination.** `DIWAI-VS-001` §4 recommended withholding credit for **3.1.8** and **3.5.8** (Mac host absent from a credential policy scored for the system), reaching 92; its §6.1 addendum moved the recommendation to **93** once the Mac gaps were closed and tested. The register meanwhile carried **94/110** as DISPUTED with the determination pending since **2026-08-07**. **The owner has determined 93/110**, on the standing rule that **a disputed figure is reported at the lower, more conservative value** — a self-assessment that resolves its own ambiguity upward is not defensible to an assessor. **(b) Supported by today's re-test.** `DIWAI-VS-002` confirmed the Mac now carries `diwai.authentication.lockout` (10 attempts / 900 s) and `diwai.password.history` (depth 6), **but recorded that neither was NEGATIVELY tested** — no deliberate lockout, no sub-minimum password attempt. Configuration demonstrated, enforcement not demonstrated; that gap is precisely what the withheld point represents. **(c) Effect:** score of record **94 → 93/110**. `DIWAI-VS-001` **Recommendation 1 CLOSED**. **(d)** The SSP is reconciled in the same pass — it had stated **87/110** (the 2026-08-03 recompute) in five live locations, roughly six points stale, with its own warning block naming the two blockers now removed: an owner determination, and the open dispute. |
| **1.31** | **2026-09-13** | **[SYSTEM-OWNER]** | **ONE NEW OPEN ITEM — POA&M-074.** SSP v2.18 §3.4 (retired components) asserts *"Prometheus + node-exporter retained, so metrics collection is unaffected; only visualization was retired"*. **C90/C91 (`DIWAI-CR-2026-08-13`) disabled both on 2026-08-04**, two days after that text was written on 08-03. Verified 2026-09-13: `systemctl is-enabled` returns **disabled** for `prometheus` and `prometheus-node-exporter`, nothing listens on 9090, and no metrics have been collected or retained since 2026-08-04. **No control impact and no SPRS change** — AU-6 / 3.3.3 and 3.14.7 were restated on Wazuh, Suricata and auditd by C64/C65 in the same engagement and all three have run continuously; 3.12.4 and 3.4.1 are already scored as deficits under POA&M-003 / POA&M-025, so this adds detail and a remediation path rather than a new deduction. Surfaced 2026-09-13 while investigating the Grafana decommission for an unrelated restore question — **no process detected it**, the same discovery mode recorded in `DIWAI-MFR-2026-08-12` §7 Action 3. **SSP cross-references repointed v1.30 → v1.31 in the same pass** to preserve the mutual SSP↔POA&M pin. |
| **1.30** | **2026-08-08** | **[SYSTEM-OWNER]** | **POA&M-010 CLOSED ON AN OBSERVED EPISODE — THIRD ATTEMPT, FIRST ONE THAT MEETS ITS OWN CRITERION; 3.3.7 +1 CONFIRMED WITH NO SCORE MOVEMENT; FILENAME REALIGNED TO THE VERSION FIELD.** **(a) Closed on evidence the item itself specified.** POA&M-010's testable criterion — *one genuine post-suspend episode in which the journal shows the ladder escalating and then the recovery line* — is met by the episode at **07:17:01–07:19:43** on 2026-08-08: `failing check #1` → `burst 4/4` → `failing check #2 (114s)` → `makestep` → `RECOVERED after 2 failing check(s) over 161s`, with **every 60-second check in the interval present in the journal**. The two previous closures (06-12 "made durable", 08-03 "with monitoring") rested on a configuration change and on a detector respectively; neither observed a recovery. **(b) The evidence window was produced by an unrelated fault and cannot easily be reproduced.** The Mac host was cycling through `Dark Wake Thermal Emergency` sleeps roughly every 20 minutes — a dark-wake power-budget artifact, **not overheating**: `pmset -g therm` has never recorded a thermal warning, thermal pressure climbed 0→4 in **5 seconds** and fell back in 42, and the kernel's own `setDetailedThermalPowerBudget` lines read **~8,700–9,800 during dark wake against 255,000 awake**, a ~26× cap that the UTM guest at 134% CPU exceeds instantly. Each host sleep suspends the guest, yielding **24 real suspend/resume events overnight**. **(c) 23 of the 24 episodes are DELIBERATELY NOT relied on**, and this is the substance of the closure rather than a caveat on it. Each contains a **17–31 minute gap with no log lines** between the corrective action and the recovery line: the guard was **suspended with the guest**, not merely quiet. Across that gap `makestep` and the recovery are separated by an interval in which nothing ran, so **correction cannot be distinguished from correct time on resume**. Citing 24 episodes would have overstated the evidence in precisely the way the two prior closures did. Aggregates are recorded (rung 1 **24/24**, rung 2 **22/24**, rungs 3–4 **never reached**, unrecovered **0**) as corroboration of the mechanism only. **(d) Two consequences stated in the item rather than left implicit:** the guard is a **post-resume corrector** and makes no continuous-coverage claim; and the `over NNNNs` durations are **wall-clock spans dominated by suspended time**, not remediation latency — the extreme case reads **3497 s for a single failing check**. **(e) 3.3.7's +1 CONFIRMED by owner determination — NO SCORE CHANGE.** Carried as "questionable but NOT withdrawn" since revision 1.16, it was **already in the score**, so confirmation moves no number; **94/110 stands**. The determination is also no longer conditional: host sleep was disabled the same day (`pmset -a sleep 0`, `disksleep 0`), which **removes the uncorrected suspend window** rather than shortening it, and with it the failure mode itself — the guard becomes a safety net rather than a routine corrector. **(f) The 94-vs-93 dispute in the Score field is UNTOUCHED and remains open.** It traces to `DIWAI-VS-001` §4 and revision 1.29 — **3.1.8 / 3.5.7 / 3.5.8 credential policy on the Mac host** — and has no relation to 3.3.7; the Score field has been annotated to say so, and a duplicated "weights VERIFIED against DoD Assessment Methodology v1.2.1" clause in that field was removed as a transcription artifact. **(g) Two residuals recorded in `DIWAI-EV-AU-2026-08-08` §6 and NOT opened as items**, on owner determination: wall-clock episode duration misleads across a suspend (signal-quality, same family as POA&M-071), and every guard message is journalled twice under two PIDs, doubling audit volume and misleading anyone counting occurrences. **(h) Filename realigned.** The `v1.7` file had absorbed revisions **1.7 through 1.29** without the filename moving; a "v1.8" would have numbered backwards against the register. This revision is issued as **v1.30 with Version 1.30**, filename and document control in agreement from here. Revision-history rows 1.7–1.29 are unchanged and remain valid cross-reference targets for `DIWAI-VS-001` and the change records that cite them. **(i) Amended same-day (2026-08-12): the `SSP Reference` field was repointed v2.17 → v2.18.** A cross-reference sweep run immediately after issuing SSP v2.18 caught that this document still named v2.17 — **the exact reciprocal of the defect v2.18 was issued to repair**, created within the hour by fixing only one direction of a mutual pin. Amended in place rather than issued as 1.31, because a currency-only correction on the same day as issue does not warrant a revision and would have re-broken v2.18's pointer in turn. **The pair SSP v2.18 ↔ POA&M v1.30 is now mutually consistent; bump neither without the other.** **No SPRS change. 94/110.** |
| **1.29** | **2026-08-07** | **[SYSTEM-OWNER]** | **MAC CREDENTIAL POLICY APPLIED AND NEGATIVE-TESTED — 3.1.8 AND 3.5.7 NOW PROVEN; 3.5.8 DEMONSTRATED UNENFORCED. RECOMMENDATION 92 → 93.** **(a) Applied** via `pwpolicy -setaccountpolicies` as a **merge** — existing `diwai.minimum.length` and Apple's FDE default preserved, verified by read-back. Minimum **14** (raised from 12 at the owner's direction, the mSCP/CIS figure; both existing passwords exceed 16, so no operational impact), lockout **10 attempts self-clearing after 15 min** (deliberately not the VM's `deny=3` — DFU-rebuild failure mode, break-glass usable only hours earlier), history depth 6. **(b) Negative-tested** with a throwaway local account, every check expecting refusal: **3.5.7 PASS at creation and at user-initiated change**; **3.1.8 PASS** — the correct password is refused after 11 failures; **3.5.8 FAIL** — reuse accepted. **(c) The first test version reported a FALSE FAIL and was corrected.** It used `sysadminctl -resetPasswordFor`, an **administrative reset**, which macOS deliberately allows to bypass history and age policy — so it exercised a path the control does not govern. v2 tests through the user path and **in both directions** (`A → B` must succeed before `B → A` is allowed to mean anything). **Third variant of one lesson today: a test must exercise the path the control governs** — an interactive run could not test a launchd job (POA&M-070), staging could not test delivery (POA&M-071), an admin reset cannot test history. **(d) 3.5.8's failure is DEMONSTRATED, not inferred**, because the control check passed first. Likely cause: history enforcement has moved to **profile** delivery (`pinHistory` in a `com.apple.mobiledevice.passwordpolicy` payload) while `minLength` and lockout are still honoured via `pwpolicy`. The RS2 baseline's own generated output includes a **`mobileconfigs/`** directory, so mSCP does not rely on `pwpolicy` for this class either. A manually installed profile can carry passcode policy (unlike PPPC, which is MDM-gated) — remedy available, needs a GUI approval. **Not done tonight.** **(e) The baseline exclusion's premise NEVER HELD.** `diwai_phase1_baseline.yaml` states *"Excludes … password policy (deferred to FreeIPA)"*. `dscl /Search -read / CSPSearchPath` returns **`/Local/Default`** — the Mac is bound to no directory, FreeIPA was never deployed, and `[USERNAME]` (501) and `sysadmin` (502) are **local** accounts no directory policy could govern. A documented exclusion, unexamined for four months, while both requirements were credited. **(f) Baseline provenance verified BY CONTENT, not by label** — the owner's apples-and-oranges caution applied. The RS2 baseline was found at `archive/reference_system_2_mac/mscp/` on the `CyberHygiene Project` volume alongside an RS1 copy at `_publication_staging/cyberinabox-phaseIV/mscp/`. Confirmed as RS2's by an **exact match of all 135 rule IDs against the deployed `org.diwai_phase1.audit.plist`** — zero difference either way. mSCP baselines carry no system marker, so content matching is the only sound test. Amended baseline (adds a `passwordpolicy` section, 135 → 139 rules) staged in `~/diwai/staging/`, **deliberately not in the CUI store** (POA&M-054). **Rule IDs could not be validated offline** — the mSCP rule library and generator are not on the volume, only this baseline's output — and `generate_guidance` fails on an unknown id; flagged in the file. **(g) SEPARATE FINDING, unrecorded elsewhere: the mSCP score cited in SSP §3.4.1 is wrong in both terms.** The plist holds **136 top-level keys but 135 rules** — `lastComplianceCheck`, a timestamp, is being counted as a passing rule. Correct is **133/135**, not 134/136; the two real failures (`os_recovery_lock_enable`, `os_firewall_default_deny_require`) are correctly identified. Cited as 3.4.1 evidence, so not cosmetic. **SSP not yet corrected.** |
| **1.28** | **2026-08-07** | **[SYSTEM-OWNER]** | **SWEEP FINDING CORRECTED: 3.5.7 IS ENFORCED — RECOMMENDATION 91 → 92; MAC CREDENTIAL POLICY BUILT.** **(a) CORRECTION, and it is the sweep's own failure mode.** `DIWAI-VS-001` §4 reported that the Mac enforced **no** password minimum. **Wrong.** `pwpolicy -getaccountpolicies` returns a **4,862-byte** policy containing `diwai.minimum.length` — `policyAttributePassword matches '.{12,}+'`, `minimumLength 12` — plus Apple's `com.apple.defaultpasswordpolicy.fde`. **A 12-character minimum IS enforced, so POA&M-016's closure is supported and 3.5.7 keeps its point.** I had grepped the output for **lockout** key names, got nothing, and concluded "no policy" — **searching for the keys I expected and reading their absence as absence of the thing**, the exact defect the sweep exists to catalogue, committed inside the sweep. **Recommendation revised 91 → 92/110.** **(b) What survives, re-checked against the full object rather than a grep:** the returned policy contains **no `policyCategoryAuthentication`** and **no `policyCategoryPasswordChange`** — the Mac has **no lockout and no reuse prohibition**. `3.1.8 −1` and `3.5.8 −1` stand. **(c) Control built (pending owner apply):** `~/diwai/staging/mac-account-policy.plist`, a **MERGE** — `pwpolicy -setaccountpolicies` replaces the entire policy set, so the existing `diwai.minimum.length` and Apple's FDE default are preserved verbatim, and the two missing categories are added: lockout **10 attempts with a 15-minute SELF-CLEARING unlock**, history **depth 6**. **Lockout deliberately NOT the VM's `deny=3`** — this host's failure mode is a DFU rebuild, its break-glass account became usable only hours earlier, and the owner mistyped passwords three times in routine work the same day; a 3-attempt permanent lock on the only working admin account is a self-inflicted denial of service. The minimum is raised **12 → 15** to match the VM's `pwquality minlen 15` — a choice, reversible in one line, since 12 already satisfied the requirement. **(d) Scope note accepted from the owner:** the single-box consolidation is a **documented VSB cost decision**, risk-accepted to 2027-03-31 (POA&M-023, D-2), and is not relitigated. That acceptance covers **separation** (3.13.5 −5, architectural, expensive); it does **not** cover credential policy on the box already owned, which costs a policy file. **(e) The mSCP *check* for these rules still cannot be added:** the mSCP repo lives on the **`Mac-CyberHygiene` USB volume, which is not mounted**, and `/usr/local/bin/run-mSCP-scan.sh` is root-only. Control and check are separate — the control lands now; the weekly scan's coverage of it waits on the USB. **(f) Behavioural testing method recorded (`DIWAI-VS-001` §4.3):** complexity can only be falsified by a **negative** test. `pwscore` on the VM rejects `abc`, `Summer2026` and an uppercase-less passphrase with specific reasons, and accepts two compliant candidates at scores 99 and 100. **The first run rejected all five, including a strong passphrase** — a check that rejects everything is as useless as one that accepts everything, and would have been recorded as proof. **macOS has no `pwscore`**, so the Mac side stays Examine-level until a throwaway account attempts a non-compliant password. |
| **1.27** | **2026-08-07** | **[SYSTEM-OWNER]** | **VERIFICATION SWEEP OF ALL 38 CLOSURES (`DIWAI-VS-001`) — SIX HOLD, THREE CREDITED POINTS DO NOT, AND 22 CLOSURES STATE NO EVIDENCE.** **(a) Why:** 2026-08-07 produced **six instances of one root cause** — verification confirming the wrong property or nothing at all (070 interactive run, 067 wrong premise, 072 wrong figure, 071 wrong directory, 073 `fdesetup list` mistaken for an auth test, plus **two of my own**: `needs-restarting` absent while my shell idiom reported an answer anyway, and an `AuthenticationAuthority` attribute that is simply filtered for unprivileged reads). Handling instances guarantees more of them; this tests the pattern. **(b) Paper triage:** of 38 closures, **1** records a positive *and* negative test, 5 quote observed output, 7 say "verified" with no mechanism, 3 rest on a document, and **22 state no evidence whatsoever.** The register therefore cannot distinguish a tested closure from an assumed one. **(c) Six closures re-tested LIVE and all hold:** POA&M-014 (`250-STARTTLS`, **no `AUTH` before TLS**); **POA&M-020/-021 → 3.5.10 (+5)** — `nsslapd-require-secure-binds: on` **and a live cleartext bind rejected with `Confidentiality required (13)`**, a genuine negative test; POA&M-053 (`wazuh:wazuh` → **HTTP 401**); **POA&M-012 → 3.3.1 (+5)** — `64 MB × 100 logs = 6.4 GB` rotation configured, 260 MB in use; POA&M-002 (`yara-fullscan.timer` enabled, ran 08-02, log present); POA&M-018 (**389 closed, 636 open**). **(d) THREE CREDITED POINTS ARE UNSUPPORTED.** POA&M-013 and -016 closed 2026-08-01 crediting `3.1.8 +1`, `3.5.7 +1`, `3.5.8 +1` — **remediation was applied to the VM only.** VM: `faillock deny=3`, `pwquality minlen 15`, 389-DS `passwordLockout on` / `passwordHistory on, inHistory 6`. **Mac host: NOTHING** — `pwpolicy -getaccountpolicies` and `-getglobalpolicy` both empty, **no lockout rule among the 136 mSCP rules**, **no passcode payload in any of the 32 installed profile payloads**, and the self-assessment's own finding A-01 records the Mac minimum as **4 characters**. **The Mac host holds the plaintext CUI document store and is the boundary router and hypervisor — it is in scope**, and SPRS has no partial credit for these three. **The same-day self-assessment had already determined all three OTHER THAN SATISFIED by Test; the points were credited anyway.** **(e) Recommendation: 94 → 91/110 — NOT applied, because it is an owner determination.** The counter-argument is on the record (FileVault, `DisableFDEAutoLogin`, owner presence, locked rack, no unauthenticated inbound path); my reading is that those are **physical and network** controls while 3.1.8/3.5.7/3.5.8 are **credential-policy** requirements — they reduce the chance to attempt a password, not the limit on attempts, the minimum, or reuse. **Score field now marked DISPUTED pending that determination.** **(f) Also found:** 389-DS **`passwordCheckSyntax: off`** with `passwordMinLength: 8` — directory passwords are length-checked but not complexity-checked, so `pwquality` (OS accounts) overstates the VM's 3.5.7 posture. **(g) Principal recommendation — a practice change, not an item: A CLOSURE MUST STATE THE EVIDENCE THAT WOULD HAVE FALSIFIED IT.** One line per closure ends the need for sweeps like this. Secondary: reopen 013/016 scoped to the **Mac host**, open an item for Mac credential policy (mSCP has rules for all three, absent from the current baseline), set `passwordCheckSyntax: on`, and re-test the **remaining 16** unverified closures — this sweep covered 6 of 22. |
| **1.26** | **2026-08-07** | **[SYSTEM-OWNER]** | **13 SECURITY UPDATES APPLIED OFF-CYCLE AND KERNEL ACTIVATED; ONE OF MY OWN POST-CHECKS WAS VACUOUS.** **(a) Applied, transaction 66:** all 13 pending security packages across 6 advisories — `sg3_utils`/`-libs`, `perl-DBI`, `perl-Archive-Tar` (**Important**), `libgcrypt`, `p11-kit`/`-trust` (Moderate), kernel ×6 (Low). **Nothing deferred.** `wazuh-manager` **pin held at 4.14.6** — upgrading it is POA&M-051 and needs a tested path, not a `--security` sweep. **`dnf check-update --security` → rc 0.** Rollback: `dnf history undo 66`. **(b) Kernel activated by attended reboot** at the UTM console (LUKS passphrase, POA&M-026) — the restart deferred since 08-02 is **discharged**. Running **5.14.0-687.36.1**, new boot id, **FIPS 1**, **14 of 14 units returned active with no manual recovery** (they had been verified `active` *and* `enabled` beforehand — the check that would have caught a unit that runs but was never enabled), `diwai-control-health` **25/25**, and published services probed from the Mac with **389 and 55000 correctly CLOSED** (POA&M-018, POA&M-053). **(c) CORRECTION — a post-check of mine verified nothing.** `needs-restarting` **is not installed on the VM**. My construction `cmd >/dev/null 2>&1 && echo NO || echo YES` reported "reboot needed" because the **command was missing**, and `needs-restarting | wc -l` reported `0` because there was **no output at all**. The patch log had recorded "no service restarts were required (checked, not assumed — the 08-03 lesson)" **while committing the 08-03 mistake in a new form.** Re-verified via `/proc/*/maps`, filtered to shared objects under library paths: **one** process mapped a deleted `.so` — `wazuh-indexer`'s JVM holding its own extracted `libzstd-jni`, a normal JVM pattern, **not** a replaced system library. The conclusion was right; the evidence had not existed. A reusable checker now lives at `~/diwai/src/check_stale_libs.sh`. **Rule recorded: verify a diagnostic command EXISTS before trusting its silence.** **(d) `diwai-clock-guard` ran but was NOT tested.** First run at boot+30s: `clock OK — selected source present`, and every 60s since; chrony selected within 30 s because `iburst` handles a clean reboot. **A reboot is not the failure mode** — suspend/resume is. **POA&M-010 stays open**; its closure criterion (a real post-suspend episode recovered by the ladder) is unmet. **(e) A reporting artifact recorded in `DIWAI-PR-LOG`:** `dnf updateinfo list --security` still names RLSA-2026:49870 against kernel `687.34.1` because it matches **exact NEVRA** and the installed `687.36.1` supersedes it. **Read `check-update`, not `updateinfo list`, when deciding whether work remains** — same class as POA&M-072. **(f) Cadence deliberately NOT tightened.** `DIWAI-PR-001` stays **weekly as a floor, not a ceiling**: off-cycle application is permitted and logged, whereas a procedure promising daily review creates an obligation that must be evidenced daily and turns every missed day into a finding. **No SPRS change. 94/110.** |
| **1.25** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-025 CLOSED; SSP REISSUED v2.17 AFTER FINDING IT CONTRADICTED ITSELF; NO POINTS RECOVERED — AND THAT CORRECTS MY OWN FORECAST.** **(a) POA&M-025 is complete.** Its three parts: a defined patch-review cadence — `DIWAI-PR-001`, weekly, with **two reviews actually logged** (08-02, 08-03) in `DIWAI-PR-LOG`, so defined **and operating**; the SCAP deviation **recorded as an accepted, justified variance** — `dnf-automatic_apply_updates` tailored out with the justification **in the tailoring file itself** (`/etc/diwai/scap/diwai-cui-tailoring.xml`), VM now reporting **101/101** rather than carrying a standing failure that trains the operator to ignore results; and the pending-update backlog — the **deferred kernel is discharged**, verified by `uname -r` = `5.14.0-687.33.1`, the newest installed, with `needs-restarting -r` reporting **no reboot pending**. **(b) A self-contradiction found in the SSP, and it had stood for two versions.** Four control-table rows — **3.7.1, 3.11.3, 3.14.1, 3.14.3** — stated that `dnf-automatic` "applies security patches" / "handles OS security advisories". **The live config is `apply_updates = no`: it downloads and applies nothing.** The plan's own **Appendix E.3 has documented that deviation since v2.15**, so the plan described, as its implementation, the very mechanism the deviation deliberately disabled. All four rows now describe the real mechanism — staged downloads plus **operator-applied updates at the weekly review** — and **3.14.1 is restated as PARTIALLY IMPLEMENTED** with its evidence and its residual named. **SSP reissued as `CUI_System_Security_Plan_v2.17.md`.** The DoD methodology makes SSP accuracy a **scoring prerequisite**, so this is not presentation. **(c) NO SPRS CHANGE, and this corrects a forecast of mine.** I described POA&M-025 as "the largest single recovery available, +5, documentation-shaped". **Wrong on both counts.** The documentation half was nearly finished already, and **`3.14.1 −5` is charged against POA&M-051 as well** — `wazuh-manager` version-pinned at 4.14.6, receiving no security updates, which is an uncorrected flaw in a security control. Closing 025 therefore **reattributes** the deduction rather than clearing it. The SSP's deduction row has been updated from `025` to `051` accordingly. **The remaining −5 is an ENGINEERING task — a tested Wazuh upgrade path — not a writing task.** Score remains **94/110**. **(d) Current backlog, for the 08-10 review:** 13 security updates pending on the VM, matching the 13 PATCH-class findings in `cve-scan-2026-08-07.json`; 4 are IMPORTANT and inside their 7-day window under `DIWAI-PR-001 §6`. |
| **1.24** | **2026-08-07** | **[SYSTEM-OWNER]** | **PHYSICAL ACCESS LOGGING INSTANTIATED; THREE DOCUMENTS RECONCILED; A CLAIM OF MINE CORRECTED.** **(a) CORRECTION to revision 1.18.** I recorded that `3.10.3 −1` and `3.10.4 −1` **had no owning POA&M item** and might be recoverable on evidence already held. **Both halves were wrong.** SSP v2.16's deduction table assigns both to **POA&M-027** — invisible in this register's item rows, which is a **presentation** gap, not an ownership one — and they are **not stale**. **(b) Three documents disagreed and the artifact settled it.** The self-assessment (08-01) said **no visitor log exists**; the PE evidence record (08-02) said **SATISFIED, "those who do are logged"**; SSP v2.16 said **"procedure defined, not yet operating."** Reading the file: `Nextcloud → Business_Admin → Visitor Log.xlsx` is a well-formed template — `Date | Visitor Name | Time in | Time Out | Company Name | US Person Y/N | Purpose of Visit | Escort` — containing **two rows, a title and a header, and NO entries.** So the **SSP is accurate**; the self-assessment was wrong that no log exists because **it searched only the Compliance store** (evidence an assessor cannot find is equivalent to absent — POA&M-048's family); and the **PE record over-claims**, its SATISFIED obtained by **Interview** while its own §5 lists "Visitor log — form and location" as an item **to confirm** that was never closed. **Third instance today of an Interview-based determination standing over an unclosed confirmation** — the break-glass account was the second. **(c) C116 — `DIWAI-PE-LOG-001` created.** Records the visitor log's canonical location so it is discoverable; **instantiates the rack physical access log**, described in SSP v2.15 and never actually created; adds a **nil-activity attestation** because an empty log and an absent log are indistinguishable unless the empty one asserts the emptiness. **Boundary stated: the RACK, not the room** — consistent with `DIWAI-EV-PE-2026-08-02 §2`, and because logging family movement through a home office in a shared residence would be the wrong control even if it scored. Routine rack openings are logged, not only unusual ones, since a log of exceptions has no baseline. **(d) NO POINTS CLAIMED, deliberately.** A defined procedure scored zero on 08-01 and scores zero now; **what moves the score is the log being kept** — one monthly attestation line, even if every figure is `0`. Claiming otherwise would be the POA&M-005 defect: a document asserting its own closure closes nothing. **Remaining external dependencies:** camera retention (open since 08-02, F-2026-08-27) and alarm-history retention with the monitoring provider (never asked) — and note the alarm is **disarmed while the premises are occupied**, so its history cannot cover working hours, making the rack log the real carrier of 3.10.4. **Score remains 94/110.** |
| **1.23** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-073 CLOSED — BREAK-GLASS REPAIRED AND TESTED; A DIAGNOSIS OF MY OWN WITHDRAWN.** **(a) Repaired (C115):** `sysadmin` password reset via `sysadminctl -resetPasswordFor`, authorised by a SecureToken-holding admin. SecureToken was already ENABLED and remains so. **(b) Verified BY TEST, which is the entire point of the item:** `dscl . -authonly sysadmin` **succeeds silently** where it returned `eDSAuthAccountDisabled`; `failedLoginCount` **18 → 0**; admin group intact. The 08-04 entry had recorded this precondition satisfied on the strength of `fdesetup list`, which shows **FileVault enablement, not the ability to authenticate**. `DIWAI-CR-2026-08-26`. **(c) CORRECTION — the cause stated in revision 1.22 and `DIWAI-CR-2026-08-25 §5` is WITHDRAWN.** That record asserted `AuthenticationAuthority` was absent and therefore no password mechanism existed. **That attribute is filtered by OpenDirectory for non-privileged reads of another user's record:** run as `[USERNAME]`, `dscl . -read` shows `AuthenticationAuthority` and `AltSecurityIdentities` for **[USERNAME]'s own record** and neither for **sysadmin's**. The comparison was a privileged read against a filtered read and proved nothing. **The finding was real — the account genuinely could not authenticate — but the mechanism asserted for it was not, and the true cause is now left UNDETERMINED rather than guessed.** Recorded because this is the same defect the assessment keeps finding in others' work: evidence that cannot support the conclusion drawn from it. **(d) MFA on the break-glass account: CONSIDERED AND DECLINED**, with owner agreement. It has no `authorized_keys` entry and `publickey` is mandatory, so the TOTP stack can never apply; its real path is the console, where MFA means editing the `loginwindow`/`authorization` PAM stack that produced **two DFU rebuilds** on this host; and a phone-dependent second factor undermines the purpose of break-glass when the emergency is that the machine will not boot. Control is instead a strong unique password, **escrowed in the sealed rack envelope** (POA&M-026/-049), console-only, not routinely used. **(e) Incidental finding for the recovery runbook:** the repair **could not be done over SSH** — `sysadminctl` failed with `-60007 errAuthorizationInteractionNotAllowed` because SecureToken operations need an authorization prompt an SSH session cannot display, and the attempt was made from a loopback SSH session **visually identical to a local one**. If this Mac were ever in the state where `sysadmin` were needed, it could not have been repaired remotely first — an argument for **scheduled** break-glass testing rather than on-demand discovery. **(f) Residual, explicitly not closed:** `fdesetup list` was **not** re-run (needs root), so **pre-boot unlock by `sysadmin` is assumed, not demonstrated** — which is exactly the assumption that created this item; escrow of the new password is unconfirmed; nothing yet schedules a re-test, and this account failed silently for ~10 weeks. **No SPRS change. Score 94/110.** |
| **1.22** | **2026-08-07** | **[SYSTEM-OWNER]** | **MFA ON THE MAC IS NOW EXERCISED — 3.5.3 RECOVERED TO −3, 92 → 94/110; BREAK-GLASS ACCOUNT FOUND DEAD.** **(a) Proof, not configuration:** `sshd-session: Accepted keyboard-interactive/pam for [USERNAME] from 127.0.0.1` at **16:41:27**, and the module's own state file shows **`DISALLOW_REUSE 59538082`** written with the **scratch-code count unchanged at 4** — so a **live time-based code** was validated, not a scratch code. Three factors on one login: key (required first by `AuthenticationMethods`), account password (`pam_opendirectory`, independently confirmed by `dscl . -authonly [USERNAME]`), TOTP. **The risk carried since 08-06 — that an adhoc-signed Homebrew PAM module might not load in Apple's `sshd` — is retired.** `DIWAI-CR-2026-08-25`. **(b) C113–C114:** interactive ECDSA P-256 key enrolled, restricted `from="[LAN-IP-REDACTED]/24,127.0.0.1,::1"` (ECDSA forced by `crypto.conf`, which accepts `ecdsa-sha2-nistp256` only — an ed25519 key would have been silently unusable); and the **existing** secret enrolled into the owner's authenticator app via a `qrencode` QR labelled **"SecureMac Mac SSH"**, distinct from the VM and Nextcloud entries, keeping the four scratch codes valid. **No PAM or sshd config was changed** — the 08-06 stack was correct; it lacked a subject. Test was on **loopback**, so proving the control opened no network path. **(c) 3.5.3 −5 → −3. Open deductions −16, score 94/110.** Defensible now where it was not on 08-06: the objection was that MFA covered **zero users**; a user now exists and the login is in the log. Console access remains **the same factor twice** (`DisableFDEAutoLogin`), which is the −3 floor. **(d) Two instructive failures first.** A **`Broken pipe`** that was **not** an auth failure but `LoginGraceTime` (120 s) expiring during a three-minute pause — proven by the authenticator file being **untouched**, so the code never reached PAM. Then a **`Permission denied`** where a mistyped password let the module **consume a scratch code** that rounds 2 and 3 then re-sent into `DISALLOW_REUSE`. **Diagnosis was by state inspection** — whether the authenticator file had changed is what separates "never reached the module" from "module ran and rejected", two failures identical from the client. **(e) POA&M-073 OPENED — the `sysadmin` break-glass account CANNOT AUTHENTICATE.** `dscl . -authonly sysadmin` → **`eDSAuthAccountDisabled`**; cause is that `AuthenticationAuthority` is **absent** — no registered password mechanism — with `failedLoginCount = 18`, so this is not new. **This contradicts POA&M-007 precondition #1, recorded as "SATISFIED — verified 2026-08-04" on owner confirmation, citing `fdesetup list`.** That command shows **FileVault enablement, not the ability to authenticate**; the wrong property was verified. On a host whose failure mode is a **DFU rebuild** (`DIWAI-INC-002`, twice in 2026), **the only recovery path was dead while this host's authentication stack was modified on 08-06 and again on 08-07.** Deliberately **not** repaired in the same record: fixing an admin account's authority is itself an authentication change here and must end with `dscl . -authonly sysadmin` **tested**, not asserted. **(f) POA&M-060 partially answered on this host:** scratch codes **work** — one was validated and consumed — where the item records them untested; `DISALLOW_REUSE` and `RATE_LIMIT` are functional here, unlike on the VM. **(g) Question raised on a scored requirement:** `pwpolicy -getaccountpolicies` returns **nothing**, yet POA&M-013 was closed and **3.1.8 credited +1** for account lockout. Counting happens (`[USERNAME]` 0, `sysadmin` 18); enforcement is unverified. Flagged for the requirements walk, not chased. |
| **1.21** | **2026-08-07** | **[SYSTEM-OWNER]** | **ARCHIVE JOB NOW SCHEDULED ONCE (POA&M-063 advanced).** **(a) It ran twice daily**, registered in **both** `/etc/cron.d/wazuh-log-archive` and an enabled `wazuh-archive.timer`, both at 02:00 — proven from the log: `02:00:01` and `02:00:02` on 08-07, `03:41:14` and `03:41:20` on 08-06. **Both runs derive the same staging filenames from the date and each ends in `rm -f`**, so one could truncate the tar another was encrypting or delete the `.enc` another was transferring. The overlap window is **minutes** wide, not seconds — 08-07 delivery landed at 02:16, sixteen minutes after both runs began. The 08-06 pair also explains the catch-up anomaly in `DIWAI-CR-2026-08-16`: the timer carried `Persistent=true`. **(b) No damage had occurred — verified, not assumed.** `wazuh-alerts-2026-08-05.tar.gz.enc`, **a genuine double-run product**, decrypts against the real key and `tar -tzf` returns rc 0 with all four expected members. An initial test used the 08-06 archive and was **discarded as evidence** because a manual single run had overwritten it, so it could say nothing about concurrency. **(c) Fixed (C111–C112):** cron entry **moved out** of `/etc/cron.d` (not renamed or commented in place — that is the remnant pattern POA&M-063 exists to remove, and the same decision taken for the LaunchDaemon plist), and the timer kept with **`Persistent=false`**. `DIWAI-CR-2026-08-24`. **(d) This REVERSES the earlier recommendation to keep cron**, on evidence: cron has no `MAILTO`, so it mails the job output daily into the mailbox de-duplicated hours earlier — **4 such messages are already in the Maildir** — while the timer's 02:00 run produced **21 journal lines** that Wazuh ingests. Cron's only advantage, no surprise catch-up, is a setting rather than a property, and is now set. **(e) Verified:** zero references under `/etc/cron*`, timer `enabled`/`active`, `Persistent=no`, `OnCalendar` unchanged, next elapse Sat 02:00. **The actual claim — one run instead of two — is observable only at 02:00 on 08-08** and should be read then. **(f) Residual:** the script still has **no lockfile**, so a manual run during the scheduled window would recreate the race; `/etc/pf.anchors/diwai.security` remains an orphan under POA&M-063. **No SPRS change.** Score **92/110**. |
| **1.20** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-010: CORRECTION DEPLOYED, ITEM DELIBERATELY LEFT OPEN.** **(a) Mechanism established from chronyd's own log**, not inferred: a UTM suspend leaves the guest clock behind, which **inflates every source's jitter and root distance**, so chrony refuses to select a source — and `makestep` cannot act until it does. `13:42:51 Jitter … exceeds maxjitter` → `13:44:19 Selected source` → `13:44:19 System clock wrong by 162.275061 seconds` → `13:47:02 stepped`. **Six minutes unaided**, with longer episodes the same morning. Suspends confirmed as the trigger by `uptime` (1 d 13:27) against `chronyd` `ActiveEnterTimestamp` (08-03 10:02) — ~2.5 days of accumulated suspended time. **(b) Fixed by pairing detection with action (C109–C110):** `diwai-clock-guard`, every 60 s, escalating `burst 4/4` → `makestep` → wait → **`restart chronyd`** → `daemon.err` + retry, and **announcing recovery with episode duration**, because silence from a watchdog is indistinguishable from a dead watchdog. It assesses the clock by **selected source (`^*`)**, never `chronyc tracking`, which once read 0.000000000s off while the clock was 24 minutes wrong. No mail is sent from the guard — control-health owns the human channel, and two alert paths for one condition is how the flood started. `DIWAI-CR-2026-08-23`. **(c) FOUR remedies rejected with reasons, and `/etc/chrony.conf` was not modified at all.** `makestep` has been configured since 06-12 and cannot act before selection — **correcting my own recommendation in revision 1.16**. `refclock PHC /dev/ptp_kvm` was **tested and is unavailable** — `/dev/ptp*` does not exist under UTM on Apple silicon — where the previous revision said it must be tested, not assumed. **`hwclock -s` was rejected as UNSAFE**, not merely useless: `rtcsync` writes the *system* clock into the RTC about every 11 minutes, so a stale RTC can hold a wrong value, and after chrony steps but before the RTC is rewritten `hwclock -s` would **move the clock backwards** — unacceptable where authentication is time-derived. Loosening `maxjitter`/`maxdistance` trades correctness for latency in the wrong direction. **(d) Verified:** ladder rungs 1–6 fire in order; `--dry-run` executes nothing and writes no state; timer fired at 14:59:59 and again at 15:01:06; and an **A/B test proves `SuccessExitStatus=0 1` stops every episode also registering as a failed unit** (without it: `failed`/`Result=exit-code`; with it: `inactive`). **(e) A test that was not a test, recorded:** the ladder was exercised with `--simulate-bad` **without** `--dry-run` under a heading claiming dry-run, so the corrective actions were **real against a healthy clock**, including `systemctl restart chronyd`. Outcome verified rather than assumed — source re-selected within seconds, **0.5 µs** offset, VM and Mac at the identical epoch — but the demonstration was luck, not method, and on a host configured to step any offset at any time an unintended `makestep` must be deliberate. **(f) ITEM STAYS OPEN.** Closed 06-12 as "made durable", reopened 08-01; closed 08-03 "with monitoring", reopened 08-07 — **both closures rested on a configuration change or a detector, never on observed recovery from a real event.** Closing on a simulated ladder would be that error a third time, and this morning's POA&M-070 lesson was exactly that a verification which cannot distinguish the fix from the bug is not one. **Closure criterion, testable: one genuine post-suspend episode in which the journal shows the ladder escalating and then the recovery line.** **(g) The control-health check was deliberately NOT desensitised**, reversing revision 1.16's recommendation: with the guard resolving episodes in 1–4 minutes against a 15-minute check interval, and POA&M-067 de-duplication in place, one alert plus one recovery notice per surviving episode is **information, not noise** — suppressing it would hide real events. **No SPRS change; 3.3.7's +1 remains questionable and not withdrawn.** Score **92/110**. |
| **1.19** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-071 CLOSED — THE FRESHNESS CHECK NOW MEASURES THE DESTINATION.** **(a) The defect was structural, not a typo.** `nas-archive-push` searched the **staging** directory for a recent archive — and staging is empty precisely when the pipeline works, because a successful push moves the file out. So the NOTE fired on every healthy run and also when the VM job had stalled: identical output in both states. It could not have measured anything else, because mount discovery happened **after** the "nothing to push" branch had already exited, leaving the check with no idea where the destination was. **(b) Fixed (C108)** by moving mount discovery earlier and measuring the age of the newest `.enc` **on the NAS** against `STALE_HOURS=48`, distinguishing **four** states where there was one: delivery current; delivery stopped (with where to look); destination reachable but empty; **mount absent — freshness could not be determined, stated outright rather than implied healthy.** The healthy case now makes a **positive statement**, because a check that is silent when satisfied cannot be distinguished from one that has stopped running — the POA&M-019 defect class. `DIWAI-CR-2026-08-22`. **(c) Demonstrated, not argued.** The log holds the before and after **95 seconds apart on identical system state**: `14:48:13 NOTE: no archive has arrived in the last 48h` (old check) against `14:49:51 Delivery current: newest archive on the NAS is 1h old` (new check) — the old check declaring delivery stalled **105 minutes after a verified successful delivery**. **(d) Verified through launchd**, not an interactive shell: kickstart of the real agent via `nas-push-runner`, exercising the POA&M-070 TCC grant, `last exit code = 0`. All four branches were exercised on rewritten copies beforehand, including a synthetic 120h-old archive. Installed file byte-identical to the staged version, **root:wheel 755**, satisfying the runner's ownership guard. **No SPRS change** — no requirement was scored on this check. Score remains **92/110**. |
| **1.18** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-072 CLOSED — THE CVE SUMMARY NOW REPORTS WHAT §6 ACTS ON.** **(a) Fix (C107):** `counts_actionable` added beside `counts` — PATCH-class severity totals against all-kinds severity totals — with an explicit `_scope` string on each **inside the report JSON**, and a log line stating the actionable subtotal or, when there is none, naming the kinds `DIWAI-PR-001 §6` does not clock. **`counts` was deliberately NOT redefined:** narrowing it would have silently changed the meaning of a field in every historical comparison. The `_scope` strings live in the report rather than only in a change record, because the defect was that a reader trusting the summary was misled — a fix documented elsewhere leaves the next reader where the last one was. `DIWAI-CR-2026-08-21`. **(b) Verified live:** `counts {CRITICAL:1, IMPORTANT:31, MODERATE:10}` against **`counts_actionable {IMPORTANT:4, MODERATE:9}` — no CRITICAL.** The finding that started a 72-hour clock on 08-02 now appears in the raw totals and is absent from the actionable figure. **(c) Scope corrected twice during the work, both narrowing it.** `dashboard-refresh` does **NOT** read the CVE report — the earlier suspicion that the phantom CRITICAL also reached the Admin Portal rested on a **same-named local variable** holding SCAP pass/fail tallies; it references no CVE data at all. And the **Mac scanner never had the defect** — `diwai-cve-scan-mac` writes a different schema reporting `brew_actionable`, already actionable-scoped. The Mac-held source copy of the VM scanner was resynchronised, SHA-256 identical on both hosts. **(d) A live finding surfaced:** the verification run fetched fresher advisory data than 08-03 and shows **13 PATCH-class findings, 4 of them IMPORTANT and inside their 7-day window** under §6, where 08-03 showed a kernel-only set. Ordinary review work for **2026-08-10**, recorded in `DIWAI-PR-LOG` so Monday starts from current figures. The off-cycle report is recorded there as a **verification run, not a review** — nothing applied, no disposition — so it is not later mistaken for a missed or duplicated weekly review. **No SPRS change** — 3.14.1 remains a deficit under POA&M-025; this improves reporting, not patch cadence. Score remains **92/110**. |
| **1.17** | **2026-08-07** | **[SYSTEM-OWNER]** | **AUG-2 CRITICAL VULNERABILITY DISPOSED; A PRIOR NOTE CORRECTED; ONE ITEM OPENED.** **(a) The finding:** `RLSA-2026:19372 / CVE-2026-42945`, `nginx-filesystem-1.20.1-28.el9_8.4.rocky.0.1`, advisory-fixed at `1.26.3`. **Disposition: NOT APPLICABLE — no exploitable code path.** No `nginx` binary on `PATH`, no `nginx.service` unit (only a `.service.d` drop-in directory), `rpm -ql` lists directories plus a `sysusers.d` file and **nothing executable**. The scanner already classified it `kind: NO-CODE`. **Accepted with a re-evaluation trigger:** if `nginx` is ever installed on this VM the CVE becomes live and §6's 72-hour clock applies. **(b) A DISPOSITION RECORD ALREADY EXISTED and was missed on the first pass** — the Patch Review Log's 2026-08-02 notes carried it. **This revision corrects an error in it:** the note called the package an "orphaned dependency", implying it could simply be removed. **It is required by `roundcubemail-1.5.15-1.el9`** (`dnf repoquery --whatrequires`), pulled in 2026-04-08 by `dnf install -y roundcubemail`, and `/etc/nginx/` holds live Roundcube/PHP-FPM drop-ins — **removing it removes webmail, which is where these alerts are read.** The note also named neither the advisory nor the CVE, so it could not be found from the alert that cited it. Both fixed; `DIWAI-PR-LOG` updated with a full disposition table. **(c) No patch was missed and no 72-hour window was breached.** `DIWAI-PR-001 §6` scopes the clock to **PATCH-class** CRITICAL findings, and this is `NO-CODE`, so §6 never covered it. The 08-02 alert was accurate to the *check as it then stood* — that version counted CRITICAL by **severity alone**; the `kind == "PATCH"` filter was added 08-04, verified from script backups (`.bak-20260802` and `.bak-cve` have no CVE check; `.bak-20260804b` has the filter). Current check: **`no actionable CRITICAL/IMPORTANT vulnerabilities`**. **(d) POA&M-072 opened** — the scan report's top-level `counts` is **kind-blind**. `cve-scan-2026-08-03.json` states `counts: {CRITICAL: 1, IMPORTANT: 27}` while its own `kinds` field shows `{NO-CODE: 5, STREAM-MIGRATION: 8, THIRD-PARTY: 15}` — **zero PATCH-class findings.** A reader trusting the summary sees an unpatched CRITICAL that does not exist. **No SPRS change** — 3.14.1 sits under POA&M-025 and was already scored as a deficit. Score remains **92/110**. |
| **1.16** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-067 CLOSED — AND ITS PREMISE WAS WRONG; POA&M-010 REOPENED.** **(a) Delivery was never broken.** POA&M-067 said the alert "went to `root`'s local mailbox, which nobody reads." In fact `/etc/aliases` maps **`root: [USERNAME]`**, there is **no `/var/spool/mail/root`**, Dovecot delivers to `maildir:~/Maildir`, and **93 of the 94 unread messages in the owner's real mailbox are control-health alerts**, spanning 08-02 → 08-07 and readable in Roundcube throughout. **The conclusion (nobody saw them) was right; the mechanism was not** — and applying the remedy as written would have moved working mail to a new address and left the defect in place. **(b) The actual defect is signal-to-noise.** `diwai-control-health.timer` fires **every 15 minutes** and the script mailed on **every failing run** with no de-duplication: one unresolved failure yields **up to 96 identical messages a day**. **81 of the 93 alerts are a single failure** (`chrony has NO selected source`). Buried underneath: the archive-staging alert this item was written about (**×8**), `dashboard authenticated requests return 500 — LDAP bind failing`, a stale-data CVE scan, and **`1 actionable CRITICAL vulnerability — patch within 72h`**. **A channel delivering 96 messages a day is not a monitored channel, whatever its address.** **(c) Fixed by state-change alerting (C106)** — failure set persisted to `/var/lib/diwai/control-health.state`; mail on a **new** failure, on **clearance**, or **once per 24 h** unchanged, plus a **recovery notice** so silence can be distinguished from broken alerting. **`syslog` left deliberately un-deduplicated** so Wazuh retains the complete per-run record: throttling the human channel must not thin the audit trail. Routing left untouched. `DIWAI-CR-2026-08-20`. **(d) Verified the way the item demanded — by observing arrival, not a return code.** Three runs against an isolated copy with a synthetic failure, mailing to the real mailbox: sent (count 0 → 1), **suppressed on the identical set (stayed 1)**, recovery notice delivered and state truncated. All three assertions passed; test messages and scratch files removed; live script then ran **25/25**. **(e) POA&M-010 REOPENED — the clock is free-running again**, 13 alerts on 08-07 alone, most recent 12:30, `RMS offset 202.17 s`; recovered by 14:08 (`^*`, 20 µs). Closed 08-03 "with monitoring" and 3.3.7 recovered **+1** on the basis that this very check watches for a selected source. **The control worked for six days and nothing acted on it** — known UTM suspend behaviour needing `chronyc makestep`; detection exists, correction is manual and absent. **(f) 3.3.7's +1 is now questionable but NOT withdrawn** — the clock is synchronised at time of writing and excursions are detected, so this is a determination for the requirements walk (the convention used for 3.5.10 under POA&M-066). **Score unchanged at 92/110.** **(g) Probable cause of a lost half-hour today, recorded:** a TOTP code rejected at ~10:30 fell inside a no-selected-source window; TOTP is time-derived, so **clock drift is a likelier cause than an expired code**, and the `PerSourcePenalties` block that followed (POA&M-061) was downstream of that rejection. **(h) Backlog disposition executed the same day on owner instruction:** **76 chrony-only messages deleted, 5 deliberately KEPT** because they also carried the archive-staging failure and were its only mail copy — "81 chrony alerts" and "81 deletable messages" were not the same set. Tarred with a SHA-256 and a per-message manifest first, since `journalctl` retains these events only from 08-03 19:15 while the alerts begin 08-02, making the mailbox the sole record for the earliest. **Mailbox 94 → 18; every distinct finding retains at least one copy.** `DIWAI-CR-2026-08-20` v1.1 §7.1. |
| **1.15** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-070 CLOSED — THE ARCHIVE PUSH NOW WORKS UNATTENDED; ONE ITEM OPENED.** **(a) Root cause proven, not inferred: TCC, not the launchd domain.** A throwaway LaunchAgent bootstrapped into `gui/501` was denied `touch` on the NAS directory (`Operation not permitted`) **at the same instant an interactive shell was allowed the same write, same user, same mount, same second.** The only variable was descent from Terminal, which holds the TCC grant its children inherit. `Operation not permitted` is `EPERM` from privacy enforcement; POSIX failures give `EACCES` — the distinction was in the error text from the first failure onward. **The 08-06 domain fix was a correct diagnosis of a non-binding cause**, and its interactive verification **could not distinguish the fix from the bug**. **(b) Fixed by a scoped grant, not a broad one.** TCC grants attach to an executable, and the agent invoked `/bin/bash` — so the direct route was **Full Disk Access for the system shell**, which would have extended full disk access to every future launchd bash job on a host holding the plaintext CUI store. Instead a **60-line purpose-built helper** was written: `/Library/PrivilegedHelperTools/nas-push-runner`, **root:wheel 755, ad-hoc signed**, no arguments, **one hard-coded exec target**, which it refuses to run unless root-owned and not group/world writable. A PPPC configuration profile was not available — **no MDM enrolment** on this host, and manual PPPC payloads have been ignored since Big Sur — so a one-time GUI approval was the only mechanism. `DIWAI-CR-2026-08-19`. **(c) Desktop placement was proposed and declined by agreement.** Raised by the owner as an accessibility improvement when the file picker proved hard to navigate; declined once the trade-off was stated — the Desktop is writable by `[USERNAME]`, so anything running as that account could replace a TCC-granted binary and inherit full disk access **without `sudo` and without an audit record**, which is POA&M-069's defect and would have made a narrowed grant worse than the broad one. `/Library/PrivilegedHelperTools` satisfies all three requirements at once: root-owned, not user-writable, **and visible in Finder** — the accessibility problem solved without weakening the grant. **(d) Verified from the context that failed.** `launchctl kickstart` of the real agent: **`Pushed 1 file(s); 0 failure(s)`**, SHA-256 verified, **`last exit code = 0`** where it read `1`; staging empty, NAS holding its 6 archives, probe removed. `TCC.db` confirms the grant exists for that binary alone (`kTCCServiceSystemPolicyAllFiles`, `auth_value 2`). **The 03:00 run on 08-08 is confirmation, not the proof.** **(e) POA&M-071 opened.** The push script's staleness check searches the **staging** directory — which is empty exactly when the pipeline is working, because a successful push moves the file out. **It fires identically on success and on failure, so it carries no information**, and it fired during this change's own smoke test minutes after a good delivery. A daily false alarm trains the reader to skip the line that would matter. Remedy: test the destination. **(f) A scoring dependency recorded, not adjusted.** 3.3.1 was recovered **+5** on 08-01 for audit retention, and this off-host delivery leg is part of how that requirement is met — it was **claimed while broken, twice, and nothing noticed.** No data was lost (keep-local-on-failure held both times) and the requirement is met today, so the fix belongs to the monitoring gap, not the score. **Score unchanged at 92/110.** **(g) POA&M-067 is now the top follow-on** — three failures in four days would all have been reported into an unread root mailbox. |
| **1.14** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-065 CLOSED — 3.7.5 RECOVERED, 87 → 92/110; ONE ITEM OPENED, AND IT IS A REPAIR THAT DID NOT HOLD.** **(a) POA&M-065 closed.** The last unrestricted service key, `[EMAIL-REDACTED]`, is now `from="[LAN-IP-REDACTED]",command="/usr/bin/scp -t /Users/[USERNAME]/nas-staging/",restrict`. **The destination is pinned server side** — a client asking to write `/tmp` had its file written into `nas-staging` instead, so the restriction does not depend on the VM's script being correct or the VM being uncompromised. Arbitrary command execution returns **0 bytes** (`cat /etc/passwd` → nothing, no shell), pty allocation is refused (rc 255), and the **full production archive job ran end to end** (rc 0; 31,456-byte `.enc` delivered, `Salted__` header intact, VM staging emptied). `restrict` was chosen over the enumerated `no-*` list used on the cert-sync key because it also picks up restrictions added in future OpenSSH releases. `DIWAI-CR-2026-08-18`. **(b) The fix required a matched change on the OTHER host, and either half alone breaks the pipeline.** Since OpenSSH 9.0 `scp` speaks the **SFTP subsystem** by default; a forced command intercepts that request and the transfer **hangs** rather than failing (verified: **rc 124 without `-O`, rc 0 with it**). So `/usr/local/sbin/wazuh-log-archive` on the VM was given `scp -O`, had its `ssh … "mkdir -p"` call **removed** (arbitrary remote commands no longer run; the staging directory is permanent), and gained `StrictHostKeyChecking=yes` — safe immediately, because root's `known_hosts` already pinned `SHA256:Kx6vC1g9Aifk…` — plus `BatchMode=yes`, which the `scp` call had always lacked while the removed `ssh` call had it. **(c) 3.7.5 RECOVERED, −5 → 0. Score 87 → 92/110.** Claimed here where `DIWAI-CR-2026-08-17` claimed nothing, and the difference is evidence: the exempted path was **tested and shown incapable of carrying a maintenance session**, not merely configured to be. Session termination is separately enforced by `01-mscp-sshd.conf`. **3.5.3 unchanged at −5** — still needs an interactive key and one recorded MFA login (**+2**). **(d) Residual recorded:** the key can still deposit files into `~/nas-staging`, which `nas-archive-push` copies to the NAS, so a compromised VM could **inject** into the archive store — but can no longer read from this host or execute on it. **Trust is now one-way toward the internet-facing host, which is the correct asymmetry.** **(e) POA&M-070 OPENED — the 2026-08-06 archive-push repair did not hold.** The job **failed again at 03:00 on 08-07** with the identical `cp: … Operation not permitted`; `launchctl print` shows `last exit code = 1`. **The cause is TCC, not the launchd domain** — `EPERM` from macOS privacy enforcement, not `EACCES` from POSIX permissions — demonstrated by the same path being **writable from an interactive shell at the same moment** the agent was refused. The domain change was necessary and **not sufficient**. **Yesterday's verification could not have detected this: it was an interactive run, the one context that carries the TCC grant.** Third instance of the "job appears healthy while doing nothing" category (POA&M-063). Pending archive pushed by hand and verified (staging empty, NAS 5 → 6); **the agent will fail again at 03:00 tomorrow.** **(f) POA&M-067 reinforced** — this is now the **second consecutive failure** the unread-mailbox gap would have hidden. |
| **1.13** | **2026-08-07** | **[SYSTEM-OWNER]** | **POA&M-007 CLOSED — SSH MFA ENFORCED ON THE MAC HOST; NO SPRS CHANGE CLAIMED; ONE ITEM OPENED.** **(a) POA&M-007 closed.** Interactive SSH to the Mac now requires `publickey` + `keyboard-interactive:pam`, where the PAM stack runs `pam_opendirectory` then `pam_google_authenticator`. Module ordering is load-bearing — `pam_opendirectory` uses `try_first_pass`, so a TOTP module placed first would have its code consumed as the account password. `nullok` deliberately absent, so unenrolled accounts fail closed. Applied without an `sshd` restart: launchd starts `sshd` per connection, so live sessions could not be disturbed. Preconditions all verified first, including a **same-day Time Machine backup** as the recovery floor. `DIWAI-CR-2026-08-17`. **(b) The VM is exempted by address** (`Match Address [LAN-IP-REDACTED]` → `publickey`) because two automated jobs cannot supply a code — `wazuh-log-archive` at 02:00 and the certbot deploy hook. **Exemption verified working from the VM after the change (rc 0, no prompts)**, twice, including after (d). **(c) NO SPRS MOVEMENT — recorded explicitly, because revision 1.7 stated both −5 deductions were gated on this item.** They are not recovered by it. **3.7.5 remains −5**: the exemption still admits one unrestricted key granting a full interactive shell from [LAN-IP-REDACTED] with a single factor, which is a nonlocal maintenance path — **recovery is gated on POA&M-065**. **3.5.3 remains −5 with a ceiling of −3**, since console access is still single-factor; and −3 is **not yet defensible because no interactive key exists for the owner**, so `publickey` — the mandatory first factor — cannot be satisfied by any human, the PAM stack **has never authenticated a user**, and MFA therefore covers zero users. **The control is enforced and unexercised.** Claiming points here would be the POA&M-062 defect (configuration asserting a control) committed in a change record. Score stays **87/110**; **+5 and +2 are near-term and identified**. **(d) POA&M-065 advanced, not closed.** `[EMAIL-REDACTED]` removed from `~/.ssh/authorized_keys`. Its private half was **not on this system or the VM**, and the owner identifies it as **inherited from the CyberHygiene Project build during documentation duplication** — `dc1` is the domain controller for **[DOMAIN.ORG], a separate boundary**, mislabelled with the `[DOMAIN.ORG]` domain, which is how it read as native. Zero use in 7 days of unified-log history (3 `Accepted publickey` events, all the live key). Exposure was **latent, not live** — `pf` admits `sshd` only from `[LAN-IP-REDACTED]/24`. **One unrestricted key remains.** **(e) POA&M-069 opened** — `/etc/pam.d/sshd` loads a module from `/opt/homebrew/lib/security`, and that path chain is owned `[USERNAME]:admin` with `/opt/homebrew/lib` **group-writable**, so root's authentication stack can be altered **without `sudo` and without a sudo audit record**. Same defect class as the user-writable `pf` config relocated in `DIWAI-CR-2026-08-03`. **(f) A wrong-host `ssh_config` alias corrected** — `securemac.[DOMAIN.ORG]`, this host, was aliased to `[LAN-IP-REDACTED]`, the VM. `known_hosts` held the **VM's** host key under this host's name, which is written only on a completed connection, so the alias had already been used. **(g) Two POA&M-063 remnants recorded:** `/etc/pf.anchors/diwai.security` is not referenced by the loaded ruleset, and **the archive job is scheduled twice** — `/etc/cron.d/wazuh-log-archive` and an `enabled`/`active` `wazuh-archive.timer`, both at 02:00. **(h) POA&M-061 confirmed live** during this work on the VM: a rejected TOTP code earned a per-source penalty and the next attempt was dropped before the banner. |
| **1.12** | **2026-08-06** | **[SYSTEM-OWNER]** | **POA&M-068 OPENED — archive key not escrowed.** Prompted by an owner question about end-to-end FIPS protection of the Wazuh archives. **Verified sound:** archives are encrypted once on the VM with `openssl enc -aes-256-cbc -pbkdf2 -iter 100000` under the **Red Hat Enterprise Linux OpenSSL FIPS Provider** (`fips_enabled: 1`), and are **never decrypted in transit** — confirmed by the `Salted__` header on the stored NAS copy and by zero decrypt references in `nas-archive-push`, which only copies and SHA-256 verifies. The FIPS boundary correctly ends at the `.enc` file, making the non-FIPS transport hops irrelevant to confidentiality. **The gap is key custody, not cryptography.** `/etc/wazuh-archive.key` exists only inside the VM; recovery depends on a chain — archives → key in the VM image → LUKS passphrase in the rack envelope — **entirely inside one building**. The risk was already written in three documents and tracked in none. **Also noted:** SMB transport shows signing supported but no session/share encryption, so **filenames** travel in clear (payload is ciphertext). **No SPRS change.** |
| **1.11** | **2026-08-06** | **[SYSTEM-OWNER]** | **ARCHIVE PUSH REPAIRED; ONE ITEM OPENED.** **(a)** The encrypted Wazuh archive push failed silently **2026-08-04 → 08-06**; four archives sat in staging. Cause was the launchd **domain**, not permissions: the job was a LaunchDaemon (system bootstrap domain) writing to a **session-scoped SMB mount**, giving `Operation not permitted` on every write. `UserName=[USERNAME]` drops privilege but does not place a daemon in the login session. Moved to a LaunchAgent (C94); backlog pushed and SHA-256 verified; duplicate logging corrected (C95). **No data lost** — the script keeps local copies on failure. `DIWAI-CR-2026-08-16`. **(b) This is the June 2026 `backup-status-push` root-domain defect recurring in a different job** — added as a category to POA&M-063. **(c) POA&M-067 opened.** `diwai-control-health` **detected the failure correctly** — the POA&M-055 fix earning its keep three days after being written — but mailed the alert to an **unread root mailbox**. Detection without delivery. **No SPRS change.** |
| **1.10** | **2026-08-04** | **[SYSTEM-OWNER]** | **NAS ATTACK SURFACE REDUCED; ONE ITEM OPENED; ONE LOCKOUT AVOIDED.** **(a) C93 — NAS SSH disabled** after verifying no consumer exists (`mount-nas.sh` uses SMB, `stage-nas-cert.sh` is local-only, grep exit 1 across all automation). **Second nonlocal maintenance path removed by deletion today**, after Prometheus. SMB, DSM and the DataStore mount verified intact. `DIWAI-CR-2026-08-15`. **(b) A DSM firewall change was prepared and ABORTED before Apply.** Synology's firewall is **deny-by-default**; the prepared state was a newly-enabled firewall whose only rule was `deny TCP 5000`, which would have cut SMB, DSM and the backup pipeline simultaneously, recoverable only by physical access. Caught by inspecting the tab before Apply. **The assessor's initial instruction omitted the default-action check** — recorded in §3 of the change record. **(c) POA&M-066 opened** — the DSM API processes authentication over cleartext HTTP on port 5000; responses are identical to HTTPS. **This puts the 3.5.10 recovery of 2026-08-03 at risk.** POA&M-033 was closed on the browser path and never exercised the API path — the same defect as `DIWAI-CR-2026-08-10`. **No SPRS change recorded pending the requirements walk**, where 3.5.10 must be re-determined. |
| **1.9** | **2026-08-04** | **[SYSTEM-OWNER]** | **INTERNET-FACING SSH CLOSED — the largest exposure found in this assessment.** **(a)** `pf` passed **SSH from any internet source** to [WAN-IP-REDACTED]. Behind it: password authentication offered, **no MFA**, **no interactive key for the owner**, on the host holding the **plaintext CUI document store** and acting as router and hypervisor. Closed by C92, validated with `pfctl -nf` before load, **no outage**. `DIWAI-CR-2026-08-14`. **(b) It persisted because a hardening comment was never acted on** — `# Post-build: add "from <admin-ips>"`. **The same file documents the identical defect twenty lines earlier** in the `en1` rule, which was found, assessed HIGH (R-09), remediated as POA&M-024 and scored **+5**. Finding one instance of a defect class is not sweeping for it. **(c) POA&M-064 opened** — the published-services evidence record was built from `pfctl -s nat` (redirections only) and was **structurally incapable** of seeing a filter pass terminating on the boundary host. **(d) POA&M-065 opened** — two `wazuh-archive` keys with no `from=` or forced `command=`. **No SPRS change** — 3.13.1/3.13.5 and 3.5.3 were already scored as deficits; this materially reduces exposure without altering the deduction list. |
| **1.8** | **2026-08-04** | **[SYSTEM-OWNER]** | **ORPHANED MONITORING STACK REMOVED; ONE ITEM OPENED.** **(a)** An **unauthenticated Prometheus API** (`/api/v1/query`, `/api/v1/targets`) was reachable from the Mac on `[LAN-IP-REDACTED]:9090`, returning data with no credentials. Removed via C89–C91: firewalld `cockpit` service removed (it was the rule opening 9090), Prometheus and node-exporter disabled. Verified unreachable; 25/25 health checks; no outage. `DIWAI-CR-2026-08-13`. **(b) The exposure was created by no single decision** — Cockpit's firewall permission opened 9090 for a service never enabled, while Grafana's removal left Prometheus running on that same port with nothing consuming it. **(c) POA&M-063 opened** for a systematic remnant sweep. **No SPRS change** — 3.4.6/3.4.7 sit under POA&M-003/-025 and were already scored as deficits; this removes an unauthenticated service and one nonlocal path, and adds no new deduction. |
| **1.7** | **2026-08-04** | **[SYSTEM-OWNER]** | **MFA ENFORCED ON THE SERVICE VM; TWO ITEMS CLOSED; THREE OPENED; DASHBOARD CORRECTED.** **(a) POA&M-004 closed** — TOTP now required for every SSH login to the VM (`AuthenticationMethods publickey,keyboard-interactive:pam`), verified by owner-confirmed interactive login **and** by a negative test proving key-alone is refused. Applied with an automatic `systemd-run` rollback armed **before** the first change and re-armed at each step; `sshd -t` run before every reload. **No outage.** `DIWAI-CR-2026-08-12`. **(b) NO SPRS MOVEMENT — recorded explicitly because the opposite was expected.** 3.5.3 and 3.7.5 each remain **−5**: the Mac host has no second factor for console access and **listens on :22 for nonlocal maintenance**. The VM was one half of each requirement; **both deductions are gated entirely on POA&M-007**, not split across the two hosts. Score stays **87/110**. **(c) POA&M-055 closed** — completed 2026-08-04 and verified again this date (25/25 checks, authenticated probe present), but the register had never been updated when 033, 035 and 053 were. **(d) Three items opened. POA&M-060:** `pam_google_authenticator` cannot write its token file — `EACCES` with **no audit record**, on a path both `root` and the owning user can write; SELinux excluded by policy inspection and by a live attempt with `dontaudit` disabled. `DISALLOW_REUSE` and `RATE_LIMIT` were **removed** to make MFA function, costing replay protection and module rate limiting, and **scratch codes are probably non-functional** — untested, and if dead the authenticator device is a single point of failure. **This is a working control with a documented weakness, not a finished one.** **POA&M-061:** OpenSSH `PerSourcePenalties` blocked [LAN-IP-REDACTED] — the sole administrative source — during testing. **POA&M-062:** `48-mfa.conf` and `49-fido2.conf` cited 3.5.3 and POA&M-047 in their headers while configuring **nothing**; a directory listing implied MFA existed. The same claim appeared in `~/.ssh/config` on the Mac. **(e) Summary dashboard corrected.** It read `30 total / 12 closed / 18 open` — a state predating items numbering to 059 — and asserted **87/110** directly above a reconciliation table ending in **56**. Counts are now derived by parsing the register table (**52 / 31 / 21**) and the score is stated as `110 − 23` so it is verifiable by addition. **(f) Known divergence, NOT corrected here:** several detail sections still carry `— OPEN` headers for items the table records as closed (022, 024, 028, 033, 053). **The table is authoritative**; the detail sections lag. Reconciliation belongs to POA&M-027. |
| **1.6** | **2026-08-03** | **[SYSTEM-OWNER]** | **SCORE RECOMPUTED 56 → 87/110; SIX ITEMS CLOSED; REGISTER SCRUBBED.** **(a) +31 recovered across nine requirements** — 3.2.1 +5, 3.2.2 +5, 3.2.3 +1 (POA&M-008, all artefacts signed); 3.11.1 +3 (POA&M-005, risk assessment accepted and signed); 3.6.3 +1 (POA&M-006, tabletop conducted and signed); 3.1.16 +5 (wireless off, pf-enforced); 3.11.2 +5 (CVE scanning operational); 3.5.10 +5 (`nsslapd-require-secure-binds: on`, `DIWAI-CR-2026-08-10`); 3.3.7 +1 (clock synced, recurrence now monitored). **Eight of the nine were already earned** — only 3.5.10 required new engineering. Deductions **−54 → −23**. **(b) Scrub against live state and the historical volume.** Five items were resolved but unclosed: POA&M-022 and -024 (which directly contradicted requirements already scored as recovered), -028, -037, -010. POA&M-003 reduced to **2 failing mSCP rules, not 5**. **Nothing new was found on the historical volume** for POA&M-026, -030, -032 — only policy templates already in the canonical set. **No item was closed on a document search alone**; every closure rests on live verification. **(c) POA&M-055 to -057 opened** — control-health verifies services are *running* not *working*; reporting tooling hosted on the reported-about asset; no DoD medium assurance certificate. Open items **24 → 21**, closed **18 → 26**. |
| **1.5**             | **2026-08-03** | **[SYSTEM-OWNER]** | **RISK ASSESSMENT ACCEPTED — POA&M-005 CLOSED; TRAINING EVIDENCE FILED; FOUR NEW ITEMS.** **(a) POA&M-005 closed** — `DIWAI-RAR-001` v1.1 accepted (3.11.1). The assessment had existed since 08-02 stating on its face that it closed this item, while the register still read **OVERDUE** and its six decisions had no route to action — the same defect class as F-2026-08-06. **A document asserting its own closure closes nothing.** **(b) All six risk decisions resolved and dated:** D-1 **treat** via break-glass LUKS escrow (TPM2/clevis rejected — would decrypt without human presence; unattended boot stays unsolved), recorded against POA&M-026; D-2 **accept R-02 in writing to 2027-03-31**, conditional on compensating controls holding and **no further internet-facing service being published**, recorded against POA&M-023. **(c) POA&M-049 to POA&M-052 opened** for D-3 (succession/credential escrow), D-4 (off-site backup), D-5 (Wazuh version lock), D-6 (restoration test) — all four had existed **only inside §7 of the risk assessment**, untracked and undated. **(d) POA&M-008 evidence filed** — IF141.16 certificate verified; `DIWAI-PAF-001` **signed**; `DIWAI-TRR-001`, `DIWAI-RAM-001`, `DIWAI-CRC-001` drafted; three signatures outstanding, **+11 recoverable on signature (56 → 67/110)**. **(e) F-2026-08-33** raised — `DIWAI-ATP-001` §3.3 cites `/srv/hr/training-records/`, which exists on neither host. **(f) FIM coverage of the CUI document store deployed and VERIFIED** (F-2026-08-34) — 2,503 files now catalogued with SHA-256 where nothing previously watched that directory. `realtime` is **silently ignored on macOS** (agent logs `WARNING 6908`; API reports `realtime: no`), making the explicit `<frequency>3600</frequency>` load-bearing — the default would have left a **12-hour** detection window while the config read "realtime". **FIM does not detect reads** and must not be cited as mitigating unauthorised disclosure. **(g) POA&M-053 and POA&M-054 opened** — Wazuh API on shipped default credentials (`wazuh:wazuh`, bound `0.0.0.0:55000`, **not** reachable off-host: firewalld does not open 55000), and the mSCP toolchain still inside the CUI boundary (2,300 files / 32 MB in group-folder trash, 43 days after the purge was recorded complete). Open items **21 → 26**, closed **17 → 18**. **No SPRS change in this revision** — POA&M-005 carried no weight, and the training recovery is not claimable until signed. |
| **1.4**             | **2026-08-03** | **[SYSTEM-OWNER]** | **ONE NEW OPEN ITEM — POA&M-048** (finding F-2026-08-32, `DIWAI-CR-2026-08-09` §5.5): compliance working copies in `~/diwai/assessment-2026-08/` drift silently from the canonical Nextcloud store. A stale local SSP — byte-identical to an 08-02 09:45 snapshot, **125 lines behind canonical** — was edited and prepared for reissue; publishing it would have reverted the carrier-separation, triple-homed-boundary, wireless-resolution and OpenSCAP 101/101 content added later that day. Caught by an ad-hoc size comparison, **not by any control**. Scored against **3.4.1 / 3.4.3 / 3.12.4**. **No SPRS change** — 3.4.1 and 3.4.3 were already scored as deficits under POA&M-003 and POA&M-025 respectively, so this item adds detail and a remediation path, not a new point deduction. **Open-item count corrected.** SSP v2.15/v2.16 stated "**18 open items**"; the actual table count was **20** before this addition and is **21** after (17 closed). The 18 was already understated before this revision — recorded here rather than silently adjusted. Companion SSP reissued **v2.16** the same day (Grafana/ClamAV reconciliation); its POA&M references updated to v1.4 and its open-item count to 21.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **1.3 (corrected)** | **2026-08-02** | **[SYSTEM-OWNER]** | **SPRS WEIGHTS VERIFIED.** All point values confirmed against the *NIST SP 800-171 DoD Assessment Methodology, Version 1.2.1 (24 June 2020)*, Annex A and §(d). **POA&M-008 resolved from "TBD" to −11** (3.2.1 = −5, 3.2.2 = −5, 3.2.3 = −1) — outstanding since 2026-06-11. **Two long-standing errors corrected:** (a) **3.7.5 was weighted −3; the methodology lists it as a Derived requirement worth −5**, understating the deficit by 2 points since v1.1; (b) the 11 points for POA&M-008 were **never subtracted**, though the SSP acknowledged they were pending. **The June baseline was therefore 85/110, not 98/110.** Provisional figures corrected: **current score 56/110** (was estimated ~61). Three of the assessor's provisional weights were wrong and are corrected: 3.5.10 −1→**−5**, 3.12.3 −1→**−5**, 3.3.4 −3→**−1**. Note 3.5.3 and 3.13.11 carry partial-credit rules; 3.13.11 scores **0** because FIPS-validated encryption is in use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **1.3**             | **2026-08-01** | **[SYSTEM-OWNER]** | **POST-DEMO REBASELINE — full objective-level assessment.** First complete SP 800-171A assessment of all 110 requirements (249 determinations): 107 satisfied, 80 partially satisfied, 50 other than satisfied, 6 unverified, 5 N/A. **Nineteen remediation changes applied and verified** (C1–C19). **Nine new items opened as CLOSED** (011–019) recording defects found and fixed the same day. **Eleven new open items** (020–030). **POA&M-010 REOPENED** — VM time-sync drift recurred despite being closed 2026-06-12 as "made durable". **POA&M-003 corrected** — describes 8 failing mSCP rules; the actual count is 5, and the figure had been unverifiable since April because the weekly scan was non-functional. SPRS recomputed provisionally 98 → ~61; the movement is almost entirely newly *found*, not newly broken.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

---

## PURPOSE

This Plan of Action and Milestones documents all open, closed, and planned
security findings for the [DOMAIN.ORG] SecureMac Reference System (RS2). It is a
living document, reviewed quarterly with the SSP. Findings are tracked from
identification through remediation or formal risk acceptance.

**Evidentiary caution on "gaps" (added 2026-08-03, at the system owner's
direction).** This project's history includes frequent course changes and
inconsistent naming of systems and artefacts; a git reorganisation corrected part
of the sprawl and some remains. A historical reference copy is retained on the
**"CyberHygiene Project" volume — 14,444 files, 2.2 GB**, with its own
`00_Consolidation_Inventory.md` and `00_Document_Assessment_Ledger.md`.

**Consequence for this register: an item recorded here as missing may in fact be
filed elsewhere.** Absence from the canonical Nextcloud store and from the two
git repositories is *not* proof that a record does not exist — both repos begin
only 2026-05-30 and 2026-06-05, so nothing earlier was ever going to be in them.
POA&M-052 is the worked example: it asserted "restoration never tested" until
`DIWAI-INC-002` was produced from the historical volume, documenting a
bare-metal recovery on 2026-04-14.

**Standard applied going forward:** before an item is opened on the basis that a
record is absent, the historical volume and its two ledgers are to be searched,
and the item must state where it looked. Where that has not been done, the item
should read *"not located in the canonical store"* rather than *"does not
exist."*

**Governing observation from the 2026-08 assessment.** Four controls were found
believed-running but inert — the Wazuh manager (down ~21 h), the Wazuh Mac agent
(previously, ~12 days), the weekly mSCP scan (executing a zero-byte script since
~June), and clock synchronisation (24 minutes adrift while reporting itself
synchronised). **Two of the four had previously been closed as fixed.** The
common cause is that nothing verified that controls were still running. This is
addressed by POA&M-019; it is also the reason several items below are recorded
as *reopened* rather than trusted as closed.

---

## POA&M ITEMS

| POA&M ID  | Control              | Weakness                                                                                                                                                                                                                                                                                                                                                                                  | Status                                                                                  | Opened     | Closed/Target     |
|-----------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|------------|-------------------|
| POA&M-001 | 3.5.3, IA-5          | YubiKey PIV re-pairing (Mac host)                                                                                                                                                                                                                                                                                                                                                         | **Closed — Superseded**                                                                     | 2026-04-15 | Closed 2026-06-06 |
| POA&M-002 | 3.14.2               | ClamAV / YARA on VM                                                                                                                                                                                                                                                                                                                                                                       | **Closed — Resolved**                                                                       | 2026-06-05 | Closed 2026-06-12 |
| POA&M-003 | 3.4.1                | mSCP failing rules (Mac) — **corrected: 5, not 8**                                                                                                                                                                                                                                                                                                                                            | Open — **reduced: 2 failing rules, not 5** (mSCP 134/136)                                                                          | 2026-06-05 | Q4 2026           |
| POA&M-004 | 3.5.3, 3.7.5         | TOTP MFA deployment — VM                                                                                                                                                                                                                                                                                                                                                                  | **Closed — Resolved 2026-08-04** (TOTP enforced for all VM SSH; positive and negative test; `DIWAI-CR-2026-08-12`). **No SPRS movement — see POA&M-007**                                                                          | 2026-06-05 | Q4 2026           |
| POA&M-005 | 3.11.1               | First annual risk assessment                                                                                                                                                                                                                                                                                                                                                              | **Closed — Resolved 2026-08-03** (`DIWAI-RAR-001` v1.1 accepted; signature pending)           | 2026-06-05 | Closed 2026-08-03 |
| POA&M-006 | 3.6.3                | IR tabletop exercise                                                                                                                                                                                                                                                                                                                                                                      | **Closed — Resolved 2026-08-03** (`DIWAI-IR-TTX-001` conducted + signed; 10 gaps)                                                                                | 2026-06-05 | was 2026-06-30    |
| POA&M-007 | 3.5.3, 3.7.5         | TOTP enrollment — Mac host                                                                                                                                                                                                                                                                                                                                                                | **Closed — Resolved 2026-08-06** (`publickey` + `keyboard-interactive:pam` enforced; VM exempt by address for two automated jobs, exemption verified rc 0; `DIWAI-CR-2026-08-17`). **NO SPRS movement — the control is enforced but UNEXERCISED:** no interactive key exists for the owner, so the PAM stack has never authenticated a user. **3.7.5 recovery gated on POA&M-065; 3.5.3 capped at −3 by single-factor console access and not defensible until one MFA login is recorded** | 2026-06-06 | Closed 2026-08-06 |
| POA&M-008 | 3.2.1/3.2.2/3.2.3    | Security awareness training — delivery + records                                                                                                                                                                                                                                                                                                                                          | **Closed — Resolved 2026-08-03** (all artefacts signed; **+11 recovered**) | 2026-06-11 | Q4 2026           |
| POA&M-009 | 3.3.1/3.3.2          | Mac Wazuh agent offline                                                                                                                                                                                                                                                                                                                                                                   | **Closed — Resolved**                                                                       | 2026-06-12 | Closed 2026-06-12 |
| POA&M-010 | 3.3.7                | VM time-sync drift — **detection without correction**. Closed 2026-08-03 "with monitoring", and 3.3.7 recovered **+1** on the basis that `diwai-control-health` checks for a *selected source*. **The check has been reporting `chrony has NO selected source` since 2026-08-02 — 81 alerts, 13 on 08-07 alone, most recent 12:30 — and nothing acted on any of them.** `RMS offset 202.17 s` records the excursion; chrony had recovered by 14:08 (`^*`, 20 µs). Triggered by UTM suspends — `uptime` (1 d 13:27) versus `chronyd` `ActiveEnterTimestamp` (2026-08-03 10:02) shows ~2.5 days of accumulated suspended time, since monotonic uptime freezes while wall-clock does not. **The control worked; the correction step does not exist.** Also the likely cause of a TOTP rejection at ~10:30 on 08-07 (TOTP is time-derived — see POA&M-061). **3.3.7's +1 is questionable and NOT withdrawn** pending the requirements walk. **`makestep` is NOT the remedy** — `/etc/chrony.conf` has carried `makestep 1.0 -1` since 2026-06-12 (F-09), and makestep cannot act until a source is *selected*, which is the very state being reported; sources are `pool pool.ntp.org iburst`, so post-resume re-resolution and polling leave a window where chrony knows it is lost and can do nothing. **Remedy, two parts:** (1) shorten time-to-selection or take time from the host (`refclock PHC /dev/ptp_kvm` if this UTM configuration exposes it — **must be tested, not assumed**; named sources with shorter `minpoll` also help); (2) make the check require the condition to persist across two runs (≥30 min), since a transient settle window is not a control failure | **Closed — Resolved 2026-08-08.** Closure rests on **one observed episode**, not on a configuration change and not on a detector — the failure mode of both previous closures. On 2026-08-08 the guest was suspended and resumed **24 times** by host dark-wake sleeps; the episode at **07:17:01–07:19:43** was the one observed by a continuously-running guard from onset to recovery, and it shows the ladder escalating and then the recovery line as the criterion requires: `failing check #1` → `burst 4/4` → `failing check #2 (114s)` → `makestep` → `clock RECOVERED after 2 failing check(s) over 161s`. Across all 24 episodes the ladder fired at rung 1 **24/24** and rung 2 **22/24**; **rungs 3 and 4 were never reached** and no episode went unrecovered. **Scope of the claim, stated explicitly:** the guard is a **post-resume corrector** — it is suspended with the guest and does **not** run during a suspend, so no continuous-coverage claim is made; and the `over NNNNs` durations in the journal are **wall-clock spans dominated by suspended time**, not remediation latency (one reads 3497 s for a single failing check). The 23 gapped episodes corroborate the mechanism but cannot distinguish correction by `makestep` from correct time on resume, and are **not** relied on. Evidence: `DIWAI-EV-AU-2026-08-08` (raw journal SHA-256 `6e1a76c9e8027946ea3653d782804b1294773889501e73f1ab3e3114ca20310a`). **Two residuals recorded in the evidence document, neither blocking and neither opened as an item on owner determination:** episode duration is reported as wall-clock and misleads across a suspend, and every guard message is journalled twice under two PIDs. **3.3.7's +1 CONFIRMED by owner determination 2026-08-08** — it had been carried as "questionable but NOT withdrawn" since revision 1.16, so it was already in the score and **this confirmation moves no number**; the upstream cause was additionally removed the same day by disabling host sleep (`pmset -a sleep 0`), which eliminates the uncorrected suspend window rather than shortening it | 2026-06-12 | Closed 2026-08-08 |
| **POA&M-011** | 3.4.3, 3.14.1        | Unattended `dnf` upgrade disabled the SIEM for ~21 h                                                                                                                                                                                                                                                                                                                                        | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-012** | 3.3.1, 3.3.6         | VM audit retention ≈ 1 hour                                                                                                                                                                                                                                                                                                                                                               | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-013** | 3.1.8, 3.5.8         | No account lockout; no password history                                                                                                                                                                                                                                                                                                                                                   | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-014** | 3.5.10, 3.13.8       | Internet-published SMTP accepted cleartext SASL auth                                                                                                                                                                                                                                                                                                                                      | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-015** | 3.4.1, 3.11.2        | Weekly mSCP scan non-functional (two independent defects)                                                                                                                                                                                                                                                                                                                                 | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-016** | 3.5.7                | Mac password minimum was **4 characters**                                                                                                                                                                                                                                                                                                                                                     | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-017** | 3.4.1, 3.12.4        | Policy set identifiers did not match SSP citations                                                                                                                                                                                                                                                                                                                                        | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-018** | 3.13.1, 3.13.6       | LDAP ports open zone-wide; rich rules gave false restriction                                                                                                                                                                                                                                                                                                                              | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-019** | 3.12.3, 3.3.4        | No control verified that controls were running                                                                                                                                                                                                                                                                                                                                            | **Closed — Resolved**                                                                       | 2026-08-01 | Closed 2026-08-01 |
| **POA&M-020** | 3.5.10, 3.1.5        | NAS binds directory as `cn=Directory Manager` in **cleartext**                                                                                                                                                                                                                                                                                                                                  | **Closed — Resolved 2026-08-02**                                                            | 2026-08-01 | Closed 2026-08-02 |
| **POA&M-021** | 3.13.10, 3.5.10      | Directory Manager credential exposed; rotation required                                                                                                                                                                                                                                                                                                                                   | **Closed — Resolved 2026-08-02**                                                            | 2026-08-01 | Closed 2026-08-02 |
| **POA&M-022** | 3.11.2               | **No CVE-level vulnerability scanning** exists                                                                                                                                                                                                                                                                                                                                                | **Closed — Resolved 2026-08-02** (CVE scanning operational; verified 08-03)                                                                                    | 2026-08-01 | Q4 2026           |
| **POA&M-023** | 3.13.5               | No separation of internet-published services from the CUI data tier                                                                                                                                                                                                                                                                                                                       | Open — architectural                                                                    | 2026-08-01 | 2027 Q1           |
| **POA&M-024** | 3.1.16               | Wireless active on the CUI host, unauthorised/undocumented                                                                                                                                                                                                                                                                                                                                | **Closed — Resolved 2026-08-02** (wireless off + pf-enforced; verified 08-03)                                                                                    | 2026-08-01 | Q3 2026           |
| **POA&M-025** | 3.4.3, 3.14.1        | No patch-review cadence; SCAP deviation undocumented                                                                                                                                                                                                                                                                                                                                      | **Closed — Resolved 2026-08-07** (cadence defined **and operating**: `DIWAI-PR-001` weekly, two reviews logged 08-02/-03 in `DIWAI-PR-LOG`; SCAP deviation **documented and tailored with justification** in `/etc/diwai/scap/diwai-cui-tailoring.xml`, VM reporting **101/101**; the deferred kernel is **discharged** — `5.14.0-687.33.1` running, no reboot pending. `DIWAI-CR-2026-08-28`). **NO POINTS RECOVERED: the `3.14.1 −5` is reattributed to POA&M-051**, not cleared — `wazuh-manager` pinned at 4.14.6 receives no security updates | 2026-08-01 | Q3 2026           |
| **POA&M-026** | 3.13.10, CP          | LUKS single keyslot, no escrow; VM cannot boot unattended                                                                                                                                                                                                                                                                                                                                 | Open — **partially remediated 2026-08-04** (passphrase sealed off-system; still co-located with the rack)                                                                    | 2026-08-01 | Q4 2026           |
| **POA&M-027** | 3.12.4 + many        | SSP accuracy and definition gaps (see detail)                                                                                                                                                                                                                                                                                                                                             | Open — **3.10.3 recovered 2026-09-13** (visitor nil attestation, `DIWAI-PE-LOG-001` §6); 3.10.4 remains −1 by owner decision | 2026-08-01 | Q4 2026           |
| **POA&M-028** | 3.14.1               | macOS Tahoe 26.6 pending (Recommended, requires restart)                                                                                                                                                                                                                                                                                                                                  | **Closed — Resolved 2026-08-03** (`sw_vers` = 26.6; upgrade applied)                                                                                    | 2026-08-01 | Q3 2026           |
| **POA&M-029** | 3.3.4, 3.13.6        | Two mSCP rules pair with assessment findings: `audit_settings_failure_notify`, `os_firewall_default_deny_require`                                                                                                                                                                                                                                                                             | Open — **3.3.4 half discharged 2026-09-13** (alert proven to the owner's inbox, `DIWAI-CR-2026-09-07`); `os_firewall_default_deny_require` (3.13.6) remains; subset of 003 | 2026-08-01 | Q4 2026           |
| **POA&M-034** | 3.5.10               | **Directory Manager password was stored in cleartext on disk** (`nsslapd-rootpw: {CLEAR}` in `dse.ldif`) despite `nsslapd-rootpwstoragescheme: PBKDF2-SHA512` being configured — written unhashed at install and never re-hashed                                                                                                                                                                    | **Closed — Resolved 2026-08-02**                                                            | 2026-08-02 | Closed 2026-08-02 |
| **POA&M-035** | 3.12.2               | **Broken citation — v1.2 refers to a "v1.1" that was never issued in this series.** Reduced 2026-08-03 from "detail exists in no current document" after searching the historical volume: two April-2026 v1.1 documents exist (different numbering series); no June v1.1 was ever created. **Remedy is a citation correction, not document recovery**                                             | **Closed — Resolved 2026-08-04** (missing detail written; v1.1 confirmed never issued)                                                                 | 2026-08-02 | Q3 2026           |
| **POA&M-036** | 3.12.4, 3.4.1        | Stale absolute paths cited across the document set                                                                                                                                                                                                                                                                                                                                        | **Closed — Resolved 2026-08-02**                                                            | 2026-08-02 | Closed 2026-08-02 |
| **POA&M-037** | 3.8.9, 3.12.4, CP    | **Backup Procedures document describes another system.** Specifies seven `backup-*.sh` scripts, none of which exist, against Graylog / Elasticsearch / FreeIPA — none of which run here. Inherited from CyberInABox and never adapted. The actual backup regime (Time Machine to encrypted USB; FIPS-encrypted Wazuh archive to NAS) is documented nowhere, yet SSP §5 points at this procedure | **Closed — Resolved 2026-08-02** (v1.0 WITHDRAWN; v2.0 issued)                                                                      | 2026-08-02 | Q3 2026           |
| **POA&M-031** | 3.3.1, 3.8.9         | **Encrypted archive pipeline non-functional** — four independent defects across VM and Mac; ran daily exiting 0 for months, delivering nothing                                                                                                                                                                                                                                                | **Closed — Resolved 2026-08-02**                                                            | 2026-08-02 | Closed 2026-08-02 |
| **POA&M-032** | 3.13.1               | NAS is **shared infrastructure** dual-homed to CyberInABox ([LAN-IP-REDACTED]) and [DOMAIN.ORG] ([LAN-IP-REDACTED]). No IP forwarding — verified. SSP §2.6 "no shared services" needs correcting; changes to it affect both systems' compliance and are recorded in only one change record                                                                                                                     | Open                                                                                    | 2026-08-02 | Q4 2026           |
| **POA&M-033** | 3.13.11, 3.1.20      | DSM transport security — **certificate half RESOLVED 2026-08-03** (current Let's Encrypt `*.[DOMAIN.ORG]` deployed and verified). **Still open:** plain HTTP on :5000 answers 200 with **no redirect to HTTPS**, and no HSTS header on :5001; QuickConnect status still to confirm                                                                                                                         | **Closed — Resolved 2026-08-04** (cert, HTTP→HTTPS redirect and HSTS all verified)                                                               | 2026-08-02 | Q3 2026           |
| **POA&M-030** | 3.8.3, 3.7.3         | Media sanitisation / off-site maintenance procedures untested, no log                                                                                                                                                                                                                                                                                                                     | Open                                                                                    | 2026-08-01 | Q4 2026           |
| **POA&M-056** | 3.6.1, 3.6.2 | **Incident-reporting tooling hosted on the VM** — the asset contained during an incident. Reporting capability is lost exactly when needed | Open | 2026-08-03 | Q4 2026 |
| **POA&M-059** | 3.12.3, 3.12.1 | **Recurring policy obligations have no execution record** — the policy set states **173** recurring activities (28 daily / 17 weekly / 30 monthly / 53 quarterly / 45 annual) against **5** automated timers. No evidence exists that the manual ones are performed | Open | 2026-08-04 | Q4 2026 |
| **POA&M-060** | 3.5.3, 3.5.2         | **TOTP token-file write failure — unresolved.** `pam_google_authenticator` cannot create its temp file (`EACCES`, **no audit record of any kind**; root and the owning user can both write the path; cause unidentified). `DISALLOW_REUSE` and `RATE_LIMIT` were removed to make MFA function: **no replay protection** (≈30 s window) and **no module-level rate limiting**. **Scratch codes are unverified and probably non-functional**, since consuming one requires the same write — if so, the authenticator device is a single point of failure for SSH | Open — raised 2026-08-04 | 2026-08-04 | Q3 2026 |
| **POA&M-061** | 3.1.1, CP            | **Source-IP penalty can remove the sole administrative path.** OpenSSH 10 `PerSourcePenalties` blocked [LAN-IP-REDACTED] during MFA testing after a prompt was left until `LoginGraceTime` expired. The Mac is the only administrative source for the VM, and adding a second factor makes fumbled logins **more** likely. Console access is unaffected and remains the fallback | Open — raised 2026-08-04 | 2026-08-04 | Q3 2026 |
| **POA&M-062** | 3.4.1, 3.4.6         | **Dead configuration asserting a control.** `49-fido2.conf` configures nothing and names hardware unpaired in May 2026; `48-mfa.conf` was identical until 2026-08-04. Both cited 3.5.3 and POA&M-047 in their headers, so a directory listing implied MFA was deployed when none was | Open — raised 2026-08-04 | 2026-08-04 | Q3 2026 |
| **POA&M-063** | 3.4.6, 3.4.7         | **Abandoned-strategy remnants across the estate.** Components left running from directions explored and abandoned during the three-year build, indistinguishable from live configuration to a cold reader. Confirmed and removed 2026-08-04: **Prometheus + node-exporter** (orphaned by Grafana's removal, **unauthenticated and network-reachable** via a firewalld rule for Cockpit — a service never enabled), **C2 Identity Edge Server** on the NAS. **Not yet examined:** Synology Virtual Machine Manager, iSCSI/SAN Manager, Hybrid Share, NFS, SNMP. **The test is not "is this running?" but "what consumes this?"** | Open — raised 2026-08-04 | 2026-08-04 | Q3 2026 |
| **POA&M-064** | 3.13.1, 3.13.5, 3.5.3 | **Published-service inventory method was structurally blind.** `DIWAI-EV-SC-2026-08-02` was built from `pfctl -s nat` — redirections only — and therefore recorded `.149` as publishing nothing while `pf` passed **SSH from any internet source** to it (password auth, no MFA, on the host holding the plaintext CUI store). Closed by C92 (`DIWAI-CR-2026-08-14`); **the item remains open for the method**: every published-service inventory must read `pfctl -s nat` **and** `pfctl -sr`, and reconcile against listening sockets on the boundary host | Open — raised 2026-08-04 | 2026-08-04 | Q3 2026 |
| **POA&M-065** | 3.1.1, 3.5.2, 3.4.7  | **Two unrestricted service keys on the Mac.** `[EMAIL-REDACTED]` and `[EMAIL-REDACTED]` in `~/.ssh/authorized_keys` carry **no `from=`, no forced `command=`** — either grants a full interactive shell to any holder. The adjacent cert-sync key shows the correct pattern is already known and applied elsewhere. **Not remediated immediately** — the Wazuh archive pipeline was repaired earlier in this assessment and must be verified after any change. `dc1.[DOMAIN.ORG]` suggests one key may itself be an architectural remnant (see POA&M-063). **Confirmed 2026-08-07 and one key removed** — `[EMAIL-REDACTED]` (`SHA256:5oc7MOXppkIr…`) had **no private half on this system or the VM** and was **inherited from the CyberHygiene Project build during documentation duplication**; `dc1` is the domain controller for **[DOMAIN.ORG], a separate boundary**, mislabelled with the `[DOMAIN.ORG]` domain. Zero use in 7 days of logs; exposure latent (pf admits `sshd` only from `[LAN-IP-REDACTED]/24`). **Scope now: the ONE remaining unrestricted key, `[EMAIL-REDACTED]`.** It is the **sole blocker on the 3.7.5 −5 recovery** after POA&M-007 closed, because the `Match Address [LAN-IP-REDACTED]` exemption grants it a single-factor full interactive shell. **Remedy:** the push script runs `ssh … "mkdir -p ~/nas-staging"` before its `scp`, so a forced `command="scp -t /Users/[USERNAME]/nas-staging/"` requires dropping that `mkdir` (the directory is permanent); interim step needing no VM change is `from="[LAN-IP-REDACTED]",restrict`. **Also in scope:** `wazuh-log-archive` passes `-o StrictHostKeyChecking=no` on both its `ssh` and `scp` calls, so it accepts any host key this host presents — **closed with this item** (`StrictHostKeyChecking=yes`, against an already-pinned host key) | **Closed — Resolved 2026-08-07** (`from=` + forced `command="/usr/bin/scp -t /Users/[USERNAME]/nas-staging/"` + `restrict`; destination pinned **server side**, command execution and pty verified refused, full production job verified end to end; `DIWAI-CR-2026-08-18`). **3.7.5 recovered, +5** | 2026-08-04 | Closed 2026-08-07 |
| **POA&M-066** | 3.5.10, 3.13.8       | **DSM API accepts cleartext authentication on port 5000.** The port serves a JavaScript redirect shim to :5001, which protects browser navigation only. `http://[LAN-IP-REDACTED]:5000/webapi/auth.cgi` returns a response **identical to HTTPS**, so credentials submitted by any script travel in the clear. **This places the +5 recovered for 3.5.10 on 2026-08-03 at risk** — DSM is in-boundary and its admin password is a system authenticator. Not internet-published (no `pf` rule); reachable from [LAN-IP-REDACTED]/24 only. **POA&M-033 was closed on the browser path** (`nas.[DOMAIN.ORG]` → 301) and never exercised the API path. Remedies: disable the HTTP port if DSM allows; or build a full DSM firewall allow-list (see the lockout warning in `DIWAI-CR-2026-08-15` §3 — Synology's firewall is deny-by-default) | Open — raised 2026-08-04 | 2026-08-04 | Q3 2026 |
| **POA&M-067** | 3.3.4, 3.6.1, 3.14.6 | **Detection without delivery.** `diwai-control-health` correctly detected a four-day archive-push failure (2026-08-04 → 08-06) and mailed the alert to **`root`'s local mailbox on the VM, which nobody reads**. The owner never saw it; the failure was found by inspection. POA&M-055 established that the check verifies the *right thing* — it did not establish that anyone **receives the answer**. **Remedy:** route alerts to a monitored channel (owner's real mailbox, or the incident-capture endpoint), and prove delivery by sending a test alert and **observing arrival**, not by the mail command exiting 0. **PREMISE CORRECTED 2026-08-07: delivery was never broken.** `/etc/aliases` maps `root: [USERNAME]`, there is **no `/var/spool/mail/root`**, Dovecot delivers to `maildir:~/Maildir`, and **93 of the 94 unread messages in the owner's real mailbox are these alerts**, spanning 08-02 → 08-07 and readable in Roundcube throughout. The conclusion was right, the mechanism wrong — the written remedy would have moved working mail to a new address and left the defect intact. **The actual defect was signal-to-noise:** a 15-minute timer mailing on **every** failing run with no de-duplication (up to **96 messages/day**), of which **81 of 93 were one unremediated failure** (chrony, now POA&M-010 reopened), burying the archive-staging alert (**×8**), a dashboard 500/LDAP-bind failure, and a **CRITICAL vulnerability inside its 72h window** | **Closed — Resolved 2026-08-07** (state-change alerting: mail on new failure, on clearance, or once per 24h; recovery notice added; `syslog` left un-deduplicated so the Wazuh audit record stays complete; **verified by observing arrival in the Maildir across sent / suppressed / recovered runs**; `DIWAI-CR-2026-08-20`) | 2026-08-06 | Closed 2026-08-07 |
| **POA&M-068** | 3.3.1, AU-11, CP     | **Wazuh archive key is not escrowed.** `/etc/wazuh-archive.key` (root:root 0600) exists **only inside the VM**; no copy in `~/diwai`, the Nextcloud CUI store, or on the NAS beside the archives it decrypts. Recovery today depends on a chain entirely within one building: encrypted archives (NAS) → key (inside the VM image on the NAS) → **LUKS passphrase (sealed envelope in the rack)**. The chain works — the 2026-08-04 restore test confirmed the key survives — but **site loss makes every archived alert permanently unreadable**. **The risk is already stated in `CUI_Backup_Procedures_v2.0`, `DIWAI-RAR-001` and `DIWAI-IR-TTX-001` and was tracked in none of them** — the same defect as D-3…D-6, which lived only inside §7 of the risk assessment until opened as POA&M-049…-052. **Remedy:** escrow the key with the off-site sealed LUKS passphrase (POA&M-026) so one action covers both, and include it in the off-site rotation under POA&M-050. **Do not store it on the NAS** — that would place key and ciphertext on one device | Open — raised 2026-08-06 | 2026-08-06 | Q3 2026 |
| **POA&M-069** | 3.4.7, 3.5.2, 3.1.5  | **Root's authentication stack loads a module from an admin-writable path.** `/etc/pam.d/sshd` references `/opt/homebrew/lib/security/pam_google_authenticator.so`. The full path is unavoidable — **SIP protects `/usr/lib/pam`**, PAM's default search directory — but the Homebrew path chain is owned `[USERNAME]:admin` with **`/opt/homebrew/lib` group-writable** (`drwxrwxr-x`, admin = `root`, `sysadmin`, `[USERNAME]`). The `security` directory or the symlink inside it can therefore be replaced **without `sudo` and without a sudo audit record**, changing what root executes during authentication; a Homebrew upgrade or a compromised formula does the same silently. **Not escalation across a trust boundary** — both admin accounts can already `sudo` — but it removes authentication and audit from the step that gains root context. **This is a recorded defect class on this system:** `pf_diwai.conf` was moved out of `/Users/[USERNAME]` for exactly this reason (`DIWAI-CR-2026-08-03`, "was user-writable, loaded as root"). **Remedy:** copy the module to `/usr/local/lib/pam/` (`/usr/local` is `root:wheel`), 444 `root:wheel`, and repoint `/etc/pam.d/sshd`; also decouples the auth stack from Homebrew version churn. **Note the failure mode is closed, not open** — an absent module fails authentication, locking out interactive SSH while leaving the `publickey`-only automation paths and the console unaffected | Open — raised 2026-08-07 | 2026-08-07 | Q3 2026 |
| **POA&M-070** | 3.8.9, 3.3.1, 3.12.3 | **The 2026-08-06 archive-push repair did not hold, and the verification method could not have detected it.** `DIWAI-CR-2026-08-16` moved `nas-archive-push` from a LaunchDaemon to a LaunchAgent (C94) on the reasoning that a system-domain process cannot write to a session-scoped SMB mount. **It failed again at 03:00 on 2026-08-07 with the identical error** — `cp: /Volumes/home/Backup/SecureMac/wazuh-alerts/…enc: Operation not permitted`, `launchctl print gui/501/org.diwai.nas-archive-push` → `last exit code = 1`. **The binding cause is TCC, not the launchd domain.** `Operation not permitted` is `EPERM` from macOS privacy enforcement; POSIX permissions produce `EACCES`. Demonstrated directly: the same path was **writable from an interactive shell at the same moment the agent was refused**, because an interactive shell inherits Terminal's TCC grant and a launchd-spawned process has none — network volumes are TCC-protected. **The domain change was necessary and not sufficient.** **The 08-06 verification was an interactive run — the single execution context that carries the grant — so it could not distinguish the fix from the bug.** Third instance of the "job appears healthy while doing nothing" category (POA&M-063); second consecutive failure that POA&M-067's unread-mailbox gap would have hidden. **Interim:** pending archive pushed by hand and SHA-256 verified (staging empty, NAS 5 → 6). **Remedy:** grant Full Disk Access to the executable launchd invokes, and **verify by observing an unattended 03:00 run succeed — not by another interactive run** | **Closed — Resolved 2026-08-07** (Full Disk Access granted to a purpose-scoped root-owned helper, `/Library/PrivilegedHelperTools/nas-push-runner`, rather than to `/bin/bash`; **verified from a launchd-spawned run** — `Pushed 1 file(s); 0 failure(s)`, `last exit code = 0`; `DIWAI-CR-2026-08-19`) | 2026-08-07 | Closed 2026-08-07 |
| **POA&M-071** | 3.12.3, 3.3.4, 3.6.1  | **A health check that fires identically on success and on failure.** `/usr/local/sbin/nas-archive-push`, when staging is empty, runs `find "${STAGING}" -name '*.enc' -mtime -2` and logs `NOTE: no archive has arrived in the last 48h` if nothing matches. **It searches the staging directory, which is empty precisely when the pipeline is working** — a successful push moves the file out. So the NOTE appears on every healthy run, and also when the VM job has genuinely stalled: **the signal is the same in both states and therefore carries no information.** Observed firing during the POA&M-070 verification minutes after a confirmed good delivery. **A daily false alarm is worse than no alarm — it trains the reader to skip the one line that would matter.** Same family as POA&M-055 (verified services were *running*, not *working*) and POA&M-067 (output reached nobody); this one reports into a log that IS read and says nothing. **Remedy:** test the **destination** — if the newest `.enc` on the NAS is older than ~48 h, either the VM job or the push has stopped. Five lines, and it makes the check falsifiable | **Closed — Resolved 2026-08-07** (mount discovery moved before the "nothing to push" branch — the defect was structural, since the destination was unknown at the point of the check — and freshness is now measured at the **destination** against `STALE_HOURS=48`, distinguishing **four** states where there was one, with the healthy case **stated positively** so a silent check can be told from a working one. All four branches exercised on rewritten copies, then verified in production through launchd and the POA&M-070 TCC grant: `Delivery current: newest archive on the NAS is 1h old`, `last exit code = 0`. `DIWAI-CR-2026-08-22`) | 2026-08-07 | Closed 2026-08-07 |
| **POA&M-072** | 3.14.1, 3.11.2, 3.12.3 | **CVE report summary counts are kind-blind and overstate exposure.** `diwai-cve-scan` writes a top-level `counts` field computed from **severity alone**. `cve-scan-2026-08-03.json` therefore reads `counts: {CRITICAL: 1, IMPORTANT: 27}` while the same report's `kinds` field reads `{NO-CODE: 5, STREAM-MIGRATION: 8, THIRD-PARTY: 15}` — **no PATCH-class findings at all.** The one "CRITICAL" is `nginx-filesystem` (`CVE-2026-42945`), which contains no executable code (disposed 2026-08-07, `DIWAI-PR-LOG`). **A reader who trusts the summary sees an unpatched CRITICAL vulnerability that does not exist**, and the 2026-08-02 control-health alert did exactly that before the `kind == PATCH` filter was added on 08-04. The detailed findings are correct; only the summary misleads. **Remedy:** compute `counts` per kind, or publish the PATCH-class subtotal alongside the severity totals, so the headline figure matches what `DIWAI-PR-001 §6` actually acts on. Same signal-quality family as POA&M-071 and POA&M-067 | **Closed — Resolved 2026-08-07** (`counts_actionable` added alongside `counts`, both carrying an explicit `_scope` string in the JSON; log summary now states the PATCH-class subtotal, or says none and names the kinds §6 does not clock. Verified live: `counts {CRITICAL:1, IMPORTANT:31, MODERATE:10}` vs **`counts_actionable {IMPORTANT:4, MODERATE:9}` — no CRITICAL**. `DIWAI-CR-2026-08-21`) | 2026-08-07 | Closed 2026-08-07 |
| **POA&M-073** | 3.5.3, CP, PS, 3.1.1 | **The break-glass account cannot authenticate.** `dscl . -authonly sysadmin` returns **`eDSAuthAccountDisabled` (-14167)**, and the cause is structural: `dscl . -read /Users/sysadmin AuthenticationAuthority` returns **No such key**, so the account has **no registered password mechanism**. `failedLoginCount = 18` shows attempts have been made and failed before, so this is not new. **A POA&M-007 precondition recorded it as working:** *"Verify the `sysadmin` break-glass account actually logs in — SATISFIED, verified 2026-08-04"*, on owner confirmation and citing `fdesetup list`. **`fdesetup list` proves FileVault enablement, not the ability to authenticate** — the wrong property was verified, and it was accepted on assertion rather than test. **Consequence:** this host's documented failure mode is not a lockout but a **DFU reauthorisation — drive wiped, OS reinstalled** (`DIWAI-INC-002`, twice in 2026). `sysadmin` is the only recovery path, and **it was dead while the authentication stack was modified on 2026-08-06 and 2026-08-07.** Nothing broke; the safety net was simply absent. **Remedy:** reset the password with `sysadminctl -resetPasswordFor sysadmin` (recreating the authority record), confirm admin group membership, re-add with `fdesetup add`, **then TEST** — `dscl . -authonly sysadmin` returning silence, with the output recorded. Reset and re-check `failedLoginCount`. **Repairing an admin account's authentication is itself an authentication change on this host and must be its own deliberate step** | **Closed — Resolved 2026-08-07** (password reset with SecureToken authorisation; **authentication VERIFIED BY TEST** — `dscl . -authonly sysadmin` now succeeds silently, `failedLoginCount` 18 → 0, SecureToken still ENABLED. **The "no `AuthenticationAuthority`" rationale above is WITHDRAWN:** that attribute is filtered by OpenDirectory for non-privileged reads of *another* user's record — the same command shows it for the reader's own record and not for another's — so it proved nothing. The inability to authenticate was real; **the cause is left undetermined rather than guessed.** MFA on this account was considered and **declined** with owner agreement: unreachable by SSH, its path is the console where MFA means touching the PAM stack behind two DFU rebuilds, and a phone-dependent factor undermines break-glass; a strong **escrowed** password is the control instead. **Repair required console access** — `sysadminctl` fails over SSH with `errAuthorizationInteractionNotAllowed`. `DIWAI-CR-2026-08-26`) | 2026-08-07 | Closed 2026-08-07 |
| **POA&M-074** | 3.12.4, 3.4.1        | **The SSP states a monitoring capability that was withdrawn two days later.** SSP v2.18 §3.4 reads *"**Prometheus + node-exporter retained**, so metrics collection is unaffected; only visualization was retired"* — written 2026-08-03 for the Grafana decommission (`DIWAI-CR-2026-08-04`). On **2026-08-04**, changes **C90/C91** (`DIWAI-CR-2026-08-13`) disabled **both**, after Grafana's removal left the stack orphaned and reachable unauthenticated on 9090. Verified 2026-09-13: both `disabled`, nothing listening on 9090, no metrics retained since 2026-08-04. **No control impact** — AU-6 / 3.3.3 and 3.14.7 rest on Wazuh, Suricata and auditd (C64/C65), all continuously running; the defect is the SSP asserting a live capability that does not exist. **Distinct from POA&M-048**, which concerns working copies drifting from canonical: here the canonical text itself was overtaken by a later change within the same engagement and never revisited. Remediation: correct the §3.4 row to record metrics collection withdrawn 2026-08-04 per `DIWAI-CR-2026-08-13`, at the next SSP reissue. | Open — raised 2026-09-13 | 2026-09-13 | Q4 2026 |
| **POA&M-075** | 3.14.2, 3.14.6, 3.12.4 | **YARA detection has never raised an alert.** `ossec.conf` had no `<ruleset>` block, so the YARA rules could not load on either host (`DIWAI-CR-2026-09-06`). Rules now load, but no YARA match has been exercised end to end, and the SSP describes YARA as an operating SI-3 layer | **Closed — Resolved 2026-09-13** (YARA alert proven end to end on both hosts — VM 2 s, Mac on the hourly scan; SSP 3.14.2 corrected; `DIWAI-CR-2026-09-06` §3a) | 2026-09-13 | Q4 2026 |
| **POA&M-076** | 3.5.6 | **Inactivity disable defined but not enforced.** SSP Appendix E.4 states accounts are disabled after 90 days' inactivity. Tested 2026-09-13: no mechanism exists — 389-DS Account Policy plugin off, no VM-local or Mac inactivity policy. The `sysadmin` break-glass account is the design constraint | Open — **directory half enforced 2026-09-13** (90-day limit proven by refusal, `DIWAI-CR-2026-09-08`); Mac and VM local accounts pending; point withheld | 2026-09-13 | Q4 2026 |
| **POA&M-058** | 3.12.4, 3.4.1 | **Signed policy set describes a materially different system** — ClamAV as an operating control in **6 of 11** policies (12 mentions in `DIWAI-SI-001` alone) and a **NetGate 2100 pfSense firewall in 10 of 11**, at an IP that is actually the Mac. Neither component exists | Open | 2026-08-04 | Q3 2026 |
| **POA&M-057** | 3.6.2 | **No DoD medium assurance certificate** — DIBNet reporting under DFARS 252.204-7012 not possible within 72 h. Moot while no contract exists; certificate has lead time | Open — pre-contract | 2026-08-03 | before first CUI contract |
| **POA&M-055** | 3.12.3, 3.3.4 | **Control-health monitoring verifies services are *running*, not *working*** — `httpd` active passes while every authenticated request returns 500. Demonstrated by a real 6-minute outage on 2026-08-03 that all 24 checks reported healthy | **Closed — Resolved 2026-08-04** (authenticated probe added and negative-tested; 25 checks; `DIWAI-CR-2026-08-11`) | 2026-08-03 | Q3 2026 |
| **POA&M-053** | 3.1.1, 3.5.7         | **Wazuh API still uses shipped default credentials** (`wazuh:wazuh`) and binds `0.0.0.0:55000`. Not reachable off-host today — firewalld does not open 55000 — so a single firewall change would expose full SIEM API control                                                                                                                                                                     | **Closed — Resolved 2026-08-04** (both defaults rotated; API bound to localhost; `DIWAI-CR-2026-08-11`)                                                                                    | 2026-08-03 | Q3 2026           |
| **POA&M-054** | 3.4.1, 3.4.6, 3.12.4 | **mSCP toolchain still inside the CUI boundary** — 2,300 files / 32 MB in the CUI group folder's `trash/`, 43 days after the purge was recorded complete                                                                                                                                                                                                                                        | **Closed — Resolved 2026-08-03** (trash emptied, 32 MB → 0 B, rescanned clean)              | 2026-08-03 | Closed 2026-08-03 |
| **POA&M-049** | 3.11.1, CP, PS       | **Succession and credential escrow** — no individual other than the sole operator can administer or recover the system                                                                                                                                                                                                                                                                        | Open                                                                                    | 2026-08-03 | Q4 2026           |
| **POA&M-050** | 3.8.9, CP            | **Backup copies neither independent nor both current** — TM is current and full; the NAS VM copy is ~2 months stale (15 GB vs 31 GB live). Both copies co-located                                                                                                                                                                                                                             | Open — **restated on evidence 2026-08-03**                                                  | 2026-08-03 | Q3 2026           |
| **POA&M-051** | 3.14.1, 3.11.2       | `wazuh-manager` **version-locked at 4.14.6** — the SIEM receives no security updates while pinned; needs a tested upgrade path                                                                                                                                                                                                                                                                  | **Closed — Resolved 2026-09-13** (manager on **4.14.7**, pin removed; crash was an SVE2 virtual-CPU quirk, fixed with `OPENSSL_armcap`; `DIWAI-CR-2026-09-04`) | 2026-08-03 | Q4 2026           |
| **POA&M-052** | 3.8.9, CP            | **Restoration never tested** — recovery is an assumption; the archive pipeline was found silently non-functional once (POA&M-031)                                                                                                                                                                                                                                                             | Open — **VM tier DISCHARGED 2026-08-04** (8-min verified restore); Mac host and Nextcloud consistency remain                                                                                    | 2026-08-03 | Q3 2026           |
| **POA&M-048** | 3.4.1, 3.4.3, 3.12.4 | **Compliance working copies drift silently from the canonical store** — a stale local SSP was edited and nearly published, which would have reverted 125 lines of canonical content                                                                                                                                                                                                           | Open — **detection implemented 2026-08-03**, enforcement pending                            | 2026-08-03 | Q4 2026           |

---

## ITEM DETAIL — NEW CLOSED ITEMS (2026-08-01)

### POA&M-011 — Unattended upgrade disabled the SIEM — CLOSED

An unattended `dnf` transaction (2026-07-31 17:04, `User: System <unset>`)
upgraded 88 packages including a new kernel and Wazuh 4.14.6 → 4.14.7. The new
build's `wazuh-apid` aborts with SIGILL on this platform, taking the whole unit
down for **~21 hours, undetected**. Resolved: downgraded to 4.14.6 (verified not
a corrupt install — a full reinstall of 4.14.7 reproduced the fault), pinned via
`versionlock`, and set `dnf-automatic` to download-only. Evidence
`DIWAI-EV-AU-2026-08-01`. **Residual:** telemetry for that window is
unrecoverable; see POA&M-012 for why local records did not cover it.

### POA&M-012 — Audit retention ≈ 1 hour — CLOSED

`max_log_file 8` MB × `num_logs 5` = a 40 MB cap on a **dedicated 10 GB
partition that was 2% used**. Measured window: 14:02 → 15:04. Resolved: raised to
64 MB × 100 (~6.4 GB). Verified `auditd` active, 113 rules, `lost 0`.

### POA&M-013 — No account lockout, no password history — CLOSED

`passwordLockout: off` and `passwordHistory: off` in 389-DS — the directory
behind the dashboard, Nextcloud, mail and the NAS, with mail and webmail
published to the internet, permitted **unlimited online password guessing** and
unrestricted password reuse. Resolved: both enabled. Supporting values were
already correct and unchanged (`passwordMaxFailure 3`,
`passwordLockoutDuration 3600`, `passwordUnlock: on` so lockouts self-clear,
`passwordInHistory 6`).

**Verified by negative test 2026-09-13** (`DIWAI-CR-2026-09-03`). Directory: reuse refused *"password in history"*; correct password refused after 3 failures *"Exceed password retry limit"*. **Mac: history did NOT hold** — the `diwai.password.history` rule applied 2026-08-07 was malformed and silently skipped; repaired in session and then refused reuse. Mac lockout held. The closure stands on this evidence, not on the 2026-08-01 configuration change.

### POA&M-014 — Cleartext SMTP authentication — CLOSED

Port 25, redirected from the internet, accepted SASL authentication without TLS
(`smtpd_sasl_auth_enable=yes`, `smtpd_tls_auth_only=no`, dovecot
`disable_plaintext_auth=no`). Credentials are LDAP-backed, so a captured mail
password was a directory password. Resolved: `smtpd_tls_auth_only=yes` and
`disable_plaintext_auth=yes`. **Verified from a non-loopback client** (both
daemons treat loopback as secured, so a localhost test proves nothing): :25
offers no AUTH before STARTTLS, :143 returns `LOGINDISABLED`, :587 and :993
unaffected. Zero SASL auths in logs since 2026-07-01 confirmed the change broke
nothing. Evidence `DIWAI-EV-SC-2026-08-02`.

### POA&M-015 — Weekly mSCP scan non-functional — CLOSED

**Two independent defects, either sufficient alone:** (1)
`/usr/local/bin/run-mSCP-scan.sh` was a **zero-byte file**; (2) the LaunchDaemon
invoked `/usr/bin/zsh`**, which does not exist on macOS**. The scan therefore
produced nothing since ~June while the SSP claimed a maintained weekly scan and
published a figure last valid in **April**. Resolved: audit script installed to a
stable path, wrapper written (`--check` only), `ProgramArguments` rewritten to
use the wrapper's shebang. **Verified by output, not by artifact** — scan log
grew 0 → 256 bytes, audit plist refreshed, result `131/136 (96%)`.

### POA&M-016 — Mac password minimum 4 characters — CLOSED

`policyAttributePassword matches '.{4,}+'`; the `diwai_phase1` mSCP baseline
contains no password complexity rules, so the macOS default stood. Resolved:
raised to 12. **Durability caveat:** macOS increasingly enforces password policy
via configuration profiles; re-verify after the next reboot and consider adding
password rules to the mSCP baseline.

**Verified by negative test 2026-09-13** (`DIWAI-CR-2026-09-03`): Mac minimum **14** refuses a 6-character password. **Related directory gap found and closed:** 389-DS `passwordMinLength` was not enforced (`passwordCheckSyntax: off`); set to **14** with syntax checking on, boundary-tested (13 refused, 14 accepted).

### POA&M-017 — Policy identifiers did not match SSP citations — CLOSED

All eleven policies declared `TCC-*-001` while the SSP and nine evidence
documents cited `DIWAI-*-001`. **No document carried a** `DIWAI-*` **identifier** —
every policy citation in the SSP was a dangling reference. Six internal
cross-references also pointed at identifiers matching no document. Resolved as an
editorial correction across 22 files (canonical + public working copies);
versions deliberately not incremented. `TCC-AT-002` was **not** renamed — it
cites a training *procedure* that has never been written, now annotated
`DIWAI-ATP-002 — NOT YET ISSUED, see POA&M-008`.

### POA&M-018 — LDAP ports open zone-wide — CLOSED

`389/tcp` and `636/tcp` were in the firewalld zone `ports:` stanza, permitting
the entire zone; per-host rich rules created a false impression of restriction.
Resolved: both removed from `ports:`, explicit rich rule added for the Mac on
636, redundant Mac 389 rule removed. Cleartext LDAP reachability reduced from
the whole zone to a single host.

### POA&M-019 — Nothing verified that controls were running — CLOSED

The governing finding. Resolved by `/usr/local/sbin/diwai-control-health` +
15-minute timer: 19 checks covering SIEM, agent connectivity, auditd and lost
records, audit headroom, **a genuinely selected chrony source**, scan-output
freshness, protective services, SELinux/FIPS, and certificate expiry.

Two checks are written specifically against observed failure modes: it requires
a **selected** chrony source (`^*`) because `chronyc tracking` reported perfect
synchronisation while the clock was 24 minutes wrong; and it checks for scan
**output** rather than whether a job ran, because the mSCP job ran faithfully and
did nothing.

Alerting is dual-path — syslog (Wazuh) **and** mail, because a Wazuh-only alert
is worthless when Wazuh is what failed. **Testing the failure path found the mail
channel was bouncing** (`maildir access problem`, no `/root/Maildir`); fixed by
aliasing `root: [USERNAME]`, re-tested `status=sent` and confirmed in the mailbox.

---

## ITEM DETAIL — NEW OPEN ITEMS

### POA&M-020 — NAS cleartext privileged bind — OPEN (Contained)

The Synology binds 389-DS as `cn=Directory Manager` — the directory
superuser — over **cleartext port 389**: 184 connections, zero TLS, to read
Samba domain attributes. The most privileged credential in the system used for
one of the least privileged tasks. **Contained** by POA&M-018 (reachable only
from the NAS) but not fixed. Requires DSM access: reconfigure to LDAPS (636)
with a **scoped read-only bind account**, or disable the client if nothing
consumes it. Likely cause of the fallback to 389 is a stale CA on the NAS — the
certificate issuer changed from `R12` to `YE2`.

### POA&M-021 — Directory Manager credential rotation — OPEN

The credential has crossed the network in cleartext at least 184 times in the
retained log window. It must be treated as exposed. Blocked by POA&M-020;
rotating before the NAS is reconfigured would break the NAS integration.

### POA&M-022 — No CVE-level vulnerability scanning — OPEN

OpenSCAP and mSCP perform **configuration compliance** scanning, not
**vulnerability** scanning. No OVAL vulnerability feed, Trivy, or equivalent is
deployed, so software with known CVEs is not flagged. 3.11.2 was likely credited
to compliance scanning previously; this is a definitional correction, not a
regression. The Wazuh 4.14.7 defect illustrates the gap.

### POA&M-023 — No separation of internet-facing and CUI tiers — OPEN

Mail (.147), webmail (.145) and OpenVPN (.146) all redirect to **[LAN-IP-REDACTED]**,
the same VM hosting 389-DS, the Nextcloud MariaDB and the Wazuh manager. No DMZ.
A compromise of a published service lands on the identity store with no lateral
movement. Mitigations (FIPS, SELinux, fapolicyd, Suricata, host firewall) reduce
likelihood but do not provide separation. Remediation is architectural — a
second VM for the internet-facing tier.

**DECISION 2026-08-03 — RISK FORMALLY ACCEPTED UNTIL 2027-03-31**
(`DIWAI-RAR-001` §7.1, D-2). This is the highest-rated risk on the register
(R-02, HIGH). Acceptance is explicit and dated, replacing what the risk
assessment identified as acceptance *by default*.

**Architectural option considered and DEFERRED 2026-08-03 — relocating the
Nextcloud datastore onto the VM.** Raised by the system owner. Recorded here so
the reasoning is on file and the question is not re-litigated from scratch.

*Motivation examined:* FIPS 140 coverage, and removing the Mac-side plaintext
exposure (Nextcloud stores documents as **plain files** at
`/opt/local/nextcloud/data`; server-side encryption is `enabled: false`, so
anything running as `[USERNAME]` or root reads CUI directly, outside Nextcloud's
2FA, ACLs and `admin_audit`).

*The FIPS motivation does not apply.* SSP §4 already records the Apple Secure
Enclave (FIPS 140-2 Level 1) on the Mac and FIPS mode on the VM, and **3.13.11
already scores a zero deficit** — "FIPS-validated encryption is in use
throughout." Relocation recovers no points and closes no FIPS gap.

*Genuine gains identified:* (a) a Mac-level compromise would no longer yield
plaintext CUI, since the data would sit inside the VM's LUKS volume whose key is
not on the Mac; (b) SELinux confinement of the serving process, which macOS does
not equivalently provide; (c) **restore consistency** — one VM snapshot would
capture database and files atomically, dissolving the split-brain problem in
POA&M-050. Capacity is not a constraint (`/opt` on the VM has 50 GB free against
243 MB of data).

*Why deferred — it worsens this very risk.* **The VM is the internet-facing
host.** Mail, webmail and OpenVPN terminate there. Today the CUI *documents* are
one host removed from the published services; relocating them means a single RCE
in Postfix, Dovecot, Roundcube or OpenVPN yields the directory, the database
**and every CUI document** rather than the first two. That raises the impact of
R-02 — the highest-rated risk on the register — weeks after it was formally
accepted (D-2 above).

*Assumption corrected:* relocation does **not** achieve physical separation. The
VM runs on the Mac; the qcow2 occupies the same disk, machine and power feed.
What changes is which OS mediates access and that a second encryption layer
applies. Defence in depth, not isolation — and it should not be described as
isolation in the SSP.

*Disposition:* **right destination, wrong sequence.** The relocation becomes
correct **after** this item's tier split, when published services sit on a DMZ
VM and CUI sits on an internal VM unreachable from the internet. Doing it first
puts the documents on the wrong side of a boundary that does not yet exist.
Interim mitigations adopted instead: dedicated service account with `0700` on the
data directory (**not yet done**), and Wazuh FIM coverage of that directory
(**deployed and verified 2026-08-03**, see F-2026-08-34).

**F-2026-08-34 — FIM coverage of the CUI document store — IMPLEMENTED 2026-08-03**

Deployed centrally as a shared `agent.conf` block scoped `os="Darwin"`, so no
change was required on the Mac host itself. Covers
`/opt/local/nextcloud/data/__groupfolders` and `/opt/local/nextcloud/config`.
**2,503 files are now catalogued with SHA-256** where nothing previously recorded
any activity against that directory at all.

**Verified working, not assumed:** a modification was detected and alerted —
*"File '…/.fim-test-20260803' modified · Mode: scheduled · Changed attributes:
size"* — approximately 13 minutes after the change.

**Three properties that must not be lost in later edits:**

1. `realtime` **is silently ignored on macOS.** Wazuh accepts the attribute, the validator passes, the manager merges and pushes it — and the agent discards it, logging `WARNING (6908): Ignoring flag for real time monitoring`. The API confirms `realtime: no`. `<frequency>3600</frequency>` **is therefore load-bearing:** without it the default is 43200s, so the control would have carried a **12-hour** detection window while the configuration file read "realtime". Detection is scheduled, up to 1 hour.
2. `report_changes="no"` **is deliberate.** Enabling it writes before/after diffs of every changed file into `/Library/Ossec/queue/diff/` — a second, unmanaged copy of CUI content outside the protected store and its access controls. An alert must say *what* changed, never reproduce it.
3. `alert_new_files` **is unset (default** `no`**)** — file *creation* in the CUI store is catalogued but **not alerted**; only modification and deletion alert. An attacker *adding* a file (a planted script, an exfil staging copy) would not raise an alert. Enabling it would also alert on every legitimate document added, which in a live document store is substantial noise. **Left off pending an owner decision** rather than changed silently.

**Scope limit, stated plainly: FIM does not detect reads.** It sees create,
modify and delete. It will **not** detect an attacker copying the CUI store out,
which is the exposure that prompted this work. FIM addresses tampering and
destruction; the read exposure is addressed only by the service-account change
above. This item must not be cited as mitigating unauthorised disclosure.

**Testing note carried into the config file:** do not use `agent_control -R` to
force a scan when testing FIM. An agent restart **re-baselines the FIM
database**, so the change under test becomes the new baseline and never alerts.
That produced four consecutive false negatives during this deployment before it
was identified — the tool was correct and the test method was wrong.

**The acceptance is conditional.** It holds only while all three remain true:

1. the compensating controls stay operational — pf, per-host firewalld rules, Wazuh, Suricata, SELinux, fapolicyd, FIPS-encrypted storage;
2. the expiry is honoured — **re-decided, not silently renewed**, at 2027-03-31;
3. **no additional internet-facing service is published into the boundary.** Publishing one voids this acceptance and requires it to be re-decided immediately.

Condition 3 is the one most easily breached without noticing, because publishing
a service is a routine act that does not feel like a risk decision.

### POA&M-024 — Wireless unauthorised and undocumented — OPEN

Wi-Fi is enabled and connected on the CUI host with a DHCP lease on an external
network ([HOME-LAN-REDACTED]). Link security is **WPA2/WPA3 Personal**, so 3.1.17 is
satisfied — but 3.1.16 requires wireless access to be *authorised* before it is
allowed, and the SSP's topology does not include it. Either authorise and
document it, or disable the interface.

### POA&M-025 — Patch-review cadence undefined — OPEN

`dnf-automatic` is now download-only, which satisfies change control but means
**3.14.1 is no longer satisfied by automation**. A defined review cadence is
required, and the resulting SCAP deviation
(`dnf-automatic_apply_updates` fails; VM CUI profile 102/102 → **101/102**) must
be recorded in the SSP as an accepted, justified variance rather than drift.
7 package updates are currently pending.

### POA&M-035 — Detail lost behind a citation to a document never issued — CLOSED 2026-08-04
**Resolved by supplying the missing content, not by correcting a reference.**

POA&M v1.2 directed readers to "v1.1 for unchanged 001, 003–008". **No June-dated
v1.1 was ever issued.** Confirmed 2026-08-04 across the canonical store, both git
repositories and the historical volume: the only v1.1 documents are two **April
2026** files in `archive/reference_system_2_mac/poam/`, which predate this lineage
and use a different numbering series. They are not the cited document.

**The consequence was not cosmetic.** Item detail for **003, 004 and 007 — all
open — existed in no current document; only one-line summary rows survived.** Two
of them (004, 007) carry the largest single scoring opportunity on the register
(**+10**) and had no recorded implementation state, obstacle or safety constraint.

**Action taken:** detail written for **POA&M-003, -004 and -007** from verified
system state — including the `diwai_rsa` passphrase problem that makes "public key
plus TOTP" a weak 3.5.3 claim, the automation dependency that blocks the obvious
fix, and the `DIWAI-INC-002` safety constraints for PAM work. Items 001 and 006
are closed and need none.

**v1.2 was deliberately not edited.** It is superseded, and its text is the record
of what was published on 2026-06-12. Rewriting it would falsify that record; the
correction belongs in the current version, which is where readers are sent.

### POA&M-003 — mSCP failing rules (Mac host) — OPEN
**Detail supplied 2026-08-04** (POA&M-035 — see that item; no detail had existed
in any current document).

**Current state: 2 failing rules of 136 (134/136).** The item text has read "5,
not 8" since the 2026-08-01 rebaseline; the figure is now **2**, following the
remediation in `DIWAI-CR-2026-08-02`. Verified from the local mSCP audit plist,
2026-08-04.

The two remaining are tracked in detail under **POA&M-029**:
`audit_settings_failure_notify` and `os_firewall_default_deny_require`. Both pair
with assessment findings rather than being cosmetic baseline misses.

**Baseline in use:** mSCP profile `diwai_phase1`, NIST 800-171 aligned, evaluated
by `/usr/local/libexec/mSCP_diwai_phase1_compliance.sh` on a weekly timer. *(Note:
`DIWAI-CMP-001` cited the CIS Apple macOS Benchmark as the Mac baseline until
corrected on 2026-08-04 — see POA&M-058.)*

**History worth retaining:** the failing-rule count was **unverifiable between
April and August 2026** because the weekly scan was executing a zero-byte script
(POA&M-015, closed 2026-08-01). Any figure quoted from that period is unsound.

### POA&M-004 — TOTP MFA deployment — VM — CLOSED 2026-08-04
**Detail supplied 2026-08-04.**

**Current state:** SSH to `services.[DOMAIN.ORG]` is **public-key only**
(`PasswordAuthentication no`, `PubkeyAuthentication yes`). **`pam_google_authenticator.so`
is installed but configured in no PAM stack.** There is no second factor.

**The obstacle is not installation.** `diwai_rsa` **has no passphrase** (verified
2026-08-04), so the key file alone grants access — a single factor, and one that
sits in `~/.ssh` on the Mac. Adding TOTP to that yields public key *plus* TOTP:
**two factors of the same category** ("something you have"), which is a weak claim
against 3.5.3. A defensible deployment requires either a passphrase-protected
interactive key or an equivalent knowledge factor.

**Automation dependency:** `post-upgrade-verify.sh` and `backup-status-push` use
`diwai_rsa`. Passphrasing it breaks them. The standard resolution is separate
keys — passphrase-protected for interactive use, a restricted automation key
(`command=`/`from=` in `authorized_keys`) for machine use. **This decision is
unmade and blocks the work.**

**Safety constraints, drawn from `DIWAI-INC-002`:** the April 2026 total lockout
was caused by a PAM module set `required` against a **network-dependent** backend
that was not running. `pam_google_authenticator` reads a **local** secret and does
not share that failure mode. Nevertheless: keep an authenticated session open
throughout, test from a second session before closing the first, and note that the
**UTM console on the Mac is an out-of-band fallback** if SSH is lost.

**Scoring:** 3.5.3 and 3.7.5 carry **−5 each**. 3.5.3 has a partial-credit rule —
−3 if MFA covers remote and privileged users only, −5 if no users. Currently −5.

### POA&M-007 — TOTP enrollment — Mac host — CLOSED 2026-08-06
**Detail supplied 2026-08-04. Closure recorded 2026-08-07 — `DIWAI-CR-2026-08-17`.**

> **CLOSURE NOTE.** SSH MFA is enforced: `publickey,keyboard-interactive:pam` for
> all sources, with `Match Address [LAN-IP-REDACTED]` reverting to `publickey` for the
> service VM's two automated jobs (verified rc 0 after the change, twice).
>
> **Enforced is not exercised.** No interactive key exists for the owner, so
> `publickey` — the mandatory first factor — cannot be satisfied by any human,
> and `pam_google_authenticator.so` has never loaded. The correct statement of
> this host's state is *"no nonlocal interactive path exists, and MFA is enforced
> on any future one"* — **not** "three-factor login". Evidence for 3.7.5 and
> 3.5.3 must say so.
>
> **No SPRS points claimed.** 3.7.5 is gated on POA&M-065 (one unrestricted key
> still holds a single-factor full shell under the exemption); 3.5.3 is capped at
> −3 by single-factor console access and is not defensible even at −3 until an
> interactive key exists and one MFA login is recorded.
>
> **The destructive failure mode described below did not apply to this change.**
> It modified `/etc/pam.d/sshd` only; `authorization`, `login`, `screensaver` and
> their variants remain Apple stock, and no account credential, smartcard pairing
> or FileVault user was touched. Worst case was loss of inbound SSH, recoverable
> at the console. The preconditions were still verified first — including a
> same-day Time Machine backup — and they remain binding for changes where the
> mode *does* apply.
>
> **Opened by this work: POA&M-069** — the module loads from an admin-writable
> Homebrew path.

**Current state: password only.** YubiKey PIV was abandoned after the 2026-05-15
lockout (POA&M-001, closed-superseded); the hardware is unpaired and the tooling
removed. `sc_auth list` and `sc_auth identities` return empty — **no smartcard
identity is paired.** The `pam_smartcard.so` entries in `/etc/pam.d/` are Apple
stock and are `sufficient`, so they fall through to password.

**Not to be mistaken for MFA:** the double login prompt observed at boot is
**`DisableFDEAutoLogin`**, enforced by configuration profile — FileVault pre-boot
unlock followed by a separate loginwindow authentication. It is a real control
(the disk-unlock credential cannot also grant a session) but it is **the same
factor twice** and contributes nothing to 3.5.3.

**Higher risk than the VM.** There is **no out-of-band console** for the Mac. The
`sysadmin` break-glass account exists and is in the admin group — a lesson
implemented from `DIWAI-INC-002` — but **it has not been tested**. It should be
verified working *before* any PAM change is attempted on this host.

**The failure mode here is destructive, and worse than a lockout — established
2026-08-04.** The 2026 DFU episodes on this host were **not** hardware failures.
The account password was replaced by a **YubiKey PIV credential**; the resulting
credential mismatch left the Mac unable to complete boot. **Apple's security model
treats that state as requiring device reauthorisation, and the DFU procedure to
clear it wipes the drive and reinstalls the OS.**

**So a botched authentication change on this host does not cost a password reset —
it costs a full rebuild and everything since the last Time Machine restore point.**
That is the mechanism behind the losses in `DIWAI-INC-002`: the usb-guard scripts,
the LaunchDaemon plist and the FIDO2 credential were not corrupted, they were
**wiped and not replayed**.

This materially raises the risk of POA&M-007 relative to POA&M-004:

| | VM (POA&M-004) | Mac host (POA&M-007) |
|:---|:---|:---|
| Fallback if auth breaks | **UTM console**, out-of-band | **None** |
| Worst realistic outcome | Restore VM — **8 min, tested** | **DFU reauthorisation: drive wiped, OS reinstalled** |
| Recovery point on failure | Current | Last Time Machine restore |
| Precedent | none | **Twice, 2026-04-15 and 2026-05-15** |

**Preconditions before any authentication change on this host — all three, not
any of them:**
1. ~~Verify the `sysadmin` break-glass account actually logs in.~~ **SATISFIED — verified 2026-08-04.** The owner confirms the break-glass password has been tested and works, and `fdesetup list` shows **both `sysadmin` and `[USERNAME]` are FileVault-enabled users**:

   ```
   sysadmin,B25E6453-98C7-4680-B7E6-1EF357CF2F72
   [USERNAME],FD9A3DEF-8C4F-4B20-8FFB-CA6E4434D461
   ```

   **This matters at the correct stage.** `DisableFDEAutoLogin` is enforced, so
   the host authenticates twice — FileVault pre-boot unlock, then loginwindow. A
   break-glass account authorised only at loginwindow would cover a *login*
   failure but not the *boot* failure that produced the 2026 DFU episodes.
   `sysadmin` is authorised at **pre-boot**, so it covers the failure mode that
   actually occurred.
2. **Confirm a current Time Machine backup**, since that is the recovery floor.
3. **Prefer a change reversible from a second, already-authenticated session** — never close the last working session until the new path is proven.

**Sequencing:** do the VM (POA&M-004) first. It has a fallback; this does not.
Recorded in **RB-05**.

### POA&M-005 — First annual risk assessment — CLOSED 2026-08-03

**3.11.1 satisfied by** `DIWAI-RAR-001` **v1.1** (NIST SP 800-30 Rev 1, qualitative;
14 risks — 3 HIGH, 10 MODERATE, 1 LOW residual). Signature pending on §7.2.

**Why this sat OVERDUE while the document existed.** The assessment was written
2026-08-02 and stated on its face that it satisfied 3.11.1 and closed this item.
It was never formally **accepted**, and the POA&M status was never updated — so a
completed control read as overdue for a day, and the six decisions it raised had
no route to action. Same defect class as F-2026-08-06: the artefact existed and
the register disagreed. **The lesson is that a document asserting its own closure
does not close anything** — closure is an act recorded in the register.

**All six §7 decisions resolved 2026-08-03** and recorded in `DIWAI-RAR-001`
§7.1: D-1 treat (break-glass LUKS escrow), D-2 accept in writing to 2027-03-31,
D-3 to D-6 opened as **POA&M-049 to POA&M-052**. Four of the six had existed only
inside the assessment with no tracking item and no target date.

### POA&M-059 — Recurring policy obligations have no execution record — OPEN
**Raised 2026-08-04 at the system owner's direction**, while correcting the
policy set under POA&M-058.

The eleven policies state **173 recurring obligations**: **28 daily**, **17
weekly**, **30 monthly**, **53 quarterly**, **45 annual**. Examples: review Wazuh
alerts daily; verify monitoring tools quarterly; verify rack lock daily; review
security bulletins weekly.

**Only 5 are automated** — the VM's `oscap-scan`, `yara-fullscan`,
`diwai-cve-scan`, `diwai-control-health` and archive timers. **For the remaining
manual obligations there is no record that they are performed at all.**

**Why this is a control gap, not administrivia.** A policy stating an activity
occurs daily is a control claim. Where nothing records performance, the claim is
unevidenced, and an assessor testing 3.12.3 (monitor controls on an ongoing
basis) or 3.12.1 (periodic assessment) has nothing to sample. It is also the
governing defect of this whole assessment in a different form: **documented, not
verified.**

**Owner's requirement:** a checklist keyed to the daily / weekly / monthly
obligations in policy, surfaced as a page in the **Admin Portal** that both
triggers the task and records its completion. **Automatic performance and
confirmation is preferred over manual attestation** — an automated check that
records its own result is evidence; a tick-box is an assertion.

**Suggested approach**, for owner decision:
1. Extract the 173 obligations into a machine-readable schedule, tagged by cadence, owning control, and whether automatable.
2. **Automate everything automatable** and have it write a dated result — `diwai-control-health` is the natural executor, since it already runs every 15 minutes with a dual alert path.
3. For genuinely manual items (e.g. physical rack-lock verification), present them in the portal with a dated confirmation that is stored, not merely displayed.
4. Surface overdue items rather than only completed ones — a checklist that shows only what was done cannot show what lapsed.

**Design caution drawn from this assessment:** the portal must not report an
obligation as met because a job *ran*. `DIWAI-CR-2026-08-10` records a six-minute
outage during which all 24 control-health checks reported healthy while the
dashboard was returning 500 to every authenticated request. Recording *execution*
without recording *outcome* would reproduce exactly that failure at scale.

### POA&M-058 — Signed policy set describes a materially different system — OPEN
**Raised 2026-08-04.** Entry point was a single stale ClamAV reference in
`DIWAI-SI-001`; the sweep it prompted found the problem is set-wide.

| Stale claim | Policies affected | Reality |
|:---|:---|:---|
| **ClamAV** as an operating malware control | **6 of 11** — SI (12 mentions), IR (3), AUP, CM, RA, SCP | Decommissioned 2026-06-12 (FIPS-incompatible); packages removed 2026-08-01. SI-3 is **YARA** + VirusTotal + fapolicyd + SELinux + Suricata |
| **`freshclam`** updates; `clamav-freshclam` service checks | 2 — SI, IR | Service does not exist |
| **"NetGate 2100 pfSense firewall ([LAN-IP-REDACTED])"** | **10 of 11** | **No such appliance.** [LAN-IP-REDACTED] is the **Mac mini**, which is the firewall/router (macOS `pf`). The VM uses `firewalld` |
| **"Suricata IDS on pfSense"** | SCP, IR | Suricata runs on the **VM** |

**Why this is more than a documentation tidy.**

1. **These are signed, approved governing documents** — `/s/ [SYSTEM-OWNER]`, several dated 2026-02-15. They are the authority the SSP cites, and `DIWAI-PAF-001` (signed 2026-08-03) attests to having read them. The operator has formally acknowledged eleven policies describing components that do not exist.
2. **Operational misdirection during an incident.** `DIWAI-IRP-001` carries **8** pfSense and **3** ClamAV references, including a worked example — *"ClamAV detected: Trojan.Generic … automatic quarantine (moved to `/var/quarantine/`)"* — and an instruction to check `systemctl status clamav-freshclam`. Followed literally under pressure these send the responder to an absent service and a non-existent firewall. The 2026-08-03 tabletop already demonstrated the operator reaching for documented-but-wrong mechanisms.
3. **It is the unexamined half of POA&M-017.** That item closed "policy identifiers did not match SSP citations"; the 2026-08-01 re-identification (`DIWAI-CR-2026-08-01` C9) changed `TCC-*-001` → `DIWAI-*-001` and explicitly left **versions and content unchanged**. Identifiers were corrected; the technical content inherited from the earlier CyberInABox/Netgate design was never reviewed. **Closing POA&M-017 created the impression the policy set had been reconciled. It had not.**

**Same defect class as F-2026-08-06** (ClamAV documented decommissioned while still installed) and **F-2026-08-33** (`DIWAI-ATP-001` citing `/srv/hr/training-records/`, present on neither host). This instance is the largest and sits in the governance layer.

**Not a control failure.** The controls are implemented and were scored on verified evidence, not on these documents. The defect is that the governing text does not describe the system it governs.

**REMEDIATION COMPLETE 2026-08-04 — all eleven policies reissued.** The sweep
found substantially more than the ClamAV reference that prompted it.

| Category | Found |
|:---|:---|
| **Wrong products** | ClamAV/freshclam (6 policies); pfSense/NetGate 2100 (10); HP iLO 5 (2) |
| **Wrong platform** | **FreeIPA `ipa` commands (4 policies, 16 in Personnel Security alone)** — `ipa-server` is not installed, so every offboarding command was inoperable; **Kerberos** tickets/keytabs/principals (9 refs in IAP) — `krb5-server` not installed, `krb5kdc` inactive |
| **Wrong hosts** | RS#1 workstations `LabRat`/`Engineering`/`Accounting`; hostname `dc1`; fictional `ws1`/`ws2`; the Mac mini variously described as a workstation, as running **Rocky Linux**, as running **macOS Sequoia**, and as holding the VM's hostname and IP |
| **Non-existent paths** | `/srv/hr/training-records/` (F-2026-08-33, now closed); `/backup/personnel-security/` |
| **Wrong authority** | Password policy cited **`CLAUDE.md`** — an assistant instruction file, not a controlled document |
| **Superseded config** | "Automatic security updates enabled (dnf-automatic)" — the configuration that caused POA&M-011, deliberately set download-only on 2026-08-01 |
| **Wrong baseline** | macOS baseline cited **CIS Apple Benchmark**; the baseline in use is **mSCP `diwai_phase1`** |

**Five claims asserted controls that do not exist. Each was withdrawn, not
restated:**

1. **"Firewall/IDS functions on separate hardware (pfSense appliance)"** (SCP) — no separation exists; the Mac carries firewall, hypervisor and CUI store. **This directly contradicted `DIWAI-RAR-001` R-02**, the accepted HIGH risk whose entire basis is that separation is absent. Two signed documents in opposition.
2. **"Suricata IPS mode: Block and alert"** (SCP) — verified af-packet IDS only; no inline mode, no nfqueue. It detects; it does not block.
3. **"Real-time ClamAV VFS scanning of NAS shares"** (SI) — no host-based scanner inspects NAS content at all.
4. **"Centralized retention: 90 days"** and **"Archival retention: 1 year"** (A&A) — **no ISM policy and no expiry rule exist.** AU-11 requires retention to be defined *and enforced*.
5. **MFA implementation timeline "Q4 2025 / Q1 2026"** (IAP) — elapsed without delivery, with nothing recording that MFA remains undeployed.

**Two capability downgrades recorded rather than papered over:** 389-DS has no
Kerberos principal expiration, so contractor account expiry is now a **manual**
control (Personnel Security v1.2); and automated training reminders do not exist
(ATP v1.1). Both are candidates for **POA&M-059**.

**Corrections made at owner direction during review:**
- **Security clearances and background investigations removed** as the basis of compliance (PS v1.2). CUI is unclassified — 3.9.1 requires *screening*, not a clearance — and the supporting evidence is not currently producible. *"A control claim that cannot be produced on request is a liability rather than an asset."*
- **Laptop prohibition reversed** (PE-MP v1.1). The inherited blanket ban would have forbidden the planned SCAP-hardened daily driver; replaced with conditions, plus a wired-by-default requirement enforced by network design and a **sequencing condition on 3.1.16** — wireless authorisation must be updated *before* that device is deployed.

**Method:** wrong facts corrected; provisions for roles or assets not yet
instantiated (employees, workstations, onboarding) **retained and scoped**, since
this is a reference model for adoption by VSBs of up to ~15 users. Controls
described by **function** rather than product wherever practical, so a future
substitution does not silently invalidate the text.

**Outstanding:** `DIWAI-PAF-001` re-executed 2026-08-04 (v1.1) — the prior
acknowledgment covered superseded text.

**Superseded original remediation note:** review all eleven policies for inherited technical claims — not only ClamAV and pfSense but any component attribution — and reissue with corrected content and incremented versions. **Re-execute `DIWAI-PAF-001`** afterwards, as the current acknowledgment covers superseded text. Prefer describing controls by **function** ("host-based malicious-code protection", "perimeter firewall") rather than product name, which is what let this drift survive a product substitution.

**Scope check performed:** the YubiKey reference in `DIWAI-IAP-001` v1.1 was examined and is **correct** — the change summary recording YubiKey's abandonment after the 2026-05-15 lockout. Not drift; excluded from this item.

### POA&M-053 — Wazuh API uses shipped default credentials — OPEN

**Found 2026-08-03 while diagnosing FIM deployment** (F-2026-08-34), not by a
scan. The Wazuh API authenticated successfully with `wazuh:wazuh` — the
credentials Wazuh ships with — returning a valid JWT. It binds `0.0.0.0:55000`,
all interfaces.

**Severity is bounded by the firewall, and this is stated precisely rather than
alarmingly.** Verified 2026-08-03: firewalld opens only `587/tcp, 1514/tcp, 1515/tcp, 1194/udp`; **55000 is not open** and there is no rich rule for it. A
connection attempt from the Mac host **fails** (`curl` returns 000). The API is
therefore reachable only from the VM itself today, and this is **not remotely
exploitable as configured.**

**Why it still matters.** The API grants full administrative control of the SIEM
— agent configuration, group membership, active-response execution, and read
access to the FIM database (which now indexes the CUI document store). The only
thing standing between a default credential and that capability is one firewall
rule. A future `firewall-cmd --add-port=55000/tcp`, a zone change, or a
misapplied rich rule would expose it instantly, with no second factor and a
password an attacker would guess first. Defence in depth means the credential
should not be the weakest link even when it is behind a boundary.

It also undercuts the control narrative: the SIEM is the system that detects
compromise of everything else. It should not itself be protected by a published
default.

**RESOLVED 2026-08-04** — `DIWAI-CR-2026-08-11`. Verified: `wazuh:wazuh` and
`wazuh-wui:wazuh-wui` both now return **HTTP 401**; API listens on
**`127.0.0.1:55000`**; connection from the Mac **refused**; manager, dashboard and
both agents healthy; 25/25 control-health checks pass.

**The item understated the problem.** It recorded one default credential. There
were **two** — the dashboard authenticates as **`wazuh-wui`**, whose password was
also the shipped default and is held in plaintext in `wazuh.yml`. It was found
only by establishing what consumed the API *before* changing it, which is also
what confirmed the dashboard uses `localhost` and would survive the rebind.

**Residual, not closed by this change:**
1. `wazuh.yml` still stores a plaintext password — inherent to this dashboard version; mitigated by `0600 root:root` permissions, not by secrecy.
2. New credentials live **only on the host they protect** (`/root/.wazuh-api-pw`) — the same defect recorded against the LUKS break-glass note. Move to the escrow under **POA&M-049**.
3. **A third API user, `[USERNAME]` (id 100), was not examined.** Owner to confirm it does not carry a default or weak password.

**Cost:** a ~90-second SIEM outage — `api.yaml` requires `host` as an *array*,
and an invalid API configuration prevents the **whole manager** from starting.
Recorded in `DIWAI-CR-2026-08-11` §4 with the method failure it shares with
`DIWAI-CR-2026-08-10`.

**Superseded remediation note:** rotate to a generated credential (`/var/ossec/api/configuration/ security/` / `wazuh-apid` user management), bind the API to `127.0.0.1` rather
than all interfaces since nothing off-host consumes it, and confirm the dashboard
still authenticates afterwards. Record the new credential in the same escrow that
POA&M-049 establishes.

**Note:** the API was used diagnostically during this session to read agent 004's
effective syscheck configuration and FIM database — that access is what produced
the evidence in F-2026-08-34.

### POA&M-054 — mSCP toolchain remains inside the CUI boundary — OPEN

**Found 2026-08-03** in the FIM catalogue produced by F-2026-08-34 — the file
inventory made the remnant visible.

`Compliance`'s group folder trash contains
`macos_security.d1782066721/mscp_gems/…` — the macOS Security Compliance Project
Ruby toolchain: **2,300 files, 32 MB.** The `.d1782066721` suffix is Nextcloud's
deletion timestamp, **2026-06-21** — the same day the CUI tagging and naming pass
recorded the mSCP toolchain as *purged from the CUI group folder*.

**The purge moved it to trash within the same group folder.** Nextcloud's trash
is inside the folder's storage and inside its access-control boundary; deleting
through the web UI relocates rather than removes. The remediation was recorded as
complete and, 43 days later, the content is still in the CUI boundary.

**Why it matters:**

- **3.4.6 least functionality** — a development toolchain with no business being in a CUI document store.
- **3.4.1 baseline inventory** — 2,300 uninventoried files inside the CUI boundary.
- **3.12.4** — a recorded remediation that did not achieve what the record claims. Same defect class as F-2026-08-06 (ClamAV documented as decommissioned while still installed).
- **Practical distortion:** these files are **92% of the FIM catalogue** for the Nextcloud tree (2,300 of 2,503 monitored files). Integrity monitoring of the CUI store is mostly monitoring discarded Ruby gems, which inflates scan cost and dilutes any review of FIM output.

**RESOLVED 2026-08-03.** `occ groupfolders:trashbin:cleanup 1` executed after
verifying the trash held nothing but the mSCP toolchain and a 44-byte WebDAV
connectivity test — **no compliance document was in it.** Disk usage **32 MB → 0 B**;
`groupfolders:scan 1` clean (22 folders, 95 files, 0 errors; trashbin 0 files).

*Safety check performed before deletion:* the operational mSCP scanner is
`/usr/local/libexec/mSCP_diwai_phase1_compliance.sh`, a self-contained generated
script. The discarded Ruby gems were the **build** toolchain that produced it, not
a runtime dependency, and mSCP is freely re-obtainable from NIST. Deleting it
does not affect the weekly mSCP scan.

**EXPECTED ALERT BURST — this is not an incident.** The FIM database still holds
**2,502** entries under the Nextcloud tree while only **187** files remain on
disk. At the next scheduled scan (within the hour) Wazuh will correctly report
approximately **2,300 file deletions** as rule 553 events. This is the documented
consequence of this remediation, performed 2026-08-03 by the system owner.

*Worth noting for incident response:* a legitimate bulk cleanup and mass
destruction of CUI by an attacker produce the **same FIM signature**. The
difference is entirely contextual — an authorised change record exists for this
one. That is precisely the fault-versus-incident distinction exercised in
`DIWAI-IR-TTX-001` Inject 1, and it argues for recording planned bulk operations
*before* they generate telemetry, not after.

**RETENTION POLICY SET 2026-08-03** — the policy question raised by this item is
now closed as well.

Both retentions were **unset**, meaning `auto`: deleted files and prior versions
were retained indefinitely while disk space allowed. For a CUI store that means
CUI content remained recoverable and in scope with no bound. Now set system-wide:

| Setting                       | Value  | Effect                                                 |
|:------------------------------|:-------|:-------------------------------------------------------|
| `trashbin_retention_obligation` | `30, 30` | Deleted items purged at a hard **30 days**                 |
| `versions_retention_obligation` | `30, 90` | Prior versions kept **at least 30 days**, purged beyond **90** |

*Why 30 days for trash:* long enough to recover an accidental deletion on a
single-operator system where a mistake may not be noticed immediately, short
enough that deleted CUI does not accumulate. The instance this item was raised
for sat for **43 days** — under this policy it would have been purged
automatically at 30.

*Why versions may run to 90:* Nextcloud's automatic versions are a convenience,
**not** the authoritative version record. Version history of record is maintained
as separately named documents (`…_v2.15`, `…_v2.16`) with superseded copies in
`CUI_Archive/`. Bounding automatic versions at 90 days therefore destroys no
compliance record. Current holdings: 2.1 MB / 34 versions in the CUI folder,
6.9 MB in Internal.

**Enforcement verified, not assumed.** A retention value that nothing acts on is
the recurring defect in this system's history, so the mechanism was checked:

- `backgroundjobs_mode` = **cron**, and Nextcloud cron last ran **1 minute** before the change (LaunchAgent `org.diwai.nextcloud-cron`)
- Four enforcement jobs are registered and running: `Files_Trashbin\ExpireTrash` and `Files_Versions\ExpireVersions` (last run 22:27 UTC), `GroupFolders\ExpireGroupTrash` and `GroupFolders\ExpireGroupVersions` (21:50 UTC)
- `occ groupfolders:expire` executed manually: completed, "Removed 0 expired trashbin items" — correct, the trash had just been emptied and no version yet exceeds 90 days

**Applies system-wide** to all group folders and user trash, not only the CUI
folder. That is intentional; FCI and Internal hold regulated content too.

**First observable effect** will be at the 30/90-day boundaries; nothing purges
immediately because all current content is newer than the minimums.

Also present: `_webdav_test.txt.d1781304715`, a leftover connectivity test.

### POA&M-049 — Succession and credential escrow — OPEN

No individual other than the sole operator can administer or recover this system.
LUKS passphrase, Directory Manager credential, break-glass material and
operational knowledge all rest with one person. Recorded as unmitigated in
`DIWAI-RAM-001` §2 and as R-12 in the risk register. **D-1's break-glass escrow
(POA&M-026) is a prerequisite but not a solution** — escrowing the disk key does
not transfer the ability to operate the system. Needs: a named successor or
custodian, sealed credential escrow, and a documented recovery path a competent
third party could follow from the runbooks.

### POA&M-050 — Backup copies are neither independent nor both current — OPEN

**Restated 2026-08-03 on evidence.** The original wording ("backups are written
to the NAS") was wrong by omission — it ignored Time Machine. Verified position:

| Copy                                     | Destination                                                   | Scope                                                                                                                                                                                                           | Currency                                                |
|:-----------------------------------------|:--------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------|
| **Time Machine**                             | External disk `SecureMac` (`/dev/disk6`, 500 GB, direct-attached) | **Full Mac, VM included** — `com.utmapp.UTM` confirmed *not* excluded (31 GB)                                                                                                                                           | **Current** — last backup 2026-08-03 11:09                  |
| **NAS** `Backup/SecureMac/archive/`            | Synology [LAN-IP-REDACTED]                                          | **Complete VM archive** from Time Machine snapshot `2026-07-16-085956`, archived 2026-08-01: `config.plist` + `.qcow2` (21.7 GB) + `efi_vars.fd`, with `MANIFEST.txt` recording source path, snapshot date and **source SHA-256** | **2026-07-16 snapshot** — 18 days old at time of assessment |
| **NAS** `Backup/SecureMac/diwai-services.utm/` | Synology [LAN-IP-REDACTED]                                          | **INCOMPLETE —** `Data/` **holds only** `efi_vars.fd`**; the** `.qcow2` **disk image is absent**                                                                                                                                      | Abandoned/partial, 2026-06-01                           |
| **NAS** `Backup/SecureMac/wazuh-alerts/`       | Synology [LAN-IP-REDACTED]                                          | Encrypted audit archives (`.tar.gz.enc`)                                                                                                                                                                          | Current                                                 |

**Correction, 2026-08-03.** An earlier restatement of this item described the NAS
VM copy as "stale, 15 GB against a 31 GB live VM." **That was wrong** — it
inspected `Backup/SecureMac/diwai-services.utm/` and missed the `archive/` tree
entirely. The `archive/` copy is complete, dated, manifest-documented and
checksummed. The NAS position is materially better than first reported, and the
correction is recorded rather than quietly amended.

**What is genuinely defective** is `Backup/SecureMac/diwai-services.utm/` — a
partial copy whose `Data/` directory contains the EFI variable store but **not the
disk image**. It is an abandoned or interrupted copy that *looks* like a VM backup
in a directory listing. It should be removed or completed; leaving it invites
exactly the misreading recorded above.

**INTEGRITY VERIFIED 2026-08-03.** The archived disk image was read in full from
the NAS and hashed:

```
computed  0d8539e1a5e66d3675f386c166883aadc8d5d20261324b36dfb0a42fd209445c
manifest  0d8539e1a5e66d3675f386c166883aadc8d5d20261324b36dfb0a42fd209445c
```

**Exact match.** The 21.7 GB image on the NAS is byte-identical to the source at
snapshot time — the SMB transfer introduced no corruption, and the copy is
intact. This is the **first end-to-end integrity verification** of a backup on
this system, and it is what the `MANIFEST.txt` checksum was written for.

**What this does not establish.** Integrity is not restorability. A byte-perfect
image still has to boot, and its LUKS volume still has to open with a passphrase
that is currently held in one place (POA&M-026, POA&M-049). **POA&M-052 remains
open and is not advanced to closure by this result** — it is advanced by one
step: the copy is now known to be intact rather than assumed to be.

**Encryption at rest is already satisfied.** Per `MANIFEST.txt`: *"The qcow2
contains a LUKS-encrypted filesystem; it is encrypted at rest."* The audit
archives are separately OpenSSL-encrypted (`.enc`). **Every VM and audit payload
on the NAS is therefore already encrypted before it is copied anywhere** — which
means off-site removable media carries no additional disclosure risk beyond
physical custody, and the media's own encryption need not be the control of
record for 3.13.11.

**Two distinct defects, previously conflated:**

**(a) Currency — the more urgent.** The NAS is believed to hold a VM backup and
does not hold a usable one. Nothing detected the drift: the audit-archive stream
to the same NAS path *is* current and healthy, so the folder looks alive. Same
defect class as POA&M-031 — a backup that appears to be working.

**(b) Correlated location.** The Time Machine disk is direct-attached and the NAS
sits in the same rack (R-14; shared rack per POA&M-032). A fire, theft, flood or
rack-level power event takes the system and both copies together. Direct
attachment also means the TM disk shares the Mac's logical failure modes —
ransomware or an erroneous delete can reach it.

**A third backup is not the remediation.** The requirement is not a copy count;
it is that a single event must not destroy every copy.

### Scope defect found 2026-08-03 — the NAS backup is the VM only

**Raised by the system owner on inspection, before the off-site copy was made.**`Backup/SecureMac/` contains `archive/` (VM), `diwai-services.utm/` (broken VM)
and `wazuh-alerts/` (audit archives). **It is a VM backup, not a system backup.**
Copying it to removable media as-is would have produced an off-site copy that
cannot rebuild this system.

**The system is split across two hosts, and Nextcloud is split across both:**

| Component                                                      | Location                 | In the NAS archive?    |
|:---------------------------------------------------------------|:-------------------------|:-----------------------|
| MariaDB — `nextcloud` **and** `roundcubemail` **databases**                | VM                       | **Yes** (inside the qcow2) |
| 389-DS directory, Wazuh, mail, Suricata                        | VM                       | **Yes**                    |
| **Nextcloud application + CUI file store** (1.3 GB; `data/` 239 MB)  | **Mac** `/opt/local/nextcloud` | **NO**                     |
| `~/diwai` — compliance working set (4.2 MB)                      | **Mac**                      | **NO**                     |
| `/usr/local/sbin` control scripts, LaunchDaemons/Agents (160 KB) | **Mac**                      | **NO**                     |

**The consequence is specific and serious. Nextcloud cannot be restored from
either host alone** — the database lives in the VM, the files live on the Mac.
An off-site copy holding only the VM would carry the CUI store's *database* and
none of its *documents*. The canonical CUI repository would be unrecoverable
after a rack-level loss, which is precisely the event this item exists to cover.

**Time Machine does cover the Mac side** — verified 2026-08-03, all critical
paths report `[Included]`: `/opt/local/nextcloud`, `/opt/homebrew`,
`/usr/local/sbin`, `~/diwai`, `/Library/LaunchDaemons`, `/private/etc`. **But
Time Machine is the only copy of the Mac side**, on one directly-attached disk in
the rack. The NAS VM archive was itself produced *from* a Time Machine snapshot,
so TM is the single origin for everything.

**Cost of fixing the scope is small:** the missing Mac-side critical set is
**~1.3 GB** against the VM archive's 35 GB. Total ≈ **36.3 GB** — still within a
64 GB volume. Excluding `~/.ollama` (16 GB of re-downloadable model weights) is
appropriate; those are not system state.

**Restore-consistency caveat.** The VM snapshot and any Mac-side file snapshot
are taken at different moments, so the Nextcloud database and its file store can
drift apart. A restore assembled from mismatched halves yields a Nextcloud whose
database references files that are absent, or vice versa. A correct archive
procedure puts Nextcloud into maintenance mode, dumps the database, and captures
the file tree **at the same point**, recording both in one manifest. **This is
not currently done** and must be part of the remediation, not discovered during
the restore test (POA&M-052).

---

### Remediation approach — owner-proposed 2026-08-03

**Primary (interim, stands alone):** attach a USB volume to the Synology and copy
the existing NAS backups to it, then **rotate that volume off-site**.

Assessed as sound, subject to four conditions:

1. **Fix the scope first.** The NAS holds the VM only. Off-site media must also carry the Mac-side set — `/opt/local/nextcloud` (1.3 GB), `~/diwai`, `/usr/local/sbin`, LaunchDaemons/Agents — or Nextcloud cannot be rebuilt. See the scope defect above. Copying what is on the NAS today would ship an incomplete backup off-site and create false confidence, which is worse than the current known gap.
2. **Copy the** `archive/` **tree, not** `Backup/SecureMac/diwai-services.utm/`**.** The latter has no disk image. Copying it would produce an off-site backup that cannot restore anything — the failure mode this item exists to prevent.
3. **The volume must physically leave the premises.** A USB drive left attached to the Synology is a third copy in the same rack and satisfies nothing. Rotation, not attachment, is the control.
4. **Verify after copy against** `MANIFEST.txt`**'s SHA-256** rather than trusting the copy. The precedent for not doing so is POA&M-031.
5. **Refresh cadence.** Copying once yields an off-site copy that ages. The archive snapshot must be regenerated on a defined interval, or the off-site copy silently becomes a relic.

**Dependency to resolve:** configuring Synology USB Copy or Hyper Backup requires
a DSM session. **As of 2026-08-03 this is no longer blocking** — the NAS presents
a valid, fully trusted `*.[DOMAIN.ORG]` certificate over HTTPS on :5001 (POA&M-033,
certificate half resolved). DSM is reachable securely at
`https://nas.[DOMAIN.ORG]:5001`; the residual POA&M-033 items (plain HTTP still
answering on :5000, no HSTS) do not prevent this work.

### POA&M-033 — DSM transport security — PARTIALLY RESOLVED 2026-08-03

**Certificate: RESOLVED and verified.** The NAS now presents the current Let's
Encrypt certificate — `CN=[DOMAIN.ORG]`, SAN `*.[DOMAIN.ORG], [DOMAIN.ORG]`, issuer YE2,
valid to 2026-09-09 — the same certificate distributed by the renewal deploy hook.
Verified from the Mac host:

```
https://nas.[DOMAIN.ORG]:5001  ->  HTTP 200, ssl_verify=0 (fully trusted, no flags)
openssl -verify_hostname nas.[DOMAIN.ORG]  ->  Verification: OK, return code 0
```

The prior findings — default `*.[DOMAIN.ORG]` certificate and an expired
`[DOMAIN.ORG]` certificate — no longer apply.

**A trust warning seen in the browser on 2026-08-03 was not a system fault.** The
error read *"'[DOMAIN.ORG]' certificate name does not match input"* — a **name**
mismatch, not a chain failure; the ISRG Root X2 → Root YE → YE2 chain validated
normally. Cause: the NAS was being reached **by IP address**
(`https://[LAN-IP-REDACTED]:5001`). A public CA cannot issue a certificate matching a
private IP, and `*.[DOMAIN.ORG]` cannot cover `[LAN-IP-REDACTED]`. Reproduced exactly:

```
by hostname nas.[DOMAIN.ORG]  ->  Verification: OK (0)
by IP [LAN-IP-REDACTED]          ->  verify error 62: hostname mismatch
```

**Access DSM as** `https://nas.[DOMAIN.ORG]:5001`**.** `/etc/hosts` on the Mac already
resolves that name to [LAN-IP-REDACTED].

**RESOLVED 2026-08-04 — verified from the wire:**

```
https://nas.[DOMAIN.ORG]              HTTP/2 200, ssl_verify_result=0 (trusted)
strict-transport-security: max-age=15768000; includeSubdomains; preload
http://nas.[DOMAIN.ORG]:5000          404 — no longer serves the DSM login
```

- **Certificate:** current Let's Encrypt `*.[DOMAIN.ORG]`, validates by hostname.
- **Plaintext DSM login eliminated.** Setting a **customized domain** (`nas.[DOMAIN.ORG]`) moved DSM to the standard HTTPS port; `:5000` now returns a 404 stub rather than a login page, so administrative credentials can no longer traverse the network in the clear.
- **HSTS enabled**, 6-month max-age.

**Two consequences recorded, neither blocking:**

1. **Certificate renewal is now load-bearing.** HSTS removes the HTTP fallback: if the certbot deploy hook fails to push a renewed certificate to the NAS, DSM becomes **unreachable** rather than degraded, with no click-through warning. The existing `diwai-control-health` certificate-expiry check covers expiry on the VM but does **not** confirm the NAS received the renewal. Extending it to do so is folded into **POA&M-059**.
2. **Port 80 still answers 200** with no redirect and no identifiable content — probably Web Station's default page. Not a credential exposure (the DSM login is not there), but a plaintext listener with no apparent purpose. Recommend disabling it if nothing requires it.

**Superseded — the gap as it stood before 2026-08-04:**

1. **Plain HTTP on :5000 answers 200 with no redirect to HTTPS.** DSM administrative credentials can still traverse the network in cleartext if that port is used. Fix in DSM: *Control Panel → Login Portal → Network* → **Automatically redirect HTTP to HTTPS**, or disable the HTTP port entirely.
2. **No HSTS header** on :5001. Without it a browser that first tries HTTP is not prevented from doing so again. Enable HSTS in the same DSM panel.
3. **QuickConnect** — presence of an external relay still to be confirmed and, if enabled, assessed as a boundary egress path.

Item **1 is the one that matters for 3.13.11** — a working certificate on 5001
does not protect a session that was established on 5000.

**Also note:** the NAS is shared infrastructure with CyberInABox (POA&M-032).
Off-site media sourced from it must contain only this system's data.

**An off-site procedure already exists and was not being used.** Found on the
historical volume 2026-08-03: `IronKey_D500S_Backup_Procedure_2025-11-04.md` —
a complete off-site backup procedure covering device handling, transfer and
verification. Written for `dc1.[DOMAIN.ORG]` (RS1), so it requires adaptation
to this system's scope, but the method and rationale are already documented and
need not be authored from scratch.

**It also resolves the media-encryption question.** The drives held are **Kingston
IronKey D500S — FIPS 140-3 Level 3 validated**, hardware XTS-AES-256. Earlier
analysis in this item flagged that the Nextcloud tree travels as **plaintext CUI**
(server-side encryption is off) and therefore that the media's own encryption
would have to be the control of record rather than defence in depth. **That
condition is satisfied by the hardware already in hand** — no procurement, and no
need to pre-encrypt the archive, though doing so remains good practice.

**Preferred (enhancement, not a gate):** SuperDuper once its macOS Tahoe issues
are resolved. Two cautions recorded so the plan does not rest on an assumption:

- Since macOS 11 and the Signed System Volume, **a genuinely bootable duplicate is no longer reliably achievable**; the major vendors default to data-only copies. "Once Tahoe support returns" may be waiting for something that does not return in its previous form — worth confirming against the vendor's current statement rather than assumed.
- A clone is **point-in-time, not versioned**. Time Machine provides version history; a clone does not. Against corruption or ransomware, versions are the property that matters. SuperDuper therefore **complements** Time Machine rather than replacing it.
- **It must not gate the interim.** Making off-site custody contingent on a third-party compatibility fix leaves this item open with no date under the owner's control — the mechanism by which POA&M items go stale.

### Option considered — Synology Active Backup for Business (2026-08-04)

Raised by the system owner as a candidate addition to the software stack. The
package is present on the NAS (the `ActiveBackupforBusiness` share exists);
whether backup tasks are configured was not determined, as that requires a DSM
session. Recorded so the reasoning survives rather than being re-derived.

**Where it fits**

| Target | Verdict |
|:---|:---|
| **Rocky VM** | **Yes** — the Linux agent supports RHEL/Rocky 9. Block-level incremental backup, and **Synology bare-metal recovery media**: a designed, documented restore path rather than an improvised one. Directly relevant to POA&M-052 |
| **Mac host** | **No — ABB has Windows and Linux agents only; there is no macOS agent.** This is decisive, because the Mac carries the plaintext CUI store, the perimeter firewall and the hypervisor, and is precisely the gap this item was raised for |
| **Agentless VM backup** | **No** — supports VMware vSphere and Hyper-V. This VM is UTM/QEMU on Apple Silicon and is not reachable that way; it would have to be treated as a physical Linux host via the agent |
| **Mac file-level** | **Partial** — an ABB *File Server* task can pull `/opt/local/nextcloud` and `~/diwai` over rsync/SMB. That covers the content gap but yields no bootable Mac |

**What it does not solve**

- **Off-site.** ABB writes to the NAS — same rack, same fate. The independence half of this item is untouched.
- **Nextcloud consistency.** An ABB VM backup plus an rsync of the Mac remain two snapshots taken at different moments; the database/file drift problem persists.

**Cost of adopting it**

A new component **inside the CUI boundary**: an SBOM entry, a patching
obligation, a network-facing service with agents, and — the governing concern of
this assessment — **another control capable of failing silently.** Two backup
mechanisms already exist (Time Machine and `archive-snapshot.sh`) and **neither
has been proven to restore.** Adding a third before verifying the first two
multiplies unverified controls rather than reducing risk.

**DISPOSITION: NOT ADOPTED — decided 2026-08-04 on evidence.** The restore test
was performed (`DIWAI-EV-CP-2026-08-04`): the existing archive restored **end to
end in ≈8 minutes**, booting to a login prompt with the directory and Nextcloud
database verified intact. Under the decision rule recorded here before the test,
a clean restore means **ABB is redundant complexity and should not be added** —
the existing mechanism demonstrably works, and a third backup system would add an
SBOM entry, a patch obligation and another control capable of silent failure
without addressing either real gap (off-site custody, and the Mac host).

ABB **remains documented as a reference-model option** for adopters — see the
manuscript §11.5, where the platform constraint is recorded: it suits an RS#1-class
deployment or a VSB with Windows workstations, and cannot serve a macOS host.

**Superseded pre-test disposition:** DEFERRED pending POA&M-052. The restore test is the deciding
evidence.

- If the existing archive restores cleanly, ABB is redundant complexity and should not be added.
- If it does not — and there is precedent, since `DIWAI-INC-002` records a bare-metal recovery that completed but returned an **incomplete host** for reasons never determined — then ABB's engineered recovery path becomes a strong candidate for the VM tier.

**Reference-model note, independent of the decision here.** ABB is free,
Synology-native, and well matched to the audience this system models: a VSB of up
to ~15 users with Windows workstations is ABB's design centre, and such adopters
face none of the macOS-agent limitation that rules it out for the Mac host. It is
worth documenting as an option in the model whether or not it is adopted in this
deployment.

---

**Pair with POA&M-052** — a restore has still never been tested. An untested copy,
off-site or not, is relied upon rather than known to work.

**Not verifiable from this host:** whether the Time Machine disk is physically
racked or stored apart. Assessment assumes racked, per TS-7/R-14 ("single
location, no off-site copy"). If it is already kept elsewhere, defect (b) is
substantially reduced and this item should be re-rated — **owner to confirm**.

### POA&M-076 — Inactivity disable defined but not enforced — OPEN

> **2026-09-13 — directory half enforced (`DIWAI-CR-2026-09-08`).** 389-DS Account Policy Plugin enabled in two phases. Recording came first, because a creation-date fallback would have refused `uid=[USERNAME]` (created 2026-04-09) immediately. Then `accountInactivityLimit` 90 days. A disposable entry backdated 100 days was **refused with the correct password** (*"Account inactivity limit exceeded"*), while a recent-login control and the real accounts bound normally. **Still open:** (1) Mac and VM local accounts, with a `sysadmin` break-glass exception; (2) never-logged-in directory entries, by adding `altStateAttrName: createTimestamp` once all existing accounts carry `lastLoginTime`. **Point withheld until both are done.**

Found 2026-09-13 by applying the evidence-strict scoring basis on the day it was adopted. SSP Appendix E.4 (added v2.15) states **"Accounts disabled after inactivity of 90 days"**, satisfying objective 3.5.6[a], and 3.5.6 carried no deduction. **Objective [b] was tested and fails:** the 389-DS Account Policy plugin is `nsslapd-pluginEnabled: off`; VM local accounts have `INACTIVE=-1` and no shadow inactivity; the Mac's global `pwpolicy` has no last-authentication rule. **The 3.5.6 point (−1) is withheld; SPRS 101 → 100/110.**

**Design constraint.** A system-wide inactivity rule would disable the rarely used `sysadmin` break-glass account — the one account that must survive long idleness. Its failure mode was POA&M-073. **Path:** (1) 389-DS — enable the Account Policy plugin with `accountInactivityLimit` 90 days and `alwaysRecordLogin`, proven by refusing a disposable entry with a backdated last login; (2) Mac and VM local accounts — a mechanism with an owner-approved break-glass exception and a compensating check, e.g. a health check alerting on break-glass idleness rather than disabling it; (3) point restored only when every identifier class is enforced or formally excepted with evidence.

### POA&M-075 — YARA detection has never raised an alert — CLOSED 2026-09-13

> **CLOSURE (`DIWAI-CR-2026-09-06` §3a).** Proven end to end on both hosts the same afternoon. EICAR in a FIM-monitored path → rule 554 → YARA `SUSP_Just_EICAR` → **alert 100200**. VM `/var/www`: 14:04:38 → 14:04:40. Mac (a folder in no groupfolder): 14:05:33 → 14:26:11, on the hourly scheduled scan. These were the first YARA alerts the system had ever raised; the Mac result also proves `active-responses.log` forwarding. The SSP 3.14.2 narrative now states the verified path and its history. The 3.14.2 determination (MET) is unchanged and is now evidenced.

Found 2026-09-13 (`DIWAI-CR-2026-09-06`). The manager's `ossec.conf` carried no `<ruleset>` block in any known copy, so `etc/rules` and `etc/decoders` never loaded. The YARA rules could not fire. The VM's YARA active-response wrote ~9,600 results into a void, and the Mac agent has never raised an alert from a watched file, so the 2026-08-06 macOS YARA deployment has never alerted. The block could not be restored while the invalid `yara_decoder.xml` existed. That decoder is retired, and the rules are rewritten on the stock `json` decoder and load.

**Remaining:** (1) exercise a YARA match end to end on each host (e.g. EICAR in a FIM-monitored path) and confirm alert 100200; (2) correct the SSP's 3.14.2 narrative, which describes YARA as an operating detection layer; (3) decide whether 3.14.2 as scored is affected. **No SPRS change is claimed by opening this item**, and the 3.14.2 determination is not altered here.

### POA&M-051 — Wazuh manager version-locked — CLOSED 2026-09-13

> **CLOSURE (`DIWAI-CR-2026-09-04`).** Diagnosed offline without installing: Wazuh 4.14.7 bundles `cryptography` 48.0.1 (OpenSSL 3.5), whose CPU probe executes `cntb`, an SVE instruction. The UTM/QEMU guest advertises SVE2 but the M4 has no SVE, so the probe crashes. Fixed with `OPENSSL_armcap=0x87d` in the manager's systemd drop-in; pin removed; upgraded to **4.14.7**. Verified: 11/11 daemons, API 401, agents 2/2, alerts flowing; the live `wazuh-apid` has the crashing module mapped, and without the setting the import still fails, so the setting is load-bearing. `diwai-control-health` check 12 guards it. **Restart Wazuh only with `systemctl`.** 3.14.1 −5 → 0.

`wazuh-manager` is pinned at **4.14.6** via `dnf versionlock` because **4.14.7's**
`wazuh-apid` **aborts with SIGILL on this platform** (`DIWAI-CR-2026-08-01` C1–C2).
The pin restored a failed SIEM and was correct at the time, but while it holds
the SIEM receives no security updates — the component that detects compromise is
itself unpatched. Needs a tested upgrade path: verify whether a later release
fixes the aarch64 SIGILL, stage it, and remove the lock. **Do not remove the lock
without testing** — that is what broke the SIEM originally.

### POA&M-052 — Restoration partially demonstrated, current backups untested — OPEN

**RESTATED 2026-08-03 on evidence.** The original wording, "restoration never
tested," was **wrong**. A bare-metal Time Machine recovery **was** performed and
documented: `DIWAI-INC-002`**, 2026-04-14** — macOS Recovery Mode, rollback to
the 2026-04-12 snapshot, after a `pam_yubico`/`pam_u2f` misconfiguration set
`required` against a VM that does not autostart locked the host out completely.

The record was not found in the compliance set or either git repository because
**it lives on the "CyberHygiene Project" historical volume**, and both repos
post-date it (`securemac-site` 2026-05-30, `diwai-repo` 2026-06-05). Copied into
`Compliance/Incident_Response/` 2026-08-03 along with `DIWAI-INC-001`.

**A second correction:** SSP and `DIWAI-RAR-001` §4 both attribute the April
recovery to the *sysadmin break-glass* account. `DIWAI-INC-002` §9 records that
the break-glass account **did not exist before this incident** and was created as
a lesson from it. The break-glass attribution belongs to the **2026-05-15** PIV
lockout, not 2026-04-14. **Both documents need correcting.**

**Why this item nonetheless stays open — the restore was lossy.** §4 of the
incident report lists what did not come back:
`/usr/local/sbin/usb-guard`, `usb-guard-monitor`,
`/Library/LaunchDaemons/org.diwai.usb-guard.plist`, `/var/lib/usb-guard/mode`,
`/var/log/usb-guard.log`, and the FIDO2-SK credential. The report's own note
suspected Time Machine had **excluded** those directories, and left it unresolved
as **OI-1**.

**OI-1 and OI-4 answered 2026-08-03:** `tmutil isexcluded` reports
`/usr/local/sbin` **[Included]** and `/Library/LaunchDaemons` **[Included]** as
configured today, together with `/opt/local/nextcloud`, `/opt/homebrew`,
`~/diwai` and `/private/etc`. That closes the standing question and **deepens the
anomaly**: the 2026-04-12 snapshot post-dated the 2026-04-10 deployment of those
files, so if the paths were covered then, the content should have been in the
snapshot. Either the exclusion set has changed since, or the restore did not
replay them. **Unexplained, and it concerns a restore the system depends on.**

**RESTORATION TEST PERFORMED AND PASSED — 2026-08-04.** Evidence:
`DIWAI-EV-CP-2026-08-04`.

| Stage | Elapsed |
|:---|---:|
| NAS → Mac copy (35 GB) | 5 min 51 s |
| Boot → LUKS prompt | **32 s** |
| LUKS unlock → login | **66 s** |
| **End-to-end recovery** | **≈ 8 minutes** |

**Integrity verified inside the restored guest, not merely at boot:** 0 filesystem
errors; **21 directory entries — identical to production**; **412 tables** in the
`nextcloud` schema; access-log date 2026-07-16 confirming the recovery point.
A VM that boots but whose directory or database is unusable would still be a
failed restore, which is why these were checked.

**Recovery time is ≈8 minutes, not the 1–3 hours estimated** in
`DIWAI-IR-TTX-001`. The estimate assumed reassembly; the archive is a complete
bundle.

**Method note:** the copy was isolated by construction, not by care — the bridged
adapter was **removed** from its config before UTM opened it, and its UUID
regenerated, because both bundles otherwise shared UUID `67BBD536-…` and the guest
holds a static [LAN-IP-REDACTED]. Booting it as-is would have collided with the live
directory, mail, database and SIEM.

### Correction — which recovery path the test actually validated (2026-08-04)

**Raised by the system owner: in a bare-metal recovery the VM would return via
Time Machine, not from the NAS archive.** The test restored from the NAS archive,
which is the *secondary* path. The distinction is material and the result must be
read accordingly.

**What the provenance chain shows.** `archive-snapshot.sh` extracts the VM **out
of a mounted Time Machine snapshot**; `MANIFEST.txt` records the source as
`/private/tmp/tmsnap-2026-07-16-085956/…/Macintosh HD - Data/Users/[USERNAME]/Library/Containers/com.utmapp.UTM/…`.
The bytes tested today therefore **came out of a Time Machine backup**.

| | Status |
|:---|:---|
| The VM image **as held in the 2026-07-16 Time Machine backup** boots, unlocks, and has an intact directory and database | **PROVEN** |
| The **Time Machine restore mechanism** delivering that image onto a rebuilt host | **UNTESTED** |

**Content is validated; delivery is not.**

**Why the untested half is the one that matters most.** `DIWAI-INC-002` records a
bare-metal Time Machine recovery that completed but returned an **incomplete
host** — `/usr/local/sbin` scripts, a LaunchDaemon plist and credentials that
should have been present did not come back, and the cause was never determined.
**That failure was in delivery, not in content.** The half this test did not
cover is precisely the half that has already failed once on this system.

**Consequence for the RTO.** The 8-minute figure describes restoring the VM from
the NAS archive — a path available only while the Mac host still functions. In
the bare-metal case the VM arrives at the end of a 90-minute-to-2-hour host
restore, and its recovery time is subsumed by that.

### Host bare-metal recovery path — documented by the system owner, 2026-08-04

**The restoration test covered the VM only.** Recovery of the Mac host follows a
different and considerably longer path, recorded here from the owner's
operational knowledge:

| # | Step | Estimated |
|:--|:---|:---|
| 1 | Wiped/replacement Mac mini booted to Recovery; **current macOS downloaded from Apple** | **90 min – 2 h combined**, bandwidth-dependent (currently **100 Mb down**) |
| 2 | **Restore from Time Machine** | *(as above)* |
| 3 | Host boots | minutes |
| 4 | VM boots | **98 s measured** |
| 5 | **System is "up" but UNVERIFIED** | — |
| 6 | Verification of services, controls and data | not yet estimated |

**System RTO is therefore of the order of 2–3 hours at best, not 1 hour.** The
1-hour objective recorded in `DIWAI-RA-001` §4.3 is a **component** figure for the
service VM and must not be read as a system-recovery objective.

**Step 5 is the important one.** "Up" is not "recovered." This assessment has
repeatedly found services running but not working; a restored host reporting no
errors is a hypothesis until its controls are exercised. Verification time belongs
in the RTO and is currently unmeasured.

**Three dependencies in this path that are not yet resolved:**

1. **The Mac is the router.** WAN (`en0`) terminates on this host and carries the /29 — `.145`, `.146`, `.147`, `.149`. A wiped Mac needs internet to download macOS, **but the Mac is what provides internet**. Recovery therefore requires connecting directly to the ISP demarcation, bypassing the site's own routing. This should be written into the runbook; discovering it during an outage costs time that the estimate does not include.
2. **The Time Machine destination is a locally attached disk** (`/Volumes/SecureMac`) **in the same rack**. In the rack-loss scenarios this path exists for (R-14), the restore source is lost with the host — POA&M-050.
3. **Apple Silicon DFU recovery — capability CONFIRMED and previously exercised.** Where the internal SSD retains recoveryOS, reinstall from Recovery works. Where the machine must be **revived or restored via DFU**, Apple Configurator on a second Mac is required. **A second Mac exists** — an **M2 Mac Studio Ultra**, out of the CUI boundary — and the owner confirms it **has been used for exactly this purpose during the 2026 lockout incidents**. This is therefore not a theoretical capability but a demonstrated one.

   **However, it is now a recorded recovery dependency, and three things follow:**

   a. **The Mac Studio is out of scope but recovery-critical.** It processes no CUI and correctly sits outside the boundary; DFU restore writes macOS to the target rather than handling CUI. But a system whose bare-metal recovery depends on specific out-of-scope equipment must **name that equipment in the recovery runbook**. It presently appears in no compliance document.

   b. **Probable co-location.** If the Studio is in the same premises, the rack-loss scenarios (R-14) that make bare-metal recovery necessary may also remove the tool required to perform it. Worth confirming and recording.

   c. **Succession (POA&M-049).** A successor performing recovery would need to know the Studio exists, that it is required for the DFU path, where it is, and how it is used. That knowledge is currently held only by the owner — the same single-point condition this item family exists to address.

   **CORRECTED 2026-08-04 — the DFU dependency was over-weighted in this item.**
   Per the system owner: **DFU is rare, and applies only to the *same* Apple-authorised
   hardware.** It is **not** the route for bringing up replacement hardware. A new
   or replacement Mac **boots its installed macOS** and permits **Migration
   Assistant or a Time Machine restore** at Setup Assistant — no second Mac, no
   DFU. Three scenarios, now documented in **RB-05**:

   | Scenario | Path | Second Mac? |
   |:---|:---|:---|
   | **Replacement / new Mac** *(most likely)* | Boot installed macOS → Migration Assistant / TM restore | **No** |
   | Same Mac, disk erased, recoveryOS intact | Recovery → reinstall macOS (download) → TM restore | **No** |
   | Same Mac, firmware-level failure *(rare)* | **DFU revive via Apple Configurator** | **Yes — M2 Mac Studio Ultra** |

   **Assessment:** there was never a hard blocker; the scenario requiring a second
   Mac is the uncommon one, and even that capability exists and has been exercised.
   **Recorded in RB-05 on 2026-08-04**, together with the two site dependencies
   that cost time if met unprepared — the Mac being the router, and the Time
   Machine disk being racked with the host.

**This item stays OPEN.** The test discharges the VM tier only:

1. **Half a recovery.** The Nextcloud database is in this VM; its **files are on the Mac** and are **not in this archive** (POA&M-050). The VM alone restores a database referencing absent documents.
2. **The Mac host has no tested restore.** Time Machine remains unproven for the host carrying the firewall, hypervisor and plaintext CUI store.
3. **Service startup untested** — the guest ran without a network adapter by design.
4. **Recovery point was 19 days** at test date. Recovery *time* is now known; recovery *point* is a separate figure and depends on archive cadence.

**Decision gated on this item:** whether to add **Synology Active Backup for
Business** to the stack is deferred pending this restore test — see the option
analysis recorded under **POA&M-050**. A clean restore argues against adding a
third backup mechanism; a failed one argues for ABB's engineered recovery path on
the VM tier.

**Residual gap, precisely scoped:** the operator has demonstrated bare-metal
macOS recovery on this hardware and understands the Tahoe two-step. What remains
untested is (a) whether **these current backups** restore — VM boot, LUKS
unlock, Nextcloud database/file reassembly — and (b) why the one documented
restore returned an incomplete host.

**Partial progress 2026-08-03:** the NAS-archived VM image was verified
byte-identical to its manifest SHA-256 (POA&M-050). That establishes the copy is
**intact**; it does not establish that it **restores**. The image must still boot
and its LUKS volume must still open. Integrity verification is a prerequisite for
a restore test, not a substitute for one. This is the cheapest high-value item on the register:
it requires no purchase, no architecture change, and no third party. Its value is
established by precedent — the archive pipeline ran daily, exited 0, and
delivered nothing for months (POA&M-031). A backup that has never been restored
is in the same epistemic position that pipeline was in. Needs: a restore to
scratch storage, a documented result, and a repeat cadence.

### POA&M-008 — Security awareness training — PROGRESS 2026-08-03

**Weight −11 (3.2.1 = −5, 3.2.2 = −5, 3.2.3 = −1). Largest single item on the
register after MFA. Evidence now substantially complete; closure blocked only on
two signatures.**

| Req         | Objective                            | Evidence                                                                                                                                                                                                        | State                                       |
|:------------|:-------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|
| **3.2.1**       | Awareness training delivered         | **IF141.16 certificate** — Certificate of Completion, [SYSTEM-OWNER], 2026-08-03, signed by Acting Senior Leader, Security Training Operating Component, DCSA                                                    | **Complete**                                    |
| 3.2.1[c\]\[d] | Policies made known and acknowledged | `DIWAI-PAF-001` **— SIGNED 2026-08-03**, all eleven policies at verified current versions                                                                                                                             | **Complete**                                    |
| **3.2.2[a\]\[b]** | Duties defined and assigned          | `DIWAI-RAM-001` — four roles defined with duties; single-operator condition, four partial offsets and unmitigated succession risk recorded                                                                        | Drafted — **signature pending**                 |
| **3.2.2[c]**    | Personnel adequately trained         | `DIWAI-CRC-001` — no certifications held (stated); competency evidenced by 71 changes, 16 evidence records, 20 runbooks, 11 policies, 110-requirement assessment, and six self-reported findings against own work | Drafted — **signature pending**                 |
| **3.2.3**       | Insider threat awareness             | **INT101.16 completed 2026-08-03.** CDSE Security Awareness Hub issues **no certificate without a STEPP account**; recorded in `DIWAI-TRR-001` T-002 with end-of-course artefact plus custodian attestation               | Complete on attestation — **signature pending** |

**Register of record:** `DIWAI-TRR-001`, with all artefacts in
`Compliance/Evidence/Training/`.

**Blocking closure:** signatures on `DIWAI-TRR-001` §4 (attestation covering the
INT101 completion) and on `DIWAI-RAM-001` §5 / `DIWAI-CRC-001` §5. Until signed,
3.2.2 and the 3.2.3 record are drafted rather than executed, and **no SPRS
recovery may be claimed**. On signature the full **+11** is recoverable, moving
the score **56 → 67/110**.

**Evidentiary weakness, stated deliberately:** the INT101.16 artefact is an
end-of-course screen, not a scored pass. It corroborates; it does not prove. The
weight rests on the custodian attestation — the ordinary mechanism for
self-delivered training in a single-person organization. If a prime contractor or
assessor requires a certificate specifically, retaking INT101.16 through STEPP
(~1 hour) yields a transcript-backed one. Not a prerequisite; the training
obligation is met.

**Related defect opened:** **F-2026-08-33** — `DIWAI-ATP-001` §3.3 mandates
training records be held in `/srv/hr/training-records/` (encrypted). That path
exists on neither host (verified 2026-08-03); it is template text describing an
HR function this organization does not have. Records are held in the canonical
CUI store instead. The policy also nominates January as the annual training
month while these events fall in August. Both are policy-text corrections, not
control gaps.

### POA&M-048 — Compliance working copies drift silently from canonical — OPEN

**Finding F-2026-08-32. Opened 2026-08-03 (**`DIWAI-CR-2026-08-09` **§5.5).**

The canonical store for compliance documents is the Nextcloud CUI groupfolder
(`Compliance/`, `CUI_`-prefixed files). `~/diwai/assessment-2026-08/` holds
working copies **with no provenance marker and no freshness check**.

**What happened.** During the 2026-08-03 documentation pass, the working file
`System_Security_Plan_v2.15.md` was edited and prepared for reissue. It was
**byte-identical to an 08-02 09:45 snapshot — 6,199 bytes and 125 lines behind
the canonical copy** written 08-02 17:20. Publishing it would have silently
reverted §2.5.1.1 carrier separation, the triple-homed interface table and
household out-of-boundary determination, the 08-02 wireless-boundary resolution
(`DIWAI-CR-2026-08-03`), and the OpenSCAP **101/101** result in 7 places. The
stale file carried the **same version number** as canonical, so nothing about
its name, content, or behaviour indicated it was old.

**How it was caught.** By comparing file sizes against canonical before
promoting the file — an ad-hoc check performed because a version bump required
touching the canonical store. **No control detected it.** Had the work stayed
local, the regression would have shipped.

**Scope.** The other three documents edited in the same pass were verified
byte-identical to canonical beforehand, so only the SSP was affected. The SBOM
published to the public repository that day was built from a current copy and is
sound (verified by diff).

**Why this is a control gap, not a one-off.** 3.4.1 requires an accurate
baseline inventory and 3.4.3 requires changes to be tracked and controlled. A
document set whose authoritative copy can be overwritten from an unmarked stale
working copy satisfies neither. It also directly threatens 3.12.4, since the SSP
is the document of record.

**Remediation — pre-edit freshness check IMPLEMENTED 2026-08-03**
(`~/diwai/scripts/doc-freshness.py`, owner-selected from the three candidates).

A plain diff was rejected as the mechanism: "working differs from canonical" is
the **normal** state while editing, so a check that warns on every difference is
ignored within a day. The tool instead keeps a **baseline** — the hash of
canonical as of the last time the two agreed (`~/diwai/etc/doc-baseline.json`) —
and resolves three hashes into an unambiguous state:

| State       | Meaning                                          | Editable |
|:------------|:-------------------------------------------------|:---------|
| IN SYNC     | identical to canonical                           | yes      |
| LOCAL AHEAD | local edits; canonical unmoved since sync        | yes      |
| **STALE**       | **canonical moved ahead; this is the old canonical** | **NO**       |
| **DIVERGED**    | both sides moved since last sync                 | **NO**       |
| **UNKNOWN**     | differs, no baseline — provenance unprovable     | **NO**       |

`publish` **refuses** on STALE/DIVERGED/UNKNOWN, so the specific action that
would have caused the 2026-08-03 damage is blocked, not merely warned about.
The check **fails closed**: if the canonical store cannot be read it exits
non-zero and states that nothing was verified — deliberately, because a checker
that passes when it cannot see canonical repeats the defect it exists to catch
(cf. POA&M-031, POA&M-015).

**Verified against the original failure**, not merely unit-tested: the 08-02
09:45 snapshot was restored as the working copy with a matching baseline, and
the tool returned **STALE**, exit 1, with `publish` **REFUSED** and canonical
confirmed byte-unchanged. Normal editing was separately confirmed to report
LOCAL AHEAD, exit 0 — no false alarm.

**First run found a second instance of the same class, in the opposite
direction:** `DIWAI-CR-2026-08-08` (Kernel and macOS Upgrades, 2026-08-03)
exists **only** in the working directory and was never published to canonical.
The canonical change-record series therefore has a gap at 08-08.

**Item remains OPEN.** The check is advisory until it is enforced — it protects
only the edits where someone remembers to run it. Closure requires either
automatic invocation before edits or a decision to accept manual use. The two
unchosen remediations (generate working copies on demand; make Nextcloud the only
editable location) remain available and would remove the drift class entirely
rather than detect it.

**Note on detection cost:** this is the second finding in this assessment where a
process ran, reported success, and delivered nothing — cf. POA&M-031 (archive
pipeline exiting 0 for months) and POA&M-015 (mSCP scan). The common defect is
absence of verification, not absence of automation.

### POA&M-026 — LUKS single keyslot, no escrow — OPEN (risk decision)

One keyslot, no TPM2/clevis token. Consequences: the VM **cannot boot
unattended**, so kernel patching requires physical presence and the system does
not self-recover from power loss; and passphrase loss is **total, unrecoverable
data loss** — the material succession risk on a single-operator system. Options:
enrol a TPM2/clevis keyslot (accepting that the disk then unlocks without human
presence), add an escrowed recovery key, or formally accept the risk.

**DECISION 2026-08-03 — TREAT via BREAK-GLASS ESCROW** (`DIWAI-RAR-001` §7.1,
D-1). A second LUKS keyslot will be enrolled holding a recovery passphrase,
sealed and stored under a documented break-glass procedure with tamper-evidence
and a use log — consistent with the sysadmin break-glass account precedent set
during the 2026-04-15 YubiKey lockout.

**TPM2/clevis was considered and rejected.** It would fix unattended boot, but
the volume would then decrypt without human presence — trading at-rest
confidentiality against physical theft for boot convenience. On a system whose
threat model includes rack-level physical loss (R-14, POA&M-050), that is the
wrong trade. **Unattended boot therefore remains unsolved** and stays a
consequence of this item; kernel patching still requires physical presence.

**Implementation requires the current passphrase and must be performed by the
owner** — it cannot be delegated or automated. Outline:

1. `cryptsetup luksAddKey` a second slot with a newly generated high-entropy passphrase.
2. Verify the new slot unlocks the volume **before** relying on it (`cryptsetup open --test-passphrase`).
3. Confirm both slots are populated (`cryptsetup luksDump`), and that the original still works.
4. Seal the recovery passphrase in tamper-evident storage, physically separate from the rack.
5. Write the break-glass procedure: who may open it, under what conditions, what is logged, and re-seal/rotate after any use.
6. Record completion here and update R-05.

**PROGRESS 2026-08-04 — passphrase printed and sealed in an envelope inside the
rack cage.**

**What this fixes.** The recovery material is no longer held **on the system it
recovers**. Until today the break-glass note lived on the Mac — the host that
would be unavailable in precisely the circumstances requiring it — a circular
dependency identified in `DIWAI-IR-TTX-001` §6.1 item 6. That is now broken, and
a second person could in principle perform a recovery. It also gave the
restoration test of the same day a real escrow to fall back on.

**What it does not yet fix — the location.** The envelope is **inside the rack
cage**, co-located with the equipment it protects. The scenarios this escrow
exists for include **rack-level loss** — fire, flood, theft (risk **R-14**) —
and in each of those the envelope is lost or taken with the hardware. It is
**off-system but not off-site**, which addresses the compromise and
unavailability cases but not the destruction case.

**Remaining to close this item:**

1. **A copy held off-site** — the residence safe, a bank box, or with a named custodian under POA&M-049. The rack copy is convenient and should stay; the point is that it must not be the only one.
2. **Tamper-evidence, not merely a seal.** A signed and dated signature across the flap, or a numbered tamper-evident bag, so that opening is *detectable* rather than merely inconvenient. A plain sealed envelope can be opened and replaced.
3. **A written break-glass procedure** — who may open it, under what conditions, what is recorded, and the requirement to **rotate the passphrase and re-seal after any use**. Without rotation-on-use, one opening compromises the credential permanently.
4. **Clarify what was escrowed.** Decision D-1 called for enrolling a **second LUKS keyslot** holding a newly generated passphrase. If what has been sealed is the **existing** passphrase, that is a valid and simpler form of escrow, but it is not a second keyslot: there is still a single credential, and compromise of the envelope compromises the volume. Owner to confirm which was done, and whether a second keyslot remains wanted.

**Superseded pre-2026-08-04 note:** Not complete until step 4. A second keyslot whose passphrase is stored beside
the machine, or only in the operator's memory, changes nothing.

### POA&M-027 — SSP accuracy and definition gaps — OPEN

> **2026-09-13 — physical-access deductions.** **3.10.3 recovered (−1 → 0):** first nil-activity attestations recorded (no non-household visitors since 2026-08-07), `DIWAI-PE-LOG-001` §4 and §6. **3.10.4 remains −1 by owner decision:** the rack is opened frequently during active development and openings are not logged. Camera retention is confirmed at 30 days maximum, and alarm history is dropped from the claim. **Also noted for this item:** the SSP Control Family Status table (Requirements Fully Met **35/110**) has not been reconciled since early August, and the dashboard now displays it.

Consolidates the documentation findings. The SSP must, in v2.15: enumerate the
internet-published services; document the wireless path; add an account
inventory including the `sysadmin` break-glass account; state the
single-operator **separation-of-duties limitation** explicitly with compensating
controls; define identifier reuse and inactivity periods, flaw
identify/report/correct timeframes, and a key-management procedure; inventory
external system dependencies; add an alternate-work-site procedure and media
custody record (the NCMA demo was exactly such an event, undocumented); correct
`en1` addressing, the `[DOMAIN.ORG]` artifact, and the DIWAI-IAP-001 date.

**These do not change the system's security. They change whether it can be
assessed, maintained, or handed to a successor** — which is why they are tracked
rather than dismissed.

### POA&M-028 — macOS Tahoe 26.6 pending — OPEN

Recommended update requiring a restart on the CUI host. Schedule.

### POA&M-029 — Two mSCP rules pair with assessment findings — OPEN

`audit_settings_failure_notify` (3.3.4 — no alert on audit failure) and
`os_firewall_default_deny_require` (3.13.6). Both were independently identified
in the assessment, so they close together with the corresponding requirements.
Subset of POA&M-003.

> **2026-09-13 — 3.3.4 half discharged (`DIWAI-CR-2026-09-07`).** `audit_warn` now uses `logger -s -p` (the mSCP rule) and copies each warning to a file the Mac agent forwards. Rule 100220 alerts, `closefile` rotation is suppressed (100221), and `diwai-control-health` check 11 mails the owner. Proven with a real `allsoft` warning: written 13:30:35, alerted 13:30:36, relayed 13:31:13, **received in the owner's Gmail 13:31:11 MDT** (evidence `CUI_EV_AU_3.3.4_Alert_Receipt_Gmail_2026-09-13.pdf`). **3.3.4 −1 → 0.** `os_firewall_default_deny_require` (3.13.6) remains open.

### POA&M-030 — Sanitisation and off-site maintenance untested — OPEN

`DIWAI-PE-MP-001` §4.5 defines media sanitisation and off-site maintenance
procedures. Neither has been exercised and no log exists. A sanitisation log
should exist even if empty.

---

## SUMMARY DASHBOARD

| Metric                            | Value                                    |
|-----------------------------------|------------------------------------------|
| Total items ever opened           | **63**                                   |
| **Closed**                        | **38**                                   |
| **Open**                          | **25** — **010 (reopened)**, 003, 023, 026, 027, 029, 030, 032, 048, 049, 050, 051, 052, 056, 057, 058, 059, 060, 061, 062, 063, 064, 066, 068, 069 |
| Overdue / past due                | **0** (005 and 006 closed 2026-08-03)    |
| Reopened                          | **1 — POA&M-010, reopened 2026-08-07** (second time; clock free-running again, detection without correction) |
| Architectural                     | 1 (023 — accepted in writing to 2027-03-31) |
| Documentation-only                | 1 (027, consolidating ~12 findings)      |

**Listing omission corrected 2026-08-07.** The open count read **27** above a list
naming only **26** items — POA&M-068 was counted in the total but never added to the
enumeration when it was opened on 2026-08-06. The count was right and the list was
short. Recorded rather than silently adjusted, since the enumeration is what a
reader checks work against.

**Counts recomputed 2026-08-04 by parsing the register table itself**, after the
previous dashboard was found to state `30 / 12 / 18` — a state predating items
that run to 059 — while asserting a score of 87 above a table reading 56.

**SPRS: 87/110.** Recomputed 2026-08-03; weights **verified** 2026-08-02 against the *NIST SP 800-171
DoD Assessment Methodology v1.2.1*, Annex A. The POA&M-008 "TBD" is resolved:
**−11** (3.2.1 −5, 3.2.2 −5, 3.2.3 −1).

|                                                       | Score |
|:------------------------------------------------------|------:|
| Maximum score                                         |   **110** |
| Open deductions (enumerated below)                    |   **−23** |
| **Current**                                           |    **87** |

**Stated as `110 − 23` rather than as a running total.** The previous revision
carried a four-line reconciliation ending in **56** directly beneath a heading
asserting **87**; the arithmetic was from an earlier state and was never updated.
The deduction list below is the authoritative figure and is verifiable by
addition.

**The June figure of 98/110 was never correct.** Two errors compounded: 3.7.5
was weighted −3 when the methodology assigns it −5, and the 11 points for
POA&M-008 were acknowledged as pending but never subtracted. The corrected
baseline was **85**.

**Open deductions (−23) — recomputed 2026-08-03, post-scrub:** 3.5.3 −5,
3.7.5 −5, 3.13.5 −5, 3.14.1 −5, 3.3.4 −1, 3.10.3 −1, 3.10.4 −1.

**Unchanged by the POA&M-007 closure of 2026-08-06 — stated because the opposite
was expected.** Revision 1.7 recorded that both the 3.5.3 and 3.7.5 deductions were
"gated entirely on POA&M-007". The item is closed and **neither point is claimed**:

* **3.7.5 (−5) — RECOVERED 2026-08-07, −5 → 0.** POA&M-065 closed: the exempted
  key is now `from=` + forced `command="/usr/bin/scp -t …"` + `restrict`, and the
  path was **tested incapable of carrying a maintenance session** — no command
  execution (0 bytes returned), no pty (rc 255), destination pinned server side.
  `DIWAI-CR-2026-08-18`.
* **3.5.3 (−5) — RECOVERED TO −3 on 2026-08-07 (+2).** An interactive key was
  enrolled and a **live three-factor login recorded** — `Accepted
  keyboard-interactive/pam for [USERNAME] from 127.0.0.1` at 16:41:27, with the
  module's `DISALLOW_REUSE 59538082` counter written and the scratch-code count
  unchanged, proving a real TOTP. **Console access remains the same factor twice,
  which is the −3 floor.** `DIWAI-CR-2026-08-25`.

**Reachable near-term figure: 94/110.** It is not claimed here, because a control
that has never authenticated a user is configuration, not a control — the POA&M-062
lesson. See `DIWAI-CR-2026-08-17` §7.

> **SUPERSEDED IN PART, 2026-08-07.** POA&M-065 closed the same day and **3.7.5 is
> recovered (+5)**. The paragraphs above are retained as the reasoning of record for
> why the point was withheld on 08-06 and released on 08-07 — the difference being a
> tested path rather than a configured one.
>
> **Open deductions are now −16: 3.5.3 −3, 3.13.5 −5, 3.14.1 −5, 3.3.4 −1,
> 3.10.3 −1, 3.10.4 −1. Score = 110 − 16 = 94/110** (3.7.5 recovered 08-07 via
> POA&M-065; 3.5.3 reduced 08-07 via the exercised MFA login).
>
> **3.5.3 remains the only near-term item at −5**, capped at −3 by single-factor
> console access and not defensible even at −3 until an interactive key exists and
> one MFA login is recorded (**+2 → 94/110**).

> **DETERMINED 2026-09-13 — the figure of record is 93/110, not 94.** The arithmetic above (110 − 16) remains correct as arithmetic. The owner determination withholds **one further point** on the `DIWAI-VS-001` §4 dispute, applying the standing rule that a disputed value is reported at the lower, more conservative reading. `DIWAI-VS-002` (2026-09-13) found the Mac credential policies present but **not negatively tested**, so enforcement is configured rather than demonstrated. The reasoning above is retained as the record of how the 94 was reached; it is not deleted.

> **RE-DETERMINED LATER 2026-09-13 — the figure of record is 94/110.** The block above is superseded, not deleted. Its basis — Mac credential policies *configured but not negatively tested* — proved incomplete when the tests were run: the **Mac password-history rule was malformed and skipped on every change since 2026-08-07**, and the **389-DS minimum length was disabled** by `passwordCheckSyntax: off`. Both were repaired in session and 3.1.8, 3.5.7 and 3.5.8 were then **proven by refusal on both hosts** (`DIWAI-CR-2026-09-03`). With no dispute remaining, the owner re-determined the score at the arithmetic figure: **110 − 16 = 94/110**.

> **RECOMPUTED 2026-09-13 (later) — the figure of record is 101/110.** Three recoveries, each proven by test before it was claimed:
>
> | Req | | Evidence |
> |:---|---:|:---|
> | 3.14.1 | **+5** | POA&M-051 closed — manager on 4.14.7, verified functioning (`DIWAI-CR-2026-09-04`) |
> | 3.3.4 | **+1** | Mac audit-failure warning received in the owner's Gmail (`DIWAI-CR-2026-09-07`) |
> | 3.10.3 | **+1** | Visitor nil attestation — owner determination (`DIWAI-PE-LOG-001` §6) |
>
> **Open deductions are now −9: 3.5.3 −3, 3.13.5 −5, 3.10.4 −1. Score = 110 − 9 = 101/110.**
> **Basis — owner determination 2026-09-13: evidence-strict.** Points are earned only by controls implemented *and* proven working by evidence, including negative testing (`DIWAI-VS-001`). The strict 800-171A objective count, **35/110**, measures definition and documentation as well and is reported alongside as the POA&M-027 gap, not as the score. See SSP v2.18 §11.
> **Withheld:** 3.10.4 by owner decision (rack openings not logged during development). The 94 reasoning above is retained.

> **WITHHELD THE SAME DAY — the figure of record is 100/110.** The evidence-strict basis was applied to **3.5.6**: a 90-day inactivity disable is *defined* (SSP Appendix E.4) but *enforced nowhere* (389-DS plugin off; no VM-local or Mac mechanism). **Open deductions are now −10: 3.5.3 −3, 3.13.5 −5, 3.10.4 −1, 3.5.6 −1. Score = 110 − 10 = 100/110.** POA&M-076.

**~~Two deductions have no POA&M item.~~ CORRECTED 2026-08-07.** `3.10.3 −1` and
`3.10.4 −1` **are** assigned — SSP v2.16's deduction table maps both to
**POA&M-027** ("No visitor log — procedure defined v2.15, not yet operating").
They are invisible in this register's item rows, which is a presentation gap, not an
ownership gap. **Nor are they recoverable on held evidence:** the visitor log exists
at `Business_Admin/Visitor Log.xlsx` but contains **headers and no entries**, so the
SSP's "defined, not operating" is accurate and the deductions are correct.
`DIWAI-PE-LOG-001` now instantiates the rack log and a nil-activity attestation;
**the +2 comes when the log is kept, not because it exists.**
`DIWAI-CR-2026-08-27`.

**3.3.7 recovered (+1) in the scrub.** Clock verified synced (0.0003 s from NTP,
one selected source, leap normal). **This requirement was closed once before and
recurred**, so the closure is qualified: what differs now is that
`diwai-control-health` explicitly checks that chrony has a *selected source*
(`DIWAI-CR-2026-08-01` C16), which is the condition that failed silently last
time — the VM reported itself synchronised while 24 minutes adrift. The control,
not the correction, is what justifies closing it again.

**SUPERSEDED 2026-08-08 — the reasoning above did not hold and should not be
cited.** "The control, not the correction, is what justifies closing it" is
exactly the basis on which revision 1.16 **reopened** POA&M-010: the check had
been reporting `chrony has NO selected source` since 2026-08-02 — 81 alerts —
and **nothing acted on any of them**. A detector without a corrector does not
satisfy 3.3.7. The +1 was thereafter carried as *questionable but not withdrawn*
(revisions 1.16, 1.20) and is **CONFIRMED by owner determination 2026-08-08** on
a different and sufficient basis: a corrector now exists (`diwai-clock-guard`)
and has been **observed recovering the clock on a real post-suspend episode**
(`DIWAI-EV-AU-2026-08-08`, episode 07:17:01–07:19:43), and the upstream cause was
removed the same day by disabling host sleep. Because the +1 was never withdrawn,
this confirmation **moves no number** — 94/110 stands. See POA&M-010 and revision
1.30.

**Recovered 2026-08-03 (+30):**

| Req | Weight | Basis | Evidence |
|:---|---:|:---|:---|
| 3.2.1 | +5 | Awareness training delivered; policies acknowledged | IF141.16 certificate; `DIWAI-PAF-001` **signed** |
| 3.2.2 | +5 | Duties defined, assigned, and competency evidenced | `DIWAI-RAM-001` + `DIWAI-CRC-001`, both **signed** |
| 3.2.3 | +1 | Insider-threat training completed | INT101.16; `DIWAI-TRR-001` attestation **signed** |
| 3.11.1 | +3 | Risk assessment conducted and formally accepted | `DIWAI-RAR-001` v1.1 §7.2 **signed** |
| 3.6.3 | +1 | IR capability tested | `DIWAI-IR-TTX-001` conducted and signed; 10 gaps recorded |
| 3.1.16 | +5 | Wireless not permitted: `en1` powered off and inactive, nothing scheduled re-enables it, pf bars CUI egress via `en1` | `DIWAI-CR-2026-08-03`; verified live |
| 3.11.2 | +5 | CVE-level scanning operational — `diwai-cve-scan.timer` active, last run 2026-08-03 07:47 | `DIWAI-CR-2026-08-04`, `-08-05`. **Caveat: POA&M-041** — Remi/Wazuh repos out of scope |
| 3.5.10 | +5 | Directory now **refuses insecure binds** (`nsslapd-require-secure-binds: on`); storage PBKDF2-SHA512; 389 closed at firewall | `DIWAI-CR-2026-08-10` |

**Every point recovered was already earned before today.** The work existed —
signatures, wireless disablement, CVE scanning — and the register had not caught
up. Only 3.5.10 required new engineering (2026-08-03).

**Score: 110 − 23 = 87/110.**

**Recovered 2026-08-01 (+13):** 3.3.1 +5 (audit retention), 3.12.3 +5 (control
health monitoring), 3.1.8 +1, 3.5.7 +1, 3.5.8 +1.

**Partial-credit rules that apply here:** 3.5.3 scores −3 if MFA covers remote
and privileged users only, **−5 if no users** — currently −5. 3.13.11 scores −3
if encryption is employed but not FIPS-validated, −5 if none; FIPS-validated
encryption **is** in use, so it scores **0**.

**Methodology note:** the DoD methodology states an assessment cannot be
completed without a system security plan describing how each requirement is met.
SSP accuracy is therefore a scoring prerequisite, not a presentational nicety —
which is the strongest argument for POA&M-027.

Under a strict SP 800-171A reading (a requirement is met only when *every*
objective is satisfied) the figure is **34/110**. The gap between the two
readings is the documentation debt tracked as POA&M-027.

**Assessor independence:** this is a self-assessment. The system owner is also
the assessor and the implementer of the remediation recorded here. No
independent review has been performed.

---

## DOCUMENT CONTROL

| Field          | Value                                |
|----------------|--------------------------------------|
| Prepared by    | [SYSTEM-OWNER], ISSO / System Owner      |
| Date           | 2026-08-01                           |
| Next review    | 2026-11-01 (quarterly, with the SSP) |
| Supersedes     | v1.2 (2026-06-12)                    |
| Classification | **CUI**                                  |
| Distribution   | Authorized personnel only            |
