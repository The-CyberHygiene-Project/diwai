> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# SYSTEM SECURITY PLAN

## NIST SP 800-171 Rev 2 Compliance

[SYSTEM-OWNER] LLC dba [ORGANIZATION]\
**System Name:** [DOMAIN.ORG] SecureMac Reference System\
**Domain:** [DOMAIN.ORG]\
**Version:** 2.14 **Date:** June 29, 2026\
**Classification:** CONFIDENTIAL BUSINESS INFORMATION

**Distribution Notice:** This document contains proprietary business information, trade secrets, and confidential system security details of [SYSTEM-OWNER] LLC. Unauthorized disclosure may cause competitive harm. Upon submission to U.S. Government agencies, this document shall be marked and protected as Controlled Unclassified Information (CUI) per 32 CFR Part 2002.

## DOCUMENT CONTROL

**Document Status:** Approved — Pending Signature\
**Security Classification:** CONTROLLED UNCLASSIFIED INFORMATION (CUI)\
**Distribution:** Limited to authorized personnel only

| Name / Title | Role | Signature / Date |
|:---|:---|:---|
| [SYSTEM-OWNER], Owner/Principal | System Owner | _____ Date: _____ |
| [SYSTEM-OWNER], Owner/Principal | ISSO | _____ Date: _____ |

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
| 1.5 | 05/15/2026 | [SYSTEM-OWNER] | Infrastructure hardening: nginx 1.31.0 reverse proxy deployed (ai.[DOMAIN.ORG] HTTPS, LAN-only). Open Web UI 0.9.5 bound to localhost only. USB Guard re-enabled (mode: on). Time Machine auto-mount LaunchAgent deployed (17-day backup gap root cause resolved). YubiKey PIV lockout incident (round 2): smartcard certs unpaired again; sysadmin break-glass used for recovery. |
| 1.6 | 05/30/2026 | [SYSTEM-OWNER] | SCAP compliance scanning operational: VM OpenSCAP CUI 102/102 (100%), Mac mSCP 126/134 (94%). Weekly automated scans with compliance dashboard at securemac.[DOMAIN.ORG]. |
| 2.0 / 2.11 | 06/05/2026 | [SYSTEM-OWNER] | **STRUCTURAL CORRECTION:** SSP rewritten from scratch as a [DOMAIN.ORG]-specific document. Prior versions (1.0–1.9 of the predecessor conflated SSP) used the CyberInABox (cyberinabox.net) SSP as a structural template, which resulted in conflation of two architecturally distinct systems. This version documents only the [DOMAIN.ORG] SecureMac Reference System. CyberInABox is a separate system with its own SSP and SPRS score. SPRS self-assessment conducted: 98/110 (89.1%). New [DOMAIN.ORG] POA&M v1.0 issued concurrently. (Version numbering aligned with cyberhygiene-docs series; 2.0 and 2.11 are identical in content.) |
| **2.12** | **06/06/2026** | **[SYSTEM-OWNER]** | **MFA STRATEGY CHANGE — YUBIKEY ABANDONED:** YubiKey Nano 5C FIPS PIV hardware-token approach abandoned for the Mac host after a second lockout incident confirmed the solution is too technically fragile for reliable production use (PIV PIN lockout, certificate-pairing brittleness — see 1.2 and 1.5 above). MFA strategy for the Mac host changed to **TOTP via Authenticator app (RFC 6238)** — the same approach already targeted for the services.[DOMAIN.ORG] VM, unifying the remediation path for 3.5.3/3.7.5 across the whole [DOMAIN.ORG] system. **POA&M-001 (YubiKey PIV re-pairing) closed — superseded by strategy change.** New item **POA&M-007** opened: TOTP Authenticator app enrollment on the Mac host (dshannon account). IA Policy (TCC-IAP-001) updated to v1.1 to reflect the unified TOTP approach. SPRS unchanged: 98/110 (89.1%) — gap remains open until POA&M-004 and POA&M-007 are both complete. |
| **2.12 (finalized)** | **06/11/2026** | **[SYSTEM-OWNER]** | **FINALIZED FOR SIGNATURE.** Open Drafting Questions resolved: (1) POA&M numbering retained as [DOMAIN.ORG]-specific (POA&M-001 closed / POA&M-007 opened), not renumbered to the conflated CPN's POA&M-046/047; (2) shared CyberInABox controls (policy set §6, physical perimeter §4.10, NAS FIPS-boundary note §4.13) remain documented inline as common controls, not split into a separate document — **superseded by the "2.12 (corrected)" entry below**. DRAFT NOTE and Open Drafting Question callouts removed; **Document Status** changed to **Approved — Pending Signature**. **Document ID correction:** the Rev. 2.12 (06/06/2026) entry above cites "TCC-IAP-001" — this is incorrect. TCC-IAP-001 is a CyberInABox/CPN-scoped document (FreeIPA-based MFA, dated 02/15/2026) and does not describe [DOMAIN.ORG]. The [DOMAIN.ORG]-specific Identification and Authentication Policy is **DIWAI-IAP-001** (v1.0, 04/10/2026 — the document that actually documents the YubiKey approach abandoned 06/06/2026). **DIWAI-IAP-001 has now been updated to v1.1** (06/11/2026) to reflect the unified TOTP MFA strategy. `[DOMAIN.ORG]_Unified_POAM_v1.1.md` (POA&M-001 through POA&M-007) has also been authored, in `Compliance/POAM/`. Both companion-document items tracked in Appendix D during the initial finalization pass are now resolved; §6, Appendix C, and §4.5 below have been corrected from TCC-IAP-001 to DIWAI-IAP-001 accordingly. (A broader review of the remaining `TCC-*-001` citations in §6/Appendix C against the parallel `DIWAI-*-001` policy set is recommended — see Appendix D Review Focus Areas — but is out of scope for this finalization pass.) |
| **2.12 (corrected)** | **06/11/2026** | **[SYSTEM-OWNER]** | **INDEPENDENCE DETERMINATION — FULL DOCUMENT-ID PURGE.** Per explicit direction: *"[DOMAIN.ORG] shares [no] company policies with another reference system. It is an independent system and it is a stand-alone."* This supersedes item (2) of the "2.12 (finalized)" entry above — [DOMAIN.ORG]'s policy set, controls, and evidence are NOT shared, common, or inherited with the CyberInABox/CPN reference system, even where physical co-location (shared rack) is a true underlying fact. Changes made: **(a)** all 10 remaining `TCC-*-001` policy citations in §6 and Appendix C corrected to their `DIWAI-*-001` equivalents (v1.0, 04/10/2026): DIWAI-IRP-001, DIWAI-RA-001, DIWAI-PS-001, DIWAI-PE-MP-001, DIWAI-SI-001, DIWAI-AUP-001, DIWAI-AAP-001, DIWAI-CMP-001, DIWAI-ATP-001, DIWAI-SCP-001 (DIWAI-IAP-001 v1.1 already corrected in the prior entry); **(b)** ~9 inline citations corrected throughout §3/§4 (3.1.21 AUP/USB → DIWAI-AUP-001 §4.2; 3.6.1/3.6.3 → DIWAI-IRP-001; 3.7.3-3.7.4 and media disposal → DIWAI-PE-MP-001 §4.5, correcting a stale "§2.6" section reference; 3.9.2 → DIWAI-PS-001; 3.11.1 → DIWAI-RA-001); **(c)** former §3.3 and §4.10 "shared physical security controls... inherited by both SSPs" notes rewritten — [DOMAIN.ORG]'s physical/media protection controls are now documented solely via DIWAI-PE-MP-001, independent of any physical co-location; **(d)** §4.2 (3.2.1, 3.2.2, 3.2.3) downgraded **IMPLEMENTED → PARTIAL** after removing the sole supporting citation, "TCC-SAT-FY2026" (a CyberInABox-specific training-completion record) — no [DOMAIN.ORG]-specific security-awareness training delivery/completion record exists. **New POA&M-008 opened** ([DOMAIN.ORG]-specific security awareness training delivery + records, target Q3 2026, SPRS impact **TBD — pending confirmation**, see §10/§11/§12). **`[DOMAIN.ORG]_Unified_POAM_v1.1.md` updated to v1.1 (corrected)** to add POA&M-008. The 98/110 (89.1%) SPRS figure appearing elsewhere in this document is the **last-confirmed score and does not yet reflect POA&M-008** — see §11 caveat. |
| **2.14** | **06/29/2026** | **[SYSTEM-OWNER]** | **NEXTCLOUD CUI REPOSITORY DOCUMENTED — APPLICATION-LAYER MFA.** The Nextcloud private-cloud document repository (32.0.11.1), in production on the Mac host since 06/11/2026 as the canonical store for CUI/FCI documents (SSP, POA&M, SBOM, evidence), is now documented as an in-boundary system component. **(a)** §3.2 adds Nextcloud + its supporting services (Homebrew PHP-FPM 8.3, Redis, Collabora Online/`richdocuments` 9.1.0 loopback-bound) to the Mac host component; §3.3 adds the `cloud.[DOMAIN.ORG]` LAN-only endpoint. **(b)** §4.5 (3.5.3) records that **Nextcloud enforces TOTP 2FA (`twofactor_totp`) instance-wide** (operator enrolled with backup codes, confirmed 06/11/2026) — an implemented application-layer MFA control over the CUI repository, added to §1.4 Strengths. **This does not change the 3.5.3 SPRS scoring:** host-OS login and VM SSH remain single-factor (POA&M-004/007), so 3.5.3 stays **NOT MET** and the SPRS figure is unchanged at 98/110. **(c)** §4.1 (3.1.1/3.1.2) and §4.8/§4.13 (SC-28) updated for Nextcloud LDAPS group-based access control (`cn=cui-users`) and FileVault at-rest encryption of the Nextcloud data directory; §4.3 (AU) notes Nextcloud `admin_audit` is enabled (Wazuh log-forwarding for `nextcloud.log` pending — tracked as a deployment task, not a control gap). No control status other than the additions above changed; SBOM (v3.0) and POA&M (v1.2) already reflect Nextcloud. |
| **2.13** | **06/12/2026** | **[SYSTEM-OWNER]** | **INDEPENDENT GAP ASSESSMENT — SI-3 SUBSTITUTION & ARCHITECTURE DIAGRAMS** (assessment: `Compliance/Assessment/RS2_Gap_Assessment_2026-06-12.md`). **(a) §3.14.2 (SI-3) rewritten:** ClamAV was found **non-functional under FIPS** (cannot download/load/verify any signature database) and has been **decommissioned**. Malicious-code protection is now provided by an already-operational, FIPS-native stack — **YARA 4.5.2 (5,972 rules, Wazuh-integrated on FIM 550/554) + a new weekly full-system YARA scan + VirusTotal + fapolicyd + SELinux + Suricata** (evidence **DIWAI-EV-SI3-002**, superseding RISK-2026-004). 3.14.2 raised **PARTIAL → IMPLEMENTED**; **POA&M-002 CLOSED**. *Correction: YARA was in fact already deployed on this VM — prior text stating otherwise was inaccurate.* **(b)** Two newly-found, now-closed items recorded: **POA&M-009** (Mac host Wazuh agent restored after ~12 days offline — config XML + ownership repair) and **POA&M-010** (VM time-sync drift, AU-8, corrected + made durable). **(c)** Architecture diagrams added as referenced figures (§3.3, §3.4, Appendix C): `RS2_Network_Schematic` and `RS2_CUI_DataFlow` in `Compliance/Architecture/`. POA&M companion updated to **v1.2**. |

---

## EXECUTIVE SUMMARY

### 1.1 Purpose

This System Security Plan documents the security controls implemented for the **[DOMAIN.ORG] SecureMac Reference System**, which processes, stores, and transmits Controlled Unclassified Information (CUI) and Federal Contract Information (FCI) on behalf of [SYSTEM-OWNER] LLC dba [ORGANIZATION]. This SSP demonstrates compliance with NIST SP 800-171 Rev 2 and supports CMMC Level 2 certification readiness.

### 1.2 System Overview

The [DOMAIN.ORG] SecureMac Reference System is an Apple Silicon-based security reference implementation demonstrating that NIST 800-171 / CMMC Level 2 compliance is achievable using macOS and ARM64 Linux virtualization on a single-appliance platform. The system is architecturally distinct from the X86 Linux-based CyberInABox approach and serves as **CyberInABox Reference System #2**.

**Architecture:** Apple Silicon (ARM64) Mac Mini M4 Pro running macOS 26.5 (Tahoe) as the host OS, with a UTM-hosted Rocky Linux 9.7 aarch64 FIPS VM (services.[DOMAIN.ORG]) providing server services — all on a single physical device.

**SPRS Score:** 98/110 (89.1%) — self-assessed June 5, 2026; last-confirmed figure, does not yet reflect POA&M-008 (see §11)\
**VM OpenSCAP CUI Compliance:** 102/102 (100%)\
**Mac mSCP Compliance:** 126/134 (94%) — 8 rules pending remediation (POA&M-003)\
**POA&M Reference:** `[DOMAIN.ORG]_Unified_POAM_v1.2.md` (companion document, `Compliance/POAM/`; see Appendix D)

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
- nginx reverse proxy restricts AI interface (ai.[DOMAIN.ORG]) to LAN only — WAN excluded
- USB Guard operational on both host (custom implementation) and VM (USBGuard)
- OpenVPN server operational on VM
- 389-DS LDAP directory operational; Apache dashboard with LDAP auth (securemac.[DOMAIN.ORG])
- Login banner confirmed on VM; pf firewall on Mac host (WAN/LAN/MGMT segregation)
- Time Machine backup auto-mount resolved — 17-day gap root cause corrected (05/15/2026)
- **MFA strategy unified (06/06/2026):** A single remediation path (TOTP via Authenticator app, RFC 6238) now covers both the Mac host and the VM, replacing the more fragile dual-track plan (YubiKey PIV + separate VM TOTP). See POA&M-004 and POA&M-007.
- **CUI repository enforces MFA (06/11/2026):** The Nextcloud private-cloud document repository — the canonical store for all CUI/FCI documents — enforces TOTP two-factor authentication (`twofactor_totp`) instance-wide on every login, layered on LDAPS-backed identity. Application-layer MFA over the CUI store is therefore already in production, even though host-OS and VM-SSH MFA remain pending (POA&M-004/007). See §3.2 and §4.5.

**Outstanding Deficits (see [DOMAIN.ORG] POA&M v1.2):**
- 3.5.3 / 3.7.5 — No MFA currently active on either system component: VM has SSH pubkey only (no TOTP); Mac host authenticates by password only following the YubiKey abandonment. Unified remediation: POA&M-004 (VM) + POA&M-007 (Mac host).
- 3.11.1 — First formal risk assessment not yet conducted (overdue) — POA&M-005
- 3.6.3 — IR tabletop exercise not yet conducted — POA&M-006
- 3.14.2 — **RESOLVED 06/12/2026:** malicious-code protection met by the YARA stack (YARA + VirusTotal + fapolicyd + SELinux + Suricata); ClamAV decommissioned (non-functional under FIPS). POA&M-002 closed — DIWAI-EV-SI3-002.

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
**Business Location:** Albuquerque, New Mexico

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
2. **services.[DOMAIN.ORG]** — Rocky Linux 9.7 aarch64 UTM VM running on the Mac Mini ([LAN-IP-REDACTED])
3. **nas.[DOMAIN.ORG]** — Synology 8-bay NAS ([LAN-IP-REDACTED]) — supporting infrastructure

**Out of scope / separate systems:**
- CyberInABox (cyberinabox.net) — architecturally distinct X86 Linux system (dc1.cyberinabox.net domain controller + LabRat/Engineering/Accounting workstations) occupying the same physical rack. Documented under its own SSP (System_Security_Plan — CyberHygiene Production Network). No shared WAN, no shared domain, no shared services with [DOMAIN.ORG]. Physical co-location only.

### 2.6 Relationship to CyberInABox

The [DOMAIN.ORG] SecureMac Reference System and the CyberInABox system are two independent reference implementations exploring alternative approaches to NIST 800-171 / CMMC Level 2 compliance for very small businesses:

| Attribute | [DOMAIN.ORG] (This SSP) | CyberInABox (Separate SSP) |
|:---|:---|:---|
| Hardware | Apple Mac Mini M4 Pro | X86 HP servers and mini PCs |
| Architecture | ARM64 (Apple Silicon) | x86_64 |
| Host OS | macOS 26.5 (Tahoe) | Rocky Linux 9.7 |
| Virtualization | UTM (ARM64 VM on Mac) | Bare metal Linux |
| Identity | 389-DS LDAP (dc=diwai,dc=org) | FreeIPA/Kerberos |
| Firewall | macOS pf (native) | pfSense/pf (Netgate, deprecated) |
| WAN Provider | [ISP-REDACTED] ([WAN-IP-REDACTED]/29) | Separate provider |
| Domain | [DOMAIN.ORG] | cyberinabox.net |
| SPRS | 98/110 (self-assessed 06/05/2026) | 106/110 (independently assessed) |

Physical co-location (shared rack enclosure, shared UPS) is noted in PE controls (4.10).

---

## 3. SYSTEM DESCRIPTION

### 3.1 System Purpose and Functions

The [DOMAIN.ORG] SecureMac Reference System provides secure information technology infrastructure for [ORGANIZATION]'s government contracting business operations, and serves as a research platform demonstrating Apple Silicon-based CMMC Level 2 compliance.

**Primary Functions:**
- WAN gateway and firewall (pf on Mac Mini host)
- AI/ML inference server (MLX + Open Web UI — LAN-restricted via nginx reverse proxy)
- CUI/FCI document management — Nextcloud private cloud (LAN-restricted via nginx reverse proxy; MFA-enforced) with Collabora Online in-browser office editing
- Identity and access management (389-DS LDAP directory on VM)
- Security monitoring and threat detection (Wazuh SIEM + Suricata on VM)
- Web services and compliance dashboard (Apache httpd on VM)
- Email services (Postfix + Dovecot + Roundcube on VM)
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
| WAN IP | [WAN-IP-REDACTED]/29 (en0 — embedded Ethernet, [ISP-REDACTED]) |
| MGMT | en1 — Wi-Fi ([MGMT-IP-REDACTED]) — management access only, not in CUI data path |
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
  - LAN (en6/[LAN-IP-REDACTED]): managed access to VM and NAS
  - MGMT (en1/Wi-Fi): management access only — never blocked, not in CUI data path
- USB Guard — custom implementation (`/usr/local/sbin/usb-guard`, `/usr/local/sbin/usb-guard-monitor`)
  - Mode: enabled (on); polls every 5 seconds via `diskutil` / `ioreg`
  - Allowlisted: Time Machine SSD (UUID: E2EBAB82-18DA-4F2D-8257-C05AE6CE42F1)
  - All other USB mass storage force-ejected and logged to `/var/log/usb-guard.log`
  - LaunchDaemon: `org.diwai.usb-guard`
- nginx 1.31.0 reverse proxy (Homebrew, ARM64) — HTTPS only, LAN interface ([LAN-IP-REDACTED]:443)
  - Proxies Open Web UI at https://ai.[DOMAIN.ORG]; WAN interface (en0) excluded
  - TLS: *.[DOMAIN.ORG] wildcard certificate (`/etc/ssl/diwai/[DOMAIN.ORG].crt`); TLSv1.2/1.3 only; HSTS enforced (max-age=31536000; includeSubDomains)
  - WebSocket proxying enabled (required for streaming AI responses)
  - LaunchDaemon: `org.diwai.nginx`; config: `/opt/homebrew/etc/nginx/servers/ai.[DOMAIN.ORG].conf`
- Open Web UI 0.9.5 (Python venv: `/opt/local/open-webui-venv`) — bound to 127.0.0.1:3000 (localhost only); ENABLE_SIGNUP=false; single admin account (dshannon); LaunchDaemon: `org.diwai.open-webui`
- AI Model: Magistral-Small-2509-MLX-4bit (MLX native, Metal Performance Shaders — no Ollama dependency); location `/opt/local/models/Magistral-Small-2509-MLX-4bit`
- **Nextcloud 32.0.11.1 private-cloud CUI/FCI document repository** (`/opt/local/nextcloud`, data dir `/opt/local/nextcloud/data` — FileVault-encrypted at rest) — the canonical store for CUI/FCI documents (SSP, POA&M, SBOM, evidence)
  - Served at `https://cloud.[DOMAIN.ORG]` via the nginx reverse proxy on the LAN interface ([LAN-IP-REDACTED]:443) and loopback only — **never exposed to WAN**, no public DNS record (local resolution only)
  - Runtime: Homebrew PHP-FPM 8.3 + local Redis (127.0.0.1:6379) cache/locking
  - Identity: 389-DS via **LDAPS** (`ldaps://services.[DOMAIN.ORG]:636`, base `dc=diwai,dc=org`); database: MariaDB on the VM
  - **MFA: TOTP two-factor authentication (`twofactor_totp`) enforced instance-wide** (operator enrolled with TOTP + backup codes, confirmed 06/11/2026); `admin_audit` enabled; `session_lifetime=1800`, `remember_login_cookie_lifetime=0`
  - Group-based access control via 389-DS groups (`cn=cui-users` restricts the CUI groupfolder; `cn=users` for Operations/AI-Knowledge-Base)
  - Office editing: Collabora Online (`richdocuments` 9.1.0) bound to loopback (127.0.0.1:9980), reached only by Nextcloud's PHP backend over the WOPI protocol — never exposed through nginx or the LAN; the nginx reverse proxy remains the sole CUI-bearing TLS boundary
- Time Machine backup to dedicated SSD with auto-mount LaunchAgent (`org.diwai.mount-tm-drive`, script `/usr/local/sbin/mount-tm-drive.sh`) — RunAtLoad, fires 5 seconds after login; resolved a FileVault-encrypted-volume auto-mount failure that caused a 17-day backup gap (2026-04-28 to 2026-05-14)
- mSCP compliance baseline: `diwai_phase1.yaml` — 126/134 rules passing (94%); weekly automated scan, results published to compliance dashboard (POA&M-003 tracks the 8 failing rules)

**MFA Status (Mac Host) — UPDATED 06/06/2026:**
YubiKey Nano 5C FIPS PIV hardware-token authentication was attempted twice (lockout incidents 2026-04-15 and 2026-05-15; both recovered via sysadmin break-glass, certs unpaired both times). Following the second incident, the approach was judged too technically fragile for reliable production use and **abandoned on 2026-06-06**. The Mac host's MFA strategy now follows the same path as the VM and the CyberInABox Linux systems: **TOTP via Authenticator app (RFC 6238)**. Current state: dshannon authenticates via password only. Remediation: **POA&M-007** (TOTP Authenticator app enrollment, Mac host). POA&M-001 (YubiKey re-pairing) is **closed — superseded**.

#### Component 2: services.[DOMAIN.ORG] — Rocky Linux 9.7 UTM VM

**Role:** Server services — SIEM, identity, web, email, network, monitoring

| Attribute | Value |
|:---|:---|
| Hostname | services.[DOMAIN.ORG] |
| IP | [LAN-IP-REDACTED]/24 |
| OS | Rocky Linux 9.7 (Blue Onyx) |
| Architecture | aarch64 (ARM64 — UTM VM on Apple M4 Pro) |
| FIPS Mode | Enabled (`fips-mode-setup --check`: FIPS mode is enabled) |
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
| Prometheus | 3.11.2 | Metrics collection |
| Grafana | 13.0.1 | Metrics visualization |
| Prometheus Node Exporter | — | Host metrics |
| OpenVPN Server | — | Remote access VPN (diwai config) |
| Unbound DNS | — | Recursive DNS resolver |
| Postfix | 3.5.25 | SMTP email server (TLS) |
| Dovecot | 2.3.16 | IMAP/POP3 email server |
| Roundcube | — | Webmail (AES-256-CBC cipher config + FPM pool fix applied for FIPS compatibility) |
| YARA | 4.5.2 | Malicious-code pattern scanner — 5,972 rules, Wazuh-integrated on FIM events + weekly full-system scan (SI-3 primary, FIPS-native). *ClamAV 1.4.3 decommissioned 06/12/2026 — non-functional under FIPS; see DIWAI-EV-SI3-002.* |
| fapolicyd | 1.3.x | File access policy / application whitelisting |
| USBGuard | — | USB device control |
| auditd | — | System call auditing |
| firewalld | — | Host firewall |
| rsyslog | — | Log forwarding |
| chronyd | — | NTP time synchronization |

**Malicious-code protection (SI-3):** Provided by **YARA 4.5.2** (5,972 rules), integrated with Wazuh active-response on FIM rules 550/554 (new/modified files) and supplemented by a **weekly full-system YARA scan** (`yara-fullscan.timer`). Layered with **VirusTotal** reputation lookups, **fapolicyd** application allow-listing, **SELinux** enforcing, and **Suricata** network IDS — all FIPS-native. *ClamAV 1.4.3 was decommissioned on 06/12/2026: under FIPS it could neither download nor load any signature database (OpenSSL verification failure), so it provided no detection. The control substitution is documented in `Compliance/Evidence/SI-3_Control_Substitution_ClamAV_Decommission_2026-06-12.md` (DIWAI-EV-SI3-002), which supersedes RISK-2026-004. POA&M-002 is closed.*

#### Component 3: Synology NAS (nas.[DOMAIN.ORG])

**Role:** Supporting infrastructure — CUI storage, log archival, backup target

| Attribute | Value |
|:---|:---|
| Hostname | nas.[DOMAIN.ORG] |
| IP | [LAN-IP-REDACTED]/24 |
| Device | Synology 8-bay NAS |
| Encryption | Folder-level AES-256/SHA-256 (non-FIPS second layer) |
| Shares | DataStore (SMB; LDAP-authenticated against services.[DOMAIN.ORG] 389-DS) |

**Note:** Synology folder encryption is not FIPS 140-2 validated. Data arriving from the VM (Wazuh alert archives) is pre-encrypted by FIPS-validated OpenSSL (AES-256-CBC + PBKDF2/SHA-256) before transfer over SSH (AES-256-CTR). The NAS encryption is a defense-in-depth second layer, not a FIPS claim. NAS is classified as **supporting infrastructure** within the physical security boundary — not as part of the FIPS cryptographic boundary itself.

### 3.3 Network Topology

```
Internet
    |
Mac Mini M4 Pro (pf firewall)
  WAN: en0 ([WAN-IP-REDACTED]/29 -- [ISP-REDACTED])
  LAN: en6 ([LAN-IP-REDACTED]/24 -- Thunderbolt USB Ethernet)
  MGMT: en1 (Wi-Fi, [MGMT-IP-REDACTED] -- never blocked, not in CUI path)
    |
    +-- services.[DOMAIN.ORG] ([LAN-IP-REDACTED]) -- Rocky Linux 9.7 aarch64 VM
    +-- nas.[DOMAIN.ORG] ([LAN-IP-REDACTED])     -- Synology 8-bay NAS

DNS ([DOMAIN.ORG] zone):
  [DOMAIN.ORG] / www         -> [WAN-IP-REDACTED]
  ai.[DOMAIN.ORG]            -> [LAN-IP-REDACTED]   (LAN only, via nginx reverse proxy)
  cloud.[DOMAIN.ORG]         -> [LAN-IP-REDACTED]   (LAN only, via nginx reverse proxy; Nextcloud)
  mail.[DOMAIN.ORG]          -> [WAN-IP-REDACTED]
  vpn.[DOMAIN.ORG]           -> [WAN-IP-REDACTED]
  securemac.[DOMAIN.ORG]     -> [LAN-IP-REDACTED]  (VM dashboard, LDAP-authenticated)
```

> **Figure 3.3 — Network & Software-Stack Schematic:** see `Compliance/Architecture/RS2_Network_Schematic.svg` (editable source `RS2_Network_Schematic.drawio`) for the full device-level topology, per-node software stack, trust boundaries, and the LAN-only AI egress control.

**Physical co-location note:** The Mac Mini M4 Pro shares a locked rack enclosure with CyberInABox (cyberinabox.net) systems. These are architecturally and logically independent, standalone systems — no shared network, no shared services, no CA-3 interconnection beyond physical-boundary acknowledgment, and no shared policy set. The rack's physical security controls (PE-2, PE-3, PE-11) for the [DOMAIN.ORG] system are documented independently in DIWAI-PE-MP-001.

### 3.4 Malware Protection Architecture

| Layer | Technology | Status |
|:---|:---|:---|
| Network IDS/IPS | Suricata 7.0.13 (VM) | Operational |
| File Integrity Monitoring | Wazuh FIM with VirusTotal integration (VM) | Operational |
| Application Whitelisting | fapolicyd (VM) + Gatekeeper (Mac) | Operational |
| Host AV — Mac | XProtect + MRT (Apple native, auto-updated) | Operational |
| Malicious-code scanning — VM | **YARA 4.5.2** (5,972 rules) — Wazuh active-response on FIM 550/554 + **weekly full-system scan** (`yara-fullscan.timer`) | **Operational** (FIPS-native) |
| Reputation | VirusTotal (hash lookup on FIM events) | Operational |
| *(retired)* Host AV — VM | ~~ClamAV 1.4.3~~ — **decommissioned 06/12/2026**; non-functional under FIPS, replaced by the YARA stack (DIWAI-EV-SI3-002) | Retired |

> **Figure 3.4 — CUI Data-Flow:** see `Compliance/Architecture/RS2_CUI_DataFlow.svg` (editable `.drawio`) — how CUI is received over encrypted channels, authenticated at 389-DS with MFA, processed in-boundary (incl. the air-gapped AI), stored encrypted at rest, continuously monitored, and backed up.

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
| 3.1.1 | Limit access to authorized users | IMPLEMENTED | 389-DS LDAP directory (dc=diwai,dc=org) manages user identities for VM services. macOS account management for the Mac host. SSH key-based access only. nginx proxy restricts the AI and Nextcloud interfaces to LAN-authorized users. Nextcloud authenticates against 389-DS over LDAPS and enforces TOTP 2FA on every login (see 3.5.3). |
| 3.1.2 | Limit access to authorized functions | IMPLEMENTED | 389-DS group-based RBAC (cn=admins group required for dashboard access). Nextcloud groupfolder access is group-restricted (cn=cui-users for the CUI groupfolder; cn=users for Operations/AI-Knowledge-Base). sudo on the VM for privileged operations. macOS standard user + sudo for host admin. fapolicyd enforces application whitelisting on the VM. |
| 3.1.3 | Control flow of CUI | IMPLEMENTED | pf firewall (Mac host) enforces WAN/LAN/MGMT boundaries. firewalld on the VM restricts inter-service traffic. nginx proxies the AI interface — no direct WAN exposure. TLS/SSH for all data in transit. |
| 3.1.4 | Separation of duties | N/A | Single-person organization. Separation enforced via audit logging, the break-glass account, and external review processes. |
| 3.1.5 | Least privilege | IMPLEMENTED | Named user (dshannon) with sudo elevation for privileged operations. No service accounts hold unnecessary privileges. fapolicyd limits application execution on the VM. |
| 3.1.6 | Non-privileged accounts | IMPLEMENTED | Administrative tasks require explicit sudo. No direct root SSH. All elevated actions logged. |
| 3.1.7 | Prevent non-privileged execution of privileged functions | IMPLEMENTED | fapolicyd application whitelisting on the VM. macOS SIP + Gatekeeper on the host. SELinux enforcing on the VM. |
| 3.1.8 | Limit unsuccessful logon attempts | IMPLEMENTED | PAM faillock on the VM (5 attempts / 30-minute lockout). macOS lockout policy on the host. |
| 3.1.9 | Privacy and security notices | IMPLEMENTED | Login banner confirmed on the VM ("AUTHORIZED USE ONLY — [DOMAIN.ORG] SecureMac Reference System"). macOS login banner configured on the host. |
| 3.1.10 | Session lock | IMPLEMENTED | SSH `ClientAliveInterval` 900s (15 min) on the VM. macOS screen lock configured on the host. |
| 3.1.11 | Session termination | IMPLEMENTED | SSH `ClientAliveCountMax` enforced; sessions terminate after the idle period. GUI sessions lock automatically. |
| 3.1.12 | Monitor/control remote access | IMPLEMENTED | All SSH sessions logged to rsyslog + Wazuh. Failed login attempts generate Wazuh alerts. |
| 3.1.13 | Cryptographic mechanisms for remote access | IMPLEMENTED | FIPS-approved SSH ciphers on the VM (FIPS mode enforces cipher restriction). TLS 1.2/1.3 for all HTTPS services. nginx enforces TLSv1.2/1.3 with HSTS. |
| 3.1.14 | Route remote access via managed access control points | IMPLEMENTED | All external access via the pf firewall (Mac host). VPN endpoint (vpn.[DOMAIN.ORG]) for remote administration on the VM. |
| 3.1.15 | Authorize remote access prior to connection | IMPLEMENTED | SSH requires key-based authentication; no anonymous access. VPN requires client certificates. |
| 3.1.16 | Authorize wireless access | N/A | Wi-Fi (en1/MGMT) used for management only — never blocked, not in the CUI data path. No wireless APs in the CUI network. |
| 3.1.17 | Protect wireless access | N/A | As above. |
| 3.1.18 | Control mobile device connections | IMPLEMENTED | USBGuard daemon active on the VM; custom USB Guard (mode: on) on the Mac host. |
| 3.1.19 | Encrypt CUI on mobile devices | IMPLEMENTED | LUKS AES-256-XTS on VM storage (FIPS 140-2). FileVault / Apple Secure Enclave on the Mac host. |
| 3.1.20 | Control portable storage devices | IMPLEMENTED | USBGuard allowlist on the VM. Custom USB Guard on the Mac host with the Time Machine SSD UUID allowlisted; all other USB storage force-ejected and logged. |
| 3.1.21 | Limit portable storage on external systems | IMPLEMENTED | DIWAI-AUP-001 §4.2 prohibits storing CUI on unencrypted portable media and removing CUI from the SPN without approved transfer procedures. USB Guard (Evidence/USBGuard_Configuration_Evidence.md) enforces device-level authorization for portable storage connected to SPN systems. |
| 3.1.22 | Control CUI on publicly accessible systems | IMPLEMENTED | No CUI on public-facing systems. The AI interface (Open Web UI) is bound to localhost — no WAN exposure. |

### 4.2 Awareness and Training (AT)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.2.1 | Ensure personnel are aware of security risks | **PARTIAL** | DIWAI-ATP-001 (Security Awareness and Training Policy, v1.0, 04/10/2026) is approved and establishes the training program (§3.2, AT-2). However, no [DOMAIN.ORG]-specific training delivery/completion record has been produced. The SSP's prior citation of "TCC-SAT-FY2026" was a CyberInABox/CPN-specific training record and has been removed (06/11/2026) per the determination that [DOMAIN.ORG] is an independent, standalone system that does not share evidence with CyberInABox. **POA&M-008** opened to deliver and document [DOMAIN.ORG]-specific initial training. |
| 3.2.2 | Security awareness training on threats | **PARTIAL** | Same gap as 3.2.1 — DIWAI-ATP-001 §3.2 defines annual refresher training requirements, but no [DOMAIN.ORG]-specific delivery/completion record exists yet. **POA&M-008**. |
| 3.2.3 | Security training before access and annually | **PARTIAL** | Same gap as 3.2.1/3.2.2 — DIWAI-ATP-001 establishes the requirement; [DOMAIN.ORG]-specific completion documentation is pending. **POA&M-008**. |

### 4.3 Audit and Accountability (AU)

**Status:** All AU controls **IMPLEMENTED**. The VM runs a full Wazuh SIEM stack (Manager 4.14.5 + Dashboard + Indexer) providing centralized, searchable audit logging. auditd captures system calls; rsyslog forwards logs to the Wazuh indexer. All audit data is stored on encrypted VM storage.

- **AU-2 / 3.3.1:** auditd (system calls), rsyslog (application/system events), Wazuh (security events, FIM, vulnerability data) — comprehensive audit-record coverage.
- **AU-3 / 3.3.2:** All records include timestamp, source, event type, outcome, and user identity. The Wazuh indexer provides long-term searchable retention.
- **AU-6 / 3.3.3:** The Wazuh Dashboard provides real-time audit review; Grafana provides metrics dashboards. The ISSO reviews Wazuh alerts daily.
- **AU-9 / 3.3.8:** Wazuh indexer data is restricted to the wazuh-indexer service account. auditd logs are root-owned. FIPS-encrypted VM storage protects the audit partition.
- **Nextcloud:** the `admin_audit` app is enabled, logging authentication, sharing, and file-access events to `/opt/local/nextcloud/data/nextcloud.log` (JSON). Forwarding this log into Wazuh (decoder + rule) is a pending deployment task, not a control gap — the audit data is captured locally on the FileVault-encrypted host volume in the interim.

### 4.4 Configuration Management (CM)

**Status:** All CM controls **IMPLEMENTED**.

- **3.4.1 (CM-6):** Configuration baselines enforced via the OpenSCAP CUI profile on the VM (102/102 passing) and mSCP on the Mac host (126/134 — 8 rules pending remediation, POA&M-003). Weekly automated scans publish results to the compliance dashboard.
- **3.4.3 (CM-3):** Wazuh FIM monitors critical paths (`/etc`, `/usr/bin`, `/usr/sbin`, `/boot`) for unauthorized changes; auditd captures file-level system calls.
- **3.4.6–3.4.8:** fapolicyd provides deny-by-default application execution on the VM. macOS SIP + Gatekeeper enforces application signing on the host.
- **3.4.9:** fapolicyd and Gatekeeper prevent unauthorized software installation.

### 4.5 Identification and Authentication (IA)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.5.1 | Identify system users | IMPLEMENTED | 389-DS LDAP (dc=diwai,dc=org) manages all VM user identities. macOS directory services manage the host. |
| 3.5.2 | Authenticate before access | IMPLEMENTED | SSH key authentication on the VM. macOS password authentication on the host. LDAP authentication for the web dashboard. |
| 3.5.3 | Multi-factor authentication | **NOT MET** | **Nextcloud CUI repository (cloud.[DOMAIN.ORG]):** **MFA is IMPLEMENTED at the application layer** — Nextcloud enforces TOTP two-factor authentication (`twofactor_totp`) instance-wide on every login, over LDAPS-backed identity, with the operator enrolled (TOTP + backup codes, confirmed 06/11/2026). The canonical CUI/FCI document store therefore already requires MFA. **VM (services.[DOMAIN.ORG]):** SSH pubkey only — no TOTP or second factor configured. Remediation: **POA&M-004**. **Mac host (securemac.[DOMAIN.ORG]):** YubiKey Nano 5C FIPS PIV hardware-token approach was attempted twice and **abandoned 06/06/2026** after a second lockout incident demonstrated the solution is too fragile for production use (see 3.2, Component 1, "MFA Status"). The host now authenticates via password only. The MFA strategy has been changed to **TOTP via Authenticator app (RFC 6238)** — the same approach used on the VM and the CyberInABox Linux systems. Remediation: **POA&M-007**. POA&M-001 (YubiKey re-pairing) is **closed — superseded by this strategy change**. **Status rationale:** despite the Nextcloud application-layer MFA above, this control is scored **NOT MET** because the host-OS login and VM-SSH access paths to the system accounts remain single-factor. **SPRS deficit: -5 points** (unchanged). |
| 3.5.4 | Replay-resistant authentication | IMPLEMENTED | SSH uses ephemeral key exchange (replay-resistant by design). TLS session tokens are not reusable. FIPS-approved algorithms on the VM. |
| 3.5.5–3.5.11 | Password management controls | IMPLEMENTED | 389-DS enforces password complexity, history, aging, and lockout policies. FIPS-compliant password hashing on the VM. |

> **Note on IA Policy version:** The June 6 strategy change required the [DOMAIN.ORG] Identification and Authentication Policy (**DIWAI-IAP-001**, v1.0, 04/10/2026 — corrected from this SSP's earlier "TCC-IAP-001" citation, which refers to a different, CyberInABox/CPN-scoped document) to be updated to reflect the unified TOTP-everywhere approach, replacing the prior text that described YubiKey PIV as the Mac-host MFA mechanism. **DIWAI-IAP-001 v1.1 has been issued (06/11/2026)**: §3.2.3 now documents MFA as NOT MET pending POA&M-004/POA&M-007, and the YubiKey approach is recorded as superseded.

### 4.6 Incident Response (IR)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.6.1 | IR capability | IMPLEMENTED | DIWAI-IRP-001 (Incident Response Policy and Procedures) approved and effective 04/10/2026. Wazuh provides automated incident detection and alerting. |
| 3.6.2 | Track/document/report incidents | IMPLEMENTED | Wazuh alert workflow with ticketing. The POA&M serves as the incident-tracking record (e.g., the two YubiKey lockout incidents of 04/15 and 05/15 are documented in the revision history above and tracked through to closure as POA&M-001). The Wazuh Dashboard provides an incident timeline. |
| 3.6.3 | Test IR capability | **NOT MET** | The annual tabletop exercise required by DIWAI-IRP-001 has not yet been conducted. Target: June 30, 2026. **SPRS deficit: -1 point.** POA&M-006. |

### 4.7 Maintenance (MA)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.7.1 | Perform maintenance | IMPLEMENTED | dnf-automatic applies security patches on the VM. macOS Software Update on the host. Wazuh's vulnerability detection module identifies unpatched packages. |
| 3.7.2 | Control maintenance tools | IMPLEMENTED | Maintenance activities are logged. No remote maintenance tools other than SSH. |
| 3.7.3–3.7.4 | Sanitize/check media | IMPLEMENTED | DIWAI-PE-MP-001 §4.5 (Media Sanitization, MP-6) procedures. Wazuh FIM monitors diagnostic tools. |
| 3.7.5 | MFA for remote maintenance | **NOT MET** | Remote maintenance is performed via SSH. SSH public-key alone is single-factor (possession only) — no second factor (TOTP) is configured on the VM, and the Mac host's MFA gap (3.5.3) applies equally to its remote-administration path. Same root gap as 3.5.3 — resolved together under the unified **POA&M-004 (VM)** + **POA&M-007 (Mac host)** remediation. **SPRS deficit: -3 points.** |
| 3.7.6 | Supervise maintenance | IMPLEMENTED | Single-operator system. All maintenance actions logged via auditd + Wazuh. |

### 4.8 Media Protection (MP)

**Status:** All MP controls **IMPLEMENTED**.
- Storage encrypted: LUKS AES-256-XTS (VM); FileVault / Apple Secure Enclave (Mac host) — covers the Nextcloud CUI/FCI data directory (`/opt/local/nextcloud/data`) at rest
- Removable media: USBGuard on the VM; custom USB Guard on the Mac host
- Media disposal: DIWAI-PE-MP-001 §4.5 (cryptographic erase / shred)
- Media transport: all CUI transmitted via encrypted channels (TLS/SSH)

### 4.9 Personnel Security (PS)

**Status:** All PS controls **IMPLEMENTED**.
- 3.9.1: System owner holds an active DoD Top Secret clearance, exceeding CUI background-investigation requirements.
- 3.9.2: DIWAI-PS-001 documents personnel security procedures.

### 4.10 Physical Protection (PE)

**Status:** All PE controls **IMPLEMENTED**.

The Mac Mini M4 Pro is housed in a locked 2U rack mount within a free-standing rack enclosure, located in a secured home-office facility with controlled access.

**Physical co-location:** The rack also contains CyberInABox (Reference System #1) components. As noted in §3.3, the two systems remain architecturally and logically independent, standalone systems with no shared policy set. PE controls — PE-2 (Physical Access Controls), PE-3 (Physical Access), PE-11 (Emergency Power) — for the [DOMAIN.ORG] system are documented independently in DIWAI-PE-MP-001.

**Note:** Physical co-location does not create a logical or network interconnection. The two systems remain fully independent (see 2.5–2.6).

### 4.11 Risk Assessment (RA)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.11.1 | Periodic risk assessment | **NOT MET** | DIWAI-RA-001 (Risk Management Policy) is approved with NIST SP 800-30 methodology. The first formal [DOMAIN.ORG]-specific risk assessment has not been conducted. **Target: overdue. SPRS deficit: -3 points.** POA&M-005. |
| 3.11.2 | Vulnerability scanning | IMPLEMENTED | Wazuh vulnerability detection module (continuous, 60-minute feed updates). OpenSCAP CUI weekly automated scan on the VM. mSCP weekly automated scan on the Mac host. |
| 3.11.3 | Remediate vulnerabilities | IMPLEMENTED | dnf-automatic applies security patches on the VM; macOS Software Update on the host. Wazuh alerts trigger a review workflow. |

### 4.12 Security Assessment (CA)

**Status:** All CA controls **IMPLEMENTED**.

- **3.12.1:** OpenSCAP CUI profile automated weekly scans on the VM (102/102). mSCP automated weekly scans on the Mac host (126/134). Results published to the compliance dashboard at securemac.[DOMAIN.ORG].
- **3.12.2:** The [DOMAIN.ORG] POA&M documents all deficiencies with remediation plans and target dates.
- **3.12.3:** Wazuh provides continuous security monitoring; Suricata provides continuous network monitoring. Weekly compliance scans supplement automated monitoring.
- **3.12.4:** This SSP constitutes the system security plan per 3.12.4.

### 4.13 System and Communications Protection (SC)

**Status:** All SC controls **IMPLEMENTED**.

- **3.13.1 (SC-7):** The pf firewall (Mac host) provides boundary protection between WAN, LAN, and MGMT interfaces. firewalld provides host-level boundary protection on the VM. Suricata provides network IDS/IPS on the VM.
- **3.13.5:** The LAN ([LAN-IP-REDACTED]/24) is segregated from the WAN by pf. The VM and NAS are not directly reachable from the WAN. nginx is the sole WAN-accessible endpoint for internal services (and even it listens only on the LAN interface and loopback).
- **3.13.6:** pf implements default-deny inbound on the WAN. firewalld implements default-deny on the VM.
- **3.13.8 (SC-8):** All data in transit is protected by TLS 1.2/1.3 or SSH. nginx enforces HSTS on both ai.[DOMAIN.ORG] and cloud.[DOMAIN.ORG] (Nextcloud). FIPS-approved cipher suites are enforced on the VM. Nextcloud↔389-DS identity traffic uses LDAPS (port 636); the Nextcloud↔Collabora editing hop stays on host loopback and never independently terminates TLS, so the nginx reverse proxy remains the sole CUI-bearing TLS boundary.
- **3.13.10:** 389-DS provides PKI and key management for identity credentials. The Apple Secure Enclave manages cryptographic keys on the Mac host.
- **3.13.11 (SC-13):** FIPS 140-2 mode is enabled on the Rocky Linux 9.7 VM (verified via `fips-mode-setup --check`). The Apple Secure Enclave (FIPS 140-2 Level 1) protects the Mac host.
- **3.13.16:** TLS encryption is enforced on all CUI transmission paths.

**Note — FIPS boundary at the NAS:** Data leaving the FIPS boundary (VM → NAS) is pre-encrypted using FIPS-validated OpenSSL (AES-256-CBC + PBKDF2/SHA-256), then transferred over SSH (AES-256-CTR). The NAS applies a second AES-256/SHA-256 encryption layer (not FIPS 140-2 validated). The FIPS artifact is the encrypted `.enc` file produced inside the boundary — the NAS layer is defense-in-depth, not a FIPS claim. The NAS is classified as supporting infrastructure within the physical security boundary, not as part of the cryptographic (FIPS) boundary.

### 4.14 System and Information Integrity (SI)

| Control | Name | Status | Implementation |
|:---|:---|:---|:---|
| 3.14.1 | Flaw remediation | IMPLEMENTED | dnf-automatic (VM); macOS Software Update (host). Wazuh vulnerability detection with CVE correlation. |
| 3.14.2 | Malware protection | **IMPLEMENTED** | **Mac host:** XProtect + MRT + Gatekeeper (Apple native, always active, auto-updated). **VM:** **YARA 4.5.2** (5,972 rules) provides malicious-code scanning — run by Wazuh active-response on FIM rules 550/554 (new/modified files) and by a **weekly full-system scan** (`yara-fullscan.timer`). Corroborated by **VirusTotal** reputation lookups and layered with **fapolicyd** application allow-listing, **SELinux** enforcing, and **Suricata** network IDS — all FIPS-native. *(ClamAV was decommissioned 06/12/2026 — non-functional under FIPS; see DIWAI-EV-SI3-002, superseding RISK-2026-004.)* **POA&M-002 CLOSED — resolved by control substitution. SPRS deficit: 0.** |
| 3.14.3 | Security alerts, advisories, directives | IMPLEMENTED | Wazuh alerts and Suricata IDS signatures auto-update. dnf-automatic handles OS security advisories. |
| 3.14.4 | Update malicious code protection | IMPLEMENTED | YARA rulesets are refreshed, and Suricata rules + Wazuh feeds update automatically. XProtect is auto-updated by Apple. |
| 3.14.5 | Periodic/real-time scans | IMPLEMENTED | Wazuh FIM operates in real time on critical paths. OpenSCAP and mSCP scan weekly. Suricata performs real-time network scanning. |
| 3.14.6 | Monitor for anomalous activity | IMPLEMENTED | Wazuh behavioral analytics + Suricata network IDS detect failed logins, USB policy violations, and anomalous traffic patterns. |
| 3.14.7 | Identify unauthorized use | IMPLEMENTED | Wazuh + Suricata correlation; auditd system-call auditing; Grafana dashboards visualize anomalies. |

---

## 5. CONTINGENCY PLANNING (CP)

### CP-9 (System Backup)

**Status:** IMPLEMENTED

**Mac Host (securemac.[DOMAIN.ORG]):**
- Time Machine backup to dedicated encrypted SSD (UUID: E2EBAB82-18DA-4F2D-8257-C05AE6CE42F1)
- LaunchAgent (`org.diwai.mount-tm-drive`) ensures the SSD auto-mounts at login
- RPO: continuous (Time Machine hourly snapshots)

**VM (services.[DOMAIN.ORG]):**
- Wazuh alert archives: daily encrypted push to the NAS (nas.[DOMAIN.ORG])
- Archives encrypted via FIPS-validated OpenSSL before transfer
- VM configuration: documented and reproducible via UTM snapshot + kickstart

**NAS (nas.[DOMAIN.ORG]):**
- Primary long-term archive target for encrypted log data (DataStore share)
- Synology folder-level encryption (AES-256/SHA-256) as a second layer

### CP-10 (System Recovery)

**Status:** IMPLEMENTED

- Mac host: Time Machine full-system restore + macOS bootable installer
- VM: UTM snapshot restore, or rebuild from the Rocky Linux 9.7 FIPS kickstart
- RTO: < 4 hours; RPO: < 24 hours

---

## 6. SECURITY POLICIES AND PROCEDURES

All policies below apply to the [DOMAIN.ORG] SecureMac Reference System as part of the single-operator organization [SYSTEM-OWNER] LLC. The same policy set covers both CyberInABox and [DOMAIN.ORG] as **organizational common controls** (not system-specific) — see 2.6 and 4.10.

| Policy | Document ID | Effective Date |
|:---|:---|:---|
| Incident Response Policy and Procedures | DIWAI-IRP-001 | 04/10/2026 |
| Risk Management Policy | DIWAI-RA-001 | 04/10/2026 |
| Personnel Security Policy | DIWAI-PS-001 | 04/10/2026 |
| Physical and Media Protection Policy | DIWAI-PE-MP-001 | 04/10/2026 |
| System and Information Integrity Policy | DIWAI-SI-001 | 04/10/2026 |
| Acceptable Use Policy | DIWAI-AUP-001 | 04/10/2026 |
| Audit and Accountability Policy | DIWAI-AAP-001 | 04/10/2026 |
| Configuration Management Policy | DIWAI-CMP-001 | 04/10/2026 |
| Security Awareness and Training Policy | DIWAI-ATP-001 | 04/10/2026 |
| **Identification and Authentication Policy** | **DIWAI-IAP-001 — v1.1** | **04/10/2026 (orig. v1.0); updated 06/11/2026 — unified TOTP MFA strategy** |
| System and Communications Protection Policy | DIWAI-SCP-001 | 04/10/2026 |

---

## 10. PLAN OF ACTION AND MILESTONES (POA&M)

The complete [DOMAIN.ORG] POA&M is maintained as a standalone document: **`[DOMAIN.ORG]_Unified_POAM_v1.2.md`** (2026-06-12, in `Compliance/POAM/`; see Appendix D, "Companion Documents"). The summary table below reflects the POA&M state as of this revision and is kept in sync with the standalone document.

### POA&M Summary (as of June 6, 2026)

| POA&M ID | Weakness | Control | SPRS | Target | Status |
|:---|:---|:---|:---|:---|:---|
| POA&M-001 | YubiKey PIV re-pairing (Mac host) | 3.5.3, IA-5 | (part of -5) | — | **CLOSED 06/06/2026 — superseded by MFA strategy change** |
| POA&M-002 | ClamAV daemon / YARA deployment on VM | 3.14.2 | +1 recovered | — | **CLOSED 06/12/2026 — resolved (SI-3 substitution to YARA stack)** |
| POA&M-003 | mSCP 8 failing rules remediation (Mac) | 3.4.1 | — | Q3 2026 | PLANNED |
| POA&M-004 | TOTP MFA deployment on VM (services.[DOMAIN.ORG]) | 3.5.3, 3.7.5 | -5 / -3 (shared) | Q3 2026 | PLANNED |
| POA&M-005 | First annual risk assessment | 3.11.1 | -3 | **OVERDUE** | OVERDUE |
| POA&M-006 | IR tabletop exercise | 3.6.3 | -1 | 06/30/2026 | ON TRACK |
| **POA&M-007** | **TOTP Authenticator app enrollment — Mac host (dshannon account)** | **3.5.3, 3.7.5** | **(shared with -004)** | **Q3 2026** | **PLANNED — opened 06/06/2026** |
| **POA&M-008** | **[DOMAIN.ORG]-specific security awareness training (delivery + records)** | **3.2.1, 3.2.2, 3.2.3** | **TBD — see note** | **Q3 2026** | **NEW — opened 06/11/2026** |
| **POA&M-009** | **Mac host Wazuh agent offline (host FIM/telemetry)** | **3.3.1/3.3.2 (AU-6/SI-4)** | — | — | **CLOSED 06/12/2026 — resolved** |
| **POA&M-010** | **VM time-sync drift (audit-timestamp integrity)** | **3.3.7 (AU-8)** | — | — | **CLOSED 06/12/2026 — resolved** |

**Current SPRS:** 98/110 (89.1%) — 3.14.2 is now **fully MET** (POA&M-002 closed; no longer reliant on risk acceptance)\
**Target SPRS upon completion:** 110/110 (100%)\
**Note:** POA&M-004 and POA&M-007 together form a single unified MFA remediation effort (TOTP via Authenticator app, RFC 6238, deployed to both the VM and the Mac host) — completing both closes the entire 3.5.3 / 3.7.5 gap (+8 points) in one coordinated rollout rather than two independent ones.\
**Note on POA&M-008 (06/11/2026):** This item was identified during the [DOMAIN.ORG]/CyberInABox independence and Document-ID correction pass — 3.2.1/3.2.2/3.2.3 were downgraded from IMPLEMENTED to PARTIAL after removing a citation to a CyberInABox-specific training record. Its SPRS point weight has **not been confirmed** against the official DoD NIST SP 800-171 Assessment Methodology scoring tables, so the **98/110 figure above does not yet reflect this finding** — recommend confirming the weight and updating the score before the next self-assessment submission.

---

## 11. IMPLEMENTATION METRICS

### SPRS Score Breakdown

| Req | Control | Weight | Status |
|:---|:---|:---|:---|
| 3.5.3 | Multi-Factor Authentication | -5 | NOT MET |
| 3.7.5 | MFA for Remote Maintenance | -3 | NOT MET |
| 3.11.1 | Periodic Risk Assessment | -3 | NOT MET (OVERDUE) |
| 3.6.3 | IR Tabletop Exercise | -1 | NOT MET |
| 3.14.2 | Malware Protection (VM) | 0 | **MET** — SI-3 substitution (YARA stack); POA&M-002 closed 06/12/2026 |
| 3.2.1 | Security Awareness (Risk) | **TBD** | PARTIAL — POA&M-008 |
| 3.2.2 | Security Awareness (Threats) | **TBD** | PARTIAL — POA&M-008 |
| 3.2.3 | Security Training (Role-Based) | **TBD** | PARTIAL — POA&M-008 |
| **All others** | 102 requirements | **0** | **MET** |
| **TOTAL DEFICIT** | | **-12 (+ TBD)** | |
| **SPRS** | | **98/110 (+ TBD)** | **89.1% (or lower)** |

**3.14.2 is now fully MET** via the SI-3 control substitution (YARA + VirusTotal + fapolicyd + SELinux + Suricata; POA&M-002 closed 06/12/2026) — the previously-pending ClamAV risk acceptance is no longer required, so the -1 is genuinely recovered rather than risk-accepted.

**Caveat (added 06/11/2026; updated 06/12/2026):** The 3.2.1/3.2.2/3.2.3 rows above (POA&M-008) have point weights that are **not yet confirmed** against the official DoD NIST SP 800-171 Assessment Methodology scoring tables. The current **-12 deficit / 98/110** figures **do not yet subtract the 3.2.1/3.2.2/3.2.3 weight**. Treat 98/110 as the last-confirmed score, not the current one, until POA&M-008's SPRS impact is confirmed and these figures are recalculated. *(Note: as of the 06/12/2026 revision, 3.14.2 is fully MET — POA&M-002 closed — so the deficit moved from -13 to -12 and the score no longer depends on the former ClamAV risk acceptance.)*

*The June 6 MFA strategy change does not alter this breakdown — both 3.5.3 and 3.7.5 remain NOT MET until POA&M-004 and POA&M-007 are actually completed. What has changed is that the path to closing them is now a single, unified, lower-risk technical approach instead of two separate ones (one of which — YubiKey PIV — had already failed twice).*

### Control Family Status

| Family | Total | Implemented | Not Met | N/A |
|:---|:---|:---|:---|:---|
| AC — Access Control | 22 | 20 | 1 (3.5.3) | 2 (wireless) |
| AT — Awareness & Training | 3 | 0 | 0 | 0 (3 PARTIAL — POA&M-008) |
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
| SI — System & Info Integrity | 7 | 7 | 0 | 0 |

---

## 12. CONCLUSION

The [DOMAIN.ORG] SecureMac Reference System demonstrates that NIST 800-171 / CMMC Level 2 compliance is achievable on Apple Silicon hardware using macOS and ARM64 Linux virtualization. The current self-assessed SPRS score of 98/110 (89.1%) reflects a system with strong foundational security — full FIPS mode on the VM, 100% OpenSCAP CUI compliance, a full Wazuh SIEM stack, Suricata IDS, a pf firewall, and comprehensive audit logging — with a small number of tractable, well-understood gaps remaining. **(Caveat, 06/11/2026: this 98/110 figure is the last-confirmed score and does not yet reflect the 3.2.1/3.2.2/3.2.3 PARTIAL finding opened as POA&M-008 — see §11.)**

The June 6, 2026 decision to abandon the YubiKey PIV approach (after two lockout incidents) and standardize on **TOTP via Authenticator app** across both the Mac host and the VM **simplifies** — rather than complicates — the path to 110/110: it consolidates what had been two separate, partially-failed MFA efforts into one coordinated rollout that recovers all 8 MFA-related points (3.5.3 -5, 3.7.5 -3) at once. Combined with the overdue annual risk assessment (+3) and the IR tabletop exercise (+1), these three actions account for all 12 of the remaining known SPRS deficit points — the 13th (3.14.2's -1) was recovered 06/12/2026 by closing POA&M-002 via the YARA control substitution. POA&M-008 (3.2.1/3.2.2/3.2.3, weight TBD) is additional and not yet included in that count.

### Priority Action Items

| Priority | Item | SPRS Recovery | Target |
|:---|:---|:---|:---|
| 1 | Unified TOTP MFA rollout — VM (POA&M-004) + Mac host (POA&M-007) | +8 pts (3.5.3 + 3.7.5) | Q3 2026 |
| 2 | Annual risk assessment (POA&M-005) | +3 pts | OVERDUE — immediate |
| 3 | IR tabletop exercise (POA&M-006) | +1 pt | 06/30/2026 |
| ✓ | SI-3 malware protection — YARA stack (POA&M-002) | **+1 recovered** | **DONE 06/12/2026** |
| 5 | [DOMAIN.ORG]-specific security awareness training (POA&M-008) | TBD pts (3.2.1/3.2.2/3.2.3) | Q3 2026 |
| — | mSCP 8 failing rules remediation — Mac host (POA&M-003) | (no direct SPRS weight) | Q3 2026 |

---

## AUTHORIZATION

**Full Authorization Granted:** June 5, 2026\
**Authorization Period:** 3 years (through June 4, 2029)\
**Authorizing Official:** /s/ [SYSTEM-OWNER], System Owner/ISSO\
**[SYSTEM-OWNER] LLC dba [ORGANIZATION]**\
**Date:** _____ (pending re-signature for v2.14)

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
- **MLX** — Machine Learning eXchange (Apple Silicon native inference framework)
- **MP** — Media Protection; **mSCP** — macOS Security Compliance Project
- **NIST** — National Institute of Standards and Technology; **PE** — Physical Protection
- **POA&M** — Plan of Action and Milestones; **PS** — Personnel Security
- **RA** — Risk Assessment; **SC** — System and Communications Protection
- **SIEM** — Security Information and Event Management; **SI** — System and Information Integrity
- **SIP** — System Integrity Protection (macOS); **SSH** — Secure Shell; **SSP** — System Security Plan
- **SPRS** — Supplier Performance Risk System; **TLS** — Transport Layer Security
- **TOTP** — Time-based One-Time Password (RFC 6238); **UTM** — Universal Turing Machine (virtualization)

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
12. RFC 6238 — TOTP: Time-Based One-Time Password Algorithm

### Appendix C: Supporting Documentation

**Compliance Scanning:**
- VM OpenSCAP scan: `/usr/local/bin/oscap-scan.sh` (weekly, Sunday 02:00)
- Mac mSCP scan: `/usr/local/bin/run-mSCP-scan.sh` (weekly, Sunday 03:00)
- Compliance dashboard: https://securemac.[DOMAIN.ORG] (Apache, LDAP-authenticated)

**Infrastructure:**
- nginx config: `/opt/homebrew/etc/nginx/servers/ai.[DOMAIN.ORG].conf`
- USB Guard (Mac): `/usr/local/sbin/usb-guard`, `/usr/local/sbin/usb-guard-monitor`, `org.diwai.usb-guard` LaunchDaemon
- Time Machine auto-mount: `/usr/local/sbin/mount-tm-drive.sh`, `org.diwai.mount-tm-drive` LaunchAgent
- OpenVPN: `/etc/openvpn/server/diwai.conf`
- AI stack: `org.diwai.magistral` (MLX server, port 8081), `org.diwai.open-webui` (port 3000), `org.diwai.nginx`
- Malicious-code scanning (VM): YARA 4.5.2 (`/usr/local/yara/rules/index.yar`); Wazuh active-response `yara.sh` (FIM 550/554); weekly `yara-fullscan.timer` (`/usr/local/sbin/yara-fullscan.sh`)

**Architecture & Assessment (`Compliance/`):**
- Network/stack schematic: `Architecture/RS2_Network_Schematic.svg` (+ editable `.drawio`)
- CUI data-flow diagram: `Architecture/RS2_CUI_DataFlow.svg` (+ `.drawio`)
- Stack & tool reference: `Architecture/RS2_Stack_Reference.md`
- Independent gap assessment: `Assessment/RS2_Gap_Assessment_2026-06-12.md`
- SI-3 control substitution (malware protection): `Evidence/SI-3_Control_Substitution_ClamAV_Decommission_2026-06-12.md` (DIWAI-EV-SI3-002)

**Policies:** DIWAI-IRP-001, DIWAI-RA-001, DIWAI-PS-001, DIWAI-PE-MP-001, DIWAI-SI-001, DIWAI-AUP-001, DIWAI-AAP-001, DIWAI-CMP-001, DIWAI-ATP-001, DIWAI-IAP-001 (v1.1), DIWAI-SCP-001

### Appendix D: Document Maintenance

This SSP shall be reviewed and updated quarterly or upon significant system changes.

**Next Scheduled Review:** September 30, 2026

**Companion Documents (resolved 06/11/2026):**
- **`[DOMAIN.ORG]_Unified_POAM_v1.2.md`** — the standalone POA&M of record (POA&M-001 through POA&M-010), 2026-06-12, in `Compliance/POAM/` (supersedes v1.1). Section 10's summary table is kept in sync; the standalone POA&M provides full per-item detail, milestones, and a status dashboard.
- **DIWAI-IAP-001 v1.1** — Identification and Authentication Policy, updated 06/11/2026 to reflect the unified TOTP MFA strategy (§4.5). This also corrects the Rev. 2.12 (06/06/2026) revision-history entry's reference to "TCC-IAP-001," which is a different, CyberInABox/CPN-scoped document (see Document ID correction in revision history above).

**Review Focus Areas:**
- POA&M-004 / POA&M-007 unified TOTP MFA deployment status
- POA&M-005 risk assessment completion (OVERDUE)
- POA&M-006 IR tabletop exercise (June 30 deadline)
- ~~POA&M-002 ClamAV daemon / YARA remediation~~ — **CLOSED 06/12/2026** (SI-3 substitution to YARA stack; DIWAI-EV-SI3-002)
- POA&M-003 mSCP 8 failing rules remediation progress
- **Document-ID audit (completed 06/11/2026):** All ten remaining `TCC-*-001` policy citations in §6 and Appendix C, plus ~9 inline citations throughout §3/§4, have been corrected to their `DIWAI-*-001` equivalents (v1.0, 04/10/2026, in `~/Documents/SecureMac Project Docs/Policies/`). This was driven by a definitive determination that **[DOMAIN.ORG] is an independent, standalone system and does not share policies, controls, or evidence with the CyberInABox/CPN reference system** — see the "2.12 (corrected)" revision-history entry above for the full list of changes. The two prior "shared/common controls, inherited by both SSPs" notes (former §3.3, §4.10) have been rewritten to describe [DOMAIN.ORG]'s physical/media protection controls as documented solely in DIWAI-PE-MP-001, independent of any physical co-location with CyberInABox.
- **POA&M-008 / SPRS weight confirmation (opened 06/11/2026):** The Document-ID audit above surfaced a substantive gap — §4.2 (3.2.1/3.2.2/3.2.3) had relied solely on a CyberInABox-specific training record (now removed). These three controls are now PARTIAL pending [DOMAIN.ORG]-specific training delivery and records (POA&M-008, target Q3 2026). Their SPRS point weight is **TBD** — confirm against the official DoD NIST SP 800-171 Assessment Methodology and update §11/§12/the POA&M dashboard accordingly before the next self-assessment submission.
- Open Web UI and MLX model currency
- macOS 26.x security updates
- Wazuh and Suricata signature updates
- Outstanding companion documents (above) — drafting and approval

---

**— END OF SYSTEM SECURITY PLAN —**

**Document Classification: CONTROLLED UNCLASSIFIED INFORMATION (CUI)**\
**System: [DOMAIN.ORG] SecureMac Reference System**\
**Version: 2.14 | Date: June 29, 2026**
