> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Identification and Authentication Policy

**Document ID:** DIWAI-IAP-001
**Editorial Correction (2026-08-01):** Document identifier changed from `TCC-IAP-001` to `DIWAI-IAP-001`; internal policy cross-references normalised to the `DIWAI-*` set. Identifier only — **no control content changed** and the version is deliberately not incremented. Aligns this document with the SSP citation set and the [DOMAIN.ORG] independence determination (SSP v2.12 corrected). See `DIWAI-EV-CM-2026-08-01`.
**Addition (2026-10-09):** Account types allowed (including reserved identities) and prohibited, intended system usage and the circumstances for disabling accounts (3.1.1 d.02, f.04, f.05), notification periods and identifier reuse added to section 3.3, and the password expiration scope and exemptions stated (3.5.7) (3.1.1, 3.5.5). Earlier 2026-10-09 corrections (password length, lockout, history) are recorded in DIWAI-CR-2026-10-11.
**Version:** 1.2
**Effective Date:** June 6, 2026
**Previous Version:** 1.0 (February 15, 2026) — YubiKey PIV hardware token as primary MFA
**Change Summary:** MFA strategy updated. YubiKey PIV hardware token abandoned (technically fragile; lockout incident 2026-05-15). Primary MFA method changed to TOTP via Authenticator app (RFC 6238).
**Review Schedule:** Annually
**Next Review:** December 2026
**Owner:** [SYSTEM-OWNER], ISSO/System Owner
**Distribution:** Authorized personnel only
**Classification:** CUI

---


**Version 1.2 (2026-08-04) — technical accuracy correction.** v1.1 (June 2026)
updated the MFA *strategy* but did not revisit the inherited technical content.
This revision does.

**Kerberos removed — it is not deployed.** Nine references described Kerberos
tickets, keytabs, principals and service principals as the authentication
mechanism. Verified 2026-08-04: **`krb5-server` and `krb5-workstation` are not
installed, `krb5kdc` is inactive, and no keytab exists.** That content came from
Reference System #1, which ran **FreeIPA** (a suite bundling 389-DS with Kerberos
and DNS). This system runs **389-DS alone**; the glossary entry describing it as
"LDAP + Kerberos + DNS" described FreeIPA, not the directory in use.

Replaced with the mechanisms actually in use: **LDAPS** for directory binds,
**LDAPI with EXTERNAL SASL** for local administrative tooling, **SSH public-key**
for host access, and scoped directory service accounts for automated processes.
The transmission clause now records that the directory **refuses insecure binds**
(`nsslapd-require-secure-binds: on`, 2026-08-03).

**MFA status stated explicitly.** The policy required MFA for privileged accounts
and remote access — correctly — under an implementation timeline of **Q4 2025 /
Q1 2026** that had elapsed without delivery, with nothing recording that it
remains undelivered. **MFA is not deployed for OS-level access**: the VM is SSH
public-key only (`pam_google_authenticator` installed but unconfigured); the Mac
host is password only. **Nextcloud's TOTP is the only second factor in the
system.** Tracked as POA&M-004 and POA&M-007; **3.5.3 and 3.7.5 each score −5**.
The requirement stands; the elapsed timeline is removed in favour of the POA&M,
which is the tracking record.

Also corrected: RS#1 hosts `ws1`/`ws2` and the pfSense appliance; `ipa user-find`
→ `dsidm`; `sys-dc1` naming example. Raised as **POA&M-058**.


## 1. Purpose

This policy establishes [DOMAIN.ORG]'s requirements for user identification and authentication on the SecureMac Reference System #2. It ensures only authorized individuals access systems and Controlled Unclassified Information (CUI) in compliance with NIST SP 800-171 Rev 2 (IA-1 through IA-11) and CMMC Level 2.

---

## 2. Scope

This policy applies to:

- **All SecureMac Systems:**
  - services.[DOMAIN.ORG] - LDAP Directory Server (389-DS)
  - services.[DOMAIN.ORG] - AI/ML Server
  - `securemac.[DOMAIN.ORG]` ([LAN-IP-REDACTED]) — Mac mini M4 Pro host and sole management workstation
  - `services.[DOMAIN.ORG]` ([LAN-IP-REDACTED]) — Rocky Linux VM: 389-DS directory
  - `nas.[DOMAIN.ORG]` ([LAN-IP-REDACTED]) — Synology NAS (authenticates against the directory over LDAPS)
  - Network: `pf` (Mac mini) and `firewalld` (VM) — software firewalls, no appliance
  - All services (email, file sharing, web applications)

- **All Users:**
  - Employees
  - Contractors and subcontractors
  - System and service accounts
  - Temporary and guest accounts (if authorized)

- **Authentication Methods:**
  - Password/passphrase
  - SSH keys
  - Multi-factor authentication (MFA)
  - Directory bind credentials and session tokens

---

## 3. Policy Statements

### 3.1 User Identification and Authentication (IA-2)

**The organization shall:**

1. **Unique User Accounts:**
   - Every user assigned unique identifier (no shared accounts)
   - User IDs tied to individual identity (First.Last format preferred)
   - Generic accounts prohibited (e.g., "admin", "user", "test")

2. **Authentication Required:**
   - Users authenticate before accessing any SecureMac resource
   - Re-authentication required after session timeout (15 minutes idle)
   - No "remember me" or saved password features on production systems

3. **Multi-Factor Authentication (IA-2(1), IA-2(2)):**
   - **Required for:**
     - Privileged accounts (system administrators, ISSO)
     - Remote access (VPN)
     - Non-organizational users (contractors, vendors) - POA&M-SPRS-1

   - **MFA Methods:**
     - TOTP via Authenticator app (primary) — e.g., Microsoft Authenticator, Google Authenticator (RFC 6238-compliant)
     - SMS/email (least preferred, emergency backup only)

   - **Current implementation status — MFA is NOT deployed for OS-level access.**
     Stated plainly because the requirement above is a requirement, not a
     description of the present state:
     - **VM (`services.[DOMAIN.ORG]`):** SSH is public-key only. `pam_google_authenticator` is installed but **not configured** in any PAM stack. A key file without a passphrase is a single factor.
     - **Mac host:** password only. YubiKey PIV was abandoned after the 2026-05-15 lockout; `pam_smartcard.so` entries are Apple stock and fall through.
     - **Nextcloud:** TOTP 2FA **is** enforced instance-wide — the only service with a second factor.
     - Tracked as **POA&M-004** (VM) and **POA&M-007** (Mac host). **3.5.3 and 3.7.5 are each scored −5** on this basis.
     - The inherited timeline (Q4 2025 / Q1 2026) had elapsed without delivery and is removed; target dates are held in the POA&M, which is the tracking record.

4. **Service Accounts:**
   - Dedicated service accounts for automated processes
   - No interactive login permitted
   - **LDAPI with EXTERNAL SASL** for local administrative tooling (`dsidm`, `dashboard-refresh`) — authenticates by Unix socket peer credentials, so no password is stored in scripts
   - **SSH public-key authentication** for host access (`PasswordAuthentication no`)
   - Annual review and re-authorization

### 3.2 Device Identification and Authentication (IA-3)

**The organization shall:**

1. **Network Device Authentication:**
   - Devices authenticate before network access
   - MAC address filtering on critical VLANs
   - 802.1X authentication (future enhancement)

2. **Software Token Authentication:**
   - TOTP via RFC 6238-compliant Authenticator app (primary MFA method)
   - Enrollment records (account username + enrollment date) tracked in ISSO log
   - Compromised TOTP secret immediately revoked and re-enrolled

### 3.3 Identifier Management (IA-4, IA-5)

**User Account Creation (IA-4):**

1. **Account Request Process:**
   - Formal request submitted to ISSO
   - Business justification required
   - Role and access level specified
   - Supervisor/sponsor approval

2. **Account Provisioning:**
   - Unique username assigned ([EMAIL-REDACTED])
   - Created in 389-DS LDAP directory
   - Directory entry created under `ou=people,dc=diwai,dc=org`
   - Initial groups assigned (ipausers minimum)
   - Home directory created with proper permissions

3. **Account Lifecycle:**
   - **Active:** Regular review (quarterly for contractors, annually for employees)
   - **Disabled:** Immediate upon termination or extended leave (>30 days)
   - **Deleted:** 90 days after termination (after backup retention)

**Account types allowed.**
- **Named administrator account.** One named, individually assigned account for the system owner (`[USERNAME]`), used for ordinary work and elevating with `sudo` for privileged operations.
- **Directory user accounts.** Named user accounts held in the 389-DS directory for VM services. Contractor accounts, if any, are limited-duration with an expiry date.
- **Service accounts.** Non-interactive accounts used by services (for example `wazuh-indexer`), with no interactive login.
- **Break-glass account.** One emergency administrative account on the Mac host (`sysadmin`), tested and used only if the owner is unavailable.
- **Application accounts.** Accounts inside applications (for example the Nextcloud and Open WebUI administrator accounts), each individually named.
- **Reserved identities.** Locked accounts held so that a name cannot be issued to anyone else (for example `demo_user`, the reserved demo identity). They are never used to log in; see the Retired Identifiers Register (`DIWAI-IA-REG-001`).

**Account types prohibited.**
- **Shared or group accounts** for interactive use.
- **Anonymous or guest accounts.**
- **Direct root login over SSH.**
- **Default or vendor-supplied accounts left active** with their original credentials.
- **Application self-registration** (Open WebUI `ENABLE_SIGNUP=false`).


**Authorizing and disabling accounts (AC-2).**

**Intended system usage.** Access to the system is authorized only for its intended uses, and an account receives only the access its holder's use requires:
- administering and maintaining the system and its security controls;
- storing, processing and exchanging the organization's CUI and FCI for contract work, through the Nextcloud CUI store and the services that support it (directory, mail, monitoring, backup);
- operating the local AI stack for the organization's compliance and operations work.

Use outside these purposes is unacceptable use under the Acceptable Use Policy, section 3. The Owner checks the intended use when an account is requested and records it with the request.

**Disabling for a policy violation.** An account is disabled when its holder commits a moderate or major violation of organizational policy, as the Personnel Security Policy sanctions define them. A first moderate offense suspends access; a major offense ends it. A contractor's directory account is disabled immediately (Acceptable Use Policy 12.2). A minor offense is handled by counseling or a written warning and does not by itself disable the account. The Owner disables the account (for the directory, by locking the entry), and the disabling is recorded in the access record with the date and the reason.

**Disabling for a significant risk.** An account is disabled when a significant risk associated with its holder is discovered, including: evidence that the holder's credentials are compromised or that the holder is acting under duress; loss or theft of a device that holds access; a credible indication of misuse or unauthorized disclosure of CUI; a security incident involving the holder; or a change in the holder's eligibility to hold access, such as loss of the status the access attestation requires. The Owner may disable the account at once, pending review. It stays disabled until the Owner records that the risk is resolved.

**Notification periods (AC-2(g)):** account managers and designated personnel or roles are notified within **24 hours** when an account is no longer required, within **24 hours** when a user is terminated or transferred, and within **24 hours** when system usage or need-to-know changes for an individual. The notification is an entry in the change or access record.

**Identifier reuse (IA-4):** an identifier is **never reused** for a different individual or service. Retired identifiers are recorded in the Retired Identifiers Register (`DIWAI-IA-REG-001`, Evidence folder).

**Authenticator Management (IA-5):**

1. **Password Requirements (IA-5(1)):**
   - **Length:** 16 characters minimum (389-DS `passwordMinLength` and the Mac `diwai.minimum.length` rule; raised from 14 on 2026-10-09, `DIWAI-CR-2026-10-11`)
   - **Complexity:** At least 3 character classes (upper, lower, number, special)
   - **Expiration:** **90 days for interactive user accounts**, counted from each password change: the Mac `[USERNAME]` account by a per-user account policy, the VM local `[USERNAME]` account by `chage -M 90`, and directory user accounts by the 389-DS global policy (warning 14 days before). **Exempt by owner decision 2026-10-09**, because expiry would break them: the service account `svc-nas` (it cannot change a password interactively), the locked reserved identity `demo_user`, the break-glass account `sysadmin` (which must work when the owner cannot), and the VM operating-system account `root` (the recovery account: remote login is refused by `PermitRootLogin no`, and no routine user signs in with it). `DIWAI-CR-2026-10-11`; `DIWAI-CR-2026-10-12`.
   - **History:** Cannot reuse the last 6 passwords (enforced on both hosts; SSP Appendix E.4)
   - **Lockout:** VM: 3 failed attempts within 5 minutes lock the account for 15 minutes; directory: 3 failed binds lock for 60 minutes; Mac: 5 consecutive failed attempts, released 15 minutes after the last (`DIWAI-CR-2026-10-11`)
   - **Transmission:** Never transmitted in clear text. The directory **refuses insecure binds** (`nsslapd-require-secure-binds: on`, enforced 2026-08-03 — `DIWAI-CR-2026-08-10`); all binds occur over **LDAPS** or the local **LDAPI** socket

2. **Initial Password:**
   - System-generated temporary password (complexity enforced)
   - Must change on first login
   - Delivered out-of-band (phone call, encrypted email, in-person)
   - Expires in 24 hours if not changed

3. **Password Reset:**
   - User identity verified before reset (security questions, supervisor confirmation)
   - Reset performed by ISSO or System Administrator only
   - New temporary password provided out-of-band
   - Immediate change required

4. **SSH Key Management (IA-5(2)(c)):**
   - **Key Generation:**
     - RSA 3072-bit minimum or Ed25519
     - Generated on user's local system (private key never transmitted)
   - **Public Key Registration:** Uploaded to 389-DS LDAP or added to `~/.ssh/authorized_keys`
   - **Private Key Protection:**
     - Encrypted with passphrase (required)
     - File permissions: 0600 (read/write owner only)
     - Stored on encrypted filesystem only
   - **Key Rotation:** Annual rotation recommended
   - **Revocation:** Immediate removal upon termination or compromise

### 3.4 Authenticator Feedback (IA-6)

**The organization shall:**

- Obscure password entry (display as asterisks or dots)
- No password display in logs or error messages
- SSH key fingerprints displayed (not full keys)
- Failed login attempts do not reveal username validity

### 3.5 Cryptographic Module Authentication (IA-7)

**The organization shall:**

- Use FIPS 140-2 validated cryptographic modules for authentication
- FIPS mode enabled on all Rocky Linux systems
- FileVault/LUKS encryption with FIPS-approved algorithms
- TLS 1.2+ for all network authentication protocols

### 3.6 Identification and Authentication (Non-Organizational Users) (IA-8)

**For contractors, vendors, and partners:**

1. **Account Requirements:**
   - Separate accounts from organizational users
   - Naming convention: contractor.firstname.lastname
   - Limited group membership (e.g., file_share_ro)
   - Explicit expiration date (contract end date)

2. **Multi-Factor Authentication (IA-8(1)):**
   - **Required:** MFA for all non-organizational users (POA&M-SPRS-1)
   - **Method:** TOTP via Authenticator app (RFC 6238)
   - **Enrollment:** Before system access granted; ISSO provisions TOTP token via `ipa otptoken-add`
   - **Backup codes:** Printed and secured by user at enrollment

3. **Enhanced Monitoring:**
   - All contractor activity logged
   - Weekly access review
   - Immediate revocation upon contract termination

### 3.7 Service Identification and Authentication (IA-9)

**The organization shall:**

1. **Service-to-Service Authentication:**
   - Dedicated directory service accounts for automated processes (e.g. `uid=svc-nas,ou=services,dc=diwai,dc=org`), scoped by ACI to least privilege
   - TLS client certificates for API authentication
   - API keys rotated annually minimum

2. **Service Account Security:**
   - No shared service accounts between systems
   - Least privilege principle applied
   - LDAPI/EXTERNAL SASL where the process is local; otherwise a scoped service account over LDAPS with the credential held root-only
   - Documented ownership and purpose

### 3.8 Adaptive Authentication (IA-10)

**The organization shall implement adaptive authentication based on:**

1. **Risk Factors:**
   - Login time (off-hours access triggers alert)
   - Geographic location (if remote access implemented)
   - Failed login attempt history
   - Account privilege level

2. **Adaptive Responses:**
   - Additional authentication challenges for high-risk logins
   - Account lockout after repeated failures
   - ISSO notification for suspicious patterns

### 3.9 Re-Authentication (IA-11)

**The organization shall require re-authentication:**

1. **Session Timeouts:**
   - Interactive sessions: 15 minutes idle timeout (AC-11)
   - Screen lock activates automatically
   - Re-authentication required to resume

2. **Privilege Escalation:**
   - sudo requires password re-entry (timeout: 15 minutes)
   - Root access logs separate session

3. **Sensitive Operations:**
   - Password changes require current password
   - Account modifications require ISSO approval
   - Critical system changes require multi-person authorization

---

## 4. Roles and Responsibilities

### 4.1 System Owner

- Approve identification and authentication policy
- Authorize privileged account creation
- Review quarterly access reports
- Ensure resource allocation for MFA implementation

### 4.2 Information System Security Officer (ISSO)

- Manage user account lifecycle
- Enforce password and authentication policies
- Configure 389-DS LDAP password policies
- Approve contractor account requests
- Conduct quarterly account reviews
- Investigate authentication anomalies
- Maintain TOTP enrollment log (username, enrollment date, app used)

### 4.3 System Administrator

- Implement technical authentication controls
- Configure the 389-DS directory
- Provision and deprovision user accounts
- Monitor authentication logs
- Respond to account lockouts
- Maintain SSH key infrastructure

### 4.4 All Users

- Protect authentication credentials (passwords, SSH keys)
- Use strong, unique passwords (password managers recommended)
- Never share passwords or SSH private keys
- Report lost/stolen authentication tokens immediately
- Change passwords if compromise suspected
- Complete MFA enrollment when required

---

## 5. Implementation Details

### 5.1 389-DS LDAP Password Policy

**Settings in force** (read back 2026-10-09; `DIWAI-CR-2026-10-11`):

| Setting | VM directory (389-DS `cn=config`) | VM operating system (PAM faillock) | Mac host (`pwpolicy`) |
|---|---|---|---|
| Minimum length | 16 (`passwordMinLength`) | n/a | 16 (`diwai.minimum.length`) |
| Character classes | 3 (`passwordMinCategories`) | n/a | n/a |
| History | 6 (`passwordInHistory`) | n/a | 6 |
| Failed attempts | 3 (`passwordMaxFailure`) | 3 (`deny`) | 5 consecutive |
| Counting window | n/a | 300 s (`fail_interval`) | n/a (consecutive count) |
| Lock duration | 3600 s | 900 s (`unlock_time`) | released 900 s after the last failure |

Administrative accounts use the same limits; there is no separate privileged-user password policy.

### 5.2 SSH Configuration

**File:** `/etc/ssh/sshd_config`

**Key Settings:**
```
PermitRootLogin no
PasswordAuthentication no (key-based only)
PubkeyAuthentication yes
AuthorizedKeysCommand /usr/bin/sss_ssh_authorizedkeys (389-DS LDAP integration)
ChallengeResponseAuthentication yes (for OTP)
UsePAM yes
```

### 5.3 Account Naming Standards

**Format:**
- **Employees:** firstname.lastname (e.g., daniel.shannon)
- **Contractors:** contractor.firstname.lastname (e.g., contractor.john.doe)
- **Service Accounts:** svc-purpose (e.g., svc-backup, svc-wazuh)
- **System Accounts:** `sys-<hostname>` (e.g. `sys-services`)

**Restrictions:**
- No special characters except hyphen and period
- Lowercase only
- Maximum 32 characters
- No spaces

### 5.4 Multi-Factor Authentication Enrollment

**Authenticator App (TOTP) Enrollment Process:**

1. **User installs an RFC 6238-compliant Authenticator app:**
   - Approved apps: Microsoft Authenticator, Google Authenticator, Authy
   - App installed on user's personal or company mobile device

2. **ISSO provisions TOTP token in 389-DS LDAP:**
   ```bash
   ipa otptoken-add --type=totp --owner=username --desc="Authenticator App - YYYY-MM-DD"
   ```
   - QR code displayed to user for scanning into app
   - Enrollment date recorded in ISSO TOTP log

3. **User verifies enrollment:**
   - SSH login: password + 6-digit OTP from app
   - Web UI login: password + 6-digit OTP from app

4. **Backup codes:**
   - Generated and provided to user at enrollment
   - User prints and stores in secure location (not digitally)
   - Backup codes revoked and re-generated if compromised

### 5.5 Account Review Process

**Quarterly Review (Due: Last Friday of March, June, September, December):**

1. **Generate Account List:**
   ```bash
   dsidm diwai user list
   ```

2. **Review Checklist:**
   - [ ] Account still required (active employee/contractor)
   - [ ] Access level appropriate for role
   - [ ] Password changed within policy timeframe
   - [ ] No excessive failed login attempts
   - [ ] MFA enrolled (if required)
   - [ ] Last login within expected timeframe

3. **Actions:**
   - Disable inactive accounts (>90 days no login, non-critical)
   - Remove expired contractor accounts
   - Adjust permissions if role changed
   - Document review in `/var/log/account-reviews/YYYY-QN.log`

---

## 6. Compliance Mapping

| NIST SP 800-171 Control | Implementation |
|-------------------------|----------------|
| **IA-1** Policy and Procedures | This document |
| **IA-2** Identification and Authentication | Section 3.1 |
| **IA-2(1)** Network Access to Privileged Accounts - MFA | Section 3.1.3 |
| **IA-2(2)** Network Access to Non-Privileged Accounts - MFA | Section 3.1.3 |
| **IA-3** Device Identification and Authentication | Section 3.2 |
| **IA-4** Identifier Management | Section 3.3 |
| **IA-5** Authenticator Management | Section 3.3 |
| **IA-5(1)** Password-Based Authentication | Section 3.3.1 |
| **IA-5(2)(c)** PKI-Based Authentication (SSH keys) | Section 3.3.4 |
| **IA-6** Authenticator Feedback | Section 3.4 |
| **IA-7** Cryptographic Module Authentication | Section 3.5 |
| **IA-8** Identification and Authentication (Non-Org Users) | Section 3.6 |
| **IA-9** Service Identification and Authentication | Section 3.7 |
| **IA-10** Adaptive Identification and Authentication | Section 3.8 |
| **IA-11** Re-Authentication | Section 3.9 |

---

## 7. Enforcement and Penalties

Violations of this policy may result in:

1. **Password Policy Violations:**
   - Account lockout (automatic)
   - Password reset by ISSO
   - Security awareness re-training

2. **Shared Credentials:**
   - Immediate termination of both accounts
   - Written reprimand
   - Potential termination of employment/contract

3. **Compromised or Lost MFA Device (Unreported):**
   - TOTP secret immediately revoked by ISSO upon report
   - Re-enrollment required before access restored
   - Written warning if failure to report promptly

4. **Circumventing Authentication Controls:**
   - Immediate account termination
   - Incident investigation
   - Potential civil/criminal prosecution

---

## 8. Policy Review and Updates

- **Review Frequency:** Annually or upon security incidents involving authentication
- **Update Triggers:**
  - New NIST guidance on authentication
  - Successful authentication bypass incidents
  - MFA technology changes
  - Regulatory requirement updates

- **Approval Authority:** System Owner / ISSO

---

## 9. Related Documents

- System Security Plan (SSP) - Section IA (Identification and Authentication)
- Acceptable Use Policy (DIWAI-AUP-001)
- Access Control Policy (future)
- Personnel Security Policy (DIWAI-PS-001)
- NIST SP 800-171 Rev 2
- NIST SP 800-63B (Digital Identity Guidelines - Authentication)

---

## 10. Definitions

- **Authenticator:** Means of confirming identity (password, token, biometric, SSH key)
- **389-DS:** Open-source LDAP directory server. *(It is a directory server only — it does not bundle Kerberos or DNS. The inherited description was of FreeIPA, which this system does not run; `ipa-server` and `krb5-server` are not installed.)*
- **LDAPS:** LDAP over TLS — the required transport for directory binds
- **LDAPI / EXTERNAL SASL:** Authentication over a local Unix socket using peer credentials, used by administrative tooling on the directory host
- **MFA (Multi-Factor Authentication):** Two or more authentication factors (something you know + something you have)
- **SSH Key:** Public-key cryptography for SSH authentication
- **TOTP:** Time-based One-Time Password (6-digit code rotates every 30 seconds)

---

## 11. Approval Signatures

**Prepared By:**
Name: [SYSTEM-OWNER], Information System Security Officer
Signature: /s/ [SYSTEM-OWNER]                Date: February 15, 2026

**Reviewed By:**
Name: [SYSTEM-OWNER], System Administrator
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
