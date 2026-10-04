default_repair: none
decisions:
objectives: 3.10.5[a], 3.10.5[b], 3.10.5[c]
user_sees: The list of keys, codes and passwords that open the office, the cabinet and the alarm still has blank entries.
means: Without a complete list nobody can tell whether a key is missing, and a successor would not know what exists.
evidence: The list is still a draft. Counts, storage places and change dates are blank for most items.
repair: No automatic repair. The owner fills in each blank, writing "unknown" rather than guessing, then signs and dates the list.
if_wrong: A guessed count makes a missing key impossible to notice.
rollback: A wrong entry is corrected with a dated note beside it.
say_no_if: Someone proposes writing the codes or passwords themselves into the list. It records who holds each one, never the secret.
---
Status as of 2026-08-04: DIWAI-INV-PAD-001 v0.1 DRAFT, awaiting owner completion (closes F-2026-08-28; DIWAI-ORW-001 C3). Nine items: rack door key, study door key, residence keys, DSC alarm user codes, alarm installer/master code (custodian unconfirmed: owner or the installer), Reolink NVR credentials, sealed LUKS passphrase envelope, IronKey D500S, sysadmin break-glass credential. Item 7 is protected by item 1. Sole custody by the owner is also a continuity risk (POA&M-049).
