> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — NAS PORT 5000 KEPT OPEN; RISK ACCEPTED; NAS BIND FOUND ON LDAPS
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-49** |
| **Date** | October 24, 2026 |
| **Status** | **RECORDED. Owner decision 2026-10-24 (option A). No system setting changed.** |
| **System** | Synology NAS (not changed); documents |
| **Addresses** | **3.13.8**; **3.5.10**; POA&M-066 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Decision

The NAS serves other clients, so its HTTP management port (5000) must stay open, and it requires multifactor authentication for the accounts that use it. The owner's basis, consistent throughout: **the information on the NAS is encrypted and not readable by others.** Option B (a firewall rule limiting port 5000 by network) was offered and not chosen.

## 2. What I checked

- The NAS's directory bind is **already on LDAPS as its own scoped account `svc-nas`**: the directory log shows "SSL connection" and TLS 1.3 for its last connections (read 2026-10-24). The August finding (bind as the directory superuser over cleartext port 389) is closed; the worklist wording was out of date.
- The backup procedures state that the Wazuh alert archives are FIPS-encrypted before transfer and the VM image archive is a LUKS image, and that any writer of CUI to the NAS must encrypt first (`CUI_Backup_Procedures_v2.0.md` §4, §5).
- None of this system's components uses port 5000 (administration uses 5001, files use SMB, NAS SSH is disabled).

## 3. Effect

- **3.13.8:** met (CUI in transmission: nothing reaches the NAS unencrypted). Strict count 94 → **95/110**.
- **3.5.10 [b]:** stays partial. The owner's position covers CUI, not a password: a script that logs in to port 5000 would send a DSM password in the clear on the local network. Recorded as a risk the owner accepts; POA&M-066 stays open on that residual, its 2026-11-30 target withdrawn.
- SSP Appendix E.18 states the decision, the facts above and its limit: the NAS's other shares were not inspected.

## 4. Rollback

Documents only: `.bak-20261024-cr49`.

## 5. Addendum (same day, later): the owner's clarification and a live check

The owner added: scripts do not use port 5000; it is strictly for human access, with multifactor sign-in. I probed the NAS read-only (no login): **port 5000 is plain HTTP** (HTTPS to port 5000 fails), and a browser that opens it is served a page whose script sends it to `https://<NAS>:5001` before any login form, so a person's password goes over HTTPS. The DSM web API on port 5000 still answers in the clear. Consequence: **3.5.10 [b] is now credited** (assessment rev 1.32; strict count 95 → **96/110**), judged on the actual transmissions, all of which are protected; the residual (a deliberately written script could send a password in the clear; none exists) stays accepted under POA&M-066. The SSP statement (Appendix E.18) was corrected to say port 5000 is HTTP with a redirect, not HTTPS.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — decision 2026-10-24 |
