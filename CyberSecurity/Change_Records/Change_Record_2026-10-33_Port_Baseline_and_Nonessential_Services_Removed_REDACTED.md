> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — PORT BASELINE ISSUED; NONESSENTIAL SERVICES REMOVED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-33** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (R1 to R3, R5 to R7). R4 pending.** |
| **Systems** | Mac host; services VM |
| **Addresses** | **3.4.6**, **3.4.7**; Rev 3 03.04.06, 03.04.07 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Changes (owner approved 2026-10-23)

Baseline `DIWAI-PORTS-001` v1.0 (every listener on both hosts with an essential/nonessential decision), and: **R1** AirPlay Receiver off; **R2** stock nginx server on 8080 removed; **R3** `netbiosd` disabled; **R5** dead TCP 4190 redirect and pass rule removed from pf; **R6** Dovecot cleartext 110 and 143 closed and `imap` removed from the firewalld zone; **R7** Wazuh 1514 limited to the Mac and 1515 closed. Detail, evidence and backups: `DIWAI-PORTS-001` §4a.

## 2. Verification

Each change was tested after it was made (listener gone, configuration check passed, dependent service still answering). The control-health monitor ran afterwards: 35 checks, one failing (the known 3.5.6 warning for a test account). Webmail was not logged into by hand; its live setting uses IMAPS (993), which still completes a handshake.

## 3. Risk

Low to medium. Largest: R6 (a client using cleartext IMAP or POP3 would stop; the log shows none) and R7 (a new Wazuh agent cannot enroll until 1515 is opened on purpose).

## 4. Rollback

Each script prints its rollback line; backups are named in `DIWAI-PORTS-001` §4a. Scripts: `~/diwai/ports/`.

## 5. Open

R4 (what the CUI LAN and VM bridge may reach on the Mac) and `rapportd`. 3.4.6 [b] and 3.4.7 [b] stay partial until R4.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-23 |
