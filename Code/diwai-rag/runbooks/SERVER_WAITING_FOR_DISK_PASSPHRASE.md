default_repair: none
decisions:
objectives: 3.13.10[b]
user_sees: Webmail and the document store are down, and the virtual server's window is asking for a passphrase.
means: The server's disk is locked to protect the records on it. Nothing on it runs until the passphrase is typed in.
evidence: The virtual server has restarted, so its disk is locked again. This is expected after every restart.
repair: No automatic repair. The owner types the passphrase into the server's window. If the owner is away, follow the owner's written emergency instructions.
if_wrong: If the server is stuck for some other reason, typing the passphrase will not help. Call the owner.
rollback: Unlocking changes nothing on the disk. Restarting the server locks it again.
say_no_if: Someone proposes storing the passphrase on the computer so the server unlocks itself. That would leave the records unprotected.
---
Status as of 2026-08-24 (VM boot behaviour) and POA&M v1.32 (POA&M-026). The VM halts at the LUKS prompt on every boot and can never recover unattended; `utmctl status` reports "started" while it is blocked at the prompt, so check the UTM console window. Alert a human; never automate restarts or unlocks. POA&M-026: single keyslot, no escrow; partially remediated 2026-08-04 (passphrase sealed off-system, still co-located with the rack; see DIWAI-INV-PAD-001 item 7); target Q4 2026. Crash recovery path if the boot itself fails: Rocky ISO rescue (2026-09-25 record).
