> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — DASHBOARD REPEATED TEXT FIXED; CONSOLE MFA GAP SHOWN
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-55** |
| **Date** | October 26, 2026 |
| **Status** | **IMPLEMENTED. Owner reported the fault and asked for the gap line (2026-10-26).** |
| **System** | Services VM, `dashboard-refresh` generator and the compliance page |
| **Addresses** | Accuracy of the compliance dashboard; 3.5.3 [b] shown as an open gap |

## 1. The fault

A patch added on 2026-10-24 (`DIWAI-CR-2026-10-41`) rewrote the Mac host TOTP line. Its text pattern joined two alternatives without grouping, so only part of the line was replaced. The unreplaced remainder stayed on the page and each refresh added one more copy. By 2026-10-26 the phrase "active (SSH: key, password and TOTP)" appeared 79 times. My earlier tests checked that the service ran twice without failing and did not read the page.

## 2. The fix

The pattern is grouped (backup `dashboard-refresh.bak-20261026-groupfix`). The damaged item was replaced with one clean line (page backup `compliance.html.bak-20261026-repeat`). Three refreshes in a row leave the page unchanged; no other item repeats.

## 3. Console MFA gap shown (owner request)

The page now carries a warning line, "Console login MFA (Mac and VM consoles) not yet in place — YubiKey pairing planned 2026-10-27", added by an idempotent step (`dashboard-refresh.bak-20261026-cr55`). It is removed when 3.5.3 [b] is closed.

## 4. Lesson

A patch that edits generated output must be tested by reading the output after at least two runs, not only by checking that the service did not fail.
