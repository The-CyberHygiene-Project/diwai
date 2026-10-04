> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# INCIDENT RESPONSE PLAN
**Organization:** [DOMAIN.ORG] (Do It With AI)
**System:** SecureMac Reference System #2 ([DOMAIN.ORG])
**Version:** 1.0 - APPROVED
**Effective Date:** December 22, 2025
**Classification:** CONTROLLED UNCLASSIFIED INFORMATION (CUI)

**NIST Controls:** IR-1, IR-4, IR-5, IR-6, IR-7, IR-8

---

## DOCUMENT CONTROL

| Name / Title | Role | Signature / Date |
|---|---|---|
| [SYSTEM-OWNER]<br>Owner/Principal | System Owner | APPROVED<br>Date: December 22, 2025 |
| [SYSTEM-OWNER]<br>Owner/Principal | ISSO / Incident Response Coordinator | APPROVED<br>Date: December 22, 2025 |

**Review Schedule:** Annually or after significant incident
**Next Review Date:** December 22, 2026

---

## 1. PURPOSE AND SCOPE

### 1.1 Purpose
This Incident Response Plan (IRP) establishes procedures for detecting, responding to, reporting, and recovering from cybersecurity incidents affecting [DOMAIN.ORG]'s SecureMac Reference System #2. This plan ensures compliance with NIST SP 800-171 incident response requirements and DFARS 252.204-7012 cyber incident reporting obligations.

### 1.2 Scope
This plan applies to:
- All systems within the [DOMAIN.ORG] domain
- Domain controller (services.[DOMAIN.ORG])
- All workstations (mac-mini.[DOMAIN.ORG])
- Network infrastructure (pfSense firewall)
- All data classified as CUI or FCI
- System owner and authorized users

### 1.3 Incident Definition
A cybersecurity incident is any event that:
- Compromises confidentiality, integrity, or availability of CUI/FCI
- Represents an actual or suspected violation of security policies
- Results in unauthorized access to systems or data
- Involves malware infection or attempted infection
- Represents a denial of service or system compromise
- Involves theft or loss of CUI-containing devices or media

---

## 2. INCIDENT RESPONSE TEAM

### 2.1 Team Structure
For a single-person organization, the Incident Response Team consists of:

**Incident Response Coordinator:** [SYSTEM-OWNER]
- Primary responsibility for all incident response activities
- Detection, analysis, containment, eradication, recovery
- External notifications and reporting
- Documentation and lessons learned

**External Resources:**
- FBI Cyber Division (for significant incidents)
- DoD Cyber Crime Center (DC3) (for defense-related incidents)
- SSL.com Support (certificate-related incidents)
- Rocky Linux Security Team (OS vulnerabilities)
- Local law enforcement (physical security incidents)

### 2.2 Contact Information

**Internal Contact:**
- Name: [SYSTEM-OWNER]
- Title: Owner/Principal, ISSO
- Phone: [PHONE-REDACTED]
- Email: [EMAIL-REDACTED]

**External Emergency Contacts:**

**FBI Cyber Division:**
- Phone: 1-855-292-3937 (1-855-CYBER-37)
- Email: [EMAIL-REDACTED]
- Website: https://www.ic3.gov

**DoD Cyber Crime Center (DC3):**
- Defense Industrial Base (DIB) Cybersecurity Program
- Phone: 410-981-0096
- Email: [EMAIL-REDACTED]
- Portal: https://dibnet.dod.mil

**US-CERT (CISA):**
- Phone: 1-888-282-0870
- Email: [EMAIL-REDACTED]
- Website: https://www.us-cert.gov

**Rocky Linux Security:**
- Email: [EMAIL-REDACTED]
- Mailing List: [EMAIL-REDACTED]

---

## 3. INCIDENT CATEGORIES AND SEVERITY

### 3.1 Incident Categories

**Category 1: Unauthorized Access**
- Successful intrusion into systems or networks
- Unauthorized privilege escalation
- Account compromise or credential theft
- Unauthorized access to CUI/FCI data

**Category 2: Malware**
- Virus, worm, or trojan detection
- Ransomware infection
- Rootkit or backdoor installation
- Potentially unwanted programs (PUPs)

**Category 3: Denial of Service**
- Network or system unavailability
- Resource exhaustion attacks
- Distributed denial of service (DDoS)
- Service degradation

**Category 4: Data Breach**
- CUI/FCI data exfiltration
- Unauthorized disclosure of sensitive information
- Loss or theft of devices containing CUI
- Improper data disposal

**Category 5: Physical Security**
- Unauthorized physical access to facilities
- Theft or loss of equipment
- Damage to systems or infrastructure
- Environmental incidents (fire, flood, power)

**Category 6: Policy Violation**
- Insider threat activities
- Unauthorized software installation
- Policy circumvention attempts
- Misuse of systems or resources

### 3.2 Severity Levels

**CRITICAL (P1) - Immediate Response Required**
- Active data breach involving CUI/FCI exfiltration
- Ransomware infection with data encryption
- Complete system compromise or takeover
- Widespread malware outbreak
- **Response Time:** Immediate (within 15 minutes)
- **Reporting:** Within 72 hours to DoD (DFARS requirement)

**HIGH (P2) - Urgent Response Required**
- Confirmed unauthorized access to systems
- Suspected CUI/FCI data compromise
- Significant service disruption
- Multiple system malware infections
- **Response Time:** Within 1 hour
- **Reporting:** Within 72-96 hours as appropriate

**MEDIUM (P3) - Prompt Response Required**
- Attempted unauthorized access (blocked)
- Single system malware infection (contained)
- Policy violations with security impact
- Suspicious activity requiring investigation
- **Response Time:** Within 4 hours
- **Reporting:** Per normal procedures

**LOW (P4) - Standard Response**
- Failed login attempts (normal threshold)
- Blocked malware attempts
- Minor policy violations
- Routine security alerts
- **Response Time:** Within 24 hours
- **Reporting:** Document in logs only

---

## 4. INCIDENT RESPONSE PROCESS

### 4.1 Phase 1: PREPARATION

**Ongoing Activities:**
- [ ] Maintain Wazuh SIEM monitoring operational 24/7
- [ ] Keep vulnerability signatures updated (hourly)
- [ ] Maintain current system backups (daily + weekly)
- [ ] Review security alerts daily
- [ ] Keep incident response kit ready (forensic tools, contact lists)
- [ ] Maintain evidence storage (USB drives, external storage)
- [ ] Keep offline copies of critical documentation
- [ ] Test backup restoration procedures monthly

**Incident Response Tools:**
- Wazuh SIEM/XDR for detection and monitoring
- Audit logs: /var/log/audit/audit.log
- System logs: journalctl
- Network capture: tcpdump, Wireshark
- Forensic imaging: dd, dc3dd
- Hash verification: sha256sum
- 389-DS LDAP logs: /var/log/dirsrv/

### 4.2 Phase 2: DETECTION AND ANALYSIS

**Detection Sources:**
1. **Wazuh SIEM Alerts**
   - High/critical severity alerts require immediate review
   - File integrity monitoring alerts
   - Malware detection alerts
   - Authentication failure patterns
   - Vulnerability detection alerts

2. **System Monitoring**
   - Unusual CPU/memory/network usage
   - Unexpected processes or services
   - Unauthorized scheduled tasks
   - Suspicious file modifications

3. **User Reports**
   - Unusual system behavior
   - Suspicious emails or phishing attempts
   - Lost or stolen devices
   - Observed policy violations

**Initial Analysis Checklist:**
- [ ] Identify incident category and severity level
- [ ] Document initial indicators of compromise (IOCs)
- [ ] Determine affected systems and scope
- [ ] Assess potential impact to CUI/FCI data
- [ ] Begin incident log and timeline
- [ ] Preserve volatile evidence if needed
- [ ] Escalate to appropriate severity level

**Incident Log Template:**
```
Incident ID: IR-{DOD|GSA|FBI}-YYYYMMDD-NNN
Detection Time: [Date/Time]
Reported By: [Source]
Category: [Category]
Severity: [P1/P2/P3/P4]
Affected Systems: [List]
Initial Description: [Brief summary]
```

> **Note:** Use the admin portal IR report forms at `https://securemac.[DOMAIN.ORG]/docs/` to generate pre-populated incident reports with the correct ID format for each reporting authority (DoD/GSA/FBI).

### 4.3 Phase 3: CONTAINMENT

**Short-Term Containment (Immediate Actions):**

**For Malware Infections:**
- [ ] Isolate infected system from network
  ```bash
  sudo ip link set <interface> down
  ```
- [ ] Kill malicious processes if identified
- [ ] Block malicious IPs at firewall
- [ ] Disable compromised user accounts
  ```bash
  sudo ldapmodify -Y EXTERNAL -H ldapi://%2Frun%2Fslapd-diwai.socket <<EOF
  dn: uid=<username>,ou=people,dc=diwai,dc=org
  changetype: modify
  replace: nsAccountLock
  nsAccountLock: TRUE
  EOF
  ```
- [ ] Take memory dump if needed for forensics
- [ ] Document all containment actions with timestamps

**For Unauthorized Access:**
- [ ] Force password resets for affected accounts
  ```bash
  sudo ldappasswd -Y EXTERNAL -H ldapi://%2Frun%2Fslapd-diwai.socket \
    -s '<new-temp-password>' 'uid=<username>,ou=people,dc=diwai,dc=org'
  ```
- [ ] Block source IP addresses at firewall
- [ ] Review and close unauthorized access paths
- [ ] Enable additional logging if needed

**For Data Breach:**
- [ ] Identify scope of compromised data
- [ ] Preserve evidence of exfiltration
- [ ] Document affected CUI/FCI datasets
- [ ] Notify appropriate authorities (DoD within 72 hours)
- [ ] Assess notification requirements for affected parties

**Long-Term Containment:**
- [ ] Apply temporary security patches or workarounds
- [ ] Implement compensating controls
- [ ] Segment affected systems on separate VLAN if needed
- [ ] Increase monitoring and logging on affected systems
- [ ] Prepare for system rebuild if compromise severe

### 4.4 Phase 4: ERADICATION

**Malware Eradication:**
- [ ] Identify and remove all malware components
- [ ] Scan all systems with updated AV definitions
- [ ] Remove backdoors, rootkits, or persistence mechanisms
- [ ] Clean or reimage affected systems
- [ ] Verify eradication with multiple tools
- [ ] Check for lateral movement to other systems

**Access Restoration:**
- [ ] Close all unauthorized access paths
- [ ] Remove unauthorized user accounts
- [ ] Reset passwords for all potentially compromised accounts
- [ ] Revoke and reissue certificates if needed
- [ ] Patch vulnerabilities that enabled access
- [ ] Review and update firewall rules

**Verification:**
- [ ] Run full system scans (ClamAV, YARA)
- [ ] Verify file integrity (FIM baseline check)
- [ ] Review audit logs for residual activity
- [ ] Check for new IOCs or suspicious activity
- [ ] Confirm clean bill of health before restoration

### 4.5 Phase 5: RECOVERY

**System Restoration Process:**
1. **Verify Eradication Complete**
   - [ ] All malware removed
   - [ ] Vulnerabilities patched
   - [ ] Clean system validation

2. **Restore from Backup (if needed)**
   ```bash
   # Restore system files from last known clean backup
   sudo restic restore latest --target /

   # Or restore a specific snapshot by ID
   sudo restic snapshots          # list available snapshots
   sudo restic restore <snap-id> --target /
   ```

3. **System Hardening**
   - [ ] Apply all security updates
   - [ ] Run OpenSCAP remediation
   - [ ] Verify FIPS mode enabled
   - [ ] Update firewall rules
   - [ ] Enable enhanced logging

4. **Service Restoration**
   - [ ] Bring systems back online gradually
   - [ ] Monitor for suspicious activity
   - [ ] Verify functionality of all services
   - [ ] Test authentication and access controls
   - [ ] Confirm data integrity

5. **Enhanced Monitoring**
   - [ ] Increase Wazuh alert sensitivity temporarily
   - [ ] Review logs frequently for 30 days
   - [ ] Watch for reinfection or continued IOCs
   - [ ] Document system behavior baseline

**Return to Operations Approval:**
- [ ] All eradication verification complete
- [ ] System functionality validated
- [ ] Enhanced monitoring in place
- [ ] Incident documentation complete
- [ ] Sign-off by System Owner

### 4.6 Phase 6: POST-INCIDENT ACTIVITY

**Lessons Learned Meeting:**
Conduct within 7 days of incident closure.

**Discussion Topics:**
1. What happened and when was it detected?
2. How well did staff and procedures work?
3. What information was needed sooner?
4. Were any actions taken that might have inhibited recovery?
5. What would we do differently next time?
6. How can we prevent similar incidents?
7. What corrective actions are needed?

**Documentation Requirements:**
- [ ] Complete incident report with timeline
- [ ] Document all indicators of compromise (IOCs)
- [ ] Preserve forensic evidence (if applicable)
- [ ] Record all actions taken and by whom
- [ ] Document root cause analysis
- [ ] List corrective actions and responsible parties
- [ ] Update incident response procedures if needed
- [ ] Share IOCs with security community (anonymized)

**Corrective Actions:**
- [ ] Update security controls
- [ ] Apply additional patches
- [ ] Revise policies or procedures
- [ ] Implement new monitoring rules
- [ ] Update training materials
- [ ] Schedule follow-up reviews

---

## 5. EXTERNAL REPORTING REQUIREMENTS

> **Admin Portal:** Use the pre-populated IR report forms at `https://securemac.[DOMAIN.ORG]/docs/` (Incident Reporting section) to generate, review, and email reports to each authority. Forms auto-populate system owner, IP addresses, hostnames, and OS details.

### 5.1 DoD — DFARS 252.204-7012 Reporting

**When Required:**
Cyber incidents affecting covered defense information (CDI) or affecting contractor's ability to perform on a DoD contract.

**Reporting Timeline:** Within **72 hours** of discovery

**Reporting Method:**
- Primary: DoD Cyber Crime Center (DC3) portal at https://dibnet.dod.mil
- Notify contracting officer (CO) simultaneously
- Use the **DoD Incident Report** form in the admin portal to generate a pre-populated report

**Key Fields Required:**
- Contractor name, CAGE code, and POC contact
- Contract number(s) affected and contracting activity
- Date/time of discovery; incident type; systems and data affected
- Impact assessment (scope, data at risk, operational impact)
- Containment and mitigation actions taken

**Incident ID format:** `IR-DOD-YYYYMMDD-NNN`

### 5.2 GSA — FISMA / GSA CIO P 2100.1 Reporting

**When Required:**
Incidents involving GSA contract work, GSA systems, or GSA-handled CUI/FCI.

**Reporting Timeline:**
- **CAT 1–3** (Unauthorized Access, Malicious Code, Improper Usage at high severity): Within **1 hour**
- **CAT 4–7** (Scans/Probes, Misuse, Investigation, Exercises): Within **24 hours**

**GSA Incident Categories:**
| CAT | Type | Deadline |
|-----|------|----------|
| 1 | Unauthorized Access | 1 hour |
| 2 | Denial of Service | 1 hour |
| 3 | Malicious Code | 1 hour |
| 4 | Improper Usage | 24 hours |
| 5 | Scans/Probes/Attempted Access | 24 hours |
| 6 | Investigation | 24 hours |
| 7 | Explain Anomaly | 24 hours |

**Reporting Method:**
- Email GSA SecOps: [EMAIL-REDACTED] (CC: contracting officer)
- Use the **GSA FISMA Incident Report** form in the admin portal

**Incident ID format:** `IR-GSA-YYYYMMDD-NNN`

### 5.3 FBI — Serious Incidents / CyWatch

**When Required:**
- Ransomware or extortion attempts
- Nation-state or advanced persistent threat (APT) activity
- Significant financial fraud or business email compromise
- Incidents with potential for criminal prosecution

**Reporting Method:**
- **Phone:** 1-855-292-3937 (1-855-CYBER-37) — 24/7
- **Email:** [EMAIL-REDACTED]
- **Online:** https://www.ic3.gov (Internet Crime Complaint Center)
- Use the **FBI CyWatch Incident Report** form in the admin portal

**Incident ID format:** `IR-FBI-YYYYMMDD-NNN`

### 5.4 US-CERT / CISA

**When Required:**
- Significant incidents affecting critical infrastructure
- Novel attack methods or widespread vulnerabilities

**Reporting Method:**
- Phone: 1-888-282-0870
- Email: [EMAIL-REDACTED]

---

## 6. EVIDENCE PRESERVATION

### 6.1 Digital Evidence Handling

**Chain of Custody Requirements:**
- Document who collected evidence, when, and how
- Maintain evidence in secured location
- Limit access to authorized personnel only
- Use write-blockers for disk imaging
- Generate and document hash values
- Preserve original evidence, work with copies

**Evidence Collection Procedures:**

**1. Volatile Data (capture before system shutdown):**
```bash
# Memory dump
sudo dd if=/dev/mem of=/evidence/memory-$(hostname)-$(date +%Y%m%d-%H%M%S).img

# Network connections
sudo ss -tulpn > /evidence/network-connections.txt

# Running processes
ps auxww > /evidence/processes.txt

# Logged in users
who -a > /evidence/users.txt
```

**2. Non-Volatile Data:**
```bash
# Disk imaging (use write blocker)
sudo dd if=/dev/sda of=/evidence/disk-image.img bs=4M conv=noerror,sync
sha256sum /evidence/disk-image.img > /evidence/disk-image.img.sha256

# Log files
sudo tar -czf /evidence/logs-$(hostname)-$(date +%Y%m%d).tar.gz /var/log/
```

**3. Evidence Documentation:**
- Date and time of collection
- System name and IP address
- Person who collected evidence
- Tools and methods used
- Hash values for integrity verification
- Storage location and access control

### 6.2 Evidence Retention

**Retention Period:**
- All incident evidence: 3 years minimum
- Evidence for ongoing legal/regulatory matters: Until case resolved
- High-severity incidents: 7 years

**Storage Requirements:**
- Encrypted storage media
- Access logs maintained
- Multiple copies (on-site + off-site)
- Regular integrity checks

---

## 7. COMMUNICATION PLAN

### 7.1 Internal Communications

**Incident Notification:**
Since this is a single-person organization, formal internal notification is not required. However, maintain detailed incident log for own reference and auditing.

### 7.2 External Communications

**Customer Notification (if CUI/FCI compromised):**
- Determine contractual notification requirements
- Coordinate with customer's security team
- Provide factual, timely updates
- Document all customer communications

**Regulatory Authorities:**
- DoD: Within 72 hours (DFARS requirement)
- FBI: For significant criminal activity
- US-CERT: For novel or widespread threats

**Vendors/Partners:**
- Notify if their systems potentially affected
- Share threat indicators (anonymized)
- Request assistance if needed

**Public Communications:**
- Generally not required for small business
- Consult legal counsel before public disclosure
- Coordinate with law enforcement if investigation ongoing

---

## 8. SPECIFIC INCIDENT SCENARIOS

### 8.1 Ransomware Attack

**Immediate Actions:**
1. Isolate infected systems immediately
2. Do NOT pay ransom
3. Identify ransomware variant (Wazuh alerts)
4. Check for decryption tools available
5. Restore from last clean backup
6. Report to FBI via IC3

**Prevention:**
- Daily backups with offline copies
- User training on phishing
- Email filtering and web filtering
- Restrict PowerShell execution
- Application whitelisting

### 8.2 Phishing / Social Engineering

**Response:**
1. Mark email as phishing in email client
2. Report to email provider
3. Check if any links clicked or files downloaded
4. Scan system for malware
5. Reset passwords if credentials entered
6. Report to FBI IC3 if financial loss

**Prevention:**
- Security awareness training
- Email filtering (SPF, DKIM, DMARC)
- Multi-factor authentication
- User verification before sensitive actions

### 8.3 Lost or Stolen Device

**Response:**
1. Report to local law enforcement
2. Remotely wipe device if capability exists
3. Disable user accounts associated with device
4. Revoke certificates
5. Assess CUI/FCI data on device
6. Notify DoD if CDI/CUI was on device
7. Report to FBI if device contained classified info

**Prevention:**
- Full disk encryption (LUKS) on all devices
- Strong authentication
- Auto-lock screens
- Remote wipe capability
- Data minimization on mobile devices

### 8.4 Insider Threat

**Response:**
1. Document all suspicious activity
2. Preserve evidence before confrontation
3. Disable account access immediately if termination
4. Review audit logs for extent of activity
5. Assess data accessed or exfiltrated
6. Report to law enforcement if criminal

**Prevention:**
- Principle of least privilege
- Separation of duties (where possible)
- Audit logging and review
- Background checks
- Exit procedures and access termination

### 8.5 Vulnerability Exploitation

**Response:**
1. Identify affected systems
2. Apply emergency patch or workaround
3. Check for exploitation in logs
4. Search for IOCs of successful exploit
5. Increase monitoring on affected systems

**Prevention:**
- Automated patching (dnf-automatic)
- Vulnerability scanning (Wazuh)
- Network segmentation
- Intrusion detection

---

## 9. TRAINING AND TESTING

### 9.1 Training Requirements

**Annual Training:**
- Incident response procedures review
- Roles and responsibilities
- Reporting requirements
- Evidence handling procedures
- Communication protocols

**Next Training Date:** November 1, 2026

### 9.2 Plan Testing

**Tabletop Exercises:**
- Frequency: Semi-annually
- Scenario-based walk-through of procedures
- Identify gaps or improvements needed
- Update plan based on findings

**Next Exercise:** May 1, 2026

**Testing Scenarios:**
1. Ransomware infection scenario
2. Data breach via phishing
3. Lost device with CUI
4. Insider threat investigation
5. Zero-day vulnerability exploitation

---

## 10. PLAN MAINTENANCE

**Review Schedule:**
- Annual review (minimum)
- After significant incidents
- After major system changes
- After regulatory changes
- After testing exercises

**Update Triggers:**
- New systems or services deployed
- Changes to external requirements
- Lessons learned from incidents
- Testing identifies gaps
- Contact information changes

**Version Control:**
| Version | Date | Changes | Author |
|---|---|---|---|
| 1.0 | Nov 1, 2025 | Initial release | [SYSTEM-OWNER] |
|  |  |  |  |
|  |  |  |  |

---

## APPENDIX A: INCIDENT SEVERITY MATRIX

| Factor | Critical (P1) | High (P2) | Medium (P3) | Low (P4) |
|---|---|---|---|---|
| **CUI/FCI Impact** | Confirmed exfiltration | Potential compromise | Attempted access | No impact |
| **System Impact** | Multiple systems down | Single system down | Degraded service | No impact |
| **Data Impact** | Data destroyed/encrypted | Data modified | Data accessed | No impact |
| **Scope** | Enterprise-wide | Multiple systems | Single system | Isolated |
| **Response Time** | Immediate (15 min) | 1 hour | 4 hours | 24 hours |
| **Reporting** | DoD + FBI (72 hrs) | DoD (72-96 hrs) | Internal | Logs only |

---

## APPENDIX B: INCIDENT RESPONSE CONTACT CARD

**Print and keep near workstation:**

```
┌──────────────────────────────────────────────────────┐
│        INCIDENT RESPONSE QUICK REFERENCE             │
├──────────────────────────────────────────────────────┤
│ INTERNAL CONTACT:                                    │
│   [SYSTEM-OWNER]: [PHONE-REDACTED]                       │
│   [EMAIL-REDACTED]                               │
│                                                      │
│ DoD REPORT (72 hr):  dibnet.dod.mil                  │
│   DC3: 410-981-0096  [EMAIL-REDACTED]                  │
│                                                      │
│ GSA REPORT (1/24 hr): [EMAIL-REDACTED]             │
│                                                      │
│ FBI CYWATCH: 1-855-292-3937  [EMAIL-REDACTED]         │
│   IC3 online: ic3.gov                                │
│                                                      │
│ US-CERT/CISA: 1-888-282-0870  [EMAIL-REDACTED]    │
│                                                      │
│ ADMIN PORTAL FORMS: securemac.[DOMAIN.ORG]/docs/        │
│   (pre-populated DoD / GSA / FBI report templates)  │
│                                                      │
│ CRITICAL INCIDENT STEPS:                             │
│  1. Isolate affected system                         │
│  2. Document incident — use portal IR form          │
│  3. Preserve evidence                               │
│  4. Report per deadline:                            │
│     DoD CUI/CDI → 72 hr                             │
│     GSA CAT1-3  → 1 hr  | CAT4-7 → 24 hr           │
│     FBI serious → immediately                       │
│  5. Complete containment & recovery                 │
└──────────────────────────────────────────────────────┘
```

---

## APPENDIX C: INCIDENT REPORT FORMS

Incident report templates are maintained as interactive forms in the SecureMac admin portal. Access them at:

**`https://securemac.[DOMAIN.ORG]/docs/`** → Incident Reporting section

Three pre-populated forms are available, one per reporting authority:

| Form | Authority | Deadline | Incident ID Format |
|------|-----------|----------|--------------------|
| **DoD Incident Report** | DC3 / DIBNet (DFARS 252.204-7012) | 72 hours | `IR-DOD-YYYYMMDD-NNN` |
| **GSA FISMA Incident Report** | GSA SecOps / Contracting Officer | 1 hr (CAT 1–3) / 24 hr (CAT 4–7) | `IR-GSA-YYYYMMDD-NNN` |
| **FBI CyWatch Incident Report** | FBI CyWatch / IC3 | Immediately (serious incidents) | `IR-FBI-YYYYMMDD-NNN` |

Each form auto-populates:
- System owner name, title, and contact information
- Organization name and domain
- System names and IP addresses (services.[DOMAIN.ORG], nas.[DOMAIN.ORG])
- Host OS and FIPS status
- Auto-generated incident ID with today's date

After completing the form narrative fields, use:
- **Email** button — opens a pre-addressed email with the report in the body
- **Copy to Clipboard** — copies the report for pasting into DIBNet or IC3 web forms

**Incident log:** Record the Incident ID, date reported, and reporting authority in the Version Control table in Section 10 of this plan for each incident filed.

---

**END OF INCIDENT RESPONSE PLAN**

---
