> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — VM DNS RESOLVER ORDER
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-52** |
| **Date** | October 25, 2026 |
| **Status** | **IMPLEMENTED AND TESTED. Owner approved 2026-10-25, on condition that the dashboards in use are not affected.** |
| **System** | Services VM, network connection `enp0s1` |
| **Addresses** | Tidiness of DNS use; no requirement status changes |

## 1. What changed

The VM's first DNS server was the Mac ([LAN-IP-REDACTED]), which has no DNS service and, since R4 (`DIWAI-CR-2026-10-34`), refuses those lookups. Each lookup failed once and then fell over to 1.1.1.1, about 8,000 refused packets a day. The order is now `127.0.0.1` (the VM's own Unbound resolver) then `1.1.1.1`.

## 2. Tests (2026-10-25 08:41, all passed)

Outside and internal names resolve; a lookup takes under 2 seconds; the VM reaches the internet; the directory answers over LDAPS; the admin portal asks for a login; Postfix, Dovecot, Unbound and the Wazuh manager run; the dashboard refresh service runs and the compliance page is served. The first attempt reverted itself because one test compared an IPv6 address; the test, not the resolver, was at fault, and it was corrected.

## 3. Rollback

`nmcli con mod enp0s1 ipv4.dns "[LAN-IP-REDACTED],1.1.1.1"` then `nmcli con up enp0s1`. Previous values saved in `/root/resolver.bak-20261025-0841`.
