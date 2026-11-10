> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# SESSION RECORD — INITIAL SELF-ASSESSMENT FOR PRODUCTION READINESS

## [DOMAIN.ORG] SecureMac Reference System

| Field          | Value                                                                                                   |
|----------------|---------------------------------------------------------------------------------------------------------|
| **Document ID**    | **DIWAI-SR-2026-08**                                                                                        |
| **Version**        | 1.0                                                                                                     |
| **Date issued**    | August 4, 2026                                                                                          |
| **Period covered** | **2026-07-30 to 2026-08-04**                                                                                |
| **Assessment ID**  | DIWAI-ASMT-2026-08                                                                                      |
| **Purpose**        | Record the initial self-assessment performed to determine readiness to place the system into production |
| **Assessor**       | [SYSTEM-OWNER] — System Owner / ISSO (self-assessment; see §1.2)                                     |
| **Classification** | Controlled Unclassified Information (CUI)                                                               |

---

## 1. Purpose and scope

### 1.1 What this was

An initial self-assessment of the [DOMAIN.ORG] SecureMac Reference System against
**NIST SP 800-171 Rev 2**, conducted at **assessment-objective level per NIST SP
800-171A**, to determine whether the system is ready to be placed into
production.

The assessment verified **each 800-171A assessment objective** against the
running system rather than against documentation, and dealt with each finding in
one of two ways: **spot-corrected during the assessment**, or **documented for
follow-up** in the Plan of Action and Milestones.

### 1.2 Assessor independence

This is a **self-assessment**. The system owner is also the operator, the
administrator and the assessor. **No independent review has been performed and
none is claimed.** The limitation is recorded rather than mitigated, and is
itself carried as risk **R-12** in `DIWAI-RAR-001`.

### 1.3 CUI status of the system — material to reading this record

**The system holds no actual CUI at this date.**

The documents it stores are **proprietary business information created by the
organisation**. They are handled, marked and protected **as if** they were CUI —
which is the point of a reference system — and **would be treated as CUI if
provided to a government agency**. No government contract is presently in place
and no covered defense information has been received.

This matters in three ways:

1. **The assessment is a readiness exercise, not an incident-free operating record.** Findings are about whether the system *would* protect CUI, not about how it has protected CUI to date.
2. **Certain obligations are not yet live.** DFARS 252.204-7012 cyber-incident reporting, and the DoD medium assurance certificate that reporting requires, do not currently apply — but both carry lead time and are tracked (**POA&M-057**) so they are not discovered on the day a contract is signed.
3. **The exposure found during this assessment did not put real CUI at risk.** That is a statement of fact about timing, not a mitigation, and the findings stand undiminished.

---

## 2. What was done

### 2.1 Objective-level verification

All **110 requirements** were assessed at objective level (≈249 determinations),
recorded in `CUI_800-171A_Self_Assessment_2026-08.md`. Verification was performed
**against the live system** — service state, configuration files, logs, running
processes and directory contents — not against the SSP's description of it. That
distinction produced most of what follows.

### 2.2 Spot corrections applied during the assessment

Where a finding could be corrected safely and verified immediately, it was.
Recorded across change records `DIWAI-CR-2026-08-01` through `-08-10`
(**C1–C79**). Principal examples:

| Area                | Correction                                                                                                                                                                         |
|:--------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SIEM availability   | Wazuh manager restored and version-locked after an unattended upgrade disabled it for ~21 h                                                                                        |
| Audit retention     | Raised from roughly **one hour** to ~6.4 GB of capacity                                                                                                                                |
| Directory security  | Account lockout and password history enabled; Directory Manager credential re-hashed from `{CLEAR}` to PBKDF2-SHA512 and rotated; cleartext LDAP port closed; **insecure binds refused** |
| Transport           | NAS moved from cleartext `cn=Directory Manager` binding to TLS with a scoped service account; Apache LDAP auth moved to LDAPS                                                        |
| Backups             | Archive pipeline repaired (four independent defects) and verified by round-trip decryption; VM archive verified **byte-identical** to its manifest SHA-256                             |
| Monitoring          | `diwai-control-health` deployed — 24 checks, dual alert path independent of Wazuh                                                                                                    |
| Least functionality | ClamAV removed (FIPS-incompatible); Grafana removed (unpatchable); mSCP toolchain purged from the CUI boundary                                                                     |
| Boundary            | Wireless disabled and pf-enforced; Spotlight indexing of CUI excluded                                                                                                              |
| Availability        | Nextcloud Office watchdog repaired — it had been starting the VM and killing it every 5 minutes while logging success                                                              |

### 2.3 Documented for follow-up

Findings not safely correctable in-session were recorded in the POA&M.
**23 items remain open**; **26 are closed**.

### 2.4 Compliance artefact set brought current

- **SSP v2.16** — including §3.2.1, recording role concentration on the Mac host and the planned daily-driver separation
- **POA&M v1.6**
- **SBOM v3.3** (published in redacted form)
- `DIWAI-RAR-001` **v1.1** — first risk assessment for this system, 14 risks, accepted and signed
- `DIWAI-IR-TTX-001` — first incident-response tabletop, conducted and signed, 10 gaps recorded
- **Training** — DoD CUI (IF141.16) certificate held; insider threat (INT101.16) completed and attested; role assignment, competency record and training register signed
- **Policy set — all eleven policies reissued** after they were found to describe Reference System #1 (POA&M-058)

### 2.5 Action checklist created

`DIWAI-CHK-001` (2026-08-04) converts the open POA&M into 21 sequenced
actions across four tiers, plus five standing items. The POA&M remains the record
of authority; the checklist exists to be worked from.

---

## 3. Result

**SPRS score: 56 → 87 of 110**, deductions reduced from −54 to −23.

Of the 31 points recovered, **30 were for work already performed** where the
register had not caught up; only one requirement (3.5.10) needed new ws-b.
That ratio is the most useful single finding of the assessment.

**The score is self-assessed, moved 31 points in one day, and has not been
independently reviewed.** An earlier figure of 98/110 was carried for months
before being corrected to 85 and then 56. The deduction list should be walked by
someone other than its author before submission to SPRS.

---

## 4. The governing observation

**The dominant failure mode found was not weak controls. It was controls that
reported success while doing nothing.**

- An encrypted archive pipeline that ran daily, exited 0, and delivered nothing for months
- A weekly compliance scan executing a zero-byte script since ~June
- Clock synchronisation reporting itself healthy while 24 minutes adrift
- A Nextcloud Office watchdog starting a VM and killing it every 5 minutes, logging "started successfully" each time
- FIM deployed, validated, pushed — and silently not alerting, because `realtime` is ignored on macOS
- 24 health checks reporting green throughout a six-minute authenticated-request outage **caused by the assessor**

**Two of these had previously been closed as fixed.**

The corollary shaped how this assessment was conducted, and should shape the next
one: **verify the thing, not the mechanism that was supposed to do it.** Several
findings surfaced only because something was actually exercised — and two of the
most serious were found by the system owner reviewing output rather than by any
automated check.

---

## 5. Production readiness determination

**The system is assessed as ready to enter production use for the handling of
proprietary information treated as CUI**, subject to the following being
understood as conditions rather than aspirations:

1. **MFA is not deployed** for OS-level access on either host (POA&M-004/-007; 3.5.3 and 3.7.5 each −5). Nextcloud's TOTP is the only second factor in the system.
2. **No internet-facing/CUI tier separation** exists. Accepted in writing to **2027-03-31** (POA&M-023 / R-02) — to be **re-decided, not renewed**, and void if a further service is published.
3. **Restoration has never been tested end to end** (POA&M-052). The one documented bare-metal recovery returned an incomplete host for reasons never determined.
4. **Succession is unmitigated** (POA&M-049). No other individual can administer or recover the system.
5. **Nextcloud stores CUI as plaintext files.** Any process running as the operator's account reads them outside Nextcloud's authentication, 2FA, ACLs and audit log.

**Before actual CUI is received under contract**, items 1 and 3 should be closed
and item 5 mitigated, and the DIBNet reporting capability (POA&M-057) must exist.

---

## 6. Next assessment

**A second self-assessment shall be performed within 30 days — due 2026-09-03.**

Its scope:

- **Re-verify every item closed during this assessment.** Two items closed in June recurred by August; closure is not permanent.
- **Test the corrections that were not exercised**, particularly backup restoration and incident-response mechanisms.
- **Work** `DIWAI-CHK-001` **in order** and record what was completed, what slipped, and why.
- **Re-walk the SPRS deduction list independently of the author** before any submission.
- **Confirm the policy set still matches the system** — the drift corrected on 2026-08-04 accumulated silently over months.

---

## 7. Records

| Artefact                                    | Location                                                      |
|:--------------------------------------------|:--------------------------------------------------------------|
| Objective-level assessment                  | `Compliance/Assessment/CUI_800-171A_Self_Assessment_2026-08.md` |
| SSP v2.16                                   | `Compliance/SSP/`                                               |
| POA&M v1.6                                  | `Compliance/POAM/`                                              |
| Change records C1–C79                       | `Compliance/Change_Records/` (`DIWAI-CR-2026-08-01`…`-08-10`)       |
| Risk assessment, tabletop, incident reports | `Compliance/Risk_Assessment/`, `Compliance/Incident_Response/`    |
| Training and acknowledgment evidence        | `Compliance/Evidence/Training/`                                 |
| Action checklist                            | `Compliance/Assessment/CUI_POAM_Action_Checklist_2026-08-04.md` |
| Superseded versions                         | `CUI_Archive/2026-08-03_superseded/`                            |

---

## 8. Attestation

I attest that the assessment described above was performed over the period
stated, that findings were verified against the running system, and that this
record accurately describes both what was corrected and what remains open.

|           |                                          |
|:----------|:-----------------------------------------|
| **Name**      | [SYSTEM-OWNER]                        |
| **Roles**     | System Owner; ISSO; System Administrator |
| **Signature** | [SYSTEM-OWNER]                        |
| **Date**      | August 4, 2026                           |

---

## Version History

| Version | Date       | Author     | Changes                                                                                                                                                                                                                                                                                                                                                                                           |
|---------|------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0     | 2026-08-04 | [SYSTEM-OWNER] | Initial issue. Records the 2026-07-30 → 2026-08-04 initial self-assessment: objective-level verification of all 110 requirements, spot corrections C1–C79, 23 items documented for follow-up, SPRS 56 → 87/110, and a production-readiness determination with five stated conditions. Records that the system holds no actual CUI at this date. Commits to a second self-assessment by 2026-09-03 |
