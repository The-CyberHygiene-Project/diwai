> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# SOFTWARE BILL OF MATERIALS (SBOM) — [DOMAIN.ORG] SecureMac Reference System

**System:** [DOMAIN.ORG] SecureMac Reference System  
**Organization:** [DOMAIN.ORG] (Do It With AI)  
**Classification:** Controlled Unclassified Information (CUI)  
**Version:** 3.3  
**Date Generated:** 2026-08-03  
**Scope:** 2 systems (1 combined firewall/DC/mail/SIEM/AI/Nextcloud server-host + 1 Rocky Linux service VM)  
**Architectures:** ARM64 (Apple Silicon — both systems)  

---

## EXECUTIVE SUMMARY

### System Inventory

| Hostname | IP | Platform | Architecture | Packages | Role |
|----------|----|----------|--------------|----------|------|
| **services.[DOMAIN.ORG]** | [LAN-IP-REDACTED] | Rocky Linux 9.7 (Blue Onyx) | aarch64 | ~817 RPM | Domain Controller, Mail, VPN, IDS, SIEM, Monitoring |
| **Mac mini (host)** | [LAN-IP-REDACTED] (LAN) / [WAN-IP-REDACTED] (WAN) | macOS Tahoe 26.4.1 | ARM64 (M4 Pro) | macOS native + Homebrew | Firewall/Router, AI Inference Host, Nextcloud (Private Cloud) |

**Total Systems:** 2  
**Architecture:** ARM64 (Apple Silicon) throughout — no x86_64  
**Compliance Target:** NIST SP 800-171 R2 / FIPS 140-2  

### Platform Distribution

- **Rocky Linux 9.7 (aarch64):** 1 system — FIPS 140-2 mode enabled, SELinux enforcing
- **macOS Tahoe 26.4 (ARM64):** 1 system — M4 Pro hardware encryption, pf firewall

---

## PURPOSE

This Software Bill of Materials (SBOM) provides a comprehensive inventory of all software components installed on the SecureMac reference system. This SBOM supports:

- **Supply chain security assessment** per NIST 800-171 SR-2
- **Vulnerability management** and patch tracking
- **Software licensing compliance** (Rocky Linux, macOS, open source)
- **System security auditing** and configuration management (CM-8)
- **Incident response and forensics** capabilities
- **CMMC Level 2 compliance** (Component Inventory requirements)

---

## DOCUMENT CLASSIFICATION

**Classification:** CUI (Controlled Unclassified Information)  
**Distribution:** Owner/ISSO, Authorized Auditors, C3PAO Assessors  
**Retention:** Maintain current version + 3 years historical  
**Review Schedule:** Quarterly (with each SSP review)  

---

## VERSION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-04-10 | [SYSTEM-OWNER] | Initial SBOM for SecureMac Reference System. All core services operational: Apache, Postfix, Dovecot, 389-ds, OpenVPN, Suricata, Wazuh, Grafana, Prometheus, ClamAV, USBGuard. OpenSCAP 102/102 pass. Let's Encrypt auto-renewal configured. |
| 2.0 | 2026-04-23 | [SYSTEM-OWNER] | Verified all package versions against installed state. Updates: kernel 611.41→611.45, php-fpm 8.0→8.2 (Remi), roundcubemail 1.5.14→1.5.15, grafana 12.4.2→13.0.1, python3 minor rev, node-exporter 1.11.1 (proper package name), OpenSCAP/SSG versions added. macOS updated to 26.4.1 (25E253). Added Homebrew YubiKey tools (ykman 5.9.0, yubico-piv-tool 2.7.3, libfido2 1.16.0, openssh 10.3p1) and YubiKey PIV hardware to macOS section. Auth section updated to reflect PIV smartcard. |
| 3.0 | 2026-06-11 | [SYSTEM-OWNER] | Major refresh. **Added:** Nextcloud 32.0.11.1 (private cloud / document management, `/opt/local/nextcloud`, instance-wide TOTP 2FA) as a new Mac mini subsystem; Local AI Inference moved from "Planned" to **operational** — Magistral-Small-2509-MLX-4bit via `mlx_lm.server` (port 8081) + Open WebUI (port 3000) behind `ai.[DOMAIN.ORG]`, plus Ollama (codestral, all-minilm). **Removed/Superseded:** YubiKey 5C Nano FIPS PIV retired as the macOS local-auth MFA mechanism (unpaired 2026-06-06, POA&M-001 closed-superseded) — Homebrew YubiKey/FIDO2 tooling remains installed but unused; unified TOTP MFA strategy (POA&M-004/007) now governs VM SSH and macOS. **Updated:** VM OpenSCAP re-verified 102/102 (2026-06-08); first-time inclusion of macOS mSCP compliance baseline (`diwai_phase1`, 129/134, 2026-06-11). **Corrected:** system title/header de-coupled from "CyberInABox Reference System #2" framing — [DOMAIN.ORG] is documented as an independent, stand-alone system per the 2026-06-11 SSP v2.12 independence determination. Document Control updated to reflect Nextcloud as the canonical CUI evidence repository. |
| 3.1 | 2026-06-29 | [SYSTEM-OWNER] | **SI-3 reconciliation with SSP v2.13+.** This SBOM (v3.0, 2026-06-11) predated the 2026-06-12 SI-3 control substitution by one day and still listed ClamAV as the active malware-protection control. **Corrected:** ClamAV 1.4.3 (`clamav`/`clamd`) marked **decommissioned 2026-06-12** — non-functional under FIPS (could neither download nor load a signature database; OpenSSL verification failure); see SSP §3.14.2 / DIWAI-EV-SI3-002 (supersedes RISK-2026-004), POA&M-002 closed. **Added:** **YARA 4.5.2** (5,972 rules) as the operational SI-3 malware scanner — Wazuh active-response on FIM 550/554 + weekly full-system scan (`yara-fullscan.timer`); SI-3 control now YARA + VirusTotal + fapolicyd + SELinux + Suricata (all FIPS-native). YubiKey entries unchanged (already correctly marked retired, consistent with SSP). |
| 3.3 | 2026-08-03 | [SYSTEM-OWNER] | **Least-functionality reconciliation — Grafana and ClamAV.** **Grafana** 13.1.1 marked **decommissioned/removed 2026-08-02** (`grafana`, `grafana-selinux`, `grafana-pcp`; 1.0 GB freed): not updatable — `rpm.grafana.com` failed GPG verification on `repomd.xml`, leaving an unpatchable component that also broke `dnf check-update` system-wide — against limited operational use. Prometheus + node-exporter **retained and verified running**, so metrics collection is unaffected; only visualization was retired. Inventory version corrected 13.0.1→13.1.1 (installed state had drifted from this SBOM before removal). License table and Security-Control summary updated. Authority `DIWAI-CR-2026-08-04`. **ClamAV** rows updated to record **package removal 2026-08-01** (`DIWAI-CR-2026-08-01` C14, 138 MB) — the June 2026 entry recorded the *decommissioning* but the software stayed installed and auto-upgrading until August (**F-2026-08-06**, now **closed**); FIPS 140 incompatibility stated explicitly as the root cause. No SPRS impact from either change: SI-3 was already rebased on the FIPS-native YARA stack, and no control named Grafana as its sole mechanism. |
| 3.2 | 2026-06-29 | [SYSTEM-OWNER] | **YubiKey tooling reconciliation with POA&M.** Corrected the Homebrew YubiKey/SSH table: `ykman` and `yubico-piv-tool` were **removed from the Mac host 2026-06-12** under least-functionality (CM-7) per POA&M-002's hygiene actions — the prior "installed, unused" listing was stale (this SBOM line predated/missed the removal). Removal confirmed absent via `brew list` (2026-06-29). `libfido2` and Homebrew `openssh` retained. No SPRS impact. |

---

## SYSTEM 1: services.[DOMAIN.ORG] (Rocky Linux 9.7 Service VM)

**Platform:** Rocky Linux 9.7 (Blue Onyx)  
**Kernel:** 5.14.0-611.45.1.el9_7.aarch64  
**Architecture:** aarch64 (ARM64)  
**Hypervisor:** UTM (QEMU ARM64) on Mac mini M4 Pro  
**FIPS Mode:** Enabled (fips=1 kernel parameter, crypto-policy=FIPS)  
**SELinux:** Enforcing  
**Total Packages:** ~817 RPM  
**IP Address:** [LAN-IP-REDACTED]/24 (LAN)  
**Role:** Domain Controller, Mail Server, VPN Endpoint, IDS, SIEM, Web, Webmail, Monitoring  

### Disk Configuration

- **Full-disk encryption:** LUKS2 AES-256-XTS on vda3 (198.4 GB)
- **Volume manager:** LVM on LUKS
- **Partitions:** /boot/efi (EFI), /boot (XFS), / (20GB), /var (25GB, nodev), /var/log (10GB), /var/log/audit (10GB), /tmp (5GB, noexec,nosuid), /home (10GB), /opt (50GB), swap (8GB)
- **GRUB2:** Password protected

---

### Critical Security Software

#### Identity & Access Management

| Package | Version | Purpose |
|---------|---------|---------|
| **389-ds-base** | 2.7.0-12.el9_7.aarch64 | LDAP Directory Server — dc=diwai,dc=org |
| **sssd** | (system) | System Security Services Daemon |

**LDAP Structure:**
- Base DN: `dc=diwai,dc=org`
- OUs: people, groups, permissions, services
- Auth backends: Dovecot IMAP, Postfix SASL, system PAM

#### Web Services

| Package | Version | Purpose |
|---------|---------|---------|
| **httpd** | 2.4.62-7.el9_7.3.aarch64 | Apache HTTP Server |
| **mod_ssl** | 2.4.62-7.el9_7.3.aarch64 | TLS module for Apache |
| **php-fpm** | 8.2.30-1.module_php.8.2.el9.remi.aarch64 | PHP FastCGI Process Manager (Roundcube) — Remi repo |
| **roundcubemail** | 1.5.15-1.el9.noarch | Webmail interface |

**Virtual Hosts:** [DOMAIN.ORG], webmail.[DOMAIN.ORG], ldap.[DOMAIN.ORG] (LAN), monitor.[DOMAIN.ORG] (LAN), wazuh.[DOMAIN.ORG] (LAN)

#### Email Services

| Package | Version | Purpose |
|---------|---------|---------|
| **postfix** | 3.5.25-1.el9.aarch64 | SMTP Mail Transfer Agent (ports 25, 465, 587) |
| **dovecot** | 2.3.16-15.el9.aarch64 | IMAP/POP3 Mail Server (port 993 IMAPS) |
| **mariadb-server** | 10.5.29-3.el9_7.aarch64 | MariaDB database (Roundcube backend) |

**Mail Auth:** SASL via Dovecot → LDAP  
**Mail Storage:** Maildir format in user home directories  

#### VPN

| Package | Version | Purpose |
|---------|---------|---------|
| **openvpn** | 2.5.11-1.el9.aarch64 | OpenVPN server (UDP 1194) |
| **easy-rsa** | 3.2.1-2.el9.noarch | RSA PKI management |

**VPN Config:** AES-256-GCM, TLS 1.2+, RSA-4096 keys, tunnel 10.8.0.0/24

#### Security & Monitoring

| Package | Version | Purpose |
|---------|---------|---------|
| **suricata** | 7.0.13-1.el9.aarch64 | Network IDS (AF_PACKET, enp0s1) |
| **wazuh-manager** | 4.14.4-1.aarch64 | SIEM — log collection, FIM, rootcheck |
| ~~**grafana**~~ | ~~13.1.1-1.aarch64~~ | Metrics visualization dashboard — **DECOMMISSIONED 2026-08-02** |
| **prometheus** | 3.10.0-1.el9.aarch64 | Time-series metrics collection |
| **node-exporter** | 1.11.1-1.el9.aarch64 | Host metrics for Prometheus |
| **audit** | 3.1.5-7.el9.aarch64 | Linux kernel audit subsystem |
| **usbguard** | 1.0.0-16.el9.aarch64 | USB device access control |

**Suricata Rules:** Emerging Threats ruleset (~49,521 rules)  
**Wazuh Integrations:** syslog, auditd, httpd access logs, OpenVPN, Suricata EVE JSON  

**Status (2026-08-02):** Grafana was **decommissioned and removed** (`grafana`, `grafana-selinux`, `grafana-pcp`; 1.0 GB freed). It was **not updatable** — `rpm.grafana.com` failed GPG verification on `repomd.xml`, so the installed 13.1.1 could not be patched, and the failing repository also broke `dnf check-update` system-wide. Its use was limited to metrics dashboards. **Metrics collection is unaffected:** Prometheus and node-exporter remain operational (verified running 2026-08-03), so the underlying telemetry and its retention are intact — only the visualization layer was retired. No control depended on Grafana as its sole mechanism; audit review (AU-6 / 3.3.3) and unauthorized-use identification (3.14.7) rest on the Wazuh Dashboard, auditd, and Suricata. Change record `DIWAI-CR-2026-08-04`; `/etc/grafana` backed up to `/root/grafana-removal-2026-08-02/`, `/var/lib/grafana` (49 MB) intentionally retained.

#### Malicious-Code Protection (SI-3)

| Package | Version | Purpose |
|---------|---------|---------|
| **yara** | 4.5.2 | Malicious-code pattern scanner — **active SI-3 control** (5,972 rules; Wazuh active-response on FIM 550/554 + weekly full-system scan via `yara-fullscan.timer`) |
| ~~**clamav**~~ | ~~1.4.3-3.el9.aarch64~~ | ClamAV antivirus engine — **DECOMMISSIONED 2026-06-12; PACKAGE REMOVED 2026-08-01** |
| ~~**clamd**~~ | ~~1.4.3-3.el9.aarch64~~ | ClamAV daemon — **DECOMMISSIONED 2026-06-12; PACKAGE REMOVED 2026-08-01** |

**Status (2026-06-12):** ClamAV was **decommissioned** — **incompatible with FIPS 140**. It could neither download nor load any signature database (OpenSSL verification failure under FIPS), so it provided no detection. Malicious-code protection (SI-3) is now provided by an already-operational, FIPS-native stack: **YARA 4.5.2** + VirusTotal reputation lookups + fapolicyd application allow-listing + SELinux enforcing + Suricata network IDS. Control substitution documented in SSP §3.14.2 / `DIWAI-EV-SI3-002` (supersedes RISK-2026-004); POA&M-002 closed.

**Update (2026-08-01):** the packages themselves were **removed** (`clamav`, `clamav-filesystem`, `clamav-freshclam`, `clamav-lib`, `clamd`; 138 MB). Between 2026-06-12 and 2026-08-01 the software remained installed and was still being auto-upgraded while the SSP recorded it decommissioned — a configuration-management defect tracked as **F-2026-08-06**, never a protection gap, since the substituted SI-3 stack was carrying the control throughout. Inventory and reality now agree and **F-2026-08-06 is closed**. Change record `DIWAI-CR-2026-08-01` C14.

#### DNS

| Package | Version | Purpose |
|---------|---------|---------|
| **unbound** | 1.16.2-21.el9.aarch64 | Recursive DNS resolver (local) |

#### Certificate Management

| Package | Version | Purpose |
|---------|---------|---------|
| **certbot** | 3.1.0-1.el9.noarch | Let's Encrypt ACME client |
| **python3-certbot-dns-cloudflare** | 3.1.0-1.el9.noarch | Cloudflare DNS-01 plugin |

**Certificate:** `*.[DOMAIN.ORG]` + `[DOMAIN.ORG]` wildcard (Let's Encrypt R12)  
**Expiry:** 2026-07-09  
**Auto-renewal:** `certbot-renew.timer` nightly; deploys via hook, restarts all TLS services  

#### Encryption & FIPS

| Package | Version | Purpose |
|---------|---------|---------|
| **openssl** | 3.5.1-7.el9_7.aarch64 | FIPS-validated TLS/crypto library |
| **openssl-libs** | 3.5.1-7.el9_7.aarch64 | OpenSSL shared libraries |
| **gnutls** | 3.8.3-10.el9_7.aarch64 | FIPS-validated TLS library |
| **cryptsetup-libs** | 2.7.2-4.el9.aarch64 | LUKS/dm-crypt support |

#### Container Runtime

| Package | Version | Purpose |
|---------|---------|---------|
| **podman** | 5.6.0-14.el9_7.aarch64 | Container runtime (available, not in use) |

#### Development & Admin Tools

| Package | Version | Purpose |
|---------|---------|---------|
| **python3** | 3.9.25-3.el9_7.2.aarch64 | Python 3 runtime |
| **git** | (system) | Version control |

#### Compliance

| Package | Version | Purpose |
|---------|---------|---------|
| **openscap** | 1.3.13-1.el9_7.rocky.0.1.aarch64 | SCAP compliance scanner |
| **openscap-scanner** | 1.3.13-1.el9_7.rocky.0.1.aarch64 | oscap CLI tool |
| **scap-security-guide** | 0.1.80-1.el9_7.rocky.1.2.noarch | NIST 800-171 CUI content |

**Last Scan Result:** 102 pass / 0 fail / 0 errors (2026-06-08)  
**Profile:** `xccdf_org.ssgproject.content_profile_cui`

---

## SYSTEM 2: Mac mini Host (macOS Tahoe 26.4)

**Platform:** macOS Tahoe 26.4.1 (Build 25E253)  
**Hardware:** Apple Mac mini (M4 Pro, 2024)  
**Chip:** Apple M4 Pro — 14-core CPU, 20-core GPU, 16-core Neural Engine  
**Architecture:** ARM64 (Apple Silicon)  
**RAM:** 64 GB unified memory  
**Storage:** 1.0 TB NVMe SSD (Apple Fabric)  
**Total Packages:** macOS native  
**Role:** Network Firewall/Router, AI Inference Host, Nextcloud (Private Cloud)  

### macOS System Software

#### Operating System

- **macOS Tahoe** 26.4.1 (Build 25E253) — Apple Unix-based OS
- **XNU Kernel** — Darwin kernel ARM64
- **System Integrity Protection (SIP)** — Enabled
- **Gatekeeper** — Enabled (code signing enforcement)

#### Security & Encryption

- **M4 Secure Enclave** — Hardware encryption, key storage
- **Secure Boot** — Boot integrity verification
- **XProtect** — Built-in malware protection
- **pf (Packet Filter)** — BSD firewall, NAT/RDR rules (config: `/etc/pf.conf`)
- **FileVault** — Full-disk encryption (APFS encryption via M4 Secure Enclave)

#### Network / Firewall

| Component | Version | Purpose |
|-----------|---------|---------|
| **pf** | macOS built-in | Stateful packet filter, NAT, port forwarding |
| **Cloudflare DNS** | — | Authoritative DNS for [DOMAIN.ORG] zone |

**pf Rules:**
- NAT: LAN ([LAN-IP-REDACTED]/24) → WAN ([WAN-IP-REDACTED])
- RDR: UDP [WAN-IP-REDACTED]:1194 → VM [LAN-IP-REDACTED]:1194 (VPN)
- Inbound allowed: TCP 22 (SSH), TCP 80/443 (.145), UDP 1194 (.146), TCP 25/465/587/993/995/4190 (.147), ICMP echo

#### USB Security

| Component | Location | Purpose |
|-----------|----------|---------|
| **usb-guard** | `/usr/local/sbin/usb-guard` | USB block/allow toggle script |
| **usb-guard-monitor** | `/usr/local/sbin/usb-guard-monitor` | LaunchDaemon polling monitor |
| **org.diwai.usb-guard** | `/Library/LaunchDaemons/` | LaunchDaemon (runs at boot) |

**State file:** `/var/lib/usb-guard/mode` (`on`/`off`)  
**Audit log:** `/var/log/usb-guard.log`

#### Nextcloud (Private Cloud / Document Management)

| Package | Version | Purpose |
|---------|---------|---------|
| **nextcloud** | 32.0.11.1 | Private cloud platform — `/opt/local/nextcloud`, data dir `/opt/local/nextcloud/data` (FileVault-encrypted) |
| **php** | 8.3.31 | PHP runtime (Homebrew, `php8.3-fpm`) |
| **nginx** | 1.31.0 | Reverse proxy / web server for `cloud.[DOMAIN.ORG]` (Homebrew) |
| **groupfolders** | 20.1.14 | Nextcloud app — shared CUI/FCI/Operations/AI-Knowledge-Base/Internal/Public/Archive group folders |
| **twofactor_totp** | (bundled) | Nextcloud app — TOTP 2FA, enforced instance-wide |
| **richdocuments (Collabora Online)** | 9.1.0 | Office document viewing/editing, proxied to `127.0.0.1:9980` |
| **redis** | 8.8.0 | Local file-locking / caching backend (`127.0.0.1:6379`, Homebrew) |

**Access:** `https://cloud.[DOMAIN.ORG]` — LAN-only (nginx binds `[LAN-IP-REDACTED]:443` / `127.0.0.1:443`; no WAN exposure, no Cloudflare Tunnel)  
**Backend (remote):** MariaDB (`nextcloud` DB) + LDAPS (`services.[DOMAIN.ORG]:636`, `dc=diwai,dc=org`) — both hosted on the Rocky Linux VM (System 1)  
**Folder taxonomy:** 7 groupfolders (CUI, Operations, AI-Knowledge-Base, FCI, Internal, Public, Archive); `CUI/Compliance/` holds `Evidence/`, `SSP/`, `POAM/`, `SBOM/` — this SBOM's canonical copy lives in `CUI/Compliance/SBOM/`  
**Authentication:** Instance-wide TOTP 2FA enforced (RFC 6238); enrolled for `dshannon`  
**Status:** Operational — supersedes any earlier plan to host Nextcloud on the Rocky Linux VM

#### AI Inference (Operational)

| Component | Version | Purpose |
|-----------|---------|---------|
| **mlx-lm** | 0.31.2 | MLX-based LLM serving engine (`mlx_lm.server`, port 8081, loopback) |
| **Magistral-Small-2509-MLX-4bit** | 4-bit MLX quant | Primary local LLM model (`/opt/local/models/Magistral-Small-2509-MLX-4bit`) |
| **Open WebUI** | 0.9.5 | Chat UI (port 3000, loopback) — reverse-proxied via nginx to `https://ai.[DOMAIN.ORG]` |
| **Ollama** | 0.21.2 | Secondary LLM runtime — serves `codestral`, `all-minilm` models |

**Status:** Operational  
**Platform:** Metal Performance Shaders (MPS) on M4 Pro 20-core GPU  
**Architecture:** `org.diwai.magistral` (LaunchAgent, `mlx_lm.server`) + `org.diwai.open-webui` (LaunchAgent, Open WebUI venv at `/opt/local/open-webui-venv`), both loopback-only; nginx reverse-proxies `https://ai.[DOMAIN.ORG]` → `127.0.0.1:3000` with TLS + WebSocket support  

#### YubiKey Hardware (Superseded — MFA Strategy Retired)

| Component | Detail | Purpose |
|-----------|--------|---------|
| **YubiKey 5C Nano FIPS** | Serial: [SERIAL-REDACTED] · Firmware: 5.4.3 · Form: Nano USB-C | Hardware security key — physically installed, **unpaired** |
| **FIPS Validation** | FIPS 140-2 Level 1 (YubiKey 5 FIPS Series) | Hardware security key |

**Status (2026-06-06):** PIV smartcard MFA for macOS local auth/screen lock has been **retired** following repeated PIV lockouts (2026-04-15, 2026-05-15). PIV slots 9A/9C unpaired from macOS; the key remains physically installed but has no active SSH/auth role. POA&M-001 closed-superseded by a unified **TOTP (RFC 6238)** MFA strategy covering VM SSH (POA&M-004) and macOS (POA&M-007), target Q3 2026 — see DIWAI-IAP-001 v1.1. Nextcloud's own TOTP 2FA (see Nextcloud section above) is independent of this POA&M and already enforced.

#### Homebrew Packages (YubiKey / SSH)

| Package | Version | Source | Purpose |
|---------|---------|--------|---------|
| ~~**ykman**~~ | ~~5.9.0~~ | Homebrew | YubiKey Manager — **REMOVED 2026-06-12** (CM-7, unused after YubiKey retirement; verified absent via `brew list`) |
| ~~**yubico-piv-tool**~~ | ~~2.7.3~~ | Homebrew | PIV tool — **REMOVED 2026-06-12** (CM-7, unused after YubiKey retirement; verified absent via `brew list`) |
| **libfido2** | 1.16.0_2 | Homebrew | FIDO2 library — dependency for Homebrew OpenSSH (retained) |
| **openssh** | 10.3p1 | Homebrew | OpenSSH compiled with libfido2 support (FIDO2-SK key ops) — retained |

**Note (updated 2026-06-29):** `ykman` and `yubico-piv-tool` were **removed from the Mac host on 2026-06-12** under least-functionality (CM-7) after the YubiKey PIV approach was retired — see POA&M-002 hygiene actions; confirmed absent by `brew list`. `libfido2` and Homebrew `openssh` are **retained** (Homebrew OpenSSH would be required if FIDO2-SK keys are ever reintroduced; macOS system OpenSSH 10.2p1/LibreSSL lacks libfido2). Current admin SSH to the VM uses an RSA-4096 key (`~/.ssh/diwai_rsa`), password+key auth.

#### Admin Tools

| Component | Purpose |
|-----------|---------|
| **SSH** (built-in + Homebrew 10.3p1) | Remote access to VM (`~/.ssh/diwai_rsa`); Homebrew SSH required for FIDO2-SK ops |
| **SuperDuper! 3.20-beta.8** | Bootable clone (blocked by Tahoe beta bug — deferred) |
| **Tunnelblick / OpenVPN Connect** | VPN client for `dshannon-diwai.ovpn` |

---

## CROSS-SYSTEM SECURITY CONTROLS

### Encryption

| Control | Implementation |
|---------|---------------|
| Disk encryption (VM) | LUKS2 AES-256-XTS on all CUI partitions |
| Disk encryption (Mac) | M4 Secure Enclave / APFS native |
| TLS in transit | TLS 1.2+ minimum, FIPS cipher suite |
| FIPS 140-2 (VM) | Enabled system-wide; kernel + OpenSSL + GnuTLS |

### Authentication

| Control | Implementation |
|---------|---------------|
| Centralized auth | 389 Directory Server (LDAP), dc=diwai,dc=org |
| Mail auth | Dovecot SASL → LDAP |
| Web auth | Apache + Roundcube → LDAP |
| Admin SSH (VM) | RSA-4096 key pair (`diwai_rsa`) + password; no MFA |
| Nextcloud auth | LDAPS (services.[DOMAIN.ORG]:636) + instance-wide TOTP 2FA (enforced) |
| macOS local auth | Standard macOS password auth; YubiKey PIV retired (see YubiKey Hardware, System 2) |
| MFA roadmap | Unified TOTP (RFC 6238) for VM SSH (POA&M-004) and macOS (POA&M-007) — target Q3 2026 |
| GRUB/LUKS | Passphrase protected |

### Monitoring

| Control | Implementation |
|---------|---------------|
| SIEM | Wazuh 4.14.4 (log collection, FIM, rootcheck) |
| Network IDS | Suricata 7.0.13 (Emerging Threats rules) |
| Metrics | Prometheus 3.10.0 + node-exporter 1.11.1 — Grafana decommissioned 2026-08-02 (collection retained, visualization retired) |
| Audit | auditd with comprehensive rules |
| Malicious-code scanning | YARA 4.5.2 (5,972 rules; SI-3 active) — ClamAV decommissioned 2026-06-12 |
| USB control | USBGuard (VM) + custom daemon (Mac) |

### Network Security

| Control | Implementation |
|---------|---------------|
| Perimeter firewall | pf on macOS (NAT, RDR, default drop) |
| VM firewall | firewalld (default drop zone) |
| SSH hardening | FIPS ciphers, no root login, key-only |
| DNS | Unbound local resolver; Cloudflare authoritative |

---

## BACKUP & RECOVERY

| Asset | Backup Method | Location | Date |
|-------|--------------|----------|------|
| Rocky Linux VM | UTM bundle copy | DataStore NAS: `/home/Backup/SecureMac/diwai-services.utm` | 2026-04-10 |
| Rocky Linux VM | UTM bundle copy | [NAS-HOSTNAME-REDACTED] NAS: `/VM/SecureMac-Backups/diwai-services.utm` | 2026-04-10 |
| Config files | File copy | DataStore NAS: `/Cyberinabox/Secure_Mac/` | 2026-04-10 |
| Nextcloud data dir | FileVault (at-rest only) | `/opt/local/nextcloud/data` (Mac mini, local disk) | — |
| Nextcloud data dir | NAS backup | **Not yet configured** — open item, NAS backup gap | — |
| Mac bootable clone | SuperDuper! | Deferred (Tahoe beta bug) | — |

---

## AI GOVERNANCE

### Local AI Inference (Operational)

**Purpose:** Administrative assistance for VSB operators; no CUI processed by AI  

| Control | Implementation |
|---------|---------------|
| Model hosting | Local only — Magistral-Small-2509-MLX (mlx_lm.server) + Ollama on Mac mini, exposed via `ai.[DOMAIN.ORG]` (loopback + nginx TLS proxy, no external API calls) |
| GPU acceleration | Apple M4 Pro Metal — 20-core GPU (MLX/MPS) |
| Data isolation | AI inference separate from compliance data; Nextcloud `AI-Knowledge-Base` groupfolder is the only AI-accessible document store |
| Human oversight | All AI-assisted actions require admin confirmation |

---

## VULNERABILITY MANAGEMENT

### Patch Management

**Rocky Linux VM:**
- Security updates via `dnf` from Rocky Linux official repositories
- Critical patches applied within 30 days
- Quarterly OpenSCAP compliance verification

**macOS Host:**
- Automatic security updates enabled
- macOS Tahoe updates via Apple Software Update
- Certbot renewal automated (nightly timer)

### Current Vulnerability Status (2026-06-11)

- VM OpenSCAP (`xccdf_org.ssgproject.content_profile_cui`): **102/102 checks passed** (2026-06-08) — zero failures
- macOS mSCP (`diwai_phase1` baseline): **129/134 checks passed** (2026-06-11) — 5 failing, tracked under POA&M-003 (Q3 2026); 1 N/A (os_dictation_disable, does not apply to this architecture)
- All packages current from official repositories
- No known critical vulnerabilities (CVSS >7.0)
- Let's Encrypt cert: valid, auto-renews before 2026-07-09

---

## LICENSE COMPLIANCE

### Open Source Licenses

| Software | License | Notes |
|---------|---------|-------|
| Rocky Linux 9.7 | GPL, BSD, Apache 2.0 (various) | Community enterprise Linux |
| Apache httpd | Apache 2.0 | Web server |
| 389 Directory Server | GPL v3 | LDAP server |
| Postfix | IBM Public License + EPL | MTA |
| Dovecot | MIT + LGPL | IMAP/POP3 |
| Roundcubemail | GPL v3 | Webmail |
| MariaDB | GPL v2 | Database |
| OpenVPN | GPL v2 | VPN |
| Suricata | GPL v2 | IDS |
| Wazuh | GPL v2 | SIEM |
| ~~Grafana~~ | ~~AGPLv3~~ | Dashboards — decommissioned 2026-08-02 |
| Prometheus | Apache 2.0 | Metrics |
| YARA | BSD-3-Clause | Malicious-code scanner (SI-3 active) |
| ~~ClamAV~~ | GPL v2 | Antivirus — decommissioned 2026-06-12 |
| Unbound | BSD | DNS resolver |
| USBGuard | GPL v2 | USB control |
| Certbot | Apache 2.0 | ACME client |
| OpenSSL | Apache 2.0 | Cryptography |
| OpenSCAP | LGPL | Compliance scanning |
| Nextcloud | AGPLv3 | Private cloud / document management |
| Collabora Online (richdocuments) | MPL 2.0 | Office document viewing/editing |
| Redis | BSD-3-Clause | Nextcloud file locking / caching |
| Open WebUI | BSD-3-Clause | Local AI chat UI |
| MLX / mlx-lm | MIT | Apple Silicon ML inference framework |
| Ollama | MIT | LLM inference (codestral, all-minilm) |
| macOS Tahoe | Proprietary Apple EULA | Included with hardware |

### Commercial Licenses

- **macOS Tahoe:** Included with Mac mini hardware purchase
- **Let's Encrypt wildcard cert:** Free (ISRG) — automated renewal
- All other software: Open source

### No PRC-Origin Software

All software sourced from US/European open source projects. No software of PRC origin is installed or planned. This is a hard requirement for Federal contract compliance.

---

## SUPPLY CHAIN SECURITY

### Software Sources

**Rocky Linux Packages:**
- Primary: Rocky Linux official repositories (HTTPS, GPG verified)
- EPEL: Extra Packages for Enterprise Linux (certbot, etc.)
- Wazuh: Official Wazuh repository (GPG verified)
- ~~Grafana: Official Grafana repository (GPG verified)~~ — **repository retired 2026-08-02** (`DIWAI-CR-2026-08-04` C44). The "GPG verified" claim had become false: `rpm.grafana.com` was **failing** GPG verification on `repomd.xml`, which both blocked patching of the installed Grafana and broke `dnf check-update` system-wide until the repository was removed
- Prometheus: Official release (GPG verified)
- Integrity: SHA-256 checksums verified by dnf

**macOS Software:**
- Primary: Apple Software Update (signed by Apple)
- Third-party: Gatekeeper / notarization required
- pf rules: Local configuration, no external downloads

**DNS:**
- Cloudflare DNS API (Cloudflare, Inc., US) for [DOMAIN.ORG] zone management

### Supply Chain Risk Mitigation

- Software obtained only from official upstream sources
- GPG signature verification mandatory (dnf)
- No software from unknown or untrusted sources
- No PRC-origin software (Federal hard requirement)
- Regular security updates from official channels only

---

## COMPLIANCE MAPPING

### NIST SP 800-171 Controls

| Control | Requirement | Implementation |
|---------|-------------|---------------|
| **CM-8** | Component inventory | This SBOM |
| **SR-2** | Supply chain risk | Verified sources, GPG checks |
| **SI-2** | Flaw remediation | dnf updates, OpenSCAP, Wazuh |
| **AC-17** | Remote access | OpenVPN AES-256-GCM, RSA-4096 |
| **AC-19** | Mobile/removable media | USBGuard (VM) + usb-guard daemon (Mac) |
| **IA-2** | Identification/Auth | 389-ds LDAP, SSH key-only |
| **SC-8** | Transmission confidentiality | TLS 1.2+, FIPS ciphers throughout |
| **SC-28** | Protection at rest | LUKS2 (VM), M4 Secure Enclave (Mac) |
| **AU-2** | Audit events | auditd + Wazuh SIEM |
| **SI-3** | Malware protection | YARA 4.5.2 (5,972 rules) + VirusTotal + fapolicyd + SELinux + Suricata IDS (FIPS-native); ClamAV decommissioned 2026-06-12 (DIWAI-EV-SI3-002, POA&M-002 closed) |

### OpenSCAP Compliance (VM)

- **Profile:** `xccdf_org.ssgproject.content_profile_cui` (NIST 800-171)
- **Last result:** 102 pass / 0 fail / 0 errors (2026-06-08)
- **Report:** `/root/oscap-report.html` (on VM); evidence copy at Nextcloud `CUI/Compliance/Evidence/oscap-20260424.html`
- **Next scheduled:** Quarterly (by 2026-07-01)

### mSCP Compliance (macOS)

- **Baseline:** `diwai_phase1` (macOS Security Compliance Project, `/usr/local/libexec/`)
- **Last result:** 129 pass / 5 fail / 1 N/A (2026-06-11)
- **Report:** `services.[DOMAIN.ORG]:/var/www/securemac/docs/evidence/mSCP-securemac-latest.html`; evidence copy at Nextcloud `CUI/Compliance/Evidence/mscp-20260424.html`
- **Open findings:** tracked under POA&M-003 (Q3 2026)
- **Next scheduled:** Weekly (`org.diwai.mscp-scan` LaunchAgent)

---

## MAINTENANCE SCHEDULE

### SBOM Update Triggers

**Quarterly Reviews:**
- Scheduled review aligned with SSP updates (June 30, September 30, December 31, March 31)
- Full package inventory refresh
- Verification of new software installations

**Event-Driven Updates:**
- New service added or removed
- Major package version updates
- Platform upgrades (Rocky Linux 9.7 → 9.8, macOS updates)
- AI model additions or changes (Magistral/Ollama)
- After security incidents

---

## POINT OF CONTACT

**SBOM Owner:** [SYSTEM-OWNER]  
**Title:** System Administrator / Security Officer  
**Organization:** [DOMAIN.ORG] — Do It With AI  
**Domain:** [DOMAIN.ORG]  

**For Questions Regarding:**
- Software inventory accuracy
- Vulnerability management
- License compliance
- Supply chain security

---

## DOCUMENT CONTROL

**Classification:** CONTROLLED UNCLASSIFIED INFORMATION (CUI)  
**Distribution:** Official Use Only — Need to Know Basis  
**Retention:** Current + 3 years  
**Next Review:** 2026-06-30  
**Local Copy:** `~/Documents/SecureMac Project Docs/Software_Bill_of_Materials.md`  
**Canonical CUI Copy (Nextcloud):** `https://cloud.[DOMAIN.ORG]` → `CUI/Compliance/SBOM/Software_Bill_of_Materials.md`  
**NAS Copy:** `DataStore:/Cyberinabox/Secure_Mac/`  

---

**END OF SBOM v3.2**

*This document supports NIST SP 800-171 CM-8, SR-2, and CMMC Level 2 compliance requirements for the [DOMAIN.ORG] SecureMac Reference System.*

---
