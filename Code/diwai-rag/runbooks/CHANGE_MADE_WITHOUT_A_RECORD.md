default_repair: none
decisions: 8
objectives: 3.4.3[a], 3.4.3[b], 3.4.3[c], 3.4.3[d]
user_sees: Something on the system was changed, such as a setting, a program or an account, and there is no change record for it.
means: Without a record nobody can tell later what changed, who approved it, or how to undo it.
evidence: A setting, program or account differs from the last recorded state, and no change record explains it.
repair: No automatic repair. Write the change record now: what changed, who approved it, how to undo it, and how it was checked.
if_wrong: If the change was never authorised, recording it as routine can hide a break-in.
rollback: A change record is corrected with a dated amendment. It is never deleted.
say_no_if: Nobody can explain the change. Then treat it as a possible security incident, not as paperwork.
---
Status as of 2026-09-15 (DIWAI-ORW-001 A11). The practice: 34 change records covering 125 discrete changes, each stating authority, rollback and verification, numbered DIWAI-CR-YYYY-MM-NN and filed in Nextcloud Change_Records/. Worklist C1 adds a security-impact field to the template (3.4.4). An unexplained change routes to INCIDENT_NOT_RECORDED.
