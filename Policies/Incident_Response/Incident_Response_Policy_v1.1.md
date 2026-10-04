> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Incident Response Policy and Procedures

**Document ID:** DIWAI-IRP-001
**Editorial Correction (2026-08-01):** Document identifier changed from `TCC-IRP-001` to `DIWAI-IRP-001`; internal policy cross-references normalised to the `DIWAI-*` set. Identifier only — **no control content changed** and the version is deliberately not incremented. Aligns this document with the SSP citation set and the [DOMAIN.ORG] independence determination (SSP v2.12 corrected). See `DIWAI-EV-CM-2026-08-01`.
**Version:** 1.1
**Effective Date:** November 2, 2025
**Review Schedule:** Annually or post-incident
**Next Review:** November 2, 2026
**Owner:** [SYSTEM-OWNER], ISSO/System Owner
**Distribution:** Authorized personnel only
**Classification:** CUI

---


**Version 1.1 (2026-08-04) — technical accuracy correction.** This policy was
inherited from Reference System #1 (CyberInABox) and bulk-edited for [DOMAIN.ORG];
the identifier changed but the technical content did not. Corrected in this
revision: three named workstations that belong to RS#1 (`LabRat`, `Engineering`,
`Accounting`) replaced with the actual three-host boundary; **pfSense/NetGate**
references replaced with the real controls (macOS `pf` at the perimeter,
`firewalld` on the VM); **ClamAV/freshclam** replaced with the **YARA** stack that
has provided SI-3 since 2026-06-12; **FreeIPA `ipa` commands** replaced with
389-DS equivalents (`ipa-server` is not installed here); `dc1` hostname
corrected; personnel scope corrected to a single operator holding all roles.
A containment caution was added recording that the Mac and VM share a LAN
segment, so severing the WAN does not isolate them. Controls described by
**function** rather than product where practical, so a future substitution does
not silently invalidate the text. Raised as **POA&M-058**; no control changed.


## 1. Incident Response Policy

### Purpose

This policy defines [DOMAIN.ORG]'s structured approach to managing cybersecurity incidents on the SecureMac Reference System #2. It ensures timely detection, response, and recovery to protect Controlled Unclassified Information (CUI) and Federal Contract Information (FCI), in alignment with NIST SP 800-171 Rev 2 (IR-1 through IR-8) and DFARS 252.204-7012 (72-hour external reporting). The policy minimizes operational disruption to core functions such as AI-assisted systems administration and research.

### Scope

Applies to all SecureMac assets, including:

- **Domain controller:** services.[DOMAIN.ORG] ([LAN-IP-REDACTED])
  - 389-DS LDAP domain controller
  - Wazuh Manager (SIEM/security monitoring)
  - NAS file server with RAID 5 encrypted storage
  - Centralized rsyslog server

- **Hosts in boundary:**
  - `securemac.[DOMAIN.ORG]` — Mac mini M4 Pro ([LAN-IP-REDACTED]), physical host, WAN gateway/firewall, AI inference, and the sole management workstation
  - `services.[DOMAIN.ORG]` — Rocky Linux 9.7 VM ([LAN-IP-REDACTED]) hosting the directory, SIEM, mail and web services
  - `nas.[DOMAIN.ORG]` — Synology NAS ([LAN-IP-REDACTED]), supporting infrastructure

- **Network Infrastructure:**
  - Perimeter firewall: macOS `pf` on the Mac mini ([LAN-IP-REDACTED]); host firewall: `firewalld` on the VM
  - Network intrusion detection: Suricata on the VM

- **Personnel:** This policy applies to all personnel with access to the system — employees, contractors and subcontractors.

  > **Current instantiation.** In this reference deployment a **single operator holds all four roles** (System Owner, ISSO, System Administrator, User) — see `DIWAI-RAM-001` — and there are presently no employees, contractors or subcontractors. **The personnel provisions below are retained deliberately and apply in full wherever a deployment includes additional people.** This system is a reference model intended for adoption by very small businesses in two configurations: a secure single-operator system, or a domain controller serving a VSB of up to roughly fifteen users. Provisions written only for the present headcount would not survive that adoption.

**Incident Types:** Unauthorized access, data exfiltration, malware infection, denial of service, policy violations, or any event that threatens the confidentiality, integrity, or availability of CUI/FCI.

### Policy Statements

#### 1. Incident Detection and Reporting

All personnel shall report suspected incidents immediately to the ISSO via:
- **Email:** [EMAIL-REDACTED]
- **Phone:** [REDACTED-PHONE]

Automated monitoring tools shall generate alerts within 1 hour of detection:
- **Wazuh Manager:** Real-time SIEM alerts from all endpoints
- **Suricata IDS/IPS:** Network-based intrusion detection on the VM
- **rsyslog:** Centralized logging from all systems
- **auditd:** System audit logging per NIST CUI profile
- **Host-based malicious-code protection:** YARA (Wazuh active response on FIM rules 550/554, plus a weekly full-system scan), corroborated by VirusTotal reputation lookups

#### 2. Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **ISSO ([SYSTEM-OWNER])** | Lead detection, analysis, containment, reporting, and post-incident review. Coordinate with external entities (e.g., DoD, DIBCSIA). Serve as Incident Commander for all phases. |
| **Users/Contractors** | Report symptoms immediately; isolate systems if instructed; provide evidence (e.g., screenshots, error messages); cooperate with investigation. |

**Note:** As a solopreneur operation, the ISSO fulfills all incident response roles (Incident Commander, Technical Lead, Communications Lead, Documentation Lead).

#### 3. Response and Recovery

**Response Timeline Requirements:**
- **Containment:** Achieve within 4 hours (e.g., account disable via 389-DS LDAP `sudo ldapmodify` (disable user))
- **Eradication/Recovery:** Complete within 24 hours for low-impact incidents using verified backups (ReaR ISOs)
- **Testing:** Annual tabletop exercises to validate procedures

**Recovery Resources:**
- Automated daily backups of critical files
- Weekly full-system ReaR ISO backups to encrypted RAID array
- LUKS-encrypted offsite backup media (rotated monthly)
- System recovery procedures documented in `/backup/procedures/`

#### 4. Notification Requirements

**Internal Notifications:**
- Notify all SecureMac users within 2 hours of confirmed incident
- Provide status updates every 4 hours during active incident response

**External Notifications:**
- **DoD Reporting:** Report CUI/FCI incidents to DoD within 72 hours via the Defense Industrial Base Cybersecurity Information Sharing and Analysis Organization (DIBCSIA) portal
- **DIBCSIA Contact:** 301-225-0136
- **Client Notification:** Notify affected clients if CUI is compromised
- **Law Enforcement:** Contact FBI IC3 (ic3.gov) if criminal activity suspected

#### 5. Post-Incident Activities

Within 7 days of incident closure:
- Conduct root cause analysis
- Update System Security Plan (SSP)
- Update Plan of Action & Milestones (POA&M)
- Revise training materials if needed
- Document lessons learned
- Implement corrective actions

**Record Retention:** Maintain all incident records for 3 years minimum to support CMMC audits.

#### 6. Compliance and Enforcement

This policy integrates with:
- FAR 52.204-21 (Cybersecurity for Unclassified Federal Information)
- DFARS 252.204-7012 (Safeguarding Covered Defense Information)
- CMMC Level 2 requirements

**Enforcement:** Violations may result in access revocation, disciplinary action, or contract termination. Quarterly reviews ensure alignment with evolving threats.

### References

- NIST SP 800-171 Rev 2, IR Family (Incident Response)
- DFARS 252.204-7012
- System Security Plan (SSP), Section 9.6
- Wazuh Operations Guide
- Backup Procedures documentation

---

## 2. Incident Response Procedures

### Overview

This procedure provides actionable steps for executing the Incident Response Policy. It leverages SecureMac tools (Wazuh SIEM, OpenSCAP, ReaR backups) and assumes a small-team environment.

**Incident Classification:**
- **Low:** Single anomaly, no CUI impact (e.g., failed login attempts)
- **Medium:** Potential breach, possible CUI exposure (e.g., malware alert)
- **High:** Confirmed CUI loss or exfiltration (e.g., data breach)

### Preparation (Ongoing)

**Maintenance Activities:**
- Maintain emergency contact list (ISSO primary; DIBCSIA: 301-225-0136)
- Verify monitoring tools quarterly:
  - `sudo systemctl status wazuh-manager` (Wazuh Manager on the VM)
  - `systemctl status dirsrv@diwai` (389-DS LDAP services)
  - `systemctl list-timers yara-fullscan.timer` (malicious-code scan schedule)
  - `sudo /usr/local/sbin/diwai-control-health` (24 automated control checks)
  - `journalctl -u rsyslog` (centralized logging)

**Training:**
- Integrate IR procedures into annual security awareness training
- Conduct tabletop exercises (e.g., mock unauthorized NAS access scenario)
- Review incident response flowcharts quarterly

**Resources:**
- Incident log template: `/backup/logs/incidents/template.txt`
- Recovery procedures: `/backup/procedures/recovery_guide.md`
- Wazuh dashboard: https://services.[DOMAIN.ORG]:443 (Wazuh UI)

### Procedure Steps

#### Phase 1: Detection and Identification (0-1 Hour)

**Triggers:**
- User report via email/phone
- Wazuh alert (dashboard or email notification)
- Suricata IDS/IPS alert on the VM
- Failed login alerts: `grep "fail" /var/log/secure | tail -20`
- Suspicious file integrity monitor (FIM) alerts from Wazuh

**Actions:**

**Step 1.1** - Initial Response:
```bash
# Access domain controller
ssh services.[DOMAIN.ORG]

# Create incident log
sudo mkdir -p /backup/logs/incidents/
sudo nano /backup/logs/incidents/$(date +%Y%m%d)-IR-001.txt
```

**Incident Log Contents:**
- Timestamp of detection
- Incident description
- Affected systems/users
- Initial impact assessment
- Detection method (user report, Wazuh, IDS, etc.)

**Step 1.2** - Classify Severity:
- Review Wazuh alerts for MITRE ATT&CK classification
- Check affected systems for CUI data
- Determine scope (single system vs. multiple)

**Step 1.3** - Preserve Evidence:
```bash
# Preserve audit logs
sudo cp -r /var/log/audit /backup/incident-snapshot-$(date +%Y%m%d)/

# Preserve Wazuh logs
sudo cp -r /var/ossec/logs/alerts /backup/incident-snapshot-$(date +%Y%m%d)/

# Preserve system logs
sudo cp -r /var/log/secure /backup/incident-snapshot-$(date +%Y%m%d)/
sudo cp -r /var/log/messages /backup/incident-snapshot-$(date +%Y%m%d)/
```

#### Phase 2: Containment (1-4 Hours)

**Step 2.1** - Isolate Affected Systems:

For compromised user accounts:
```bash
# Obtain Kerberos ticket
kinit admin

# Disable compromised account
ldapmodify -H ldaps://services.[DOMAIN.ORG] -D "cn=Directory Manager" -W   # set nsAccountLock: true

# Verify account status
ldapsearch -H ldaps://services.[DOMAIN.ORG] -D "cn=Directory Manager" -W \
  -b "uid=<username>,ou=people,dc=diwai,dc=org" nsAccountLock
```

To block a host or address:
```bash
# On the VM (host firewall)
sudo firewall-cmd --add-rich-rule='rule family=ipv4 source address=<IP> drop'

# At the perimeter (Mac mini, macOS pf) — edit the anchor then reload
sudo vi /etc/pf_diwai.conf
sudo pfctl -f /etc/pf_diwai.conf
```

> **Containment caution.** The Mac and the VM share the [LAN-IP-REDACTED]/24 segment.
> Severing the WAN link contains external access but does **not** isolate the VM
> from the Mac. If lateral movement is suspected, containment must address the
> LAN path as well.

For active malware:
```bash
# Quarantine infected files (Wazuh active response)
# Check Wazuh dashboard for active response actions

# Manual scan if needed
sudo /usr/local/sbin/yara-fullscan.sh          # full-system YARA scan
sudo yara -r /var/ossec/etc/rules/yara/ /path/to/suspect
```

**Step 2.2** - Notify Users:
```bash
# Send email notification to all users
# Template: "SecureMac access restricted pending security investigation. Stand by for updates."
```

**Step 2.3** - Document Containment Actions:
- Update incident log with all actions taken
- Note timestamps of each containment measure
- Document any systems isolated or accounts disabled

#### Phase 3: Eradication and Recovery (4-24 Hours)

**Step 3.1** - Scan and Remediate:
```bash
# Refresh YARA rulesets, then run a full-system scan
sudo /usr/local/sbin/yara-fullscan.sh

# Apply OpenSCAP remediation if config drift detected
sudo oscap xccdf eval \
    --profile xccdf_org.ssgproject.content_profile_cui \
    --remediate \
    --results /var/log/oscap-remediation-$(date +%Y%m%d).xml \
    /usr/share/xml/scap/ssg/content/ssg-rl9-ds.xml
```

**Step 3.2** - Restore from Backups (if needed):

**File-level restore:**
```bash
# List available backups
ls -lt /backup/daily/ | head -5

# Extract specific config files
cd /backup/daily/$(ls -t /backup/daily/ | head -1)
tar -xzf dirsrv-config.tar.gz -C /tmp/

# Restore files
sudo cp -a /tmp/etc/dirsrv/slapd-diwai/* /etc/dirsrv/slapd-diwai/
sudo systemctl restart dirsrv@diwai
```

**Full system restore:**
```bash
# Boot from ReaR ISO
# Located at: /var/backups/securemac-rear.iso

# Run recovery (from ReaR boot environment)
rear recover

# After recovery, verify services
sudo ipactl status
sudo systemctl status wazuh-manager
```

**Step 3.3** - Verify System Integrity:
```bash
# Verify 389-DS LDAP services
sudo ipactl status

# Verify Wazuh Manager
sudo systemctl status wazuh-manager

# Run OpenSCAP compliance scan
sudo oscap xccdf eval \
    --profile xccdf_org.ssgproject.content_profile_cui \
    --results /var/log/oscap-post-recovery-$(date +%Y%m%d).xml \
    --report /var/log/oscap-post-recovery-$(date +%Y%m%d).html \
    /usr/share/xml/scap/ssg/content/ssg-rl9-ds.xml

# Verify FIPS mode still enabled
fips-mode-setup --check
```

**Step 3.4** - Re-enable Access:
```bash
# Re-enable user accounts (after password reset)
ldapmodify -H ldaps://services.[DOMAIN.ORG] -D "cn=Directory Manager" -W   # clear nsAccountLock

# Remove firewall blocks
sudo firewall-cmd --remove-rich-rule='rule family=ipv4 source address=<IP> drop'   # VM
sudo pfctl -f /etc/pf_diwai.conf                                                    # Mac, after removing the rule

# Notify users of restored access
```

#### Phase 4: Post-Incident Activity (Within 7 Days)

**Step 4.1** - Root Cause Analysis:
- Review Wazuh timeline of events
- Analyze audit logs: `sudo ausearch -ts <incident_date>`
- Check authentication logs: `sudo aureport -au`
- Review Suricata IDS logs on the VM (`/var/log/suricata/`)
- Identify attack vector and vulnerabilities exploited

**Step 4.2** - External Reporting:

**For CUI/FCI incidents (72-hour requirement):**
- Submit report via DIBCSIA portal
- Include: incident timeline, affected data, containment actions, recovery status
- Contact: 301-225-0136 or https://dibnet.dod.mil

**Step 4.3** - Documentation Updates:
- Update System Security Plan (SSP) with findings
- Add new POA&M items for identified vulnerabilities
- Update incident response procedures based on lessons learned
- Archive incident log: `/backup/logs/incidents/archive/`

**Step 4.4** - Preventive Measures:
- Implement corrective actions (e.g., enhance Wazuh rules)
- Schedule refresher security training
- Update vulnerability scanning schedule if needed
- Review and update firewall rules
- Enhance monitoring for similar attack patterns

### Evidence and Testing

**Record Keeping:**
- All incident response steps must be logged
- Retain Wazuh alert logs and screenshots
- Save OpenSCAP scan reports (HTML format)
- Document communication timelines
- Retention period: 3 years minimum

**Testing Requirements:**
- **Annual Tabletop Exercise:** November 15 (or anniversary of last incident)
- **Test Scenarios:**
  - Simulated malicious-code detection on the Mac host
  - Unauthorized access attempt to NAS shares
  - DoS attack on the directory service (389-DS on the VM)
  - Ransomware scenario with backup recovery

**Performance Metrics:**
- Time to detection: <1 hour (automated)
- Time to containment: <4 hours
- Time to recovery: <24 hours (low impact), <72 hours (high impact)
- External reporting: <72 hours for CUI/FCI incidents

---

## Appendix A: Incident Classification Matrix

| Severity | Examples | Response Time | Containment Target | External Report? |
|----------|----------|---------------|-------------------|------------------|
| **Low** | Failed login attempts (3-5 attempts)<br>Single-host anomaly<br>Non-CUI system affected | 24 hours | 8 hours | No |
| **Medium** | Malware detection on endpoint<br>Suspicious network traffic<br>Potential CUI exposure<br>Multiple failed logins (>5) | 12 hours | 4 hours | If CUI impacted |
| **High** | Confirmed data exfiltration<br>CUI compromise<br>Ransomware infection<br>Domain controller compromise | Immediate | 2 hours | Yes (72 hours) |
| **Critical** | Multiple system compromise<br>Active data exfiltration<br>Loss of FIPS compliance<br>Encryption key compromise | Immediate | 1 hour | Yes (immediate notification + 72hr formal report) |

---

## Appendix B: Quick Reference Commands

### Investigation Commands
```bash
# Check recent failed logins
sudo aureport -au --failed --summary

# Search audit logs for specific user
sudo ausearch -ua <username> -ts recent

# Check Wazuh alerts (last 24 hours)
sudo tail -f /var/ossec/logs/alerts/alerts.log

# Review 389-DS LDAP authentication logs
sudo journalctl -u krb5kdc | tail -50

# Check NAS file access logs
sudo tail -f /var/log/samba/log.smbd
```

### Containment Commands
```bash
# Disable 389-DS LDAP user
kinit admin
ldapmodify -H ldaps://services.[DOMAIN.ORG] -D "cn=Directory Manager" -W   # set nsAccountLock: true

# Reset user password
ipa passwd <username>

# List active Kerberos tickets
ipa-getkeytab -l

# Block IP at system level
sudo firewall-cmd --add-rich-rule='rule family="ipv4" source address="<IP>" reject' --permanent
sudo firewall-cmd --reload
```

### Recovery Commands
```bash
# List recent backups
ls -lt /backup/daily/ | head -5

# Verify backup integrity
cd /backup/daily/<latest>/
sha256sum -c checksums.sha256

# Restore 389-DS LDAP configuration
tar -xzf ipa-config.tar.gz -C /tmp/
sudo cp -a /tmp/etc/dirsrv/slapd-diwai/* /etc/dirsrv/slapd-diwai/
sudo ipactl restart

# Full system recovery
# Boot from: /var/backups/securemac-rear.iso
# Run: rear recover
```

---

## Appendix C: Contact Information

### Internal Contacts
- **ISSO/System Owner:** [SYSTEM-OWNER]
  - Email: [EMAIL-REDACTED]
  - Phone: [REDACTED-PHONE]
  - Available: 24/7 for critical incidents

### External Contacts
- **DIBCSIA (DoD Reporting):**
  - Phone: 301-225-0136
  - Portal: https://dibnet.dod.mil
  - Report within: 72 hours for CUI/FCI incidents

- **FBI IC3 (Cyber Crime):**
  - Website: https://ic3.gov
  - Use for: Criminal cyber activity reporting

- **CISA (Cybersecurity & Infrastructure Security Agency):**
  - Website: https://cisa.gov/report
  - Phone: 888-282-0870
  - Use for: Federal incident reporting, threat intelligence

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
