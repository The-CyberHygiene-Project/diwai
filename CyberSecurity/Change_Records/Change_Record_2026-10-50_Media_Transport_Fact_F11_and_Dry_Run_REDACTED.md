> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MEDIA TRANSPORT: FACT F11 AND A DRY-RUN CUSTODY RECORD
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-50** |
| **Date** | October 24, 2026 |
| **Status** | **RECORDED. Owner confirmed F11 and approved 2026-10-24. No system setting changed.** |
| **System** | Documents only |
| **Addresses** | **3.8.5** |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Changes

- **Fact F11** (owner): no medium containing CUI leaves the controlled area. Added to `DIWAI-APP-001` v1.4, which marks 3.8.5 [b] (accountability during transport) not applicable while F11 holds and withdraws that the day any such medium leaves.
- **SSP Appendix E.19:** access to media (encryption and the locked cabinet) and the procedure if media ever must travel (written authorization, encrypted and locked, custody record of E.7).
- **Dry-run custody record `DIWAI-EV-MP-2026-10-24`:** the E.7 procedure walked through for an imaginary restore-test trip of the Time Machine drive. FileVault was read live on both attached drives (Time Machine volume: Yes, Unlocked; CyberHygiene Project: Yes). **No medium moved.**

## 2. Effect

3.8.5 met: [a] satisfied, [b] not applicable. Strict count 96 → **97/110**; Media Protection 8 of 9. SPRS unchanged.

## 3. Limit

F11 is a statement of fact; an outside assessor may ask for a real custody record. The first real trip would supply it, and the dry run shows the procedure can be done with the controls in place. The drive labels (`DIWAI-M-001`, `-002`) are still to be applied.

## 4. Rollback

Documents only: `.bak-20261024-cr50`.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
