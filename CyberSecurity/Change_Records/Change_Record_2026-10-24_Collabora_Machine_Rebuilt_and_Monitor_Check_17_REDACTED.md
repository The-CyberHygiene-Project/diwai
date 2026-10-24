> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — NEXTCLOUD OFFICE (COLLABORA) RESTORED BY REBUILDING ITS PODMAN MACHINE; MONITOR CHECK 17 ADDED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-24** |
| **Date** | October 23, 2026 (the number follows `DIWAI-CR-2026-10-23`) |
| **Status** | **IMPLEMENTED AND VERIFIED (§5). Owner approved 2026-10-23** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac host: the `podman-machine-default` VM that hosts the Collabora container; VM: `/usr/local/sbin/diwai-control-health` |
| **Addresses** | **3.12.3** (monitoring on an ongoing basis), **3.14.6**, **3.4.7** (a service of no use is not left standing), **3.13.2** (least functionality in the rebuilt machine) |
| **Related** | `DIWAI-CR-2026-06-21` (Collabora auto-recovery), `DIWAI-CR-2026-08-05` (pinned image) |
| **Authority** | Owner, 2026-10-23: "yes, fix it and add the monitor check" |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Condition addressed

Nextcloud Office (editing documents in the browser) had been **down for 20 days**. Nextcloud logged a failed fetch of `/hosting/discovery` (HTTP 502) about 24 times a day from 2026-10-10 on (and intermittently since June). **Nothing alerted**: every monitor check asked whether a service was *running*, none asked whether Collabora *answered*.

## 2. Cause

The Collabora container runs inside a small Linux VM, a `podman machine`, on the Mac. That VM's **root filesystem was unreadable**: its console log reads `mount: /sysroot: can't read superblock on /dev/vda4`, after which the guest stops in **emergency mode** waiting for a keypress. It most likely dates from the 2026-09-25 host panic and the unclean restart of 2026-10-03 (the recovery log shows `vfkit exited unexpectedly` on 09-25 and a start that never returned on 10-03). The recovery helper `collabora-ensure.sh` was **stuck for 20 days** waiting on `podman machine start`, which never completed. The damage is **not caused by** the 2026-10-23 patch review.

## 3. Change

| # | Change | Rollback |
|--:|:---|:---|
| 1 | Stopped the recovery agent, the hung start and its `vfkit`; **kept the damaged disk** as `podman-machine-default-arm64.raw.corrupt-20261023` (20 GiB sparse) | none needed; the file is evidence |
| 2 | `podman machine rm`, then `podman machine init --cpus 2 --memory 2048 --disk-size 20 --volume ""` (the same size as before; **no host folders are mounted into the machine**, where the default had mounted `/Users`, `/private` and `/var/folders`, which the container never used) | the old machine cannot be restored (damaged); a new one can be rebuilt the same way |
| 3 | `collabora-ensure.sh` created the container **from the pinned image** (digest checked, no drift), restart policy `unless-stopped` | `podman rm -f collabora-code` |
| 4 | Re-armed the launch agent `org.diwai.podman-machine` | `launchctl bootout gui/$(id -u)/org.diwai.podman-machine` |
| 5 | **Monitor check 17 "Nextcloud Office (Collabora) answers"** added to `diwai-control-health` (now 34 checks): the discovery document through the Mac's nginx must return HTTP 200 and contain `wopi-discovery`; a 502 says the machine is down. Backup `diwai-control-health.bak-20261023-chk17` | `cp -p` the backup over the monitor |

**No data was lost:** Collabora is stateless; the documents live in Nextcloud. The container was recreated from the digest pinned in `~/diwai/etc/collabora-image.pin`.

## 4. Security analysis

Least functionality improves: the rebuilt machine has **no access to the Mac's folders**, so a compromised container could not read them. The pinned image is unchanged (`DIWAI-CR-2026-08-05`); podman is 6.0.2 (the CVE-2026-57231 fix is in 5.8.4 and later). Check 17 adds a monitoring path to the owner's offsite alert (failures are mailed on change of state).

## 5. Verification

| Check | Result |
|:---|:---|
| Machine boots, container up | 60 s after start: discovery **HTTP 200** directly and through the Nextcloud proxy; `/hosting/capabilities` 200 |
| Pinned image | digest matches the pin, no drift line |
| Host mounts in the new machine | none |
| Check 17, all branches (stand-in harness, no live outage caused) | healthy → OK; 502 → FAIL naming the machine; no answer, 200 with a wrong body and a failed `curl` → FAIL |
| Check 17 live | **OK** at 14:00; monitor 34 rows, 1 failure (the unrelated 2026-10-23 Mac warning test) |

## 6. Open items

1. The helper `collabora-ensure.sh` should **time out** a `podman machine start` that does not return, and mail the owner, instead of waiting forever (it hid this for 20 days). Check 17 now covers the alerting.
2. Optional: delete the damaged disk image (`.corrupt-20261023`, up to 20 GiB) after a week.
3. Owner signature: done 2026-10-23.

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
