# SYSTEM SECURITY PLAN

## NIST SP 800-171 Rev 2 Compliance

[SYSTEM-OWNER] LLC dba [ORGANIZATION]\
System Name: CyberHygiene Production Network\
Domain: [DOMAIN.ORG]\
Version 2.10 Date: May 15, 2026\
Classification: CONFIDENTIAL BUSINESS INFORMATION

**Distribution Notice:** This document contains proprietary business information, trade secrets, and confidential system security details of [SYSTEM-OWNER] LLC. Unauthorized disclosure may cause competitive harm. Upon submission to U.S. Government agencies, this document shall be marked and protected as Controlled Unclassified Information (CUI) per 32 CFR Part 2002.

## DOCUMENT CONTROL

**Document Status:** Approved - Operational\
**Security Classification:** CONTROLLED UNCLASSIFIED INFORMATION (CUI)\
**Distribution:** Limited to authorized personnel only

<table style="width:83%;">
<colgroup>
<col style="width: 33%" />
<col style="width: 15%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name / Title</th>
<th style="text-align: left;">Role</th>
<th style="text-align: left;">Signature / Date</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">[SYSTEM-OWNER], Owner/Principal</td>
<td style="text-align: left;">System Owner</td>
<td style="text-align: left;">[SYSTEM-OWNER] _____<br />
Date: 05/15/2026</td>
</tr>
<tr>
<td style="text-align: left;">[SYSTEM-OWNER], Owner/Principal</td>
<td style="text-align: left;">ISSO</td>
<td style="text-align: left;">[SYSTEM-OWNER] _____<br />
Date: 05/15/2026</td>
</tr>
</tbody>
</table>


**Review Schedule:** Quarterly or upon significant system changes **Next Review Date:** July 31, 2026

### Document Revision History

| Version | Date       | Author         | Description                                                  |
| :------ | :--------- | :------------- | :----------------------------------------------------------- |
| 1.0     | 10/26/2025 | [SYSTEM-OWNER] | Initial SSP - Implementation Phase                           |
| 1.1     | 10/28/2025 | [SYSTEM-OWNER] | RAID 5 array rebuilt with FIPS-compliant LUKS encryption; GUI/console/SSH login banners implemented; ClamAV antivirus installed and configured; Samba share configured for CUI data |
| 1.2     | 10/28/2025 | [SYSTEM-OWNER] | Wazuh SIEM/XDR v4.9.2 deployed with vulnerability detection, file integrity monitoring, and security configuration assessment; Automated backup system implemented with ReaR for weekly full system backups and daily critical file backups; Implementation status increased to 94% |
| 1.3     | 10/31/2025 | [SYSTEM-OWNER] | YARA 4.5.2 malware detection fully operational: Installed from source with FIPS-compatible OpenSSL 3.2.2; Deployed 25 malware detection rules (generic, Linux, Windows); Integrated with Wazuh active response for automated FIM-triggered scanning; Created 8 custom Wazuh alert rules for malware severity levels; Successfully tested end-to-end detection with EICAR; POA&M-014 advanced to 85% complete; Implementation status increased to 97.6% |
| 1.4     | 11/02/2025 | [SYSTEM-OWNER] | Policy Documentation Package: 6 comprehensive policy documents (TCC-IRP-001, TCC-RA-001, TCC-PS-001, TCC-PE-MP-001, TCC-SI-001, TCC-AUP-001). 50+ controls formally documented across 11 families. Authorization extended to January 1, 2026. |
| 1.5     | 12/02/2025 | [SYSTEM-OWNER] | Added Graylog centralized logging deployment (POA&M-037). Updated AU controls (AU-2, AU-3, AU-6, AU-7, AU-9) and SI-4. Implementation status: 99% complete. |
| 1.6     | 12/26/2025 | [SYSTEM-OWNER] | Added AI server, updated SPRS score (105/110), infrastructure totals, Apple Silicon security controls |
| 1.7     | 01/24/2026 | [SYSTEM-OWNER] | Incorporated YARA malware detection enhancements (Graylog/Grafana integration, 22 detection rules). Added FIPS-compliant Prometheus/Node Exporter monitoring across 6 systems. |
| 1.8     | 01/29/2026 | [SYSTEM-OWNER] | Incorporated AI-assisted administration (SysAdmin Agent Dashboard, Code Assistant) with TLS encryption. |
| 1.9     | 01/31/2026 | [SYSTEM-OWNER] | CRITICAL CORRECTIONS: Removed incorrect RAID 5 references (storage is LVM+LUKS on single SSD). Updated mail server status to operational (Postfix 3.5.25, Dovecot 2.3.16). Added SysAdmin Agent Dashboard v2.0 with Explainable AI. |
| 2.0     | 02/03/2026 | [SYSTEM-OWNER] | CRITICAL SYNCHRONIZATION UPDATE: Aligned with POA&M v2.3. Corrected malware protection section. Added OpenClaw AI Security Architecture. Integrated 8 AI POA&M items (POA&M-036 through POA&M-043). |
| 2.1     | 02/11/2026 | [SYSTEM-OWNER] | SPRS score revised from 107 to 88 per independent CMMC L2 Preliminary Gap Analysis (02/09/2026). Section 10 POA&M updated with 10 NOT MET requirements (-22 points total). |
| 2.2     | 02/11/2026 | [SYSTEM-OWNER] | VirusTotal integration status updated to operational. Wazuh integratord configured with rate-limit retry/backoff. |
| 2.3     | 02/15/2026 | [SYSTEM-OWNER] | CMMC GAP ANALYSIS REMEDIATION: 5 DRAFT policies formally approved (AU, CM, AT, IA, SC). Technical controls implemented on dc1: USBGuard (3.8.7), GNOME session lock (3.1.10), login banners (3.1.9). SPRS corrected to 88/110. |
| 2.4     | 02/17/2026 | [SYSTEM-OWNER] | SECURITY CONTROL ASSESSMENT PROGRAM: 3.12.1 (CA-2) status changed to MET. Centralized OpenSCAP CUI profile assessment deployed across all 4 CPN systems. Training controls (3.2.1, 3.2.2, 3.2.3) updated to MET. SPRS updated to 101/110 (+13 points). |
| 2.5     | 02/21/2026 | [SYSTEM-OWNER] | AI SERVER CONFIGURATION UPDATE: Ollama inference server reconfigured to listen on all interfaces. Default model changed to codellama:34b. No SPRS impact. |
| 2.6     | 02/21/2026 | [SYSTEM-OWNER] | VIRUSTOTAL INTEGRATION TUNING: Alert threshold raised 7→10. MD5 hash deduplication cache and daily quota guard (490/day) added. No SPRS impact. |
| 2.7     | 02/21/2026 | [SYSTEM-OWNER] | ACCOUNTING WORKSTATION DEPLOYMENT COMPLETE: All 4 CPN systems now fully hardened with CMMC controls. No SPRS impact. |
| 2.8     | 02/21/2026 | [SYSTEM-OWNER] | ADMIN METHOD SWITCHOVER + FULL OPENSCAP COMPLIANCE: Remote administration changed from direct root SSH to named-user [USERNAME] with NOPASSWD sudo. All 4 CPN systems now 100% OpenSCAP CUI compliant (104/104). |
| 2.9     | 02/21/2026 | [SYSTEM-OWNER] | MFA DEPLOYMENT COMPLETE: SSH publickey + TOTP (pam_google_authenticator) deployed on all 4 CPN systems. 3.5.3 status: MET. SPRS improved 101/110 → 106/110 (+5 points). POA&M reference: v2.11. |
| 2.10    | 05/15/2026 | [SYSTEM-OWNER] | **SECUREMAC INFRASTRUCTURE HARDENING:** nginx 1.31.0 reverse proxy deployed via LaunchDaemon; ai.[DOMAIN.ORG] HTTPS endpoint on LAN interface ([LAN-IP-REDACTED]:443) with *.[DOMAIN.ORG] wildcard cert. Open Web UI upgraded 0.8.12→0.9.5, bound to 127.0.0.1:3000. macOS version corrected to 26.5 (Tahoe). USB Guard re-enabled (mode: on). Time Machine auto-mount LaunchAgent deployed (root cause of 17-day backup gap resolved). YubiKey PIV lockout incident: smartcard certs unpaired; sysadmin break-glass used for recovery; POA&M-046 opened. SPRS unchanged: 106/110. POA&M reference: v2.12. |

## EXECUTIVE SUMMARY

### 1.1 Purpose

This System Security Plan (SSP) documents the security controls implemented for [ORGANIZATION]'s production network environment that processes, stores, and transmits Controlled Unclassified Information (CUI) and Federal Contract Information (FCI). This SSP demonstrates compliance with NIST SP 800-171 Rev 2 requirements as mandated by FAR 52.204-21 and supports Cybersecurity Maturity Model Certification (CMMC) Level 1 and Level 2 certification readiness.

### 1.2 System Overview

The CyberHygiene Production Network ([DOMAIN.ORG]) is a Microsoft-free, open-source infrastructure built on Rocky Linux 9.7 to provide secure identity management, file storage, email services, and client workstation management for [ORGANIZATION]'s government contracting operations. The SecureMac host (ai.[DOMAIN.ORG], Mac Mini M4 Pro running macOS 26.5 Tahoe) provides AI/ML inference, nginx reverse proxy, and serves as the management workstation for the CyberInABox reference system.

Current Implementation Status: 96.4% SPRS Compliance (as of May 15, 2026)\
Compliance Verification: 100% OpenSCAP CUI Profile (104/104 checks passed on all CPN systems)\
SPRS Score: 106/110 (96.4%) per independent assessment — Target: 110/110 by June 30, 2026\
POA&M Reference: Unified_POAM_v2.12 (May 15, 2026)

### 1.3 Compliance Requirements

**Primary Requirements:**

- NIST SP 800-171 Rev 2 - Protecting CUI in Nonfederal Systems
- FIPS 140-2/140-3 - Cryptographic Module Validation
- FAR 52.204-21 - Basic Safeguarding of Covered Contractor Information Systems
- DFARS 252.204-7012 - Safeguarding Covered Defense Information
- CMMC Level 1 - Foundational cybersecurity practices (17 practices)
- CMMC Level 2 - Advanced cybersecurity practices (110 practices)

**Supporting Standards:**

- NIST SP 800-53 Rev 5 - Security and Privacy Controls
- NIST SP 800-171A - Assessing Security Requirements for CUI
- CIS Controls - Center for Internet Security Benchmarks

### 1.4 Key Findings

**Strengths:**

- FIPS 140-2 cryptographic validation active on all Rocky Linux CPN systems
- 100% OpenSCAP CUI compliance on all 4 CPN systems (104/104 rules passing)
- Three production workstations fully deployed and hardened
- Strong authentication via Kerberos SSO (FreeIPA) + TOTP MFA on all 4 CPN systems
- Comprehensive audit logging to dedicated encrypted partitions
- Wazuh SIEM operational for threat detection and FIM
- Centralized OpenSCAP compliance dashboard with 12-hour automated scans
- nginx reverse proxy deployed on SecureMac host — ai.[DOMAIN.ORG] HTTPS access restricted to LAN only
- USB Guard enabled on SecureMac host (mode: on); Time Machine UUID allowlisted
- Time Machine backup auto-mount resolved (org.diwai.mount-tm-drive LaunchAgent deployed)

**Outstanding Deficits (see Unified_POAM_v2.12):**

- 3.11.1 Periodic Risk Assessment — -3 SPRS points — Target: April 30, 2026 (**OVERDUE** as of June 2026)
- 3.6.3 IR Tabletop Exercise — -1 SPRS point — Target: June 30, 2026
- POA&M-046: YubiKey PIV smartcard re-pairing on SecureMac host (MFA gap — host authenticates password-only; CPN systems unaffected)

### 1.5 Authorization

**Full Authorization Granted:** January 1, 2026\
**Authorization Period:** 3 years (through December 31, 2028)\
**Current SPRS:** 106/110 (96.4%)\
**CMMC Level 2 Conditional Eligibility:** ELIGIBLE (score ≥ 80, no single finding > 5 points)

## 2. SYSTEM IDENTIFICATION

### 2.1 System Information

**System Name:** CyberHygiene Production Network\
**System Acronym:** CPN\
**System Owner:** [SYSTEM-OWNER] LLC dba [ORGANIZATION]\
**System Type:** General Support System (GSS)\
**Operational Status:** Operational (Full Authorization)

### 2.2 Organization Information

**Legal Entity:** [SYSTEM-OWNER] LLC\
**Doing Business As:** [ORGANIZATION]\
**CAGE Code:** [GOVT-ID-REDACTED]\
**DUNS Number:** [GOVT-ID-REDACTED]\
**NAICS Codes:** 541611, 541613, 541690\
**Business Location:** [LOCATION-REDACTED]

### 2.3 Contact Information

**System Owner / ISSO:**\
Name: [SYSTEM-OWNER]\
Title: Owner/Principal\
Email: [EMAIL-REDACTED]\
Phone: [PHONE-REDACTED]\
Security Clearance: Active DoD Top Secret

### 2.4 System Categorization

Based on FIPS 199 Standards for Security Categorization:

**Information Type:** Federal Contract Information (FCI) / Controlled Unclassified Information (CUI)\
**Confidentiality:** MODERATE\
**Integrity:** MODERATE\
**Availability:** LOW\
**Overall System Categorization:** MODERATE

**Rationale:** The system processes and stores government contract information, proposals, cost/pricing data, and other sensitive business information that requires protection from unauthorized disclosure (Confidentiality) and modification (Integrity). Loss of availability would impact business operations but not result in significant harm to government interests.

## 3. SYSTEM DESCRIPTION

### 3.1 System Purpose and Functions

The CyberHygiene Production Network provides secure information technology infrastructure for [ORGANIZATION]'s government contracting business operations.

**Primary Functions:**

- Centralized identity and access management (FreeIPA/LDAP/Kerberos)
- Security monitoring and threat detection (Wazuh SIEM/XDR)
- Multi-layered malware protection (YARA + VirusTotal + Wazuh FIM)
- Vulnerability management and scanning
- File integrity monitoring and alerting
- Automated backup and disaster recovery
- Secure file storage and sharing
- Email communications with encryption
- Client workstation management and authentication
- Document management for proposals and contracts
- Security audit logging and compliance reporting
- Certificate management via internal PKI
- AI/ML inference (SecureMac host, access-restricted via nginx reverse proxy)

**Business Processes Supported:**

- Proposal development and submission
- Contract management and administration
- Project management documentation
- Cost estimating and pricing
- Client communications
- Business development activities
- Records retention and compliance

### 3.2 General System Description

**Architecture:** Client-server architecture with centralized services\
**Primary OS:** Rocky Linux 9.7 (Blue Onyx) — RHEL binary compatible\
**Management Host OS:** macOS 26.5 (Tahoe) — Apple Silicon (M4 Pro)\
**Security Posture:** FIPS 140-2 validated, OpenSCAP hardened, SELinux enforcing (Rocky Linux systems)\
**Network:** Internal LAN ([LAN-IP-REDACTED]/24 — SecureMac LAN; [LAN-IP-REDACTED]/24 — CPN internal) behind pf firewall (SecureMac host)

**Core Components:**

#### 1. Domain Controller (dc1.[DOMAIN.ORG] - [LAN-IP-REDACTED])

- FreeIPA identity management server
- LDAP directory services (389-ds)
- Kerberos authentication (KDC)
- Certificate Authority (Dogtag PKI)
- DNS services (BIND)
- NTP time synchronization
- Centralized logging (Graylog 6.1.16 / OpenSearch 2.19.4 / MongoDB 7.0.30)
- Wazuh SIEM (Manager 4.14.3 + Dashboard 4.14.3 + OpenSearch backend)
- Prometheus 2.48.0 monitoring (7 targets)
- Samba 4.22.4 file sharing
- NextCloud 32.0.5 collaboration platform
- Postfix 3.5.25 / Dovecot 2.3.16 email (TLS, DKIM via OpenDKIM 2.11.0)
- Storage: 1.8TB NVMe SSD — LVM + LUKS (AES-256-XTS, FIPS 140-2)
- FIPS 140-2 mode enabled; OpenSSL 3.5.1 FIPS provider active
- Rocky Linux 9.7 kernel: 5.14.0-611.30.1.el9_7.x86_64

#### 2. AI Server / SecureMac Management Host (ai.[DOMAIN.ORG] — Mac Mini M4 Pro)

**System Information:**

- Hostname: ai.[DOMAIN.ORG] (also responds as ai.[DOMAIN.ORG] on CPN)
- IP Address: [LAN-IP-REDACTED]/24 (LAN interface, Thunderbolt USB Ethernet)
- Role: AI/ML Inference Server, nginx Reverse Proxy, CyberInABox Management Host
- OS: **macOS 26.5 (Tahoe)** — Build 25F71
- Architecture: ARM64 (Apple Silicon)

**Hardware Platform:**

- Model: Apple Mac Mini (2024)
- Chip: Apple M4 Pro System on Chip (12-core CPU: 8P+4E)
- RAM: 64 GB unified memory (LPDDR5X)
- Neural Engine: 16-core for ML acceleration
- GPU: 16-core integrated GPU
- Storage: NVMe SSD with hardware encryption (Apple T2/M4 Secure Enclave)

**Security Features:**

- System Integrity Protection (SIP) enabled
- FileVault full-disk encryption enabled
- Apple T2/M4 Secure Enclave with hardware encryption
- pf firewall: WAN interface (en0/[WAN-IP-REDACTED]) isolated; LAN (en6/[LAN-IP-REDACTED]x); MGMT (en1/Wi-Fi)
- USB Guard: **ENABLED** (mode: on) — custom implementation at /usr/local/sbin/usb-guard
  - Time Machine SSD UUID ([TM-UUID-REDACTED]) allowlisted
  - All other USB storage blocked and logged to /var/log/usb-guard.log

**AI/ML Components:**

- **AI Model:** Magistral-Small-2509-MLX-4bit (MLX native, Apple Silicon)
  - Location: /opt/local/models/Magistral-Small-2509-MLX-4bit
  - Inference: MLX native (Metal Performance Shaders — no Ollama dependency)
  - Previous model: codellama:34b (Ollama) — replaced May 15, 2026
  - Use: General AI assistance, compliance document queries, system administration

- **Open Web UI** 0.9.5 (Python venv: /opt/local/open-webui-venv)
  - Upgraded from 0.8.12 on May 15, 2026
  - Bind address: **127.0.0.1:3000** (localhost only — changed from 0.0.0.0)
  - Access: Via nginx reverse proxy at https://ai.[DOMAIN.ORG] only
  - LaunchDaemon: /Library/LaunchDaemons/org.diwai.open-webui.plist
  - Signup disabled (ENABLE_SIGNUP=false); single admin account: [USERNAME]

- **nginx Reverse Proxy** 1.31.0 (Homebrew, ARM64) — *NEW May 15, 2026*
  - Purpose: HTTPS reverse proxy for Open Web UI
  - Listen: [LAN-IP-REDACTED]:443 (LAN) and 127.0.0.1:443 (loopback) — WAN interface (en0) excluded
  - TLS: *.[DOMAIN.ORG] wildcard certificate ([CERT-PATH-REDACTED]), TLSv1.2/1.3 only
  - Upstream: http://127.0.0.1:3000 (Open Web UI)
  - WebSocket: Enabled (required for streaming AI responses)
  - Security headers: HSTS (max-age=31536000; includeSubDomains), X-Frame-Options: SAMEORIGIN, X-Content-Type-Options: nosniff
  - LaunchDaemon: /Library/LaunchDaemons/org.diwai.nginx.plist
  - Config: /opt/homebrew/etc/nginx/servers/ai.[DOMAIN.ORG].conf

- **Time Machine Auto-Mount LaunchAgent** — *NEW May 15, 2026*
  - Script: /usr/local/sbin/mount-tm-drive.sh
  - Plist: ~/Library/LaunchAgents/org.diwai.mount-tm-drive.plist
  - Trigger: RunAtLoad (fires 5 seconds after user login)
  - Function: Detects and mounts SecureMac Time Machine SSD (UUID E2EBAB82) if not mounted
  - Root cause addressed: FileVault-encrypted APFS volume did not auto-mount after software-update reboot; caused 17-day backup gap (2026-04-28 to 2026-05-14)

**MFA Status (SecureMac Host):**

- YubiKey PIV smartcard authentication was configured (slot 9C cert paired to [USERNAME] account).
- Lockout incident on 2026-05-15: unknown PIV PIN prevented login; certs unpaired via recovery using sysadmin break-glass account (password-only, by design).
- Current state: [USERNAME] authenticates via password only. YubiKey hardware present (Nano 5C FIPS, SN: [HARDWARE-SERIAL]) but certs unpaired.
- Remediation: POA&M-046 (YubiKey PIV re-pairing, PLANNED)
- **Note:** This gap affects the management host only. CPN Linux systems (dc1, labrat, engineering, accounting) MFA (SSH pubkey + TOTP) is unaffected — 3.5.3 MET for CPN.

#### 3. Network Security (SecureMac pf Firewall)

- macOS pf firewall on Mac Mini M4 Pro (replaces deprecated Netgate pfSense)
- WAN interface: en0 ([WAN-IP-REDACTED]/29, [ISP-REDACTED])
- LAN interface: en6 ([LAN-IP-REDACTED]/24, Thunderbolt USB Ethernet)
- MGMT interface: en1 (Wi-Fi, [LAN-IP-REDACTED] — never blocked)
- Stateful packet inspection; NAT; inbound port restrictions
- VPN capability (OpenVPN, planned — POA&M-028)

#### 4. Client Workstations (DEPLOYED)

**LabRat** ([LAN-IP-REDACTED]): Rocky Linux 9.6, FIPS 140-2 enabled, 100% OpenSCAP CUI compliant (104/104), full LUKS disk encryption, USBGuard, session lock 15 min, MFA (SSH pubkey + TOTP)

**Engineering** ([LAN-IP-REDACTED]): Rocky Linux 9.7, FIPS 140-2 enabled, 100% OpenSCAP CUI compliant (104/104), full LUKS disk encryption, USBGuard, session lock 15 min, MFA (SSH pubkey + TOTP)

**Accounting** ([LAN-IP-REDACTED]): Rocky Linux 9.7, FIPS 140-2 enabled, 100% OpenSCAP CUI compliant (104/104), full LUKS disk encryption, USBGuard, session lock 15 min, MFA (SSH pubkey + TOTP)

#### 5. Email Server (dc1.[DOMAIN.ORG] — integrated) ✅ OPERATIONAL

- Postfix 3.5.25 SMTP with TLS enforcement
- Dovecot 2.3.16 IMAP/POP3 with encryption
- OpenDKIM 2.11.0 — DKIM signing/verification (operational 02/03/2026)
- SpamAssassin 3.4.6 + spamass-milter — spam filtering (operational 02/03/2026)
- Domain: [DOMAIN.ORG]
- Integration: FreeIPA authentication via LDAP

### 3.3 Network Topology

```
Internet ([WAN-IP-REDACTED]/29)
    |
SecureMac Host (Mac Mini M4 Pro -- pf firewall)
  en0: WAN ([WAN-IP-REDACTED])
  en6: LAN ([LAN-IP-REDACTED]/24)
    +-- services.[DOMAIN.ORG] ([LAN-IP-REDACTED]) -- Rocky Linux 9.7 VM (UTM)
    +-- nas.[DOMAIN.ORG] ([LAN-IP-REDACTED]) -- Synology 8-bay NAS

CPN Internal ([LAN-IP-REDACTED]/24 -- via VM routing)
  +-- dc1.[DOMAIN.ORG] ([LAN-IP-REDACTED]) -- Domain Controller + SIEM
  +-- labrat ([LAN-IP-REDACTED]) -- Lab Workstation
  +-- engineering ([LAN-IP-REDACTED]) -- Engineering Workstation
  +-- accounting ([LAN-IP-REDACTED]) -- Accounting Workstation
```

### 3.4 Malware Protection Architecture

The system employs a defense-in-depth malware protection strategy:

- **Layer 1: YARA 4.5.2** — Pattern-based detection (operational). 22 active rules. Wazuh active response integration (FIM rules 550, 554).
- **Layer 2: VirusTotal Integration** — Cloud multi-engine scanning (70+ engines). Wazuh FIM triggers (level 10+ alerts). Rate limit: 490/day quota guard.
- **Layer 3: Wazuh SIEM Correlation** — Centralizes all detection events, automated alerting, cross-layer threat intelligence.
- **ClamAV:** RISK ACCEPTED — FIPS 140-2 incompatible. Compensating controls: YARA, VirusTotal, Wazuh FIM, network IDS/IPS.

**FIPS Compliance:**

- YARA: Uses OpenSSL 3.2.2 (FIPS-approved cryptography)
- VirusTotal: HTTPS/TLS transport (FIPS-compatible)

## 4. SECURITY CONTROL IMPLEMENTATION

This section documents the implementation status of all NIST SP 800-171 security requirements.

**Control Status Legend:**

- **IMPLEMENTED** — Control is fully operational and verified
- **ENHANCED** — Control exceeds baseline requirements
- **PLANNED** — Control design complete, implementation in progress
- **N/A** — Control not applicable to this system

### 4.1 Access Control (AC)

| Control ID | Control Name                                                 | Status      | Implementation                                               | Assessment                                                   |
| :--------- | :----------------------------------------------------------- | :---------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 3.1.1      | Limit system access to authorized users                      | IMPLEMENTED | FreeIPA provides centralized authentication for CPN systems. All user accounts managed via LDAP. SSH keys enforced. **SecureMac host (05/15/2026):** Open Web UI AI interface access restricted to authenticated nginx proxy at https://ai.[DOMAIN.ORG]. Direct port 3000 access blocked (localhost-only bind). nginx listens only on LAN interface ([LAN-IP-REDACTED]) and loopback — WAN interface (en0) not exposed. Strengthens logical access control for AI platform per 3.1.1. | Verified via FreeIPA user database, SSH configuration audit, nginx listener configuration |
| 3.1.2      | Limit system access to authorized functions                  | IMPLEMENTED | Role-based access control via FreeIPA groups and sudo rules. SELinux enforcing mandatory access controls. **SecureMac host (05/15/2026):** AI capabilities accessible only via nginx reverse proxy requiring network-layer access to LAN ([LAN-IP-REDACTED]) — WAN interface excluded. Strengthens functional access control per 3.1.2. | Verified via sudo configuration, SELinux policy audit, nginx configuration |
| 3.1.3      | Control flow of CUI                                          | IMPLEMENTED | Network segmentation via firewall. TLS/SSH encryption for data in transit. LUKS encryption at rest. AI platform access controlled via nginx proxy; no direct port exposure on WAN. | Verified via firewall rules, encryption verification, network traffic analysis |
| 3.1.4      | Separation of duties                                         | N/A         | Single-person organization. Separation enforced via audit logging and external review processes. | Documented in operational procedures                         |
| 3.1.5      | Employ principle of least privilege                          | IMPLEMENTED | Standard users have no administrative access. Sudo elevation required for privileged operations. Logged. | Verified via user permission audit and sudo logs             |
| 3.1.6      | Use non-privileged accounts                                  | IMPLEMENTED | Administrative tasks require sudo elevation. No direct root login via SSH. All activities logged. | Verified via SSH configuration and authentication logs       |
| 3.1.7      | Prevent non-privileged users from executing privileged functions | IMPLEMENTED | SELinux enforcing prevents privilege escalation. Sudo configuration restricts command execution. | Verified via SELinux audit and sudo configuration            |
| 3.1.8      | Limit unsuccessful logon attempts                            | IMPLEMENTED | PAM faillock: 5 failed attempts trigger 30-minute lockout. Configured via OpenSCAP. | Verified via OpenSCAP scan (100% pass) and PAM configuration |
| 3.1.9      | Provide privacy and security notices                         | IMPLEMENTED | Login banners configured on SSH and console on all 4 CPN systems. Banner text: CyberHygiene Project Contractor Information System (CIS) access notice. | Verified via /etc/issue and /etc/ssh/sshd_config on all systems |
| 3.1.10     | Use session lock with pattern-hiding displays                | IMPLEMENTED | Automatic screen lock after 15 minutes idle on all 4 CPN workstations. GNOME dconf: idle-delay=900s, lock-enabled=true. | Verified on all workstations via user session configuration  |
| 3.1.11     | Terminate user session after defined period                  | IMPLEMENTED | SSH sessions timeout after 15 minutes idle (ClientAliveInterval). GUI sessions lock automatically. | Verified via SSH configuration and user session policies     |
| 3.1.12     | Monitor and control remote access sessions                   | IMPLEMENTED | SSH access logged to centralized rsyslog/Graylog. Failed attempts trigger Wazuh alerts. | Verified via authentication logs and firewall rules          |
| 3.1.13     | Employ cryptographic mechanisms to protect remote access     | IMPLEMENTED | SSH with FIPS-approved ciphers only. TLS 1.2/1.3 for HTTPS. nginx proxy enforces TLSv1.2/1.3 with HSTS. | Verified via SSH and TLS configuration audits                |
| 3.1.14     | Route remote access via managed access control points        | IMPLEMENTED | All remote access through pf firewall (SecureMac). SSH on managed ports. VPN planned (POA&M-028). | Verified via firewall configuration                          |
| 3.1.15     | Authorize remote access prior to allowing connections        | IMPLEMENTED | SSH requires FreeIPA authentication. Public key + TOTP enforced. No anonymous access. | Verified via SSH configuration and access logs               |
| 3.1.16     | Authorize wireless access prior to allowing connections      | N/A         | No wireless access points in CPN boundary.                   | Physical inspection confirmed no wireless APs on CPN         |
| 3.1.17     | Protect wireless access using authentication and encryption  | N/A         | No wireless access points in CPN boundary.                   | N/A                                                          |
| 3.1.18     | Control connection of mobile devices                         | IMPLEMENTED | USB device restrictions via USBGuard on all 4 CPN systems (operational 02/15/2026). SecureMac USB Guard enabled (mode: on). | Verified via USBGuard status on all systems                  |
| 3.1.19     | Encrypt CUI on mobile devices                                | IMPLEMENTED | All systems have full disk encryption (LUKS on Rocky Linux; FileVault on macOS). FIPS 140-2 validated cryptography. | Verified via cryptsetup status on all systems                |
| 3.1.20     | Control use of portable storage devices                      | IMPLEMENTED | USBGuard deployed on all 4 CPN systems (device-specific allow policy). SecureMac USB Guard enabled with Time Machine UUID allowlisted. | Verified via USBGuard device lists                           |
| 3.1.21     | Limit use of portable storage devices on external systems    | IMPLEMENTED | Policy prohibits use of organizational USB devices on non-organizational systems. Documented in TCC-AUP-001. | Verified via AUP and user training records                   |
| 3.1.22     | Control CUI posted or processed on publicly accessible systems | IMPLEMENTED | CUI prohibited from public-facing systems. No CUI on websites or public repositories. | Verified via system inventory and data classification procedures |

### 4.2 Awareness and Training (AT)

| Control ID | Control Name                                                 | Status      | Implementation                                               | Assessment                                                   |
| :--------- | :----------------------------------------------------------- | :---------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 3.2.1      | Ensure managers, systems administrators, and users are trained | IMPLEMENTED | Security awareness training delivered FY2026: TCC-SAT-FY2026 (4 hrs) covering CUI handling, phishing, insider threat awareness. Quiz: TCC-SAT-QUIZ-FY2026 (80% pass threshold). Completed 02/17/2026. | Training records: TCC-SAT-RECORD-FY2026. POA&M-006 CLOSED 02/17/2026. |
| 3.2.2      | Provide security awareness training on recognizing and reporting threats | IMPLEMENTED | Role-based training module TCC-SAT-FY2026 Section 2. Annual refresher scheduled. Completed 02/17/2026. | Training records: TCC-SAT-RECORD-FY2026. POA&M-006 CLOSED 02/17/2026. |
| 3.2.3      | Provide security training before access, when required, and annually | IMPLEMENTED | Insider threat awareness module TCC-SAT-FY2026 Section 3. Training required before CUI access and annually thereafter. Completed 02/17/2026. | Training records: TCC-SAT-RECORD-FY2026. POA&M-006 CLOSED 02/17/2026. |

### 4.3 Audit and Accountability (AU)

**Status:** All AU controls are **IMPLEMENTED**. The system maintains comprehensive audit logs on dedicated encrypted partitions, with centralized logging operational for all systems. Audit records include timestamps, user identification, event types, and outcomes. Logs are protected from unauthorized access and retained per policy.

**AU-2 (Auditable Events):** All system logs centralized in Graylog 6.1.16. rsyslog forwards logs from all system components including system logs (journald), FreeIPA authentication and authorization events, Wazuh security alerts and FIM events, Linux audit logs (auditd), and application logs.

**AU-3 (Content of Audit Records):** Graylog preserves all original audit record content including timestamps, source identifiers, event types, outcomes, and user identities. OpenSearch provides indexed storage for rapid search and retrieval.

**AU-6 (Audit Review, Analysis, and Reporting):** Graylog Web UI provides centralized audit review. ISSO reviews security-relevant events daily. Wazuh provides automated audit review via analytics engine with real-time correlation and alerting.

**AU-7 (Audit Reduction and Report Generation):** Graylog provides audit reduction through full-text search, field-based filtering, dashboard creation, and export capabilities (CSV, JSON).

**AU-9 (Protection of Audit Information):** OpenSearch data directory root-owned (700 permissions). MongoDB metadata restricted to mongod user. Backend services bound to localhost only.

### 4.4 Configuration Management (CM)

**Status:** All CM controls are **IMPLEMENTED**. Configuration baselines established via OpenSCAP. Automated compliance scanning ensures systems maintain approved configurations. Changes are documented and tracked. Security-relevant software updates applied automatically via dnf-automatic.

**CM-6 Enhancement:** Wazuh Security Configuration Assessment (SCA) provides continuous compliance verification against CIS Rocky Linux 9 Benchmark, automated deviation detection, and policy-based configuration enforcement.

### 4.5 Identification and Authentication (IA)

**Status:** All IA controls are **IMPLEMENTED**. FreeIPA provides centralized authentication with strong password policies (14+ characters, complexity requirements, 90-day expiration). Kerberos SSO reduces password exposure.

**3.5.3 Multi-Factor Authentication — CPN Systems:** SSH publickey (ECDSA-521) + TOTP via pam_google_authenticator.so deployed on all 4 CPN systems (dc1, labrat, engineering, accounting) as of 02/21/2026. Microsoft Authenticator (TOTP-compatible, RFC 6238). Status: **MET**. SPRS: +5 points recovered.

**3.5.3 Multi-Factor Authentication — SecureMac Host (05/15/2026):** YubiKey PIV smartcard authentication was previously configured on the SecureMac host ([USERNAME] account, slot 9C cert). Following an account lockout on 2026-05-15 (unknown PIV PIN after cert pairing change), smartcard certs were unpaired as recovery measure. Host currently authenticates via password only. Remediation tracked in POA&M-046 (YubiKey PIV re-pairing, PLANNED). Sysadmin break-glass account (password-only, by design) functioned correctly during incident.

**Note:** This affects the management host only. CPN Linux systems MFA status (SSH pubkey + TOTP) is unaffected — 3.5.3 remains MET for CPN.

### 4.6 Incident Response (IR)

**Status:** All IR controls are **IMPLEMENTED**. Incident Response Policy and Procedures (TCC-IRP-001) approved and effective since 11/02/2025. Wazuh SIEM provides real-time intrusion detection and automated incident response capabilities. Annual tabletop exercise scheduled June 30, 2026 (POA&M-SPRS-2, -1 SPRS point).

### 4.7 Maintenance (MA)

**Status:** All MA controls are **IMPLEMENTED**. Maintenance activities are logged and tracked. Security patches applied automatically via dnf-automatic. Maintenance tools are controlled and logged.

### 4.8 Media Protection (MP)

**Status:** All MP controls are **IMPLEMENTED**. Media sanitization procedures documented in TCC-PE-MP-001, Section 2.6 (LUKS erase, shred). All storage encrypted via LUKS (Rocky Linux) or FileVault (macOS). Media disposal follows NIST SP 800-88 guidelines.

### 4.9 Physical Protection (PE)

**Status:** All PE controls are **IMPLEMENTED**. Physical access controls in place. System housed in locked rack enclosure within secured facility. Rack contains both CyberInABox (Ref System #1) and SecureMac (Ref System #2) behind a single locked door — shared physical security perimeter.

**PE-2/PE-3 (Physical Access):** Single locked rack enclosure covers both reference systems. Controls documented as Common Controls in TCC-PE-MP-001, inherited by both SSPs.

**PE-11 (Emergency Power):** UPS serves both systems within the shared rack enclosure.

### 4.10 Personnel Security (PS)

**Status:** All PS controls are **IMPLEMENTED**. Background investigations conducted. Personnel termination procedures documented in TCC-PS-001. System owner maintains active DoD Top Secret clearance.

### 4.11 Risk Assessment (RA)

**Status:** All RA policy controls are **IMPLEMENTED**. Risk Management Policy (TCC-RA-001) approved with NIST SP 800-30 methodology.

**3.11.1 Periodic Risk Assessment:** Risk Management Policy (TCC-RA-001) is approved and methodology is established. The first formal periodic risk assessment has not yet been conducted. **Target was April 30, 2026 — OVERDUE as of May 2026.** Status: NOT MET — -3 SPRS points. See POA&M-035.

**RA-5 (Vulnerability Scanning):** Wazuh vulnerability detection module operational with automated vulnerability feeds updated every 60 minutes. Integration with CVE databases. Continuous agent-based scanning of installed packages. OpenSCAP CUI profile automated scanning every 12 hours on all 4 CPN systems.

### 4.12 Security Assessment (CA)

**Status:** All CA controls are **IMPLEMENTED**. Independent CMMC L2 Preliminary Gap Analysis conducted 02/09/2026. OpenSCAP automated scanning provides continuous compliance verification (100% on all 4 CPN systems). Wazuh Dashboard 4.14.3 operational at https://dc1.[DOMAIN.ORG]:5601.

### 4.13 System and Communications Protection (SC)

**Status:** All SC controls are **IMPLEMENTED**. Network segmentation operational. Encryption enforced for all communications. pf firewall provides boundary protection. FIPS 140-2 cryptography validated on all Rocky Linux systems.

**SC-7 (Boundary Protection):** SecureMac: pf firewall on Mac Mini (WAN/LAN/MGMT segregation). CPN: dc1 routing on [LAN-IP-REDACTED]/24. No shared firewall — independent boundary protection per system.

**SC-8 (Transmission Confidentiality and Integrity):** All metrics transmission encrypted TLS 1.2/1.3 (FIPS cipher suites). nginx enforces TLSv1.2/1.3 with *.[DOMAIN.ORG] wildcard cert for ai.[DOMAIN.ORG]. WebSocket proxying encrypted end-to-end.

**SC-13 (Cryptographic Protection):** FIPS 140-2 mode enabled on all Rocky Linux systems. OpenSSL 3.5.1 FIPS provider active. FIPS-approved cipher suites enforced.

**SC-28 (Protection of Information at Rest):** Rocky Linux systems: LUKS AES-256-XTS. macOS host: FileVault full-disk encryption. NAS: Synology folder-level AES-256/SHA-256 encryption (non-FIPS second layer).

**Note — FIPS Boundary / NAS:** The Wazuh log archival pipeline crosses a FIPS boundary. Inside FIPS boundary: Rocky Linux 9.7 VM encrypts daily alert archives using OpenSSL AES-256-CBC + PBKDF2/SHA-256 (FIPS 140-2 validated). Transfer via SSH (AES-256-CTR). Outside FIPS boundary: Synology NAS folder encryption (AES-256/SHA-256, not FIPS 140-2 validated). The encrypted .enc file is the FIPS artifact; the NAS provides a non-FIPS second layer (defense in depth, not a FIPS claim). NAS is classified as Supporting Infrastructure within the physical security boundary.

### 4.14 System and Information Integrity (SI)

**Status:** All SI controls are **IMPLEMENTED** with **ENHANCED** capabilities for malware protection.

**SI-3 (Malicious Code Protection) — Multi-Layer Defense:**

*Layer 1: YARA 4.5.2 (Fully Operational)*

- Pattern-based malware detection using custom signatures (22 active rules)
- Built from source with FIPS-compatible OpenSSL 3.2.2
- Integration: Wazuh active response triggered by FIM events (rules 550, 554)
- Graylog integration via GELF UDP; Grafana dashboard visualization
- Testing: End-to-end EICAR detection verified

*Layer 2: VirusTotal Integration (Operational)*

- Cloud-based multi-engine scanning (70+ antivirus engines)
- Integration via Wazuh FIM triggers (level 10+ alerts — threshold raised from 7 to reduce API volume)
- MD5 hash deduplication cache; daily quota guard (490/day)

*Layer 3: ClamAV — RISK ACCEPTED*

- ClamAV 1.4.3 incompatible with FIPS mode. Risk accepted per Risk_Acceptance_ClamAV_FIPS_Incompatibility.md.
- Compensating controls: YARA (primary), VirusTotal, Wazuh FIM, network IDS/IPS.
- Annual risk review: December 31, 2026.

**SI-4 (System Monitoring) — Enhanced:**

- Wazuh SIEM 4.14.3: Real-time security event detection, FIM, vulnerability scanning
- Wazuh Dashboard 4.14.3 (OpenSearch 2.19.4 backend): Centralized visibility at https://dc1.[DOMAIN.ORG]:5601
- Graylog 6.1.16: Centralized log management and search
- Prometheus 2.48.0: Time-series metrics (7 targets, 15s interval, 15-day retention)
- Node Exporter 1.10.2: Host metrics across all systems (FIPS-compliant TLS, HTTPS port 9100)
- Auditd: System call auditing with OSPP v42 rules

**SI-7 (Software, Firmware, and Information Integrity):** Wazuh FIM with real-time change detection on critical files (/etc, /usr/bin, /usr/sbin, /bin, /sbin, /boot). SHA256 checksums. 12-hour scan frequency with real-time monitoring. Automated YARA scanning on file changes.

**SI-2 (Flaw Remediation):** Automated security updates via dnf-automatic with Wazuh vulnerability correlation.

## 5. CONTINGENCY PLANNING (CP)

### CP-9 (System Backup)

**Status:** IMPLEMENTED

**CPN Systems (dc1):**

- Daily critical files backup to /backup/daily/ (30-day retention)
- Weekly full system backup via ReaR to /srv/samba/backups/ (4-week retention)
- SHA256 checksums for all archives; LUKS encrypted partition storage

**SecureMac Host:**

- Time Machine backup to dedicated SSD (UUID: [TM-UUID-REDACTED])
- org.diwai.mount-tm-drive LaunchAgent ensures SSD mounts automatically at login
- Wazuh log archival pipeline: daily alert archives pushed to NAS (nas.[DOMAIN.ORG])

### CP-10 (System Recovery and Reconstitution)

**Status:** IMPLEMENTED

- ReaR bootable ISO enables bare-metal recovery for CPN systems
- Recovery Time Objective (RTO): < 4 hours
- Recovery Point Objective (RPO): 24 hours (daily backup)
- macOS: Time Machine + bootable installer for SecureMac host recovery

## 6. SECURITY POLICIES AND PROCEDURES

### 6.1 Policy Framework

The organization maintains a comprehensive set of security policies aligned with NIST 800-171 requirements.

**Approved Policies (all formally signed as of February 15, 2026 or earlier):**

| Policy Document                             | ID            | Controls                              | Effective Date |
| :------------------------------------------ | :------------ | :------------------------------------ | :------------- |
| Incident Response Policy and Procedures     | TCC-IRP-001   | IR-1 through IR-8                     | 11/02/2025     |
| Risk Management Policy                      | TCC-RA-001    | RA-1 through RA-9                     | 11/02/2025     |
| Personnel Security Policy                   | TCC-PS-001    | PS-1 through PS-8                     | 11/02/2025     |
| Physical and Media Protection Policy        | TCC-PE-MP-001 | PE-1 through PE-20, MP-1 through MP-8 | 11/02/2025     |
| System and Information Integrity Policy     | TCC-SI-001    | SI-1 through SI-12                    | 11/02/2025     |
| Acceptable Use Policy                       | TCC-AUP-001   | AC-1, PS-6, PL-4                      | 11/02/2025     |
| Audit and Accountability Policy             | TCC-AAP-001   | AU-1 through AU-12                    | 02/15/2026     |
| Configuration Management Policy             | TCC-CMP-001   | CM-1 through CM-11                    | 02/15/2026     |
| Security Awareness and Training Policy      | TCC-ATP-001   | AT-1 through AT-4                     | 02/15/2026     |
| Identification and Authentication Policy    | TCC-IAP-001   | IA-1 through IA-11                    | 02/15/2026     |
| System and Communications Protection Policy | TCC-SCP-001   | SC-1 through SC-16                    | 02/15/2026     |

### 6.2 Malware Protection Policy (SI-3)

**Policy Statement:** The organization employs malicious code protection mechanisms at information system entry and exit points to detect and eradicate malicious code.

**Implementation:** Multi-layered malware detection (YARA + VirusTotal + Wazuh FIM). Real-time file scanning on creation and modification. Automated signature and pattern database updates. Centralized alert management via Wazuh SIEM.

**Compliance:** Satisfies NIST 800-171 3.14.1, 3.14.2, 3.14.3 and CMMC Level 2 SI.3.217.

## 10. PLAN OF ACTION & MILESTONES (POA&M)

The complete POA&M is maintained as a standalone document: **Unified_POAM_v2.12.md** (May 15, 2026).

### Current POA&M Summary (as of May 15, 2026)

| Metric                 | Count    |
| :--------------------- | :------- |
| Total Items            | 46       |
| Completed              | 35 (76%) |
| On Track               | 4 (9%)   |
| Ongoing                | 2 (4%)   |
| Closed (Risk Accepted) | 1 (2%)   |
| Planned                | 2 (4%)   |

**SPRS Score:** 106/110 (96.4%)\
**Remaining Deficit:** -4 points\
**Outstanding SPRS Items:**

| POA&M ID     | Control                         | Deficit | Target     | Status      |
| :----------- | :------------------------------ | :------ | :--------- | :---------- |
| POA&M-035    | 3.11.1 Periodic Risk Assessment | -3 pts  | 04/30/2026 | **OVERDUE** |
| POA&M-SPRS-2 | 3.6.3 IR Tabletop Exercise      | -1 pt   | 06/30/2026 | ON TRACK    |

**Non-SPRS Open Items:**

| POA&M ID  | Item                                    | Status                       |
| :-------- | :-------------------------------------- | :--------------------------- |
| POA&M-028 | VPN with MFA for remote access          | PLANNED — Target 06/30/2026  |
| POA&M-046 | YubiKey PIV re-pairing (SecureMac host) | PLANNED — TBD                |
| POA&M-012 | Disaster recovery testing               | ON TRACK — Target 04/30/2026 |

For full item details, evidence, and completion tracking, see: `CyberSecurity/Current/POAM/Unified_POAM_v2.12.md`

## 11. IMPLEMENTATION METRICS

### Control Implementation Status

Overall Implementation Status: 96.4% SPRS Compliance (as of May 15, 2026). SPRS: 106/110.

#### By Control Family

| Family | Family Name              | Total Controls | Implemented | Partial | Planned | N/A  | % Complete               |
| :----- | :----------------------- | :------------- | :---------- | :------ | :------ | :--- | :----------------------- |
| AC     | Access Control           | 22             | 22          | 0       | 0       | 1    | 100%                     |
| AT     | Awareness & Training     | 4              | 4           | 0       | 0       | 0    | 100%                     |
| AU     | Audit & Accountability   | 12             | 12          | 0       | 0       | 0    | 100%                     |
| CA     | Security Assessment      | 9              | 9           | 0       | 0       | 0    | 100%                     |
| CM     | Configuration Mgmt       | 11             | 11          | 0       | 0       | 0    | 100%                     |
| CP     | Contingency Planning     | 4              | 4           | 0       | 0       | 0    | 100%                     |
| IA     | Identification & Auth    | 11             | 11          | 0       | 0       | 0    | 100%                     |
| IR     | Incident Response        | 8              | 7           | 1       | 0       | 0    | 97% (IR testing pending) |
| MA     | Maintenance              | 6              | 6           | 0       | 0       | 0    | 100%                     |
| MP     | Media Protection         | 8              | 8           | 0       | 0       | 0    | 100%                     |
| PE     | Physical Protection      | 20             | 15          | 0       | 0       | 5    | 100%                     |
| PS     | Personnel Security       | 8              | 8           | 0       | 0       | 0    | 100%                     |
| RA     | Risk Assessment          | 6              | 5           | 1       | 0       | 0    | 97% (3.11.1 overdue)     |
| SC     | System & Comm Protection | 35             | 35          | 0       | 0       | 0    | 100%                     |
| SI     | System & Info Integrity  | 12             | 12          | 0       | 0       | 0    | 100%                     |

#### Policy Documentation Completion

| Policy                          | Status   | Effective Date | Controls Covered                      |
| :------------------------------ | :------- | :------------- | :------------------------------------ |
| Incident Response               | Complete | 11/02/2025     | IR-1 through IR-8                     |
| Risk Management                 | Complete | 11/02/2025     | RA-1 through RA-9                     |
| Personnel Security              | Complete | 11/02/2025     | PS-1 through PS-8                     |
| Physical & Media Protection     | Complete | 11/02/2025     | PE-1 through PE-20, MP-1 through MP-8 |
| System & Information Integrity  | Complete | 11/02/2025     | SI-1 through SI-12                    |
| Acceptable Use                  | Complete | 11/02/2025     | AC-1, PS-6, PL-4                      |
| Audit & Accountability          | Complete | 02/15/2026     | AU-1 through AU-12                    |
| Configuration Management        | Complete | 02/15/2026     | CM-1 through CM-11                    |
| Awareness & Training            | Complete | 02/15/2026     | AT-1 through AT-4                     |
| Identification & Authentication | Complete | 02/15/2026     | IA-1 through IA-11                    |
| System & Comms Protection       | Complete | 02/15/2026     | SC-1 through SC-16                    |

**Total Policy Coverage:** 110 controls across all 14 families — 100%

## COMPLIANCE IMPACT SUMMARY

### SPRS Score Status

**Current SPRS Score:** 106/110 (96.4%) per independent CMMC L2 Preliminary Gap Analysis (February 9, 2026), updated through May 15, 2026.\
**Previous Score:** 101/110 (February 17, 2026)\
**Target Score:** 110/110 (100%)\
**POA&M Reference:** Unified_POAM_v2.12 (May 15, 2026)

**Remaining Deficits:**

| Req ID | Control Description      | Weight | Target     | Status   |
| :----- | :----------------------- | :----- | :--------- | :------- |
| 3.11.1 | Periodic Risk Assessment | -3     | 04/30/2026 | OVERDUE  |
| 3.6.3  | IR Testing (Tabletop)    | -1     | 06/30/2026 | On Track |

### CMMC Level 2 Readiness

**Practice Maturity:**

- Level 1: Performed — Technical controls implemented
- Level 2: Documented — Policies and procedures established (all 11 policy families complete)
- Level 2: Managed — Review schedules and metrics defined
- Level 2: Reviewed — First formal risk assessment overdue (POA&M-035)

**Assessment Evidence Package:**

- 11 approved policy documents (signed, effective dates documented)
- Independent CMMC L2 Preliminary Gap Analysis (02/09/2026)
- OpenSCAP CUI compliance reports (100% on all 4 CPN systems)
- Wazuh Dashboard monitoring (continuous monitoring evidence)
- MFA deployment records
- Backup verification logs (ReaR weekly + daily critical files)
- Top Secret clearance documentation (personnel security evidence)

**Assessment Readiness:** HIGH — Comprehensive documentation package ready for C3PAO assessment.

## 12. CONCLUSION

The CyberHygiene Production Network is a fully authorized, NIST 800-171 compliant infrastructure operating under full 3-year ATO (January 1, 2026 — December 31, 2028). SPRS score is 106/110 (96.4%) with 2 remaining deficits — periodic risk assessment (overdue, POA&M-035) and IR tabletop exercise (due June 30, 2026, POA&M-SPRS-2).

### Key Accomplishments (as of May 15, 2026)

- **MFA Complete:** SSH publickey + TOTP deployed on all 4 CPN systems (02/21/2026) — +5 SPRS points
- **Full OpenSCAP CUI Compliance:** All 4 CPN systems at 104/104 (0 failures) since 02/21/2026
- **All Policies Approved:** 11 policy documents covering all 110 NIST 800-171 controls, all signed
- **Security Training Complete:** TCC-SAT-FY2026 delivered, assessed, records retained
- **AI Platform Access-Hardened:** nginx reverse proxy deployed, Open Web UI localhost-only, WAN excluded (05/15/2026)
- **USB Guard Re-Enabled:** SecureMac host mode: on, Time Machine UUID allowlisted (05/15/2026)
- **Time Machine Auto-Mount Resolved:** 17-day backup gap root cause corrected (05/15/2026)

### Remaining Tasks

| Item                                               | Target     | Status   |
| :------------------------------------------------- | :--------- | :------- |
| POA&M-035: First annual risk assessment (3.11.1)   | 04/30/2026 | OVERDUE  |
| POA&M-SPRS-2: IR tabletop exercise (3.6.3)         | 06/30/2026 | ON TRACK |
| POA&M-028: VPN with MFA for remote access          | 06/30/2026 | PLANNED  |
| POA&M-046: YubiKey PIV re-pairing (SecureMac host) | TBD        | PLANNED  |

## AUTHORIZATION

**Full Authorization Granted:** January 1, 2026\
**Authorization Period:** 3 years (through December 31, 2028)\
**Authorizing Official:** /s/ [SYSTEM-OWNER], System Owner/ISSO, [ORGANIZATION]\
**Date:** May 15, 2026

## APPENDICES

### Appendix A: Acronyms and Abbreviations

- **AC** - Access Control
- **ATO** - Authorization to Operate
- **AU** - Audit and Accountability
- **CA** - Security Assessment
- **CMMC** - Cybersecurity Maturity Model Certification
- **CP** - Contingency Planning
- **CUI** - Controlled Unclassified Information
- **CVE** - Common Vulnerabilities and Exposures
- **DFARS** - Defense Federal Acquisition Regulation Supplement
- **FAR** - Federal Acquisition Regulation
- **FCI** - Federal Contract Information
- **FIM** - File Integrity Monitoring
- **FIPS** - Federal Information Processing Standards
- **IA** - Identification and Authentication
- **IDS/IPS** - Intrusion Detection/Prevention System
- **IR** - Incident Response
- **ISSO** - Information System Security Officer
- **LDAP** - Lightweight Directory Access Protocol
- **LLM** - Large Language Model
- **LUKS** - Linux Unified Key Setup
- **MFA** - Multi-Factor Authentication
- **MLX** - Machine Learning eXchange (Apple Silicon native inference framework)
- **NIST** - National Institute of Standards and Technology
- **POA&M** - Plan of Action and Milestones
- **RA** - Risk Assessment
- **ReaR** - Relax-and-Recover
- **SC** - System and Communications Protection
- **SCA** - Security Configuration Assessment
- **SI** - System and Information Integrity
- **SIEM** - Security Information and Event Management
- **SSH** - Secure Shell
- **SSP** - System Security Plan
- **TLS** - Transport Layer Security
- **TOTP** - Time-based One-Time Password
- **YARA** - Yet Another Recursive Acronym (malware detection tool)

### Appendix B: References

1. NIST Special Publication 800-171 Revision 2, Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations
2. NIST Special Publication 800-171A, Assessing Security Requirements for Controlled Unclassified Information
3. FAR 52.204-21, Basic Safeguarding of Covered Contractor Information Systems
4. DFARS 252.204-7012, Safeguarding Covered Defense Information and Cyber Incident Reporting
5. FIPS 140-2, Security Requirements for Cryptographic Modules
6. FIPS 199, Standards for Security Categorization of Federal Information and Information Systems
7. CMMC Model Version 2.0, Cybersecurity Maturity Model Certification
8. 32 CFR Part 2002, Controlled Unclassified Information
9. Wazuh Security Platform Documentation v4.14.3
10. NIST SP 800-88 Rev 1, Guidelines for Media Sanitization
11. YARA Documentation v4.5.2, https://yara.readthedocs.io
12. VirusTotal API Documentation, https://developers.virustotal.com
13. nginx Documentation v1.31.0, https://nginx.org/en/docs/

### Appendix C: Supporting Documentation

**AI/ML Infrastructure:**

- nginx reverse proxy config: /opt/homebrew/etc/nginx/servers/ai.[DOMAIN.ORG].conf
- Open Web UI service: /Library/LaunchDaemons/org.diwai.open-webui.plist
- nginx LaunchDaemon: /Library/LaunchDaemons/org.diwai.nginx.plist
- USB Guard scripts: /usr/local/sbin/usb-guard, /usr/local/sbin/usb-guard-monitor
- Time Machine auto-mount: /usr/local/sbin/mount-tm-drive.sh, ~/Library/LaunchAgents/org.diwai.mount-tm-drive.plist

**Antimalware Documentation:**

- Wazuh_YARA_Integration_Guide.md
- Wazuh_VirusTotal_Integration_Guide.md
- ClamAV_FIPS_Incompatibility_Final_Report.md
- Risk_Acceptance_ClamAV_FIPS_Incompatibility.md

**Policy Documentation:**

- TCC-IRP-001, TCC-RA-001, TCC-PS-001, TCC-PE-MP-001, TCC-SI-001, TCC-AUP-001
- TCC-AAP-001, TCC-CMP-001, TCC-ATP-001, TCC-IAP-001, TCC-SCP-001

### Appendix D: Document Maintenance

This System Security Plan shall be reviewed and updated:

- Quarterly (every 3 months) or more frequently as needed
- Upon significant system changes (hardware, software, or security posture)
- Following security incidents requiring corrective actions
- When new threats or vulnerabilities are identified
- When NIST 800-171 requirements are updated

**Next Scheduled Review:** July 31, 2026

**Review Focus Areas:**

- POA&M-035 risk assessment completion (overdue)
- POA&M-SPRS-2 IR tabletop exercise (due June 30, 2026)
- POA&M-046 YubiKey PIV re-pairing status
- POA&M-028 VPN with MFA progress
- Open Web UI version currency
- macOS security updates (macOS 26.x)
- OpenSCAP scan results review

### Appendix E: SSP Addendums

| Addendum                              | Version | Date       | Description                                                  |
| :------------------------------------ | :------ | :--------- | :----------------------------------------------------------- |
| YARA Malware Detection System         | 1.0     | 12/30/2025 | YARA v4.5.2 integration with Wazuh SIEM, 22 detection rules, Graylog GELF integration, Grafana dashboard. Addresses SI-3, SI-4, AU-2, AU-3, AU-6, AU-12, IR-4, RA-5. |
| FIPS-Compliant Workstation Monitoring | 1.0     | 12/31/2025 | Prometheus 2.48.0 and Node Exporter 1.10.2 deployment with FIPS 140-2 compliant TLS encryption across 6 systems. Addresses SI-4, SC-8, SC-13, AU-2, CM-3, CM-6. |
| AI-Assisted Administration            | 1.0     | 01/31/2026 | SysAdmin Agent Dashboard v2.0 with Explainable AI, feedback collection, evaluation reporting, and CMMC compliance features. Addresses AC-3, AU-2, AU-3, AU-6, SI-4, CA-7. |

**Addendum Locations:**

- Documentation/SSP_Addendums/SSP_Addendum_YARA_Malware_Detection.md
- Documentation/SSP_Addendums/SSP_Addendum_Workstation_Monitoring.md
- Documentation/SSP_Addendums/SSP_Addendum_AI_Assisted_Administration.md

---

**-- END OF SYSTEM SECURITY PLAN --**

**Document Classification: CONTROLLED UNCLASSIFIED INFORMATION (CUI)**\
**Distribution: Limited to authorized personnel only**\
**Version: 2.10 | Date: May 15, 2026**
