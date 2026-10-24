> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — COMPLIANCE DASHBOARD: FAMILY TABLE RELABELLED SO IT CANNOT BE MISREAD
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-20** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§4). Owner approved 2026-10-23** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Services VM: `/usr/local/sbin/dashboard-refresh` and the page it writes, `/var/www/securemac/compliance.html`. The Mac and the SSP were not changed |
| **Addresses** | **3.12.3** (the owner's working view of control status), **3.4.3** (change control) |
| **Related** | `DIWAI-CR-2026-09-05` (dashboard figures pipeline; §5 had already noted the family table lags), SSP v2.18 Control Family Status table, POA&M-027 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

The owner viewed `compliance.html` on 2026-10-23 and found that the family table (access control 32%, personnel security 0%, risk assessment 0%, and so on, under a column headed "Pass") reads as failing next to an SPRS score of 101/110, and would be embarrassing in front of an assessor.

**The figures were correct and the labelling was not.** The table is read from the SSP's Control Family Status table: a requirement counts as met only when **every** SP 800-171A objective is satisfied, **including definition and documentation**. It adds to **42 of 110**. SPRS (101/110) is a different measure: controls implemented and proven working. The SSP already says the two are not in conflict and that the gap is documentation (POA&M-027). The page said neither. Its note also carried a stale sentence ("Risk Assessment and Awareness & Training still show pre-remediation status"), although Awareness & Training reads 100%.

## 2. Change (text only)

In `/usr/local/sbin/dashboard-refresh` (backup `dashboard-refresh.bak-20261023-relabel2`; a first attempt's backup `.bak-20261023-relabel` records a run that rolled itself back):

1. **Explanatory paragraph** under the family-table heading rewritten: it states "This is NOT the SPRS score", what each figure measures, why they differ (documentation not yet complete, POA&M-027), that a low percentage means documentation still to do and not a missing control, and the known lag (improvements after the assessment date in the heading are not reflected; a re-walk is pending). The stale sentence is removed.
2. **Column headers of the family table only:** "Pass" became "Fully met"; "Controls" became "Requirements".
3. **Section heading:** "Control Family Status" became "Control Family Status — objective-level view".

**No figure, data source, extractor or colour rule was changed.** The assessment date still comes from the assessment file's modification time (2026-09-15).

## 3. Safety design

Installer `scripts/dashboard/dashboard-relabel-retry.sh` (owner ran it with `sudo`): backs up the generator and the current page; requires each anchor to match exactly once; checks the patched file parses; runs the generator once; checks the page (new text present, stale sentence gone, headers changed, 14 family rows, the SPRS and strict-objective cards still show values, assessment date present); restores both backups on any failure. Read-only extracts `dashboard-0-diag.sh` and `dashboard-0b-diag.sh` (owner ran them) produced the exact text to match; their output files were deleted afterwards. A dry run of the patch on a copy of the generator's extracted text and on a copy of the live page was done first (headers changed, other tables untouched, second pass identical).

## 4. Verification

| Check | Result |
|:---|:---|
| First run (2026-10-23 11:11) | Text checks passed; **rolled back automatically** because my own check for the two score cards used a wrong pattern (their `stat-value` div carries a style attribute). The page was restored and confirmed unchanged |
| Pattern corrected and tested against the live page | SPRS card 101/110, strict card 42/110 matched |
| Retry (2026-10-23 11:13) | **All nine checks passed**; generator figures unchanged (SPRS 101/110, 42/110, POA&M 25 open / 66, SCAP 100/101, mSCP 133/135) |
| Page read back | New heading and paragraph present on the live page |

## 5. Open items

1. **The table is stale (assessment last re-walked 2026-09-15).** The honest fix for the low numbers is to re-walk the objective assessment where evidence has changed since then (POA&M-027, the recovery worklist). The relabel does not change any number.
2. Do not present the dashboard to an assessor as evidence; the SSP, POA&M, change records and evidence folder are the record.
3. Owner signature: done 2026-10-23.

## 6. Rollback

`cp -p /usr/local/sbin/dashboard-refresh.bak-20261023-relabel2 /usr/local/sbin/dashboard-refresh`, then `cp -p /root/compliance.html.bak-20261023-relabel2 /var/www/securemac/compliance.html` and `restorecon` it.

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
