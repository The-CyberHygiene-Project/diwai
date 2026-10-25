> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — SEPARATION DOCUMENTED; 3.1.4 NOT APPLICABLE; 3.1.6 ROLE RULE; STALE GROUP MEMBER REMOVED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-47** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED. Owner approved each item 2026-10-24.** |
| **System** | Documents; one directory group membership (services VM) |
| **Addresses** | **3.13.3** [c]; **3.1.4**; **3.1.6** |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Changes

1. **SSP Appendix E.15 (3.13.3):** how user and management functions are separated, from the live settings: network limits on the management interfaces, the separate administrator and user groups, Cockpit disabled, scoped service accounts, the user repository and the management portal on different hosts. The limit is stated: one person holds both roles.
2. **3.1.4 not applicable (owner option A):** `DIWAI-APP-001` v1.3 and SSP Appendix E.16. Basis: facts F1 and F2, one individual with any access. Compensating controls recorded. Withdrawn the day a second individual is given any access. **Risk, stated:** an outside assessor may not accept not-applicable; it would revert to unmet.
3. **3.1.6 role rule (owner option A):** SSP Appendix E.17 defines the nonsecurity functions; privileged work is by `sudo`, which asks for the password (Mac 5 minutes per terminal, VM 2 minutes, read from `sudo -V` and `/etc/sudoers.d/[USERNAME]` on 2026-10-24). A separate daily account is not claimed.
4. **Directory cleanup:** `uid=drilldbg61ff`, a disposable account from the 2026-10-23 lockout drill whose entry had been deleted, was removed from `cn=cui-users`. `cn=cui-users` now lists only `uid=[USERNAME]`. No other group member lacks an entry (checked across all groups).

## 2. Effect

Assessment revision 1.30; strict count 91 → **94/110**. Access Control 20 of 22; System & Communications Protection 12 of 16. SPRS unchanged.

## 3. Open items

- **3.1.6 caveat:** passwordless `sudo` is in force until 2026-10-26 13:33 (Mac) and 13:36 (VM). The first check that the password rule is back is on 2026-10-26.
- **Found, not changed:** the `monitor` virtual host proxies to a service that is not running; the cleanup of that virtual host needs the owner's approval.
- Cause of item 4: my drill's cleanup deleted the directory entry but not its group membership. The drill script should remove the membership first.

## 4. Rollback

Documents: `.bak-20261024-cr47`. Group member: not worth restoring (the entry does not exist).

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
