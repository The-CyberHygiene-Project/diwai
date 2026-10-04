> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# BACKUP AND RECOVERY PROCEDURES
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-BP-001** |
| **Version** | 2.0 |
| **Date** | August 2, 2026 |
| **Supersedes** | `CUI_Backup_Procedures_v1.0_WITHDRAWN.md` — see §1.1 |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Owner** | [SYSTEM-OWNER], ISSO / System Owner |
| **Classification** | Controlled Unclassified Information (CUI) |
| **Distribution** | Authorized personnel only |
| **Review** | Quarterly, with the SSP |
| **Related** | SSP §5 (Contingency Planning), POA&M-037, `DIWAI-EV-CM-2026-08-02` |

---

## 1. Purpose and scope

This procedure describes how [DOMAIN.ORG] SecureMac data is backed up, encrypted,
retained, verified and restored. It covers the Mac mini host, the
services.[DOMAIN.ORG] VM, and the CUI repository.

### 1.1 Why version 1.0 was withdrawn

Version 1.0 was **not a description of this system.** It was Chapter 29 of the
CyberInABox administrator guide, carried across unmodified: 895 lines specifying
seven `backup-*.sh` scripts that exist on neither host, operating on **Graylog**,
**Elasticsearch** and **FreeIPA** — none of which run here — and backing up a
host called `dc1` to `/datastore/backups/`.

Meanwhile the backups that genuinely protect this system were documented
nowhere. Identified by the citation sweep of 2026-08-02
(`DIWAI-EV-CM-2026-08-02`) and tracked as **POA&M-037**.

Every mechanism below was verified operating on 2026-08-02.

---

## 2. What is backed up

| Asset | Mechanism | Location |
|:---|:---|:---|
| Mac host — full system | Time Machine | SecureMac USB (encrypted) |
| **Nextcloud CUI repository** (`/opt/local/nextcloud/data`) | Time Machine | as above |
| **services.[DOMAIN.ORG] VM** (`diwai-services.utm`, ~30 GB) | Time Machine — confirmed `[Included]` | as above |
| Wazuh alert archives (daily) | FIPS-encrypted push | NAS `Backup/SecureMac/wazuh-alerts/` |
| VM disk image (point-in-time) | On-demand archive | NAS `Backup/SecureMac/archive/` |
| Configuration changes | `.bak` files + change records | in place, and `Compliance/Change_Records/` |

**Not backed up, by design:** the AI model store (`/opt/local/models/`,
re-downloadable), package caches, and `/tmp`.

---

## 3. Mechanism 1 — Time Machine to encrypted USB

**Destination:** `SecureMac`, APFS, **FileVault: Yes** (verified 2026-08-01)
**Mount:** `org.diwai.mount-tm-drive` LaunchAgent
**Schedule:** automatic (`AutoBackup = 1`)
**Capacity:** 466 GB total, 210 GB free (55% used) as at 2026-08-02

This is the only mechanism that captures the **whole** system, including the VM
bundle and the Nextcloud CUI data directory. The VM's own disk is LUKS-encrypted
inside the image, so VM data is doubly protected at rest.

### 3.1 Retention

25 snapshots retained, **2026-06-06 → 2026-08-02**.

Time Machine thins oldest-first automatically when space runs low. On 2026-08-01
the drive had reached 89% and was on course to silently delete the July 16
pre-conference snapshot; the April and May snapshots were deliberately pruned,
recovering 157 GB and taking utilisation to 55%.

**Retention rule:** keep no less than 90 days of history. Before pruning, archive
anything of lasting value with `archive-snapshot.sh` (§5) — thinning is
automatic and gives no warning.

### 3.2 Verification

```
tmutil listbackups -d /Volumes/SecureMac      # snapshot inventory
tmutil latestbackup -d /Volumes/SecureMac     # most recent
diskutil info /Volumes/SecureMac | grep FileVault   # must report Yes
df -h /Volumes/SecureMac                      # keep below ~80%
```

---

## 4. Mechanism 2 — FIPS-encrypted Wazuh alert archive to the NAS

Audit records leave the FIPS boundary encrypted. Four stages, two hosts.

| Stage | Where | Trigger | Action |
|:---|:---|:---|:---|
| 1 | VM | `wazuh-archive.timer`, daily **02:00** | `wazuh-log-archive` collects the previous day's alerts from `/var/ossec/logs/alerts/YYYY/MMM/ossec-alerts-DD.*` and tars them |
| 2 | VM | same run | `openssl enc -aes-256-cbc -pbkdf2 -iter 100000`, key `/etc/wazuh-archive.key` (mode 600, root) |
| 3 | VM → Mac | same run | `scp` over SSH (key `/root/.ssh/id_ecdsa_archive_p256`) to `/Users/[USERNAME]/nas-staging` |
| 4 | Mac | `org.diwai.nas-archive-push`, daily **03:00** | `nas-archive-push` copies to the NAS, **verifies SHA-256, then deletes the local copy** |

**NAS mount:** `org.diwai.mount-nas` LaunchAgent — `RunAtLoad` plus a 30-minute
re-check. Deliberately an Agent rather than a Daemon so it can use the Keychain
entry; **no NAS password is stored on disk anywhere.**

**Destination:** `home` share → `Backup/SecureMac/wazuh-alerts/`

### 4.1 FIPS boundary

The **`.enc` file is the FIPS artifact.** It is produced inside the boundary by
FIPS-validated OpenSSL (AES-256-CBC, PBKDF2/SHA-256, 100 000 iterations) and is
already encrypted before it reaches the NAS.

The Synology's own folder encryption is **not** FIPS 140-2 validated and is
claimed only as defence in depth. This matters because the NAS is **shared
infrastructure**, also connected to the CyberInABox network (POA&M-032) — the
encryption is what makes that acceptable, so it must not be bypassed.

**Any future writer of CUI to the NAS must encrypt before transfer.** The
control is applied by the sender; nothing on the NAS enforces it.

### 4.2 Verification

```
# on the VM
sudo tail /var/log/wazuh-archive.log
# on the Mac
tail ~/Library/Logs/nas-archive-push.log
ls -la /Volumes/home/Backup/SecureMac/wazuh-alerts/
# confirm a file really is encrypted
file <archive>.enc         # -> "openssl enc'd data with salted password"
```

Automated: the control-health check (§7) fails if no archive has shipped in 48
hours, or if archives are backing up in Mac staging.

---

## 5. Mechanism 3 — on-demand VM image archive

For preserving a specific system state beyond Time Machine's thinning.

```
sudo ~/diwai/cert-sync/archive-snapshot.sh <snapshot-date>
```

Mounts the Time Machine snapshot read-only, locates the VM bundle, copies it to
`Backup/SecureMac/archive/<snapshot>/` on the NAS, **verifies by SHA-256 read-back
(default)**, and writes a `MANIFEST.txt` recording the source checksum.

Verify an existing archive independently:

```
sudo ~/diwai/cert-sync/verify-archive.sh <archive-date>
```

**Do not delete a Time Machine snapshot until `verify-archive.sh` passes** — the
manifest checksum is taken from the *source*, so on its own it proves nothing
about what landed on the NAS.

The VM image contains a LUKS-encrypted filesystem, so it is encrypted at rest on
the NAS.

---

## 6. Restoration

### 6.1 Mac host or individual files
Time Machine restore from `/Volumes/SecureMac` (Migration Assistant, or Finder
"Enter Time Machine"). The destination is FileVault-encrypted; unlocking requires
the volume password.

### 6.2 services.[DOMAIN.ORG] VM
Restore `~/Library/Containers/com.utmapp.UTM/Data/Documents/diwai-services.utm`
from Time Machine, **or** copy it back from `Backup/SecureMac/archive/<date>/`.

**The VM will demand its LUKS passphrase at first boot.** It cannot boot
unattended — single keyslot, no TPM2 or clevis enrolment, **no escrow**. Without
that passphrase the image is unrecoverable (POA&M-026).

### 6.3 Wazuh alert archive
```
openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 \
  -pass file:/etc/wazuh-archive.key \
  -in wazuh-alerts-YYYY-MM-DD.tar.gz.enc | tar -xzf -
```
Losing `/etc/wazuh-archive.key` makes every archived alert file unreadable. It
is backed up only as part of the VM image.

### 6.4 Restoration testing
**Not yet performed.** Restoration has never been exercised end to end. Tracked
with the contingency items in the POA&M; a documented restore that has never been
attempted is an assumption, not a control.

---

## 7. Monitoring

`/usr/local/sbin/diwai-control-health` (VM, every 15 minutes) covers backup
health among its 21 checks:

- an encrypted archive has shipped within 48 hours
- Mac staging is draining rather than accumulating
- audit partition headroom
- SIEM and agents running

Alerts take **two independent paths**: syslog (ingested by Wazuh) and local mail
to `[USERNAME]` — because a Wazuh-only alert is worthless when Wazuh is the thing
that failed.

**Why this exists.** Before 2026-08-02 the entire archive pipeline had been
non-functional for months across four independent defects, exiting 0 every day
and logging "No alert files found". Nothing noticed. Backup jobs that report
success while doing nothing are the specific failure this monitoring addresses.

---

## 8. Known limitations and accepted risks

| # | Limitation | Consequence | Tracking |
|:---|:---|:---|:---|
| 1 | **Single Time Machine destination** | Failure of one USB drive loses all snapshot history. No second or off-site copy | Open |
| 2 | **LUKS single keyslot, no escrow** | Passphrase loss makes the VM permanently unrecoverable; also prevents unattended boot | POA&M-026 |
| 3 | **NAS is shared infrastructure** | Ransomware or failure there affects both [DOMAIN.ORG] and CyberInABox backups | POA&M-032 |
| 4 | **Restoration never tested** | Recovery time and completeness are unproven | §6.4 |
| 5 | **Encryption applied by the sender** | A future writer that skips encryption puts plaintext CUI on shared storage; nothing detects it | §4.1 |
| 6 | Archive key stored only inside the VM image | Loss of the VM with the key makes archives unreadable | §6.3 |

---

## 9. Revision history

| Version | Date | Author | Description |
|:---|:---|:---|:---|
| 1.0 | — | — | **WITHDRAWN.** CyberInABox administrator-guide chapter, never adapted: seven non-existent scripts, Graylog/Elasticsearch/FreeIPA, host `dc1`. Described no part of this system |
| **2.0** | **2026-08-02** | **[SYSTEM-OWNER]** | Complete rewrite against the system as it actually operates. Documents the three real mechanisms, the FIPS boundary, retention (following the 2026-08-01 prune), restoration, automated monitoring, and six accepted limitations. Every mechanism verified operating on the date of issue |
