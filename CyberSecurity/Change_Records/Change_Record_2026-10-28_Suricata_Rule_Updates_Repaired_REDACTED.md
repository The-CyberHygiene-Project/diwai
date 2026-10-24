> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — SURICATA RULE UPDATES REPAIRED (FAILED SILENTLY FOR SIX MONTHS)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-28** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§4). Monitor check 19 DECLINED by the owner (§5). Owner approved the change 2026-10-23.** |
| **System** | services VM (`services.[DOMAIN.ORG]`) |
| **Addresses** | **3.14.4** (update malicious code protection), 3.14.6 (monitoring); Rev 3 03.14.04 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Finding

The nightly job `/usr/local/bin/update-threat-rules.sh` (cron, 03:15) failed on its Suricata step on **90 of its 91 runs** between 2026-04-20 and 2026-10-23. Log line: `suricata-update: command not found` — cron's short PATH did not include `/usr/sbin`. The Suricata rules file therefore stayed at its **2026-04-09** state (about 6½ months stale). YARA updates were working (9 updates and 80 "already current" runs). No check noticed. The SSP stated that Suricata rules "update automatically"; that was **false as written** and is corrected (SSP amendment 44).

A second fault was hidden behind the first: with the path fixed, the update downloaded the new rules but Suricata's own load test rejected them (15 Modbus and DNP3 rules; those protocol parsers are disabled in `suricata.yaml`), and `suricata-update` restored the old rules. The script had logged "OK" as soon as it saw "Writing rules", before that test.

## 2. Changes (all on the VM; backups in `/root/bak-suri-20261023-1507` and `/root/bak-suri2-20261023-1511`)

1. `update-threat-rules.sh`: `suricata-update` called by full path `/usr/sbin/suricata-update`.
2. New `/etc/suricata/disable.conf`: `group:modbus-events.rules`, `group:dnp3-events.rules` (no industrial-control equipment exists here).
3. `update-threat-rules.sh`: success is logged only when `suricata-update` exits 0, prints no `<Error>`, and reports "Writing rules to" or "No changes detected".

## 3. Risk

Six months of new rules can raise alert volume or a failing rule. Mitigation: Suricata reloads rather than restarts, `suricata-update` restores the previous rules if the load test fails, and the previous rules file is backed up.

## 4. Verification (2026-10-23)

Run by hand with cron's own PATH (`env -i PATH=/usr/bin:/bin`): `Suricata: OK — 53254 rules enabled`, service reloaded; rules file rewritten 15:11 (45,991,090 bytes, 53,253 alert rules, was 49,521 on 2026-04-09); `rule reload complete`; Suricata active. **Still to be seen:** the first scheduled run at 03:15 on 2026-10-24 under real cron.

## 5. Open

- **Monitor check 19** (Suricata rules file age and last update result) was proposed. The owner decided on 2026-10-23 **not to add it**. Consequence recorded openly: a repeat of this failure is detected only when someone reads `/var/log/threat-rules-update.log` or the rules file date. The corrected script now logs FAILED honestly, which removes the false-OK cause.
- The first real cron run (2026-10-24 03:15) is the proof; the 3.14.4 determination is made after it.

## 6. Rollback

Restore the files from the two backup directories, remove `/etc/suricata/disable.conf`, `systemctl reload suricata`.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-23 (path fix and disable.conf; monitor check declined) |
