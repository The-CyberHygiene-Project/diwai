default_repair: none
decisions:
objectives: 3.13.5[a], 3.13.5[b]
user_sees: Usually nothing. Webmail, mail and the VPN, which anyone on the internet can reach, run on the same virtual server as the protected records.
means: An attacker who breaks into one of those public services is already on the machine that holds the sign-in directory and the document database.
evidence: The internet-facing services are listed in the security plan, but they are not walled off in a separate network zone of their own.
repair: No automatic repair. This is a planned redesign, due early 2027: move the public services to a separate server in their own walled-off network zone.
if_wrong: Rushing the move can cut off email and remote access until it is finished.
rollback: Nothing on the system is changed by this card. The redesign will carry its own undo plan, written before work starts.
say_no_if: Someone proposes opening any more services to the internet before this separation is finished.
---
Status as of 2026-08-01 (SSP v2.18 §2.5.1; POA&M-023, open, architectural, target 2027 Q1). Published via pf rdr on the Mac host: [WAN-IP-REDACTED] 80/443 webmail, .147 25/465/587/993/995/4190 mail, .146 1194/udp OpenVPN, all to [LAN-IP-REDACTED], the VM that also hosts 389-DS, the Nextcloud MariaDB database and the Wazuh manager. Objective [a] rests on that inventory, but POA&M-064 found the inventory method structurally blind (built from `pfctl -s nat` redirections only; it missed WAN SSH, closed 2026-08-04 by DIWAI-CR-2026-08-14). Re-verify [a] from the pass rules as well as the nat table before claiming it.
