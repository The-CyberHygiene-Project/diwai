> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# System and Information Integrity Policy

**Document ID:** DIWAI-SI-001
**Editorial Correction (2026-08-01):** Document identifier changed from `TCC-SI-001` to `DIWAI-SI-001`; internal policy cross-references normalised to the `DIWAI-*` set. Identifier only — **no control content changed** and the version is deliberately not incremented. Aligns this document with the SSP citation set and the [DOMAIN.ORG] independence determination (SSP v2.12 corrected). See `DIWAI-EV-CM-2026-08-01`.
**Version:** 1.1
**Effective Date:** November 2, 2025
**Review Schedule:** Annually or upon system changes
**Next Review:** November 2, 2026
**Owner:** [SYSTEM-OWNER], ISSO/System Owner
**Distribution:** Authorized personnel only
**Classification:** Controlled Unclassified Information (CUI)

---


**Version 1.1 (2026-08-04) — technical accuracy correction.** Inherited from
Reference System #1 (CyberInABox) and bulk-edited for [DOMAIN.ORG]; the identifier
changed, the technical content did not. Corrected here: **ClamAV/freshclam**
(decommissioned 2026-06-12, packages removed 2026-08-01) replaced throughout with
the **YARA** stack that has provided SI-3 since — YARA had appeared in this policy
only as "custom rules… if applicable" while actually being the primary control;
**pfSense/NetGate 2100** replaced with macOS `pf` and `firewalld`, and Suricata
correctly located on the VM; RS#1 workstations (`LabRat`, `Engineering`,
`Accounting`) and the `dc1` hostname removed; **"HP iLO 5 firmware on dc1 Mac mini
M4 Pro"** — a line conflating an HP server, RS#1's hostname and this host —
corrected to Apple firmware.

**One claimed control was withdrawn, not restated.** The policy asserted
real-time ClamAV VFS scanning of NAS shares. **No such scanning exists**: the
VM's YARA scan does not traverse the NAS and the Mac host runs no equivalent.
Recorded as a coverage limit under SI-3 rather than carried forward as a false
claim.

Workstation and personnel provisions are **retained and scoped** — this system is
a reference model for adoption by very small businesses, including multi-user
deployments, and provisions written only for the present headcount would not
survive that adoption. Raised as **POA&M-058**; no control changed.


## Purpose

This policy establishes requirements for maintaining the integrity of systems and information within [DOMAIN.ORG]'s SecureMac Reference System #2, ensuring flaws are remediated, malicious code is detected, and security functions are monitored to protect Controlled Unclassified Information (CUI) and Federal Contract Information (FCI). It aligns with NIST SP 800-171 Revision 2 (SI-1 through SI-12) and supports CMMC Level 2 by integrating automated tools, including the Wazuh security information and event management (SIEM) platform deployed as the Wazuh Manager on services.[DOMAIN.ORG] ([LAN-IP-REDACTED]). The policy safeguards data integrity for systems administration and AI research operations, including secure file storage on the encrypted RAID 5 array.

## Scope

This policy applies to all SecureMac systems, including:

**Server:**
- **services.[DOMAIN.ORG]** ([LAN-IP-REDACTED])
  - Rocky Linux 9.7 with FIPS 140-2 mode enabled
  - Wazuh Manager (centralized SIEM and security monitoring)
  - 389-DS LDAP domain controller
  - NAS file server with encrypted RAID 5 storage
  - rsyslog centralized logging server

**Workstations:**
- None presently deployed. The Mac mini host doubles as the sole management
  workstation — a concentration recorded, with its risks, in SSP §3.2.1.

  > **Where a deployment includes workstations** — the expected case for a VSB
  > adopting this model, and recommended even for a single operator — the
  > provisions of this policy apply to them in full.

**Network Infrastructure:**
- Perimeter firewall: macOS `pf` on the Mac mini ([LAN-IP-REDACTED])
- Host firewall: `firewalld` on the VM ([LAN-IP-REDACTED])
- Suricata IDS/IPS **on the VM**, integrated with Wazuh
- Network traffic monitoring

**Security Tools:**
- **Wazuh SIEM:** Log aggregation, vulnerability detection, file integrity monitoring, active response
- **YARA:** Malicious-code detection (5,972 rules) — Wazuh active response on FIM rules 550/554, plus a weekly full-system scan (`yara-fullscan.timer`)
- **VirusTotal:** Reputation lookup on FIM events
- **fapolicyd / SELinux:** Application allow-listing and mandatory access control on the VM
- **dnf-automatic:** Automated security patching
- **OpenSCAP:** Compliance verification and configuration assessment
- **Suricata:** Network intrusion detection/prevention

**Personnel:**
- All users responsible for reporting system anomalies and integrity issues

**Exclusions:** Non-security integrity functions (e.g., business application logic, data validation) are covered under Configuration Management Policy.

## Definitions

- **Wazuh Manager:** Centralized SIEM on the VM (`services.[DOMAIN.ORG]`) for real-time monitoring, alerting, threat detection, and compliance reporting

- **Flaw Remediation:** Process of patching vulnerabilities and correcting security weaknesses, including those detected by Wazuh vulnerability scanner

- **Integrity Verification:** Confirmation that system configurations and file contents match approved baselines via Wazuh agents and OpenSCAP scans

- **Malicious Code:** Software designed to compromise system security, including viruses, worms, trojans, ransomware, spyware

- **File Integrity Monitoring (FIM):** Continuous monitoring of critical files and directories for unauthorized changes

- **CVE (Common Vulnerabilities and Exposures):** Standardized identifier for known security vulnerabilities

- **CVSS (Common Vulnerability Scoring System):** Standard for assessing severity of vulnerabilities (0.0-10.0 scale)

## Policy Statements

### 1. System and Information Integrity Policy and Procedures (SI-1)

[DOMAIN.ORG] shall maintain and review this policy annually. Implementation procedures are documented in Section 2 of this document. Compliance is verified through:
- Quarterly Wazuh dashboard reviews
- Quarterly OpenSCAP compliance scans
- Monthly vulnerability scan reports
- Weekly flaw remediation status reviews

### 2. Flaw Remediation (SI-2)

**Vulnerability Identification:**
- Wazuh vulnerability detection runs continuously on all systems
- CVE feed updates every 60 minutes
- OpenSCAP scans quarterly (minimum)
- Manual security bulletins reviewed weekly (US-CERT, Rocky Linux, vendor advisories)

**Remediation Timelines:**
- **Critical vulnerabilities (CVSS 9.0-10.0):** 7 days maximum
- **High severity (CVSS 7.0-8.9):** 30 days
- **Medium severity (CVSS 4.0-6.9):** 90 days
- **Low severity (CVSS 0.1-3.9):** Next scheduled maintenance window

**Automated Patching:**
- `dnf-automatic` enabled on all SecureMac systems
- Security updates applied automatically (with testing on non-production first)
- Critical patches may require manual application with immediate testing

**Flaw Remediation Process:**
1. Wazuh vulnerability detector identifies flaw and generates alert
2. ISSO reviews alert and assesses CVSS score and exploitability
3. Prioritize remediation based on severity and criticality of affected system
4. Stage the patch on the lowest-criticality component available; where a
   deployment has workstations, patch those before the server tier
5. Apply to the VM, then the Mac host, per `CUI_Patch_Review_Procedure`
6. Verify FIPS mode integrity after patching: `fips-mode-setup --check`
7. Rescan with Wazuh and OpenSCAP to verify remediation
8. Document remediation in POA&M
9. Escalate to Owner/Principal if patch causes operational issues

**Exception Process:**
- If patch unavailable or incompatible, implement compensating controls
- Document accepted risk with Owner/Principal approval
- Add to POA&M with target remediation date
- Re-assess monthly until resolved

### 3. Malicious Code Protection (SI-3)

**Anti-Malware Deployment.** ClamAV was **decommissioned 2026-06-12** — under
FIPS it could neither download nor load a signature database, so it provided no
detection — and its packages were removed 2026-08-01. SI-3 is met by a
FIPS-native stack (evidence `DIWAI-EV-SI3-002`; SSP §3.4):

- **YARA 4.5.2** (5,972 rules) — the primary malicious-code scanner on the VM
- **Wazuh active response** invokes YARA on FIM rules 550/554 (file created/modified)
- **VirusTotal** reputation lookup on FIM events
- **fapolicyd** application allow-listing and **SELinux** enforcing on the VM
- **XProtect, MRT and Gatekeeper** on the Mac host (Apple-native, auto-updated)

**Scanning Schedule:**
- **Event-driven:** YARA runs via Wazuh active response whenever a monitored file is created or modified
- **Weekly:** full-system YARA scan (`yara-fullscan.timer`)
- **On-demand:** `sudo /usr/local/sbin/yara-fullscan.sh`

**Known coverage limit — NAS content is not scanned.** No host-based scanner
inspects data at rest on `nas.[DOMAIN.ORG]`. The VM's YARA scan does not traverse
the NAS, and the Mac host runs no equivalent scanner. Earlier text in this policy
claimed real-time VFS scanning of NAS shares; **that control does not exist** and
the claim is withdrawn rather than restated. Recorded for remediation.

**Malware Response:**
```bash
# Wazuh active response invokes YARA on FIM events (rules 550/554)
# Detections are logged to the Wazuh manager and alert the ISSO
# Manual scan:
sudo /usr/local/sbin/yara-fullscan.sh
```

**Rule Updates:**
- YARA rulesets refreshed as part of the scan tooling
- Wazuh detection rules update automatically
- Apple XProtect/MRT signatures update automatically on the Mac host
- Verify schedule: `systemctl list-timers yara-fullscan.timer`

**User Responsibilities:**
- Report suspicious files or behaviors immediately to ISSO
- Do not attempt to open or execute suspected malware
- Do not disable anti-malware tools
- Avoid downloading software from untrusted sources

### 4. System Monitoring (SI-4)

**Continuous Monitoring via Wazuh Manager:**
- **Log Aggregation:** rsyslog forwards system logs to the Wazuh manager on the VM
- **Real-Time Analysis:** Wazuh analyzes logs as they arrive
- **Alert Generation:** Immediate notifications for security events
- **Dashboard Visibility:** Real-time security posture via web interface

**Monitoring Scope:**
- Authentication attempts (successful and failed)
- Privilege escalation (sudo usage)
- File access on CUI directories (/mnt/nas, /home)
- System configuration changes (/etc, /var/ossec, 389-DS LDAP configs)
- Network connections (via Suricata IDS integration)
- Process execution (new binaries, suspicious commands)
- Software installation/removal (dnf activity)

**Network Monitoring:**
- Suricata IDS/IPS on the VM monitors network traffic
- Rules updated daily from Emerging Threats and Snort
- Integration with Wazuh for centralized alerting
- Focus on: malware communication, data exfiltration, port scans, DoS attacks

**File Integrity Monitoring (FIM):**
Wazuh monitors these critical paths (12-hour scan interval):
- `/etc/` - System configuration files
- `/var/ossec/` - Wazuh configuration
- `/etc/dirsrv/slapd-diwai/` - 389-DS LDAP configuration
- `/etc/samba/` - NAS configuration
- `/mnt/nas/` - CUI file shares (selected directories)
- `/usr/local/bin/` - Custom scripts
- `/boot/` - Boot files and kernel

**Alert Priorities:**
- **Critical:** Immediate ISSO notification (SMS/email), investigate within 1 hour
- **High:** Email alert, investigate within 4 hours
- **Medium:** Dashboard alert, review within 24 hours
- **Low:** Weekly summary review

**Review Schedule:**
- **Daily:** ISSO reviews Wazuh dashboard for critical/high alerts
- **Weekly:** Comprehensive review of all alerts and trends
- **Monthly:** Statistical analysis and reporting to Owner/Principal
- **Quarterly:** Monitoring effectiveness assessment

### 5. Security Alerts, Advisories, and Directives (SI-5)

**Information Sources:**
- **US-CERT (CISA):** Subscribe to alerts via email and RSS
- **Rocky Linux Security:** Monitor errata and security advisories
- **NIST National Vulnerability Database:** CVE notifications
- **Wazuh Feed:** Integrated vulnerability intelligence
- **Vendor Security Bulletins:** Apple (macOS, firmware), Rocky Linux / Red Hat (VM), Synology (NAS), Wazuh
- **DISA STIGs:** DoD security guidance updates

**Alert Processing:**
1. Wazuh automatically ingests CVE feeds (updated hourly)
2. ISSO reviews US-CERT/CISA alerts weekly
3. Critical alerts trigger immediate assessment of SecureMac exposure
4. Applicable alerts generate remediation tasks in POA&M
5. High-priority alerts drive immediate patching (per SI-2 timelines)

**Dissemination:**
- Security-relevant alerts shared with all SecureMac users
- Training updates for new threat vectors (per DIWAI-ATP-001)
- Contractor notifications for applicable risks
- Client notifications if contract-specific vulnerabilities identified

**Response Actions:**
```bash
# Example: US-CERT alert for critical Linux kernel vulnerability
# 1. Check SecureMac systems for vulnerable kernel version
uname -r
rpm -q kernel

# 2. Review Wazuh vulnerability detector for auto-detection
# Dashboard: Vulnerabilities > Search: CVE-YYYY-NNNNN

# 3. If vulnerable, apply emergency patch
sudo dnf update kernel --security
sudo reboot

# 4. Verify patch and FIPS mode post-reboot
uname -r
fips-mode-setup --check

# 5. Document in POA&M and incident log
```

### 6. Security Functionality Verification (SI-6)

**Quarterly Verification via OpenSCAP:**
```bash
# Run comprehensive CUI profile scan
sudo oscap xccdf eval \
    --profile xccdf_org.ssgproject.content_profile_cui \
    --results /backup/compliance-scans/oscap-$(date +%Y%m%d).xml \
    --report /backup/compliance-scans/oscap-$(date +%Y%m%d).html \
    /usr/share/xml/scap/ssg/content/ssg-rl9-ds.xml
```

**Critical Security Functions to Verify:**
- **FIPS 140-2 mode:** `fips-mode-setup --check` (must return "FIPS mode is enabled")
- **SELinux enforcement:** `getenforce` (must return "Enforcing")
- **Firewall status:** `sudo firewall-cmd --state` (must return "running")
- **Audit daemon:** `sudo systemctl status auditd` (must be active)
- **Wazuh Manager:** `sudo systemctl status wazuh-manager` (must be active)
- **Malicious-code scanning:** `systemctl list-timers yara-fullscan.timer` (must be scheduled)
- **Automatic updates:** `sudo systemctl status dnf-automatic.timer` (must be active)

**Wazuh Dashboard Correlation:**
- Review Wazuh compliance module for PCI-DSS, NIST 800-171, CIS benchmarks
- Correlate OpenSCAP results with Wazuh Security Configuration Assessment (SCA)
- Generate combined compliance report quarterly

**Deviation Response:**
- Any security function failure triggers immediate investigation
- Remediate within 30 days or document compensating control
- Critical function failures (FIPS, SELinux) require same-day remediation
- Update POA&M with remediation plan and target date

### 7. Software, Firmware, and Information Integrity (SI-7)

**Software Integrity:**
- All software installed via trusted repositories (Rocky Linux BaseOS, AppStream)
- Package signature verification enforced: `rpm --checksig`
- Checksum validation during updates: `dnf verify`
- Wazuh FIM detects unauthorized changes to binaries

**Firmware Integrity:**
- Apple firmware / macOS updates on the Mac mini M4 Pro (no out-of-band management controller is present)
- Firmware updates obtained directly from HP support site
- Checksum verification before applying updates
- Post-update verification via iLO console
- Document firmware versions in system baseline

**File Integrity Monitoring:**
Wazuh monitors file hashes (SHA-256) for:
- All files in `/etc/` (system configuration)
- All files in `/var/ossec/` (Wazuh configuration)
- 389-DS LDAP configuration: `/etc/dirsrv/slapd-diwai/`, `/var/lib/dirsrv/slapd-diwai/`
- NAS configuration: `/etc/samba/`
- Critical binaries: `/bin/`, `/sbin/`, `/usr/bin/`, `/usr/sbin/`
- Boot files: `/boot/`

**Integrity Verification Process:**
```bash
# Verify RPM package integrity
sudo rpm -Va | grep -E '^..5' # Check for modified files

# Verify specific package
sudo rpm -V package_name

# Check Wazuh FIM alerts
# Dashboard: Integrity Monitoring > Search: last 24 hours

# Investigate unauthorized changes
sudo ausearch -f /path/to/modified/file -ts recent
```

**Response to Integrity Violations:**
1. Wazuh FIM alert triggers immediate investigation
2. Determine if change was authorized (check change log, recent admin activity)
3. If unauthorized:
   - Preserve evidence (copy audit logs)
   - Restore file from backup or reinstall package
   - Initiate incident response procedure (DIWAI-IRP-001)
   - Investigate root cause
4. Document all integrity incidents
5. Update baseline if change was legitimate but undocumented

### 8. Spam Protection (SI-8)

**Current Status:** Not applicable - SecureMac does not currently operate inbound email services

**Future Implementation (when Postfix/Dovecot deployed):**
- Deploy SpamAssassin or Rspamd for spam filtering
- Configure DKIM, SPF, DMARC for email authentication
- Implement sender reputation checks
- Quarantine suspected spam
- User training on phishing recognition

### 9. Information Input Validation (SI-10)

**Application-Level Controls:**
- Web applications (if deployed) shall validate all user inputs
- 389-DS LDAP web interface uses built-in input validation
- Wazuh dashboard validates all API inputs
- NAS validates file names and paths

**System-Level Controls:**
- SELinux enforces type enforcement for all processes
- File system mount options enforce security (noexec, nosuid for /tmp)
- Firewall restricts network inputs to authorized ports/protocols

**User-Uploaded Files:**
- NAS shares: **no host-based malicious-code scanning is currently performed** — see the coverage limit recorded under SI-3 above
- File type restrictions enforced (if configured)
- Max file size limits prevent DoS via storage exhaustion
- Executable files flagged and quarantined

### 10. Error Handling (SI-11)

**Error Message Policy:**
- System errors shall not reveal sensitive information (file paths, credentials, internal IP addresses)
- User-facing errors provide minimal detail
- Detailed error information logged to audit logs (ISSO access only)
- Application errors captured in centralized logging

**Logging Requirements:**
- All errors logged with sufficient detail for troubleshooting
- Error logs protected with same controls as audit logs
- SELinux prevents unauthorized error log access
- Wazuh monitors error patterns for anomalies

### 11. Information Handling and Retention (SI-12)

**CUI Data Handling:**
- All CUI data stored on LUKS-encrypted partitions (FIPS 140-2)
- CUI marked per 32 CFR Part 2002 requirements
- Access restricted via 389-DS LDAP group membership
- NAS audit logging tracks all CUI file access

**Data Retention:**
- Audit logs: 90 days online, 3 years archived
- System backups: 30 days daily, 1 year full backups
- CUI documents: Per contract requirements (minimum 3 years)
- Compliance reports: 3 years
- Incident records: 3 years post-incident

**Secure Disposal:**
- LUKS-encrypted media: `cryptsetup luksErase` destroys encryption keys
- Unencrypted media (if any): `shred -vfz -n 10` (NIST SP 800-88)
- Physical media destruction for high-sensitivity data
- Document all disposal activities

## Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **ISSO ([SYSTEM-OWNER])** | Configure Wazuh rules and alerts; review dashboards daily; oversee vulnerability remediation; conduct integrity verifications; maintain documentation in `/backup/integrity-logs/`; respond to security alerts; coordinate incident response for integrity violations |
| **Owner/Principal ([SYSTEM-OWNER])** | Approve critical remediation actions; review quarterly Wazuh reports; accept residual risks; authorize emergency patches; ensure policy compliance |
| **Users/Contractors** | Report potential integrity issues immediately (unexpected file changes, suspicious behavior); comply with no-unauthorized-software rule; report malware detections; do not disable security tools |
| **System Administrator (ISSO concurrent role)** | Apply security patches; configure security tools; maintain system baselines; execute OpenSCAP scans; manage Wazuh Manager |

## Compliance and Enforcement

**Monitoring:**
- Wazuh dashboards provide real-time security metrics
- Quarterly OpenSCAP/Wazuh correlation reports
- Monthly vulnerability trending analysis
- Integration with Audit and Accountability Policy (DIWAI-AAP-001) for log protection

**Training:**
- Covered in Security Awareness and Training Procedure (DIWAI-ATP-002 — NOT YET ISSUED, see POA&M-008)
- Wazuh alert recognition and response
- Malware identification and reporting
- Incident reporting procedures

**Enforcement:**
- Non-compliance (e.g., ignored Wazuh alerts, disabled security tools) results in access revocation per Personnel Security Policy (DIWAI-PS-001)
- Security incidents trigger Incident Response Policy (DIWAI-IRP-001)
- Violations may result in contract termination

**Metrics:**
- Mean Time to Detect (MTTD): Target <1 hour
- Mean Time to Respond (MTTR): Target <4 hours
- Patch compliance rate: Target >95%
- OpenSCAP compliance score: Target >95%
- False positive rate: Track and tune Wazuh rules

## References

- NIST SP 800-171 Rev 2, SI Family (System and Information Integrity)
- NIST SP 800-53 Rev 5 (SI controls)
- System Security Plan (SSP), Section 3.14
- Wazuh Documentation: https://documentation.wazuh.com
- YARA Documentation: https://yara.readthedocs.io/
- Rocky Linux Security Guide
- DISA STIG for RHEL 9
- Risk Management Policy (DIWAI-RA-001)
- Incident Response Policy (DIWAI-IRP-001)
- Configuration Management Baseline

---

## Section 2: System and Information Integrity Procedures

### Procedure 1: Daily Wazuh Dashboard Review

**Frequency:** Daily (weekday mornings)

**Process:**
1. Access Wazuh dashboard: https://services.[DOMAIN.ORG]:443
2. Review Security Events dashboard:
   - Critical and High severity alerts from last 24 hours
   - Authentication failures (look for patterns)
   - File Integrity Monitoring alerts
   - Malware detections
3. Review Vulnerabilities dashboard:
   - New CVEs detected
   - Critical vulnerabilities (CVSS >9.0)
   - Unpatched systems
4. Review Compliance dashboard:
   - NIST 800-171 compliance status
   - CIS benchmark failures
   - Configuration drift
5. Investigate any anomalies
6. Document findings in `/backup/integrity-logs/daily-review-$(date +%Y%m%d).txt`
7. Create tickets for remediation actions

**Time Required:** 15-30 minutes

### Procedure 2: Weekly Vulnerability Remediation

**Frequency:** Weekly (Friday mornings)

**Process:**
```bash
# 1. Review available security updates
sudo dnf updateinfo list security

# 2. Stage updates on the lowest-criticality component available
# (SSH to the staging host, where one exists)
sudo dnf update --security -y

# 3. Verify FIPS mode after update
fips-mode-setup --check

# 4. Reboot if kernel updated
sudo reboot

# 5. Post-reboot verification
uname -r
sudo systemctl status wazuh-agent

# 6. If successful, apply to any workstations in the deployment
# (Repeat for Engineering and Accounting)

# 7. Finally, update the VM (services.[DOMAIN.ORG]) during a maintenance window
# (Schedule for weekend or evening)

# 8. Document all updates in POA&M
```

### Procedure 3: Quarterly Compliance Verification

**Frequency:** Quarterly (first week of Jan, Apr, Jul, Oct)

**Process:**
```bash
# 1. Run comprehensive OpenSCAP scan
sudo oscap xccdf eval \
    --profile xccdf_org.ssgproject.content_profile_cui \
    --results /backup/compliance-scans/oscap-$(date +%Y%m%d).xml \
    --report /backup/compliance-scans/oscap-$(date +%Y%m%d).html \
    /usr/share/xml/scap/ssg/content/ssg-rl9-ds.xml

# 2. Review results
firefox /backup/compliance-scans/oscap-$(date +%Y%m%d).html

# 3. Verify critical security functions
fips-mode-setup --check
getenforce
sudo systemctl status auditd
sudo systemctl status wazuh-manager
systemctl list-timers yara-fullscan.timer

# 4. Generate Wazuh compliance report
# Dashboard: Management > Reporting > Generate Report (NIST 800-171)

# 5. Correlate findings
# Compare OpenSCAP failures with Wazuh SCA results
# Identify discrepancies

# 6. Create remediation plan for failures
# Add to POA&M with target dates

# 7. Brief Owner/Principal on compliance posture
# Provide summary report with trends

# 8. Update SSP if needed
```

---

## Appendix: Wazuh Alert Examples and Responses

### Example 1: File Integrity Violation
**Alert:** "File /etc/samba/smb.conf modified"
**Response:**
1. Check if change was authorized (recent admin activity?)
2. Review audit logs: `sudo ausearch -f /etc/samba/smb.conf -ts recent`
3. If unauthorized, restore from backup and investigate
4. If authorized, update change log

### Example 2: Critical Vulnerability Detected
**Alert:** "CVE-2024-XXXXX detected - CVSS 9.8 - kernel vulnerability"
**Response:**
1. Assess exploit availability (check NVD, exploit-db)
2. Verify all affected systems via Wazuh vulnerability dashboard
3. Stage and test the patch within 24 hours
4. Deploy to production within 7 days
5. Document in POA&M

### Example 3: Malware Detection
**Alert:** "YARA rule match on a file created under a monitored directory (Wazuh rule 554)"
**Response:**
1. Wazuh active response records the detection and alerts the ISSO
2. Identify user who uploaded file: `sudo grep file.exe /var/log/samba/log.smbd`
3. Notify user immediately
4. Scan the affected host: `sudo /usr/local/sbin/yara-fullscan.sh`
5. Initiate incident response if widespread infection
6. User training on safe file handling

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
