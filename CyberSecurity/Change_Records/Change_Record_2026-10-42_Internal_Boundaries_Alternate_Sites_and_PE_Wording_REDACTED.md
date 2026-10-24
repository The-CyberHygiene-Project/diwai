> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — INTERNAL BOUNDARIES DEFINED; ALTERNATE SITES; PHYSICAL PROTECTION WORDING
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-42** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED. Owner approved each item 2026-10-24.** |
| **System** | Documents only; no system setting changed |
| **Addresses** | **3.13.1** [b]; **3.10.6** [b]; **3.10.2** [b]; the owner's authorization wording in the Physical and Media Protection policy |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Changes

1. **SSP §2.5.3 added (3.13.1 [b]).** Five key internal boundaries and the control at each: the internet edge, the household network, the CUI network, host to VM, and shared storage. Read from the live `pf` and `firewalld` rules on 2026-10-24. It states two known gaps: the CUI network is open inside the Mac until the port baseline R4 is loaded, and the shared NAS depends on POA&M-032.
2. **Alternate work sites (3.10.6 [b]).** The owner stated that CUI is not handled anywhere other than the controlled rack site. SSP Appendix E.7 records the statement; [b] is Not applicable on that reason. The safeguards stay defined for a change.
3. **Support infrastructure (3.10.2 [b]).** The owner decided that connecting the UPS to a monitor is not practical and that the monthly observation (`DIWAI-SCH-001` M7) is the correct mode. The Physical and Media Protection policy now says so.
4. [PERSONNEL-SCREENING-NOTE-REDACTED]

## 2. Effect

Assessment revision 1.23; strict count 83 → **86/110**; Physical Protection 4 of 6, System & Communications Protection 10 of 16. SPRS unchanged.

## 3. Backup-media wording (added the same day, owner approved)

The policy's media list named "ReaR ISO images" (none exist) and "LUKS-encrypted" external backup drives. It now names the Time Machine drive (FileVault, APFS), the encrypted alert archive on the NAS and the on-demand VM image archives, and points to `CUI_Backup_Procedures_v2.0.md`.

## 4. Rollback

Backups `.bak-20261024-cr42` and `.bak-20261024-rear` (policy) and `.bak-20261024-am62` (SSP).

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
