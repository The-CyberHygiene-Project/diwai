> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — TWO READ-ONLY DIAGNOSTIC SCRIPTS MAY BE RUN WITHOUT A SUDO PASSWORD (MAC)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-22** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§4). Owner approved 2026-10-23** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac host only: `/etc/sudoers.d/zz-diwai-ro`, `/usr/local/libexec/diwai-ro/`. The VM is covered by `DIWAI-CR-2026-10-21` |
| **Addresses** | **3.1.5** (least privilege), **3.1.7**, **3.4.3** (change control), **3.13.6** (the firewall's live state can now be read without a password) |
| **Related** | `DIWAI-CR-2026-10-21` (the VM exception, same design) |
| **Authority** | Owner direction 2026-10-23: "let's do the same type of rule for the Mac" |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

Same as `DIWAI-CR-2026-10-21`: root-only reads cost the owner a pasted command each time. On the Mac the two most-needed reads are the live `pf` firewall (rules, counters) and the inactivity job's state.

## 2. Change

| # | What | Detail |
|--:|:---|:---|
| 1 | `/usr/local/libexec/diwai-ro/` | root:wheel 755; the owner's account cannot add, edit or replace anything in it |
| 2 | `diwai-ro-pf` | no arguments; prints pf status, the loaded rules with counters, the `doh_resolvers` table, and the rules file's size and fingerprint |
| 3 | `diwai-ro-inactivity` | no arguments; prints days since each covered account was last seen, the last 12 lines of `/var/log/diwai-inactivity.log`, the installed job's fingerprint and its launchd state |
| 4 | `/etc/sudoers.d/zz-diwai-ro` (root:wheel 440) | `Cmnd_Alias DIWAI_RO` listing exactly those two paths, each with an empty argument list (which forbids arguments); `[USERNAME] ALL=(root) NOPASSWD: DIWAI_RO`. Named `zz-` so it loads after `/etc/sudoers.d/mscp` |

**Not changed:** the main sudoers file, `/etc/sudoers.d/mscp`, every other command (still asks for the password), the VM.

## 3. Security analysis

Same as `DIWAI-CR-2026-10-21` §3. Neither script writes, changes a setting or runs a command from input; neither takes an argument; the folder and scripts are root-owned. What they expose: the firewall rules (the rules file is world-readable), the inactivity log (world-readable) and the job's state file (account names and days since last use). Nothing credential-bearing. Sudo logs every use. Residual risk: a script added later widens the exception; adding one needs the owner's password and a record.

## 4. Verification

Installer `scripts/sudoers-ro/mac/diwai-ro-mac-install.sh` (owner read the sudoers file and ran it with `sudo`; transcript in the session scratchpad, kept with the evidence): sudoers file valid by `visudo` before installation; then, as the owner's account: the `pf` script runs without a password and shows pf Enabled (**PASS**); the inactivity script runs and lists accounts (**PASS**); an extra argument is refused (**PASS**); an unrelated command still asks for the password (**PASS**); the owner's account cannot add a file to the folder (**PASS**) or modify a script (**PASS**). 6 of 6.
**First real use (from the assistant's own session, no password):** the live ruleset shows pf **Enabled**, the four encrypted-DNS block rules from `DIWAI-CR-2026-10-19` §2B loaded (TCP and UDP, ports 443 and 853, to the `doh_resolvers` table), and **no** rule for the removed trial account. This is the first read of the live firewall rather than of its rules file.

## 5. Rollback

`sudo rm -f /etc/sudoers.d/zz-diwai-ro ; sudo rm -rf /usr/local/libexec/diwai-ro`

## 6. Open items

1. Owner signature: done 2026-10-23.

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
