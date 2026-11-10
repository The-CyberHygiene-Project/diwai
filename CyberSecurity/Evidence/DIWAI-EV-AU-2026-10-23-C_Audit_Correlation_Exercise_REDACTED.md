> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# EVIDENCE RECORD — AUDIT CORRELATION EXERCISE
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-EV-AU-2026-10-23-C** |
| **Date** | October 23, 2026 (18:00 local) |
| **Supports** | **3.3.5** [a], [b]; `DIWAI-COR-001` |
| **Run by** | Claude (AI assistant); script `scripts/correlation-exercise.sh`, output `correlation-exercise-20261023.out` |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Method

From the Mac ([LAN-IP-REDACTED]) three SSH logins were attempted to the VM as a **non-existent** user, `nosuch56358c` (a synthetic unauthorized-access event). The event was then traced in each source on the join keys of `DIWAI-COR-001`.

## 2. The chain

| Source | What it shows | Join key |
|:---|:---|:---|
| Mac (origin) | Three outbound connections, 18:00:40 | time, source address [LAN-IP-REDACTED] |
| VM sshd journal | `Invalid user nosuch56358c from [LAN-IP-REDACTED] port 57640`, sshd-session pid **487067** | user, address, **port 57640**, pid |
| VM kernel audit trail | Records of the same connection: `CRYPTO_SESSION` and `CRYPTO_KEY_USER` with pid **487067** and `rport=57640`, 18:00:40 | **pid, remote port**, time |
| Wazuh | Rule **5710**, level 5, "sshd: Attempt to login using a non-existent user", source [LAN-IP-REDACTED], user `nosuch56358c`, three alerts 18:00:40 to 18:00:42 | user, address, time |

One event, four records in three sources, joined by time, address, port, process ID and user name.

## 3. Findings and limits

- **The audit trail does not name the user** for a pre-authentication failure. It ties in by process ID and remote port. This is recorded in `DIWAI-COR-001` §6.
- A first attempt used a slow audit search (`ausearch`) that did not finish; the exercise now reads the log directly. The first run's sshd journal result was the same.
- A synthetic event, not real unauthorized activity.
- The rule fired at level 5, below the level that triggers an immediate review in `DIWAI-COR-001` §3; the exercise tested the joining of records, not the escalation path.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-23 |
