> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — CUI INFORMATION FLOWS STATED (3.1.3)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-57** |
| **Date** | October 26, 2026 |
| **Status** | **RECORDED. Owner approved the approach and E.22 on 2026-10-26. Documents only; no system setting changed.** |
| **Addresses** | 3.1.3 (recovered) |

## 1. What was done

SSP Appendix E.22 now states every CUI flow, who authorises it and what enforces it, using mechanisms that already exist: the Mac firewall allow-list (`DIWAI-CR-2026-10-34`), Nextcloud folder permissions and TOTP, USBGuard, FIPS-encrypted archive transfers, the release rule (E.19, E.20) and the redaction gate. The stale 3.1.3 row in section 4 was replaced.

## 2. Owner-accepted limit

A person authorised to read CUI can copy it out; there is no data-loss-prevention tool, and the Mac itself may reach the internet. The owner judged a DLP product disproportionate for a home-based single-operator office. Owner clarification (same day): CUI by mail is hypothetical (the mail service is available, so a document with CUI could arrive; to be in policy it must be encrypted), and the more common outside route is a Government-approved transfer site such as DoD SAFE. Limiting the Mac's own internet access would also limit permitted uses, so the fix is procedural: CUI leaves only by those routes, with the owner's authorization. E.22 rows 2 and 2A and the limit paragraph say so.

## 3. Effect

3.1.3 satisfied (assessment rev 1.42); Access Control 21 of 22; strict count 103/110; SPRS unchanged.
