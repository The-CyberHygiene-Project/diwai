# SYSTEM SECURITY PLAN

## NIST SP 800-171 Rev 2 Compliance

[SYSTEM-OWNER] LLC dba [ORGANIZATION]\
**System Name:** [DOMAIN.ORG] SecureMac Reference System\
**Domain:** [DOMAIN.ORG]\
**Version:** 2.11 **Date:** June 5, 2026\
**Classification:** CONFIDENTIAL BUSINESS INFORMATION

**Distribution Notice:** This document contains proprietary business information, trade secrets, and confidential system security details of [SYSTEM-OWNER] LLC. Unauthorized disclosure may cause competitive harm. Upon submission to U.S. Government agencies, this document shall be marked and protected as Controlled Unclassified Information (CUI) per 32 CFR Part 2002.

## DOCUMENT CONTROL

**Document Status:** Approved — Operational\
**Security Classification:** CONTROLLED UNCLASSIFIED INFORMATION (CUI)\
**Distribution:** Limited to authorized personnel only

| Name / Title | Role | Signature / Date |
|:---|:---|:---|
| [SYSTEM-OWNER], Owner/Principal | System Owner | [SYSTEM-OWNER] _____ Date: 06/05/2026 |
| [SYSTEM-OWNER], Owner/Principal | ISSO | [SYSTEM-OWNER] _____ Date: 06/05/2026 |

**Review Schedule:** Quarterly or upon significant system changes\
**Next Review Date:** September 30, 2026

### Document Revision History

| Version | Date | Author | Description |
|:---|:---|:---|:---|
| 1.0 | 04/10/2026 | [SYSTEM-OWNER] | Initial SSP — [DOMAIN.ORG] SecureMac Reference System. Apple Silicon Mac Mini M4 Pro host with UTM Rocky Linux 9.7 aarch64 FIPS VM. pf firewall operational. Rack installation complete. |
| 1.1 | 04/12/2026 | [SYSTEM-OWNER] | Network cutover complete. services.[DOMAIN.ORG] VM live at [LAN-IP-REDACTED] on LAN interface (en6). 389-DS LDAP directory (dc=diwai,dc=org) operational. |
| 1.2 | 04/15/2026 | [SYSTEM-OWNER] | YubiKey Nano 5C FIPS PIV deployment attempted. Lockout incident: unknown PIV PIN after cert pairing; recovery via sysadmin break-glass account; certs unpaired. Host returns to password-only auth. POA&M-001 opened (YubiKey PIV re-pairing). |
| 1.3 | 05/11/2026 | [SYSTEM-OWNER] | Wazuh SIEM (Manager + Dashboard + Indexer) operational on services.[DOMAIN.ORG] VM. Suricata 7.0.13 IDS deployed. VirusTotal integration operational. Apache httpd + LDAP dashboard auth (securemac.[DOMAIN.ORG]) operational. |
| 1.4 | 05/13/2026 | [SYSTEM-OWNER] | SecureMac dashboard LDAP auth operational. mod_authnz_ldap configured against 389-DS. ACI fix applied for group member reads. |
| 1.5 | 05/15/2026 | [SYSTEM-OWNER] | Infrastructure hardening: nginx 1.31.0 reverse proxy deployed (ai.[DOMAIN.ORG] HTTPS, LAN-only). Open Web UI 0.9.5 bound to localhost only. USB Guard re-enabled (mode: on). Time Machine auto-mount LaunchAgent deployed (17-day backup gap root cause resolved). |
| 1.6 | 05/30/2026 | [SYSTEM-OWNER] | SCAP compliance scanning operational: VM OpenSCAP CUI 102/102 (100%), Mac mSCP 126/134 (94%). Weekly automated scans with compliance dashboard at securemac.[DOMAIN.ORG]. |
| 2.0 | 06/05/2026 | [SYSTEM-OWNER] | **STRUCTURAL CORRECTION:** SSP rewritten from scratch as a [DOMAIN.ORG]-specific document. Prior versions (1.0–1.9) used CyberInABox ([DOMAIN.ORG]) SSP as a structural template, which resulted in conflation of two architecturally distinct systems. This version documents only the [DOMAIN.ORG] SecureMac Reference System. CyberInABox is a separate system with its own SSP and SPRS score. SPRS self-assessment conducted: 98/110 (89.1%). New [DOMAIN.ORG] POAM v1.0 issued concurrently. |
| 2.11 | 06/05/2026 | [SYSTEM-OWNER] | Version numbering aligned with cyberhygiene-docs document series for consistency. Content identical to v2.0. |

---

## EXECUTIVE SUMMARY

### 1.1 Purpose

This System Security Plan documents the security controls implemented for the [DOMAIN.ORG] SecureMac Reference System, which processes, stores, and transmits Controlled Unclassified Information (CUI) and Federal Contract Information (FCI) on behalf of [SYSTEM-OWNER] LLC dba [ORGANIZATION]. This SSP demonstrates compliance with NIST SP 800-171 Rev 2 and supports CMMC Level 2 certification readiness.

### 1.2 System Overview

The [DOMAIN.ORG] SecureMac Reference System is an Apple Silicon-based security reference implementation demonstrating that NIST 800-171 / CMMC Level 2 compliance is achievable using macOS and ARM64 Linux virtualization on a single-appliance platform. The system is architecturally distinct from X86 Linux-based approaches and serves as CyberInABox Reference System #2.

**Architecture:** Apple Silicon (ARM64) Mac Mini M4 Pro running macOS 26.5 (Tahoe) as the host OS, with a UTM-hosted Rocky Linux 9.7 aarch64 FIPS VM providing server services — all on a single physical device.

**SPRS Score:** 98/110 (89.1%) — self-assessed June 5, 2026\
**VM OpenSCAP CUI Compliance:** 102/102 (100%)\
**Mac mSCP Compliance:** 126/134 (94%) — 8 rules pending remediation\
**POA&M Reference:** [DOMAIN.ORG] Unified POAM v1.0 (June 5, 2026)

### 1.3 Compliance Requirements

**Primary Requirements:**
- NIST SP 800-171 Rev 2 — Protecting CUI in Nonfederal Systems and Organizations
- FIPS 140-2 — Cryptographic Module Validation (VM: FIPS mode enabled; Mac: Apple Secure Enclave)
- FAR 52.204-21 — Basic Safeguarding of Covered Contractor Information Systems
- DFARS 252.204-7012 — Safeguarding Covered Defense Information and Cyber Incident Reporting
- CMMC Level 2 — Advanced cybersecurity practices (110 practices)

**Supporting Standards:**
- NIST SP 800-53 Rev 5, NIST SP 800-171A, CIS Controls, mSCP (macOS Security Compliance Project)

### 1.4 Key Findings

**Strengths:**
- Apple M4 Pro Secure Enclave provides hardware-rooted encryption and key management
- FileVault full-disk encryption on Mac host; FIPS 140-2 LUKS on VM
- Rocky Linux 9.7 aarch64 VM runs in FIPS mode — 100% OpenSCAP CUI compliance (102/102)
- Mac host at 94% mSCP compliance (126/134) — 8 rules pending remediation
- Full Wazuh SIEM stack (Manager + Dashboard + Indexer) operational on VM
- Suricata 7.0.13 IDS operational on VM
- nginx reverse proxy restricts AI interface to LAN only — WAN excluded
- USB Guard operational on both host and VM
- OpenVPN server operational on VM
- 389-DS LDAP directory operational; Apache dashboard with LDAP auth
- Login banner confirmed on VM; pf firewall on Mac host

**Outstanding Deficits (see [DOMAIN.ORG] POAM v1.0):**
- 3.5.3 / 3.7.5 — No MFA on VM (SSH pubkey only; no TOTP) and YubiKey PIV unpaired on Mac host
- 3.11.1 — First formal risk assessment not yet conducted (overdue)
- 3.6.3 — IR tabletop exercise not yet conducted
- 3.14.2 — ClamAV daemon inactive on VM; YARA not deployed (compensating: Wazuh FIM + VirusTotal + Suricata; risk acceptance pending)

### 1.5 Authorization

**Full Authorization Granted:** June 5, 2026\
**Authorization Period:** 3 years (through June 4, 2029)\
**Current SPRS:** 98/110 (89.1%) — self-assessed\
**CMMC Level 2 Conditional Eligibility:** ELIGIBLE (score ≥ 80; no single finding > 5 points)

---

## 2. SYSTEM IDENTIFICATION

### 2.1 System Information

**System Name:** [DOMAIN.ORG] SecureMac Reference System\
**System Acronym:** SecureMac\
**System Owner:** [SYSTEM-OWNER] LLC dba [ORGANIZATION]\
**System Type:** General Support System (GSS)\
**Operational Status:** Operational (Full Authorization)\
**Research Context:** CyberInABox Reference System #2 — Apple Silicon / macOS architecture

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

**Information Type:** Federal Contract Information (FCI) / Controlled Unclassified Information (CUI)\
**Confidentiality:** MODERATE\
**Integrity:** MODERATE\
**Availability:** LOW\
**Overall System Categorization:** MODERATE

### 2.5 System Boundary

The [DOMAIN.ORG] SecureMac Reference System boundary encompasses:

1. **Mac Mini M4 Pro** (securemac.[DOMAIN.ORG] / ai.[DOMAIN.ORG]) — physical host
2. **services.[DOMAIN.ORG]** — Rocky Linux 9.7 aarch64 UTM VM running on the Mac Mini
3. **nas.[DOMAIN.ORG]** — Synology 8-bay NAS (Synology NTA-STOR) — supporting infrastructure

**Out of scope / separate systems:**
- CyberInABox ([DOMAIN.ORG]) — architecturally distinct X86 Linux system occupying the same physical rack. Documented under a separate SSP. No shared WAN, no shared domain, no shared services with [DOMAIN.ORG]. Physical co-location only.

### 2.6 Relationship to CyberInABox

The [DOMAIN.ORG] SecureMac Reference System and the CyberInABox system are two independent reference implementations exploring alternative approaches to NIST 800-171 / CMMC Level 2 compliance for very small businesses:

| Attribute | [DOMAIN.ORG] (This SSP) | CyberInABox (Separate SSP) |
|:---|:---|:---|
| Hardware | Apple Mac Mini M4 Pro | X86 HP servers and mini PCs |
| Architecture | ARM64 (Apple Silicon) | x86_64 |
| Host OS | macOS 26.5 (Tahoe) | Rocky Linux 9.7 |
| Virtualization | UTM (ARM64 VM on Mac) | Bare metal Linux |
| Identity | 389-DS LDAP | FreeIPA/Kerberos |
| Firewall | macOS pf (native) | pfSense/pf (Netgate, deprecated) |
| WAN Provider | [ISP-REDACTED] ([WAN-IP-REDACTED]/29) | Separate provider |
| Domain | [DOMAIN.ORG] | [DOMAIN.ORG] |
| SPRS | 98/110 (self-assessed) | 106/110 (independently assessed) |

Physical co-location (shared rack enclosure, shared UPS) is noted in PE controls.

---

## 3. SYSTEM DESCRIPTION

### 3.1 System Purpose and Functions

The [DOMAIN.ORG] SecureMac Reference System provides secure information technology infrastructure for [ORGANIZATION]'s government contracting business operations, and serves as a research platform demonstrating Apple Silicon-based CMMC Level 2 compliance.

**Primary Functions:**
- WAN gateway and firewall (pf on Mac Mini host)
- AI/ML inference server (MLX, Open Web UI — LAN-restricted via nginx proxy)
- Identity and access management (389-DS LDAP directory on VM)
- Security monitoring and threat detection (Wazuh SIEM + Suricata on VM)
- Web services and compliance dashboard (Apache httpd on VM)
- Email services (Postfix + Dovecot on VM)
- Network services (OpenVPN, Unbound DNS, NTP on VM)
- Metrics and monitoring (Prometheus + Grafana on VM)
- Compliance scanning (OpenSCAP on VM, mSCP on Mac host)
- CUI storage and backup (FileVault/LUKS encrypted; Time Machine + NAS archival)

### 3.2 System Components

#### Component 1: Mac Mini M4 Pro Host (securemac.[DOMAIN.ORG] / ai.[DOMAIN.ORG])

**Role:** Physical host, WAN gateway/firewall, AI inference server, management workstation

| Attribute | Value |
|:---|:---|
| Hostname | securemac.[DOMAIN.ORG] / ai.[DOMAIN.ORG] |
| LAN IP | [LAN-IP-REDACTED]/24 (en6 — Thunderbolt USB Ethernet) |
| WAN IP | [WAN-IP-REDACTED]/29 (en0 — embedded Ethernet) |
| OS | macOS 26.5 (Tahoe) — Build 25F71 |
| Hardware | Apple Mac Mini (2024) |
| Chip | Apple M4 Pro SoC (12-core CPU: 8P+4E, 16-core GPU, 16-core Neural Engine) |
| RAM | 64 GB unified memory (LPDDR5X) |
| Storage | NVMe SSD — hardware encryption via Apple Secure Enclave |
| Architecture | ARM64 (Apple Silicon) |

**Security Controls (Mac Host):**
- FileVault full-disk encryption (AES-256, Apple Secure Enclave key storage)
- System Integrity Protection (SIP) enabled
- Gatekeeper application allowlisting
- XProtect + MRT malware detection (Apple native, continuously updated)
- pf firewall — stateful packet inspection, NAT, inbound port restrictions
  - WAN (en0): restricted inbound; NAT outbound
  - LAN (en6/[LAN-IP-REDACTED]x): managed access to VM and NAS
  - MGMT (en1/Wi-Fi/cassinet): management access only — not in CUI data path
- USB Guard — custom implementation (/usr/local/sbin/usb-guard)
  - Mode: enabled (on); polls every 5 seconds via diskutil
  - Allowlisted: Time Machine SSD (UUID: [TM-UUID-REDACTED])
  - All other USB storage blocked and logged
- nginx 1.31.0 reverse proxy — HTTPS only, LAN interface ([LAN-IP-REDACTED]:443)
  - Proxies Open Web UI (ai.[DOMAIN.ORG]); WAN interface excluded
  - TLS: *.[DOMAIN.ORG] wildcard cert; TLSv1.2/1.3 only; HSTS enforced
- Open Web UI 0.9.5 — bound to 127.0.0.1:3000 (localhost only); ENABLE_SIGNUP=false
- AI Model: Magistral-Small-2509-MLX-4bit (MLX native ARM64 inference)
- Time Machine backup to dedicated SSD with LaunchAgent auto-mount
- mSCP compliance baseline: diwai_phase1.yaml — 126/134 rules passing (94%)

**MFA Status (Mac Host):**
YubiKey Nano 5C FIPS present (slot 9A/9C PIV certs present on hardware) but unpaired following lockout incident on 2026-04-15. Host authenticates via password only. Remediation: POA&M-001 (YubiKey PIV re-pairing).

#### Component 2: services.[DOMAIN.ORG] — Rocky Linux 9.7 UTM VM

**Role:** Server services — SIEM, identity, web, email, network, monitoring

| Attribute | Value |
|:---|:---|
| Hostname | services.[DOMAIN.ORG] |
| IP | [LAN-IP-REDACTED]/24 |
| OS | Rocky Linux 9.7 (Blue Onyx) |
| Architecture | aarch64 (ARM64 — UTM VM on Apple M4 Pro) |
| FIPS Mode | Enabled (fips-mode-setup --check: FIPS mode is enabled) |
| OpenSCAP CUI | 102/102 — 100% (weekly automated scan) |

**Services running on VM:**

| Service | Version | Purpose |
|:---|:---|:---|
| 389-DS LDAP | dirsrv@diwai | Identity directory (dc=diwai,dc=org) |
| Apache httpd + PHP-FPM | 2.4.x / 8.x | Dashboard (securemac.[DOMAIN.ORG]) with LDAP auth |
| MariaDB | 10.5 | Database backend for web services |
| Wazuh Manager | 4.14.5 | SIEM — security monitoring, FIM, alerts |
| Wazuh Dashboard | 4.14.5 | SIEM UI (HTTPS on VM) |
| Wazuh Indexer | 4.14.5 | Search/analytics backend |
| Suricata IDS | 7.0.13 | Network intrusion detection |
| Prometheus | 3.11.2 | Metrics collection (targets: VM + localhost) |
| Grafana | 13.0.1 | Metrics visualization |
| Prometheus Node Exporter | — | Host metrics |
| OpenVPN Server | — | Remote access VPN (diwai config) |
| Unbound DNS | — | Recursive DNS resolver |
| Postfix | 3.5.25 | SMTP email server (TLS) |
| Dovecot | 2.3.16 | IMAP/POP3 email server |
| ClamAV (freshclam) | 1.4.3 | AV database updater (daemon inactive — see POA&M-002) |
| fapolicyd | 1.3.x | File access policy / application whitelisting |
| USBGuard | — | USB device control |
| auditd | — | System call auditing |
| firewalld | — | Host firewall |
| rsyslog | — | Log forwarding |
| chronyd | — | NTP time synchronization |

**Malware protection gap:** ClamAV 1.4.3 installed and database kept current via freshclam, but the ClamAV daemon is inactive. YARA has not been deployed. Compensating controls: Wazuh FIM (file integrity monitoring with VirusTotal integration), Suricata network IDS, fapolicyd application whitelisting. Risk acceptance documented in POA&M-002.

#### Component 3: Synology NAS (nas.[DOMAIN.ORG])

**Role:** Supporting infrastructure — CUI storage, log archival, backup target

| Attribute | Value |
|:---|:---|
| Hostname | nas.[DOMAIN.ORG] |
| IP | [LAN-IP-REDACTED]/24 |
| Device | Synology 8-bay NAS (NTA-STOR) |
| Encryption | Folder-level AES-256/SHA-256 (non-FIPS second layer) |

**Note:** Synology folder encryption is not FIPS 140-2 validated. Data arriving from the VM is pre-encrypted by FIPS-validated OpenSSL (AES-256-CBC + PBKDF2/SHA-256) before transfer. The NAS encryption is a defense-in-depth second layer, not a FIPS claim. NAS is classified as supporting infrastructure within the physical security boundary.

### 3.3 Network Topology

```
Internet
    |
Mac Mini M4 Pro (pf firewall)
  WAN: en0 ([WAN-IP-REDACTED]/29)
  LAN: en6 ([LAN-IP-REDACTED]/24)
    |
    +-- services.[DOMAIN.ORG] ([LAN-IP-REDACTED]) -- Rocky Linux 9.7 aarch64 VM
    +-- nas.[DOMAIN.ORG] ([LAN-IP-REDACTED])     -- Synology NAS

DNS (Cloudflare, [DOMAIN.ORG] zone):
  [DOMAIN.ORG] / www   -> [WAN-IP-REDACTED]
  ai.[DOMAIN.ORG]      -> [LAN-IP-REDACTED] (LAN only via nginx)
  mail.[DOMAIN.ORG]    -> [WAN-IP-REDACTED]
  vpn.[DOMAIN.ORG]     -> [WAN-IP-REDACTED]
  securemac.[DOMAIN.ORG] -> [LAN-IP-REDACTED] (VM dashboard)
```

**Physical co-location note:** The Mac Mini M4 Pro shares a locked rack enclosure with CyberInABox ([DOMAIN.ORG]) systems. These are architecturally and logically independent systems. The shared rack provides common physical security controls (PE-2, PE-3, PE-11) documented in TCC-PE-MP-001. No shared network, no shared services, no CA-3 interconnection required beyond physical boundary acknowledgment.

### 3.4 Malware Protection Architecture

| Layer | Technology | Status |
|:---|:---|:---|
| Network IDS/IPS | Suricata 7.0.13 (VM) | Operational |
| File Integrity Monitoring | Wazuh FIM with VirusTotal integration (VM) | Operational |
| Application Whitelisting | fapolicyd (VM) + Gatekeeper (Mac) | Operational |
| Host AV — Mac | XProtect + MRT (Apple native, auto-updated) | Operational |
| Host AV — VM | ClamAV 1.4.3 (DB current via freshclam; daemon inactive) | **Gap — POA&M-002** |
| Pattern scanning | YARA — not deployed | **Gap — POA&M-002** |

---

## 4. SECURITY CONTROL IMPLEMENTATION

**Control Status Legend:**
- **IMPLEMENTED** — Control fully operational and verified
- **ENHANCED** — Control exceeds baseline requirements
- **NOT MET** — Control not implemented; SPRS deficit applies
- **PARTIAL** — Partially implemented; compensating controls documented
- **N/A** — Not applicable to this system

### 4.1 Access Control (AC)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.1.1 | Limit access to authorized users | IMPLEMENTED | 389-DS LDAP directory (dc=diwai,dc=org) manages user identities for VM services. macOS account management for host. SSH key-based access only. nginx proxy restricts AI interface to LAN-authorized users. |
| 3.1.2 | Limit access to authorized functions | IMPLEMENTED | 389-DS group-based RBAC (cn=admins group required for dashboard). sudo on VM for privileged operations. macOS standard user + sudo for host admin. fapolicyd enforces application whitelisting on VM. |
| 3.1.3 | Control flow of CUI | IMPLEMENTED | pf firewall (Mac host) enforces WAN/LAN boundary. firewalld on VM restricts inter-service traffic. nginx proxies AI interface — no direct WAN exposure. TLS/SSH for all data in transit. |
| 3.1.4 | Separation of duties | N/A | Single-person organization. Separation enforced via audit logging, break-glass account, and external review processes. |
| 3.1.5 | Least privilege | IMPLEMENTED | Named user ([USERNAME]) with sudo elevation for privileged operations. No service accounts have unnecessary privileges. fapolicyd limits application execution. |
| 3.1.6 | Non-privileged accounts | IMPLEMENTED | Administrative tasks require explicit sudo. No direct root SSH. All elevated actions logged. |
| 3.1.7 | Prevent non-privileged execution of privileged functions | IMPLEMENTED | fapolicyd application whitelisting on VM. macOS SIP + Gatekeeper on host. SELinux enforcing on VM. |
| 3.1.8 | Limit unsuccessful logon attempts | IMPLEMENTED | PAM faillock on VM (5 attempts / 30-minute lockout). macOS lockout policy on host. |
| 3.1.9 | Privacy and security notices | IMPLEMENTED | Login banner confirmed on VM: "AUTHORIZED USE ONLY — [DOMAIN.ORG] SecureMac Reference System." macOS login banner: configured via /etc/motd equivalent. |
| 3.1.10 | Session lock | IMPLEMENTED | SSH ClientAliveInterval 900s (15 min) on VM. macOS screen lock configured on host. |
| 3.1.11 | Session termination | IMPLEMENTED | SSH ClientAliveCountMax enforced. SSH sessions terminate after idle period. |
| 3.1.12 | Monitor/control remote access | IMPLEMENTED | All SSH sessions logged to rsyslog + Wazuh. Failed login attempts generate Wazuh alerts. |
| 3.1.13 | Cryptographic mechanisms for remote access | IMPLEMENTED | FIPS-approved SSH ciphers on VM (FIPS mode enforces cipher restriction). TLS 1.2/1.3 for all HTTPS services. nginx enforces TLSv1.2/1.3 with HSTS. |
| 3.1.14 | Route remote access via managed access control points | IMPLEMENTED | All external access via pf firewall (Mac host). VPN endpoint (vpn.[DOMAIN.ORG]) for remote administration. |
| 3.1.15 | Authorize remote access prior to connection | IMPLEMENTED | SSH requires key-based authentication. No anonymous access. VPN requires client certificates. |
| 3.1.16 | Authorize wireless access | N/A | Wi-Fi (cassinet SSID) used for management only; not in CUI data path. No wireless APs on CUI network. |
| 3.1.17 | Protect wireless access | N/A | As above. |
| 3.1.18 | Control mobile device connections | IMPLEMENTED | USBGuard enabled on VM (daemon active) and Mac host (custom implementation, mode: on). |
| 3.1.19 | Encrypt CUI on mobile devices | IMPLEMENTED | LUKS AES-256-XTS on VM storage. FileVault (Apple Secure Enclave) on Mac host. |
| 3.1.20 | Control portable storage devices | IMPLEMENTED | USBGuard allowlist on VM. Custom USB Guard on Mac host with Time Machine SSD allowlisted; all others blocked. |
| 3.1.21 | Limit portable storage on external systems | IMPLEMENTED | TCC-AUP-001 prohibits organizational USB devices on non-organizational systems. |
| 3.1.22 | Control CUI on publicly accessible systems | IMPLEMENTED | No CUI on public-facing systems. AI interface (Open Web UI) bound to localhost — no WAN exposure. |

### 4.2 Awareness and Training (AT)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.2.1 | Ensure personnel are aware of security risks | IMPLEMENTED | TCC-SAT-FY2026 delivered: 4-hour training (3 modules — General Security Awareness, Role-Based Technical, Insider Threat). Quiz TCC-SAT-QUIZ-FY2026 (80% pass threshold). Completed 02/17/2026. Records: TCC-SAT-RECORD-FY2026. |
| 3.2.2 | Security awareness training on threats | IMPLEMENTED | Role-based technical module (TCC-SAT-FY2026 Section 2). Annual refresher scheduled FY2027. |
| 3.2.3 | Security training before access and annually | IMPLEMENTED | Training completed prior to CUI access and on annual schedule. Insider Threat module (Section 3) completed. |

### 4.3 Audit and Accountability (AU)

**Status:** All AU controls **IMPLEMENTED**. The VM runs a full Wazuh SIEM stack (Manager 4.14.5 + Dashboard + Indexer) providing centralized, searchable audit logging. auditd captures system calls. rsyslog forwards logs to Wazuh indexer. All audit data stored on encrypted VM storage.

- **AU-2 / 3.3.1:** auditd (system calls), rsyslog (application/system events), Wazuh (security events, FIM, vulnerability data) — comprehensive audit record coverage
- **AU-3 / 3.3.2:** All records include: timestamp, source, event type, outcome, user identity. Wazuh indexer provides long-term searchable retention.
- **AU-6 / 3.3.3:** Wazuh Dashboard provides real-time audit review. Grafana dashboards for metrics. ISSO reviews Wazuh alerts daily.
- **AU-9 / 3.3.8:** Wazuh indexer data restricted to wazuh-indexer service account. auditd logs root-owned. FIPS-encrypted VM storage protects audit partition.

### 4.4 Configuration Management (CM)

**Status:** All CM controls **IMPLEMENTED**.

- **3.4.1 (CM-6):** Configuration baselines enforced via OpenSCAP CUI profile on VM (102/102 passing) and mSCP on Mac host (126/134 — 8 rules pending remediation per POA&M-003). Weekly automated scans; results published to compliance dashboard.
- **3.4.3 (CM-3):** Wazuh FIM monitors critical paths (/etc, /usr/bin, /usr/sbin, /boot) for unauthorized changes. auditd captures file-level system calls.
- **3.4.6–3.4.8:** fapolicyd provides deny-by-default application execution on VM. macOS SIP + Gatekeeper enforces application signing on host.
- **3.4.9:** fapolicyd and Gatekeeper prevent unauthorized software installation.

### 4.5 Identification and Authentication (IA)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.5.1 | Identify system users | IMPLEMENTED | 389-DS LDAP (dc=diwai,dc=org) manages all VM user identities. macOS directory for host. |
| 3.5.2 | Authenticate before access | IMPLEMENTED | SSH key authentication on VM. macOS password authentication on host. LDAP authentication for web dashboard. |
| 3.5.3 | Multi-factor authentication | **NOT MET** | **VM:** SSH pubkey only — no TOTP or second factor configured. **Mac host:** YubiKey Nano 5C FIPS present but PIV certs unpaired following lockout incident (2026-04-15). Host authenticates via password only. Remediation: POA&M-001 (YubiKey re-pairing, Mac host) + POA&M-004 (TOTP deployment, VM). **SPRS deficit: -5 points.** |
| 3.5.4 | Replay-resistant authentication | IMPLEMENTED | SSH uses ephemeral key exchange (replay-resistant by design). TLS session tokens not reusable. FIPS-approved algorithms on VM. |
| 3.5.5–3.5.11 | Password management controls | IMPLEMENTED | 389-DS enforces password complexity, history, aging, and lockout policies. FIPS-compliant password hashing on VM. |

### 4.6 Incident Response (IR)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.6.1 | IR capability | IMPLEMENTED | TCC-IRP-001 (Incident Response Policy and Procedures) approved and effective 11/02/2025. Wazuh provides automated incident detection and alerting. |
| 3.6.2 | Track/document/report incidents | IMPLEMENTED | Wazuh alert workflow with ticketing. POA&M serves as incident tracking record. Wazuh Dashboard provides incident timeline. |
| 3.6.3 | Test IR capability | **NOT MET** | Annual tabletop exercise required by TCC-IRP-001 but not yet conducted. Target: June 30, 2026. **SPRS deficit: -1 point.** |

### 4.7 Maintenance (MA)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.7.1 | Perform maintenance | IMPLEMENTED | dnf-automatic applies security patches on VM. macOS Software Update on host. Wazuh vulnerability detection module identifies unpatched packages. |
| 3.7.2 | Control maintenance tools | IMPLEMENTED | Maintenance activities logged. No remote maintenance tools other than SSH. |
| 3.7.3–3.7.4 | Sanitize/check media | IMPLEMENTED | TCC-PE-MP-001 procedures. Wazuh FIM monitors diagnostic tools. |
| 3.7.5 | MFA for remote maintenance | **NOT MET** | Remote maintenance performed via SSH. SSH pubkey alone is single-factor (possession). No second factor (TOTP) configured on VM. Same gap as 3.5.3 — resolved together under POA&M-004. **SPRS deficit: -3 points.** |
| 3.7.6 | Supervise maintenance | IMPLEMENTED | Single-operator system. All maintenance actions logged via auditd + Wazuh. |

### 4.8 Media Protection (MP)

**Status:** All MP controls **IMPLEMENTED**.
- Storage encrypted: LUKS AES-256-XTS (VM), FileVault/Apple Secure Enclave (Mac host)
- Removable media: USBGuard on VM and Mac host
- Media disposal: TCC-PE-MP-001, Section 2.6 (cryptographic erase / shred)
- Media transport: All CUI transmitted via encrypted channels (TLS/SSH)

### 4.9 Personnel Security (PS)

**Status:** All PS controls **IMPLEMENTED**.
- 3.9.1: System owner holds active DoD Top Secret clearance, exceeding CUI background investigation requirements
- 3.9.2: TCC-PS-001 documents personnel security procedures

### 4.10 Physical Protection (PE)

**Status:** All PE controls **IMPLEMENTED**.

The Mac Mini M4 Pro is housed in a locked 2U rack mount within a free-standing rack enclosure. The rack is locked and located within a secured home office facility with controlled access.

**Shared physical boundary:** The rack also contains CyberInABox (Reference System #1) components. Both systems operate under a single physical security perimeter. PE controls (PE-2 Physical Access Controls, PE-3 Physical Access, PE-11 Emergency Power) cover both systems as shared controls documented in TCC-PE-MP-001.

**Note:** Physical co-location does not create a logical or network interconnection. The two systems are fully independent.

### 4.11 Risk Assessment (RA)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.11.1 | Periodic risk assessment | **NOT MET** | TCC-RA-001 (Risk Management Policy) approved with NIST SP 800-30 methodology. First formal [DOMAIN.ORG]-specific risk assessment has not been conducted. **Target: overdue. SPRS deficit: -3 points.** POA&M-005. |
| 3.11.2 | Vulnerability scanning | IMPLEMENTED | Wazuh vulnerability detection module (continuous, 60-min feed updates). OpenSCAP CUI weekly automated scan on VM. mSCP weekly automated scan on Mac host. |
| 3.11.3 | Remediate vulnerabilities | IMPLEMENTED | dnf-automatic applies security patches. macOS Software Update. Wazuh alerts trigger review workflow. |

### 4.12 Security Assessment (CA)

**Status:** All CA controls **IMPLEMENTED**.

- **3.12.1:** OpenSCAP CUI profile automated weekly scans on VM (102/102). mSCP automated weekly scans on Mac host (126/134). Results published to compliance dashboard at securemac.[DOMAIN.ORG].
- **3.12.2:** [DOMAIN.ORG] POAM v1.0 documents all deficiencies with remediation plans and target dates.
- **3.12.3:** Wazuh provides continuous security monitoring. Suricata provides continuous network monitoring. Weekly compliance scans supplement automated monitoring.
- **3.12.4:** This SSP constitutes the system security plan per 3.12.4.

### 4.13 System and Communications Protection (SC)

**Status:** All SC controls **IMPLEMENTED**.

- **3.13.1 (SC-7):** pf firewall (Mac host) provides boundary protection between WAN, LAN, and MGMT interfaces. firewalld provides host-level boundary on VM. Suricata provides network IDS/IPS on VM.
- **3.13.5:** LAN ([LAN-IP-REDACTED]/24) is segregated from WAN by pf. VM and NAS are not directly reachable from WAN. nginx proxy is the sole WAN-accessible endpoint for internal services.
- **3.13.6:** pf implements default-deny inbound on WAN. firewalld implements default-deny on VM.
- **3.13.8 (SC-8):** All data in transit protected by TLS 1.2/1.3 or SSH. nginx enforces HSTS. FIPS-approved cipher suites on VM.
- **3.13.10:** 389-DS provides PKI and key management for identity credentials. Apple Secure Enclave manages cryptographic keys on Mac host.
- **3.13.11 (SC-13):** FIPS 140-2 mode enabled on Rocky Linux 9.7 VM (verified). Apple Secure Enclave (FIPS 140-2 Level 1) on Mac host.
- **3.13.16:** TLS encryption enforced on all CUI transmission paths.

**Note — FIPS boundary at NAS:** Data leaving the FIPS boundary (VM → NAS) is pre-encrypted using FIPS-validated OpenSSL (AES-256-CBC + PBKDF2/SHA-256). The NAS applies a second AES-256/SHA-256 layer (not FIPS 140-2 validated). The FIPS artifact is the encrypted .enc file — the NAS provides defense-in-depth, not a FIPS claim.

### 4.14 System and Information Integrity (SI)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.14.1 | Flaw remediation | IMPLEMENTED | dnf-automatic (VM), macOS Software Update (host). Wazuh vulnerability detection with CVE correlation. |
| 3.14.2 | Malware protection | **PARTIAL** | **Mac host:** XProtect + MRT + Gatekeeper (Apple native, always active, auto-updated). **VM:** ClamAV 1.4.3 installed; freshclam keeps DB current; daemon inactive (not scanning). YARA not deployed. Compensating controls: Wazuh FIM with VirusTotal integration (cloud multi-engine scanning on FIM events), Suricata network IDS, fapolicyd application whitelisting. Risk acceptance pending formal documentation. **POA&M-002. SPRS deficit: -1 point (risk acceptance under review).** |
| 3.14.3 | Security alerts, advisories, directives | IMPLEMENTED | Wazuh alerts, Suricata IDS signatures auto-updated. dnf-automatic handles OS security advisories. |
| 3.14.4 | Update malicious code protection | IMPLEMENTED | ClamAV freshclam (DB current). XProtect auto-updated by Apple. Suricata rules updated. Wazuh feeds updated. |
| 3.14.5 | Periodic/real-time scans | IMPLEMENTED | Wazuh FIM real-time on critical paths. OpenSCAP weekly. mSCP weekly. Suricata real-time network scanning. |
| 3.14.6 | Monitor for anomalous activity | IMPLEMENTED | Wazuh behavioral analytics + Suricata network IDS. Failed login detection, USB policy violations, anomalous traffic patterns. |
| 3.14.7 | Identify unauthorized use | IMPLEMENTED | Wazuh + Suricata correlation. auditd system-call auditing. Grafana dashboards for anomaly visualization. |

---

## 5. CONTINGENCY PLANNING (CP)

### CP-9 (System Backup)

**Status:** IMPLEMENTED

**Mac Host (securemac.[DOMAIN.ORG]):**
- Time Machine to dedicated encrypted SSD (UUID: [TM-UUID-REDACTED])
- LaunchAgent (org.diwai.mount-tm-drive) ensures SSD auto-mounts at login
- RPO: continuous (Time Machine hourly snapshots)

**VM (services.[DOMAIN.ORG]):**
- Wazuh alert archives: daily encrypted push to NAS (nas.[DOMAIN.ORG]/Logs share)
- Archives encrypted via FIPS-validated OpenSSL before transfer
- VM configuration: documented and reproducible via UTM snapshot + kickstart

**NAS (nas.[DOMAIN.ORG]):**
- Primary long-term archive target for encrypted log data
- Synology folder-level encryption (AES-256/SHA-256) as second layer

### CP-10 (System Recovery)

**Status:** IMPLEMENTED

- Mac host: Time Machine full-system restore + macOS bootable installer
- VM: UTM snapshot restore; alternatively, rebuild from Rocky Linux 9.7 FIPS kickstart
- RTO: < 4 hours; RPO: < 24 hours

---

## 6. SECURITY POLICIES AND PROCEDURES

All policies apply to the [DOMAIN.ORG] SecureMac Reference System as the single-operator system of [SYSTEM-OWNER] LLC. The same policy set covers both CyberInABox and [DOMAIN.ORG] as organizational policies (not system-specific).

| Policy | Document ID | Effective Date |
|:---|:---|:---|
| Incident Response Policy and Procedures | TCC-IRP-001 | 11/02/2025 |
| Risk Management Policy | TCC-RA-001 | 11/02/2025 |
| Personnel Security Policy | TCC-PS-001 | 11/02/2025 |
| Physical and Media Protection Policy | TCC-PE-MP-001 | 11/02/2025 |
| System and Information Integrity Policy | TCC-SI-001 | 11/02/2025 |
| Acceptable Use Policy | TCC-AUP-001 | 11/02/2025 |
| Audit and Accountability Policy | TCC-AAP-001 | 02/15/2026 |
| Configuration Management Policy | TCC-CMP-001 | 02/15/2026 |
| Security Awareness and Training Policy | TCC-ATP-001 | 02/15/2026 |
| Identification and Authentication Policy | TCC-IAP-001 | 02/15/2026 |
| System and Communications Protection Policy | TCC-SCP-001 | 02/15/2026 |

---

## 10. PLAN OF ACTION AND MILESTONES (POA&M)

The complete [DOMAIN.ORG] POA&M is maintained as a standalone document: **[DOMAIN.ORG]_Unified_POAM_v1.0.md** (June 5, 2026).

### POA&M Summary (as of June 5, 2026)

| POA&M ID | Weakness | Control | SPRS | Target | Status |
|:---|:---|:---|:---|:---|:---|
| POA&M-001 | YubiKey PIV re-pairing (Mac host) | 3.5.3, IA-5 | (part of -5) | TBD | PLANNED |
| POA&M-002 | ClamAV daemon / YARA deployment on VM | 3.14.2 | -1 | Q3 2026 | PLANNED |
| POA&M-003 | mSCP 8 failing rules remediation (Mac) | 3.4.1 | — | Q3 2026 | PLANNED |
| POA&M-004 | TOTP MFA deployment on VM | 3.5.3, 3.7.5 | -5 / -3 | Q3 2026 | PLANNED |
| POA&M-005 | First annual risk assessment | 3.11.1 | -3 | **OVERDUE** | OVERDUE |
| POA&M-006 | IR tabletop exercise | 3.6.3 | -1 | 06/30/2026 | ON TRACK |

**Current SPRS:** 98/110 (89.1%) — 3.14.2 risk accepted with compensating controls\
**Target SPRS upon completion:** 110/110 (100%)

---

## 11. IMPLEMENTATION METRICS

### SPRS Score Breakdown

| Req | Control | Weight | Status |
|:---|:---|:---|:---|
| 3.5.3 | Multi-Factor Authentication | -5 | NOT MET |
| 3.7.5 | MFA for Remote Maintenance | -3 | NOT MET |
| 3.11.1 | Periodic Risk Assessment | -3 | NOT MET (OVERDUE) |
| 3.6.3 | IR Tabletop Exercise | -1 | NOT MET |
| 3.14.2 | Malware Protection (VM) | -1 | PARTIAL (risk accept) |
| **All others** | 105 requirements | **0** | **MET** |
| **TOTAL DEFICIT** | | **-13** | |
| **SPRS** | | **97/110** | **88.2%** |

**With 3.14.2 risk accepted (compensating controls documented):** 98/110 (89.1%)

### Control Family Status

| Family | Total | Implemented | Not Met | N/A |
|:---|:---|:---|:---|:---|
| AC — Access Control | 22 | 20 | 1 (3.5.3) | 2 (wireless) |
| AT — Awareness & Training | 3 | 3 | 0 | 0 |
| AU — Audit & Accountability | 9 | 9 | 0 | 0 |
| CM — Configuration Mgmt | 9 | 9 | 0 | 0 |
| IA — Identification & Auth | 11 | 10 | 1 (3.5.3) | 0 |
| IR — Incident Response | 3 | 2 | 1 (3.6.3) | 0 |
| MA — Maintenance | 6 | 5 | 1 (3.7.5) | 0 |
| MP — Media Protection | 9 | 9 | 0 | 0 |
| PS — Personnel Security | 2 | 2 | 0 | 0 |
| PE — Physical Protection | 6 | 6 | 0 | 0 |
| RA — Risk Assessment | 3 | 2 | 1 (3.11.1) | 0 |
| CA — Security Assessment | 4 | 4 | 0 | 0 |
| SC — System & Comms Protection | 16 | 16 | 0 | 0 |
| SI — System & Info Integrity | 7 | 6 | 1 (3.14.2 partial) | 0 |

---

## 12. CONCLUSION

The [DOMAIN.ORG] SecureMac Reference System demonstrates that NIST 800-171 / CMMC Level 2 compliance is achievable on Apple Silicon hardware using macOS and ARM64 Linux virtualization. The current self-assessed SPRS score of 98/110 (89.1%) reflects a system with strong foundational security — full FIPS mode on the VM, 100% OpenSCAP CUI compliance, full Wazuh SIEM stack, Suricata IDS, pf firewall, and comprehensive audit logging — with four tractable gaps remaining.

The primary path to 110/110 is deploying TOTP MFA on the VM (recovers 8 points: 3.5.3 -5, 3.7.5 -3 share the same fix) and completing the overdue annual risk assessment (recovers 3 points). The IR tabletop exercise (June 30 deadline) and ClamAV/YARA remediation complete the picture.

### Priority Action Items

| Priority | Item | SPRS Recovery | Target |
|:---|:---|:---|:---|
| 1 | TOTP MFA on VM (SSH pubkey + TOTP) | +8 pts (3.5.3 + 3.7.5) | Q3 2026 |
| 2 | Annual risk assessment | +3 pts | OVERDUE — immediate |
| 3 | IR tabletop exercise | +1 pt | 06/30/2026 |
| 4 | YubiKey PIV re-pairing (Mac host) | (part of 3.5.3) | TBD |
| 5 | ClamAV daemon / YARA on VM | +1 pt | Q3 2026 |

---

## AUTHORIZATION

**Full Authorization Granted:** June 5, 2026\
**Authorization Period:** 3 years (through June 4, 2029)\
**Authorizing Official:** /s/ [SYSTEM-OWNER], System Owner/ISSO\
**[ORGANIZATION]**\
**Date:** June 5, 2026

---

## APPENDICES

### Appendix A: Acronyms

- **AC** — Access Control; **aarch64** — ARM64 architecture; **ATO** — Authorization to Operate
- **AU** — Audit and Accountability; **CA** — Security Assessment; **CM** — Configuration Management
- **CMMC** — Cybersecurity Maturity Model Certification; **CP** — Contingency Planning
- **CUI** — Controlled Unclassified Information; **CVE** — Common Vulnerabilities and Exposures
- **DFARS** — Defense Federal Acquisition Regulation Supplement; **FAR** — Federal Acquisition Regulation
- **FCI** — Federal Contract Information; **FIM** — File Integrity Monitoring
- **FIPS** — Federal Information Processing Standards; **IA** — Identification and Authentication
- **IDS/IPS** — Intrusion Detection/Prevention System; **IR** — Incident Response
- **ISSO** — Information System Security Officer; **LDAP** — Lightweight Directory Access Protocol
- **LUKS** — Linux Unified Key Setup; **MA** — Maintenance; **MFA** — Multi-Factor Authentication
- **MLX** — Machine Learning eXchange (Apple Silicon inference framework)
- **MP** — Media Protection; **mSCP** — macOS Security Compliance Project
- **NIST** — National Institute of Standards and Technology; **PE** — Physical Protection
- **POA&M** — Plan of Action and Milestones; **PS** — Personnel Security
- **RA** — Risk Assessment; **SC** — System and Communications Protection
- **SIEM** — Security Information and Event Management; **SI** — System and Information Integrity
- **SIP** — System Integrity Protection (macOS); **SSH** — Secure Shell; **SSP** — System Security Plan
- **SPRS** — Supplier Performance Risk System; **TLS** — Transport Layer Security
- **TOTP** — Time-based One-Time Password; **UTM** — Universal Turing Machine (virtualization)

### Appendix B: References

1. NIST SP 800-171 Rev 2 — Protecting CUI in Nonfederal Systems and Organizations
2. NIST SP 800-171A — Assessing Security Requirements for CUI
3. FAR 52.204-21 — Basic Safeguarding of Covered Contractor Information Systems
4. DFARS 252.204-7012 — Safeguarding Covered Defense Information
5. FIPS 140-2 — Security Requirements for Cryptographic Modules
6. CMMC Model Version 2.0 — Cybersecurity Maturity Model Certification
7. 32 CFR Part 2002 — Controlled Unclassified Information
8. macOS Security Compliance Project (mSCP) — github.com/usnistgov/macos_security
9. Wazuh Documentation v4.14.5 — documentation.wazuh.com
10. Rocky Linux 9 SCAP Security Guide — access.redhat.com/documentation
11. NIST SP 800-88 Rev 1 — Guidelines for Media Sanitization

### Appendix C: Supporting Documentation

**Compliance Scanning:**
- VM OpenSCAP scan: /usr/local/bin/oscap-scan.sh (weekly Sunday 02:00)
- Mac mSCP scan: /usr/local/bin/run-mSCP-scan.sh (weekly Sunday 03:00)
- Compliance dashboard: https://securemac.[DOMAIN.ORG] (Apache, LDAP-authenticated)

**Infrastructure:**
- nginx config: /opt/homebrew/etc/nginx/servers/ai.[DOMAIN.ORG].conf
- USB Guard (Mac): /usr/local/sbin/usb-guard, org.diwai.usb-guard LaunchDaemon
- Time Machine auto-mount: /usr/local/sbin/mount-tm-drive.sh, org.diwai.mount-tm-drive LaunchAgent
- OpenVPN: /etc/openvpn/server/diwai.conf

**Policies:** TCC-IRP-001, TCC-RA-001, TCC-PS-001, TCC-PE-MP-001, TCC-SI-001, TCC-AUP-001, TCC-AAP-001, TCC-CMP-001, TCC-ATP-001, TCC-IAP-001, TCC-SCP-001

### Appendix D: Document Maintenance

This SSP shall be reviewed and updated quarterly or upon significant system changes.

**Next Scheduled Review:** September 30, 2026

**Review Focus Areas:**
- POA&M-004 TOTP MFA deployment status
- POA&M-005 risk assessment completion (OVERDUE)
- POA&M-006 IR tabletop (June 30 deadline)
- mSCP 8 failing rules remediation progress
- Open Web UI and MLX model currency
- macOS 26.x security updates
- Wazuh and Suricata signature updates

---

**— END OF SYSTEM SECURITY PLAN —**

**Document Classification: CONTROLLED UNCLASSIFIED INFORMATION (CUI)**\
**System: [DOMAIN.ORG] SecureMac Reference System**\
**Version: 2.11 | Date: June 5, 2026**
