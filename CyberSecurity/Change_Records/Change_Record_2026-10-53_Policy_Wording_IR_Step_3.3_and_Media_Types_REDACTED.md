> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — POLICY WORDING: IR STEP 3.3 AND MEDIA TYPES
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-53** |
| **Date** | October 25, 2026 |
| **Status** | **RECORDED. Owner approved the wording 2026-10-25. Documents only; no system setting changed.** |
| **Addresses** | Accuracy of the Incident Response and Physical and Media Protection policies; no requirement status changes |

## 1. Incident Response Policy, Step 3.3

The post-recovery check ran `sudo ipactl status`, a FreeIPA command that is not installed here. It now runs `sudo systemctl status dirsrv@diwai`; that unit is active on the VM (checked 2026-10-25).

## 2. Physical and Media Protection Policy, media types

| Was | Now |
|---|---|
| Digital media encrypted (LUKS) | FileVault on the Mac and the backup drive, LUKS2 on the VM, folder encryption on the NAS |
| RAID array with LUKS-encrypted volumes | Synology 8-bay NAS with folder-level AES-256 encryption (not FIPS-validated; VM data arrives pre-encrypted by FIPS-validated OpenSSL; SSP Component 3) |
| Backup USB drives, LUKS-encrypted | The Time Machine SSD, FileVault-encrypted, stored in the locked rack or locked safe |

The existing note that offsite rotation is not in effect (POA&M-050) is unchanged. Policy versions are unchanged.
