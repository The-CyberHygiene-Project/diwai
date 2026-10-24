> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — SERVICE BIND ACCOUNTS SEPARATED FROM THE OWNER'S ACCOUNT
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-38** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§3), including the owner's own sign-in to all three services on 2026-10-23.** |
| **Systems** | services VM (389-DS, Apache, Dovecot); Mac (Nextcloud) |
| **Addresses** | **3.3.2** (actions traceable to individual users), 3.5.10, 3.1.5; POA&M-063 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Finding

`uid=[USERNAME]`, the owner's own account, was also the background bind account for Apache (portal login), Dovecot (webmail) and Nextcloud. The directory log could not tell the owner from those services, and a personal password sat in three service configurations plus a stale Grafana file. A failing service also locked the owner out (three failed binds lock the account).

## 2. Changes (owner approved the fixes 2026-10-23)

| Service | Now binds as | Rollback |
|:---|:---|:---|
| Apache portal | `uid=svc-apache,ou=services,dc=diwai,dc=org` | `/root/bak-svc-apache-20261023-1805` |
| Dovecot webmail | `uid=svc-dovecot,ou=services,dc=diwai,dc=org` | `/root/bak-svc-dovecot-20261023-1805` |
| Nextcloud | `uid=svc-nextcloud,ou=services,dc=diwai,dc=org` | `/var/root/bak-svc-nextcloud-20261023-1809` (root only) |

Each account: read-only access to `ou=people` and group membership only (one access rule each, modelled on `svc-nas`); **cannot read password hashes; cannot write** (tested: "Insufficient access"); lockout on, password expiry off; a 28-character random password written straight into its one config file and never printed. Also: the personal bind settings were scrubbed from the stale Grafana file (Grafana is not installed); `change-directory-password.sh` no longer touches the service configs (it would have overwritten the new service passwords with the owner's) and now handles only the directory password and the NAS Keychain copy.

## 3. Verification

- Directory result codes after the final reload: `svc-apache`, `svc-dovecot`, `svc-nextcloud` binds all `err=0`; `uid=[USERNAME]` retry count 0.
- Nextcloud: "configuration is valid and the connection could be established"; user check and search succeed.
- Dovecot: user lookup returns the full record; no "binding failed" lines after the fix.
- Apache: an unknown user returns 401 and `svc-apache` binds with `err=0`.
- **Owner's sign-in test (2026-10-23):** the owner signed in to the portal, webmail and Nextcloud and all three worked, which proves the user lookups and the portal group check end to end. (The assistant never handles the owner's password.)

## 4. What went wrong during the change (`DIWAI-INCREG-001` INC-008)

1. **About 2 minutes of failed service binds (18:05 to 18:07).** Stage 0 stored each password with a trailing newline; the configs held it without. The first web test returned 401 in both the working and the failing case, so it could not detect this; the directory's result codes (`err=49`) did.
2. **The owner's account was locked (about 18:07 to 18:09).** The assistant's test logins used the real account name; three counted as failed logins and the directory locked `uid=[USERNAME]`. The retry counters were cleared at about 18:09. Tests now use a made-up user name.
3. A first Nextcloud run rolled itself back because its check used the wrong internal user id (`[USERNAME]`); the restored settings were verified.

## 5. Open

- `diwai-control-health` check 10 still describes "stored by 4 services"; its message should be updated to the single remaining copy (the NAS mount). Not changed: monitor edits are the owner's to approve.
- Backups of the old Apache and Dovecot configs (root-only) still hold the old bind settings. Delete them after a few days of clean operation. Older dated backups in `/etc/dovecot` (for example `dovecot-ldap.conf.ext.bak-20260913-084430`) also hold earlier copies.
- Service-account passwords do not expire; rotate yearly with the key rotation (`DIWAI-SCH-001` A8).

## 6. Rollback

Restore each service's config from its backup and reload that service. The new accounts can stay or be deleted from `ou=services`.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — fixes approved 2026-10-23; the INC-008 events were not approved and are reported here |
