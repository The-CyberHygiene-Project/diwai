> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — DOCUMENT GATE ACCEPTED AS ENFORCEMENT; CHANGE AUTHORITY DOCUMENTED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-32** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED (documentation and owner decision). Owner approved 2026-10-23.** |
| **Addresses** | **3.4.3** [a], **3.4.5**; POA&M-048; Rev 3 03.04.03, 03.04.05 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Decision (POA&M-048)

POA&M-048 left one closure condition: either automatic invocation of the freshness check before edits, or a decision to accept manual use. **The owner decided on 2026-10-23 to accept the publish gate plus manual checking as the enforcement.** `doc-freshness.py publish` refuses stale, diverged and unproven-provenance copies. It did so on 2026-10-23, refusing six policy files whose provenance had not been recorded, until it was proven that the originals matched canonical. POA&M-048 is closed.

**Limit recorded:** a direct write into the Nextcloud compliance folder, or an edit through the Nextcloud Text app, bypasses the gate (see also the Text-app corruption finding of 2026-10-23). The gate protects every path that goes through `publish`.

## 2. Document issued

`DIWAI-CMA-001` v1.0, *Change Authority and Administrative Accounts*: approval authority, the restrictions that enforce it, and the verified administrative account inventory (VM `wheel` = `[USERNAME]`; Mac `admin` = `root`, `sysadmin`, `[USERNAME]`).

## 3. Rollback

Reopen POA&M-048; withdraw `DIWAI-CMA-001`. No system was changed.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-23 |
