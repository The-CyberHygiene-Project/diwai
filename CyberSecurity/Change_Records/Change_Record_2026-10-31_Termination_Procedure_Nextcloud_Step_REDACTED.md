> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — TERMINATION PROCEDURE: NEXTCLOUD STEP ADDED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-31** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§3)** |
| **Addresses** | **3.9.2**; 3.1.1; Rev 3 03.09.02 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Finding

`DIWAI-EV-PS-2026-10-23-N`: after the termination steps in `DIWAI-PS-001` PS-4, a Nextcloud app password still returned HTTP 207. Only `occ user:disable` ended it.

## 2. Change

`DIWAI-PS-001` PS-4 (Immediate Actions) now lists, in order: lock the directory entry, remove from `cui-users`, lock and expire the VM local account, **disable the Nextcloud user and delete its app passwords**. A dated change note was added. Backup `CUI_Personnel_Security_Policy_v1.2.md.bak-20261023-nc`; version unchanged.

## 3. Verification

The drill (evidence record above) showed 207 after the lock and 503 after disable, with the account then deleted.

## 4. Rollback

Restore the policy from the backup. No system change was made; the drill used a disposable account that no longer exists.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-23 (drill) |
