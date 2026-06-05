# PLAN OF ACTION & MILESTONES (POA&M)

**Version:** 2.11\
**Date:** June 5, 2026\
**Organization:** [SYSTEM-OWNER] LLC dba [ORGANIZATION]\
**System:** [DOMAIN.ORG] SecureMac Reference System\
**Reference:** System Security Plan Version 2.11\
**Classification:** Controlled Unclassified Information (CUI)

---

## Version Alignment Note

This document is versioned at **2.11** to align with the concurrently issued System Security Plan v2.11. This is the **first [DOMAIN.ORG]-specific POA&M**. Prior POA&M documents in the cyberhygiene-docs repository (Unified_POAM_v2.2 through v2.13) tracked the **CyberInABox ([DOMAIN.ORG]) system**, which is an architecturally distinct X86 Linux reference implementation maintained under a separate SSP. Those documents are archived in the CyberInABox documentation set and are not applicable to the [DOMAIN.ORG] SecureMac Reference System.

---

## Executive Summary

**SPRS Score Status:**
- **Current Score:** 98/110 (89.1%) — self-assessed June 5, 2026
- **Target Score:** 110/110 (100%)
- **Primary path to 110/110:** Deploy TOTP MFA on VM (+8 points: 3.5.3 + 3.7.5) + complete risk assessment (+3 points)

**POA&M Summary:**

| Metric | Count |
|--------|-------|
| Total Items | 6 |
| Completed | 0 |
| On Track | 1 |
| Overdue | 1 |
| Planned | 4 |

---

## Section 1: OPEN POA&M Items

### HIGH PRIORITY — SPRS Deficit Items

| POA&M ID | Weakness | NIST Controls | SPRS Impact | Target Date | Priority | Status | POC |
|----------|----------|---------------|-------------|-------------|----------|--------|-----|
| POA&M-004 | TOTP MFA not deployed on services.[DOMAIN.ORG] VM — SSH pubkey only; no second factor | 3.5.3 (IA-2(1), IA-2(2)), 3.7.5 (MA-4) | **-8 points** (3.5.3: -5, 3.7.5: -3) | Q3 2026 | High | PLANNED | Shannon |
| POA&M-005 | First annual risk assessment not conducted | 3.11.1 (RA-3) | **-3 points** | 04/30/2026 | High | **OVERDUE** | Shannon |
| POA&M-006 | IR tabletop exercise not conducted | 3.6.3 (IR-3) | **-1 point** | 06/30/2026 | Medium | ON TRACK | Shannon |
| POA&M-001 | YubiKey PIV smartcard certs unpaired on Mac host — password-only auth | 3.5.3, IA-2(1), IA-5 | (part of 3.5.3 -5) | TBD | High | PLANNED | Shannon |

### MEDIUM PRIORITY — Configuration / Integrity Gaps

| POA&M ID | Weakness | NIST Controls | SPRS Impact | Target Date | Priority | Status | POC |
|----------|----------|---------------|-------------|-------------|----------|--------|-----|
| POA&M-002 | ClamAV daemon inactive on VM; YARA not deployed — no active file-level AV scanner | 3.14.2 (SI-3) | **-1 point** (risk acceptance pending) | Q3 2026 | Medium | PLANNED | Shannon |
| POA&M-003 | mSCP 8 failing rules on Mac host (126/134 — 94%) — remediation pending | 3.4.1 (CM-6) | — | Q3 2026 | Low | PLANNED | Shannon |

---

## Section 2: POA&M Item Details

### POA&M-004 — TOTP MFA on services.[DOMAIN.ORG] VM

**Assessment Finding:** 3.5.3 requires multi-factor authentication for privileged and non-privileged access to systems containing CUI. SSH public key authentication is a single factor (something you have). A second factor (TOTP or equivalent) is required. 3.7.5 requires MFA for remote maintenance sessions — same gap, same fix.

**Current state:**
- VM (services.[DOMAIN.ORG]): SSH pubkey only. No pam_google_authenticator or equivalent configured.
- Mac host (securemac.[DOMAIN.ORG]): Password-only (YubiKey PIV unpaired — see POA&M-001).

**Remediation path (VM):**
1. Install google-authenticator-libpam on services.[DOMAIN.ORG]
2. Configure pam_google_authenticator.so in /etc/pam.d/sshd
3. Set AuthenticationMethods publickey,keyboard-interactive in sshd_config.d/
4. Deploy TOTP via authenticator app (Microsoft Authenticator or equivalent)
5. Verify end-to-end with fallback break-glass access
6. Update SSP 3.5.3 and 3.7.5 to MET
7. Close POA&M-004; update SPRS +8

**Note:** POA&M-001 (YubiKey PIV re-pairing on Mac host) and POA&M-004 (TOTP on VM) together close the 3.5.3 deficit. POA&M-004 addresses the larger SPRS impact and is the higher priority.

---

### POA&M-005 — First Annual Risk Assessment (OVERDUE)

**Assessment Finding:** 3.11.1 requires periodic assessment of risk to organizational operations, assets, and individuals. TCC-RA-001 (Risk Management Policy) is approved and NIST SP 800-30 methodology is established. However, the first formal risk assessment for the [DOMAIN.ORG] system has not been conducted.

**Target was:** April 30, 2026 — **36+ days overdue as of June 5, 2026.**

**Remediation path:**
1. Conduct [DOMAIN.ORG]-specific risk assessment per TCC-RA-001 / NIST SP 800-30
2. Identify and document threat sources, threat events, and vulnerabilities
3. Assess likelihood and impact
4. Document risk register
5. Update POA&M with any newly identified risks
6. Update SPRS +3

---

### POA&M-006 — IR Tabletop Exercise

**Assessment Finding:** 3.6.3 requires testing of incident response capability. TCC-IRP-001 requires an annual tabletop exercise. First exercise for [DOMAIN.ORG] system has not been conducted.

**Target:** June 30, 2026 (25 days remaining as of June 5, 2026).

**Remediation path:**
1. Develop tabletop scenario for [DOMAIN.ORG] threat model (e.g., WAN breach, AI interface compromise, VM ransomware)
2. Execute exercise and document findings
3. Update IRP with lessons learned
4. Update SPRS +1

---

### POA&M-001 — YubiKey PIV Re-Pairing (Mac Host)

**Incident summary:** YubiKey Nano 5C FIPS (SN: [HARDWARE-SERIAL]) was initially configured with PIV certs in slot 9C for macOS CryptoTokenKit two-factor login on the [USERNAME] account. On 2026-04-15, an account lockout occurred because the PIV PIN was unknown after a cert pairing change. Recovery was accomplished via the sysadmin break-glass account (password-only, by design). Both slot 9A and slot 9C certs were unpaired. Host now authenticates via password only.

**Current state:**
- YubiKey hardware present and functional (Nano 5C FIPS, firmware 5.4.3)
- PIV certs present on hardware but unpaired from macOS accounts
- [USERNAME] account: password authentication only
- sysadmin break-glass: password only (by design — no smartcard)

**Remediation path:**
1. Confirm current PIV PIN (candidates in KeePass vault)
2. Regenerate slot 9A cert with correct PIN/touch policies using [DOMAIN.ORG] CA (services.[DOMAIN.ORG])
3. Re-pair slot 9A cert: `sc_auth pair -h <hash> -u [USERNAME]`
4. Test login with smartcard + PIN before enabling enforcement
5. Enable smartcard enforcement after confirmed successful login
6. Update SSP 3.5.3 (Mac host component to MET)

---

### POA&M-002 — ClamAV Daemon / YARA on VM

**Current state:**
- ClamAV 1.4.3 installed on services.[DOMAIN.ORG]; virus database current via clamav-freshclam (running)
- ClamAV daemon (clamd): inactive — not scanning
- YARA: not deployed on [DOMAIN.ORG] VM

**Compensating controls (active):**
- Wazuh FIM with VirusTotal integration (cloud multi-engine scanning on FIM events, operational 2026-05-11)
- Suricata 7.0.13 network IDS (operational)
- fapolicyd application whitelisting (operational)
- XProtect + MRT on Mac host (Apple native AV, always active)

**Risk acceptance pending:** Formal risk acceptance document to be completed covering the ClamAV daemon inactive gap on the VM, citing compensating controls above.

**Remediation path (preferred):**
1. Verify if ClamAV daemon can run in FIPS mode on Rocky Linux 9.7 aarch64 (newer version may resolve FIPS incompatibility seen on CyberInABox x86_64)
2. If compatible: enable and configure clamd for on-access scanning
3. If FIPS-incompatible: deploy YARA from source (OpenSSL 3.x FIPS-compatible build) + Wazuh active response integration
4. Complete formal risk acceptance document regardless
5. Update SPRS +1 upon resolution

---

### POA&M-003 — mSCP 8 Failing Rules (Mac Host)

**Current state:** Mac host mSCP scan score: 126/134 (94%). 8 rules failing remediation.

**Note:** The specific failing rules have not yet been individually reviewed. Remediation scripts to be developed per mSCP tooling. No direct SPRS impact — these are configuration hardening items, not 800-171 requirement gaps. Tracking for configuration baseline completeness.

**Remediation path:**
1. Run mSCP report to identify the 8 specific failing rules
2. Review each rule for applicability and remediation approach
3. Apply fixes or document justified exceptions per TCC-CMP-001
4. Target: 134/134 or documented exception for each failing rule

---

## SPRS Impact Summary

### Remaining Deficits (as of June 5, 2026)

| POA&M ID | Req ID | Control Description | Weight | Target | Status |
|----------|--------|---------------------|--------|--------|--------|
| POA&M-004 | 3.5.3 | Multi-Factor Authentication | -5 | Q3 2026 | PLANNED |
| POA&M-004 | 3.7.5 | MFA for Remote Maintenance | -3 | Q3 2026 | PLANNED |
| POA&M-005 | 3.11.1 | Periodic Risk Assessment | -3 | OVERDUE | OVERDUE |
| POA&M-006 | 3.6.3 | IR Testing (Tabletop) | -1 | 06/30/2026 | ON TRACK |
| POA&M-002 | 3.14.2 | Malware Protection (VM) | -1 | Q3 2026 | PLANNED (risk accept) |
| **TOTAL** | | | **-13** | | |

**Current SPRS:** 98/110 (89.1%) — with 3.14.2 risk accepted under compensating controls\
**Target SPRS:** 110/110 (100%)

### Path to 110/110

| Step | Action | SPRS Recovery | Cumulative |
|------|--------|---------------|------------|
| 1 | Deploy TOTP MFA on VM (POA&M-004) | +8 | 106/110 |
| 2 | Complete risk assessment (POA&M-005) | +3 | 109/110 |
| 3 | Conduct IR tabletop (POA&M-006) | +1 | 110/110 |
| 4 | Resolve ClamAV/YARA gap (POA&M-002) | +1 (if not risk-accepted) | 110/110 |

---

## Completion Trend

| Date | Total Items | Completed | % Complete | Notes |
|------|-------------|-----------|------------|-------|
| 06/05/2026 | 6 | 0 | 0% | Initial [DOMAIN.ORG] POA&M. System self-assessed at 98/110. Prior POAM documents (v2.12, v2.13) tracked the CyberInABox system and are not applicable to [DOMAIN.ORG]. |
| Target Q3 2026 | 6 | 4 | 67% | TOTP MFA + mSCP + ClamAV/YARA target. Projected SPRS: 106/110 |
| Target Q4 2026 | 6 | 6 | 100% | Risk assessment + IR testing complete. Projected SPRS: 110/110 |

---

## Evidence Storage

All POA&M evidence stored in:
- **Compliance scans:** https://securemac.[DOMAIN.ORG] (LDAP-authenticated dashboard)
- **VM OpenSCAP reports:** /var/www/securemac/docs/evidence/ (services.[DOMAIN.ORG])
- **Mac mSCP reports:** /var/www/securemac/docs/evidence/mSCP-securemac-latest.html
- **Policies:** CyberSecurity/Current/Policies/ (cyberhygiene-docs repository)
- **Training records:** TCC-SAT-RECORD-FY2026

---

## Review Schedule

- **Quarterly POA&M Review:** March, June, September, December
- **Last Review:** June 5, 2026 (initial — document creation)
- **Next Review:** September 30, 2026
- **POA&M Owner:** [SYSTEM-OWNER], ISSO

---

## Document Control

**Classification:** Controlled Unclassified Information (CUI)\
**Owner:** [SYSTEM-OWNER], ISSO\
**Distribution:** Owner/ISSO, Authorized Auditors, C3PAO Assessors

### Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 2.11 | 06/05/2026 | [SYSTEM-OWNER] | Initial [DOMAIN.ORG] POA&M. Version aligned with SSP v2.11. This document supersedes no prior [DOMAIN.ORG] POA&M — prior POAM documents in the cyberhygiene-docs repository (v2.2 through v2.13) tracked the CyberInABox ([DOMAIN.ORG]) system and are not applicable here. 6 items identified. SPRS self-assessed: 98/110 (89.1%). |

---

*END OF [DOMAIN.ORG] UNIFIED POA&M v2.11*
