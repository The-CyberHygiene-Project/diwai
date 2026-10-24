> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — AU AND IR POLICY WORDING CORRECTED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-40** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED. Owner approved the drafted wording 2026-10-24.** |
| **System** | Documents only; no system setting changed |
| **Addresses** | **3.3.1** [d] (retention defined and stated truly); recovery wording in the Incident Response Policy |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. What was checked (read-only, 2026-10-24)

- The Wazuh indexer holds the index lifecycle policy `wazuh-90day-retention` (delete an alert index 90 days after creation), attached to **85 of 85** `wazuh-alerts-*` indices. Rebuilt 2026-09-25 from the deletion history after the host panic (19 deletions, each at 90.00 to 90.01 days); definition in `~/diwai/etc/wazuh-90day-retention.ism.json`. The oldest index is 2026-07-27, so the first deletion under the rebuilt policy falls on 2026-10-25.
- The NAS archive job (`wazuh-log-archive`, 02:00) removes only its own staging files; nothing expires the archives. Still outstanding.
- `/backup/daily`, `/backup/procedures`, `/var/backups/securemac-rear.iso` and the `rear` command do not exist on the VM.

## 2. Changes

- **AU policy §3.2 item 3:** the "no retention policy" statement replaced by the enforced 90-day rule (verification date, rebuild history); Mac 90 days added; the POA&M-059 note narrowed to the NAS archive expiry. Dated change note added; version unchanged.
- **IR policy:** "ReaR ISOs" and "ReaR backups" replaced by the backup procedures and Time Machine/archive; "Automated daily backups of critical files" removed; both restore blocks (Step 3.2 and the appendix) replaced by a pointer to `CUI_Backup_Procedures_v2.0.md` §6; two pointers to `/backup/procedures/` repointed. Response targets unchanged. Dated change note added; version unchanged.
- No new restore steps were written; they exist in the backup procedures.

## 3. Found, not changed

- Step 3.3 of the IR policy still uses `ipactl` (a FreeIPA command; this system runs 389-DS, `dirsrv@diwai`). Needs the owner's approval to correct.
- First-deletion check: confirm on or after 2026-10-25 that the oldest alert index is gone.

## 4. Rollback

Backups `.bak-20261024-cr40` of both policies.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved as drafted 2026-10-24 |
