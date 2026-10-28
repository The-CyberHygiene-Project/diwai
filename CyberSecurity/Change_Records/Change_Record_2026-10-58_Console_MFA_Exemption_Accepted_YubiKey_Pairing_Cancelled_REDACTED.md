> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — CONSOLE MFA EXEMPTION ACCEPTED; YUBIKEY PAIRING CANCELLED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-58** |
| **Date** | October 26, 2026 |
| **Status** | **RECORDED. Owner decision 2026-10-26. Documents and one dashboard line; no system setting changed.** |
| **Addresses** | 3.5.3 [b] (satisfied as an exemption); 3.5.3 stays partial |

## 1. Decision

The owner had thought the YubiKey already protected console login. It is plugged into the Mac but was never paired for login. After looking at what pairing involves, the owner judged it a large and fragile undertaking with a real lockout risk on a rack machine, and cancelled the pairing planned for 2026-10-27. Single-factor console logon on the Mac and the VM is accepted as an exemption (SSP Appendix E.23).

## 2. Reasons recorded

Locked study and rack; the VM runs under the Mac, so its console is reached only from a logged-in Mac session; every network path to a privileged account has a second factor; break-glass exists; the password policy and lockout apply.

## 3. Other points settled the same day

- 3.5.3 [c] and [d] stay open: webmail and mail-client logins are password-only on the CUI network, and two VM-to-Mac jobs authenticate by key alone. The owner prefers pruning stale authenticator entries or reusing an existing mechanism to adding another authenticator code. The owner will remove the one stale phone entry. Webmail two-factor is parked.
- The strict count is unchanged at 103/110; the dashboard line for the console now reads "single-factor, owner-accepted exemption".
