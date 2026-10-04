> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# System and Communications Protection Policy

**Document ID:** DIWAI-SCP-001
**Editorial Correction (2026-08-01):** Document identifier changed from `TCC-SCP-001` to `DIWAI-SCP-001`; internal policy cross-references normalised to the `DIWAI-*` set. Identifier only — **no control content changed** and the version is deliberately not incremented. Aligns this document with the SSP citation set and the [DOMAIN.ORG] independence determination (SSP v2.12 corrected). See `DIWAI-EV-CM-2026-08-01`.
**Version:** 1.1
**Effective Date:** February 15, 2026
**Review Schedule:** Annually
**Next Review:** December 2026
**Owner:** [SYSTEM-OWNER], ISSO/System Owner
**Distribution:** Authorized personnel only
**Classification:** CUI

---


**Version 1.1 (2026-08-04) — technical accuracy correction.** Inherited from
Reference System #1 (CyberInABox) and bulk-edited for [DOMAIN.ORG].

**Two claims asserted controls stronger than those in place. Both are corrected
rather than restated:**

1. **"Firewall/IDS functions on separate hardware (pfSense appliance)."** There is no separate hardware and no DMZ. The perimeter firewall (`pf`) runs on the Mac mini, which is also the hypervisor for the VM carrying the directory, SIEM and CUI database, and which holds the Nextcloud file store. This condition is **formally accepted** — risk **R-02** (HIGH) in `DIWAI-RAR-001`, tracked as **POA&M-023**, accepted in writing to 2027-03-31. **A signed policy claiming the separation exists directly contradicted an accepted risk stating it does not.**
2. **"Suricata — IPS mode: Block and alert on threats."** Verified 2026-08-04: Suricata runs af-packet on `enp0s1`/`tun0` with no inline copy-mode and no nfqueue — **IDS only**. It detects and alerts; it does not block. Blocking is performed by `pf` and `firewalld` on rules, not by Suricata on detections.

**Host inventory corrected.** The scope list gave `services.[DOMAIN.ORG]` two
different addresses and roles, listed the Mac mini as a workstation, invented
`ws1`/`ws2`, and placed a pfSense appliance at **[LAN-IP-REDACTED]** — the Mac's own
address. Three different entities claimed one IP. Replaced with the actual three
hosts; interface detail added for the triple-homed Mac.

Also corrected: §5.1 rewritten for macOS `pf` (`/etc/pf_diwai.conf`); the
superseded ClamAV FIPS risk-acceptance memo replaced with `DIWAI-EV-SI3-002`.
Workstation provisions retained and scoped. Raised as **POA&M-058**; no control
changed — but see item 1, where the policy had claimed one that never existed.


## 1. Purpose

This policy establishes [DOMAIN.ORG]'s requirements for protecting system boundaries and communications on the SecureMac Reference System #2. It ensures confidentiality, integrity, and availability of Controlled Unclassified Information (CUI) during storage and transmission in compliance with NIST SP 800-171 Rev 2 (SC-1 through SC-28) and CMMC Level 2.

---

## 2. Scope

This policy applies to:

- **All SecureMac Systems:**
  - `securemac.[DOMAIN.ORG]` / `ai.[DOMAIN.ORG]` (**[LAN-IP-REDACTED]**) — Mac mini M4 Pro: perimeter firewall (macOS `pf`), hypervisor, Nextcloud CUI store, AI inference, sole management workstation
  - `services.[DOMAIN.ORG]` (**[LAN-IP-REDACTED]**) — Rocky Linux VM: 389-DS directory, Wazuh SIEM, mail, Nextcloud database
  - `nas.[DOMAIN.ORG]` (**[LAN-IP-REDACTED]**) — Synology NAS: backups and file shares
  - Workstations: none presently deployed; in scope where a deployment adds them

- **All Communications:**
  - Network traffic (internal and external)
  - Email communications
  - File transfers
  - Remote access connections
  - Voice/video communications
  - Administrative sessions

- **All Data States:**
  - Data in transit (network communications)
  - Data at rest (stored on systems)
  - Data in use (active processing)

---

## 3. Policy Statements

### 3.1 Application Partitioning (SC-2)

**The organization shall:**

1. **Separate User Functionality from Management Functionality:**
   - Administrative interfaces separated from user interfaces
   - Management traffic on dedicated network segments where feasible
   - Web-based admin interfaces on non-standard ports with restricted access

2. **Service Isolation:**
   - Each major service runs on dedicated system or container
   - File server (NAS) separate from domain controller functions
   - AI/ML workloads isolated on dedicated hardware (services.[DOMAIN.ORG])

### 3.2 Security Function Isolation (SC-3)

**The organization shall:**

1. **Security Functions Isolated:**
   - SELinux mandatory access control enforces isolation
   - Wazuh SIEM operates on the service VM
   - **Security functions are NOT isolated on separate hardware.** The perimeter firewall (`pf`) runs on the Mac mini, which is also the hypervisor for the VM carrying the directory, SIEM and CUI database, and which holds the Nextcloud file store. There is no DMZ and no dedicated firewall appliance.

     > This is a **known and formally accepted** condition, not an oversight: risk **R-02** (HIGH) in `DIWAI-RAR-001`, tracked as **POA&M-023**, accepted in writing until **2027-03-31**. The earlier text in this policy claimed separation on dedicated hardware; that claim was inherited from Reference System #1 and was never true here. Isolation is provided instead by SELinux, `fapolicyd`, per-host firewall rules and virtualization boundaries — mitigations, not separation.

2. **Least Privilege for Security Components:**
   - Security services run with minimal required permissions
   - Dedicated service accounts for security tools
   - No direct user access to security component internals

### 3.3 Information in Shared Resources (SC-4)

**The organization shall:**

1. **Prevent Unauthorized Information Transfer:**
   - Memory sanitization on process termination
   - Temporary files securely deleted (shred, wipe)
   - No residual CUI data in RAM or storage after access

2. **Shared Resource Protections:**
   - SELinux type enforcement prevents cross-process information leakage
   - File system permissions restrict access to user-owned files only
   - Virtualization not used (dedicated hardware reduces shared resource risks)

### 3.4 Denial of Service Protection (SC-5)

**The organization shall protect against denial of service attacks:**

1. **Network-Level Protections:**
   - `pf` state table limits on the Mac mini; `firewalld` connection limits on the VM
   - Syn flood protection enabled
   - Connection rate limiting per source IP
   - Geographic IP blocking for high-risk countries

2. **Application-Level Protections:**
   - Apache MaxRequestWorkers limit (prevent resource exhaustion)
   - Email rate limiting (Postfix: 10 messages/hour from single source)
   - Failed authentication rate limiting (5 attempts = 30-minute lockout)

3. **Resource Management:**
   - System resource limits (ulimit) configured per user
   - CPU and memory limits on services via systemd
   - Disk quotas considered for future implementation

### 3.5 Resource Availability (SC-6)

**The organization shall:**

1. **Protect Availability of Resources:**
   - Critical services configured for automatic restart (systemd watchdog)
   - Monitoring alerts on resource exhaustion (Wazuh)
   - Storage capacity monitoring (alert at 75%, critical at 90%)

2. **Priority Resource Allocation:**
   - Critical services (389-DS LDAP, Wazuh) have elevated priority
   - Nice values adjusted to prioritize security services
   - QoS on network for VoIP/video if implemented

### 3.6 Boundary Protection (SC-7)

**The organization shall:**

1. **Managed Interfaces (SC-7):**
   - macOS `pf` on the Mac mini controls all external connections
   - Default-deny firewall policy
   - Explicit allow rules for required services only
   - DMZ not required (no externally-facing services)

2. **External Telecommunications Services (SC-7(3)):**
   - Internet connectivity via commercial ISP
   - No direct external access to SecureMac resources
   - All external connections routed through `pf` on the Mac mini
   - Future: VPN with MFA for authorized remote access (POA&M-028)

3. **Access Points (SC-7(7)):**
   - Single internet connection point (`en0`, [ISP-REDACTED], on the Mac mini)
   - All wireless access points disabled or removed
   - Physical network ports in server room secured

4. **Firewall Configuration:**
   - Stateful packet inspection enabled
   - Outbound connections allowed from in-boundary hosts as permitted by the `pf` ruleset
   - Inbound connections blocked by default
   - Allowed inbound: None (air-gapped from external access)
   - Internal zone: [LAN-IP-REDACTED]/24 (trusted)

### 3.7 Split Tunneling Prevention (SC-7(4))

**The organization shall prevent:**

- Remote users from simultaneously connecting to SecureMac and untrusted networks
- VPN split tunneling prohibited when implemented (POA&M-028)
- All traffic routed through VPN tunnel (no local breakout)

### 3.8 Transmission Confidentiality and Integrity (SC-8, SC-8(1))

**The organization shall:**

1. **Encrypt CUI in Transit (SC-8(1)):**
   - **TLS 1.2 or higher** for all network communications
   - **SSH (OpenSSH 8.x+)** for administrative access
   - **Kerberos** for authentication (encrypted tickets)
   - **HTTPS** for all web-based services
   - **SMTPS/IMAPS** for email (TLS required)
   - **SMB3** with encryption for file sharing

2. **Prohibited Clear-Text Protocols:**
   - ❌ HTTP (redirect to HTTPS)
   - ❌ Telnet (SSH only)
   - ❌ FTP (SFTP only)
   - ❌ SMTP without TLS
   - ❌ POP3/IMAP without TLS

3. **Cryptographic Standards:**
   - FIPS 140-2 validated algorithms
   - AES-256 for symmetric encryption
   - RSA 3072-bit or ECDSA P-384 for asymmetric
   - SHA-256 or stronger for hashing
   - Perfect Forward Secrecy (PFS) enabled

### 3.9 Network Disconnect (SC-10)

**The organization shall:**

- Terminate network sessions after 15 minutes of inactivity
- SSH session timeout: ClientAliveInterval 300, ClientAliveCountMax 0
- Web session timeout: 15 minutes (application-specific)
- Kerberos ticket lifetime: 10 hours, renewable for 7 days

### 3.10 Cryptographic Key Establishment and Management (SC-12, SC-13)

**The organization shall:**

1. **FIPS 140-2 Cryptographic Protection (SC-13):**
   - FIPS mode enabled on all Rocky Linux systems
   - Only FIPS-approved algorithms permitted
   - Verification: `fips-mode-setup --check`

2. **Key Management (SC-12):**
   - **SSH Host Keys:**
     - Generated on first boot (automated)
     - RSA 3072-bit or Ed25519
     - Stored in `/etc/ssh/` with 0600 permissions
     - Backed up securely

   - **SSL/TLS Certificates:**
     - Commercial certificate from SSL.com (wildcard)
     - Private key: 2048-bit RSA minimum
     - Stored in `/etc/pki/tls/private/` with 0400 permissions
     - Annual renewal

   - **LUKS Encryption Keys:**
     - AES-256-XTS
     - Passphrase-based key derivation (PBKDF2)
     - Master key stored in LUKS header
     - Backup passphrase stored in secure location (physical safe)

   - **Kerberos Keys:**
     - Managed by 389-DS LDAP
     - AES-256 encryption
     - Key rotation on password change

### 3.11 Cryptographic Protection (SC-13)

**Mandatory Cryptographic Use:**

| Data State | Protection Method | Algorithm |
|------------|-------------------|-----------|
| Data at Rest (disks) | LUKS full-disk encryption | AES-256-XTS |
| Data at Rest (macOS) | FileVault + T2/M4 Secure Enclave | AES-256-XTS |
| Data in Transit (web) | TLS 1.2+ | AES-256-GCM, ECDHE |
| Data in Transit (SSH) | OpenSSH | AES-256-CTR, Ed25519 |
| Data in Transit (email) | STARTTLS | AES-256-GCM |
| Data in Transit (files) | SMB3 encryption | AES-128-GCM |
| Authentication | Kerberos | AES-256-CTS-HMAC-SHA1-96 |
| VPN (future) | OpenVPN/WireGuard | AES-256-GCM / ChaCha20-Poly1305 |

### 3.12 Collaborative Computing Devices (SC-15)

**The organization shall:**

1. **Videoconferencing Security:**
   - Prohibit CUI discussion on unapproved platforms
   - Virtual backgrounds required to hide CUI in workspace
   - Microphone/camera muted when not actively speaking
   - Screen sharing limited to approved content only

2. **Approved Platforms:**
   - Zoom (enterprise account with encryption)
   - Microsoft Teams (with data residency in US)
   - Google Meet (enterprise only)

3. **Prohibited Platforms:**
   - Consumer-grade videoconferencing
   - Peer-to-peer video services
   - Platforms with foreign hosting/data storage

### 3.13 Protection of Information at Rest (SC-28, SC-28(1))

**The organization shall:**

1. **Full-Disk Encryption (SC-28(1)):**
   - **Rocky Linux systems:** LUKS AES-256-XTS
   - **macOS system (AI server):** FileVault with T2/M4 Secure Enclave
   - Encryption status verified monthly via OpenSCAP

2. **Encrypted Partitions:**
   - `/` root filesystem (LUKS)
   - `/home` user data (LUKS)
   - `/var` system logs and data (LUKS)
   - `/srv` file shares and services (LUKS)
   - `/data` CUI storage (LUKS)
   - `/backup` backup storage (LUKS - separate passphrase)

3. **Removable Media:**
   - USB drives encrypted with VeraCrypt or LUKS
   - CD/DVD burning prohibited (no optical drives)
   - External drives encrypted before CUI storage

4. **Backup Media Protection:**
   - Backup media encrypted (LUKS container)
   - Stored in locked, fireproof safe
   - Offsite backups transported in locked container
   - Annual backup restoration test

### 3.14 Mobile Code (SC-18)

**The organization shall:**

1. **Acceptable Mobile Code:**
   - JavaScript (web browsers, sandboxed)
   - Java (OpenJDK, from trusted repos only)
   - Python scripts (reviewed before execution)

2. **Prohibited Mobile Code:**
   - ActiveX controls
   - Flash/Shockwave
   - Unsigned Java applets
   - PowerShell scripts from untrusted sources

3. **Mobile Code Controls:**
   - Browser JavaScript enabled but restricted (NoScript extension considered)
   - Java applets blocked unless explicitly allowed
   - Code signing verification required for executables

### 3.15 Voice over Internet Protocol (SC-19)

**If VoIP is implemented:**

1. **VoIP Security Requirements:**
   - SIP/RTP encryption (SRTP)
   - Separate VLAN for voice traffic
   - Quality of Service (QoS) configured
   - VoIP provider must be US-based with encryption

2. **Current Status:** VoIP not implemented (traditional phone service used)

### 3.16 Secure Name/Address Resolution (SC-20, SC-21)

**The organization shall:**

1. **DNS Security (SC-20, SC-21):**
   - 389-DS LDAP provides authoritative DNS for [DOMAIN.ORG]
   - DNSSEC enabled for external queries
   - DNS queries authenticated via TSIG (zone transfers)
   - Recursive queries restricted to internal network only

2. **DNS Configuration:**
   - Internal DNS: services.[DOMAIN.ORG] ([LAN-IP-REDACTED])
   - External forwarders: 1.1.1.1 (Cloudflare), 8.8.8.8 (Google)
   - DNS over TLS (DoT) for external queries (future enhancement)

### 3.17 Architecture and Provisioning for Name/Address Resolution (SC-22)

**The organization shall:**

- Provide authoritative DNS within SecureMac (389-DS LDAP integrated DNS)
- Fault-tolerant: Secondary DNS on future backup domain controller
- DNS records signed with DNSSEC

### 3.18 Session Authenticity (SC-23)

**The organization shall:**

1. **Protect Session Authenticity:**
   - Kerberos tickets authenticated and encrypted
   - TLS session IDs randomized
   - SSH session keys unique per connection
   - HTTP cookies marked Secure and HttpOnly

2. **Session Hijacking Protections:**
   - TCP sequence number randomization
   - Strong session token generation (cryptographically random)
   - Session binding to IP address (where feasible)
   - Automatic logout on session timeout

### 3.19 Fail in Known State (SC-24)

**The organization shall:**

- Systems fail to secure state on failure
- SELinux enforces deny-by-default on errors
- Firewall defaults to block on rule processing errors
- Services disabled if critical dependencies fail (systemd dependencies)

### 3.20 Thin Nodes (SC-25)

**Not applicable:** SecureMac does not use thin clients or zero clients.

### 3.21 Honeypots (SC-26)

**Not implemented:** Honeypots not deployed. Deception technology not required for current risk profile.

### 3.22 Platform-Independent Applications (SC-27)

**The organization shall prioritize:**

- Cross-platform tools where feasible (Python, Java)
- Open standards and protocols
- Avoid vendor lock-in to proprietary systems

### 3.23 Protection of Information at Rest (SC-28)

**Addressed in Section 3.13 (SC-28, SC-28(1))**

---

## 4. Roles and Responsibilities

### 4.1 System Owner

- Approve encryption and boundary protection policies
- Ensure adequate resources for security infrastructure
- Review and approve firewall rule changes
- Authorize VPN and remote access implementations

### 4.2 Information System Security Officer (ISSO)

- Define security architecture and boundary protections
- Configure and maintain firewall rules
- Manage cryptographic key lifecycle
- Monitor network security controls (IDS/IPS)
- Approve encryption implementations
- Conduct annual security architecture review

### 4.3 System Administrator

- Implement and maintain encryption (LUKS, TLS, SSH)
- Configure network security controls (`pf` on the Mac mini, `firewalld` and Suricata on the VM)
- Monitor security logs for boundary violations
- Maintain TLS certificates (renewal, deployment)
- Configure secure communication protocols
- Implement session timeout and termination controls

### 4.4 All Users

- Use encrypted communication channels for CUI
- Verify TLS certificate validity (green padlock)
- Report unencrypted CUI transmission
- Comply with session timeout policies
- Do not disable security features (TLS, encryption)

---

## 5. Implementation Details

### 5.1 Perimeter Firewall Configuration — macOS `pf` on the Mac mini

**Interfaces (Mac mini, triple-homed):**
- `en0` — WAN, [WAN-IP-REDACTED]/29 ([ISP-REDACTED], static /29 block)
- `en6` — LAN/CUI, [LAN-IP-REDACTED]/24 (Thunderbolt Ethernet)
- `en1` — Wi-Fi, **powered off**; out of the CUI data path (SSP §2.5.2)

Ruleset: `/etc/pf_diwai.conf`, loaded with `pfctl -f`.

**Default Rules:**
- WAN inbound: BLOCK ALL (default deny)
- LAN outbound: ALLOW (in-boundary hosts require internet for updates and mail)
- LAN to LAN: ALLOW (internal communication)

**Suricata — intrusion *detection*, on the service VM:**
- Emerging Threats Open ruleset (~49,500 rules)
- Interfaces: `enp0s1`, `tun0` (af-packet)
- **IDS mode — detect and alert only.** Suricata is **not** deployed inline and does **not** block traffic. The inherited text claimed "IPS mode: Block and alert"; that overstated the control. Blocking is performed by `pf` and `firewalld`, on rules, not by Suricata on detections.
- Logs sent to Wazuh SIEM

**Advanced Settings:**
- SYN flood protection: enabled
- State table optimization: aggressive
- Bogon networks blocked
- RFC1918 WAN blocking: enabled

### 5.2 TLS/SSL Configuration

**Apache HTTPS Configuration:**

```apache
SSLEngine on
SSLProtocol -all +TLSv1.2 +TLSv1.3
SSLCipherSuite HIGH:!aNULL:!MD5:!3DES
SSLHonorCipherOrder on
SSLCompression off
SSLSessionTickets off
Header always set Strict-Transport-Security "max-age=31536000"
```

**Certificate Locations:**
- Certificate: `/etc/pki/tls/certs/[DOMAIN.ORG].crt`
- Private Key: `/etc/pki/tls/private/[DOMAIN.ORG].key`
- CA Chain: `/etc/pki/tls/certs/ca-bundle.crt`

### 5.3 SSH Hardening

**File:** `/etc/ssh/sshd_config`

```
Port 22
Protocol 2
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
ChallengeResponseAuthentication yes
UsePAM yes
X11Forwarding no
Ciphers aes256-ctr,aes192-ctr,aes128-ctr
MACs hmac-sha2-512,hmac-sha2-256
KexAlgorithms ecdh-sha2-nistp384,ecdh-sha2-nistp256
ClientAliveInterval 300
ClientAliveCountMax 0
```

### 5.4 Email Encryption

**Postfix TLS Configuration:**

```
# Outbound TLS
smtp_tls_security_level = may
smtp_tls_loglevel = 1
smtp_tls_protocols = !SSLv2, !SSLv3, !TLSv1, !TLSv1.1

# Inbound TLS
smtpd_tls_security_level = may
smtpd_tls_auth_only = yes
smtpd_tls_cert_file = /etc/pki/tls/certs/[DOMAIN.ORG].crt
smtpd_tls_key_file = /etc/pki/tls/private/[DOMAIN.ORG].key
smtpd_tls_protocols = !SSLv2, !SSLv3, !TLSv1, !TLSv1.1
```

### 5.5 LUKS Encryption Verification

**Monthly Verification Script:**

```bash
#!/bin/bash
# Check LUKS encryption status on all partitions

for dev in $(lsblk -ln -o NAME,TYPE | awk '$2=="crypt" {print $1}'); do
    echo "Checking /dev/mapper/$dev"
    cryptsetup status $dev
    cryptsetup luksDump /dev/$(readlink -f /dev/mapper/$dev | sed 's|/dev/mapper/||')
done
```

**Expected Output:**
- Type: LUKS2
- Cipher: aes-xts-plain64
- Key size: 512 bits (AES-256)

### 5.6 Network Segmentation (Future)

**Planned VLANs (if implemented):**
- LAN: Management ([LAN-IP-REDACTED]/24)
- Subnet: Mac host ([LAN-IP-REDACTED])
- Subnet: Services VM ([LAN-IP-REDACTED])
- Guest WiFi: isolated VLAN (if applicable)

**Current State:** Single flat network ([LAN-IP-REDACTED]/24)

---

## 6. Compliance Mapping

| NIST SP 800-171 Control | Implementation |
|-------------------------|----------------|
| **SC-1** Policy and Procedures | This document |
| **SC-2** Application Partitioning | Section 3.1 |
| **SC-3** Security Function Isolation | Section 3.2 |
| **SC-4** Information in Shared Resources | Section 3.3 |
| **SC-5** Denial of Service Protection | Section 3.4 |
| **SC-6** Resource Availability | Section 3.5 |
| **SC-7** Boundary Protection | Section 3.6 |
| **SC-7(3)** Access Points | Section 3.6.3 |
| **SC-7(4)** External Telecommunications | Section 3.7 |
| **SC-7(5)** Deny by Default / Allow by Exception | Section 3.6 firewall rules |
| **SC-8** Transmission Confidentiality/Integrity | Section 3.8 |
| **SC-8(1)** Cryptographic Protection | Section 3.8.1 |
| **SC-10** Network Disconnect | Section 3.9 |
| **SC-12** Cryptographic Key Management | Section 3.10 |
| **SC-13** Cryptographic Protection | Section 3.11 |
| **SC-15** Collaborative Computing Devices | Section 3.12 |
| **SC-17** Public Key Infrastructure | Section 3.10 (SSL certs) |
| **SC-18** Mobile Code | Section 3.14 |
| **SC-19** Voice over IP | Section 3.15 |
| **SC-20** Secure Name Resolution (authoritative) | Section 3.16 |
| **SC-21** Secure Name Resolution (recursive) | Section 3.16 |
| **SC-22** Architecture for Name Resolution | Section 3.17 |
| **SC-23** Session Authenticity | Section 3.18 |
| **SC-28** Protection of Information at Rest | Section 3.13 |
| **SC-28(1)** Cryptographic Protection (at rest) | Section 3.13.1 |

---

## 7. Prohibited Activities

**Users shall NOT:**

1. Disable or bypass encryption (LUKS, TLS, SSH)
2. Transmit CUI over unencrypted channels
3. Disable firewall or security services
4. Install unauthorized VPN or remote access software
5. Use split tunneling if VPN access granted
6. Modify cryptographic configurations
7. Share cryptographic keys or passphrases
8. Store CUI on unencrypted media
9. Use prohibited protocols (Telnet, FTP, HTTP for CUI)
10. Disable SELinux or FIPS mode

**Violations may result in:**
- Immediate account suspension
- Security incident investigation
- Termination of employment/contract
- Civil or criminal prosecution

---

## 8. Encryption Key Recovery

**In case of lost/forgotten encryption passphrase:**

1. **LUKS Backup Passphrase:**
   - Secondary passphrase stored in physical safe
   - Accessible only to System Owner and ISSO
   - Used to add new passphrase slot if primary lost

2. **Recovery Procedure:**
   - User contacts ISSO immediately
   - ISSO retrieves backup passphrase from safe
   - Temporary passphrase added to LUKS key slot
   - User sets new primary passphrase
   - Temporary slot removed

3. **If No Recovery Possible:**
   - Data is PERMANENTLY INACCESSIBLE (by design)
   - System restore from backups required
   - Incident documented and reported

---

## 9. Monitoring and Validation

**Monthly Security Checks:**

| Check | Command | Expected Result |
|-------|---------|----------------|
| FIPS mode | `fips-mode-setup --check` | FIPS mode is enabled |
| Encryption status | `lsblk -f` | crypto_LUKS on all partitions |
| Firewall status | `sudo firewall-cmd --state` | running |
| TLS certificate | `openssl s_client -connect localhost:443` | Valid cert, TLS 1.2+ |
| SSH config | `sudo sshd -T \| grep -i password` | PasswordAuthentication no |
| SELinux | `getenforce` | Enforcing |
| Suricata IDS | `sudo systemctl status suricata` | active (running) |

**Annual Security Assessment:**
- Penetration testing (internal or external)
- Firewall rule review and cleanup
- Encryption algorithm review (NIST updates)
- Certificate expiration tracking

---

## 10. Policy Review and Updates

- **Review Frequency:** Annually or upon significant security incidents
- **Update Triggers:**
  - New NIST cryptographic guidance
  - TLS/SSL vulnerabilities (Heartbleed, POODLE, etc.)
  - Firewall breach or attempted intrusion
  - Regulatory requirement changes
  - Technology refresh (VPN implementation, network segmentation)

- **Approval Authority:** System Owner / ISSO

---

## 11. Related Documents

- System Security Plan (SSP) - Section SC (System and Communications Protection)
- Configuration Management Policy (DIWAI-CMP-001)
- Incident Response Policy (DIWAI-IRP-001)
- `DIWAI-EV-SI3-002` — SI-3 Control Substitution (ClamAV decommissioned; YARA stack adopted). Supersedes the earlier ClamAV FIPS risk-acceptance memo (RISK-2026-004)
- NIST SP 800-171 Rev 2
- NIST SP 800-52 Rev 2 (TLS Guidelines)
- NIST SP 800-77 Rev 1 (IPsec VPN Guide)

---

## 12. Definitions

- **Boundary Protection:** Monitoring and control of communications at external boundaries and key internal boundaries
- **Cryptographic Key:** Value used to control cryptographic operations (encryption, authentication)
- **FIPS 140-2:** Federal Information Processing Standard for cryptographic module validation
- **LUKS:** Linux Unified Key Setup - disk encryption specification
- **Session Hijacking:** Exploitation of a valid session to gain unauthorized access
- **Split Tunneling:** Simultaneous connection to secure and unsecure networks (prohibited)
- **TLS:** Transport Layer Security - cryptographic protocol for secure communications

---

## 13. Approval Signatures

**Prepared By:**
Name: [SYSTEM-OWNER], System Administrator
Signature: /s/ [SYSTEM-OWNER]                Date: February 15, 2026

**Reviewed By:**
Name: [SYSTEM-OWNER], Information System Security Officer
Signature: /s/ [SYSTEM-OWNER]                Date: February 15, 2026

**Approved By:**
Name: [SYSTEM-OWNER], System Owner
Signature: /s/ [SYSTEM-OWNER]                Date: February 15, 2026

---

**CLASSIFICATION:** CONTROLLED UNCLASSIFIED INFORMATION (CUI)
**DISTRIBUTION:** Official Use Only - Need to Know Basis
**STATUS:** APPROVED

---

**END OF DOCUMENT**

---
