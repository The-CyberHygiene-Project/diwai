> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Configuration Management Policy

**Document ID:** DIWAI-CMP-001
**Editorial Correction (2026-08-01):** Document identifier changed from `TCC-CMP-001` to `DIWAI-CMP-001`; internal policy cross-references normalised to the `DIWAI-*` set. Identifier only — **no control content changed** and the version is deliberately not incremented. Aligns this document with the SSP citation set and the [DOMAIN.ORG] independence determination (SSP v2.12 corrected). See `DIWAI-EV-CM-2026-08-01`.
**Technical Correction (2026-10-09):** the password policy line in the baseline table (section 3.5) corrected to the values in force: minimum length 16 and a 90-day expiry for interactive user accounts, with service, break-glass and reserved accounts exempt (`DIWAI-IAP-001`, `DIWAI-CR-2026-10-11`). No other change.
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

**The system inventory — the core artefact of a configuration management policy —
described the wrong machines running the wrong operating systems:**

- `services.[DOMAIN.ORG]` was listed **twice**, once as a Rocky Linux server and once as a **macOS Sequoia** "AI/ML Server". The AI host is the **Mac mini** (`ai.[DOMAIN.ORG]` / `securemac.[DOMAIN.ORG]`), and it runs **macOS Tahoe 26**, not Sequoia.
- The **Mac mini was listed as a workstation running Rocky Linux 9.7**, alongside fictional hosts `ws1` and `ws2`.
- A **pfSense appliance** appeared as network infrastructure; none exists.
- No entry recorded that `services.[DOMAIN.ORG]` is a **virtual machine on the Mac mini** rather than separate hardware — material to a hardware inventory.

**Baseline standards corrected.** The policy cited the **CIS Apple macOS
Benchmark** for the Mac. The baseline actually in use is the **macOS Security
Compliance Project (mSCP)**, local profile `diwai_phase1`, NIST 800-171 aligned —
the one the weekly scan evaluates and the SSP reports against. The **pfSense DISA
STIG** line is replaced by treating the `pf` ruleset and `firewalld` configuration
as configuration items under change control, which is what they are.

Also corrected: **ClamAV** replaced with the YARA stack in the software inventory
(SI-3 since 2026-06-12); workstation provisions retained and scoped.

Raised as **POA&M-058**; no control changed.


## 1. Purpose

This policy establishes [DOMAIN.ORG]'s requirements for configuration management on the SecureMac Reference System #2. It ensures systems are configured securely, changes are controlled, and baseline configurations are maintained to protect Controlled Unclassified Information (CUI) in compliance with NIST SP 800-171 Rev 2 (CM-1 through CM-11) and CMMC Level 2.

---

## 2. Scope

This policy applies to:

- **All SecureMac Systems:**
  - `securemac.[DOMAIN.ORG]` / `ai.[DOMAIN.ORG]` (**macOS Tahoe 26**) — Mac mini M4 Pro: perimeter firewall (`pf`), hypervisor, Nextcloud CUI store, AI inference, sole management workstation
  - `services.[DOMAIN.ORG]` (**Rocky Linux 9.7/9.8 aarch64**, FIPS mode) — UTM virtual machine on the Mac mini: 389-DS, Wazuh, mail, Nextcloud database
  - `nas.[DOMAIN.ORG]` (**Synology DSM**) — NAS: backups and file shares
  - Workstations: none presently deployed; in scope where a deployment adds them
  - Network: `pf` on the Mac mini (perimeter), `firewalld` on the VM — **software firewalls; no appliance**

- **Configuration Items:** Operating systems, applications, firmware, network devices, security tools, baseline configurations

- **All Personnel:** Employees, contractors, and subcontractors with system administration privileges

---

## 3. Policy Statements

### 3.1 Baseline Configurations (CM-2, CM-6)

**The organization shall:**

1. **Establish Security Baselines (CM-2):**
   - Maintain documented baseline configurations for each system type
   - Baselines based on industry standards:
     - **Rocky Linux (VM):** NIST 800-171 CUI profile, evaluated with OpenSCAP/SSG against a tailored profile
     - **macOS (Mac mini):** **macOS Security Compliance Project (mSCP)** — local baseline `diwai_phase1`, NIST 800-171 aligned. *(The inherited reference to the CIS Apple macOS Benchmark did not describe the baseline actually in use.)*
     - **Firewall rulesets:** `/etc/pf_diwai.conf` (Mac) and `firewalld` zones/rich rules (VM) are configuration items under change control; there is no appliance to which a DISA STIG applies
   - Document deviations from baseline with security justification

2. **Configuration Settings (CM-6):**
   - FIPS 140-2 cryptographic mode enabled (Rocky Linux systems)
   - SELinux enforcing mode (Rocky Linux systems)
   - FileVault/LUKS full-disk encryption enabled
   - Automatic updates disabled (manual control for stability)
   - Unnecessary services disabled (principle of least functionality)

3. **Baseline Documentation Location:**
   - `/Documentation/Baselines/` on services.[DOMAIN.ORG]
   - Version-controlled configuration files in Git repository
   - Software Bill of Materials (SBOM) maintained quarterly

### 3.2 Configuration Change Control (CM-3)

**Change Management Process:**

1. **Change Request Requirements:**
   - All configuration changes require documented justification
   - Changes classified by risk level:
     - **Low:** Application updates, user account changes
     - **Medium:** Service configuration changes, new software installation
     - **High:** Operating system upgrades, security control modifications

2. **Change Approval:**
   - **Low risk:** System Administrator approval
   - **Medium risk:** ISSO review and approval
   - **High risk:** System Owner approval + testing in non-production environment

3. **Change Testing:**
   - **High-risk changes:** Tested on non-production system first
   - **Medium-risk changes:** Tested during off-peak hours with rollback plan
   - **Emergency changes:** Document post-implementation

4. **Change Documentation:**
   - Change records maintained in the CUI repository under `Compliance/Change_Records/`
   - Include: Date, change description, approver, outcome, rollback procedure
   - POA&M updated if change addresses security finding

5. **Prohibited Changes:**
   - Disabling FIPS mode
   - Disabling SELinux
   - Disabling audit logging
   - Removing encryption
   - Opening unnecessary firewall ports
   - Installing unauthorized software

### 3.3 Security Impact Analysis (CM-4)

**Before implementing changes, analyze:**

1. Impact on security controls (weakening vs. strengthening)
2. Effect on CUI confidentiality, integrity, availability
3. Compatibility with FIPS 140-2 and NIST 800-171 requirements
4. Potential for introducing vulnerabilities
5. Dependencies on other system components

**High-impact changes require:**
- Written security impact analysis
- ISSO approval
- Post-implementation validation

### 3.4 Access Restrictions for Change (CM-5)

**Physical Access Controls:**
- Server room locked (physical key required)
- Access log maintained
- Authorized personnel only

**Logical Access Controls:**
- Administrative access requires:
  - Unique user account (no shared accounts)
  - Kerberos authentication via 389-DS LDAP
  - sudo elevation for privileged commands (logged via auditd)
- Root account disabled for remote login
- Multi-factor authentication required for contractors (POA&M-SPRS-1)

**Change Implementation Windows:**
- Planned changes: Tuesday/Thursday 1800-2000 MST
- Emergency changes: Any time with immediate documentation

### 3.5 Configuration Settings (CM-6)

**Mandatory Security Settings:**

| Configuration Item | Required Setting | Verification |
|--------------------|------------------|--------------|
| FIPS Mode | Enabled (Rocky Linux) | `fips-mode-setup --check` |
| SELinux | Enforcing | `getenforce` |
| Encryption | LUKS AES-256 / FileVault | `lsblk`, `fdesetup status` |
| Firewall | Enabled, default-deny | `firewall-cmd --state` |
| Auditd | Running, CUI profile | `systemctl status auditd` |
| SSH | Key-based only, no root login | `/etc/ssh/sshd_config` |
| Password Policy | 16-char min; 90-day expiry for interactive accounts | 389-DS LDAP policy; Mac `pwpolicy` |
| Session Lock | 15-minute timeout | `gsettings` or screen saver |

### 3.6 Least Functionality (CM-7)

**The organization shall:**

1. **Disable Unnecessary Services:**
   - Remove development tools from production systems
   - Disable unused network services (telnet, FTP, etc.)
   - Remove or disable unnecessary software packages

2. **Principle of Least Functionality:**
   - Systems configured for specific mission functions only
   - No personal use software on production systems
   - Web browsing prohibited on servers (air-gapped)

3. **Prohibited Software:**
   - Peer-to-peer file sharing applications
   - Unauthorized remote access tools
   - Unapproved encryption software
   - Games or entertainment software

### 3.7 Component Inventory (CM-8)

**The organization shall maintain:**

1. **System Inventory:**
   - Hardware inventory (hosts, workstations where deployed, network devices). Note that `services.[DOMAIN.ORG]` is a **virtual machine** on the Mac mini and has no separate hardware entry
   - Location, serial numbers, acquisition dates
   - Assignment (user/function)
   - Update quarterly

2. **Software Inventory (SBOM):**
   - Operating systems and versions
   - Installed applications and patch levels
   - Security software (Wazuh, YARA, Suricata, fapolicyd, usbguard)
   - Update quarterly or upon major changes
   - Location: `Evidence/Software_Inventory/`

3. **Automated Inventory Tools:**
   - `rpm -qa` (Rocky Linux package inventory)
   - `brew list` (macOS Homebrew packages)
   - Wazuh agent inventory module

### 3.8 Configuration Management Plan (CM-9)

**The organization shall:**

1. Maintain this Configuration Management Policy as the CM Plan
2. Include baseline configurations in System Security Plan (SSP)
3. Track configuration items in version control (Git where applicable)
4. Review CM Plan annually or upon significant infrastructure changes

### 3.9 Software Usage Restrictions (CM-10)

**Requirements:**

1. **Licensed Software Only:**
   - All software properly licensed
   - License tracking spreadsheet maintained
   - Annual license compliance review

2. **Open Source Software:**
   - Only from trusted repositories (RHEL/Rocky official repos)
   - Security vulnerabilities monitored
   - Approval required for non-standard packages

3. **Software Installation:**
   - Installed from official repositories only
   - Package signatures verified
   - Custom/third-party software requires ISSO approval

### 3.10 User-Installed Software (CM-11)

**Restrictions:**

1. **Production Systems:**
   - Users prohibited from installing software
   - sudo access limited to System Administrator
   - Change management process required for all installations

2. **Workstations** *(where a deployment includes them; none presently)*:
   - Standard software suite pre-installed
   - Additional software requests submitted via change management
   - ISSO reviews security implications

3. **Monitoring:**
   - File integrity monitoring (Wazuh FIM) detects unauthorized installations
   - Package installation events logged via auditd
   - Monthly review of installed software inventory

---

## 4. Roles and Responsibilities

### 4.1 System Owner

- Approve high-risk configuration changes
- Ensure adequate resources for configuration management
- Review and approve CM Policy annually

### 4.2 Information System Security Officer (ISSO)

- Define security baseline configurations
- Review medium and high-risk change requests
- Conduct security impact analysis for changes
- Validate compliance with configuration requirements
- Maintain configuration management documentation

### 4.3 System Administrator

- Implement and maintain baseline configurations
- Execute approved configuration changes
- Document all configuration modifications
- Monitor for unauthorized changes
- Generate quarterly software inventory reports
- Respond to configuration drift alerts

### 4.4 All Users

- Do not attempt to modify system configurations
- Request software installations through proper channels
- Report suspected unauthorized changes
- Comply with software usage restrictions

---

## 5. Implementation Details

### 5.1 Baseline Configuration Files

**Rocky Linux Systems:**
```
/etc/fips-mode-setup.conf          # FIPS mode configuration
/etc/selinux/config                # SELinux configuration
/etc/ssh/sshd_config               # SSH hardening
/etc/audit/audit.rules             # Audit configuration (CUI profile)
/etc/firewalld/                    # Firewall rules
```

**macOS System (services.[DOMAIN.ORG]):**
```
/etc/pf.conf                       # Packet filter firewall
~/Library/Preferences/             # Security preferences
/System/Library/LaunchDaemons/     # System services
```

**Version Control:**
- Configuration files backed up to `/backup/configs/`
- Git repository for tracking changes (where applicable)
- Daily differential backups

### 5.2 Configuration Compliance Verification

**Monthly Compliance Checks:**

1. **OpenSCAP Scans:**
   ```bash
   oscap xccdf eval --profile cui \
     --results-arf /root/oscap-$(date +%Y%m%d).xml \
     /usr/share/xml/scap/ssg/content/ssg-rl9-ds.xml
   ```

2. **Manual Verification:**
   - FIPS mode status
   - SELinux mode
   - Critical service status
   - Firewall rules review
   - User account audit

3. **Configuration Drift Detection:**
   - Wazuh FIM monitors system files
   - Alerts on unauthorized changes to:
     - `/etc/` (configuration files)
     - `/usr/bin/`, `/usr/sbin/` (binaries)
     - `/boot/` (kernel and boot files)

### 5.3 Change Management Log Format

**Required Fields:**
```
Date: YYYY-MM-DD HH:MM:SS
Change ID: CM-YYYY-NNN
System(s): <hostname(s)>
Risk Level: Low / Medium / High
Description: <detailed change description>
Justification: <business or security need>
Approved By: <name and role>
Implemented By: <name>
Testing Performed: <test description and results>
Rollback Procedure: <steps to reverse change>
Outcome: Success / Failed / Rolled Back
Post-Implementation Validation: <verification results>
```

**Log Location:** CUI repository, `Compliance/Change_Records/` (one record per engagement; see `DIWAI-CR-2026-08-01`)

---

## 6. Compliance Mapping

| NIST SP 800-171 Control | Implementation |
|-------------------------|----------------|
| **CM-1** Policy and Procedures | This document |
| **CM-2** Baseline Configuration | Section 3.1 |
| **CM-3** Configuration Change Control | Section 3.2 |
| **CM-4** Security Impact Analysis | Section 3.3 |
| **CM-5** Access Restrictions for Change | Section 3.4 |
| **CM-6** Configuration Settings | Section 3.5 |
| **CM-7** Least Functionality | Section 3.6 |
| **CM-8** Information System Component Inventory | Section 3.7 |
| **CM-9** Configuration Management Plan | Section 3.8 |
| **CM-10** Software Usage Restrictions | Section 3.9 |
| **CM-11** User-Installed Software | Section 3.10 |

---

## 7. Enforcement and Penalties

Violations of this policy may result in:

1. Immediate reversal of unauthorized changes
2. Suspension of administrative access
3. Written reprimand
4. Termination of employment or contract
5. Civil or criminal prosecution (for malicious changes)

All violations shall be investigated as potential security incidents.

---

## 8. Policy Review and Updates

- **Review Frequency:** Annually or upon significant infrastructure changes
- **Update Triggers:**
  - New NIST guidance or regulatory requirements
  - Security incidents revealing configuration weaknesses
  - Technology refresh or major system upgrades
  - Audit findings

- **Approval Authority:** System Owner / ISSO

---

## 9. Related Documents

- System Security Plan (SSP) - Section CM (Configuration Management)
- Software Bill of Materials (SBOM) v2.0
- Baseline Configuration Documentation
- Change Management Log
- NIST SP 800-171 Rev 2
- NIST SP 800-53 Rev 5 (CM family)
- CIS Benchmarks (Rocky Linux 9, macOS)

---

## 10. Definitions

- **Baseline Configuration:** Documented set of specifications for a system approved as the secure starting point
- **Configuration Item:** Hardware, software, or documentation item under configuration management
- **Configuration Management:** Process of establishing and maintaining consistency of system performance and attributes
- **Security Impact Analysis:** Assessment of potential security effects from proposed system changes
- **SBOM:** Software Bill of Materials - comprehensive inventory of software components

---

## 11. Approval Signatures

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
