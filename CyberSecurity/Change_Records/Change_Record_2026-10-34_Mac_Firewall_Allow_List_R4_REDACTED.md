> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MAC FIREWALL ALLOW-LIST FOR THE CUI NETWORK (R4)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-34** |
| **Date** | October 24, 2026 (loaded 17:33); recorded October 25, 2026 |
| **Status** | **IMPLEMENTED AND TESTED. Owner approved 2026-10-24 ("approved, run R4 after 17:30").** |
| **System** | Mac host firewall (`/etc/pf_diwai.conf`, loaded by `org.diwai.pf`) |
| **Addresses** | 3.4.6, 3.4.7 (recovered), 3.1.1 [f] (stays partial) |

## 1. What changed

Step 1 (2026-10-23 17:32) logged all inbound connections on the CUI network and the VM bridge. Step 2 replaced the two "pass everything" rules with an allow-list:

- the services VM may connect to the Mac on TCP 22 and 443; ping from the CUI network; IPv6 neighbour discovery;
- any other connection to the Mac is refused and logged;
- only the VM ([LAN-IP-REDACTED]) and the NAS ([LAN-IP-REDACTED]) are passed through to the internet;
- everything else on those interfaces is blocked and logged.

## 2. Evidence

A 24-hour capture before the change (19,756 connection starts) showed the Mac itself was reached only by the VM: SSH (241), HTTPS (96), DNS (8,098). The rest was traffic passing through to other hosts, plus the NAS's NetBIOS broadcasts and its second address.

## 3. History

The 17:30 run failed because the script could not write the firewall file without sudo (nothing loaded). The first loaded run at 17:30:59 failed two tests that were themselves wrong (they read a successful empty result as a failure) and reverted by itself. After the test fix the third run, 17:33:38, passed all nine tests and the automatic revert was cancelled: ports 22 and 443 open from the VM, another port refused at once, VM DNS fast, VM reaches the internet, Mac reaches the VM (LDAPS, Wazuh agent channel), the NAS, and `cloud.[DOMAIN.ORG]` answers. The blocked-traffic capture began at 17:30:30; the first three minutes of it hold the two tested attempts.

Backup: `/etc/pf_diwai.conf.bak-20261024-1733-r4s2`. Rollback: copy it back and `pfctl -f /etc/pf_diwai.conf`.

## 4. What the overnight blocked-traffic capture shows (8,410 packets)

The Netgear switch's address requests (2,220), the NAS's second address ([LAN-IP-REDACTED]) broadcasting NetBIOS and discovery (967), and the VM's DNS tries to the Mac, refused so that it falls over to its other resolver at once. Nothing else. The VM's first resolver entry is the Mac ([LAN-IP-REDACTED]), which has no DNS service; that is a separate small fix.

## 5. Effect on the requirements

3.4.6 and 3.4.7 are satisfied (assessment rev 1.36; Configuration Management 9 of 9). 3.1.1 [f] stays partial: the allow-list does not control which devices can plug into the switch and talk to the VM or NAS directly. Strict count 99/110; SPRS unchanged.
