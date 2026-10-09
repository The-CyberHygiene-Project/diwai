> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Acceptable Use Policy

**Document ID:** DIWAI-AUP-001
**Editorial Correction (2026-08-01):** Document identifier changed from `TCC-AUP-001` to `DIWAI-AUP-001`; internal policy cross-references normalised to the `DIWAI-*` set. Identifier only — **no control content changed** and the version is deliberately not incremented. Aligns this document with the SSP citation set and the [DOMAIN.ORG] independence determination (SSP v2.12 corrected). See `DIWAI-EV-CM-2026-08-01`.
**Addition (2026-10-09):** Section 10.1, use of external systems, added (3.1.20). Section 2.2 password requirements brought to the values in force (length 16, expiration scope, history 6, lockout). No other change.
**Version:** 1.1
**Effective Date:** November 2, 2025
**Review Schedule:** Annually
**Next Review:** November 2, 2026
**Owner:** [SYSTEM-OWNER], ISSO/System Owner
**Distribution:** All SecureMac users (employees and contractors)
**Classification:** Controlled Unclassified Information (CUI)

---


**Version 1.1 (2026-08-04) — technical accuracy correction.** Inherited from
Reference System #1 (CyberInABox) and bulk-edited for [DOMAIN.ORG]. Corrections:

- RS#1 workstations (`LabRat`, `Engineering`, `Accounting`) removed; the actual two-host boundary and the NAS stated, with the Mac mini's concentration of roles noted (SSP §3.2.1).
- **pfSense** replaced with macOS `pf` (perimeter) and `firewalld` (VM); Suricata correctly located on the VM.
- **ClamAV** replaced with the YARA stack (SI-3 since 2026-06-12) and Apple XProtect/MRT/Gatekeeper on the host.
- **Encryption corrected** — the policy claimed LUKS for all systems; the Mac uses **FileVault**, LUKS2 applies to the VM.
- **"Automatic security updates enabled (dnf-automatic)" was inaccurate.** `dnf-automatic` was set **download-only** on 2026-08-01 (`DIWAI-CR-2026-08-01` C3) after an unattended upgrade disabled the SIEM for ~21 hours (POA&M-011). Updates are staged automatically and applied under change control. The policy described the configuration that caused the incident.
- **Password policy cited `CLAUDE.md` as its authority.** That is an assistant instruction file, not a controlled document, and is not part of the compliance artefact set. Replaced with a citation to **`DIWAI-IAP-001`**.
- Screen-lock shortcut corrected for macOS (Ctrl+Cmd+Q); the inherited value was Linux-only.

**Left deliberately unchanged:** references to *windows* in §§ on privacy filters
mean glass windows, not the operating system. **§13 "Solopreneur Applicability"**
already scopes employee and HR references correctly and is retained as written —
it is the pattern the rest of this correction effort adopts.

Raised as **POA&M-058**; no control changed.


## Overview

[DOMAIN.ORG] is committed to protecting the organization, employees, contractors, and clients from illegal or damaging actions by individuals, either knowingly or unknowingly. The SecureMac Reference System #2 and all associated systems, including computer equipment, mobile devices, software, operating systems, storage media, and network accounts are the property of [DOMAIN.ORG]. These systems shall be used for business purposes in serving the interests of the company and our clients, particularly in fulfillment of operational requirements requiring protection of Controlled Unclassified Information (CUI) and Federal Contract Information (FCI).

Effective security is a team effort involving the participation and support of every person who accesses SecureMac systems. It is the responsibility of every user to know these guidelines and to conduct their activities accordingly.

## Purpose

The purpose of this policy is to outline the acceptable use of computer equipment, network resources, and other electronic devices within [DOMAIN.ORG]'s SecureMac Reference System #2. These rules are in place to protect users, the organization, our clients, and the confidentiality, integrity, and availability of CUI and FCI. Inappropriate use exposes [DOMAIN.ORG] to cyber risks including malware attacks (viruses, ransomware), compromise of network systems and services, data breaches, loss of CUI, contract termination, and legal liability under FAR 52.204-21 and DFARS 252.204-7012.

This policy supports compliance with NIST SP 800-171 Rev 2 (AC-1, PS-6, PL-4) and CMMC Level 2 requirements.

## Scope

This policy applies to:

**Systems and Equipment:**
- Mac mini host: `securemac.[DOMAIN.ORG]` ([LAN-IP-REDACTED]) — perimeter firewall, hypervisor, Nextcloud CUI store, AI stack, and sole management workstation
- Directory / service VM: `services.[DOMAIN.ORG]` ([LAN-IP-REDACTED]) — 389-DS, Wazuh, mail, Nextcloud database
- Workstations: none presently deployed; where a deployment adds them, they are in scope (see §13)
- Network infrastructure: macOS `pf` (perimeter, on the Mac mini), `firewalld` (VM), switches
- File shares (NAS shares on nas.[DOMAIN.ORG])
- All information, electronic devices, and network resources used to conduct [DOMAIN.ORG] business

**Personnel:**
- Owner/Principal ([SYSTEM-OWNER])
- All employees
- Contractors and consultants with SecureMac access
- Temporary workers
- Third parties accessing SecureMac resources

**Information:**
- All data on SecureMac systems (CUI, FCI, proprietary business information)
- Email, documents, databases, backups
- System configurations and credentials

This policy applies to all equipment and accounts, whether owned or leased by [DOMAIN.ORG], owned by employees or contractors, or provided by third parties.

## Policy

### 1. General Use and Ownership

#### 1.1 Information Ownership
[DOMAIN.ORG] proprietary information and Government FCI/CUI stored on electronic and computing devices, whether owned or leased by [DOMAIN.ORG] or by individuals, remains the sole property of [DOMAIN.ORG]. Users must ensure through technical and procedural means that proprietary information and CUI/FCI are protected in accordance with this policy and all referenced security policies.

#### 1.2 Reporting Requirements
Users have a responsibility to promptly report (within 1 hour of discovery):
- Theft, loss, or unauthorized disclosure of [DOMAIN.ORG] proprietary information or CUI/FCI
- Security incidents or suspected incidents
- Malware infections or suspected infections
- System malfunctions that could affect CUI protection
- Physical security breaches
- Policy violations observed

**Reporting Contact:**
- ISSO: [SYSTEM-OWNER]
- Email: [EMAIL-REDACTED]
- Phone: [REDACTED-PHONE]

#### 1.3 Access Authorization
Users may access, use, or share [DOMAIN.ORG] proprietary information or CUI/FCI only to the extent it is authorized and necessary to fulfill assigned job duties. Access is granted based on least privilege principles and documented business need.

#### 1.4 Personal Use
Limited personal use of SecureMac systems is permitted provided it:
- Does not interfere with business operations
- Does not violate any provision of this policy
- Does not involve storage of personal CUI or sensitive personal information
- Does not consume excessive system resources
- Occurs during non-business hours when possible

**Examples of Acceptable Personal Use:**
- Checking personal email during breaks (not on SecureMac email system)
- Brief personal research or online shopping during lunch
- Personal financial management (not on SecureMac systems processing CUI)

**Examples of Unacceptable Personal Use:**
- Personal business activities or operating a business
- Excessive use that impacts work productivity
- Any activity listed in Section 3 (Unacceptable Use)

#### 1.5 Monitoring
For security, incident response, and network maintenance purposes, authorized individuals (ISSO, system administrators) may monitor equipment, systems, network traffic, and user activities at any time. Monitoring includes but is not limited to:
- Audit log review (auditd, rsyslog)
- Network traffic analysis (Suricata IDS on the service VM)
- Security information and event management (Wazuh SIEM)
- File integrity monitoring (Wazuh FIM)
- Authentication logging (389-DS LDAP)
- File access logging (NAS VFS audit module)

**Users have no expectation of privacy** when using SecureMac systems. All activities may be logged, monitored, and reviewed.

#### 1.6 Compliance Audits
[DOMAIN.ORG] reserves the right to audit networks, systems, and user activities on a periodic basis or in response to security incidents to ensure compliance with this policy and all security policies. Audits may include:
- Quarterly access reviews
- Annual security assessments
- Incident-driven forensic investigations
- Compliance verification scans (OpenSCAP)
- Contractor activity reviews

### 2. Security and CUI/FCI Protection

#### 2.1 Device Security
All computing devices that connect to SecureMac must comply with:
- FIPS 140-2 mode enabled (all systems)
- Full-disk encryption on all systems processing or storing CUI: **FileVault** (Mac host), **LUKS2** (service VM)
- SELinux enforcing mode
- Wazuh agent installed and operational
- `dnf-automatic` configured **download-only** on the VM (`apply_updates = no`, `DIWAI-CR-2026-08-01` C3) — updates are staged automatically and applied under change control, not unattended
- Malicious-code protection operating: **YARA** with Wazuh active response and a weekly full scan (VM); **XProtect/MRT/Gatekeeper** (Mac host)

#### 2.2 Password Requirements
System-level and user-level passwords must comply with the 389-DS directory password policy, as specified in **`DIWAI-IAP-001`** (Identification and Authentication Policy):
- Minimum 16 characters
- At least 3 character classes (uppercase, lowercase, numbers, special characters)
- Expiration: 90 days for interactive user accounts; service, break-glass and reserved accounts are exempt (see `DIWAI-IAP-001`, section 3.3)
- Password history: the last 6 passwords cannot be reused
- Lockout: 3 failed attempts lock a VM account for 15 minutes (5 consecutive failures on the Mac host); see `DIWAI-IAP-001`

**Password Protection:**
- Passwords must never be shared with others
- Passwords must never be written down or stored in plaintext
- Passwords must not be stored in browser password managers (use password manager software if needed: KeePassXC recommended)
- Providing access to another individual, either deliberately or through failure to secure your account, is strictly prohibited
- Family and household members must never use your SecureMac credentials or systems

#### 2.3 Screen Lock
All computing devices must be secured with a password-protected lock screen:
- Automatic activation set to 15 minutes or less
- Users must manually lock screens when leaving workspace: `Ctrl+Alt+L` on Linux
- Users must fully log off when finished working for the day
- Screens visible from windows must use privacy filters

#### 2.4 Email and External Communication
- SecureMac email system (when deployed) for business use only
- External email from personal accounts discussing CUI must use encryption
- Postings from a [ORGANIZATION] email address to public forums must include disclaimer: "Opinions expressed are my own and not necessarily those of [DOMAIN.ORG]"
- Email signature should not reveal sensitive business information

#### 2.5 Email Security
Users must exercise extreme caution with email:
- Do not open email attachments from unknown senders
- Do not click links in unsolicited emails (phishing)
- Verify sender identity before opening attachments, even from known senders
- Report suspicious emails to ISSO immediately
- Do not respond to requests for passwords or credentials
- Mark CUI emails with "CUI" in subject line

#### 2.6 CUI Marking and Handling
Users must properly mark and handle CUI per 32 CFR Part 2002:
- Mark documents with "CUI" header and footer
- Include CUI in email subject lines when applicable
- Store CUI only on encrypted SecureMac systems
- Do not send CUI via unencrypted channels
- Do not store CUI on personal devices, cloud services, or unencrypted media
- Refer to CUI marking guide for detailed requirements

### 3. Unacceptable Use

The following activities are prohibited. Users may NOT be exempted from these restrictions except as explicitly documented and approved by Owner/Principal for legitimate business purposes.

**Under no circumstances is any user authorized to engage in any activity that is illegal under local, state, federal, or international law while utilizing [DOMAIN.ORG]-owned resources.**

The lists below provide a framework for activities which constitute unacceptable use.

#### 3.1 System and Network Activities (Strictly Prohibited)

The following activities are **strictly prohibited** with **no exceptions**:

1. **Intellectual Property Violations:** Violations of the rights of any person or company protected by copyright, trade secret, patent, or other intellectual property, including installation or distribution of "pirated" or unlicensed software

2. **Unauthorized Copying:** Unauthorized copying of copyrighted material including digitization and distribution of photographs, music, videos, books, or software for which [DOMAIN.ORG] or the user does not have an active license

3. **Unauthorized Access:** Accessing data, a server, or an account for any purpose other than conducting authorized business, even if you have authorized access to the system

4. **Export Control Violations:** Exporting software, technical information, encryption software, or technology in violation of international or regional export control laws

5. **Malware Introduction:** Introduction of malicious programs into the network or systems (viruses, worms, trojans, ransomware, spyware, keyloggers, etc.)

6. **Password Sharing:** Revealing your account password to others or allowing use of your account by others, including family and household members

7. **Harassment:** Using SecureMac systems to actively engage in procuring or transmitting material that violates sexual harassment or hostile workplace laws

8. **Fraudulent Offers:** Making fraudulent offers of products, items, or services originating from any [ORGANIZATION] account

9. **Unauthorized Data Collection:** Effecting security breaches or disruptions of network communication, including but not limited to:
   - Port scanning
   - Ping floods, SYN floods, or other denial-of-service attacks
   - Packet spoofing
   - Sniffing network traffic without authorization
   - ARP poisoning

10. **Circumventing Security:** Circumventing user authentication or security of any host, network, or account ("cracking" or "hacking")

11. **Network Interference:** Interfering with or denying service to any user (except as authorized for security purposes by ISSO)

12. **Unauthorized Software:** Installing or using any software not approved by ISSO, including but not limited to:
    - Peer-to-peer file sharing applications
    - Remote access tools not authorized
    - Cryptocurrency mining software
    - Hacking tools (unless authorized for security testing)
    - Software from untrusted sources

#### 3.2 Email and Communication Activities (Strictly Prohibited)

1. **Spam:** Sending unsolicited email messages ("spam"), including advertising material to individuals who did not specifically request such material

2. **Email Harassment:** Sending annoying or harassing email, including harassment based on sex, race, religion, national origin, disability, or age

3. **Forged Email:** Forging or attempting to forge email header information

4. **Solicitation:** Soliciting for personal gain or non-business purposes

5. **Chain Letters:** Sending or forwarding chain letters or pyramid schemes

6. **Phishing:** Creating or forwarding phishing emails or participating in social engineering attacks

#### 3.3 Blogging and Social Media

1. **Unauthorized Disclosure:** Blogging or posting on social media about CUI, FCI, contract-specific information, or proprietary business information

2. **Impersonation:** Employees and contractors are prohibited from posting to blogging or social media sites using [DOMAIN.ORG] name without explicit authorization

3. **Company Representation:** Representing yourself as speaking for [DOMAIN.ORG] without authorization

4. **Client Information:** Discussing clients, contracts, or business relationships on social media without authorization

### 4. Acceptable Personal Use

The following personal activities are acceptable provided they comply with Section 1.4 (limited, non-interfering personal use):

1. **Checking Personal Email:** During breaks or non-business hours (not using SecureMac email system)

2. **Brief Personal Research:** Online shopping, news reading, personal finance (during breaks)

3. **Personal Education:** Professional development, online courses related to job skills

4. **Emergency Personal Business:** Handling personal emergencies (doctor appointments, family emergencies)

**Not Acceptable Even as Personal Use:**
- Storing personal CUI or sensitive personal information on SecureMac
- Operating a personal business
- Excessive gaming
- Streaming entertainment content (bandwidth consumption)
- Any activity listed in Section 3 (Unacceptable Use)

### 5. Removable Media and Data Transfer

#### 5.1 USB Drives and Removable Media

**Correction 2026-09-15 (`DIWAI-CR-2026-09-09` C128, finding F-2026-09-02).** The
prior wording required "encrypted (LUKS)" drives. LUKS is Linux-specific and
**cannot be satisfied by a Mac-attached APFS volume**, so the clause was unmeetable
on the host that holds the CUI repository. It also drew no distinction between
portable media and fixed attached storage, which on Apple Silicon is unavoidable.

- Portable USB drives used for CUI must be **authorized and encrypted with
  platform-appropriate full-disk encryption** — **LUKS** on Linux, **FileVault /
  APFS encryption** on macOS
- **Fixed attached storage is not portable media.** On Apple Silicon, capacity
  beyond the internal SSD is *necessarily* Thunderbolt- or USB-attached. Such
  volumes report `Removable Media: Fixed`, remain inside the locked rack cabinet,
  carry drive marking, and must be **full-disk encrypted**. They are inventoried in
  the SBOM and in SSP §2.5, and the transport and custody requirements for portable
  media (3.8.5, 3.8.6) do not apply to them
- USB drives must be scanned for malware before connecting to SecureMac
- Personal USB drives must not be used for CUI
- **USBGuard enforces a UUID allowlist** for connected devices
  (`CUI_USBGuard_Configuration_Evidence.md`, enforced 2026-06-12) — previously
  recorded here as a "future enhancement", corrected 2026-09-15

#### 5.2 Cloud Storage
- **Prohibited:** CUI must never be stored in commercial cloud services (Dropbox, Google Drive, OneDrive, iCloud, etc.)
- Personal cloud services may be used for personal data only, on personal devices only
- Government-approved cloud services (e.g., approved FedRAMP providers) may be used only with explicit authorization for specific contracts

#### 5.3 Mobile Devices
- Personal mobile devices (smartphones, tablets) may not access SecureMac systems (until mobile device management implemented)
- CUI must not be stored on mobile devices
- Do not photograph or screenshot CUI on mobile devices
- Mobile devices must not be used to photograph SecureMac systems or configurations

### 6. Software Installation

#### 6.1 Authorized Software
- Only software approved by ISSO may be installed
- Software must be obtained from trusted repositories (Rocky Linux BaseOS/AppStream)
- All software installations logged via dnf logging
- Software license compliance is mandatory

#### 6.2 Prohibited Software
- Unlicensed or pirated software
- Peer-to-peer file sharing (BitTorrent, etc.)
- Remote access tools not approved (TeamViewer, etc. - unless authorized)
- Cryptocurrency mining software
- Hacking or penetration testing tools (unless authorized for security assessment)
- Software from untrusted sources

#### 6.3 Software Request Process
To request software installation:
1. Submit request to ISSO with business justification
2. ISSO assesses security implications
3. ISSO verifies licensing compliance
4. If approved, ISSO installs software
5. Software added to approved baseline

### 7. Physical Security Responsibilities

Users must:
- Lock the screen when leaving the workspace — macOS: **Ctrl+Cmd+Q**; Linux console: **Ctrl+Alt+L**
- Log off at end of workday
- Never leave systems logged in and unattended
- Protect printouts containing CUI (retrieve immediately, shred when done)
- Report lost or stolen equipment immediately
- Not allow unauthorized individuals to view CUI on screens
- Use privacy filters on screens visible from windows or public areas

### 8. Incident Reporting

Users must report the following incidents immediately (within 1 hour):

1. **Security Incidents:**
   - Suspected malware infection
   - Suspected unauthorized access
   - Unusual system behavior
   - Missing or stolen equipment
   - CUI data breach or suspected breach

2. **Policy Violations:**
   - Observed violations of this policy by others
   - Requests to violate security policies
   - Suspicious activity by other users

3. **System Issues:**
   - Wazuh agent not running
   - Anti-malware not updating
   - FIPS mode disabled
   - Encryption errors

**Reporting Procedure:**
- Email: [EMAIL-REDACTED]
- Phone: [REDACTED-PHONE]
- Document what you observed, when, and any evidence
- Do not investigate security incidents yourself (unless you are the ISSO)
- Preserve evidence (don't delete logs, don't reboot unless directed)

### 9. Remote Access

**Current Status:** Remote access not currently configured

**Future Remote Access Requirements (when implemented):**
- VPN required for all remote connections
- Multi-factor authentication (MFA) required
- No storage of CUI on remote devices
- Remote devices must meet same security requirements as SecureMac systems
- Remote access sessions monitored and logged

### 10. Bring Your Own Device (BYOD)

**Current Policy:** BYOD not permitted for SecureMac access

**Personal Devices:**
- Personal laptops, tablets, and smartphones may not connect to SecureMac
- Personal devices may not process or store CUI
- Personal devices may not access NAS file shares (nas.[DOMAIN.ORG])
- Future BYOD program may be developed with mobile device management (MDM)

#### 10.1 Use of External Systems (AC-20, 3.1.20)

**External systems.** An external system is any system not owned, operated and administered by the organization, including personal computers, phones, tablets, and cloud or hosted services outside the system boundary.

1. **Prohibited unless authorized.** Use of an external system to access, process, store or transmit CUI is prohibited unless the Owner has specifically authorized that system in writing.
2. **Requirements before authorization.** Before authorizing an external system, the Owner confirms that: (a) the system encrypts data in transit and at rest with FIPS-validated cryptography; (b) access requires multi-factor authentication; (c) the system receives security updates from its publisher; (d) CUI is not retained on it after the session unless the authorization states otherwise; and (e) the host organization's terms do not conflict with the contract's CUI requirements.
3. **Verification.** The Owner records the verification of items (a) to (e), or the provider's published attestation, in the authorization record before use. Authorization is reviewed annually and whenever the provider's terms change.
4. **Agreements.** For each authorized external system, the Owner keeps the signed connection or processing agreement, or the provider's terms of service in force at the time of authorization, in the compliance evidence folder.
5. **Current state.** No external system is currently authorized to access, process or store CUI. Email is self-hosted inside the system boundary (Dovecot and Roundcube) with encryption and safeguards, so it is not an external system. The control-health and security alert messages sent to an external mail account carry system status only and contain no CUI.

### 11. Training and Awareness

All users must:
- Complete annual security awareness training
- Acknowledge receipt and understanding of this policy (annually)
- Stay informed of policy updates
- Complete role-specific training (e.g., CUI marking for proposal developers)

### 12. Compliance and Enforcement

#### 12.1 Policy Violations
Violations of this policy may result in:
- Verbal or written warning
- Temporary suspension of access
- Permanent revocation of access
- Termination of employment or contract
- Legal action (civil or criminal)
- Reporting to law enforcement or government agencies

#### 12.2 Contractor-Specific Enforcement
Contractors who violate this policy may have:
- 389-DS LDAP account disabled immediately
- Contract terminated for cause
- Company barred from future [ORGANIZATION] engagements
- Government contracting officer notified (if contract-related violation)

#### 12.3 Sanctions Process
Follows Personnel Security Policy (DIWAI-PS-001), Section PS-8:
- Minor violations: Counseling, remedial training
- Moderate violations: Written warning, access suspension
- Major violations: Termination, legal action
- Criminal violations: Law enforcement referral, DoD reporting

### 13. Solopreneur Applicability

As a single-person business with occasional contractors, certain provisions of this policy are modified:

- References to "employees" refer to Owner/Principal or authorized contractors
- No HR department exists; Owner self-enforces policy and makes all decisions
- No supervisor escalation needed for policy questions (Owner is final authority)
- Owner serves as both user and system administrator

**Owner Responsibilities:**
- Lead by example in policy compliance
- Enforce policy for all contractors
- Document all policy violations and enforcement actions
- Review and update policy annually

### 14. Policy Acknowledgment

All users must sign an acknowledgment form indicating they have read, understood, and agree to comply with this policy.

**Acknowledgment Form:**

---

**[DOMAIN.ORG] Acceptable Use Policy Acknowledgment**

I, _________________________ (print name), acknowledge that I have received, read, and understood [DOMAIN.ORG] Acceptable Use Policy (DIWAI-AUP-001). I understand that:

- SecureMac systems are for authorized business use
- All activity on SecureMac systems may be monitored and logged
- I have no expectation of privacy when using SecureMac systems
- I must protect CUI and FCI in accordance with this policy
- I must report security incidents and policy violations immediately
- Violations of this policy may result in access revocation, termination, and legal action

I agree to comply with all provisions of this policy and all referenced security policies.

Signature: _______________________________ Date: _______________

389-DS LDAP Username: _______________________________

Role: [ ] Employee [ ] Contractor [ ] Consultant

---

**For Official Use:**
- Acknowledgment received by: _______________________
- Date filed: _______________________
- 389-DS LDAP account: _______________________
- Access granted date: _______________________

## References

- NIST SP 800-171 Rev 2 (AC-1, PS-6, PL-4)
- FAR 52.204-21 (Basic Safeguarding of Covered Contractor Information Systems)
- DFARS 252.204-7012 (Safeguarding Covered Defense Information)
- 32 CFR Part 2002 (Controlled Unclassified Information)
- System Security Plan (SSP)
- Personnel Security Policy (DIWAI-PS-001)
- Incident Response Policy (DIWAI-IRP-001)
- Physical and Media Protection Policy (DIWAI-PE-MP-001)
- 389-DS directory password policy — see `DIWAI-IAP-001` (Identification and Authentication Policy)

---

## Appendix A: Quick Reference - Do's and Don'ts

### DO:
✓ Lock your screen when leaving your workspace (Ctrl+Alt+L)
✓ Use strong, unique passwords
✓ Report security incidents immediately
✓ Mark CUI documents properly ("CUI" header/footer)
✓ Verify email sender before opening attachments
✓ Store CUI only on encrypted SecureMac systems
✓ Complete security training annually
✓ Ask ISSO if you're unsure about policy

### DON'T:
✗ Share your password with anyone
✗ Store CUI on personal devices or cloud storage
✗ Click links in suspicious emails
✗ Install unauthorized software
✗ Leave systems logged in and unattended
✗ Use personal USB drives for CUI
✗ Discuss CUI on social media
✗ Ignore security warnings or bypass security controls

---

## Appendix B: Reporting Template

**Security Incident Report**

**Your Information:**
- Name: _______________________
- Date/Time of Incident: _______________________
- Date/Time Reported: _______________________

**Incident Details:**
- Type of Incident: [ ] Malware [ ] Unauthorized Access [ ] Lost/Stolen Equipment [ ] Policy Violation [ ] Other: _______
- Affected System(s): _______________________
- Description of Incident: _______________________
- CUI Potentially Affected? [ ] Yes [ ] No [ ] Unknown
- Evidence Preserved? [ ] Yes [ ] No

**Actions Taken:**
- Immediate actions you took: _______________________
- Who else was notified: _______________________

**Submit to:** [EMAIL-REDACTED] or call [REDACTED-PHONE]

---

## Approval

**Prepared By:**
[SYSTEM-OWNER], ISSO

**Approved By:**
/s/ [SYSTEM-OWNER]
Owner/Principal, [DOMAIN.ORG]

**Date:** November 2, 2025

**Next Review Date:** November 2, 2026

---

## Document Control

**Revision History:**
- Version 1.0 - November 2, 2025 - Initial policy establishment
- Version 1.1 correction - September 15, 2026 - §5.1 rewritten (`DIWAI-CR-2026-09-09` C128): platform-appropriate full-disk encryption replaces the LUKS-only requirement, which was unmeetable on macOS; fixed rack-resident attached storage distinguished from portable media; USBGuard recorded as **enforced** rather than a future enhancement. Raised by F-2026-09-02, an unencrypted attached SSD holding CUI and private keys, encrypted the same day

**Distribution:**
- All SecureMac users
- Signed acknowledgment required before account activation
- Filed in: `/backup/personnel-security/policies/`

---
