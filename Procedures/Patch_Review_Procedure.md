> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# PATCH REVIEW PROCEDURE
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-PR-001** |
| **Version** | 1.3 |
| **Date** | October 9, 2026 (issued August 2, 2026) |
| **Owner** | [SYSTEM-OWNER], ISSO / System Owner |
| **Implements** | SSP v2.18 **Appendix E.3** (Flaw Remediation Timeframes) |
| **Satisfies** | 3.14.1, 3.4.3 · addresses **POA&M-025** |
| **Cadence** | **Monthly** — after the automated scans — **plus on return to the system after any gap over 30 days**. Revised 2026-09-15 (was weekly). **PATCH-class CRITICAL is exempt from the cadence: 72 h from detection, §6.1** |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Why this exists

Appendix E.3 defines *when* flaws must be remediated. It did not say *how* the
review is performed or *where* it is recorded, so the cadence existed on paper
and had never been exercised. That was the 3.4.3 finding.

**The compensating control for the `dnf-automatic` deviation is this review.**
If the review does not happen, the deviation is not compensated — it is simply
an unpatched system. That is the one thing this document exists to prevent.

---

## 2. Background — the deviation being compensated

`dnf-automatic` runs **download-only** (`apply_updates = no`).

On 2026-07-31 an unattended upgrade applied a change nobody reviewed and took
the Wazuh manager down for **21 hours, undetected**. Unattended installation
also applies unapproved changes to a CUI baseline, contrary to 3.4.3/3.4.4.

Consequences, both deliberate:

- Updates are **downloaded and staged** — they are on disk and immediately
  installable, so review costs time but not availability.
- The SSG rule `dnf-automatic_apply_updates` cannot pass. It is **tailored out**
  of the scan with justification recorded in
  `/etc/diwai/scap/diwai-cui-tailoring.xml`, not silently suppressed. The VM
  therefore reports **101/101** rather than a standing 101/102 failure.

---

## 3. Timeframes (from Appendix E.3)

| Activity | Timeframe |
|:---|:---|
| Identify available updates | Daily, automated |
| **Review pending updates** | **Monthly** — this procedure — **and on return after any gap over 30 days** (revised 2026-09-15; was weekly) |
| Apply Critical / security-relevant | **Within 7 days** of review — **except PATCH-class CRITICAL, which is 72 hours from detection (§6, §6.1)** |
| Apply routine updates | **Within 30 days** of review |
| Reboot for kernel/OS updates | **Within 14 days**, scheduled and attended |

---

## 4. Review procedure

Allow 15–20 minutes. Run after the Monday scans (`diwai-cve-scan.timer` 04:30,
`oscap-scan.timer`).

### 4.1 VM — what is actually vulnerable

```
sudo /usr/local/sbin/diwai-cve-scan
```

Read the **classification**, not the total. The three sections mean different
things:

| Class | Action |
|:---|:---|
| **PATCH** | Same stream, fix available. **This is the actionable list.** Apply within the E.3 timeframe |
| **STREAM-MIGRATION** | No fix in the installed stream. Not a patch — raise or update a POA&M item. Do not attempt during a review |
| **THIRD-PARTY** | Rocky errata cannot judge these. Check the vendor separately — see §4.3 |

If the output says **`STALE CACHE`**, the advisory data did not refresh. Treat
the run as **incomplete**, not clean, and investigate connectivity.

### 4.2 VM — what is staged

```
sudo dnf check-update
sudo dnf updateinfo --summary
```

`check-update` exits **100** when updates are available and **0** when none are
— it is not an error. `updateinfo` returns nothing on Rocky (no errata
metadata); that is expected and is why `diwai-cve-scan` exists.

### 4.3 Third-party components

`diwai-cve-scan` cannot assess these. Check each against its vendor:

| Component | Where to check |
|:---|:---|
| **Remi PHP** | Remi release notes / `dnf --disablerepo='*' --enablerepo=remi* check-update` |
| **Wazuh** | **Version-locked at 4.14.6** by `dnf versionlock`. It will **not** receive security updates until the lock is deliberately lifted and an upgrade tested. Review the lock quarterly |

Tracked as POA&M-041.

### 4.4 Mac host

```
sudo /Users/[USERNAME]/diwai/scripts/diwai-cve-scan-mac
softwareupdate --list
```

`diwai-cve-scan-mac` covers Homebrew (NVD CPE match), Python packages (OSV) and
macOS update currency. Read its classification the same way as the VM's:

| Class | Action |
|:---|:---|
| **UPGRADE AVAILABLE** | The actionable list. Apply per the timeframes above |
| **AT LATEST** | Already newest — **upgrading changes nothing.** Do not re-triage between reviews |
| **SUPPRESSED** | Triaged not-applicable; reasons in `~/diwai/etc/cve-mac-suppressions.txt` |

**Treat Homebrew results as ADVISORY.** CPE product is assumed to equal the
formula name, so a formula whose upstream name differs returns nothing —
**absence of findings is not evidence of absence.** Entries marked `UNPINNED`
used a wildcard vendor and may include unrelated products; verify before acting.
Python results (OSV) are authoritative. `softwareupdate` is a currency check
only — Apple publishes no machine-readable CVE-to-build map.

### 4.5 Apply

Apply only what the review selected, and record what was applied.

```
sudo dnf update --advisory=<RLSA-ID>        # preferred: scoped to the advisory
sudo dnf update <package> [<package>...]     # or named packages
```

**Do not run a bare `dnf update` during a review.** That is unattended
installation performed by hand — the thing this deviation exists to avoid.

### 4.6 Verify afterwards — mandatory

The 2026-07-31 outage happened because nothing checked the system after a
change.

```
sudo /usr/local/sbin/diwai-control-health
systemctl is-active wazuh-manager suricata auditd chronyd httpd mariadb dirsrv@diwai
```

Both must be clean before the review is closed. If the update requires a
reboot, schedule it within **14 days**, attended — the VM cannot boot
unattended (single LUKS keyslot, no escrow, POA&M-026).

### 4.7 After a macOS update — mandatory

A macOS update can silently reset controls on the Mac. Two have been found: the
mSCP settings (`audit_warn`, screensaver unlock; POA&M-003, -029) and, on
2026-09-03, the TOTP line in `/etc/pam.d/sshd`, which stayed missing for 36 days
(`DIWAI-CR-2026-10-11`, finding 7). After every macOS update, and before the
review is closed:

```
sudo bash ~/diwai/scripts/fix-mscp-regression.sh
```

Read the last step of its output (step 5, the Mac SSH TOTP check). **OK** means
SSH on the Mac still asks for a TOTP code. **FAIL** means it may ask for a key
and password only: run `sudo bash ~/diwai/scripts/restore-mac-ssh-totp.sh` with a
second session open, then run the step again. Record the result in the review log.

---

## 5. Record

One row per week, appended to `Compliance/Patch_Reviews/CUI_Patch_Review_Log.md`.
**A review that is not recorded did not happen** — the record is the evidence
for 3.14.1 and for the compensating control.

| Date | PATCH findings | Applied | Deferred (and why) | Reboot needed | Post-check clean | By |
|:---|:---|:---|:---|:---|:---|:---|
| 2026-08-02 | 7 (kernel RLSA-2026:49212) | — | Pending scheduled reboot window | Yes | Yes | DES |

Deferrals need a reason and a date. An item deferred twice should become a
POA&M entry rather than a recurring row.

---

## 6. Escalation

| Condition | Action |
|:---|:---|
| PATCH-class **CRITICAL** | Apply within **72 hours of detection** — out of cycle, without waiting for the next review |
| A CVE with known exploitation | Apply immediately; treat as an incident if the system is exposed |
| Fix requires a stream migration | POA&M item — do not attempt in a review |
| Update breaks a control | Roll back, record it, and treat the breakage as the finding |

### 6.1 When the 72-hour clock starts (added 2026-09-15, F-2026-09-04)

**"Detection" means the timestamp of the scan report that first lists the
finding** — `cve-scan-mac-<date>.json` on the Mac, the `diwai-cve-scan` report on
the VM. Not the date of the review, not the date the alert mail is read,
and not the vendor's publication date.

**Why it needed saying.** As issued, §6 set a 72-hour deadline and **never said
what started it**, while §3 measures "within 7 days" from *review*. On 2026-09-15
three CRITICAL findings visible in the 09-14 scan were applied about a day and a
half after detection — a breach under one reading and compliant under the other,
with the procedure itself unable to settle which. A deadline whose start is
undefined cannot be assessed, met, or evidenced.

**Precedence.** For PATCH-class CRITICAL, **§6 governs and §3 does not apply**: 72
hours from detection, regardless of when the next review falls. §3's review-based
timeframes govern everything else.

**This is what the automation already measures.** `diwai-control-health` computes
the 72 hours from the scan report's own timestamp and mails on breach. The
procedure now matches the check, rather than asserting a deadline the check
measures differently.

**The clock does not pause for a missed review.** A lapsed weekly cadence is its
own finding (3.14.1) and never converts an overdue critical into a compliant one.

---

## 7. Known gaps

| # | Gap | Tracking |
|:--|:---|:---|
| 1 | ~~Mac host has no CVE-level scanning~~ — **closed 2026-08-03**, `diwai-cve-scan-mac` | POA&M-022 closed |
| 2 | ~~`diwai-cve-scan` not monitored by `diwai-control-health`~~ — **closed 2026-08-02**, check 5c; scan freshness, advisory-cache staleness and actionable CRITICAL all monitored, failure paths tested | POA&M-022 closed |
| 3 | Third-party repos not covered by `diwai-cve-scan` (Remi, Wazuh) | POA&M-041 |
| 4 | Wazuh version-locked and therefore unpatched | POA&M-041; `DIWAI-RAR-001` D-5 |
| 5 | `nodejs` 18 and `mariadb` 10.5 are EOL; no fix exists in the installed streams | POA&M-022 detail |
| 6 | **Homebrew CPE matching is heuristic** — a formula whose upstream CPE product differs returns nothing, silently. Absence of Mac findings is not evidence of absence | `DIWAI-CR-2026-08-05` §2 |
| 7 | **`libssh2` 9 HIGH CVEs, no fix available**, at latest version | POA&M-042 |

---

## 8. Revision history

| Version | Date | Author | Description |
|:---|:---|:---|:---|
| **1.3** | **2026-10-09** | **[SYSTEM-OWNER]** | **NEW §4.7: after every macOS update, run the mSCP fix and read the Mac SSH TOTP check.** A macOS update removed the Mac TOTP line on 2026-09-03 and nothing noticed for 36 days (`DIWAI-CR-2026-10-11`, finding 7). The mSCP fix script now ends with the TOTP check; the procedure requires it to be read and recorded. |
| **1.2** | **2026-09-15** | **[SYSTEM-OWNER]** | **REVIEW CADENCE WEEKLY → MONTHLY, by owner decision, plus a mandatory review on return after any gap over 30 days.** The weekly cadence lapsed for five and a half weeks and was caught by automation, not the calendar. The system is worked in concentrated sessions and may sit unattended for weeks, but **its exposure does not pause** — webmail, mail and OpenVPN are internet-published continuously. The response is split: **detection stays daily and automated** with control-health alerting on actionable CRITICAL; **PATCH-class CRITICAL stays at 72 h from detection** (§6.1, unchanged); **the human review moves to monthly**. 3.14.1 requires timeframes to be defined *and met* — a monthly cadence that is met evidences the control better than a weekly one that is not. **Header version corrected 1.0 → 1.2**: the 1.1 entry below was recorded without bumping the header. SSP Appendix E.3 revised to match. **Outstanding:** a reminder to the owner (SMS preferred) is not yet wired, so the cadence currently depends on memory |
| **1.1** | **2026-09-15** | **[SYSTEM-OWNER]** | **The 72-hour escalation clock now has a defined start (F-2026-09-04).** As issued, §6 required PATCH-class CRITICAL within 72 hours but never said from *what*, while §3 measured "within 7 days" from review — so the same event was both a breach and compliant depending on which row was read. §6.1 defines detection as the timestamp of the scan report that first lists the finding, states that §6 takes precedence over §3 for PATCH-class CRITICAL, and records that a lapsed review cadence does not pause the clock. This aligns the procedure with what `diwai-control-health` already measures. Raised while applying six Mac upgrades on 2026-09-15 (`CUI_Patch_Review_Log.md`) |
| **1.0** | **2026-08-02** | **[SYSTEM-OWNER]** | Initial issue. Operationalises SSP Appendix E.3; establishes the weekly review as the compensating control for the `dnf-automatic` deviation |
