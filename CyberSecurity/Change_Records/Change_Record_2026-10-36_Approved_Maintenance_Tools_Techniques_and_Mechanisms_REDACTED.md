> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — APPROVED MAINTENANCE TOOLS, TECHNIQUES AND MECHANISMS ISSUED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-36** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED (documentation). Owner approved as drafted 2026-10-23.** |
| **Addresses** | **3.7.2**; 3.7.1, 3.7.4, 3.7.5; hand-over of routine maintenance to the local AI |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Change

`DIWAI-MNT-001` v1.0 issued: the approved maintenance tools, techniques and mechanisms, and three tiers for AI assistants (observe; run a pre-approved repair; make an approved change). The local AI works in tiers 1 and 2; moving it up, or adding a repair, needs the owner's written approval. The rules apply equally to the frontier assistant used today.

## 2. Verification

Controls the document relies on were checked on 2026-10-23: `fapolicyd`, `usbguard`, `auditd` active on the VM; Gatekeeper enabled on the Mac; `diwai-repair` installed root-owned with two approved repairs; SSH multifactor authentication refused a valid key without the second factor on both hosts.

## 3. Limits

The scripts directory belongs to the owner's account, not root; an approved script is controlled by its change record. The hardware-key approval of repairs has been used for two repairs and has not yet been exercised by the local AI in routine use.

## 4. Rollback

Withdraw `DIWAI-MNT-001`. No system was changed.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved as drafted 2026-10-23 |
