> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — NETWORK LOGON WITHOUT A SECOND FACTOR: OWNER-ACCEPTED EXEMPTIONS
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-63** |
| **Date** | October 28, 2026 |
| **Status** | **RECORDED. Owner accepted 2026-10-28.** No system change. |
| **Addresses** | 3.5.3 [c] and [d] |

## 1. What was decided

Webmail (password-only, CUI network only) and three non-interactive VM-to-Mac jobs (key alone, restricted to the VM's address and a forced command) stay as they are. SSP Appendix E.25 states the reason, the residual risk and the conditions for withdrawing the acceptance. The Mac's authorized keys were checked on 2026-10-28: each of the three job keys carries an address restriction and a forced command.

## 2. Effect

3.5.3 is satisfied as a whole ([b] under E.23, [c] and [d] under E.25). Identification and Authentication is 10 of 11. The strict count is 105/110; SPRS is unchanged.
