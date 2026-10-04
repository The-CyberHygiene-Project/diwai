default_repair: none
decisions:
objectives: 3.12.3, 3.3.4[c]
user_sees: Warning emails from the system's self-check are piling up unread in the owner's mailbox.
means: The self-check can spot a failure days before anyone else does, but only if someone reads its warnings.
evidence: The self-check runs every 15 minutes and emails a warning when something fails. Unread warnings mean nobody has looked.
repair: No automatic repair. Read the newest warning first, write down what it says, and tell the owner before deleting anything.
if_wrong: Reading does no harm. Deleting warnings unread can hide the one that mattered.
rollback: Reading changes nothing. A deleted warning can only be recovered from a backup.
say_no_if: Someone proposes switching the warnings off, or filtering them out of sight, because there are too many.
---
Status as of 2026-09-15 (DIWAI-ORW-001 A3; POA&M-067). `diwai-control-health` on the VM runs about 30 checks every 15 minutes; alerts go to root, aliased to [USERNAME], delivered by Dovecot to ~[USERNAME]/Maildir and readable in Roundcube, with a second alert path proven end to end 2026-09-13 and 2026-09-15. POA&M-067 found 93 of 94 unread messages in that mailbox were these alerts (2026-08-02 to 08-07): delivery worked, reading did not. The healthcheck 401 result is a deliberate bad-password probe and means success. The monitor diagnosed the 2026-09-09 portal outage four days before it was found by hand: check it first.
