> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — ONLYOFFICE DESKTOP EDITORS ADDED TO THE MAC HOST
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-10** |
| **Date opened** | October 6, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§6); owner approval signature pending** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host only |
| **Addresses** | **3.4.3** (change control); **3.4.1** (baseline inventory kept accurate: SBOM v3.13); **3.4.8/3.4.9** (software installed on the system is known and controlled) |
| **Authority** | Owner suggestion 2026-10-06: ONLYOFFICE Desktop as the way to open the Rev 3 measurement register |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

The Rev 3 measurement register (`NIST_800-171r3_Measurement_Register_diwai.xlsx`) is a spreadsheet. The Mac host had no application that opens `.xlsx` files, so the results of the Rev 3 AI scan could not be read or edited there.

## 2. Scope

1. **Installed** ONLYOFFICE Desktop Editors **9.4.0** (Apple Silicon) with `brew install --cask onlyoffice`, into `/Applications/ONLYOFFICE.app`. Homebrew downloaded ONLYOFFICE's own release (`github.com/ONLYOFFICE/DesktopEditors`, v9.4.0, `ONLYOFFICE-arm.dmg`, 542,306,356 bytes) and checked it against the SHA-256 pinned in the cask: `e965be2222609add6b5a70baa2a8cdb599402491fb2925825d9039dcb154beb4`.
2. **Automatic updates turned off:** `defaults write asc.onlyoffice.ONLYOFFICE SUEnableAutomaticChecks -bool false` and `SUAutomaticallyUpdate -bool false`. The cask is flagged `auto_updates`, so without this the app could change itself outside the change process.
3. **No other change.** No configuration, firewall, account or service was touched, and no administrator password was needed.

## 3. Rollback

`brew uninstall --cask onlyoffice`, then delete `~/Library/Preferences/asc.onlyoffice.ONLYOFFICE.plist` and `~/Library/Application Support/asc.onlyoffice.ONLYOFFICE`. The register file is unaffected.

## 4. Execution log

1. Checked the cask before installing: version 9.4.0, flagged `auto_updates`, `/Applications` writable by the admin group.
2. Installed; Homebrew reported success.
3. Verified the app: `codesign` shows Developer ID Application: **Ascensio System SIA (Team 2WH24U26GJ)**; `spctl` reports **accepted, source Notarized Developer ID**; `codesign --verify --deep --strict` passed.
4. Opened the register: all seven sheets (Read Me, Summary, Requirements, ODPs, Objectives, Methods, Withdrawn) display with their formatting.
5. Turned automatic updates off and read the values back.
6. SBOM updated to **v3.13**; the freshness tooling and baseline repointed (backups `.bak-20261006-sbom313`).

## 5. Observations

1. **The app has an "AI" menu** for connecting outside AI services. It is **not configured and must not be used on this host**: it would send content to an outside service. Nothing in the Mac host's AI stack changes.
2. **The vendor is Ascensio System SIA** (Latvia). The app is open source (AGPL-3.0, per the vendor); the owner's non-PRC rule is met.
3. **Updates are now manual.** A new version is a change: check, install through this process, update the SBOM.
4. The app was installed to **open the owner's own register**. It should not be used to open documents from unknown sources.

## 6. Verification

| Check | Result |
|:---|:---|
| Download checksum matches the cask's pinned SHA-256 (checked by Homebrew) | **Pass** |
| Developer ID signature, notarization, signature intact | **Pass** |
| The register opens with all sheets and formatting | **Pass** |
| Automatic update settings both read back as off | **Pass** |
| SBOM v3.13 published; freshness check 0 unsafe | **Pass** |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — \______________________ *(pending)* |
| **Date** | \______________________ |

---

**Distribution:** Limited to authorized personnel
