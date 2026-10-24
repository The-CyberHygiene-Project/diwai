> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — RECURRING OBLIGATIONS TAILORED AND RECORDED (POA&M-059)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-30** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED (§2). Not yet proven over time (§4). Owner approved every disposition 2026-10-23.** |
| **Systems** | Policy set; Mac host scripts; read-only probes of the services VM |
| **Addresses** | **3.12.3** (monitor controls on an ongoing basis), 3.12.1; POA&M-059; Rev 3 03.12.03 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Finding

The policies name a cadence on 224 lines (POA&M-059 counted 173 obligations on 2026-08-04). Five were automated; for the rest nothing recorded that they were performed. Many were inherited from the reference system and are not done here.

## 2. Changes

1. **Schedule `DIWAI-SCH-001` v1.0.** The mentions collapse into 46 distinct activities: **32 form the operating schedule (8 automated, 24 manual)**, 7 are dropped, 7 are folded into another entry. The owner approved every dropped item, change and fold on 2026-10-23.
2. **Eight policies amended** so their text matches (AU, IR, RM, AT, PS, CM, PE, SI); each carries a dated change note, versions unchanged. Backups `*.bak-20261023-sch`. AUP, IA and SC needed no change.
3. **Ledger `DIWAI-LEDGER-001`** and `scripts/obligations-log.py`: a manual obligation is recorded with a dated entry that states what was found. Seven entries were **back-filled** from records that already existed and are marked BACKFILL.
4. **Overdue report `scripts/obligations-status.py`**: manual items from the ledger; automated items read from the job's own output (archive, updates, CVE scan, YARA scan, baseline scan, rule update, backup, agents). It shows overdue and never-recorded items; it does not hide them.

## 3. What the first report showed (2026-10-23)

**15 of 32 in order.** The 17 that are not are all manual items with no entry yet (for example D1 alert mail, W1 weekly review, M3 and M7 monthly, the quarterly items). None of the automated probes failed. **The October physical attestation (M7) has not been recorded**; the last is September, and `3.10.3` rests on it being kept monthly.

## 4. Limits, stated plainly

- A schedule and a ledger are not evidence of performance. **The proof is entries over time**; about two weeks of dated entries is the first useful sample, so **3.12.3 [a] is not raised today.**
- Probe results are the job's own output, but D6 only shows both Wazuh agents active, not that a file-integrity scan completed.
- D4 (rule updates) is first proven by the 03:15 cron run on 2026-10-24.
- Change D1 (alert mail each working day) is a commitment from 2026-10-23, not a claim about past practice.
- I did not add checks to `diwai-control-health`; the report is a separate read-only script, run by hand.

## 5. Rollback

Restore each policy from its `.bak-20261023-sch` backup. The schedule, ledger and scripts can be removed without effect on any system.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-23 |
