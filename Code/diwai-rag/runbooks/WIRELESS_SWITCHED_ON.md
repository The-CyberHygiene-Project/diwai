default_repair: none
decisions:
objectives: 3.1.16[a], 3.1.16[b]
user_sees: The Mac's Wi-Fi is switched on.
means: Wi-Fi is a second way into the Mac. It is kept off and saved for emergency recovery when the wired network fails.
evidence: The Mac's wireless is on, and nobody has recorded an emergency that needed it.
repair: No automatic repair. If it was not switched on for an emergency, the owner switches it off and notes when and why it was on.
if_wrong: Switching it off during an emergency can cut off the only working connection.
rollback: Wi-Fi can be switched back on from the Mac's menu bar at any time.
say_no_if: Someone wants to leave it on for convenience. It is kept for emergency recovery only.
---
Status as of 2026-09-15 (DIWAI-ORW-001 B7). `networksetup -getairportpower en1` returned Off, not associated. en1 joins the household network (out of boundary, WPA2/WPA3 Personal). PENDING OWNER DECISION: SSP v2.18 §2.5.2 still describes en1 as active and management-only; worklist B7 proposes recording it as an authorised, normally-disabled break-glass recovery path, naming the access point and the condition for enabling it. This card follows that proposal and must be revisited if the owner decides otherwise. Formerly POA&M-024.
