> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — DETECTION COVERAGE STATEMENT AND MOBILE-CODE POLICY ADOPTED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-44** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED. Owner approved both documents 2026-10-24.** |
| **System** | Documents only; no system setting changed |
| **Addresses** | **3.6.1**; **3.13.13** (in part) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Adopted

- **`DIWAI-DET-001` v1.0, Detection Coverage Statement** (Incident_Response folder): what is watched, how the owner finds out, where detection failed in INC-003 to INC-008 and what covers each now, six blind spots, and the standing question for any event that no control found. Two entries are marked *(to be confirmed)* (how the 2026-09-25 host crash was noticed; whether the NAS is monitored).
- **`DIWAI-MCP-001` v1.0, Mobile Code Policy** (Policies folder): acceptable categories, prohibited plug-ins, macros disabled, extensions listed, how it is controlled and monitored. Three entries are marked *(to be confirmed)*: the macro setting in the editors, browser extensions, and that CUI is not handled in a browser profile used for other browsing.

## 2. Effect

- **3.6.1** re-determined SATISFIED (assessment rev 1.27); strict count 89 → **90/110**; Incident Response 3 of 3.
- **3.13.13** not re-determined: [a] waits for the owner's confirmation of the three entries; [b] (monitoring) stays partial, because scripts running in the browser and content-security-policy violations are not collected.

## 3. Rollback

Remove the two documents from the canonical folders; revert the assessment and SSP from `.bak-20261024-cr44`.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
