> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# PLAN OF ACTION AND MILESTONES (POA&M)
## [DOMAIN.ORG] SecureMac Reference System

**Document Control:**

| Field | Value |
|-------|-------|
| **System Name** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **System Owner** | Donald [SYSTEM-OWNER] |
| **Organization** | [DOMAIN.ORG] (Do It With AI) |
| **Classification** | Controlled Unclassified Information (CUI) |
| **Version** | 1.2 |
| **Date** | June 12, 2026 |
| **SSP Reference** | System_Security_Plan_v2.13.md (§10) |
| **SPRS Score** | 98 / 110 (89.1%) — see Summary Dashboard caveats |
| **Compliance Framework** | NIST SP 800-171 Rev 2 / FIPS 140-2 |
| **Supersedes** | [DOMAIN.ORG]_Unified_POAM_v1.1.md (2026-06-11) |

---

## DOCUMENT REVISION HISTORY

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.1 | 2026-06-11 | [SYSTEM-OWNER] | Initial standalone document consolidating POA&M-001–008 (see that file for full lineage). |
| 1.1 (corrected) | 2026-06-11 | [SYSTEM-OWNER] | Added POA&M-008 (security awareness training) per independence determination. |
| **1.2** | **2026-06-12** | **[SYSTEM-OWNER]** | **Independent gap assessment + remediation pass** (report: `Compliance/Assessment/RS2_Gap_Assessment_2026-06-12.md`). **POA&M-002 CLOSED** via SI-3 control substitution — ClamAV decommissioned (non-functional under FIPS); malicious-code protection rebased on YARA + VirusTotal + fapolicyd + SELinux + Suricata (evidence DIWAI-EV-SI3-002). Correction recorded: **YARA was in fact already deployed and Wazuh-integrated** on the VM (prior docs erroneously stated otherwise). Added closed items **POA&M-009** (host Wazuh agent restored) and **POA&M-010** (VM time-sync drift corrected). Minor config-hygiene fixes (reverse-proxy `trusted_proxies`, removal of `sshpass`/YubiKey tooling) recorded as closed with no SPRS impact. Carries forward open items 003, 004, 005, 006, 007, 008. |

---

## PURPOSE

This Plan of Action and Milestones documents all open, closed, and planned security findings for the [DOMAIN.ORG] SecureMac Reference System (RS2). It is a living document, reviewed quarterly with the SSP. Findings are tracked from identification through remediation or formal risk acceptance.

**Relationship to SSP:** `System_Security_Plan_v2.13.md` §10 references this document as the authoritative POA&M and reproduces a summary table of the same items.

---

## POA&M ITEMS

| POA&M ID | Control | Weakness | Status | Opened | Closed/Target |
|----------|---------|----------|--------|--------|---------------|
| POA&M-001 | 3.5.3, IA-5 | YubiKey PIV re-pairing (Mac host) | **Closed — Superseded** | 2026-04-15 | Closed 2026-06-06 |
| POA&M-002 | 3.14.2 | ClamAV daemon / YARA deployment on VM | **Closed — Resolved (substitution)** | 2026-06-05 | **Closed 2026-06-12** |
| POA&M-003 | 3.4.1 | mSCP 8 failing rules remediation (Mac host) | Planned | 2026-06-05 | Q3 2026 |
| POA&M-004 | 3.5.3, 3.7.5 | TOTP MFA deployment — VM | Planned | 2026-06-05 | Q3 2026 |
| POA&M-005 | 3.11.1 | First annual risk assessment | **Overdue** | 2026-06-05 | OVERDUE |
| POA&M-006 | 3.6.3 | IR tabletop exercise | On Track | 2026-06-05 | 2026-06-30 |
| POA&M-007 | 3.5.3, 3.7.5 | TOTP enrollment — Mac host | Planned | 2026-06-06 | Q3 2026 |
| POA&M-008 | 3.2.1/3.2.2/3.2.3 | [DOMAIN.ORG]-specific security awareness training | New — Planned | 2026-06-11 | Q3 2026 |
| **POA&M-009** | **3.3.1/3.3.2, AU-6/SI-4** | **Mac host Wazuh agent offline (host telemetry/FIM)** | **Closed — Resolved** | 2026-06-12 | **Closed 2026-06-12** |
| **POA&M-010** | **3.3.7, AU-8** | **VM time-synchronization drift (audit-timestamp integrity)** | **Closed — Resolved** | 2026-06-12 | **Closed 2026-06-12** |

---

## ITEM DETAIL (new / changed items — see v1.1 for unchanged 001, 003–008)

### POA&M-002 — ClamAV daemon / YARA deployment on VM — CLOSED (Resolved by control substitution)
**Control:** NIST SP 800-171 § 3.14.2 / SI-3
**Status:** **Closed — Resolved 2026-06-12**
**SPRS Impact:** +1 recovered (3.14.2 now fully MET; no longer dependent on risk acceptance)

**Resolution:** The 2026-06-12 independent assessment found ClamAV was **non-functional under FIPS** — not merely "daemon inactive," but unable to download or load any signature database (`freshclam`/`clamd` fail OpenSSL FIPS verification with `Can't allocate memory`). It provided **zero** malicious-code detection. ClamAV was **decommissioned**, and SI-3 was **substituted** to a FIPS-native, defense-in-depth control set already operational on the VM:

- **YARA 4.5.2** — 5,972 rules — already deployed and integrated via Wazuh active-response on FIM rules 550/554 (new/modified files). *(Correction: prior POA&M/SSP text stated YARA was "not deployed on this system" — that was incorrect; it was deployed.)*
- **Weekly full-system YARA scan** (`yara-fullscan.timer`) — added 2026-06-12 to close the on-change-only coverage gap (validated).
- **VirusTotal** reputation on FIM events; **fapolicyd** application allow-listing; **SELinux** enforcing; **Suricata** network IDS.

**Evidence:** `Compliance/Evidence/SI-3_Control_Substitution_ClamAV_Decommission_2026-06-12.md` (DIWAI-EV-SI3-002) — supersedes the prior ClamAV/FIPS risk acceptance (RISK-2026-004, now archived). See also the remediation log `Compliance/Architecture/Part2_remediation_log.txt`.

### POA&M-009 — Mac Host Wazuh Agent Offline — CLOSED (Resolved)
**Control:** NIST SP 800-171 § 3.3.1/3.3.2 (AU-6, SI-4)
**Status:** **Closed — Resolved 2026-06-12**

**Finding:** The Mac host (securemac.[DOMAIN.ORG]) Wazuh agent (id 003) had been **disconnected since 2026-05-31** — ~12 days with no host-side FIM/SCA/log telemetry reaching the SIEM. Two faults: (1) malformed `ossec.conf` (unescaped `&&` in a netstat `full_command` localfile broke XML parsing); (2) ownership damage — `ossec.conf`, `queue/`, `var/` were `root:wheel` instead of `root:wazuh`, blocking the dropped-privilege `wazuh` process (errors 1226/1210/1212).

**Resolution:** Escaped the XML; restored ownership (`chown -R root:wazuh /Library/Ossec`; `chown -R wazuh:wazuh queue var logs`). Manager confirms **agent 003 = Active**; host telemetry restored. *Note: this gap was not previously tracked because the agent's last known state predated the breakage.*

### POA&M-010 — VM Time-Synchronization Drift — CLOSED (Resolved)
**Control:** NIST SP 800-171 § 3.3.7 (AU-8 — time stamps)
**Status:** **Closed — Resolved 2026-06-12**

**Finding:** The services.[DOMAIN.ORG] VM clock was **~30.7 hours slow** (chronyd active but not stepping large UTM-suspend-induced offsets), so all VM audit/log timestamps were wrong by >1 day — undermining log correlation and forensic integrity (AU-8).

**Resolution:** `chronyc makestep` corrected the clock; `/etc/chrony.conf` set to `makestep 1.0 -1` (steps any offset, survives future suspends). chronyd verified active and synchronized.

### Minor config-hygiene fixes (closed 2026-06-12, no SPRS impact)
- **Reverse-proxy client IP:** Nextcloud `trusted_proxies` set (defense-in-depth; on analysis the PHP path already receives the real client IP, so no exposure existed).
- **Least functionality (CM-7):** removed `sshpass`, `ykman`, `yubico-piv-tool` from the Mac host (unused after YubiKey retirement; `oath-toolkit`/`qrencode` retained for the planned TOTP rollout).

---

## SUMMARY DASHBOARD

| Status | Count | POA&M IDs |
|--------|-------|-----------|
| Closed — Superseded | 1 | 001 |
| Closed — Resolved | 3 | 002, 009, 010 |
| Planned | 3 | 003, 004, 007 |
| Overdue | 1 | 005 |
| On Track | 1 | 006 |
| New — Planned | 1 | 008 |
| **Total** | **10** | |

**Current SPRS:** 98/110 (89.1%) — last-confirmed figure. With **POA&M-002 closed**, 3.14.2 is now **fully MET** (no longer reliant on the previously-pending risk acceptance). **This figure still does not reflect POA&M-008** (3.2.1/3.2.2/3.2.3, SPRS weight TBD — see SSP §11).

**Score path to 110/110:**

| Priority | Item | SPRS Recovery | Target |
|:---|:---|:---|:---|
| 1 | Unified TOTP MFA — VM (004) + Mac host (007) | +8 (3.5.3 + 3.7.5) | Q3 2026 |
| 2 | Annual risk assessment (005) | +3 | OVERDUE — immediate |
| 3 | IR tabletop exercise (006) | +1 | 2026-06-30 |
| 4 | Security awareness training (008) | TBD | Q3 2026 |
| — | mSCP 8 failing rules (003) | (no direct SPRS weight) | Q3 2026 |
| — | ClamAV/YARA SI-3 (002) | **closed — done** | — |

---

## DOCUMENT CONTROL

**Classification:** CONTROLLED UNCLASSIFIED INFORMATION (CUI) — Official Use Only — Need to Know.
**Retention:** Current + 3 years.
**Next Review:** 2026-09-30 (quarterly, aligned with SSP).
**Canonical Copy:** Nextcloud `CUI/Compliance/POAM/[DOMAIN.ORG]_Unified_POAM_v1.2.md` (cloud.[DOMAIN.ORG]).

---

**END OF POA&M v1.2** — supports NIST SP 800-171 Rev 2 / CMMC Level 2 for RS2; referenced by `System_Security_Plan_v2.13.md` §10.
