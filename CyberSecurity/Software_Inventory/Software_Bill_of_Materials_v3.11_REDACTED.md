> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# SOFTWARE BILL OF MATERIALS (SBOM) — [DOMAIN.ORG] SecureMac Reference System

**System:** [DOMAIN.ORG] SecureMac Reference System  
**Organization:** [DOMAIN.ORG] (Do It With AI)  
**Classification:** Controlled Unclassified Information (CUI)  
**Version:** 3.11  
**Date Generated:** 2026-10-03  
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
| 3.4 | 2026-10-03 | [SYSTEM-OWNER] | **AI inference reconciliation (record-completeness).** Drift found by local check RC-001 (2026-09-26) and re-observed 2026-10-03 from the running host. **Corrected:** Ollama 0.21.2 → **0.34.4**; recorded models `codestral` and `all-minilm` are **not installed** and were removed from this SBOM. **Added (previously unrecorded):** seven Ollama models — `gemma4:31b-it-q8_0`, `gemma4:26b-a4b-it-q8_0`, `gemma4:26b-a4b-it-qat` (2026-09-24), `devstral:latest`, `devstral-agent:latest` (2026-08-20), `mistral:latest`, `nomic-embed-text:latest` (2026-04-10 — both already missing from v3.0); `org.diwai.ollama` LaunchAgent (replaces `brew services`, which overwrote runtime settings on restart) with 64K context, f16 KV cache, flash attention, loopback-only; LiteLLM 1.97.0 (on-demand loopback shim, `:4000`). **Status corrected:** `org.diwai.magistral` has `RunAtLoad`/`KeepAlive` false (plist changed 2026-08-20) and was not running when observed — Magistral is installed but not auto-started, so the section is no longer labelled operational as a whole. Licences of all installed models verified via `ollama show --license` (Apache 2.0). |
| 3.5 | 2026-10-03 | [SYSTEM-OWNER] | **Model server replaced: Ollama + mlx-lm → LM Studio (DIWAI-CR-2026-10-01).** LM Studio 0.4.25+1 is the single model runtime, mirroring the Mac Studio reference stack. **Added:** LM Studio (headless service, `org.diwai.lmstudio`, 127.0.0.1:1234, prompt logging off, no plugins enabled, LM Link not signed in); models devstral-small-2-2512 (MLX 4-bit, primary), gpt-oss-20b (MXFP4; **barred from drift checks: failed the injected-instruction test 3/3**), nomic-embed-text v1.5 f16 (Open WebUI embeddings; vectors identical to Ollama's, cosine 1.0000, so no re-embed) and Q4_K_M (bundled). **Retired, not removed:** Ollama 0.34.4 and its 7 models, mlx-lm 0.31.2 + Magistral, LiteLLM 1.97.0 (LM Studio serves the Anthropic Messages API natively). Open WebUI chat and both custom assistants now on devstral. |
| 3.6 | 2026-10-03 | [SYSTEM-OWNER] | **DIWAI document library (offline RAG), LM Studio tuning, Aider repointed (DIWAI-CR-2026-10-02).** **Added:** `~/diwai-rag` — read-only MCP server `diwai-rag` (LaunchAgent `org.diwai.rag-mcp`, **127.0.0.1:8767**), browser manager (`/Applications/DIWAI Library.app`, **127.0.0.1:8766**, on demand), recovery tool; Python 3.12.15 environment with 13 pinned packages; HTMX 2.0.4 vendored; Homebrew `python@3.12` 3.12.15 and `ghostscript` 10.08.0; LM Studio model `google/gemma-4-e4b` (MLX 4-bit); LM Studio `mcp.json` entry and "DIWAI Library" preset; Open WebUI tool server "DIWAI Library (read-only)". **Changed:** LM Studio `developer.unloadPreviousJITModelOnLoad` true → false (Devstral and the embedder stay loaded together). **Previously unrecorded, now listed:** Aider 0.86.2 (pipx 1.11.1, repointed from Ollama to LM Studio), Tesseract 5.5.3. Model files verified against Hugging Face sha256 (24/24). |
| 3.7 | 2026-10-03 | [SYSTEM-OWNER] | **Open WebUI 0.9.5 → 0.11.4 (DIWAI-CR-2026-10-03).** Owner-approved manual update (decision register row 11): 56 Python packages in `/opt/local/open-webui-venv` were updated or newly installed (11 of them new: aiodns, antlr4-python3-runtime, colorlog, google-re2, hiredis, joserfc, langchain-protocol, omegaconf, pycares, python-docx, rapidocr; none removed), including chromadb 1.5.2 → 1.5.9, SQLAlchemy 2.0.48 → 2.0.50, fastapi 0.135.1 → 0.136.3, sentence-transformers 5.4.0 → 5.5.1 (full lists before and after kept with the change record). 16 database migrations applied. Still loopback-only (127.0.0.1:3000). **Also corrected:** the diwai-rag row now cites git `main` (the `phase2-build` branch was merged and deleted 2026-10-03). |
| 3.8 | 2026-10-03 | [SYSTEM-OWNER] | **Aider put on a leash (DIWAI-CR-2026-10-04, decision 13).** **Added:** `aider-leashed` launcher (bash, `~/diwai/aider-leash/`, 18 unit tests + live check 8/8). **Changed:** Aider context file brought in line with decision 13 (drafting role; retired services removed). **Corrected:** the Aider row said "a person approves every edit"; Aider writes to in-chat files without asking, so the row now says a person reviews every edit and approves every command. |
| 3.9 | 2026-10-03 | [SYSTEM-OWNER] | **Retired Ollama models removed (DIWAI-CR-2026-10-05).** 7 models, 90 GB, deleted from `~/.ollama/models`: devstral, devstral-agent, gemma4 26b-a4b-it-q8_0, gemma4 26b-a4b-it-qat, gemma4 31b-it-q8_0, mistral, nomic-embed-text. The Ollama binary, the disabled launcher and the retired Magistral MLX model (13 GB, `/opt/local/models`) are unchanged. |
| 3.10 | 2026-10-04 | [SYSTEM-OWNER] | **Repair library v1 (DIWAI-CR-2026-10-07).** **Added:** `diwai-repair` (root-owned, standard-library Python) with two YubiKey-approved repairs; approver key = P-256 FIDO2 credential on a standard YubiKey 5 (public key SHA-256 `42ca390a…104f`). **Changed:** Open WebUI launcher gains `CORS_ALLOW_ORIGIN=https://ai.[DOMAIN.ORG]` (run by the repair). **Related:** VM sudo now asks for the password (DIWAI-CR-2026-10-06). |
| 3.11 | 2026-10-04 | [SYSTEM-OWNER] | **Magistral back in service through LM Studio (DIWAI-CR-2026-10-08).** The retired Magistral Small 2509 MLX model (kept by owner decision) was verified against the publisher and copied (APFS clone, no extra space) into LM Studio as `magistral-small-2509-mlx`; Open WebUI assistant `magistral-general` added. mlx-lm stays retired. |

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

**VPN Config:** AES-256-GCM, TLS 1.2+, RSA-4096 keys, tunnel [VPN-SUBNET-REDACTED]

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
**Storage:** 1.0 TB NVMe SSD (Apple Fabric), FileVault (Secure Enclave)  
**Attached storage (fixed, rack-resident):** *On Apple Silicon, capacity beyond the internal SSD is necessarily Thunderbolt- or USB-attached; both volumes below report `Removable Media: Fixed` and are protected by full-disk encryption, drive marking and the locked rack cabinet — they are **not** portable media (`DIWAI-CR-2026-09-09`).*

| Volume | Device | Capacity / used | Encryption | Role |
|:---|:---|:---|:---|:---|
| `SecureMac` | USB SATA SSD, APFS (case-sensitive) | 499.9 GB / 395.5 GB | **FileVault** | Time Machine destination |
| `CyberHygiene Project` | USB SATA SSD, APFS | 249.8 GB / 2.3 GB | **FileVault — encrypted 2026-09-15**, `DIWAI-CR-2026-09-09` C125 | Historical reference / publish-transfer volume; USBGuard UUID `FED67739-…` |

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
**Authentication:** Instance-wide TOTP 2FA enforced (RFC 6238); enrolled for `[USERNAME]`  
**Status:** Operational — supersedes any earlier plan to host Nextcloud on the Rocky Linux VM

#### AI Inference

| Component | Version | Purpose |
|-----------|---------|---------|
| **LM Studio** | 0.4.25+1 | **Single model runtime.** Headless service (`LM Studio --run-as-service`), OpenAI- and Anthropic-compatible API on **127.0.0.1:1234** only. Element Labs Inc, notarized (`D65G88RHWN`) |
| ↳ mlx-llm engine | 1.11.0 | Serves MLX (safetensors) models |
| ↳ llama.cpp engine | 2.51.0 | Serves GGUF models, incl. embeddings |
| **Open WebUI** | 0.11.4 | Chat UI (port 3000, loopback), reverse-proxied via nginx to `https://ai.[DOMAIN.ORG]`; chat and RAG embeddings both use LM Studio |

**LM Studio models** (observed 2026-10-03, `lms ls --json`):

| Model | Variant | Size | Licence | Role |
|-------|---------|------|---------|------|
| `mistralai/devstral-small-2-2512` | MLX 4-bit | 15.1 GB | Apache 2.0 | Primary. Drift checks, Open WebUI assistants, offline Claude Code |
| `openai/gpt-oss-20b` | MXFP4 | 12.1 GB | Apache 2.0 | Fast alternative. **Not for drift checks**: obeyed an injected instruction in 3 of 3 test runs |
| `text-embedding-nomic-embed-text-v1.5@f16` | GGUF f16 | 0.27 GB | Apache 2.0 | Open WebUI RAG embeddings (identical vectors to the former Ollama build) |
| `text-embedding-nomic-embed-text-v1.5@q4_k_m` | GGUF Q4_K_M | 0.08 GB | Apache 2.0 | Bundled with LM Studio; not used (cosine 0.93 vs f16) |
| `google/gemma-4-e4b` | MLX 4-bit (`lmstudio-community/gemma-4-E4B-it-MLX-4bit`) | 6.9 GB | Apache 2.0 | Small fallback model (added 2026-10-03, CR-2026-10-02). The library prefers Devstral |
| `magistral-small-2509-mlx` | MLX 4-bit (`lmstudio-community/Magistral-Small-2509-MLX-4bit`, base `mistralai/Magistral-Small-2509`) | 13.1 GB | Apache 2.0 | General questions and writing (not coding); reasoning model, thinking in `[THINK]` markers. Open WebUI assistant "Magistral (general)" folds the thinking away. Files verified 14/14 against the publisher (5 SHA-256, 9 byte-identical) |

**Status:** LM Studio and Open WebUI operational (auto-start)  
**Platform:** Metal on M4 Pro 20-core GPU  
**Architecture:** `org.diwai.lmstudio` (LaunchAgent, RunAtLoad) runs `lms server start --port 1234 --bind 127.0.0.1`. Server settings in `~/.lmstudio/.internal/http-server-config.json`: `networkInterface` 127.0.0.1, `cors` false, **`logSensitiveData` false** (default was true). `settings.json`: development plugins off, runtime auto-update off, context 32768, JIT loading with 1 h idle unload, **`developer.unloadPreviousJITModelOnLoad` false** (2026-10-03, CR-2026-10-02: Devstral and the embedder stay loaded together; the service must be restarted, and it needs SIGKILL, for the setting to apply). `mcp.json`: one server, `diwai-rag` (read-only). Preset "DIWAI Library" in `config-presets/`. Model files verified against Hugging Face sha256 on 2026-10-03. **The app can still check for and stage its own updates**; check the version after every restart. `org.diwai.open-webui` (LaunchAgent) → nginx → `https://ai.[DOMAIN.ORG]`.

#### DIWAI Document Library (offline RAG) — `DIWAI-CR-2026-10-02`

Local library the models search offline (`~/diwai-rag`, local git, no remote). **The AI's access is read-only**: its MCP tools search and list; only a person adds or removes documents.

| Component | Version | Purpose |
|-----------|---------|---------|
| **diwai-rag MCP server** | project (git `main`) | Tools `search_documents`, `search_identifiers`, `list_documents`. LM Studio via stdio (`~/.lmstudio/mcp.json`); Open WebUI via streamable HTTP on **127.0.0.1:8767** (LaunchAgent `org.diwai.rag-mcp`, KeepAlive). DNS-rebinding protection on |
| **Browser manager** | project | Add/remove documents by drag and drop; **127.0.0.1:8766**; started on demand by `/Applications/DIWAI Library.app`, stops on Quit. Single writer thread |
| **Recovery tool** `rebuild_index.py` | project | Rebuilds the vector index from `chroma.sqlite3` into a fresh store; non-destructive |
| **Python** (Homebrew `python@3.12`) | 3.12.15 | Project environment `~/diwai-rag/venv` |
| ↳ chromadb | 1.5.9 | Vector store (`~/diwai-rag/data/chroma_db`, collection `diwai_sysadmin`, cosine) |
| ↳ fastapi / uvicorn / Jinja2 / python-multipart | 0.142.2 / 0.54.0 / 3.1.6 / 0.0.32 | Browser manager |
| ↳ mcp | 2.3.0 | MCP server SDK |
| ↳ pypdf / python-docx / python-pptx / lxml | 6.19.0 / 1.2.0 / 1.0.2 / 6.1.3 | Document readers |
| ↳ requests / httpx / pytest | 2.34.2 / 0.28.1 / 9.1.1 | LM Studio calls; tests |
| **HTMX** (vendored) | 2.0.4 | Browser-manager pages; served locally, sha256 `e209dda5…8fb447` |
| **Ghostscript** (Homebrew) | 10.08.0 | PDF text fallback (no automatic OCR) |
| **Tesseract** (Homebrew) | 5.5.3 | Manual OCR of scanned PDFs only (previously unrecorded) |

**Embeddings:** LM Studio `text-embedding-nomic-embed-text-v1.5@f16` with `search_document:`/`search_query:` task labels. **Content (2026-10-03):** 49 documents, 1,520 chunks — RB-00…RB-18, 13 draft runbook cards, 10 vendor pages with provenance records, and 7 owner-added references.

**Retired 2026-10-03 (installed, not running; removal is a later change):** Ollama 0.34.4 (`org.diwai.ollama.plist.disabled`; binary on disk, **models removed 2026-10-03**, DIWAI-CR-2026-10-05), mlx-lm 0.31.2 + Magistral-Small-2509 (`org.diwai.magistral.plist.disabled`), LiteLLM 1.97.0 (`~/diwai/litellm-venv`, not started).

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
| **Tunnelblick / OpenVPN Connect** | VPN client for `[USERNAME]-diwai.ovpn` |
| **Aider 0.86.2** (pipx 1.11.1, Python 3.11) | AI pair-programming CLI on the build side: drafts runbooks, repairs and tests; never edits a live configuration file itself; may run an ISSO-approved repair after a typed yes (decision 13, option B). Started through **`aider-leashed`** (`~/diwai/aider-leash/`, git-tracked; linked as `~/.local/bin/aider-leashed`), which refuses project-level Aider settings and flags that skip a person, and turns automatic test/lint commands off. It edits only the files a person adds to the chat; a person reviews every edit; a shell command runs only after a typed yes. Context file `~/diwai/aider-system-context.md` (updated 2026-10-03). Model: Devstral via LM Studio 127.0.0.1:1234 (repointed from Ollama 2026-10-03); offline settings (no update check, no analytics, no model-price download); temperature 0.15. Previously unrecorded |
| **diwai-repair 1.0** (repair library; `/usr/local/lib/diwai-repair`, root-owned; `/usr/local/bin/diwai-repair`) | Runs only ISSO-approved repairs (check, back up, one change, verify, undo). Python standard library under `/usr/bin/python3` 3.9.6; approvals = YubiKey FIDO2 assertions (`fido2-assert`, PIN + touch; libfido2 1.17.0, Homebrew) checked with `/usr/bin/openssl` (LibreSSL 3.3.6). Run records `/var/db/diwai-repair/runs` (root, 700). Source `~/diwai-rag` (git). v1 repairs: `owui-cors-any-origin`, `wazuh-ruleset-missing` (DIWAI-CR-2026-10-07) |

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
| **Mac host (full system)** | **Time Machine** | **`SecureMac` — USB-attached APFS, FileVault-encrypted, 395.5 GB of 499.9 GB used** | **2026-09-15 16:50** |
| Mac bootable clone | SuperDuper! | Deferred (Tahoe beta bug) | — |

> **Added 2026-09-15 (`DIWAI-CR-2026-09-09` C127).** Time Machine was **absent from
> this table entirely** although it is the primary Mac backup and holds CUI. An
> asset absent from the inventory is an asset no assessment examines.


---

## AI GOVERNANCE

### Local AI Inference (Operational)

**Purpose:** Administrative assistance for VSB operators; no CUI processed by AI  

| Control | Implementation |
|---------|---------------|
| Model hosting | Local only — LM Studio (127.0.0.1:1234) on Mac mini, exposed via `ai.[DOMAIN.ORG]` (loopback + nginx TLS proxy, no external API calls) |
| GPU acceleration | Apple M4 Pro Metal — 20-core GPU (MLX/MPS) |
| Data isolation | AI inference separate from compliance data. AI-accessible document stores: the Nextcloud `AI-Knowledge-Base` groupfolder (Open WebUI) and the DIWAI document library `~/diwai-rag` (read-only to the AI; documents added by a person; CR-2026-10-02) |
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
| LM Studio | Proprietary (Element Labs terms; no-cost) | Model runtime |
| MLX / mlx-llm, llama.cpp | MIT | Inference engines bundled with LM Studio |
| Ollama, LiteLLM (retired, on disk) | MIT | Former runtime / shim |
| Devstral, gpt-oss, nomic-embed-text, Gemma 4 E4B (LM Studio); Gemma 4, Mistral 7B (retired; Ollama copies removed 2026-10-03) (model weights) | Apache 2.0 | Local LLM / embedding models (verified `ollama show --license`) |
| Aider | Apache 2.0 | AI pair-programming CLI |
| chromadb | Apache 2.0 | Vector store (DIWAI library) |
| FastAPI, mcp, python-docx, python-pptx, pytest, pipx | MIT | DIWAI library components; pipx installer |
| uvicorn, Jinja2, lxml, pypdf, httpx | BSD-3-Clause | DIWAI library components |
| requests, python-multipart | Apache 2.0 | DIWAI library components |
| HTMX 2.0.4 | 0BSD | Browser-manager pages (vendored) |
| Ghostscript | AGPL-3.0-or-later | PDF text fallback (run as a separate program) |
| Tesseract | Apache 2.0 | Manual OCR |
| Python 3.12 | PSF License | DIWAI library runtime |
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
- AI model additions or changes (LM Studio)
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
