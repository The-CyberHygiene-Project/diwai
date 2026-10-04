default_repair: none
decisions: 4, 10
objectives: 3.10.4
user_sees: The equipment cabinet was opened, but the access log has no entry saying when, by whom, or why.
means: With no entry there is no record of who handled the equipment, and this requirement cannot be counted as met.
evidence: The cabinet is opened often during the working day, and those openings are not being written in the access log.
repair: No automatic repair. Each time the cabinet is opened, write the date, time, name, reason and which system in the log. Once a month, sign the log's monthly statement.
if_wrong: Little harm. Writing an entry that turns out not to matter costs a minute.
rollback: A wrong entry is corrected with a dated note beside it, never by erasing it.
say_no_if: Someone proposes a camera inside the house, or a sensor on the cabinet door, in place of the log. The owner has ruled out both.
---
Status as of 2026-09-24. 3.10.4 is -1 by owner decision (POA&M v1.32, 2026-09-13, under POA&M-027): the rack is opened frequently during active development and openings are not logged. DIWAI-MFR-2026-09-24 declines a reed switch and restates the no-interior-camera rule; 3.10.4 rests on the maintained rack log DIWAI-PE-LOG-001 plus its monthly nil-activity attestation, and a defined procedure scores zero until entries and attestations exist. The rack, not the room, is the logged boundary. The cabinet also houses dc1, a separate boundary, so each entry names the system accessed. Residual risk accepted by the owner: a self-maintained log with no independent corroboration; the premises alarm is disarmed while occupied.
