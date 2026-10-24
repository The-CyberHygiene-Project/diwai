> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — THREE READ-ONLY DIAGNOSTIC SCRIPTS MAY BE RUN WITHOUT A SUDO PASSWORD (VM)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-21** |
| **Date** | October 23, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§4). Owner approved 2026-10-23** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Services VM only: `/etc/sudoers.d/zz-diwai-ro`, `/usr/local/libexec/diwai-ro/`. The Mac was not changed |
| **Addresses** | **3.1.5** (least privilege), **3.1.7**, **3.4.3** (change control), **3.3.x** (every use is logged by sudo) |
| **Related** | `DIWAI-CR-2026-10-06` (VM sudo asks for the password; this record makes a deliberate, narrow exception to it) |
| **Authority** | Owner direction 2026-10-23: "let's try the narrower option", after the owner declined to give the AI assistant blanket sudo |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

Each root-only read the assistant needs (a service's rules, a generator's text, a Wazuh alert) cost the owner a pasted command and a transcript round-trip, and several were mis-pasted. `DIWAI-CR-2026-10-06` had removed blanket passwordless sudo, correctly: any process running as the owner, including the assistant, could otherwise act as root. This record keeps that decision and carves out **three read-only scripts**, nothing else.

## 2. Change

| # | What | Detail |
|--:|:---|:---|
| 1 | `/usr/local/libexec/diwai-ro/` | root:root 755; the owner's account cannot add, edit or replace anything in it |
| 2 | `diwai-ro-fapolicyd` | no arguments; prints fapolicyd's mode, trust sources, config check, compiled rules and rule-file list |
| 3 | `diwai-ro-dashboard-src` | no arguments; prints the dashboard generator's text with key file paths masked |
| 4 | `diwai-ro-wazuh-alert <account>` | one argument, checked against `^[A-Za-z0-9_.-]{1,32}$`; prints Wazuh alerts for a `WARNING user=<account>` line (time, rule, level, mail flag, agent, the line) |
| 5 | `/etc/sudoers.d/zz-diwai-ro` (root:root 440) | `Cmnd_Alias DIWAI_RO` listing exactly those three paths (the first two with an empty argument list, which forbids arguments); `[USERNAME] ALL=(root) NOPASSWD: DIWAI_RO`. Named `zz-` so it loads **after** `/etc/sudoers.d/[USERNAME]`: sudo applies the last matching rule |

**Not changed:** `/etc/sudoers.d/[USERNAME]` (password still required for everything else), any other host, any service.

## 3. Security analysis

- **What the exception allows:** any process running as the owner's account can run those three scripts as root without a password. Each only reads and prints. None writes a file, changes a setting or runs a command taken from its input. The fapolicyd and dashboard scripts take no arguments; the alert script validates its one argument and uses it only as a fixed-string search pattern.
- **What it exposes:** the fapolicyd rules (not secret), the dashboard generator's text (key paths masked), and Wazuh alert lines for warning events (account names and idle days). Nothing credential-bearing.
- **Why it cannot be widened by the owner's account:** the scripts and their folder are root-owned and not writable by it; a replacement needs the sudo password.
- **Audit:** sudo logs each use (the journal showed the install test uses).
- **Residual risk:** a future script added to this folder widens the exception. Adding one requires the owner's password and a record here; it must be read-only, argument-free or strictly validated.

## 4. Verification

Installer `scripts/sudoers-ro/vm/diwai-ro-1-install.sh` (owner read the sudoers file and ran it with `sudo`; transcript `~/diwai-ro-install-20261023-112045.log` on the VM): the sudoers file was validated with `visudo` before installation, and then, **as the owner's account**: allowed script runs without a password (**PASS**); an extra argument to a no-argument script is refused (**PASS**); a bad account name is rejected by the script (**PASS**); the dashboard script runs (**PASS**); an unrelated command (`sudo /bin/true`) **still asks for the password** (**PASS**); the owner's account cannot add a file to the folder (**PASS**) or modify a script (**PASS**). 7 of 7. Any failure would have removed everything.
First real use: the assistant read the compiled fapolicyd rules over the owner's session (no password prompt), which cleared an open limit in SSP amendment 28 (SSP amendment 30).

## 5. Rollback

`sudo rm -f /etc/sudoers.d/zz-diwai-ro ; sudo rm -rf /usr/local/libexec/diwai-ro`

## 6. Open items

1. The same exception for the Mac was done on 2026-10-23: `DIWAI-CR-2026-10-22`.
2. Owner signature: done 2026-10-23.

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
