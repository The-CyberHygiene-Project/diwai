> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Audit and Accountability Policy

**Document ID:** DIWAI-AAP-001
**Editorial Correction (2026-08-01):** Document identifier changed from `TCC-AAP-001` to `DIWAI-AAP-001`; internal policy cross-references normalised to the `DIWAI-*` set. Identifier only — **no control content changed** and the version is deliberately not incremented. Aligns this document with the SSP citation set and the [DOMAIN.ORG] independence determination (SSP v2.12 corrected). See `DIWAI-EV-CM-2026-08-01`.
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

- **The audited-systems list named one host three times.** `mac-mini.[DOMAIN.ORG] ([LAN-IP-REDACTED])` appeared as "Admin Workstation", "Engineering Workstation" and "Operations Workstation" — three RS#1 workstations bulk-replaced with this system's single host, leaving three identical entries. Replaced with the actual three hosts.
- **`pfSense` removed** from the log-source table; the firewalls are macOS `pf` and `firewalld`, whose logs reach Wazuh via the host agents.

**Two retention figures were unsubstantiated and are corrected rather than
restated** (verified 2026-08-04):

- **"Centralized retention: 90 days on Wazuh Manager"** — **no ISM retention policy is configured** on the indexer. Nothing deletes indices at 90 days; data accumulates. The figure was not enforced by any mechanism.
- **"Archival retention: 1 year on encrypted backup media"** — encrypted archives ship to the NAS daily, but **no expiry rule or verified one-year retention exists**.
- **"Online retention: 30 days minimum"** is now achievable and is restated with its basis (6.4 GB configured capacity), together with the material caveat that retention was raised only on **2026-08-01** — before which it held roughly **one hour** (POA&M-012) — so audit history begins at that date and 30-day depth accrues from it.

**AU-11 is a requirement to define and enforce retention.** Publishing periods
that no mechanism enforces would be a claim that cannot be demonstrated on
request. Defining an indexer ISM policy and a NAS archive expiry rule is
outstanding work, tracked under **POA&M-059**.

Raised as **POA&M-058**.


## 1. Purpose

This policy establishes [DOMAIN.ORG]'s requirements for audit logging, monitoring, and accountability on the SecureMac Reference System #2. It ensures comprehensive audit trails for all security-relevant events to detect unauthorized activity, support incident investigations, and meet NIST SP 800-171 Rev 2 requirements (AU-1 through AU-12) and CMMC Level 2 compliance.

---

## 2. Scope

This policy applies to:

- **All SecureMac Systems:**
  - services.[DOMAIN.ORG] ([LAN-IP-REDACTED]) - LDAP/Services Server
  - services.[DOMAIN.ORG] ([LAN-IP-REDACTED]) - AI/ML Server
  - `securemac.[DOMAIN.ORG]` ([LAN-IP-REDACTED]) — Mac mini M4 Pro: host, perimeter firewall, hypervisor, Nextcloud CUI store, and sole management workstation
  - `services.[DOMAIN.ORG]` ([LAN-IP-REDACTED]) — Rocky Linux VM: 389-DS, Wazuh manager, mail, Nextcloud database
  - `nas.[DOMAIN.ORG]` ([LAN-IP-REDACTED]) — Synology NAS
  - Additional workstations, where a deployment includes them

- **All Personnel:** Employees, contractors, and subcontractors accessing SecureMac resources

- **Audit Events:** Authentication, authorization, file access, system configuration changes, privileged operations, security incidents

---

## 3. Policy Statements

### 3.1 Audit Logging Requirements (AU-2, AU-3, AU-12)

**The organization shall:**

1. **Log Security-Relevant Events:**
   - User authentication (successful and failed) - AU-2(a)
   - Privileged operations (sudo, root access) - AU-2(a)
   - File access to CUI data stores - AU-2(d)
   - System configuration changes - AU-2(a)
   - Account creation, modification, deletion - AU-2(a)
   - Network connections and firewall events - AU-2(a)
   - Security alerts from Wazuh SIEM and Suricata IDS/IPS - AU-2(a)

2. **Audit Record Content (AU-3):**
   Each audit record shall include:
   - Event type and outcome (success/failure)
   - Date and timestamp (synchronized via NTP)
   - User/process identity
   - Source and destination IP addresses (network events)
   - Object/resource accessed
   - Additional details for security investigations

### 3.2 Audit Storage and Protection (AU-4, AU-9, AU-11)

**Requirements:**

1. **Storage Capacity (AU-4):**
   - Minimum 30 days of audit logs retained online
   - Alert when storage reaches 75% capacity
   - Automatic log rotation to prevent storage exhaustion

2. **Audit Log Protection (AU-9):**
   - Audit logs protected from unauthorized access, modification, and deletion
   - File permissions: 0640 (owner read/write, group read only)
   - SELinux context: `auditd_log_t` or equivalent
   - Logs transmitted to centralized Wazuh Manager for tamper-resistant storage

3. **Retention Period (AU-11):**
   - **Online retention (VM audit logs):** configured for `max_log_file = 64` MB × `num_logs = 100` ≈ **6.4 GB**, which at current volume supports well over 30 days. *Note: retention was raised on 2026-08-01 (`DIWAI-CR-2026-08-01` C12) from a prior configuration holding roughly one hour; audit history therefore begins 2026-08-01 and the 30-day depth accrues from that date.*
   - **Centralized retention (Wazuh indexer):** **no automated retention policy is configured.** Verified 2026-08-04 — no ISM policy governs index deletion. Data accumulates rather than being retained for a defined period and then aged out. The previously stated "90 days" was not enforced by any mechanism.
   - **Archival retention:** encrypted audit archives are shipped to the NAS daily (`wazuh-log-archive`). **No automated expiry or verified one-year retention is in place**; the previously stated "1 year" was not enforced.
   - Extended retention for incidents under investigation

   > **Both centralized and archival figures were unsubstantiated claims and are
   > corrected rather than restated.** Defining and enforcing retention periods —
   > an ISM policy on the indexer, and an expiry rule for the NAS archives — is
   > outstanding work, tracked with the other recurring-obligation gaps under
   > **POA&M-059**. Stating a retention period no mechanism enforces would be an
   > AU-11 claim that cannot be demonstrated.

### 3.3 Audit Monitoring and Review (AU-6, AU-6(1))

**The organization shall:**

1. **Automated Monitoring (AU-6(1)):**
   - Wazuh SIEM configured to analyze logs in real-time
   - Automated alerts for:
     - Multiple failed login attempts (5 within 15 minutes)
     - Privileged command execution (sudo, su)
     - File integrity changes to system binaries
     - Suspicious network activity (IDS/IPS alerts)
     - Account lockouts or disablements

2. **Manual Review (AU-6):**
   - Daily review of Wazuh alerts by System Administrator
   - Weekly comprehensive audit log review
   - Monthly trend analysis for anomaly detection
   - Immediate review upon security incident

3. **Review Documentation:**
   - Log review activities documented in security log
   - Findings and follow-up actions tracked in POA&M
   - Escalation to ISSO for high-severity findings

### 3.4 Time Synchronization (AU-8)

**Requirements:**

1. All systems synchronized to authoritative time source:
   - Primary NTP: time.nist.gov
   - Secondary NTP: time.cloudflare.com
   - Maximum time drift: ±1 second

2. Time zone: Mountain Standard Time (MST/MDT)

3. Timestamp format: ISO 8601 (YYYY-MM-DD HH:MM:SS)

### 3.5 Audit Record Generation (AU-12)

**Logging Mechanisms:**

| System Component | Logging Tool | Configuration |
|------------------|--------------|---------------|
| Operating System | auditd | NIST 800-171 CUI profile |
| Authentication | pam, sssd, 389-DS LDAP | All auth events logged |
| File Access | auditd file watches | CUI directories monitored |
| Web Services | Apache access/error logs | Combined log format |
| Email Services | Postfix, Dovecot | Mail delivery and access logged |
| SIEM | Wazuh Manager | Centralized log aggregation |
| Network | Suricata IDS/IPS | EVE JSON format |
| Firewall | macOS `pf` (Mac mini) / `firewalld` (VM) | pf logs via the Mac Wazuh agent; firewalld via the VM agent |

### 3.6 Audit Reduction and Reporting (AU-7)

**The organization shall:**

1. Provide audit log search and filtering capabilities via:
   - Wazuh web interface (Kibana/OpenSearch)
   - Command-line tools (ausearch, grep, journalctl)

2. Generate monthly audit summary reports including:
   - Authentication statistics (successful/failed logins)
   - Privileged operations count
   - Security alerts by severity
   - Top 10 security events
   - Compliance status

3. Custom queries available for incident investigation

### 3.7 Response to Audit Processing Failures (AU-5)

**Failure Handling:**

1. **Storage Capacity Alerts:**
   - Alert at 75% capacity: Email to System Administrator
   - Alert at 90% capacity: Critical alert, immediate action required
   - At 95% capacity: Automatic log rotation and archival

2. **Logging Service Failures:**
   - Wazuh agent offline >1 hour: Alert generated
   - auditd service failure: System prevents operations until restored
   - Automatic service restart attempts (systemd watchdog)

3. **Incident Escalation:**
   - Audit processing failures treated as security incidents
   - Root cause analysis required
   - POA&M item created if systemic issue

---

## 4. Roles and Responsibilities

### 4.1 Information System Security Officer (ISSO)

- Define audit events to be logged (AU-2)
- Review audit logs for security incidents
- Approve audit policy changes
- Ensure compliance with retention requirements
- Coordinate incident response based on audit findings

### 4.2 System Administrator

- Configure and maintain audit logging systems
- Monitor audit storage capacity
- Perform daily alert review
- Generate monthly audit reports
- Protect audit logs from unauthorized access
- Respond to audit processing failures

### 4.3 All Users

- Understand that activities are logged and monitored
- Report suspected security incidents immediately
- Cooperate with audit-based investigations
- Do not attempt to disable or circumvent audit mechanisms

---

## 5. Implementation Details

### 5.1 Auditd Configuration

**File:** `/etc/audit/audit.rules` (NIST 800-171 CUI profile)

**Key Rules:**
```bash
# Authentication events
-w /var/log/lastlog -p wa -k logins
-w /var/run/faillock/ -p wa -k logins

# Privileged commands
-a always,exit -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -k privileged

# File integrity monitoring
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/gshadow -p wa -k identity

# CUI data access
-w /mnt/nas/shared -p rwa -k cui_access
-w /data -p rwa -k cui_access
```

### 5.2 Wazuh SIEM Integration

**Wazuh Manager:** services.[DOMAIN.ORG]:1514

**Monitored Logs:**
- `/var/log/audit/audit.log` (auditd)
- `/var/log/secure` (authentication)
- `/var/log/messages` (system events)
- `/var/log/httpd/` (web server)
- `/var/log/samba/` (file sharing)

**Alert Severity Levels:**
- Level 12+: Critical - Immediate action required
- Level 8-11: High - Review within 4 hours
- Level 5-7: Medium - Review within 24 hours
- Level 1-4: Low - Weekly review

### 5.3 Log Rotation

**Configuration:** `/etc/logrotate.conf`

**Retention:**
- Daily rotation at midnight
- Compress logs older than 1 day (gzip)
- Retain 30 daily logs locally
- Archive to centralized storage after 30 days

---

## 6. Compliance Mapping

| NIST SP 800-171 Control | Implementation |
|-------------------------|----------------|
| **AU-1** Policy and Procedures | This document |
| **AU-2** Audit Events | Section 3.1 |
| **AU-3** Content of Audit Records | Section 3.1.2 |
| **AU-4** Audit Storage Capacity | Section 3.2.1 |
| **AU-5** Response to Audit Failures | Section 3.7 |
| **AU-6** Audit Review, Analysis, Reporting | Section 3.3 |
| **AU-6(1)** Automated Process Integration | Section 3.3.1 |
| **AU-7** Audit Reduction and Report Generation | Section 3.6 |
| **AU-8** Time Stamps | Section 3.4 |
| **AU-9** Protection of Audit Information | Section 3.2.2 |
| **AU-11** Audit Record Retention | Section 3.2.3 |
| **AU-12** Audit Generation | Section 3.5 |

---

## 7. Enforcement and Penalties

Violations of this policy may result in:

1. Verbal or written warning
2. Suspension of system access
3. Termination of employment or contract
4. Civil or criminal prosecution (for malicious activity)

All violations shall be documented and investigated according to the Incident Response Policy.

---

## 8. Policy Review and Updates

- **Review Frequency:** Annually or upon significant system changes
- **Update Triggers:**
  - New regulatory requirements
  - Security incidents revealing policy gaps
  - Changes to SecureMac infrastructure
  - Audit findings or assessments

- **Approval Authority:** System Owner / ISSO

---

## 9. Related Documents

- System Security Plan (SSP) - Section AU (Audit and Accountability)
- Incident Response Policy (DIWAI-IRP-001)
- System and Information Integrity Policy (DIWAI-SI-001)
- NIST SP 800-171 Rev 2
- NIST SP 800-53 Rev 5 (AU family)

---

## 10. Definitions

- **Audit Log:** Record of system activities including user actions, security events, and system changes
- **Audit Trail:** Chronological record of audit logs enabling reconstruction of events
- **CUI:** Controlled Unclassified Information requiring protection per NIST SP 800-171
- **Security-Relevant Event:** Activity that could affect system security posture
- **SIEM:** Security Information and Event Management system (Wazuh)

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
