default_repair: none
decisions: 2
objectives: 3.5.6[a], 3.5.6[b]
user_sees: Usually nothing. An account nobody has used for 90 days still lets someone sign in.
means: A forgotten or leaked account stays open, so someone could sign in with it without being noticed.
evidence: The central sign-in directory locks accounts unused for 90 days. Accounts kept on the Mac itself and on the virtual server have no such limit.
repair: No automatic repair. The owner reviews the accounts on the Mac and on the virtual server by hand and turns off any not used in 90 days.
if_wrong: Turning off the emergency spare administrator account, or the owner's own account, can leave nobody able to sign in and fix things.
rollback: An administrator can turn a disabled account back on. If no administrator account still works, it cannot be undone this way.
say_no_if: Someone proposes locking every account that has no recorded sign-in. Until every account has one, that can lock out the owner.
---
Status as of 2026-09-13 (DIWAI-CR-2026-09-08); recheck before ISSO approval. SSP E.4 defines the 90-day period, so objective [a] is met. The 389-DS account-policy plugin enforces it for directory accounts using lastLoginTime, which refreshes on each login; enforcement was proven by a refused login. Mac local accounts and VM local accounts are not enforced, so [b] is not met and 3.5.6 is withheld (POA&M-076). Do not add a createTimestamp fallback to the account policy until every account has a lastLoginTime: accounts without one would lock at once. The break-glass account `sysadmin` must stay exempt.
