> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MAC AUDIT RETENTION 7 DAYS → 90 DAYS
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-39** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§2). Owner approved 90 days 2026-10-23.** |
| **System** | Mac host |
| **Addresses** | **3.3.1** [d] (audit records are retained as defined); Rev 3 03.03.01 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Change

`/etc/security/audit_control`: `expire-after:7d` → `expire-after:90d`, matching the VM (83 days held) and the Wazuh alerts (90 days). Backup `/etc/security/audit_control.bak-20261023-1816`. SSP Appendix E.9 updated.

## 2. Verification

The file reads `expire-after:90d`; `audit -s` was sent and `auditd` is running and writing a new trail file; the 1,798 existing files (3.6 GB, from 2026-10-17) were all still present afterwards, so nothing was deleted by the change.

## 3. Cost

About 0.5 GB a day, so about 46 GB at 90 days, of 675 GB free (about 7%). The setting file had not changed since April and is not managed by the mSCP fixer, so a macOS update is not expected to reset it.

## 4. Limits and follow-up

- **Retention is configured today; it takes 90 days to accumulate.** Until then the Mac holds 7 days and growing. **Verify on 2027-01-21** that the oldest Mac audit file is about 90 days old (`ls /var/audit`).
- The weekly mSCP scan may report this as a difference from its default; if so, record it as a deliberate stricter setting.
- The Mac audit trail is not collected by Wazuh; it is held locally only.

## 5. Rollback

`sudo cp -p /etc/security/audit_control.bak-20261023-1816 /etc/security/audit_control && sudo audit -s`. Files already kept are not deleted by a rollback until the 7-day rule next runs, so a rollback would drop everything older than 7 days.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 90 days 2026-10-23 |
