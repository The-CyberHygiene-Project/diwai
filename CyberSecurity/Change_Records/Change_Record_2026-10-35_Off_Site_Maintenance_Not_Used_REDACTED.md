> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — OFF-SITE EQUIPMENT MAINTENANCE: NOT USED (3.7.3 NOT APPLICABLE)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-35** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED (documentation). Owner statement 2026-10-23.** |
| **Addresses** | **3.7.3**; Rev 3 03.07.04 family (maintenance); `DIWAI-APP-001` |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Owner statement

On 2026-10-23 the owner stated: *there will be no off-site service of equipment; if it breaks I fix it or provide a replacement.*

## 2. Changes

1. `DIWAI-APP-001` v1.2: new fact **F10**; requirement 3.7.3 determined **NOT APPLICABLE**, with the trigger that withdraws it (equipment ever leaving for service). Count 94 / 7 / 4 / 5.
2. `DIWAI-PE-MP-001` (Physical and Media Protection Policy), Authorized Removal: equipment repair off site stated as **not used**; failed storage media is not returned to a vendor or any third party; if that changes, the equipment is sanitized first and logged. Dated change note; version unchanged.

## 3. Limits

- The determination rests on the owner's statement and a policy. It is not technically enforced: nothing stops a drive being sent back under a warranty. The trigger and the policy line are the control.
- Failed storage media still has to be sanitized or destroyed when it is retired. That is 3.8.3 and stays open.

## 4. Rollback

Restore `DIWAI-APP-001` and the policy from `*.bak-20261023-offsite`.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — statement and approval 2026-10-23 |
