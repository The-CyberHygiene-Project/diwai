> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MAIL-CLIENT PORTS CLOSED ON THE VM
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-59** |
| **Date** | October 26, 2026 |
| **Status** | **IMPLEMENTED AND TESTED. Owner approved 2026-10-26.** |
| **System** | Services VM firewall (`firewalld`, public zone) |
| **Addresses** | 3.5.3 [c], [d] (narrowed; requirement stays partial) |

## 1. What changed

The services IMAPS (993) and SMTPS (465) and the port 587/tcp were removed from the VM firewall zone, runtime first and then permanent. Postfix and Dovecot still listen; the VM's own webmail reaches them on localhost. Port 25 (mail from other servers) and https are unchanged. Backup of the zone file: `/root/public.xml.bak-20261026-0932-cr59`.

## 2. Evidence of use before the change

Fourteen days of mail logs show IMAP logins only from the VM itself (webmail), plus a handful of connection tests from the Mac's own address (mine, during earlier changes). No mail client on the CUI network used these ports.

## 3. Tests (all passed on the second run)

Webmail's own path works (IMAPS and submission on localhost); the webmail page answers on the CUI network; from the Mac, 993, 587 and 465 are refused and 25, 443 and 636 answer; Postfix and Dovecot are active. The first run reverted itself: its command combined two options firewalld does not allow together. The second run applied the change at runtime and passed; the "make permanent" step in the script was killed by my own cleanup command, so I ran it by hand and confirmed the permanent and runtime zones match.

## 4. Effect

No password-only mail-client logins remain on the network. The webmail login is still password-only on the CUI network (owner-accepted for now). 3.5.3 stays partial; strict count 103/110. Rollback: restore the zone file and `firewall-cmd --reload`.
