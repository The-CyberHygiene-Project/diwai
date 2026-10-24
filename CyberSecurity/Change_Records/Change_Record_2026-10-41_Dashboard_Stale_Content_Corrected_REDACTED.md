> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — COMPLIANCE DASHBOARD: STALE CONTENT CORRECTED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-41** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§3). Owner approved 2026-10-24.** |
| **System** | services VM: `/usr/local/sbin/dashboard-refresh`, `/var/www/securemac/compliance.html` |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Why

After the 83/110 refresh, the rest of the compliance page was still hand-written text from August or earlier, and contradicted the records. The refresh job did not touch it.

## 2. Changes (made in the generator, so a refresh keeps them)

| Page text | Now |
|---|---|
| "Known lag… a re-walk of the assessment is pending" | "The figures follow the assessment file; its date is in the heading." |
| POA&M badge "134/136 Complete" (hard-coded; disagreed with "21 open / 67") | Derived from the register: **46 of 67 closed** (yellow while any item is open) |
| Formal Risk Assessment "due 2026-04-30" (warning) | Done 2026-08-02, next due 2027-03 (`DIWAI-SCH-001` A2) |
| IR Tabletop "due 2026-06-30" (warning) | Done 2026-08-03, next due 2027-08-03 (`DIWAI-SCH-001` A3) |
| "SecureMac host MFA pending (POA&M-047)" | Active: SSH key, password and TOTP on the Mac (exercised 2026-08-07; re-tested 2026-10-23) |
| Rev 3 "119 requirements" | 97 requirements |
| NAS row "Pending / Not Scanned" (yellow) | "Not scanned" / "By design: encrypted data only" (green), on the owner's statement of 2026-10-24 that the NAS is not scanned and should appear to the Synology as opaque data if everything is done right. That is the design; it is not a scan result. |

## 3. Verification

The refresh job reported each substitution `ok`; the rendered page was read back and each old string is absent and each new one present. The strict card still reads 83/110 and the family table is unchanged. Backups: `/usr/local/sbin/dashboard-refresh.bak-20261024-0944-cr41`, `/var/www/securemac/compliance.html.bak-20261024-cr41`.

## 4. Limits and follow-up

- The two due dates and the Mac MFA line are written into the generator, not derived. They go stale again when the next risk assessment or tabletop is done; update them then (or derive them from the obligations ledger).
- Every substitution in the generator is written to be repeatable: a second refresh matches the already-corrected text. (The first version of the Rev 3 and NAS patches were not, and made the refresh job exit with an error until fixed the same morning.)
- The OpenSCAP "Last Scan 2026-10-18" is the last weekly run; the next is 2026-10-25 02:04.

## 5. Rollback

Copy the two `.bak` files back, then `systemctl start dashboard-refresh.service`.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
