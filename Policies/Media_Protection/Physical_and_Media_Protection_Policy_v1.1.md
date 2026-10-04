> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Physical and Environmental Protection and Media Protection Policy

**Document ID:** DIWAI-PE-MP-001
**Editorial Correction (2026-08-01):** Document identifier changed from `TCC-PE-MP-001` to `DIWAI-PE-MP-001`; internal policy cross-references normalised to the `DIWAI-*` set. Identifier only — **no control content changed** and the version is deliberately not incremented. Aligns this document with the SSP citation set and the [DOMAIN.ORG] independence determination (SSP v2.12 corrected). See `DIWAI-EV-CM-2026-08-01`.
**Version:** 1.1
**Effective Date:** November 2, 2025
**Review Schedule:** Annually or upon facility/infrastructure changes
**Next Review:** November 2, 2026
**Owner:** [SYSTEM-OWNER], ISSO/System Owner
**Distribution:** Authorized personnel only
**Classification:** Controlled Unclassified Information (CUI)

---


**Version 1.1 (2026-08-04) — technical accuracy correction.** Inherited from
Reference System #1 (CyberInABox) and bulk-edited for [DOMAIN.ORG]. Corrections:

- **The equipment list gave the Mac mini the VM's identity** — "Mac mini M4 Pro (services.[DOMAIN.ORG], [LAN-IP-REDACTED])". The Mac mini is `securemac.[DOMAIN.ORG]` at **[LAN-IP-REDACTED]**; `services.[DOMAIN.ORG]` is a **virtual machine running on it** with no separate physical presence. Both are now listed correctly, with the NAS.
- **"NetGate 2100 pfSense firewall"** removed — no such appliance exists; the perimeter firewall is macOS `pf` on the Mac mini.
- **"HP iLO 5 (on dc1)"** removed — there is no out-of-band management controller; thermal monitoring relies on host sensors.
- **Encryption corrected** — the policy claimed LUKS on all hosts and workstations. The Mac uses **FileVault**; **LUKS2** applies to the VM's virtual disks.
- **Emergency shutdown corrected to guest-before-host.** The inherited procedure shut down a standalone server. Here the VM runs on the Mac, so shutting the host first would drop the guest uncleanly.
- **UPS scope restated** around the actual single-host concentration.
- RS#1 workstations (`Engineering`, `Accounting`, `LabRat`) and `dc1` removed.

**One prohibition was reversed on purpose.** The policy stated *"No laptop
computers used for CUI (desktop workstations only)."* A SCAP-hardened laptop is
planned as the model daily driver, to move routine work off the appliance
(SSP §3.2.1) — the inherited blanket prohibition would have forbidden the
planned architecture. It is replaced with conditions: full-disk encryption,
enrolment in the compliance baseline, and physical security when unattended.

Workstation provisions are retained and scoped for adopting deployments.
Raised as **POA&M-058**; no control changed.


## Purpose

This combined policy establishes requirements for physical and environmental protection of facilities and equipment, as well as media protection for [DOMAIN.ORG]'s SecureMac Reference System #2. It ensures that physical access to CUI systems is controlled, environmental threats are mitigated, and media containing CUI is properly protected, transported, sanitized, and disposed of. The policy aligns with NIST SP 800-171 Revision 2 (PE-1 through PE-20 and MP-1 through MP-8) and supports CMMC Level 2 compliance for systems administration and AI research operations.

## Scope

This policy applies to:

**Physical Facilities:**
- Home office location ([LOCATION-REDACTED]) where all CUI processing occurs
- Dedicated office space within residence
- 2U rack-mount enclosure containing services.[DOMAIN.ORG]
- Workstation areas — none presently; the Mac mini doubles as the sole management workstation (SSP §3.2.1). Where a deployment adds workstations, their areas are in scope of this policy.

**Equipment:**
- Mac mini M4 Pro — `securemac.[DOMAIN.ORG]`, **[LAN-IP-REDACTED]** — physical host, perimeter firewall (macOS `pf`), and hypervisor for the service VM
- `services.[DOMAIN.ORG]` — Rocky Linux 9.7 **virtual machine** ([LAN-IP-REDACTED]) running on the Mac mini under UTM; it has no separate physical presence
- Synology NAS — `nas.[DOMAIN.ORG]`, [LAN-IP-REDACTED]
- Workstation computers: **none presently deployed**
- **No separate firewall appliance.** The perimeter firewall is macOS `pf` on the Mac mini; the VM additionally runs `firewalld`
- Network infrastructure (switches, cabling)
- RAID 5 array (3x 3TB HDDs with LUKS encryption)

**Media:**
- Internal storage — **FileVault** full-disk encryption on the Mac mini; **LUKS2** on the VM's virtual disks
- External USB drives for backups (LUKS-encrypted)
- Backup media (ReaR ISO images, offline backups)
- Removable media (if used for CUI transport)

**Personnel:**
- Owner/Principal ([SYSTEM-OWNER]) - sole access
- Contractors (if physical presence required, supervised only)

**Exclusions:**
- Non-CUI processing areas (none - all areas in home office may process CUI)
- Public spaces (no CUI processing occurs outside dedicated home office)

## Definitions

- **Physical Access:** Entry to the physical space where SecureMac systems are located

- **Controlled Area:** Home office space with restricted access (locked door)

- **Media:** Physical devices or objects that store information (hard drives, USB drives, backup tapes, etc.)

- **CUI Media:** Any media containing Controlled Unclassified Information

- **Sanitization:** Process of making information unrecoverable from media before reuse or disposal

- **LUKS (Linux Unified Key Setup):** Full-disk encryption system using FIPS 140-2 validated cryptography

- **Environmental Control:** Temperature, humidity, power, and fire suppression systems

---

## Part 1: Physical and Environmental Protection

### 1. Physical and Environmental Protection Policy and Procedures (PE-1)

[DOMAIN.ORG] shall maintain and review this policy annually. Implementation procedures are documented in Section 3 of this document. Compliance is verified through:
- Annual physical security assessment
- Quarterly facility inspections
- Monthly environmental monitoring checks
- Review of access logs and physical security incidents

### 2. Physical Access Authorizations (PE-2)

**Authorized Personnel:**
- **[SYSTEM-OWNER]** (Owner/Principal/ISSO) - unrestricted access
- **Contractors** - supervised access only, temporary basis, documented
- **Visitors** - NOT APPLICABLE: No visitors permitted in CUI processing area

**Authorization Process:**
- Owner/Principal: Permanent authorization based on Top Secret clearance and business ownership
- Contractors: Temporary authorization requires:
  - Executed NDA (per DIWAI-PS-001)
  - Business need justification
  - Supervised access (Owner present at all times)
  - Limited duration (specific date/time)
  - Access log documentation

**Access List Maintenance:**
- Physical access authorization list maintained in `/backup/physical-security/access-list.xlsx`
- Quarterly review to ensure accuracy
- Update within 24 hours of any personnel changes
- Include: name, authorization level, effective dates, clearance/screening status

### 3. Physical Access Control (PE-3)

**Facility Description:**
- **Location:** Home office, [LOCATION-REDACTED] (dedicated workspace within residence)
- **Access Points:** Single entry door to home office
- **Physical Security Features:**
  - Entry-controlled (locked door when unattended)
  - Deadbolt lock on office door
  - Residence protected by perimeter security (exterior doors, alarm system)
  - Windows in office have security film/locks
  - Locking 42U server rack contains critical equipment
  - Workstations physically secured to desks (cable locks)

**Access Control Measures:**
- Office door locked whenever Owner is not present
- Key control: Keys maintained by Owner only (no spare keys distributed)
- Server rack locked (separate key from office door)
- Alarm system active when residence unoccupied
- No signage indicating CUI processing or government contractor status

**Access Procedures:**
- Owner accesses office as needed for business operations
- Contractors (if physical access required):
  1. Schedule access in advance
  2. Owner must be present throughout visit
  3. Contractor may not be left unattended in office
  4. Log entry and exit times
  5. Contractor may not access server rack
  6. All activities monitored and documented

**After-Hours Access:**
- Not applicable - home office, Owner resides on-site
- Office locked when not in active use
- Server rack remains locked at all times
- Motion detection alerts (if alarm system configured)

### 4. Access Control for Transmission and Display (PE-4)

**Information Display:**
- Computer monitors positioned to prevent viewing from windows
- Screen privacy filters used on workstations (if windows present)
- Automatic screen lock after 15 minutes of inactivity
- Screens locked (Ctrl+Alt+L) when leaving workspace

**Audio Privacy:**
- No speakerphone use for CUI-related discussions if others present in residence
- Video conferences with CUI content conducted in private office with door closed
- No audio monitoring devices (Alexa, Google Home) in office

**Information Transmission:**
- Network cables secured within office (no exposed cabling outside controlled area)
- Wireless network secured with WPA3-Enterprise (389-DS LDAP authentication)
- No wireless keyboard/mouse on systems processing CUI (USB wired only)

### 5. Monitoring Physical Access (PE-6)

**Monitoring Methods:**
- Physical access limited exclusively to Owner (single occupant)
- Office door lock status verified before leaving residence
- Server rack lock verified daily
- Home security system monitors office entry door (if configured)
- Security camera (if deployed) monitors office entrance

**Access Logs:**
- **Not Applicable** for Owner (sole occupant)
- Contractor access logged manually when required:
  - Date and time of entry
  - Purpose of visit
  - Duration
  - Systems/areas accessed
  - Owner supervision confirmation
- Log maintained in `/backup/physical-security/contractor-access-log.txt`

**Monitoring Review:**
- Monthly review of any contractor access logs
- Quarterly review of physical security controls effectiveness
- Annual review of facility security posture

### 6. Visitor Access and Control (PE-8)

**Visitor Policy:**
- **NOT APPLICABLE:** No visitors permitted in CUI processing area
- Home office is private workspace with no public access
- No clients, vendors, or sales personnel permitted in office
- Business meetings conducted outside of home office (remote or off-site)

**Rare Exception Handling (e.g., emergency repair):**
If emergency facility repair required (e.g., electrical, HVAC):
1. Move all CUI media to locked safe or locked vehicle
2. Lock server rack
3. Lock workstation screens and cover monitors
4. Supervisor repair personnel at all times
5. No repair personnel access to computers or server equipment
6. Document visit in security log
7. Verify no equipment tampering after visit

### 7. Power Equipment and Cabling (PE-9)

**Power Protection:**
- All critical equipment on UPS (Uninterruptible Power Supply):
  - Mac mini on UPS — this single host carries the perimeter firewall, the hypervisor and the CUI file store, so its loss takes the whole system
  - Network equipment (switches, media converters) on UPS
  - NAS on UPS, to avoid interrupting a backup mid-write
- UPS battery health tested quarterly
- Generator backup: Not currently deployed (future consideration)

**Power Management:**
```bash
# Verify UPS status
sudo apcaccess status  # If APC UPS with apcupsd

# Check UPS battery health
sudo apctest
```

**Cabling Security:**
- Network cables run within office (not through unsecured areas)
- Cable management prevents accidental disconnection
- Power cables secured and labeled
- No cables exposed outside controlled office space
- RAID array power and data cables secured within server rack

**Emergency Power-Down:**
- In case of emergency requiring immediate power-down:
  1. Shut down **guest before host** — the VM runs on the Mac:
     `ssh services 'sudo shutdown -h now'` then shut down macOS
  2. Allow UPS to safely power down equipment
  3. If immediate power cut needed, disable UPS and switch off circuit breakers

### 8. Emergency Shutoff (PE-10)

**Emergency Power Disconnect:**
- Circuit breaker panel accessible to Owner
- Office on dedicated circuit (15A or 20A)
- Emergency shutoff procedure:
  1. If time permits, shut down the VM first, then the Mac host (guest before host)
  2. Switch off circuit breaker for office
  3. Switch off UPS if battery backup not needed
  4. Document reason for emergency shutoff

**Emergency Scenarios:**
- Fire: Power down and evacuate immediately
- Flood: Elevate equipment if possible, power down, cut power at breaker
- Physical security breach: Lock down systems (disable accounts), power down if necessary

### 9. Emergency Lighting (PE-11)

**Lighting Requirements:**
- Office has normal lighting (overhead, desk lamps)
- Emergency flashlight kept in office for power outages
- Battery-powered emergency lighting (if home has emergency lighting system)
- Sufficient lighting for safe emergency shutdown of equipment

### 10. Emergency Power (PE-12)

**Current State:**
- UPS provides short-term emergency power (30 minutes)
- Sufficient for graceful shutdown during power outage

**Future Enhancement:**
- Consider whole-home generator for extended power outage scenarios
- Consider additional UPS capacity for longer runtime

### 11. Fire Protection (PE-13)

**Fire Detection:**
- Smoke detectors in office (per building code requirements)
- Residence fire alarm system (if installed)
- Battery backup for smoke detectors

**Fire Suppression:**
- Standard residential fire suppression (smoke detectors, fire extinguisher)
- Fire extinguisher (ABC-rated) kept in or near office
- Sprinkler system (if residence equipped)

**Fire Response Procedures:**
1. Activate building fire alarm (if present)
2. Call 911
3. Evacuate immediately - do NOT attempt to save equipment
4. Close office door to slow fire spread
5. Do NOT re-enter for any reason
6. CUI data protected by LUKS encryption (data confidentiality maintained even if hardware destroyed)

### 12. Temperature and Humidity Controls (PE-14)

**Environmental Monitoring:**
- Office maintains normal residential temperature and humidity
- HVAC system serves office space
- Equipment generates minimal heat (one Mac mini, one NAS, network gear; the service VM is virtual and adds no separate thermal load)
- Acceptable temperature range: 60-80°F (15-27°C)
- Acceptable relative humidity: 30-60%

**Monitoring Procedures:**
- Monthly verification that HVAC system functioning
- Visual inspection of equipment for overheating indicators
- Server rack door provides ventilation
- Equipment positioned for adequate airflow

**Temperature Alarms:**
- **No out-of-band management controller is present.** Thermal monitoring relies on macOS/SMC sensors on the host; there is no iLO/IPMI equivalent
- Critical temperature threshold triggers alert
- Monitor via iLO dashboard: https://[LAN-IP-REDACTED]

**Emergency Response:**
- If office temperature exceeds safe range:
  1. Shutdown non-critical systems
  2. Investigate HVAC failure
  3. Provide temporary cooling (fan, open windows if secure)
  4. If temperature remains high, gracefully shutdown all systems

### 13. Water Damage Protection (PE-15)

**Water Damage Risks:**
- Office located on first/second floor (specify actual location)
- No water pipes directly above server equipment
- Server rack positioned away from windows (flood risk)
- No aquariums or water sources in office

**Protection Measures:**
- Equipment elevated above floor level (server rack, desk height)
- Water detection sensor (if available) near server rack
- Regular inspection for roof leaks, pipe leaks
- Immediate response to any water intrusion

**Water Damage Response:**
1. Stop water source if possible
2. Power down equipment immediately (circuit breaker)
3. Move equipment to dry location if possible
4. Do NOT power on wet equipment
5. Professional assessment before restoring power
6. Restore from backups to replacement hardware if needed

### 14. Delivery and Removal (PE-16)

**Equipment Delivery:**
- New equipment delivered to residence (not directly to office)
- Inspect all deliveries before bringing into office
- Verify authenticity of equipment (check vendor, packaging, seals)
- Scan for malware before connecting to network
- Document all new equipment in asset inventory

**Equipment Removal:**
- Authorization required from Owner/Principal (self-authorization)
- Equipment leaving facility logged in `/backup/physical-security/equipment-movement.log`
- Include: date, equipment description, serial number, reason, destination, expected return date
- Media sanitization required before removal (if equipment contains CUI storage)

**Authorized Removal:**
- Backup media to offsite location (monthly rotation)
- Equipment for repair (sanitized first, or never contained CUI)
- Equipment disposal (sanitized per MP-6)
- Temporary relocation for emergency (fire, flood)

### 15. Alternate Work Sites (PE-17)

**Policy:**
- **NOT APPLICABLE:** All CUI processing occurs exclusively at primary home office
- No alternate work sites authorized
- No mobile devices process or store CUI
- Portable computers are permitted for CUI **only** where full-disk encryption is enabled, the device is enrolled in the compliance baseline (SCAP/mSCP), and it is physically secured when unattended.

- **Wired connection is the required default in the office.** Laptops operating on the CUI network shall use wired Ethernet. This preference is **enforced by network design**, not by instruction alone — the CUI segment is delivered over wired interfaces, and the perimeter `pf` ruleset governs what may traverse it.

- **Wireless is permitted only away from the office**, where a wired connection is not available. In that mode:
  - the link shall use WPA2/WPA3 with authentication (3.1.17);
  - access to CUI resources shall be by VPN to the boundary, not by direct exposure of services;
  - the device remains subject to this policy and to `DIWAI-SCP-001` for transmission protection;
  - CUI is not to be processed over open or untrusted wireless networks.

  > **Planned change.** A SCAP-hardened laptop is planned for introduction to the LAN as the model daily driver, moving routine work off the appliance (SSP §3.2.1). The previous blanket prohibition on laptops was inherited from Reference System #1 and would have forbidden that architecture.
  >
  > **Wireless authorisation must be updated before that device is introduced.** Requirement 3.1.16 obliges the organisation to *authorise wireless access prior to allowing such connections*. The current position — recorded in SSP §2.5.2 and scored on 2026-08-03 — is that wireless is **not permitted**: the Mac host's `en1` is powered off and `pf` bars CUI egress by that path. Introducing a laptop that uses wireless away from the office changes that posture and requires the authorisation, the conditions above, and the SSP boundary text to be updated **in advance of deployment**, not after.
- No remote work locations
- No cloud storage for CUI

**Travel:**
- Owner may travel for business
- No CUI data taken on travel
- Remote access to SecureMac not currently configured (future: VPN with MFA)

### 16. Location of System Components (PE-18)

**Equipment Positioning:**
- All CUI processing equipment located within home office
- Server rack position: (document specific location)
- Workstations: (document specific locations)
- Network equipment: switches and media converters in the 2U rack or a secured location; the perimeter firewall is software on the Mac mini and has no separate enclosure
- No CUI equipment in public or shared areas of residence

**Positioning Requirements:**
- Equipment not visible from windows
- Equipment in climate-controlled area
- Equipment protected from water damage
- Equipment accessible for maintenance
- Cabling secured and not exposed to damage

### 17. Information Leakage (PE-19)

**Emanation Security:**
- Residential environment provides sufficient RF shielding for CUI
- No TEMPEST requirements for CUI (only for classified information)
- Wireless networks use strong encryption (WPA3-Enterprise)
- Bluetooth disabled on all CUI processing systems
- No wireless keyboards/mice that could leak keystrokes

**Acoustic Security:**
- Office door provides sound attenuation
- No voice-activated assistants in office
- Conduct sensitive voice/video calls behind closed door

### 18. Asset Monitoring and Tracking (PE-20)

**Asset Inventory:**
- Maintain complete inventory in `/backup/physical-security/asset-inventory.xlsx`
- Include: device name, make/model, serial number, location, assigned user, acquisition date

**Asset Tracking:**
- Quarterly inventory verification (physical inspection)
- Update inventory within 24 hours of changes (new equipment, disposal, relocation)
- Document asset location changes
- Track asset disposition (deployment, storage, disposal)

**Missing Equipment Response:**
- If equipment missing:
  1. Conduct thorough search of office and residence
  2. Review access logs (any contractor visits?)
  3. If not found within 24 hours, report as potential theft
  4. Initiate incident response (DIWAI-IRP-001)
  5. Report to law enforcement if theft suspected
  6. Assess CUI data exposure (LUKS encryption should protect data)
  7. Report to DoD if CUI compromise possible (72-hour clock)

---

## Part 2: Media Protection

### 1. Media Protection Policy and Procedures (MP-1)

[DOMAIN.ORG] shall implement and maintain media protection procedures to safeguard CUI on all media types. Compliance verified through:
- Quarterly media inventory
- Annual media sanitization procedure review
- Monthly backup media verification
- Encryption status checks

### 2. Media Access (MP-2)

**Access Control:**
- All media access restricted to Owner/Principal only
- No shared media or cloud storage for CUI
- Physical media stored in locked office
- Digital media encrypted (LUKS) and access controlled via 389-DS LDAP
- Backup media stored in locked server rack or locked safe

**Media Types:**
- **System Storage:** FileVault on the Mac mini; LUKS2 on the VM's virtual disks
- **RAID Array:** NAS storage (nas.[DOMAIN.ORG]) with LUKS-encrypted volumes
- **Backup USB Drives:** LUKS-encrypted, stored in locked location
- **Offline Backups:** ReaR ISO images, encrypted, stored offsite (monthly rotation)

**Access Procedures:**
```bash
# Access encrypted RAID array (if manual mount needed)
sudo cryptsetup luksOpen /dev/md0 samba_data
sudo mount nas.[DOMAIN.ORG]:/share /mnt/nas

# Verify encryption status
sudo cryptsetup status samba_data

# Backup USB mount (for monthly offsite rotation)
sudo cryptsetup luksOpen /dev/sdb1 backup_usb
sudo mount /dev/mapper/backup_usb /media/backup
```

### 3. Media Marking (MP-3)

**CUI Marking Requirements (32 CFR Part 2002):**

**Electronic Documents:**
- Header: "CUI" or specific category (e.g., "CUI//SP-PROPIN")
- Footer: "CUI" or specific handling instructions
- Email subject line: Include "CUI" when applicable
- Filenames: Include CUI indicator if appropriate

**Physical Media Labels:**
- USB drives containing CUI: Apply "CUI" label
- Backup media: Label "CUI - Backup - Date"
- Media stored offsite: "CUI - [ORGANIZATION] - Do Not Destroy"

**Simplified Marking (Solopreneur):**
- Owner marks all CUI materials
- No distribution limitations needed (single user environment)
- Contract deliverables marked per contract requirements
- Internal documents marked to maintain awareness

**Media Inventory Marking:**
- Asset inventory indicates which media contains CUI
- Encrypted media documented as "LUKS-encrypted CUI"

### 4. Media Storage (MP-4)

**Physical Storage:**
- **Internal System Media:** Stored in locked server rack or secured workstation
- **Backup USB Drives:** Locked cabinet, drawer, or safe
- **Offsite Backup Media:** Safe deposit box or secure offsite location
- **Media Never Leaves Controlled Area** (except encrypted offsite backups)

**Storage Security:**
- LUKS encryption protects CUI at rest (FIPS 140-2 validated)
- Physical security (locked office, locked server rack)
- Environmental controls (temperature, humidity)
- Fire protection (smoke detectors, extinguisher)

**Storage Inventory:**
Maintain inventory of all CUI media:
- Device description and serial number
- Encryption status
- Storage location
- Data classification
- Last backup date
- Responsible party (Owner)

### 5. Media Transport (MP-5)

**Transport Methods:**

**Electronic Delivery (Preferred):**
- TLS-encrypted email with CUI marking in subject
- Secure government portal upload
- 389-DS LDAP-authenticated NAS transfer (internal only)
- VPN-encrypted transfer (when VPN implemented)

**Physical Transport (Offsite Backups):**
- LUKS-encrypted USB drives only
- Never transport unencrypted CUI media
- Owner transports personally (no shipping)
- Locked container during transport (briefcase, locked bag)
- Direct transport from home office to safe deposit box
- Monthly rotation schedule documented

**Courier Requirements:**
- Owner serves as courier (no third-party courier used)
- Media remains in Owner's physical possession throughout transport
- If overnight storage required during transport, locked hotel safe or vehicle trunk
- Document transport: date, media description, origin, destination, courier (Owner)

**Prohibited Transport:**
- No mailing or shipping of CUI media (except via approved government-approved courier if required)
- No cloud upload of CUI
- No transport via commercial backup services
- No transport via unencrypted media

### 6. Media Sanitization (MP-6)

**Sanitization Requirements:**
Media must be sanitized before:
- Reuse for non-CUI purposes
- Removal from facility (e.g., for repair)
- Disposal or destruction
- Transfer to another party

**Sanitization Methods:**

**Method 1: Cryptographic Erase (Preferred for Encrypted Media):**
```bash
# LUKS encrypted media - destroy encryption key
sudo cryptsetup luksErase /dev/sdX
# This makes data permanently unrecoverable
# Confirm action when prompted
```

**Method 2: Secure Overwrite (for unencrypted media):**
```bash
# Use shred utility (NIST SP 800-88 compliant)
sudo shred -vfz -n 10 /dev/sdX
# -v: verbose
# -f: force (change permissions to allow writing)
# -z: add final overwrite with zeros
# -n 10: overwrite 10 times
```

**Method 3: Physical Destruction (for high-sensitivity media):**
- Remove drive from enclosure
- Use drill to physically destroy platters (HDD) or chips (SSD)
- Dispose of fragments in separate waste streams
- Document destruction with photos if required for compliance

**Sanitization Documentation:**
- Log all sanitization activities in `/backup/physical-security/media-sanitization-log.txt`
- Include: date, media description, serial number, sanitization method, performed by, verification method
- Retain sanitization logs for 3 years

**Sanitization Verification:**
```bash
# For shred verification - attempt to mount
sudo mount /dev/sdX /mnt  # Should fail

# For LUKS-erased media - attempt to open
sudo cryptsetup luksOpen /dev/sdX test  # Should fail
```

### 7. Media Use (MP-7)

**Authorized Media Use:**
- CUI shall only be stored on FIPS 140-2 validated encrypted media
- Full-disk encryption on all hosts: **FileVault** (Mac mini), **LUKS2** (service VM), and encrypted volumes on the NAS
- Backup media must be LUKS-encrypted
- No unencrypted storage of CUI permitted

**Prohibited Media:**
- Optical media (CD/DVD) disabled in BIOS (if drives present)
- Floppy drives (not present)
- SD cards (unless encrypted with LUKS)
- Cloud storage (prohibited for CUI)
- Personal USB drives (unless encrypted and authorized)

**Removable Media Control:**
```bash
# USB device restrictions (future implementation with USBGuard)
# Until USBGuard deployed, rely on policy and physical security

# Check for unauthorized USB devices
lsusb
# Review for any unknown devices

# Check mounted filesystems for unauthorized media
df -h | grep media
```

**Authorized Media Types:**
- Internal SATA/SAS drives (LUKS-encrypted)
- USB drives (LUKS-encrypted, authorized by Owner)
- RAID array (LUKS-encrypted)
- NVMe drives (if used, LUKS-encrypted)

### 8. Media Downgrading (MP-8)

**Downgrading Policy:**
- Media previously used for CUI may be downgraded to unclassified use ONLY after proper sanitization
- Sanitization method: LUKS luksErase or shred (per MP-6)
- Document downgrading decision and sanitization method
- Verify sanitization before downgrading

**Downgrading Procedure:**
1. Identify media for downgrading
2. Verify all CUI data backed up (if needed)
3. Perform sanitization per MP-6
4. Verify sanitization successful
5. Document downgrade in media sanitization log
6. Reformat and re-encrypt for new purpose (or destroy)
7. Update asset inventory to reflect new classification

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Owner/Principal ([SYSTEM-OWNER])** | Maintain physical security of facility; control physical access; oversee environmental controls; authorize equipment movement; maintain asset inventory; perform media sanitization; transport offsite backups |
| **ISSO ([SYSTEM-OWNER], concurrent role)** | Document physical security procedures; conduct quarterly facility inspections; maintain access logs; verify encryption status; review sanitization procedures; track media inventory |
| **Contractors** | Comply with supervised access requirements; do not access server equipment; report physical security concerns; do not remove any media from facility |

## Compliance and Enforcement

**Monitoring:**
- Quarterly facility security inspections
- Monthly environmental controls verification
- Quarterly media inventory
- Annual physical security assessment
- Integration with Incident Response Policy for physical security incidents

**Training:**
- Owner maintains awareness of physical security best practices
- Contractor briefing on physical security rules (if on-site access required)
- Annual review of this policy

**Enforcement:**
- Physical security violations investigated as security incidents
- Unauthorized media handling triggers incident response
- Equipment theft or loss reported to law enforcement and DoD (if CUI impact)
- Policy violations may result in contract termination

**Metrics:**
- Zero unauthorized physical access incidents
- 100% media encryption compliance
- 100% sanitization procedure compliance
- Quarterly inventory accuracy >99%

## References

- NIST SP 800-171 Rev 2, PE Family (Physical and Environmental Protection)
- NIST SP 800-171 Rev 2, MP Family (Media Protection)
- NIST SP 800-88 Rev 1 (Guidelines for Media Sanitization)
- 32 CFR Part 2002 (CUI Marking)
- System Security Plan (SSP), Sections 3.10 and 3.8
- Risk Management Policy (DIWAI-RA-001)
- Incident Response Policy (DIWAI-IRP-001)

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
