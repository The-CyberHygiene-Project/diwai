> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# EVIDENCE RECORD — MEDIA SANITIZATION EXERCISE
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-EV-MP-2026-10-23** |
| **Date** | October 23, 2026 (17:49 local) |
| **Supports** | **3.8.3** [a], [b]; `DIWAI-PE-MP-001` section 6 |
| **Run by** | Claude (AI assistant), at the owner's request; script `scripts/media-sanitization-drill.sh`, output `media-sanitization-drill-20261023.out` |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Method

Two **disposable** 8 MB disk images were made in a scratch folder. No real media was touched. A random marker string stood in for CUI. Passphrases were random, held in memory only, and never written or printed.

## 2. Results

| Test | Observation | Result |
|:---|:---|:---|
| 1. Unencrypted image, **clear by overwrite** | Marker found in the raw image **before** (positive control): 1. Found **after** overwriting with random data: **0** | Pass |
| 2. Encrypted image, **cryptographic erase** | Marker absent from the raw encrypted image at rest: 0. Mounts **with** the key (positive control). After the key is destroyed, mounting **without** it is **refused** | Pass |
| Clean-up | Images and scratch files removed; no image attached | Done |

## 3. Limits, stated plainly

- Disposable images, not real media. The two methods used for real media in `DIWAI-PE-MP-001` section 6 (the Mac's *Erase All Content and Settings*, `diskutil eraseDisk` on an external drive) and physical destruction were **not** exercised: they are irreversible and no media is being retired.
- The key destruction in test 2 is the removal of the only copy of the passphrase; it shows the principle (no key, no access), not a hardware key erase.
- No real disposal or reuse has occurred (`DIWAI-MSL-001`).

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved as drafted 2026-10-23 |
