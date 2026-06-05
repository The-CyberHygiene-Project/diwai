# SOFTWARE BILL OF MATERIALS (SBOM)

**System:** [DOMAIN.ORG] SecureMac Reference System\
**Organization:** [SYSTEM-OWNER] LLC dba [ORGANIZATION]\
**Classification:** Controlled Unclassified Information (CUI)\
**Version:** 1.0\
**Date Generated:** June 5, 2026\
**Scope:** 2 systems (1 Mac Mini host, 1 ARM64 Linux VM)\
**Architecture:** ARM64 (Apple Silicon) throughout

---

## Version Note

This is the **first [DOMAIN.ORG]-specific SBOM**. Prior SBOM documents in the cyberhygiene-docs repository (Software_Bill_of_Materials_v2.0 through v2.6) tracked the **CyberInABox ([DOMAIN.ORG]) production network** (X86 Rocky Linux systems). Those documents are archived in the CyberInABox documentation set. This document covers only the [DOMAIN.ORG] SecureMac Reference System.

---

## Executive Summary

### System Inventory

| Hostname | IP | Platform | Architecture | Packages | Role |
|----------|----|-----------|--------------|----|------|
| **securemac.[DOMAIN.ORG]** | [LAN-IP-REDACTED] | macOS 26.5 (Tahoe) | ARM64 (Apple M4 Pro) | ~30 Homebrew + system | Host, firewall, nginx, AI inference |
| **services.[DOMAIN.ORG]** | [LAN-IP-REDACTED] | Rocky Linux 9.7 (Blue Onyx) | aarch64 (UTM VM) | 868 RPM | SIEM, identity, email, monitoring, VPN |

**Total Systems:** 2\
**Architecture:** ARM64 throughout — both Mac host and UTM VM run on Apple M4 Pro silicon\
**Note:** The Synology NAS (nas.[DOMAIN.ORG], [LAN-IP-REDACTED]) is supporting infrastructure; its software inventory is maintained separately by Synology DSM and is out of scope for this SBOM.

---

## VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-06-05 | [SYSTEM-OWNER] | Initial [DOMAIN.ORG] SBOM. Covers Mac Mini M4 Pro host (macOS 26.5 Tahoe) and services.[DOMAIN.ORG] UTM VM (Rocky Linux 9.7 aarch64). 868 RPM packages on VM; ~30 Homebrew packages on Mac host. First [DOMAIN.ORG]-specific document — not a continuation of CyberInABox SBOM series. |

---

## PURPOSE

This Software Bill of Materials provides a comprehensive inventory of all software components installed across the [DOMAIN.ORG] SecureMac Reference System. This SBOM supports:

- **Supply chain security assessment** per NIST 800-171 SR-2
- **Vulnerability management** and patch tracking
- **Software licensing compliance** (Rocky Linux, macOS, open source)
- **System security auditing** and configuration management (CM-8)
- **Incident response and forensics** capabilities
- **CMMC Level 2 compliance** (Component Inventory requirements)

---

## SYSTEM 1: securemac.[DOMAIN.ORG] (Mac Mini M4 Pro Host)

**Platform:** macOS 26.5 (Tahoe) — Build 25F71\
**Architecture:** ARM64 (Apple Silicon — M4 Pro)\
**Role:** Physical host, WAN gateway/firewall, nginx reverse proxy, AI/ML inference server, management workstation\
**FIPS:** Apple Secure Enclave (hardware-based FIPS 140-2 Level 1 cryptography)\
**Compliance Scan:** mSCP baseline diwai_phase1.yaml — 126/134 (94%) as of 2026-05-30

### macOS System Software

#### Core OS

- **macOS 26.5 (Tahoe)** Build 25F71 — Apple's Unix-based operating system (Darwin/XNU kernel, ARM64)
- **XNU Kernel** — Darwin kernel, ARM64 optimized
- **APFS** — Apple File System with native encryption support

#### Apple Security Features (Always Active)

- **FileVault** — Full-disk encryption via Apple Secure Enclave (AES-256, hardware key storage)
- **System Integrity Protection (SIP)** — Kernel-level protection against unauthorized system modifications
- **Gatekeeper** — Application signature verification and notarization enforcement
- **XProtect** — Built-in malware signature detection (auto-updated by Apple)
- **MRT (Malware Removal Tool)** — Automated malware remediation (Apple native)
- **pf firewall** — BSD packet filter (stateful, NAT, default-deny inbound on WAN)
- **Apple Secure Enclave** — Dedicated security processor for key management (FIPS 140-2 Level 1)

#### Network and Security

- **pf** — macOS native packet filter firewall (WAN boundary protection)
- **nginx** 1.31.0 (Homebrew, ARM64) — HTTPS reverse proxy for ai.[DOMAIN.ORG]
- **pcre2** 10.47_1 (Homebrew) — nginx dependency (regex support)
- **openssl@3** 3.6.2 (Homebrew) — TLS/SSL library
- **OpenVPN** client capability (via macOS system libraries)

#### AI/ML Platform

- **Open Web UI** 0.9.5 (Python venv: /opt/local/open-webui-venv) — AI chat interface
  - Bound to 127.0.0.1:3000 (localhost only)
  - Access via nginx proxy at https://ai.[DOMAIN.ORG]
  - Signup disabled; single admin account
- **Magistral-Small-2509-MLX-4bit** — AI inference model (MLX native format)
  - Location: /opt/local/models/Magistral-Small-2509-MLX-4bit
  - Inference: MLX (Metal Performance Shaders — Apple Silicon native)
  - No Ollama dependency for this model
- **Ollama** 0.21.2_1 (Homebrew) — LLM runtime (installed; Magistral uses MLX directly)
- **Python@3.11** 3.11.15 (Homebrew) — Open Web UI runtime
- **Python@3.14** 3.14.4 (Homebrew) — General scripting

#### System Management

- **USB Guard** (custom — /usr/local/sbin/usb-guard) — USB device control daemon
  - LaunchDaemon: /Library/LaunchDaemons/org.diwai.usb-guard.plist
  - Allowlisted device: Time Machine SSD (UUID: [TM-UUID-REDACTED])
- **org.diwai.mount-tm-drive** — Time Machine auto-mount LaunchAgent
  - Script: /usr/local/sbin/mount-tm-drive.sh
- **org.diwai.mscp-scan** — mSCP weekly compliance scan LaunchDaemon
  - Script: /usr/local/bin/run-mSCP-scan.sh (weekly Sunday 03:00)
- **mSCP (macOS Security Compliance Project)** — Compliance scanning framework
  - Repo: ~/macos_security/ (NIST clone)
  - Baseline: ~/macos_security/baselines/diwai_phase1.yaml
- **git** (Xcode CLT / Homebrew) — Version control

#### YubiKey Management Tools

- **ykman** 5.9.0 (Homebrew) — YubiKey manager CLI
- **yubico-piv-tool** (Homebrew) — PIV certificate management
- **YubiKey Nano 5C FIPS** (hardware) — Firmware 5.4.3; PIV certs present but unpaired (see POA&M-001)

---

## SYSTEM 2: services.[DOMAIN.ORG] (Rocky Linux 9.7 UTM VM)

**Platform:** Rocky Linux 9.7 (Blue Onyx)\
**Kernel:** 5.14.0-611.45.1.el9_7.aarch64\
**Architecture:** aarch64 (ARM64 — UTM virtualized on Apple M4 Pro)\
**FIPS Mode:** Enabled (verified: fips-mode-setup --check)\
**Total Packages:** 868 RPM\
**OpenSCAP CUI Compliance:** 102/102 — 100% (weekly automated scan)\
**Role:** SIEM, identity directory, web services, email, network services, monitoring

### Critical Security Software

#### Identity & Access Management

| Package | Version | Purpose |
|---------|---------|---------|
| **389-ds-base** | 2.7.0-12.el9_7 | 389 Directory Server (LDAP) — dc=diwai,dc=org identity directory |
| **389-ds-base-libs** | 2.7.0-12.el9_7 | 389-DS library dependencies |
| **openssl** | 3.5.1-7.el9_7 | FIPS-validated cryptography (FIPS provider active) |
| **openssl-fips-provider** | 3.5.1-7.el9_7 | FIPS 140-2 validated provider module |
| **openssl-libs** | 3.5.1-7.el9_7 | OpenSSL shared libraries |

#### Security Monitoring (SIEM Stack)

| Package | Version | Purpose |
|---------|---------|---------|
| **wazuh-manager** | 4.14.5-1 | Wazuh SIEM Manager — security event management, FIM, vulnerability detection |
| **wazuh-dashboard** | 4.14.5-1 | Wazuh Dashboard UI — HTTPS web interface for SIEM |
| **wazuh-indexer** | 4.14.5-1 | OpenSearch-based search and analytics backend for Wazuh |
| **suricata** | 7.0.13-1.el9 | Network Intrusion Detection/Prevention System |
| **filebeat** | — | Log shipper (Wazuh alert forwarding) |
| **audit** | 3.1.5-7.el9 | Linux kernel audit framework (system call auditing) |
| **audit-libs** | 3.1.5-7.el9 | Audit library dependencies |
| **fapolicyd** | 1.3.3-106.el9_6.1 | File Access Policy Daemon (application whitelisting) |
| **fapolicyd-selinux** | 1.3.3-106.el9_6.1 | SELinux policy for fapolicyd |
| **rsyslog** | — | System log collection and forwarding |

#### Malware Protection

| Package | Version | Purpose | Status |
|---------|---------|---------|--------|
| **clamav** | 1.4.3-3.el9 | Antivirus engine | Installed; daemon **inactive** (see POA&M-002) |
| **clamav-freshclam** | 1.4.3-3.el9 | ClamAV database updater | **Running** — DB kept current |
| **clamav-lib** | 1.4.3-3.el9 | ClamAV library | Installed |
| **YARA** | — | Pattern-based malware detection | **Not deployed** (see POA&M-002) |

*Compensating controls: Wazuh FIM with VirusTotal integration, Suricata IDS, fapolicyd*

#### Monitoring & Metrics

| Package | Version | Purpose |
|---------|---------|---------|
| **grafana** | 13.0.1^security_01-1 | Metrics visualization dashboards |
| **grafana-pcp** | 5.1.1-14.el9_7 | Performance Co-Pilot plugin for Grafana |
| **prometheus** | 3.11.2-1.el9 | Time-series metrics collection (targets: VM + localhost) |
| **prometheus-node-exporter** | — | Host metrics exporter |

#### Web Services

| Package | Version | Purpose |
|---------|---------|---------|
| **httpd** | 2.4.62-7.el9_7.3 | Apache HTTP Server (securemac.[DOMAIN.ORG] dashboard) |
| **httpd-core** | 2.4.62-7.el9_7.3 | Apache core module |
| **php-fpm** | — | PHP FastCGI Process Manager |
| **mariadb-server** | 10.5.29-3.el9_7 | MariaDB database server (web services backend) |
| **mariadb** | 10.5.29-3.el9_7 | MariaDB client tools |

#### Email Services

| Package | Version | Purpose |
|---------|---------|---------|
| **postfix** | 3.5.25-1.el9 | SMTP mail server (TLS enforced) |
| **dovecot** | 2.3.16-15.el9_7.1 | IMAP/POP3 mail server (encrypted) |
| **dovecot-pigeonhole** | 2.3.16-15.el9_7.1 | Sieve mail filtering |

#### Network Services

| Package | Version | Purpose |
|---------|---------|---------|
| **openvpn** | 2.5.11-1.el9 | OpenVPN server (vpn.[DOMAIN.ORG] remote access) |
| **unbound** | — | Recursive DNS resolver |
| **chrony** | 4.6.1-2.el9 | NTP client/server (time synchronization) |
| **firewalld** | 1.3.4-18.el9_7 | Host firewall (dynamic, nftables backend) |
| **NetworkManager** | — | Network configuration management |

#### System Hardening

| Package | Version | Purpose |
|---------|---------|---------|
| **usbguard** | — | USB device access control |
| **dnf-automatic** | 4.14.0-31.el9.rocky.0.1 | Automated security package updates |
| **dnf** | 4.14.0-31.el9.rocky.0.1 | Package manager |

#### Compliance Scanning

| Tool | Version | Purpose |
|------|---------|---------|
| **OpenSCAP** (oscap) | — | CUI profile compliance scanning (weekly Sunday 02:00) |
| **ssg-rl9-ds.xml** | SCAP Security Guide | Rocky Linux 9 CUI/NIST 800-171 content |
| **oscap-scan.sh** | custom | /usr/local/bin/oscap-scan.sh — automated weekly scan |
| **oscap-update-compliance.py** | custom | Updates compliance.html dashboard row |

---

## COMPLIANCE NOTES

### FIPS Cryptography

| System | FIPS Implementation | Status |
|--------|---------------------|--------|
| securemac.[DOMAIN.ORG] | Apple Secure Enclave (FIPS 140-2 Level 1) + FileVault AES-256 | Active |
| services.[DOMAIN.ORG] | OpenSSL 3.5.1 FIPS provider (fips-mode-setup enabled) | Active (verified) |

### Software Licensing

- **Rocky Linux:** Community-supported RHEL binary compatible — open source (GPL/LGPL)
- **macOS:** Apple Commercial License
- **Wazuh:** GPL v2
- **Grafana:** AGPLv3
- **Suricata:** GPL v2
- **nginx:** BSD 2-Clause
- **OpenVPN:** GPL v2
- **389 Directory Server:** GPL v2
- **Open Web UI:** MIT License
- **Magistral-Small-2509-MLX-4bit:** Mistral AI License

### Vulnerability Management

- Rocky Linux security advisories tracked via dnf-automatic (automatic security updates)
- Wazuh vulnerability detection module monitors CVEs against installed package versions
- OpenSCAP weekly scan validates configuration against CUI profile
- macOS Software Update handles Mac host OS and security patches

---

**Document Classification: CONTROLLED UNCLASSIFIED INFORMATION (CUI)**\
**System: [DOMAIN.ORG] SecureMac Reference System**\
**Version: 1.0 | Date: June 5, 2026**
