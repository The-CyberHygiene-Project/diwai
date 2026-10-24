> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MEDIA SANITIZATION (MP-6) REWRITTEN; LOG OPENED; ANNUAL EXERCISE ADDED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-37** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED (documentation and exercise). Owner approved as drafted 2026-10-23.** |
| **Addresses** | **3.8.3**; Rev 3 03.08.03 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Finding

The sanitization section of `DIWAI-PE-MP-001` described another system (`/dev/sdX`, `shred`, a `/backup` log path). Overwriting is not valid for solid-state storage, and no sanitization log existed.

## 2. Changes

1. **Policy section 6 (MP-6) rewritten** for the media in use: Mac SSD (FileVault erase), VM disk image (LUKS; delete every copy and destroy the passphrase record), external encrypted drives (erase the whole drive), IronKey, NAS disks (key destruction if confirmed encrypted, otherwise physical destruction), paper, and physical destruction for anything that cannot be erased. Failed media never goes to a third party (`DIWAI-APP-001` F10). Dated change note; version unchanged. Backup `*.bak-20261023-mp6`.
2. **`DIWAI-MSL-001`** Media Sanitization Log opened; it states that there have been no real disposals.
3. **`DIWAI-SCH-001` v1.1:** obligation **A13**, an annual run of the sanitization exercise (a new commitment, approved by the owner).
4. **Exercise** on two disposable images with positive controls: passed (`DIWAI-EV-MP-2026-10-23`).

## 3. Limits

The Mac erase, the external-drive erase and physical destruction were not exercised (irreversible; no media is being retired). Whether the NAS volume is encrypted is not established; the policy covers both cases.

## 4. Rollback

Restore the policy from its backup; withdraw `DIWAI-MSL-001`; remove A13. No system was changed.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved as drafted 2026-10-23 |
