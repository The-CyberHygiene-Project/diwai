> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — WEBMAIL, MAIL-CLIENT PORTS AND VPN TAKEN OFF THE INTERNET
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-51** |
| **Date** | October 25, 2026 |
| **Status** | **IMPLEMENTED AND TESTED. Owner approved 2026-10-24 (choice B for 3.5.3; VPN off) and again on 2026-10-25 for the rerun.** |
| **System** | Mac host firewall (`/etc/pf_diwai.conf`); services VM (web server, OpenVPN, firewalld) |
| **Addresses** | 3.5.3 (exposure reduced, not met), 3.1.12, 3.1.14, 3.13.5 (unchanged) |

## 1. What changed

- **Mac firewall:** the mail address forwards and accepts only port 25. Ports 465, 587, 993, 995 and the VPN's UDP 1194 are no longer forwarded or accepted from the internet.
- **VM web server:** the `webmail.[DOMAIN.ORG]` virtual host allows only `[LAN-IP-REDACTED]/24` and `127.0.0.1`.
- **VM:** `openvpn-server@diwai` stopped and disabled; 1194/udp removed from the firewall zone. Certificates and configuration stay on the VM.
- **Kept, by owner direction:** webmail and the VPN stay installed as future enabled enhancements. Re-enabling is a recorded reversal (restore the backups, `pfctl -f`, reload the web server, `systemctl enable --now openvpn-server@diwai`).

## 2. History

The first run (2026-10-24 17:46) failed on a script fault: its firewall edit had no permission to write the file. Its own tests undid the VM part, leaving nothing half-applied. The script was fixed and rerun 2026-10-25 07:53. Backups: `/etc/pf_diwai.conf.bak-20261025-0753-cr51`; VM `/root/diwai.conf.bak-20261025-0753-cr51`.

## 3. Tests (2026-10-25 07:53, all passed, automatic revert cancelled)

Webmail answers on the CUI network; IMAP 993 and submission 587 answer on the CUI network; port 25 answers; the admin portal still asks for a login; `cloud.[DOMAIN.ORG]` answers; no firewall rule forwards 465, 587, 993, 995 or 1194; the mail address forwards port 25; the VPN service is off; Postfix and Dovecot run.

**Test from outside:** the owner's phone (Wi-Fi off) could not open `webmail.[DOMAIN.ORG]`: "server cannot be found". The phone gave the same message for `cloud.[DOMAIN.ORG]`, which has no public address, so it was not resolving these names at all. This shows the page is not reachable from that phone, not that the server returned "403 Forbidden". The expected 403 was not observed.

## 4. Effect on the requirements

- **3.5.3 stays partial.** Webmail and mail clients still sign in with a password alone from the CUI network. The internet exposure is gone; the objective needs a second factor or removal of the services.
- **3.13.5 unchanged.** Port 25 mail still ends on the same VM as the directory and the SIEM.
- **3.1.12 and 3.1.14:** there is no remote way in until the VPN is re-enabled.

## 5. Records updated

SSP v2.18 amendment 77 (§2.5.1, 3.1.14, 3.1.15, remote access text); `DIWAI-PORTS-001`; `DIWAI-APP-001` fact F5; `DIWAI-EXT-001` mail row; the dashboard's VPN line (pending).
