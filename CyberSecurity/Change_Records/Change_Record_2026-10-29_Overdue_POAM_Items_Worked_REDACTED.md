> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — OVERDUE POA&M ITEMS WORKED (3.12.2)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-29** |
| **Date** | October 23, 2026 |
| **Status** | **§2 to §4 IMPLEMENTED AND VERIFIED. §5 (re-dating of seven items) APPROVED by the owner 2026-10-23 and entered in the POA&M.** |
| **Systems** | services VM; Mac host |
| **Addresses** | **3.12.2** (plans of action are implemented); 3.1.1, 3.4.1, 3.4.6, 3.4.7, 3.5.2, 3.13.1; Rev 3 03.12.02 |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Why

Eleven open POA&M items had passed their Q3 2026 target date with the work not done (060, 061, 062, 063, 064, 066, 068, 069, 058, 050, 052). The assessment held 3.12.2 [b] at partial for that reason. The owner chose to **fix what can be fixed first and re-date the rest** (2026-10-23). Four of the eleven were fixed; seven remain and are proposed for re-dating in §5.

## 2. Changes (owner approved each one separately on 2026-10-23)

| Item | Change | Where | Backup / rollback |
|:---|:---|:---|:---|
| **062** | Retired `49-fido2.conf`, a dead file naming the unpaired YubiKey. Correction to the item text: it carried one live line accepting hardware-key (`sk-ecdsa`) signatures. That algorithm is no longer accepted; ECDSA and RSA keys and the two-factor requirement are unchanged. | VM `/etc/ssh/sshd_config.d/` | `/root/bak-fido2-20261023-1642/49-fido2.conf`; `sudo mv` it back and reload sshd |
| **061** | Added `47-penalty-exempt.conf`: `PerSourcePenaltyExemptList [LAN-IP-REDACTED]` (the Mac, the only administrative source). All other sources stay penalised. | VM `/etc/ssh/sshd_config.d/` | `sudo rm` the file and reload sshd |
| **069** | The sshd PAM stack now loads the TOTP module from root-owned `/usr/local/lib/security/pam_google_authenticator.so` (byte-identical copy, signature valid) instead of the admin-writable Homebrew folder. | Mac `/etc/pam.d/sshd` line 12 | `/etc/pam.d/sshd.bak-20261023-1644`; `sudo cp -p` it back |
| **064** | Method written down and run once (§3). | Procedure, this record | None needed |

Scripts: `~/diwai/scripts/ssh-cleanup/`. Outputs: `~/fido2-removal-20261023.out`, `~/penalty-exempt-20261023.out` (VM), `pam-module-20261023.out`.

**Side effect to remember (069).** A Homebrew upgrade of `google-authenticator-libpam` no longer updates the module sshd uses. After any such upgrade, re-run `scripts/ssh-cleanup/pam-module-rootowned.sh` and confirm with a login.

## 3. Verification

- **062:** `sshd -t` passed; `sshd -T` showed only the `pubkeyacceptedalgorithms` list changing; a fresh connection passed the key stage and reached the TOTP prompt. The full login through a shell was not shown at that step.
- **061:** `sshd -T` shows `persourcepenaltyexemptlist [LAN-IP-REDACTED]` (was `none`). Twelve failed connection attempts from the Mac, then a fresh good connection reached the TOTP stage; no penalty messages in the journal. **Not shown:** the same test before the change.
- **069:** module loads (`dlopen`), signature valid, copy identical. **The owner then logged in to the Mac over SSH (key, password, TOTP) and reached a shell.**
- **064, the method run on 2026-10-23.** Published-service inventory = `pfctl -s nat` **and** `pfctl -sr`, reconciled against listening sockets. Result: 10 redirections (80 and 443 on .145; 1194/udp on .146; 25, 465, 587, 993, 995 and 4190 on .147), all to the VM [LAN-IP-REDACTED], and **exactly 10 matching inbound pass rules on en0 plus ICMP echo**. No pass rule exists for any other port. Mac listeners on wildcard addresses (22, 5000, 7000, 8080, 49165) have no inbound pass rule on en0 and are therefore not published. Inventory and rules agree.

## 4. Risk

Low for 062 and 061. 069 was the highest: a wrong PAM path would have removed Mac SSH. Mitigations were the open session, the backup and the post-change login by the owner. Remaining risk is the stale-copy effect in §2.

## 5. Re-dating of the seven items not fixed (APPROVED by the owner 2026-10-23, dates as listed)

| Item | What it needs | Proposed new target | Why not now |
|:---|:---|:---|:---|
| **066** DSM cleartext API on :5000 | A DSM setting or allow-list | 2026-11-30 | Owner action on the NAS |
| **052** Restoration test (Mac host, Nextcloud) | A real restore of each | 2026-12-31 | VM tier done 2026-08-04; the others need an attended window |
| **050** Backup independence | Off-site copy decision (D-4) | 2026-12-31 | Depends on the off-site decision |
| **063** Abandoned remnants | Examine the five Synology features | 2026-12-31 | Owner action on the NAS |
| **068** Wazuh archive key escrow | Escrow copy off site | 2026-12-31 | Tied to succession item POA&M-049 |
| **060** TOTP token-file write failure | Root-cause the `EACCES` | 2027-01-31 | Cause unknown; compensating: key + password + TOTP |
| **058** Policy set describes ClamAV and a NetGate | Rewrite 6 to 10 of 11 policies | 2027-03-31 | Large document job |

Each date and reason is entered in the POA&M (v1.32 amendment 11). No open item is past its target.

## 6. Open

- 3.12.2 [b] is raised on this basis: four items fixed and verified, seven re-dated with reasons on the owner's approval. **Limit:** re-dating is plan management, not remediation; the seven weaknesses remain open.
- 3.12.3 [a] is a separate objective (POA&M-059, 173 recurring obligations with no execution record) and still blocks Security Assessment from being fully met.

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — §2 changes approved one at a time and §5 dates approved 2026-10-23 |
