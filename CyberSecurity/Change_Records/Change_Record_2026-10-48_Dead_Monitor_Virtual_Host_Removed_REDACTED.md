> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — DEAD `monitor` VIRTUAL HOST REMOVED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-48** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED. Owner approved 2026-10-24.** |
| **System** | services VM: `/etc/httpd/conf.d/diwai.conf` |
| **Addresses** | 3.4.7 (nonessential functions removed), 3.13.3 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Change

The `monitor.[DOMAIN.ORG]` virtual host (LAN only) proxied to `127.0.0.1:3000`, where Grafana ran until its removal on 2026-08-04 (`DIWAI-CR-2026-08-04` §5). Nothing listens on that port, so the virtual host did nothing. It was removed and a comment left in its place. Backups `/root/diwai.conf.bak-20261024-1223-cr48-b` (and `…-cr48`, taken before a first attempt that changed nothing).

## 2. Verification

`apachectl configtest`: Syntax OK; reload succeeded. After the change (tested from the host): `securemac` 401 (login required), `webmail` 200, `wazuh` 302, `ldap` 302, `services` 403, `diwai` 200. A request for `monitor.[DOMAIN.ORG]` is now answered by the default virtual host (200) and no longer proxies anywhere. The name may still be in the public DNS; that is not changed here.

## 3. Rollback

`sudo cp -p /root/diwai.conf.bak-20261024-1223-cr48-b /etc/httpd/conf.d/diwai.conf && sudo systemctl reload httpd`

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
