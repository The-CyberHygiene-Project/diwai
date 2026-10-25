> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# SYSTEM SECURITY PLAN

## NIST SP 800-171 Rev 2 Compliance

[SYSTEM-OWNER] LLC dba [ORGANIZATION]\
**System Name:** [DOMAIN.ORG] SecureMac Reference System\
**Domain:** [DOMAIN.ORG]\
**Version:** 2.18 **Date:** August 12, 2026\
**Classification:** CONFIDENTIAL BUSINESS INFORMATION

**Distribution Notice:** This document contains proprietary business information, trade secrets, and confidential system security details of [SYSTEM-OWNER] LLC. Unauthorized disclosure may cause competitive harm. Upon submission to U.S. Government agencies, this document shall be marked and protected as Controlled Unclassified Information (CUI) per 32 CFR Part 2002.

## DOCUMENT CONTROL

**Document Status:** Approved — Pending Signature\
**Security Classification:** CONTROLLED UNCLASSIFIED INFORMATION (CUI)\
**Distribution:** Limited to authorized personnel only

| Name / Title                       | Role         | Signature / Date  |
|:-----------------------------------|:-------------|:------------------|
| [SYSTEM-OWNER], Owner/Principal | System Owner | \____\_ Date: \____\_ |
| [SYSTEM-OWNER], Owner/Principal | ISSO         | \____\_ Date: \____\_ |

**Review Schedule:** Quarterly or upon significant system changes\
**Next Review Date:** November 1, 2026 (aligned with POA&M quarterly review)

### Document Revision History

| Version          | Date       | Author     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-----------------|:-----------|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0              | 04/10/2026 | [SYSTEM-OWNER] | Initial SSP — [DOMAIN.ORG] SecureMac Reference System. Apple Silicon Mac Mini M4 Pro host with UTM Rocky Linux 9.7 aarch64 FIPS VM. pf firewall operational. Rack installation complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 1.1              | 04/12/2026 | [SYSTEM-OWNER] | Network cutover complete. services.[DOMAIN.ORG] VM live at [LAN-IP-REDACTED] on LAN interface (en6). 389-DS LDAP directory (dc=diwai,dc=org) operational.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 1.2              | 04/15/2026 | [SYSTEM-OWNER] | YubiKey Nano 5C FIPS PIV deployment attempted. Lockout incident: unknown PIV PIN after cert pairing; recovery via sysadmin break-glass account; certs unpaired. Host returns to password-only auth. POA&M-001 opened (YubiKey PIV re-pairing).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1.3              | 05/11/2026 | [SYSTEM-OWNER] | Wazuh SIEM (Manager + Dashboard + Indexer) operational on services.[DOMAIN.ORG] VM. Suricata 7.0.13 IDS deployed. VirusTotal integration operational. Apache httpd + LDAP dashboard auth (securemac.[DOMAIN.ORG]) operational.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1.4              | 05/13/2026 | [SYSTEM-OWNER] | SecureMac dashboard LDAP auth operational. mod_authnz_ldap configured against 389-DS. ACI fix applied for group member reads.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 1.5              | 05/15/2026 | [SYSTEM-OWNER] | Infrastructure hardening: nginx 1.31.0 reverse proxy deployed (ai.[DOMAIN.ORG] HTTPS, LAN-only). Open Web UI 0.9.5 bound to localhost only. USB Guard re-enabled (mode: on). Time Machine auto-mount LaunchAgent deployed (17-day backup gap root cause resolved). YubiKey PIV lockout incident (round 2): smartcard certs unpaired again; sysadmin break-glass used for recovery.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 1.6              | 05/30/2026 | [SYSTEM-OWNER] | SCAP compliance scanning operational: VM OpenSCAP CUI 102/102 (100%), Mac mSCP 126/134 (94%). Weekly automated scans with compliance dashboard at securemac.[DOMAIN.ORG].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2.0 / 2.11       | 06/05/2026 | [SYSTEM-OWNER] | **STRUCTURAL CORRECTION:** SSP rewritten from scratch as a [DOMAIN.ORG]-specific document. Prior versions (1.0–1.9 of the predecessor conflated SSP) used the CyberInABox ([DOMAIN.ORG]) SSP as a structural template, which resulted in conflation of two architecturally distinct systems. This version documents only the [DOMAIN.ORG] SecureMac Reference System. CyberInABox is a separate system with its own SSP and SPRS score. SPRS self-assessment conducted: 98/110 (89.1%). New [DOMAIN.ORG] POA&M v1.0 issued concurrently. (Version numbering aligned with cyberhygiene-docs series; 2.0 and 2.11 are identical in content.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **2.12**             | **06/06/2026** | **[SYSTEM-OWNER]** | **MFA STRATEGY CHANGE — YUBIKEY ABANDONED:** YubiKey Nano 5C FIPS PIV hardware-token approach abandoned for the Mac host after a second lockout incident confirmed the solution is too technically fragile for reliable production use (PIV PIN lockout, certificate-pairing brittleness — see 1.2 and 1.5 above). MFA strategy for the Mac host changed to **TOTP via Authenticator app (RFC 6238)** — the same approach already targeted for the services.[DOMAIN.ORG] VM, unifying the remediation path for 3.5.3/3.7.5 across the whole [DOMAIN.ORG] system. **POA&M-001 (YubiKey PIV re-pairing) closed — superseded by strategy change.** New item **POA&M-007** opened: TOTP Authenticator app enrollment on the Mac host ([USERNAME] account). IA Policy (TCC-IAP-001) updated to v1.1 to reflect the unified TOTP approach. SPRS unchanged: 98/110 (89.1%) — gap remains open until POA&M-004 and POA&M-007 are both complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **2.12 (finalized)** | **06/11/2026** | **[SYSTEM-OWNER]** | **FINALIZED FOR SIGNATURE.** Open Drafting Questions resolved: (1) POA&M numbering retained as [DOMAIN.ORG]-specific (POA&M-001 closed / POA&M-007 opened), not renumbered to the conflated CPN's POA&M-046/047; (2) shared CyberInABox controls (policy set §6, physical perimeter §4.10, NAS FIPS-boundary note §4.13) remain documented inline as common controls, not split into a separate document — **superseded by the "2.12 (corrected)" entry below**. DRAFT NOTE and Open Drafting Question callouts removed; **Document Status** changed to **Approved — Pending Signature**. **Document ID correction:** the Rev. 2.12 (06/06/2026) entry above cites "TCC-IAP-001" — this is incorrect. TCC-IAP-001 is a CyberInABox/CPN-scoped document (FreeIPA-based MFA, dated 02/15/2026) and does not describe [DOMAIN.ORG]. The [DOMAIN.ORG]-specific Identification and Authentication Policy is **DIWAI-IAP-001** (v1.0, 04/10/2026 — the document that actually documents the YubiKey approach abandoned 06/06/2026). **DIWAI-IAP-001 has now been updated to v1.1** (06/11/2026) to reflect the unified TOTP MFA strategy. `[DOMAIN.ORG]_Unified_POAM_v1.1.md` (POA&M-001 through POA&M-007) has also been authored, in `Compliance/POAM/`. Both companion-document items tracked in Appendix D during the initial finalization pass are now resolved; §6, Appendix C, and §4.5 below have been corrected from TCC-IAP-001 to DIWAI-IAP-001 accordingly. (A broader review of the remaining `TCC-*-001` citations in §6/Appendix C against the parallel `DIWAI-*-001` policy set is recommended — see Appendix D Review Focus Areas — but is out of scope for this finalization pass.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **2.12 (corrected)** | **06/11/2026** | **[SYSTEM-OWNER]** | **INDEPENDENCE DETERMINATION — FULL DOCUMENT-ID PURGE.** Per explicit direction: *"[DOMAIN.ORG] shares [no] company policies with another reference system. It is an independent system and it is a stand-alone."* This supersedes item (2) of the "2.12 (finalized)" entry above — [DOMAIN.ORG]'s policy set, controls, and evidence are NOT shared, common, or inherited with the CyberInABox/CPN reference system, even where physical co-location (shared rack) is a true underlying fact. Changes made: **(a)** all 10 remaining `TCC-*-001` policy citations in §6 and Appendix C corrected to their `DIWAI-*-001` equivalents (v1.0, 04/10/2026): DIWAI-IRP-001, DIWAI-RA-001, DIWAI-PS-001, DIWAI-PE-MP-001, DIWAI-SI-001, DIWAI-AUP-001, DIWAI-AAP-001, DIWAI-CMP-001, DIWAI-ATP-001, DIWAI-SCP-001 (DIWAI-IAP-001 v1.1 already corrected in the prior entry); **(b)** ~9 inline citations corrected throughout §3/§4 (3.1.21 AUP/USB → DIWAI-AUP-001 §4.2; 3.6.1/3.6.3 → DIWAI-IRP-001; 3.7.3-3.7.4 and media disposal → DIWAI-PE-MP-001 §4.5, correcting a stale "§2.6" section reference; 3.9.2 → DIWAI-PS-001; 3.11.1 → DIWAI-RA-001); **(c)** former §3.3 and §4.10 "shared physical security controls... inherited by both SSPs" notes rewritten — [DOMAIN.ORG]'s physical/media protection controls are now documented solely via DIWAI-PE-MP-001, independent of any physical co-location; **(d)** §4.2 (3.2.1, 3.2.2, 3.2.3) downgraded **IMPLEMENTED → PARTIAL** after removing the sole supporting citation, "TCC-SAT-FY2026" (a CyberInABox-specific training-completion record) — no [DOMAIN.ORG]-specific security-awareness training delivery/completion record exists. **New POA&M-008 opened** ([DOMAIN.ORG]-specific security awareness training delivery + records, target Q3 2026, SPRS impact **TBD — pending confirmation**, see §10/§11/§12). `[DOMAIN.ORG]_Unified_POAM_v1.1.md` **updated to v1.1 (corrected)** to add POA&M-008. The 98/110 (89.1%) SPRS figure appearing elsewhere in this document is the **last-confirmed score and does not yet reflect POA&M-008** — see §11 caveat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **2.18 (amended)**   | **09/13/2026** | **[SYSTEM-OWNER]** | **POA&M CROSS-REFERENCES REPOINTED v1.30 → v1.31; ONE ITEM OPENED AGAINST THIS DOCUMENT.** **(a)** The live POA&M pointers in §1.3, §10 and Appendix D now cite `CUI_[DOMAIN.ORG]_Unified_POAM_v1.32.md`, with counts updated to **64 tracked items, POA&M-001 through POA&M-074, 39 closed, 25 open**. The 08/12 revision-history entry is a point-in-time citation and is **deliberately left at v1.30** per the rule in `DIWAI-CR-2026-08-09` §7. **(b) POA&M-074 opened against §3.4 of this document:** the retired-components row asserts *"Prometheus + node-exporter retained, so metrics collection is unaffected"*, but **C90/C91 (**`DIWAI-CR-2026-08-13`**) disabled both on 2026-08-04**, two days after that text was written. Verified 2026-09-13: both `disabled`, nothing on 9090, no metrics retained since 2026-08-04. **The §3.4 text is left uncorrected at this revision** — the correction is the item's remediation and is scheduled for the next substantive reissue, so the defect stays visible in the register rather than being silently edited away. **(c) No control narrative, no compliance determination, no SPRS change** — AU-6 / 3.3.3 and 3.14.7 rest on Wazuh, Suricata and auditd (C64/C65), all continuously running.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **2.18 (amended 19)** | **10/09/2026** | **[SYSTEM-OWNER]** | **PASSWORD LENGTH 14 → 16 AND LOCKOUT ALIGNED TO THE DoD Rev 3 PARAMETERS; RECORD CORRECTIONS.** **(a)** `DIWAI-CR-2026-10-11`: 389-DS and Mac minimum length 16; VM faillock counting window 300 s; Mac lockout 5 consecutive failures; each proven by refusal. **(b)** §3.1.8 and Appendix E.4 corrected: the VM was documented as "5 attempts / 30-minute lockout" but is configured for 3 attempts and a 15-minute lock (first noted in `DIWAI-CR-2026-09-03`). **(c)** Remaining "weekly patch review" wording in 3.7.1, 3.11.3, 3.14.1, 3.14.3 and E.3 corrected to monthly, matching amended 9. **(d)** 3.6.3 text corrected: the IR tabletop was conducted and signed on 2026-08-03 (`DIWAI-IR-TTX-001`); the known-gaps list, the control row and the deficit table still said it had not been held. **(e)** §11 deductions ledger and the §1.4 outstanding-deficits list rebuilt to the 100/110 determination: the four open deductions (3.5.3 −3, 3.13.5 −5, 3.10.4 −1, 3.5.6 −1) are listed as open; every other row of the 2026-08 table is kept under "recovered" with the date and evidence of its recovery; a score history is added; no weight and no determination is changed. **(f)** The 3.5.3 and 3.7.5 control rows and the Mac MFA status paragraph corrected to the real state: TOTP required on the VM; TOTP on the Mac restored 2026-10-09 after being absent 2026-09-03 to 2026-10-09 (`DIWAI-CR-2026-10-11`, finding 7). **(g)** Appendix E.4 gains the password-expiration row: 90 days for interactive user accounts, with the service, break-glass and reserved-account exemptions stated (`DIWAI-CR-2026-10-11`). **(h) No SPRS change.** |
| **2.18 (amended 20)** | **10/09/2026** | **[SYSTEM-OWNER]** | **PASSWORD EXPIRATION: VM LOCAL ACCOUNT AND `root` EXEMPTION.** Appendix E.4 (password expiration) now lists the VM local `[USERNAME]` account as enforced (`chage -M 90`; password expires 2027-01-07) and adds the VM operating-system account `root` to the stated exemptions, beside `svc-nas`, `demo_user` and `sysadmin`. `DIWAI-CR-2026-10-12`. **No SPRS change.** |
| **2.18 (amended 21)** | **10/09/2026** | **[SYSTEM-OWNER]** | **POST-UPDATE ROUTINE.** The Mac MFA status paragraph (§3.2) now states that after every macOS update the Mac SSH TOTP check is read at once (Patch Review Procedure DIWAI-PR-001 v1.3 §4.7; `fix-mscp-regression.sh` step 5). Wording only; no control and no SPRS change. |
| **2.18 (amended 22)** | **10/18/2026** | **[SYSTEM-OWNER]** | **MAC STUDIO TOOLS, THREE DOCUMENT LIBRARIES, REPLACEMENT TIME MACHINE DRIVE.** **(a)** `DIWAI-CR-2026-10-13`: §3.2 Component 1 records the Contract Library, RFPShred and the contract tools brought from the Mac Studio, a new Compliance library beside the Sysadmin library (each upload page now names its library), the removal of `gpt-oss-20b` (it was "on disk but barred"), and the Gemma 4 26B model (previously unrecorded). **(b)** `DIWAI-CR-2026-10-14`: the Time Machine drive failed and was replaced; the USB Guard allowlist, §3.1.20 and the backup description now carry the new drive's UUID `[HW-UUID-REDACTED]`; the new drive is FileVault-encrypted; the guard was off for 1 h 39 min during the 2026-10-18 transfer (recorded in the change record). **Open items recorded, not resolved:** the failed drive's failure date and backup gap; whether the transfer drive `AI-TRANSFER` is encrypted; ownership ([DOMAIN.ORG] or [DOMAIN.ORG]) of some documents now in the Compliance library. **No control determination, no SPRS change.** |
| **2.18 (amended 23)** | **10/19/2026** | **[SYSTEM-OWNER]** | **MAC INACTIVITY ENFORCEMENT RECORDED AND RETESTED; LIBRARY RECORDS UPDATED; 3.5.6 POINT STAYS WITHHELD UNTIL THE VM IS COVERED.** **(a)** `DIWAI-CR-2026-10-17`: the Mac daily job `diwai-inactivity-enforce` (installed 2026-09-13) is recorded; §1.4, the open-deductions table and Appendix E.4 now say the directory and the Mac are enforced and the VM's local accounts are not. The disable path was retested on 2026-10-19 on a disposable account (login refused); the job's `verified` field is unreliable, a limitation of its check and not of the enforcement. **No score change:** SPRS stays 100/110 (Rev 2); the owner decided on 2026-10-19 to keep 3.5.6 withheld until the VM is covered. The 2026-09-13 amendment rows are history and were left as written. **(b)** `DIWAI-CR-2026-10-16`: the library app is now `DIWAI Sysadmin Library.app`; the Compliance library holds 175 documents; read-only lookup tool `requirement_lookup`; XLSX and OCR readers; `openpyxl` added (SBOM v3.16). |
| **2.18 (amended 24)** | **10/19/2026** | **[SYSTEM-OWNER]** | **VM LOCAL ACCOUNTS COVERED FOR INACTIVITY; MAC CHECK CORRECTED; MONITOR SPLIT; 3.5.6 POINT STILL WITHHELD PENDING THE OWNER'S DECISION.** **(a)** `DIWAI-CR-2026-10-18`: a daily job on the VM (`diwai-inactivity-enforce-vm`, 04:25) expires local accounts idle 90 days (`root` exempt, console-only, password reset by the owner and tested); proven on a disposable account, with PAM refusing the expired account; Wazuh collects its log. **(b)** `DIWAI-CR-2026-10-17` §3A: the Mac job's confirmation check, which had read `verified=NO` on a disable that worked, was corrected and retested (5 of 5). **(c)** The control-health monitor now checks the VM job (check 16) and tells the Mac's heartbeat from the VM's; before this the two shared one log path and one could have masked the other. **(d) No score change:** SPRS stays 100/110 (Rev 2). §1.4, the open-deductions table and Appendix E.4 now say both hosts are covered. The 2026-09-13 and 2026-10-19 (amendment 23) rows are history and were left as written. |
| **2.18 (amended 25)** | **10/22/2026** | **[SYSTEM-OWNER]** | **3.5.6 POINT AWARDED — SPRS 100 → 101/110 (REV 2 BASIS) ON OWNER DECISION.** **(a)** Owner decision 2026-10-22, taken after the withholding condition set on 2026-10-19 (both hosts covered) was met and the first scheduled runs were seen. **(b) Evidence:** the directory limit proven by refusal (`DIWAI-CR-2026-09-08`); the Mac and VM daily jobs each proven on a disposable account (`DIWAI-CR-2026-10-17`, `-10-18`); and the first scheduled runs observed on both hosts on 2026-10-20, -21 and -22 (Mac 04:20, VM 04:25: `RUN … disabled=0 warned=0`), with the control-health monitor passing all 33 checks and checks 13 and 16 OK. **(c) Stated limits:** no real account has yet aged 90 days, so the jobs have disabled only disposable test accounts; the warning mail path is unexercised; never-logged-in directory entries are not yet covered (POA&M-076 stays open for these). **(d) Open deductions −10 → −9** (3.5.3 −3, 3.13.5 −5, 3.10.4 −1). Revision 3 withdrew 3.5.6 (its intent is in 03.01.01 f.02); this figure is Rev 2 only. §1.4, the SPRS statements, the open-deductions and recovered tables and Appendix E.4 updated. |
| **2.18 (amended 26)** | **10/22/2026** | **[SYSTEM-OWNER]** | **ONLYOFFICE 10.0.0 AND A LOCAL-ONLY AI CONNECTION; ENCRYPTED-DNS BLOCK ON THE MAC FIREWALL; NO SCORE CHANGE.** **(a)** `DIWAI-CR-2026-10-19` Parts A and B (owner-approved 2026-10-22; record still unsigned): ONLYOFFICE Desktop Editors upgraded 9.4.0 → 10.0.0 on the Mac host (SBOM v3.17), automatic updates still off; the app's bundled AI plugin is configured with one provider, the LM Studio server on `127.0.0.1:1234` (no key; model `google/gemma-4-26b-a4b-qat`). Connection checks during setup and two test prompts showed the editor's AI traffic going only to that loopback address. LM Studio now has CORS enabled (needed by the editor) and its "per-request MCPs" option off. **(b)** The vendor's separate "AI Tools (beta)" add-on (command execution, MCP, web search) is **not installed** and is to be tried first on a separate non-admin account (CR Part C, not started). **(c)** Observed and recorded: the app contacts the vendor's template servers and CDN, GitHub's content servers when its Plugin Manager is open, and (since first install on 2026-10-06, unrecorded until now) public encrypted-DNS services. **`/etc/pf_diwai.conf` now blocks encrypted DNS (ports 443 and 853) to 1.1.1.1, 1.0.0.1, 162.159.61.3, 172.64.41.3, 104.16.248.249, 104.16.249.249, 8.8.8.8 and 8.8.4.4**, for the Mac and for the CUI network's traffic through it; plain DNS (port 53) is unchanged. Tested: refusal confirmed, plain DNS, web fetches and the VM unaffected. **(d) Limits:** no CUI document has been used with the AI; the traffic checks are connection logs of an encrypted channel, not proof of content; the owner's signature on the change record is pending. No SPRS change (100/110 → **101/110** applies only to amendment 25). |
| **2.18 (amended 27)** | **10/23/2026** | **[SYSTEM-OWNER]** | **ONLYOFFICE "AI TOOLS (BETA)" ADD-ON NOT APPROVED (TRIAL FAILED); CHANGE RECORDS 16 TO 19 SIGNED; NO SCORE CHANGE.** **(a)** `DIWAI-CR-2026-10-19` Part C was run on 2026-10-22 on a disposable standard user account (`aitrial`, no admin rights, no read access to the owner's home, `.ssh`, the Nextcloud data folder or the libraries, no internet by a `pf` rule, LM Studio on loopback only, MCP and web search off). **Result: FAIL.** The add-on ran shell commands and read a file **with no approval prompt, and it has no approval setting**; the harmless tests were held only by the account's own limits (reading the owner's file and writing to `/etc` were refused by the operating system). A hidden instruction in a test document was not carried out, which was the model's choice and is not a control. **(b) Decision (owner, 2026-10-22): the "AI Tools (beta)" add-on is not approved and is not installed on the owner's account or any other.** The trial account, its home folder and its firewall rule were removed. It may be reconsidered only if the vendor adds a working approval step, and then re-tested the same way. The bundled AI plugin (text chat and edit, one loopback provider, MCP and web search off) is unchanged from amendment 26. **(c) Section 3.4.9** now states this decision. **(d)** Change records `DIWAI-CR-2026-10-16`, `-10-17`, `-10-18` and `-10-19` were signed by the owner's instruction on 2026-10-23 (the correction to amendment 26: its "record still unsigned" and "Part C not started" are history). LM Studio CORS was turned off again on 2026-10-23. **(e) Limits:** one model and one test document; the network test of the trial account cannot show what the add-on would contact on an account with internet access; no CUI document has been used with the AI. **No control determination, no SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 28)** | **10/23/2026** | **[SYSTEM-OWNER]** | **FAPOLICYD WORDING CORRECTED; NO CONTROL DETERMINATION, NO SCORE CHANGE.** Checked on the VM on 2026-10-23: `fapolicyd` 1.4.5 is active and enabled, `permissive = 0` (enforcing), `trust = rpmdb,file`, `integrity = none`. **(a)** The component table said "1.3.x"; it now says 1.4.5 and states the mode and trust sources. **(b)** §3.4.9 had said fapolicyd and Gatekeeper "prevent unauthorized software installation"; fapolicyd controls what may **run**, not what is installed, so the text now says that and names change control (3.4.3) for installation. **(c)** §3.4.9 now records that fapolicyd's integrity checking is off and that file-integrity monitoring (Wazuh) is what detects changes to trusted files. **Not verified:** the rule list under `/etc/fapolicyd` is root-only and was not read, so the "deny-by-default" wording rests on enforcing mode and the trust model, not on reading the final rule. SPRS stays 101/110 (Rev 2). |
| **2.18 (amended 29)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.5.6 WARNING PATH PROVEN ON BOTH HOSTS, WITH RECEIPT IN THE OWNER'S GMAIL; NO SCORE CHANGE.** **(a)** Amendment 25 (c) listed the 80-day warning mail path as unexercised; it is now exercised. **VM** (`DIWAI-CR-2026-10-18` §6B, §6C): on a disposable account backdated 85 days the job logged WARNING, did not disable the account (the system's own login check still accepted it) and mailed the owner; the job's recipient line was extended on 2026-10-23 so the mail also goes to the owner's Gmail, and **receipt in Gmail was confirmed**. **Mac** (`DIWAI-CR-2026-10-17` §3B): the WARNING line reaches Wazuh as alert 100223 within a second; an untagged run made the control-health monitor fail check 13 and mail the owner's Gmail, and **receipt was confirmed**. The Mac route runs through the monitor by design (Wazuh's own email is disabled, `DIWAI-CR-2026-09-07`). **(b) Stated limits unchanged otherwise:** both tests used backdated disposable accounts; no real account has aged 90 days, so no real account has been disabled; never-logged-in directory entries are not yet covered (POA&M-076 stays open for these). **(c) Also on 2026-10-23:** the VM control-health monitor's check 15 (Mac SSH still demands TOTP) was found unreliable from 2026-10-19 to 2026-10-23 (a function removed by the 10-19 patch) and was fixed (`DIWAI-CR-2026-10-18` §6A). **No control determination, no SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 30)** | **10/23/2026** | **[SYSTEM-OWNER]** | **FAPOLICYD RULES READ AND VERIFIED; THREE READ-ONLY DIAGNOSTIC SCRIPTS ALLOWED WITHOUT A SUDO PASSWORD; NO SCORE CHANGE.** **(a)** The compiled fapolicyd rules on the VM were read for the first time (2026-10-23, with the new read-only script): mode enforcing (`permissive = 0`), and for **execution** the last rule is `deny_audit perm=execute all : all` after `allow perm=execute all : trust=1`, so a binary that is not trusted (package database or local trust file) is refused. **Nuances now stated in §3.4.9:** shell scripts are allowed for every user by rule (`allow perm=any all : ftype=text/x-shellscript`); Python, Java and JavaScript files are denied unless trusted, except when run by root; root running a trusted program is allowed everything; opening (reading) files is allowed by default (`allow perm=open all : all`). Amendment 28's "rule list not read" limit is cleared. **(b) `DIWAI-CR-2026-10-21`:** on the VM, `/etc/sudoers.d/zz-diwai-ro` lets the owner's account run **exactly three** read-only, root-owned scripts in `/usr/local/libexec/diwai-ro/` without a password (fapolicyd mode and rules; the dashboard generator's text with key paths masked; Wazuh alerts for a warning line, one validated account-name argument). Every other command still asks for the password (`DIWAI-CR-2026-10-06`); the folder and scripts cannot be edited by the owner's account; sudo logs every use. Tested as the owner's account, 7 of 7 passed. **(c)** §3.1.5 row notes the exception. **No control determination, no SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 31)** | **10/23/2026** | **[SYSTEM-OWNER]** | **THE SAME READ-ONLY SUDO EXCEPTION FOR THE MAC (TWO SCRIPTS); LIVE FIREWALL READ; NO SCORE CHANGE.** `DIWAI-CR-2026-10-22`: on the Mac host, `/etc/sudoers.d/zz-diwai-ro` lets the owner's account run **exactly two** read-only, root-owned, argument-free scripts in `/usr/local/libexec/diwai-ro/` without a password (the live `pf` firewall status, rules and counters; the inactivity job's state, log tail and launchd state). Everything else still asks for the password; the folder and scripts cannot be edited by the owner's account; sudo logs every use. Tested as the owner's account, 6 of 6 passed. **First read of the live ruleset (not just its file):** pf Enabled, the four encrypted-DNS block rules loaded, no rule for the removed trial account (`DIWAI-CR-2026-10-19` §2B, §2D). The §3.1.5 row now names both exceptions. **No control determination, no SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 32)** | **10/23/2026** | **[SYSTEM-OWNER]** | **OBJECTIVE-LEVEL COMPLIANCE 42 → 45/110 (ASSESSMENT REVISION 1.2); CONTROL FAMILY STATUS TABLE UPDATED; SPRS UNCHANGED.** The Tier A re-walk of `DIWAI-ORW-001` (owner request 2026-10-23): evidence cited by the worklist was verified first, then re-determined in place with each superseded determination retained. **Recovered: 3.4.9, 3.11.1, 3.11.3** (family table: CM 3 → 4 met, RA 0 → 2 met; total 42 → 45 met, 66 → 63 not met). **Moved without recovery:** 3.4.3 [b][c], 3.5.6 [a][b], 3.11.2 [b][c], 3.12.3 [a], 3.13.1 [a]. **Not recovered:** 3.10.2, 3.10.6, 3.6.1, 3.6.2, 3.12.2, 3.12.3, 3.13.1, 3.4.3 (and 3.11.2), each for a stated reason; the lower status was kept where a judgement was close (the owner's rule for disputed values). **A finding raised by the re-walk:** 11 open POA&M items carry a target of "Q3 2026", which has passed (POA&M-050, -052, -058, -060, -061, -062, -063, -064, -066, -068 and -069); their target dates need review, and until then 3.12.2 [b] cannot be satisfied. The dashboard reads the family-table TOTAL row, so its "Strict 800-171A objectives met" card moves to 45/110 at the next refresh. **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 33)** | **10/23/2026** | **[SYSTEM-OWNER]** | **APPLICABILITY AND INTERPRETATION STATEMENT ISSUED (`DIWAI-APP-001`); 3.1.18 AND 3.1.19 NOT APPLICABLE; OBJECTIVE-LEVEL 45 → 47/110; SPRS UNCHANGED.** New §2.7 points to the statement. It records, for all 110 requirements, whether each applies to a one-person company with a secured home office and how it is interpreted: **95** applicable as written, **7** single-operator interpretations (3.1.2, 3.1.4, 3.1.5, 3.1.6, 3.3.9, 3.9.1, 3.12.1), **4** provisions for additional personnel (3.2.1, 3.2.2, 3.2.3, 3.9.2) and **4 not applicable** (3.1.18, 3.1.19, 3.7.6, 3.13.14). Owner facts of 2026-10-23: no mobile device handles CUI (consistent with `DIWAI-AUP-001` §5.3); the paid assistant is a provision only; mail, webmail and VPN are published by decision, mail being the FIPS 140 channel for CUI (so 3.13.5 stays applicable and not met). **Observed and recorded, not changed:** the Mac's Wi-Fi radio is On but not associated (it was Off on 2026-09-15). Assessment revision 1.3; family table AC 7 → 9 met, total 45 → 47 met, 63 → 61 not met. **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 34)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.11.2 MET; OBJECTIVE-LEVEL 47 → 48/110; RISK ASSESSMENT FAMILY 3 OF 3; SPRS UNCHANGED.** `DIWAI-PR-001` v1.4 §6.2 (a scan runs on demand, within one working day, when a new vulnerability is reported; the 72-hour clock for a new CRITICAL starts at that report) was exercised on 2026-10-23: the Mac scan found nothing new; **the VM scan found a new patch-class CRITICAL (`webkit2gtk3-jsc`, RLSA-2026:84583)**, patched 31 minutes after detection (`dnf history` 70), rescan clean, monitor check 5c cleared. Recorded in `DIWAI-PR-LOG`. Stated limit: the trigger was a drill; no vendor-reported vulnerability has yet been handled under §6.2. Assessment revision 1.4; family table RA 2 → 3 met, total 47 → 48 met, 61 → 60 not met. **`DIWAI-APP-001` signed 2026-10-23** (facts F2, F4, F5 in effect). **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 35)** | **10/23/2026** | **[SYSTEM-OWNER]** | **FULL RE-WALK BEGUN: SYSTEM AND INFORMATION INTEGRITY 2 → 6 OF 7; OBJECTIVE-LEVEL 48 → 52/110; MONTHLY PATCH REVIEW RUN; SPRS UNCHANGED.** **(a)** Owner direction 2026-10-23: the objective-level table understated the system and must be corrected, not removed. Re-walked against current evidence: **3.14.1** (Appendix E.3 defines identify, report, correct; E.3 now states the reporting time, 30 minutes for an actionable CRITICAL), **3.14.3**, **3.14.6**, **3.14.7** are met; **3.14.4** stays partial. Assessment revision 1.5; the count is computed by `scripts/assessment-tools/count.py` so the assessment and this table cannot disagree. **(b) Monthly patch review run 2026-10-23** (`DIWAI-PR-LOG`): VM, 42 patch-class advisories (`dnf history` 71) and Remi PHP 8.2.35 (history 72, RLSA-2026:87072); Mac, `libssh2`, `openssh`, `php@8.3` 8.3.36. VM 14 of 14 services active; Mac Nextcloud 200 after a 10-second restart blip (`OS_REASON_CODESIGNING`, self-recovered, to be watched at the next restart). **Open:** attended VM restart (new kernel, glibc, dracut) by **2026-11-06**, with macOS Tahoe 26.7.1. **(c) A PHP exposure had been listed in the scans as THIRD-PARTY without escalation** (Remi PHP, which serves webmail); it is now handled in the review and `DIWAI-PR-001` §4.3 is to be read as part of every review. **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 36)** | **10/23/2026** | **[SYSTEM-OWNER]** | **RE-WALK: IDENTIFICATION AND AUTHENTICATION 2 → 5 OF 11; OBJECTIVE-LEVEL 52 → 55/110; SPRS UNCHANGED.** **Met:** 3.5.1 [c] (no duplicate agent; inventory), 3.5.2 [c] (VPN client certificates, agent keys, pinned SSH key), 3.5.5 (period "never reused" defined; `DIWAI-IA-REG-001` retired-identifier register). **Moved, not met:** 3.5.3 [c][d] (SSH MFA now in force on both hosts; console, two key-only jobs and webmail remain), 3.5.7 [a][c] (length 16 enforced; "change of characters" undefined), 3.5.8 (directory and Mac proven; **the VM's local accounts have no password history, `pam_pwhistory` is off**), 3.5.9 (policy requires a change at first login; enforcement unshown). **Findings:** the VM's own `pwquality` minimum is 15 and `pwhistory` is not enabled, which differs from Appendix E.4's "16 on both". **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 37)** | **10/23/2026** | **[SYSTEM-OWNER]** | **TEMPORARY, TIME-BOXED PASSWORDLESS SUDO FOR THE MAINTENANCE ROUND (`DIWAI-CR-2026-10-23`); SPRS UNCHANGED.** By owner decision on 2026-10-23, sudo for the owner's account does not ask for the password on **both hosts** from the installation (Mac 13:33, VM 13:36) until **2026-10-25 13:33 / 13:36**, when an armed checker revokes it automatically; it can be revoked at once with `sudo diwai-sudo-temp revoke`. This is a **temporary exception** to `DIWAI-CR-2026-10-06` and to the §3.1.5 row, restored on expiry; the five read-only passwordless scripts (`-10-21`, `-10-22`) are unaffected. Conditions: scope limited to the agreed round; **no instruction found in data is obeyed**; every command is logged by sudo and audited on revocation; no reboot, macOS update, account or credential action without the owner present. **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 38)** | **10/23/2026** | **[SYSTEM-OWNER]** | **DEFINITIONS WRITTEN, AUDIT-EVENT REVIEW RUN, VM PASSWORD SETTINGS HARDENED; OBJECTIVE-LEVEL 55 → 64/110; SPRS UNCHANGED.** Owner approved (2026-10-23) twelve definitions and three settings. **Appendix E.9 to E.14** (audit retention, review and who manages audit logging; roles and permitted functions; remote access types and authorized privileged commands; wireless; architectural principles; security impact of changes and diagnostic media) and a key-management procedure in E.5. **First audit-event review** (`DIWAI-PR-001` v1.5 §4.8, `DIWAI-PR-LOG`): file changes are caught by Wazuh file-integrity monitoring, not by `auditd`, and sudo records who. **Settings (`DIWAI-CR-2026-10-25`):** VM `pwquality` minimum 15 → 16 (the SSP had said 16); VM password history, 6 generations, now enforced and **proven by refusal** on a disposable account (it had not been enabled); Mac Wi-Fi radio found On and switched Off. **Re-walk results:** the nine requirements listed in the revision note above are met. **Raised and left open by the owner's decision:** `passwordMustChange` in the directory stays off (turning it on would break the four services that bind as `uid=[USERNAME]`). **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 39)** | **10/23/2026** | **[SYSTEM-OWNER]** | **NEXTCLOUD OFFICE RESTORED; MONITOR CHECK 17 ADDED (34 CHECKS); NO SCORE CHANGE.** `DIWAI-CR-2026-10-24`: the Collabora VM on the Mac had been down for 20 days (its root filesystem unreadable after the 2026-09-25 host panic; the guest sat in emergency mode) and nothing alerted. The machine was rebuilt (damaged disk kept aside), now **with no host folders mounted into it**; the container was recreated from the pinned image; Nextcloud Office answers again. **Monitor check 17** (Collabora discovery returns 200 with a `wopi-discovery` body, 502 means the machine is down) is live. **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 40)** | **10/23/2026** | **[SYSTEM-OWNER]** | **PASSWORD CHANGE INTERVAL 90 DAYS → THREE YEARS ON ALL THREE STORES; CREDENTIAL REGISTER AND MONITOR CHECK 18; POA&M-077 OPENED; NO SCORE CHANGE.** `DIWAI-CR-2026-10-26`. Owner decisions of 2026-10-23 on the Rev 3 approach (Rev 3 03.05.12.e). **Appendix E.4:** the "Password expiration" row is now a **change interval**: at least every three years and after any incident, for every password (none has a second factor on every path); enforced by the system (Mac 1095 days, VM `chage -M 1095`, directory `passwordMaxAge` 94,608,000 s; `[USERNAME]` next change 2029-10-08) and, for `root`, `sysadmin` and `svc-nas`, by the credential register `DIWAI-CRR-001` checked by monitor check 18 (**the monitor now runs 35 checks**). Proven on the VM: 1,000 days accepted, 1,100 refused. **Part C (the Rev 3 password screening list) is not installed and the policy says so: POA&M-077.** IA policy, AUP and CM policy lines updated. **No SPRS change:** stays 101/110 (Rev 2). |
| **2.18 (amended 41)** | **10/23/2026** | **[SYSTEM-OWNER]** | [PERSONNEL-SCREENING-NOTE-REDACTED] **(b)** The PS-4 termination procedure was run on a disposable account on the VM: lock, group removal and expiry in 1 second; correct password refused by the directory and the VM afterwards; two later attempts logged (err=53). Recorded in `DIWAI-EV-PS-2026-10-23`. **(c)** A second drill on the Mac host (a disposable local account, run 2026-10-23 14:40) was refused after the lock with a passing positive control. Nextcloud's own login could not be exercised (two-factor authentication blocked a scripted login), so the 3.9.2 [c] determination is unchanged. |
| **2.18 (amended 42)** | **10/23/2026** | **[SYSTEM-OWNER]** | **SOLE-OWNER SCREENING BASIS APPROVED (`DIWAI-CR-2026-10-27`); 3.9.1 DETERMINATION PENDING THE SIGNED ATTESTATION; NO SCORE CHANGE.** Owner approved, as drafted, a written basis for the owner's own access (company ownership, a signed attestation, the DD Form 2345 while in force) with full screening kept for every other person; `DIWAI-APP-001` v1.1 and a dated paragraph in `DIWAI-PS-001` section 3 record it. §4.9 rewritten. The 3.9.1 [a] objective moves to satisfied (64 → 65/110) only when the attestation is signed and filed; until then the count is unchanged. |
| **2.18 (amended 43)** | **10/23/2026** | **[SYSTEM-OWNER]** | **ATTESTATION SIGNED; 3.9.1 RECOVERED AS INTERPRETED; OBJECTIVE-LEVEL 64 → 65/110 (ASSESSMENT REVISION 1.8); SPRS UNCHANGED.** The owner's attestation of eligibility (`DIWAI-EV-PS-2026-10-23-S`) was signed by entry at the owner's explicit instruction and filed in `Compliance/Evidence/Personnel/`. With the basis approved in amendment 42, 3.9.1 [a] is satisfied as interpreted. Personnel Security 1 of 2 (3.9.2 [c] still partial: Nextcloud's own login refusal not shown). Control Family Status table recomputed (65/43/2). |
| **2.18 (amended 44)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.14.4 CLAIM CORRECTED: SURICATA RULES HAD NOT UPDATED SINCE 2026-04-09; REPAIRED; NO SCORE CHANGE.** The SSP said Suricata rules update automatically; the nightly job had failed 90 of 91 runs (`DIWAI-CR-2026-10-28`). Path fixed, Modbus/DNP3 rule groups skipped (their parsers are disabled), success logging corrected; rules updated 2026-10-23 and Suricata reloaded cleanly. 3.14.4 stays partial until the first scheduled run (2026-10-24 03:15) is seen. A monitor check for stale Suricata rules was proposed and declined by the owner (2026-10-23); detection of a repeat rests on reading the update log. |
| **2.18 (amended 45)** | **10/23/2026** | **[SYSTEM-OWNER]** | **INCIDENT REGISTER ISSUED AND APPROVED (`DIWAI-INCREG-001` v1.0); 3.6.2 RECOVERED; OBJECTIVE-LEVEL 65 → 66/110 (ASSESSMENT REVISION 1.9); SPRS UNCHANGED.** §4.6 row 3.6.2 now cites the register instead of the POA&M. Incident Response is 2 of 3; 3.6.1 stays partial because detection is still the gap. Entries INC-003 to INC-007 are reconstructed and say so. Backup `.bak-20261023-am45`. |
| **2.18 (amended 46)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.12.2 RECOVERED; OBJECTIVE-LEVEL 66 → 67/110 (ASSESSMENT REVISION 1.10); SPRS UNCHANGED.** Four overdue POA&M items fixed and verified (-061, -062, -064, -069) and seven re-dated with reasons on the owner's approval (`DIWAI-CR-2026-10-29`). Security Assessment is 3 of 4; 3.12.3 stays partial (POA&M-059). Backup `.bak-20261023-am46`. |
| **2.18 (amended 47)** | **10/23/2026** | **[SYSTEM-OWNER]** | **RECURRING OBLIGATIONS TAILORED AND RECORDED (`DIWAI-CR-2026-10-30`); NO COUNT CHANGE (67/110); SPRS UNCHANGED.** Schedule `DIWAI-SCH-001` (32 operating activities, 8 automated), eight policies aligned, ledger `DIWAI-LEDGER-001` and overdue report live. 3.12.3 [a] stays partial until the ledger holds dated entries over time. Backup `.bak-20261023-am47`. |
| **2.18 (amended 48)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.9.2 RECOVERED; OBJECTIVE-LEVEL 67 → 68/110 (ASSESSMENT REVISION 1.11); SPRS UNCHANGED.** Nextcloud lockout drill with a positive control (`DIWAI-EV-PS-2026-10-23-N`) found that the directory lock did not stop a Nextcloud app password; PS-4 now includes `occ user:disable` and token revocation (`DIWAI-CR-2026-10-31`). Personnel Security is 2 of 2. Backup `.bak-20261023-am48`. |
| **2.18 (amended 49)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.4.3 AND 3.4.5 RECOVERED; OBJECTIVE-LEVEL 68 → 70/110 (ASSESSMENT REVISION 1.12); SPRS UNCHANGED.** POA&M-048 closed on the owner's acceptance of the publish gate plus manual checking (`DIWAI-CR-2026-10-32`); `DIWAI-CMA-001` documents change authority and the administrative account inventory. Configuration Management is 7 of 9; 3.4.6 and 3.4.7 stay open. Backup `.bak-20261023-am49`. |
| **2.18 (amended 50)** | **10/23/2026** | **[SYSTEM-OWNER]** | **PORT BASELINE ISSUED AND NONESSENTIAL SERVICES REMOVED (`DIWAI-CR-2026-10-33`); NO COUNT CHANGE (70/110); SPRS UNCHANGED.** `DIWAI-PORTS-001` records every listener on both hosts. Removed: Mac AirPlay Receiver, stock nginx server on 8080, NetBIOS; the dead pf rule for 4190; VM cleartext POP3 and IMAP; the open Wazuh ports (1514 now Mac-only, 1515 closed). 3.4.6 and 3.4.7 stay partial until the Mac firewall change R4. Backup `.bak-20261023-am50`. |
| **2.18 (amended 51)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.7.5 AND 3.3.7 RECOVERED; OBJECTIVE-LEVEL 70 → 72/110 (ASSESSMENT REVISION 1.13); SPRS UNCHANGED.** SSH multifactor authentication proven by negative tests on both hosts and the owner's Mac login; the VM clock synchronised and guarded by `diwai-clock-guard` (`DIWAI-EV-MFA-TIME-2026-10-23`). Maintenance 4 of 6; Audit and Accountability 6 of 9. Backup `.bak-20261023-am51`. |
| **2.18 (amended 52)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.7.3 NOT APPLICABLE; OBJECTIVE-LEVEL 72 → 73/110 (ASSESSMENT REVISION 1.14); SPRS UNCHANGED.** The owner stated that no equipment is removed for off-site maintenance (`DIWAI-APP-001` v1.2 fact F10, `DIWAI-CR-2026-10-35`); the Physical and Media Protection Policy says so. Maintenance is 5 of 6. Backup `.bak-20261023-am52`. |
| **2.18 (amended 53)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.7.2 RECOVERED; OBJECTIVE-LEVEL 73 → 74/110 (ASSESSMENT REVISION 1.15); SPRS UNCHANGED.** `DIWAI-MNT-001` v1.0 (approved 2026-10-23) defines the approved maintenance tools, techniques and mechanisms and three tiers for AI assistants (`DIWAI-CR-2026-10-36`). Maintenance is 6 of 6. Backup `.bak-20261023-am53`. |
| **2.18 (amended 54)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.8.3 RECOVERED; OBJECTIVE-LEVEL 74 → 75/110 (ASSESSMENT REVISION 1.16); SPRS UNCHANGED.** Media sanitization (MP-6) rewritten for the media in use; log `DIWAI-MSL-001` opened; method exercised with positive controls (`DIWAI-CR-2026-10-37`, `DIWAI-EV-MP-2026-10-23`). Annual exercise added to the schedule (A13). No UNVERIFIED requirement remains. Backup `.bak-20261023-am54`. |
| **2.18 (amended 55)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.3.5 RECOVERED; OBJECTIVE-LEVEL 75 → 76/110 (ASSESSMENT REVISION 1.17); SPRS UNCHANGED.** `DIWAI-COR-001` v1.0 (approved 2026-10-23) defines audit correlation, review and reporting; exercised across sources (`DIWAI-EV-AU-2026-10-23-C`). Audit and Accountability is 7 of 9. Backup `.bak-20261023-am55`. |
| **2.18 (amended 56)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.3.2 RECOVERED; OBJECTIVE-LEVEL 76 → 77/110 (ASSESSMENT REVISION 1.18); SPRS UNCHANGED.** The portal (Apache), webmail (Dovecot) and Nextcloud now bind to the directory as `svc-apache`, `svc-dovecot` and `svc-nextcloud` (read-only, no access to password hashes) instead of the owner's account; the personal bind was scrubbed from a stale Grafana file (`DIWAI-CR-2026-10-38`). The change caused two short faults, recorded as INC-008. Audit and Accountability is 8 of 9. Backup `.bak-20261023-am56`. |
| **2.18 (amended 57)** | **10/23/2026** | **[SYSTEM-OWNER]** | **3.3.1 RECOVERED; OBJECTIVE-LEVEL 77 → 78/110 (ASSESSMENT REVISION 1.19); SPRS UNCHANGED.** Mac audit retention raised from 7 to 90 days (`DIWAI-CR-2026-10-39`); Appendix E.9 updated. Retention is configured now and accumulates over 90 days (verify 2027-01-21). **Audit and Accountability is 9 of 9.** Backup `.bak-20261023-am57`. |
| **2.18 (amended 78)** | **10/25/2026** | **[SYSTEM-OWNER]** | **3.4.6 AND 3.4.7 RECOVERED; OBJECTIVE-LEVEL 97 → 99/110 (ASSESSMENT REVISION 1.36); SPRS UNCHANGED.** The Mac firewall allow-list (R4 step 2, `DIWAI-CR-2026-10-34`) has been loaded since 2026-10-24 17:33: only the services VM may connect to the Mac itself (ports 22 and 443); the VM and the NAS are the only hosts passed through to the internet; everything else is refused and logged. Nine tests passed with automatic revert. Configuration Management is now 9 of 9. 3.1.1 [f] stays partial. Appendix on the Mac firewall rules updated in `DIWAI-PORTS-001`. |
| **2.18 (amended 77)** | **10/25/2026** | **[SYSTEM-OWNER]** | **WEBMAIL, MAIL-CLIENT PORTS AND VPN TAKEN OFF THE INTERNET (`DIWAI-CR-2026-10-51`); NO COUNT CHANGE (97/110); SPRS UNCHANGED.** Owner decision 2026-10-24 (choice B). Webmail answers only the CUI network; the mail address forwards port 25 only; OpenVPN is stopped and disabled and port 1194 is closed. Ten tests passed and the owner's phone could not open webmail from outside (the phone could not resolve names at all, so this shows non-reachability, not a 403). 3.5.3 stays partial because LAN logins are still password-only; 3.13.5 is unchanged because port 25 mail still ends on the same VM. §2.5.1, 3.1.14, 3.1.15 text and Appendix remote-access text updated. |
| **2.18 (amended 76)** | **10/24/2026** | **[SYSTEM-OWNER]** | **CORRECTION TO AMENDMENT 75: NO SHARED SWITCH IS PROVEN.** The owner traced the cables: the Netgear switch is on this network and the HP switch is on the owner's other network. The device with hardware address `54:07:7d:16:9d:f3` is therefore this network's own switch asking for an address, not a foreign device. Amendment 75's reading (a shared, unconfigured switch) was wrong and is withdrawn; what remains is the NAS answering on a second address of the other network (POA&M-032). `DIWAI-EXT-001` now lists the Netgear switch as an authorized device. No count change (97/110). Backup `.bak-20261024-netgearfix`. |
| **2.18 (amended 75)** | **10/24/2026** | **[SYSTEM-OWNER]** | **SHARED SWITCH FOUND; NO COUNT CHANGE (97/110); SPRS UNCHANGED.** The firewall capture showed a device of the owner's other network (a NETGEAR product) and a second NAS address on the CUI network's wire: the HP switch is shared and unconfigured, so the two networks share one broadcast domain. Recorded in §2.5.3 and `DIWAI-EXT-001`; the R4 allow-list is tightened so only the VM and the NAS pass through the Mac; separating the switch ports is open (POA&M-032). Backup `.bak-20261024-switch`. |
| **2.18 (amended 74)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.8.5 RECOVERED; OBJECTIVE-LEVEL 96 → 97/110 (ASSESSMENT REVISION 1.33); SPRS UNCHANGED (`DIWAI-CR-2026-10-50`).** The owner confirmed fact F11 (no medium containing CUI leaves the controlled area) and approved Appendix E.19 (media access and transport). 3.8.5 [b], accountability during transport, is not applicable while F11 holds; `DIWAI-APP-001` v1.4. A dry-run custody record (`DIWAI-EV-MP-2026-10-24`) shows the E.7 procedure working with the controls in place. Media Protection is 8 of 9. Backup `.bak-20261024-cr50`. |
| **2.18 (amended 73)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.5.10 RECOVERED ON THE OWNER'S CLARIFICATION AND A LIVE CHECK; OBJECTIVE-LEVEL 95 → 96/110 (ASSESSMENT REVISION 1.32); SPRS UNCHANGED (`DIWAI-CR-2026-10-49`, addendum).** The owner stated that NAS port 5000 is used only by people, never by scripts, with multifactor sign-in. A live probe confirmed port 5000 is plain HTTP and serves a page that redirects the browser to HTTPS on 5001 before any login form; the owner's description of port 5000 as HTTPS is corrected in Appendix E.18. The DSM API on 5000 still answers in the clear and is unused; that residual stays accepted (POA&M-066). Identification & Authentication is 9 of 11. Backup `.bak-20261024-cr49b`. |
| **2.18 (amended 72)** | **10/24/2026** | **[SYSTEM-OWNER]** | **NAS PORT 5000 KEPT OPEN BY OWNER DECISION; 3.13.8 RECOVERED; OBJECTIVE-LEVEL 94 → 95/110 (ASSESSMENT REVISION 1.31); SPRS UNCHANGED (`DIWAI-CR-2026-10-49`).** The NAS serves other clients, so its management port 5000 stays open; the owner's position, that the information on the NAS is encrypted before it arrives and unreadable by others, matches the backup procedures and is recorded in Appendix E.18 with its limits. The NAS's directory bind was found already on LDAPS with its own scoped account (TLS 1.3). 3.5.10 stays partial for the cleartext password path on port 5000 alone. System & Communications Protection is 13 of 16. Backup `.bak-20261024-cr49`. |
| **2.18 (amended 71)** | **10/24/2026** | **[SYSTEM-OWNER]** | **DEAD `monitor` VIRTUAL HOST REMOVED; NO COUNT CHANGE (94/110); SPRS UNCHANGED (`DIWAI-CR-2026-10-48`).** The `monitor.[DOMAIN.ORG]` virtual host proxied to a Grafana that was removed on 2026-08-04; nothing listens on its port. Removed, the web server reloaded, the other virtual hosts re-tested. Appendix E.15 no longer lists it. Backup `.bak-20261024-cr48`. |
| **2.18 (amended 70)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.13.3, 3.1.4, 3.1.6 RECOVERED; OBJECTIVE-LEVEL 91 → 94/110 (ASSESSMENT REVISION 1.30); SPRS UNCHANGED (`DIWAI-CR-2026-10-47`).** On the owner's decisions of 2026-10-24: Appendix E.15 records how user and management functions are separated (3.13.3); separation of duties is not applicable on the fact that one individual has any access, with compensating controls (E.16, 3.1.4, `DIWAI-APP-001` v1.3); the nonsecurity functions are defined and privileged work is by `sudo` elevation (E.17, 3.1.6). A stale member (`uid=drilldbg61ff`) was removed from `cn=cui-users`. Access Control is 20 of 22, System & Communications Protection 12 of 16. Backup `.bak-20261024-cr47`. |
| **2.18 (amended 69)** | **10/24/2026** | **[SYSTEM-OWNER]** | **VIRUSTOTAL LOOKUPS: CONTROLLED DOCUMENTS SKIPPED; NO COUNT CHANGE (91/110); SPRS UNCHANGED (`DIWAI-CR-2026-10-46`).** Bursts of file events from the hourly Mac scan exceeded the free API's 4 lookups a minute, so the integration failed on the later events (exit status 4). The wrapper now skips files under Nextcloud's group-folder data (the controlled documents, whose hash lookups were pointless and sent hashes to a third party); file-integrity alerts are unaffected. Backup `.bak-20261024-cr46`. |
| **2.18 (amended 68)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.13.13 RECOVERED; OBJECTIVE-LEVEL 90 → 91/110 (ASSESSMENT REVISION 1.29); SPRS UNCHANGED (`DIWAI-CR-2026-10-45`).** Mobile code the system serves is now monitored: the Mac Wazuh agent checks Nextcloud's `apps`, `core` and `themes` (about 35,000 files; its configuration and group-folder data were already covered), and the weekly review (`DIWAI-SCH-001` v1.2, W1) has a mobile-code step. A test file raised rule 554 at the next hourly scan. Browser-side script execution stays unmonitored (stated in `DIWAI-MCP-001`). System & Communications Protection is 11 of 16. **Found:** the VirusTotal integration logged errors on file events at 10:14 today (not changed). Backup `.bak-20261024-cr45`. |
| **2.18 (amended 67)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.13.13 [a] RECOVERED; NO COUNT CHANGE (90/110); SPRS UNCHANGED (ASSESSMENT REVISION 1.28).** The owner confirmed the three open entries of `DIWAI-MCP-001` (document macros disabled; no browser extensions for CUI work; no other browsing in the CUI profile). The requirement stays unmet at [b], monitoring: scripts in the browser and content-security-policy violations are not collected. Backup `.bak-20261024-mcp`. |
| **2.18 (amended 66)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.6.1 RECOVERED; OBJECTIVE-LEVEL 89 → 90/110 (ASSESSMENT REVISION 1.27); SPRS UNCHANGED (`DIWAI-CR-2026-10-44`).** The owner approved `DIWAI-DET-001` (detection coverage statement) and `DIWAI-MCP-001` (mobile-code policy). DET-001 states what is watched, how the owner finds out, where detection failed in INC-003 to INC-008 and the blind spots that remain. MCP-001 awaits the owner's confirmation of three entries (macros, extensions, browsing) before 3.13.13 is re-determined. Incident Response is 3 of 3. Backup `.bak-20261024-cr44`. |
| **2.18 (amended 65)** | **10/24/2026** | **[SYSTEM-OWNER]** | **APPENDIX E.5 CORRECTED; NO COUNT CHANGE (89/110); SPRS UNCHANGED.** The key-management table listed the directory superuser credential as "Overdue, POA&M-021"; that item was closed on 2026-08-02 when the credential was rotated, so the row now says so. The remaining open item under 3.13.10 is the VM's single LUKS keyslot with no off-rack escrow (POA&M-026, POA&M-049). The account table's Directory Manager row, which still said the NAS used it and that it was exposed, was corrected the same way. Backup `.bak-20261024-am65`. |
| **2.18 (amended 64)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.5.7 AND 3.5.9 RECOVERED; OBJECTIVE-LEVEL 87 → 89/110 (ASSESSMENT REVISION 1.25); SPRS UNCHANGED (`DIWAI-CR-2026-10-43`).** The rule for change of characters is stated in the IA policy and Appendix E.4 (a new password must differ from the previous six). The directory setting `passwordMustChange` is on, and a forced change was proven on a disposable account; service-account binds were re-checked afterwards (no failures). Identification & Authentication is 8 of 11. Backup `.bak-20261024-cr43`. |
| **2.18 (amended 63)** | **10/24/2026** | **[SYSTEM-OWNER]** | [PERSONNEL-SCREENING-NOTE-REDACTED] Policy backup-media wording corrected (no ReaR images; the Time Machine drive is FileVault-encrypted). Access Control is 18 of 22. Backup `.bak-20261024-am63`. |
| **2.18 (amended 62)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.10.2, 3.10.6, 3.13.1 RECOVERED; OBJECTIVE-LEVEL 83 → 86/110 (ASSESSMENT REVISION 1.23); SPRS UNCHANGED (`DIWAI-CR-2026-10-42`).** On the owner's decisions of 2026-10-24: (a) §2.5.3 added, defining five key internal boundaries and their controls (3.13.1); (b) support infrastructure (UPS, ventilation) is monitored by the monthly observation, automated monitoring being impractical (3.10.2); (c) CUI is not handled outside the rack site, so enforcement at alternate work sites is not applicable (3.10.6, Appendix E.7). [PERSONNEL-SCREENING-NOTE-REDACTED] Physical Protection is 4 of 6, System & Communications Protection 10 of 16. Backup `.bak-20261024-am62`. |
| **2.18 (amended 61)** | **10/24/2026** | **[SYSTEM-OWNER]** | **LIVE RE-WALK OF 3.10.2, 3.10.6, 3.13.1; NO COUNT CHANGE (83/110); SPRS UNCHANGED (ASSESSMENT REVISION 1.22).** 3.10.2 [a] (facility protection and monitoring) and 3.10.6 [a] (alternate-site safeguards defined, Appendix E.7) recovered; neither requirement is fully met. 3.13.1 [b] (key internal boundaries) needs an SSP statement; a draft was prepared from the live `pf` and `firewalld` rules and awaits the owner. Dashboard stale content corrected (`DIWAI-CR-2026-10-41`). Backup `.bak-20261024-am61`. |
| **2.18 (amended 60)** | **10/24/2026** | **[SYSTEM-OWNER]** | **AU AND IR POLICY WORDING CORRECTED; NO COUNT CHANGE (83/110); SPRS UNCHANGED (`DIWAI-CR-2026-10-40`).** The Wazuh index retention is stated as enforced (90 days, verified 2026-10-24); the NAS archive expiry remains outstanding (POA&M-059). Recovery wording in the IR policy now points to the backup procedures instead of a regime that does not exist here. Backup `.bak-20261024-cr40`. |
| **2.18 (amended 59)** | **10/24/2026** | **[SYSTEM-OWNER]** | **3.14.4, 3.1.20, 3.1.1 [c] RECOVERED; OBJECTIVE-LEVEL 81 → 83/110 (ASSESSMENT REVISION 1.21); SPRS UNCHANGED.** The 2026-10-24 03:15 scheduled rule update completed (Suricata 53,254 rules, YARA index 748 files), settling 3.14.4 (System & Information Integrity 7 of 7). The owner approved `DIWAI-EXT-001` v1.0 (external systems and authorised devices) and confirmed its three open entries, settling 3.1.20 and 3.1.1 [c]; 3.1.1 [f] stays partial until the Mac firewall allow-list (R4). Access Control is 17 of 22. Backup `.bak-20261024-am59`. |
| **2.18 (amended 58)** | **10/23/2026** | **[SYSTEM-OWNER]** | **ACCESS CONTROL RE-WALK: 3.1.5, 3.1.8, 3.1.10 RECOVERED; OBJECTIVE-LEVEL 78 → 81/110 (ASSESSMENT REVISION 1.20); SPRS UNCHANGED.** Three requirements whose August findings were closed earlier (lockout, the NAS bind as Directory Manager, the session-unlock rule) were re-determined on live checks (`DIWAI-EV-AC-2026-10-23`). [PERSONNEL-SCREENING-NOTE-REDACTED] Backup `.bak-20261023-am58`. |
| **2.18 (amended 18)** | **10/04/2026** | **[SYSTEM-OWNER]** | **DIAGNOSIS LOOP.** §3.2 Component 1 records `diwai-diagnose` (read-only diagnosis that names the approved repair, never runs one; `DIWAI-CR-2026-10-09`); Component 2 notes that the control-health monitor also writes a JSON report for it. **No control determination, no SPRS change.** |
| **2.18 (amended 17)** | **10/04/2026** | **[SYSTEM-OWNER]** | **MAGISTRAL BACK IN SERVICE.** §3.2 Component 1's model list adds Magistral Small 2509 through LM Studio for general questions (`DIWAI-CR-2026-10-08`). **No control determination, no SPRS change.** |
| **2.18 (amended 16)** | **10/04/2026** | **[SYSTEM-OWNER]** | **REPAIR LIBRARY; VM SUDO ASKS FOR THE PASSWORD.** §3.2 Component 1 records `diwai-repair` (YubiKey-approved repairs, `DIWAI-CR-2026-10-07`) and the VM sudo change (`DIWAI-CR-2026-10-06`: `/etc/sudoers.d/[USERNAME]` was `NOPASSWD: ALL` since 2026-04-08, never recorded; now password, remembered at most 2 minutes). **No SPRS change** (3.1.5/3.5.3 determinations unchanged pending reassessment). |
| **2.18 (amended 15)** | **10/03/2026** | **[SYSTEM-OWNER]** | **RETIRED OLLAMA MODELS REMOVED; SBOM CITED WITHOUT A VERSION.** §3.2 Component 1 notes that the retired Ollama models (90 GB) were deleted (`DIWAI-CR-2026-10-05`). Appendix C now cites the SBOM by its canonical file, not a version number, so routine SBOM revisions no longer require an SSP amendment. **No control determination, no SPRS change.** |
| **2.18 (amended 14)** | **10/03/2026** | **[SYSTEM-OWNER]** | **AIDER ON A LEASH.** §3.2 Component 1 now states Aider's role under owner decision 13 (option B): it drafts on the build side, never edits a live configuration file itself, and may run an ISSO-approved repair only after a typed yes; started through `aider-leashed` (`DIWAI-CR-2026-10-04`). This replaces amendment 12's "never in a repair path". Appendix C cites SBOM v3.8. **No control determination, no SPRS change.** |
| **2.18 (amended 13)** | **10/03/2026** | **[SYSTEM-OWNER]** | **OPEN WEBUI 0.9.5 → 0.11.4.** §3.2 Component 1 records the update (`DIWAI-CR-2026-10-03`, owner-approved manual update; security fixes included) and Appendix C now cites SBOM v3.7. The 05/15/2026 revision-history entry is left as written. **No control determination, no SPRS change.** |
| **2.18 (amended 12)** | **10/03/2026** | **[SYSTEM-OWNER]** | **AI STACK DESCRIPTION BROUGHT CURRENT.** §3.1, §3.2 Component 1 and Appendix C described the retired Magistral/MLX server (port 8081). They now record **LM Studio 0.4.25+1** as the single model runtime (`DIWAI-CR-2026-10-01`, complete; reboot test passed 2026-10-03) and the read-only **DIWAI document library** (`DIWAI-CR-2026-10-02`, approved 10-03-2026), all listeners loopback-only. Open Web UI's launcher corrected from LaunchDaemon to LaunchAgent. The 05/15/2026 revision-history entry is left as written (point-in-time). **No control determination, no SPRS change.** |
| **2.18 (amended 11)** | **10/03/2026** | **[SYSTEM-OWNER]** | **CUI MARKING APPLIED IN ADVANCE — STATED FOR ASSESSORS.** Owner determination 2026-10-03: documents marked CUI on this system are company-proprietary while held here and become CUI only when held by the U.S. Government; they are marked in advance because they may be shared with a Government or third-party assessor. **(a)** §4.8 now states this, so that `CUI_`-marked files in the local AI knowledge base are not read as a CUI-handling violation. **(b)** §3.2 Component 1 carries a one-line pointer to §4.8. **(c) No control determination, no SPRS change.** |
| **2.18 (amended 10)** | **09/15/2026** | **[SYSTEM-OWNER]** | **OBJECTIVE-LEVEL COMPLIANCE 35 → 42/110; THE ASSESSMENT IS NOW REVISED AS EVIDENCE CHANGES.** **(a)** `DIWAI-ASMT-2026-08` reissued as **revision 1.1** with a reassessment log (§0): determinations are re-walked in place, the superseded determination retained beside the new one, so the change history lives in the document and the figure the dashboard reads stays current. **(b) Seven requirements recovered** on evidence produced 08-03 → 09-15 but never re-assessed: **3.2.1/3.2.2/3.2.3** (IF141 certificate, policy acknowledgment, role assignment, dated role-based self-study, two peer-reviewed articles and a CPE-accredited session — POA&M-008 satisfied, AT now 3/3), **3.3.4** (alert proven end to end 09-13 and re-proven 09-15 after the macOS upgrade silently reverted `audit_warn`), **3.4.1** (baseline maintenance restored and evidenced; attached storage added to boundary and SBOM), **3.6.3** (tabletop conducted 08-03, signed, POA&M-006 closed), **3.10.3** (visitor log operating, nil attestations). **(c) Deliberately unchanged:** **3.10.4** — no interior camera will ever be permitted (owner privacy decision), so video cannot evidence rack access; **3.10.5** — device inventory still has blank fields; **3.1.8/3.5.7/3.5.8** — controls proven by refusal testing, but the IA policy, Appendix E.4 and the hosts state conflicting values, and that reconciliation is the next recovery. **(d)** Control Family Status table and objective tallies updated (**257 determinations: 123 satisfied**). **(e) The finding behind the finding:** the evidence had existed for up to six weeks while the published figure understated the system — an assessment not re-walked reports the past. **(f) No SPRS change** — SPRS measures proven control effectiveness (100/110) and is unaffected by documentation recovery. |
| **2.18 (amended 9)** | **09/15/2026** | **[SYSTEM-OWNER]** | **FLAW-REMEDIATION REVIEW CADENCE WEEKLY → MONTHLY (Appendix E.3), BY OWNER DECISION; 72-HOUR CRITICAL CLOCK GIVEN A DEFINED START.** **(a)** The weekly review cadence set in v2.15 **lapsed 2026-08-07 → 2026-09-15** while the owner worked on other systems; the gap was found by the automated control-health check, not the calendar. E.3 now requires review **monthly, and on return after any gap over 30 days**. The rationale is recorded in E.3: the system is worked in concentrated sessions and may sit unattended for weeks, but **exposure does not pause** — webmail, mail and OpenVPN are internet-published continuously — so detection stays daily and automated while the *human* review moves to a cadence that is actually met. 3.14.1 requires timeframes defined **and met**. **(b) F-2026-09-04:** `DIWAI-PR-001` §6 required PATCH-class CRITICAL within 72 hours but never defined what started the clock, while §3 measured 7 days from *review* — the same event was both compliant and a breach depending on which row was read. §6.1 now defines **detection** (the timestamp of the scan report first listing the finding) and gives §6 precedence; a lapsed review cadence does not pause it. Procedure reissued **v1.2**. **(c)** Six Mac packages upgraded the same session — 3 CRITICAL (`apr-util`, `curl`, `openssl@3`) and 3 lower — re-scan **`brew_actionable: 0`**, consumers relinked, Nextcloud verified (`CUI_Patch_Review_Log.md`). **(d) Outstanding:** no reminder yet exists for the review cadence, and the control-health check watches CVE age, not review age — until wired, the cadence depends on the owner's memory. **(e) No SPRS change.** |
| **2.18 (amended 8)** | **09/15/2026** | **[SYSTEM-OWNER]** | **ATTACHED STORAGE ENCRYPTED AND ADDED TO THE BOUNDARY; A CONTROL CLAIM RESTED ON A NON-EXISTENT POLICY SECTION.** Change record `DIWAI-CR-2026-09-09`. **(a) F-2026-09-02:** the USB-attached 250 GB APFS volume `CyberHygiene Project` — the register's designated historical reference copy, holding the [DOMAIN.ORG] TLS private key, a LUKS/GRUB credentials image, MFA scratch codes, 4 CUI-marked files and a 123-document compliance archive — was **not encrypted**, contrary to `DIWAI-AUP-001`. **Encrypted in place by the owner the same session** (C125); verified `FileVault: Yes (Unlocked)`, one cryptographic user, volume UUID unchanged so the USBGuard allowlist still matches. The Time Machine volume `SecureMac` was already FileVault-encrypted. **(b) F-2026-09-03:** the 3.1.21 row cited **`DIWAI-AUP-001` §4.2, which does not exist**; corrected to §5.1 and §2.6. **(c)** §2.5 now inventories attached storage and records the architecture: on Apple Silicon, capacity beyond the internal SSD is necessarily Thunderbolt- or USB-attached, so these are **rack-resident fixed volumes** (`Removable Media: Fixed`) protected by full-disk encryption, marking and the locked cabinet — **not portable media**, so 3.8.5/3.8.6 transport requirements do not apply. **(d)** SBOM records both SSDs and, for the first time, **Time Machine**, previously absent from the backup table. AUP §5.1 rewritten: platform-appropriate encryption, fixed storage distinguished from portable media, USBGuard recorded as enforced. **(e) No SPRS change.** |
| **2.18 (amended 7)** | **09/15/2026** | **[SYSTEM-OWNER]** | **PHYSICAL LAYER 5 CORRECTED; NO-INTERIOR-CAMERA CONSTRAINT RECORDED; TRAINING EVIDENCE RE-BASED.** **(a) F-2026-09-01 raised:** the layer table stated the Mac mini was "rack-mounted in a 2U tray, restricting access to ports and the power button". **The tray was repurposed**; the host sits on a shelf inside the same locked cabinet. No security effect — layer 4, the cabinet lock, was always the enforcing control — but a filed photograph (`CUI_PE_03`) depicts a dismantled configuration, and **nothing verifies physical configuration against this plan**. Same defect class as F-2026-08-06 and F-2026-08-33. **(b) Owner constraint, standing:** no video camera is permitted inside the residence, on privacy grounds. All nine cameras are exterior, so **video is permanently unavailable as a 3.10.4 mechanism**; 3.10.4 stays −1 as a recorded acceptance, with non-video options listed in `CUI_PE_Physical_Access_Log.md` §5.1. **(c)** Physical evidence artefacts were found to carry copy-in dates rather than capture dates; originals (2025-02-07 to 2026-08-02) are outside the store and one filed image no longer matches the room. **(d)** `DIWAI-TRR-001` §2.1 adds dated, sourced role-based self-study (T-003–T-010) under the first-in-role condition now recorded in `DIWAI-RAM-001` §2.1; `DIWAI-CRC-001` v1.3 records the **peer-reviewed** *Journal of Contract Management* article and corrects "no third-party validation". **(e) No score change.** |
| **2.18 (amended 6)** | **09/13/2026** | **[SYSTEM-OWNER]** | **3.14.2 YARA PATH NOW EVIDENCED; 3.5.6 DIRECTORY HALF ENFORCED.** **(a)** The 3.14.2 warning is replaced with the proof: YARA detection exercised end to end on both hosts with EICAR — the first alerts it had ever raised (`DIWAI-CR-2026-09-06` §3a; POA&M-075 closed). **(b)** Appendix E.4 and the §11 3.5.6 row now record 389-DS inactivity enforcement, proven by refusal (`DIWAI-CR-2026-09-08`). The point stays withheld pending the Mac and VM local accounts. No figure changed. |
| **2.18 (amended 5)** | **09/13/2026** | **[SYSTEM-OWNER]** | **3.5.6 WITHHELD — SPRS 101 → 100/110 UNDER THE EVIDENCE-STRICT BASIS.** Applied the same day it was adopted. Appendix E.4 stated "Accounts disabled after inactivity of 90 days"; testing found no enforcement on any host (389-DS Account Policy plugin off; VM local accounts and Mac unconfigured). E.4 corrected to *defined, not yet enforced*; 3.5.6 −1 added to the §11 deductions; **POA&M-076** opened. The `sysadmin` break-glass account is the design constraint for enforcement. |
| **2.18 (amended 4)** | **09/13/2026** | **[SYSTEM-OWNER]** | **SCORING BASIS DETERMINED: EVIDENCE-STRICT.** The owner recorded, for the first time, the basis on which SPRS is scored — a question put in `CUI_SPRS_Recomputation_and_Punchlist_2026-08` §1 and never answered on the record. A requirement earns its points only when implemented **and** proven working by evidence, including negative testing, per the `DIWAI-VS-001` standard. The strict 800-171A objective count (**35/110**) is reported alongside as the documentation gap (POA&M-027), not as the score. §11 statement added; no figure changed. |
| **2.18 (amended 3)** | **09/13/2026** | **[SYSTEM-OWNER]** | **SPRS 94 → 101/110 ON THREE TESTED RECOVERIES.** **(a)** 3.14.1 +5: Wazuh manager unpinned and upgraded to 4.14.7 after the SIGILL was traced to an SVE2 virtual-CPU quirk (`DIWAI-CR-2026-09-04`). **(b)** 3.3.4 +1: Mac audit-failure alert proven end to end to the owner's inbox (`DIWAI-CR-2026-09-07`). **(c)** 3.10.3 +1: visitor nil attestation; 3.10.4 withheld by owner decision (`DIWAI-PE-LOG-001`). **(d) Flagged, not resolved:** the 3.14.2 narrative describes YARA as operating, but its Wazuh rules had never loaded (`DIWAI-CR-2026-09-06`, **POA&M-075**). The Control Family Status table (35/110 fully met) remains unreconciled since early August (POA&M-027). Score updated in the five live locations, §10 and §11; prior reasoning retained. |
| **2.18 (amended 2)** | **09/13/2026** | **[SYSTEM-OWNER]** | **SPRS RE-DETERMINED 93 → 94/110 ON NEGATIVE-TEST EVIDENCE; DIRECTORY PASSWORD LENGTH ALIGNED TO 14.** **(a)** The earlier amendment's stated basis — credential policies "configured but not negatively tested" — was itself incomplete: negative tests on disposable accounts found the **Mac password-history rule malformed and skipped since 2026-08-07** and the **389-DS minimum length disabled** (`passwordCheckSyntax: off`). **(b)** Both repaired in session; 3.1.8, 3.5.7 and 3.5.8 then **proven by refusal on both hosts** (`DIWAI-CR-2026-09-03`). **(c)** 389-DS `passwordMinLength` 8 → **14** at the owner's direction, closing E.4's "to be aligned". **(d)** The owner re-determined the score at **94/110** in the five live locations and §10; the 93 reasoning is retained. POA&M reference unchanged (v1.32, amended). **(e) Not changed, flagged:** §3.1.8 describes VM faillock as 5 attempts / 30 min; `DIWAI-VS-002` recorded `deny = 3`. |
| **2.18 (amended)** | **09/13/2026** | **[SYSTEM-OWNER]** | **SPRS RECONCILED 87 → 93/110 ON OWNER DETERMINATION; THE v2.18 DISCREPANCY BLOCK IS CLOSED.** **(a)** The owner determined the `DIWAI-VS-001` §4 dispute (3.1.8 / 3.5.7 / 3.5.8 credential policy) on 2026-09-13, outstanding since 08-07, applying the standing rule that **a disputed figure is reported at the lower, more conservative value**. **(b)** This document stated **87/110** — the 08-03 recompute — in five live locations while the register had since recorded **3.7.5 +5** (`DIWAI-CR-2026-08-18`) and **3.5.3 +2**, reaching 94 by arithmetic. The determination withholds one further point, so the figure of record is **93/110**. **(c)** The v2.18 ⚠ block recording this as an unresolved discrepancy is replaced with the resolution — both blockers it named are removed. **(d)** POA&M cross-references repointed **v1.31 → v1.32**. **(e) No control narrative and no compliance determination is altered** — the withheld point reflects that `DIWAI-VS-002` found the Mac credential policies configured but **not negatively tested**. |
| **2.18**             | **08/12/2026** | **[SYSTEM-OWNER]** | **POA&M REFERENCE REPAIRED; EMBEDDED REGISTER COPY REMOVED; SPRS DISCREPANCY RECORDED.** **(a) The SSP named a superseded POA&M as the document of record in three places** — §1.2 header field, §10, and Appendix D — all citing `[DOMAIN.ORG]_Unified_POAM_v1.6.md` and describing it as "POA&M-001 through POA&M-030; 12 closed, 18 open". The register had advanced to **POA&M-073 / 63 tracked items / 39 closed / 24 open**, and the file had been superseded twice. The reference was never repointed when v1.7 was issued, so a reader following the SSP's own pointer would have landed on a two-generation-stale document and read materially wrong counts. All three now cite `CUI_[DOMAIN.ORG]_Unified_POAM_v1.30.md`. **(b) §10's embedded summary table is REMOVED, not refreshed.** It was labelled "kept in sync with the standalone document" while frozen at **2026-06-06** and listing only POA&M-001 through -010 — the document asserted its own currency and was wrong. Duplicating a register inside the document that cites it **is** the drift mechanism, so §10 now carries **counts only** plus a pointer, and the standalone POA&M is stated as the single source of truth. **(c) A SPRS discrepancy is RECORDED AND DELIBERATELY NOT CORRECTED.** This SSP states **87/110** (the 2026-08-03 recompute) in four places; the POA&M states **94/110 — DISPUTED, 93 recommended**, having since recorded 3.7.5 recovered (+5) and further movement on 08-07. The SSP is ~7 points stale. Correcting it is an **owner determination** and is additionally blocked on the open `DIWAI-VS-001` §4 dispute (3.1.8 / 3.5.7 / 3.5.8 credential policy); a warning block in §10 records this and directs readers to treat the POA&M as authoritative for score meanwhile. **(d) Scope discipline:** this revision repairs *references and duplication only*. No control narrative, no score, and no compliance determination was altered. **Memo for record:** `DIWAI-MFR-2026-08-12`**.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **2.17**             | **08/07/2026** | **[SYSTEM-OWNER]** | **CONTROL TABLE CORRECTED — FOUR ROWS DESCRIBED A DISABLED AUTOMATION** (change record `DIWAI-CR-2026-08-28`). **(a)** Rows for **3.7.1, 3.11.3, 3.14.1 and 3.14.3** stated that `dnf-automatic` "applies security patches" / "handles OS security advisories" on the VM. **It does not:** `apply_updates = no`**.** It downloads and applies nothing — the accepted deviation recorded in this plan's own Appendix E.3 since v2.15. **The plan contradicted itself for two versions**, describing the mechanism the deviation had deliberately disabled. All four rows now describe the real mechanism: staged downloads plus **operator-applied updates at the weekly review** (`DIWAI-PR-001`, log `DIWAI-PR-LOG`), with identification by `diwai-cve-scan`/`-mac`, Wazuh and the SCAP/mSCP baselines. **(b) 3.14.1 restated as PARTIALLY IMPLEMENTED** with its evidence spelled out — two reviews logged 08-02/-03, ~40 CVEs closed on the host, and the deferred VM kernel now **running 5.14.0-687.33.1** with no reboot pending — and its residual named: `wazuh-manager` **pinned at 4.14.6 receives no security updates (POA&M-051)**, which is an uncorrected flaw in a security control and the reason the requirement is not scored as met. **(c) Deduction attribution corrected.** The `3.14.1 −5` row cited POA&M-025 ("adherence not yet evidenced"). Adherence **is** now evidenced and **025 is closed**; the deduction is reattributed to **POA&M-051**. **This matters for planning: the remaining −5 is an engineering task (a tested Wazuh upgrade path), not a documentation task.** **(d) No SPRS change. 94/110.** This corrects the plan's accuracy — which the DoD methodology makes a **scoring prerequisite** — without altering any determination in a favourable direction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **2.16**             | **08/03/2026** | **[SYSTEM-OWNER]** | **LEAST-FUNCTIONALITY RECONCILIATION — GRAFANA REMOVED, CLAMAV PACKAGES REMOVED.** Change record `DIWAI-CR-2026-08-09`. **(a) Grafana 13.1.1 decommissioned 08/02/2026** (`DIWAI-CR-2026-08-04`): not patchable — `rpm.grafana.com` failed GPG verification on `repomd.xml`, leaving an unpatchable internet-sourced component that additionally broke `dnf check-update` system-wide — weighed against limited operational use. §3.1 system functions, §3.2 component inventory (version also corrected 13.0.1→13.1.1, which had drifted from installed state before removal), and the §3.4 retired-components table updated. **(b) Two control narratives struck:** **AU-6 / 3.3.3** no longer credits Grafana with metrics dashboards, and **3.14.7** no longer cites "Grafana dashboards visualize anomalies." **Neither control status changes and there is no SPRS impact** — Grafana visualized data but detected nothing; audit review rests on the Wazuh Dashboard and identification of unauthorized use on Wazuh correlation + Suricata + auditd, all unchanged. **Prometheus + node-exporter retained and verified running 08/03/2026**, so metrics collection and retention are unaffected; only the visualization layer was retired. **(c) ClamAV packages removed from the VM 08/01/2026** (`DIWAI-CR-2026-08-01` C14, 5 packages / 138 MB), stated explicitly as **FIPS 140 incompatibility**. This closes **F-2026-08-06**, the inventory-vs-reality gap in which the software remained installed and auto-upgrading from the 06/12/2026 decommissioning until August — a configuration-management defect, never a protection gap, as the substituted FIPS-native SI-3 stack carried the control throughout. §3.14.2 and POA&M-002 unchanged and still correct. Companion SBOM reissued as **v3.3**. **Document-control note:** this revision was drafted against a **stale local working copy** of v2.15 (an 08-02 09:45 snapshot missing the wireless-boundary and OpenSCAP 101/101 content added later that day). The edits were re-applied to the canonical Nextcloud copy before issue; see `DIWAI-CR-2026-08-09` §5.5. **(d) Companion POA&M reissued v1.3→v1.4** the same day, adding **POA&M-048** (that document-control defect, F-2026-08-32, scored against 3.4.1/3.4.3/3.12.4 with no SPRS change). All POA&M references in this plan updated to v1.4; one such reference also carried the wrong date (2026-06-12, which is v1.2's) and is corrected. **Open-item count corrected 18 → 21** — the figure carried in v2.15 was already understated against the POA&M table, independently of this revision. |
| **2.16 (amended)**   | **08/04/2026** | **[SYSTEM-OWNER]** | **§3.2.1 added — role concentration and the daily-driver question.** Records that the Mac mini currently carries the perimeter firewall, hypervisor, plaintext CUI store, AI stack **and** the operator's daily working environment, and that the system owner's own guidance for adopters — place a separate workstation on the network as the daily driver — **is not followed by this deployment**. Technical basis stated: Nextcloud holds CUI as plaintext files, so any process running as the operator's account reads the store outside Nextcloud's authentication, 2FA, ACLs and audit log; daily-driver use widens that process population. **Planned remediation recorded:** introduce the existing SCAP-hardened laptop to the LAN as the model daily driver — not yet scheduled. Framed for the reference-model audience (single-operator system, or domain controller for a VSB of ≤15). No control status or SPRS change.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **2.16 (amended)**   | **08/03/2026** | **[SYSTEM-OWNER]** | **SPRS RECOMPUTED 56 → 87/110.** Thirty points recovered across eight requirements on evidence produced or verified 2026-08-03: 3.2.1/3.2.2/3.2.3 **+11** (POA&M-008 closed — DoD IF141.16 certificate, and `DIWAI-PAF-001`, `DIWAI-TRR-001`, `DIWAI-RAM-001`, `DIWAI-CRC-001` all signed); 3.11.1 **+3** (POA&M-005 closed — `DIWAI-RAR-001` v1.1 accepted and signed); 3.6.3 **+1** (POA&M-006 closed — tabletop conducted and signed, 10 gaps recorded); 3.1.16 **+5** (wireless powered off, pf-enforced, verified live); 3.11.2 **+5** (CVE scanning operational, last run 08-03 07:47); 3.5.10 **+5** (`nsslapd-require-secure-binds: on`, `DIWAI-CR-2026-08-10`). **Seven of the eight were already earned before this date** — the register had not caught up; only 3.5.10 required new engineering. Open deductions **−54 → −24**. CMMC L2 conditional-eligibility text updated: the score ≥ 80 condition is now met. Companion POA&M reissued **v1.6** (21 open, 26 closed) following a full scrub of the register against live state and the historical volume.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **2.15 (corrected)** | **08/02/2026** | **[SYSTEM-OWNER]** | **SPRS WEIGHTS VERIFIED — SCORE FINALISED AT 56/110.** All point values confirmed against the *NIST SP 800-171 DoD Assessment Methodology, Version 1.2.1 (24 June 2020)*, Annex A and §(d), replacing the provisional ~61 in the 08/01 entry. **POA&M-008 resolved from "TBD" to −11** after being outstanding since 06/11/2026 (3.2.1 −5, 3.2.2 −5, 3.2.3 −1). **Two errors of long standing corrected:** (a) **3.7.5 has been weighted −3 in this plan since v2.11; the methodology assigns it −5**; (b) the 11 points for POA&M-008 were acknowledged as pending but **never subtracted**. **The June 2026 baseline was therefore 85/110, not the 98/110 published in v2.11–v2.14.** Three provisional weights from the 08/01 assessment are also corrected: 3.5.10 −1→−5, 3.12.3 −1→−5, 3.3.4 −3→−1. Partial-credit rules recorded: 3.5.3 is −5 (MFA implemented for no users; −3 would apply if it covered remote and privileged users only), and **3.13.11 scores 0** because FIPS-validated encryption is in use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **2.15**             | **08/01/2026** | **[SYSTEM-OWNER]** | **POST-DEMO REBASELINE — FULL SP 800-171A OBJECTIVE-LEVEL SELF-ASSESSMENT** (`Compliance/Assessment/CUI_800-171A_Self_Assessment_2026-08.md`; change record `DIWAI-CR-2026-08-01`). First assessment of **all 110 requirements at assessment-objective level** (249 determinations). **(a) Metrics corrected against measurement rather than assumption:** Mac mSCP **130/135 (96.30%)**, superseding the 126/134 figure which had been unverifiable since April because the weekly scan was executing a **zero-byte script**; VM OpenSCAP CUI profile **101/102**, down from 102/102 — the single failure (`dnf-automatic_apply_updates`) is a **documented, accepted deviation**, see §11. **(b) Control Family Status table replaced** — the prior table asserted whole families fully implemented (AU 9/9, CM 9/9, SC 16/16, SI 7/7); objective-level assessment gives **35 of 110 requirements with every objective satisfied**. The difference is largely undocumented-but-working controls, tracked as POA&M-027. **(c) Nineteen remediation changes applied and verified** — account lockout and password history enabled, audit retention raised from ~1 hour to ~6.4 GB, cleartext SMTP authentication closed on the internet-published mail service, zone-wide LDAP exposure removed, policy identifiers reconciled, mSCP scanning restored, and a **control-health check deployed** after four controls were found believed-running but inert. **(d) New documentation added** per POA&M-027: internet-published service inventory (§2.5), wireless path, account inventory, separation-of-duties limitation, flaw-remediation timeframes, external system dependencies (Appendix E). **(e) Corrections:** `[DOMAIN.ORG]` artifact in the 2.14 entry; DIWAI-IAP-001 effective date 06/11/2026 → **06/06/2026**. **(f) SPRS:** the 98/110 figure is **withdrawn as unverified**; provisional recomputation ~61/110 with **unverified weights** — see §11. POA&M reissued as **v1.3** (30 items: 12 closed, 18 open).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2.14             | 06/29/2026 | **[SYSTEM-OWNER]** | **NEXTCLOUD CUI REPOSITORY DOCUMENTED — APPLICATION-LAYER MFA.** The Nextcloud private-cloud document repository (32.0.11.1), in production on the Mac host since 06/11/2026 as the canonical store for CUI/FCI documents (SSP, POA&M, SBOM, evidence), is now documented as an in-boundary system component. **(a)** §3.2 adds Nextcloud + its supporting services (Homebrew PHP-FPM 8.3, Redis, Collabora Online/`richdocuments` 9.1.0 loopback-bound) to the Mac host component; §3.3 adds the `cloud.[DOMAIN.ORG]` LAN-only endpoint to the topology. **(b)** §4.5 (3.5.3) records that **Nextcloud enforces TOTP 2FA (**`twofactor_totp`**) instance-wide** (enrolled for the system operator with backup codes, confirmed 06/11/2026) — an implemented application-layer MFA control over the CUI repository, added to §1.4 Strengths. **This does not change the 3.5.3 SPRS scoring:** host-OS login and VM SSH remain single-factor (POA&M-004/007), so 3.5.3 stays **NOT MET** and the SPRS figure is unchanged at 98/110. **(c)** §4.1 (3.1.1/3.1.2) and §4.8/§4.13 (SC-28) updated for Nextcloud LDAPS group-based access control (`cn=cui-users`) and FileVault at-rest encryption of the Nextcloud data directory; §4.3 (AU) notes Nextcloud `admin_audit` is enabled (Wazuh log-forwarding for `nextcloud.log` pending — tracked as a deployment task, not a control gap). No control status other than the additions above changed; SBOM (v3.0) and POA&M (v1.2) already reflect Nextcloud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **2.13**             | **06/12/2026** | **[SYSTEM-OWNER]** | **INDEPENDENT GAP ASSESSMENT — SI-3 SUBSTITUTION & ARCHITECTURE DIAGRAMS** (assessment: `Compliance/Assessment/RS2_Gap_Assessment_2026-06-12.md`). **(a) §3.14.2 (SI-3) rewritten:** ClamAV was found **non-functional under FIPS** (cannot download/load/verify any signature database) and has been **decommissioned**. Malicious-code protection is now provided by an already-operational, FIPS-native stack — **YARA 4.5.2 (5,972 rules, Wazuh-integrated on FIM 550/554) + a new weekly full-system YARA scan + VirusTotal + fapolicyd + SELinux + Suricata** (evidence **DIWAI-EV-SI3-002**, superseding RISK-2026-004). 3.14.2 raised **PARTIAL → IMPLEMENTED**; **POA&M-002 CLOSED**. *Correction: YARA was in fact already deployed on this VM — prior text stating otherwise was inaccurate.* **(b)** Two newly-found, now-closed items recorded: **POA&M-009** (Mac host Wazuh agent restored after ~12 days offline — config XML + ownership repair) and **POA&M-010** (VM time-sync drift, AU-8, corrected + made durable). **(c)** Architecture diagrams added as referenced figures (§3.3, §3.4, Appendix C): `RS2_Network_Schematic` and `RS2_CUI_DataFlow` in `Compliance/Architecture/`. POA&M companion updated to **v1.2**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

---

## EXECUTIVE SUMMARY

### 1.1 Purpose

This System Security Plan documents the security controls implemented for the **[DOMAIN.ORG] SecureMac Reference System**, which processes, stores, and transmits Controlled Unclassified Information (CUI) and Federal Contract Information (FCI) on behalf of [SYSTEM-OWNER] LLC dba [ORGANIZATION]. This SSP demonstrates compliance with NIST SP 800-171 Rev 2 and supports CMMC Level 2 certification readiness.

### 1.2 System Overview

The [DOMAIN.ORG] SecureMac Reference System is an Apple Silicon-based security reference implementation demonstrating that NIST 800-171 / CMMC Level 2 compliance is achievable using macOS and ARM64 Linux virtualization on a single-appliance platform. The system is architecturally distinct from the X86 Linux-based CyberInABox approach and serves as **CyberInABox Reference System #2**.

**Architecture:** Apple Silicon (ARM64) Mac Mini M4 Pro running macOS 26.5 (Tahoe) as the host OS, with a UTM-hosted Rocky Linux 9.7 aarch64 FIPS VM (services.[DOMAIN.ORG]) providing server services — all on a single physical device.

**SPRS Score:** **101/110** (evidence-strict; 3.5.6 withheld 2026-09-13 as defined but not enforced, awarded 2026-10-22 once enforced on all three account stores and proven, POA&M-076; recomputed on tested recoveries of 3.14.1, 3.3.4 and 3.10.3; `DIWAI-CR-2026-09-04`, `-07`, `DIWAI-PE-LOG-001` §6) — weights **verified** 2026-08-02 against the DoD Assessment Methodology v1.2.1. The 98/110 published in v2.11–v2.14 was never correct; the corrected June baseline was **85/110** (see §11).\
**Objective-level compliance:** **65 of 110** requirements have every SP 800-171A assessment objective satisfied or not applicable (`CUI_800-171A_Self_Assessment_2026-08.md` **revision 1.8, 2026-10-23**; was 64/110 at revision 1.7, 55/110 at revision 1.6, 52/110 at 1.5, 48/110 at 1.4, 47/110 at 1.3, 45/110 at 1.2, 42/110 at 1.1 and 35/110 at 1.0). Applicability is written down in `DIWAI-APP-001` (new §2.7). **This is not the security score** — it counts requirements whose *documentation and definition* objectives are also complete. The measure of control effectiveness is the SPRS score above\
**VM OpenSCAP CUI Compliance:** **101/101** — scanned against a tailored profile carrying one documented deviation (`dnf-automatic_apply_updates`, tailored out with justification; see Appendix E.3 and `/etc/diwai/scap/diwai-cui-tailoring.xml`)\
**Mac mSCP Compliance:** **130/135 (96.30%)** — measured 2026-08-01, superseding 126/134 which had been unverifiable since April (POA&M-015); 5 rules pending remediation (POA&M-003)\
**POA&M Reference:** `CUI_[DOMAIN.ORG]_Unified_POAM_v1.32.md` (companion document, `Compliance/POAM/`; see Appendix D). **64 tracked items, POA&M-001 through POA&M-074 — 39 closed, 25 open** as of 2026-09-13

### 1.3 Compliance Requirements

**Primary Requirements:**

- NIST SP 800-171 Rev 2 — Protecting CUI in Nonfederal Systems and Organizations
- FIPS 140-2 — Cryptographic Module Validation (VM: FIPS mode enabled; Mac: Apple Secure Enclave)
- FAR 52.204-21 — Basic Safeguarding of Covered Contractor Information Systems
- DFARS 252.204-7012 — Safeguarding Covered Defense Information and Cyber Incident Reporting
- CMMC Level 2 — Advanced cybersecurity practices (110 practices)

**Supporting Standards:**

- NIST SP 800-53 Rev 5, NIST SP 800-171A, CIS Controls, mSCP (macOS Security Compliance Project)

### 1.4 Key Findings

**Strengths:**

- Apple M4 Pro Secure Enclave provides hardware-rooted encryption and key management
- FileVault full-disk encryption on Mac host; FIPS 140-2 LUKS on VM
- Rocky Linux 9.8 aarch64 VM runs in FIPS mode — **101/101** OpenSCAP CUI compliance against a tailored profile; the single deviation is documented and tailored out with justification (Appendix E.3)
- Mac host at **96.30% mSCP compliance (130/135)** — measured 2026-08-01; 5 rules pending remediation (POA&M-003)
- Full Wazuh SIEM stack (Manager + Dashboard + Indexer) operational on VM
- Suricata 7.0.13 IDS operational on VM
- nginx reverse proxy restricts AI interface (ai.[DOMAIN.ORG]) to LAN only — WAN excluded
- USB Guard operational on both host (custom implementation) and VM (USBGuard)
- OpenVPN server installed on the VM, switched off since 2026-10-25 (`DIWAI-CR-2026-10-51`)
- 389-DS LDAP directory operational; Apache dashboard with LDAP auth (securemac.[DOMAIN.ORG])
- Login banner confirmed on VM; pf firewall on Mac host (WAN/LAN/MGMT segregation)
- Time Machine backup auto-mount resolved — 17-day gap root cause corrected (05/15/2026)
- **MFA strategy unified (06/06/2026):** A single remediation path (TOTP via Authenticator app, RFC 6238) now covers both the Mac host and the VM, replacing the more fragile dual-track plan (YubiKey PIV + separate VM TOTP). See POA&M-004 and POA&M-007.
- **CUI repository enforces MFA (06/11/2026):** The Nextcloud private-cloud document repository — the canonical store for all CUI/FCI documents — enforces TOTP two-factor authentication (`twofactor_totp`) instance-wide on every login, layered on LDAPS-backed identity. Application-layer MFA over the CUI store is therefore already in production, even though host-OS and VM-SSH MFA remain pending (POA&M-004/007). See §3.2 and §4.5.

**Outstanding Deficits (see [DOMAIN.ORG] POA&M v1.32 — 25 open items):**

- 3.7.5 — **RECOVERED** (+5, `DIWAI-CR-2026-08-18`). 3.5.3 — **−3 stands** (partial credit: MFA covers remote and privileged access, not every user); see the 3.5.3 row and the Partial-credit requirements.
- 3.11.1 — **RESOLVED 2026-08-03:** risk assessment accepted and signed (`DIWAI-RAR-001` v1.1); POA&M-005 closed.
- 3.6.3 — **RESOLVED 2026-08-03:** the IR tabletop exercise was conducted and signed (`DIWAI-IR-TTX-001`, 10 gaps identified; POA&M-006 closed; follow-on items POA&M-056 and -057)
- 3.11.2 — **RESOLVED 2026-08-03:** CVE scanning operational (`diwai-cve-scan`); POA&M-022.
- 3.13.5 — **Internet-published services share a host with the CUI data tier**; no DMZ separation — POA&M-023
- 3.10.4 — **−1 stands:** rack openings are not logged during development, by owner decision 2026-09-13; POA&M-027.
- 3.5.6 — **AWARDED 2026-10-22 (+1, owner decision; was withheld 2026-09-13):** the 90-day inactivity disable (Appendix E.4) is enforced on the directory (`DIWAI-CR-2026-09-08`) and, by daily jobs, on the Mac and on the VM's local accounts (`diwai-inactivity-enforce`, `DIWAI-CR-2026-10-17`; `diwai-inactivity-enforce-vm`, `DIWAI-CR-2026-10-18`), each proven by refusal on a disposable account on 2026-10-19; the first scheduled runs were observed on 2026-10-20, -21 and -22. Limits: no real account has yet aged out, and never-logged-in directory entries are not yet covered; POA&M-076 stays open for them. Rev 2 requirement; Revision 3 withdrew it (03.01.01 f.02).
- 3.5.10 — **RESOLVED 2026-08-03:** `nsslapd-require-secure-binds: on` (`DIWAI-CR-2026-08-10`); POA&M-020/021.
- 3.1.16 — **RESOLVED 2026-08-03:** wireless powered off and pf-enforced, verified live; POA&M-024.
- 3.3.7 — **RESOLVED 2026-08-08:** POA&M-010 closed on an observed episode (POA&M v1.30).
- 3.12.4 + others — Definition and documentation gaps consolidated as POA&M-027
- 3.14.2 — **RESOLVED 06/12/2026:** malicious-code protection met by the YARA stack (YARA + VirusTotal + fapolicyd + SELinux + Suricata); ClamAV decommissioned (non-functional under FIPS). POA&M-002 closed — DIWAI-EV-SI3-002.

### 1.5 Authorization

**Full Authorization Granted:** June 5, 2026\
**Authorization Period:** 3 years (through June 4, 2029)\
**Current SPRS:** **101/110** (evidence-strict, 2026-10-22; 3.5.6 awarded, POA&M-076; recomputed 2026-08-03; weights verified 2026-08-02) — see §11\
**CMMC Level 2 Conditional Eligibility:** **NOT CURRENTLY ELIGIBLE.** The prior eligibility claim rested on the withdrawn 98/110. At **101/110** the score ≥ 80 condition **is now met**; conditional eligibility rests additionally on a POA&M closure plan for the remaining items. Eligibility can be restored by working POA&M v1.32 — the four largest single recoveries available are 3.5.3/3.7.5 (MFA, +10 combined), 3.2.1/3.2.2/3.2.3 (training records, +11), 3.11.2 (vulnerability scanning, +5) and 3.13.5 (tier separation, +5).

---

## 2. SYSTEM IDENTIFICATION

### 2.1 System Information

**System Name:** [DOMAIN.ORG] SecureMac Reference System\
**System Acronym:** SecureMac\
**System Owner:** [SYSTEM-OWNER] LLC dba [ORGANIZATION]\
**System Type:** General Support System (GSS)\
**Operational Status:** Operational (Full Authorization)\
**Research Context:** CyberInABox Reference System #2 — Apple Silicon / macOS architecture

### 2.2 Organization Information

**Legal Entity:** [SYSTEM-OWNER] LLC\
**Doing Business As:** [ORGANIZATION]\
**CAGE Code:** [GOVT-ID-REDACTED]\
**DUNS Number:** [GOVT-ID-REDACTED]\
**NAICS Codes:** 541611, 541613, 541690\
**Business Location:** [LOCATION-REDACTED]

### 2.3 Contact Information

**System Owner / ISSO:**\
Name: [SYSTEM-OWNER]\
Title: Owner/Principal\
Email: [EMAIL-REDACTED]\
Phone: [PHONE-REDACTED]

### 2.4 System Categorization

**Information Type:** Federal Contract Information (FCI) / Controlled Unclassified Information (CUI)\
**Confidentiality:** MODERATE\
**Integrity:** MODERATE\
**Availability:** LOW\
**Overall System Categorization:** MODERATE

### 2.5 System Boundary

The [DOMAIN.ORG] SecureMac Reference System boundary encompasses:

1. **Mac Mini M4 Pro** (securemac.[DOMAIN.ORG] / ai.[DOMAIN.ORG]) — physical host
2. **services.[DOMAIN.ORG]** — Rocky Linux 9.7 aarch64 UTM VM running on the Mac Mini ([LAN-IP-REDACTED])
3. **nas.[DOMAIN.ORG]** — Synology 8-bay NAS ([LAN-IP-REDACTED]) — supporting infrastructure
4. **Attached fixed storage** — two USB-attached SSDs, below

#### 2.5.0 Attached storage (added 2026-09-15, `DIWAI-CR-2026-09-09`)

**Why this section exists.** Until this revision the boundary listed three assets
and **no storage**, although two attached SSDs hold CUI — one of them the Time
Machine destination for the whole host. An asset absent from the boundary is an
asset no assessment examines, and F-2026-09-02 was found only by inspection.

**Architecture, stated so it is not re-litigated.** On Apple Silicon the internal
SSD is not expandable, so **any capacity beyond it is necessarily Thunderbolt- or
USB-attached**. That is a property of the platform, not a storage choice. Both
volumes report **`Removable Media: Fixed`**, remain inside the locked rack cabinet
(PE layer 4), and carry drive marking.

**They are therefore fixed storage, not portable media.** The safeguards are the
same ones protecting the internal SSD: full-disk encryption, physical security in
the rack, and marking. The transport and custody requirements of **3.8.5 and
3.8.6 do not apply**, and no media custody record is required for them.

| Volume | Device | Capacity / used | Encryption | Role |
|:---|:---|:---|:---|:---|
| `SecureMac` | USB SSD, case-sensitive APFS — **replacement drive, 2026-10-18** (`DIWAI-CR-2026-10-14`) | 499.9 GB / 247.4 GB | **FileVault** (read back: Yes, Unlocked) | **Time Machine destination** — full host backup, therefore CUI-bearing; latest backup 2026-10-18 10:47; allowlist partition UUID `[HW-UUID-REDACTED]` |
| `CyberHygiene Project` | USB SATA SSD, APFS | 249.8 GB / 2.3 GB | **FileVault — encrypted 2026-09-15** (C125) | Historical reference copy (the register's designated search target) and publish/transfer volume; USBGuard allowlist UUID `[HW-UUID-REDACTED]` |

Both are recorded in `CUI_Software_Bill_of_Materials.md`. Encryption also provides
the sanitisation path for **3.8.3**: on disposal the key is destroyed, which is the
only reliable erasure for wear-levelled SSDs.

#### 2.5.1 Internet-Published Services (added v2.15)

The ISP allocates a /29 (`[WAN-IP-REDACTED]/29`, gateway `.150`). The Mac host
performs NAT and inbound redirection via pf; **the VM holds no public address**.
Verified from `pfctl -s nat`, 2026-08-01:

| Public address | Ports                        | Redirected to | Service                          |
|:---------------|:-----------------------------|:--------------|:---------------------------------|
| [WAN-IP-REDACTED]  | 80, 443                      | [LAN-IP-REDACTED]    | Web address; webmail (`webmail.[DOMAIN.ORG]`) answers the CUI network only (403 from elsewhere) |
| [WAN-IP-REDACTED]  | 25                           | [LAN-IP-REDACTED]    | Mail from other mail servers (`mail.[DOMAIN.ORG]`, MX target); 465, 587, 993, 995 not forwarded |
| [WAN-IP-REDACTED]  | none                         | —             | OpenVPN (`vpn.[DOMAIN.ORG]`) switched off, not published |

**Changed 2026-10-25 (`DIWAI-CR-2026-10-51`, owner decision 2026-10-24):** webmail, mail clients and the VPN are no longer reachable from the internet; they stay installed as future enhancements. Re-enabling is a recorded reversal of that change. Internet mail (port 25) is still published, so 3.13.5 is unchanged.
| [WAN-IP-REDACTED]  | —                            | —             | NAT egress for [LAN-IP-REDACTED]/24      |

`.148` is unassigned. The apex `[DOMAIN.ORG]` and `www` resolve to Cloudflare, not
to this block. **Assessment note (3.13.5):** these published services terminate
on the same VM that hosts 389-DS, the Nextcloud database and the Wazuh manager —
there is no DMZ separation. Tracked as **POA&M-023**.

#### 2.5.1.1 Carrier separation (added v2.15, evidenced 2026-08-02)

The premises are served by **three independent internet circuits**, one per
system. This is a deliberate design property, not an accident of provisioning:

| Circuit               | Serves                                       | Network                |
|:----------------------|:---------------------------------------------|:-----------------------|
| **[ISP-REDACTED]**           | **[DOMAIN.ORG] — this system**                      | [WAN-IP-REDACTED]/29 → `en0` |
| **[ISP-REDACTED]**      | CyberInABox (Reference System #1)            | separate               |
| **[ISP-REDACTED] (residential)** | Household / personal use, incl. a Mac Studio | [HOME-LAN-REDACTED]            |

**Assessment significance.** Separate carriers and separate demarcation points
are the strongest available evidence for the independence asserted in §2.6.
[DOMAIN.ORG] and CyberInABox do not merely occupy different subnets — they do not
share a WAN path, a router, or an ISP account. The only shared elements are
physical: the rack, the UPS, and the NAS (POA&M-032).

**The [ISP-REDACTED] residential network is out of boundary** and carries no CUI. Its
relevance here is that the Mac host currently holds an interface on it — see
§2.5.2.

#### 2.5.2 Wireless (added v2.15)

The Mac host has an **active Wi-Fi interface (**`en1`**)** holding a DHCP address on
an external network (observed [HOME-LAN-REDACTED]), 802.11ax/5 GHz, link security
**WPA2/WPA3 Personal**. Link protection satisfies 3.1.17. Wireless use is
**not yet authorised in this plan** (3.1.16) — tracked as **POA&M-024**.

**Restated 2026-08-02 on evidence.** The [HOME-LAN-REDACTED] network is the **household
[ISP-REDACTED] residential network** (§2.5.1.1), not an unidentified external network.
The host is therefore **triple-homed**:

| Interface | Network                      | Role                                         |
|:----------|:-----------------------------|:---------------------------------------------|
| `en0`       | [WAN-IP-REDACTED]/.146/.147/.149 | [ISP-REDACTED] — public, in boundary            |
| `en6`       | [LAN-IP-REDACTED]                    | **CUI network** — VM, NAS                        |
| `en1`       | [HOME-LAN-REDACTED] (Wi-Fi)           | **Household personal network — out of boundary** |

`net.inet.ip.forwarding = 1` (required for the `rdr` rules in §2.5.1). With
forwarding enabled across three interfaces, **the pf rule set is the only control
separating the household network from the CUI network.** That separation has not
yet been verified rule-by-rule.

**Resolution decided 2026-08-02:** disable the interface, with a documented
re-enable procedure for demo and off-site use. Disabling removes the host's only
attachment to a personal-use network and costs nothing in the CUI boundary —
camera recording is performed by a standalone NVR on the household network and is
unaffected.

**Out of scope / separate systems:**

- CyberInABox ([DOMAIN.ORG]) — architecturally distinct X86 Linux system (dc1.[DOMAIN.ORG] domain controller + LabRat/Engineering/Accounting workstations) occupying the same physical rack. Documented under its own SSP (System_Security_Plan — CyberHygiene Production Network). No shared WAN, no shared domain, no shared services with [DOMAIN.ORG]. Physical co-location only.

#### 2.5.3 Key internal boundaries (added 2026-10-24)

The key internal boundaries are the points where traffic passes between parts of the system that are trusted differently. Each is enforced by a named control.

| # | Boundary | Between | Enforced by |
|---|---|---|---|
| 1 | Internet edge | The internet (`en0`) and everything inside | Mac `pf`: default `block drop all`; private and special address ranges dropped both ways on `en0`; only the published services of §2.5.1 are passed in |
| 2 | Household network | The Mac's Wi-Fi (`en1`, the household network) and the CUI network ([LAN-IP-REDACTED]/24) | Mac `pf`: traffic from `en1` to the CUI network is dropped, and traffic from the CUI network out of `en1` is dropped. `en1` is currently inactive; it is a break-glass uplink only (§2.5.2) |
| 3 | CUI network | The Mac (`en6`, `bridge100`), the services VM and the NAS | Mac `pf` passes the CUI network; the VM adds `firewalld` (default zone `public`, only the listed services and ports). **Until the port baseline R4 is loaded, the Mac passes all traffic arriving from the CUI network** (`DIWAI-PORTS-001`) |
| 4 | Host to VM | The Mac host and the services VM (`bridge100`) | The VM `firewalld` zone; forwarded VM traffic passes through the Mac and is subject to its `pf` rules |
| 5 | Shared storage | The NAS and the second system it also serves | The NAS is dual-homed (POA&M-032); IP forwarding between the two networks is off (verified); the NAS is treated as outside this system's trust and holds encrypted data only |

Monitoring at these boundaries: `pf` logs blocked and CUI-network traffic; Suricata watches network traffic on the VM; Wazuh collects from both hosts; the 33 control-health checks run every 15 minutes (§ monitoring).

Known gaps: boundary 3 is open inside until the port baseline R4 is loaded; boundary 5 depends on POA&M-032 (documentation of the shared NAS). **Added 2026-10-24, corrected the same day:** the CUI network's switch is a Netgear switch (owner traced the cables); an HP switch on the owner's other, separate network is not part of this system. The NAS also answers on a second address of that other network on this wire (POA&M-032); the R4 allow-list limits what passes through the Mac to the VM and the NAS, and the NAS's second address is not passed. Approved by the owner 2026-10-24.

### 2.6 Relationship to CyberInABox

The [DOMAIN.ORG] SecureMac Reference System and the CyberInABox system are two independent reference implementations exploring alternative approaches to NIST 800-171 / CMMC Level 2 compliance for very small businesses:

| Attribute      | [DOMAIN.ORG] (This SSP)                                                       | CyberInABox (Separate SSP)       |
|:---------------|:---------------------------------------------------------------------------|:---------------------------------|
| Hardware       | Apple Mac Mini M4 Pro                                                      | X86 HP servers and mini PCs      |
| Architecture   | ARM64 (Apple Silicon)                                                      | x86_64                           |
| Host OS        | macOS 26.5 (Tahoe)                                                         | Rocky Linux 9.7                  |
| Virtualization | UTM (ARM64 VM on Mac)                                                      | Bare metal Linux                 |
| Identity       | 389-DS LDAP (dc=diwai,dc=org)                                              | FreeIPA/Kerberos                 |
| Firewall       | macOS pf (native)                                                          | pfSense/pf (Netgate, deprecated) |
| WAN Provider   | [ISP-REDACTED] ([WAN-IP-REDACTED]/29)                                               | Separate provider                |
| Domain         | [DOMAIN.ORG]                                                                  | [DOMAIN.ORG]                  |
| SPRS           | **101/110** (self-assessed, evidence-strict, 10/22/2026, recomputed 08/03/2026; weights verified 08/02/2026) | 106/110 (independently assessed) |

Physical co-location (shared rack enclosure, shared UPS) is noted in PE controls (4.10).

---

### 2.7 Applicability and interpretation

Which of the 110 requirements apply to this organization, and how each is interpreted for a one-person company with a secured home office, is written in **`DIWAI-APP-001`** (*Applicability and Interpretation Statement*, v1.0, 2026-10-23). It records four **not applicable** requirements (3.1.18, 3.1.19, 3.7.6, 3.13.14), seven **single-operator interpretations**, four **provisions for additional personnel**, and states what is **not** claimed as met. It does not lower any requirement and does not change the SPRS score. Where this plan and `DIWAI-APP-001` differ, the statement governs applicability and this plan governs implementation.

---

## 3. SYSTEM DESCRIPTION

### 3.1 System Purpose and Functions

The [DOMAIN.ORG] SecureMac Reference System provides secure information technology infrastructure for [ORGANIZATION]'s government contracting business operations, and serves as a research platform demonstrating Apple Silicon-based CMMC Level 2 compliance.

**Primary Functions:**

- WAN gateway and firewall (pf on Mac Mini host)
- AI/ML inference server (LM Studio + Open Web UI — LAN-restricted via nginx reverse proxy) and a read-only AI document library
- CUI/FCI document management — Nextcloud private cloud (LAN-restricted via nginx reverse proxy; MFA-enforced) with Collabora Online in-browser office editing
- Identity and access management (389-DS LDAP directory on VM)
- Security monitoring and threat detection (Wazuh SIEM + Suricata on VM)
- Web services and compliance dashboard (Apache httpd on VM)
- Email services (Postfix + Dovecot + Roundcube on VM)
- Network services (OpenVPN, Unbound DNS, NTP on VM)
- Metrics and monitoring (Prometheus + node-exporter on VM; Grafana decommissioned 2026-08-02)
- Compliance scanning (OpenSCAP on VM, mSCP on Mac host)
- CUI storage and backup (FileVault/LUKS encrypted; Time Machine + NAS archival)

### 3.2 System Components

#### Component 1: Mac Mini M4 Pro Host (securemac.[DOMAIN.ORG] / ai.[DOMAIN.ORG])

**Role:** Physical host, WAN gateway/firewall, AI inference server, management workstation

| Attribute    | Value                                                                     |
|:-------------|:--------------------------------------------------------------------------|
| Hostname     | securemac.[DOMAIN.ORG] / ai.[DOMAIN.ORG]                                        |
| LAN IP       | [LAN-IP-REDACTED]/24 (en6 — Thunderbolt USB Ethernet)                             |
| WAN IP       | [WAN-IP-REDACTED]/29 (en0 — embedded Ethernet, [ISP-REDACTED])                     |
| MGMT         | en1 — Wi-Fi ([HOME-LAN-REDACTED]) — management access only, not in CUI data path   |
| OS           | macOS 26.5 (Tahoe) — Build 25F71                                          |
| Hardware     | Apple Mac Mini (2024)                                                     |
| Chip         | Apple M4 Pro SoC (12-core CPU: 8P+4E, 16-core GPU, 16-core Neural Engine) |
| RAM          | 64 GB unified memory (LPDDR5X)                                            |
| Storage      | NVMe SSD — hardware encryption via Apple Secure Enclave                   |
| Architecture | ARM64 (Apple Silicon)                                                     |

**Security Controls (Mac Host):**

- FileVault full-disk encryption (AES-256, Apple Secure Enclave key storage)
- System Integrity Protection (SIP) enabled
- Gatekeeper application allowlisting
- XProtect + MRT malware detection (Apple native, continuously updated)
- pf firewall — stateful packet inspection, NAT, inbound port restrictions 
  - WAN (en0): restricted inbound; NAT outbound
  - LAN (en6/[LAN-IP-REDACTED]): managed access to VM and NAS
  - MGMT (en1/Wi-Fi): management access only — never blocked, not in CUI data path
- USB Guard — custom implementation (`/usr/local/sbin/usb-guard`, `/usr/local/sbin/usb-guard-monitor`) 
  - Mode: enabled (on); polls every 5 seconds via `diskutil` / `ioreg`
  - Allowlisted: Time Machine SSD (partition UUID: [HW-UUID-REDACTED]; replaced 2026-10-18, the failed drive's [HW-UUID-REDACTED] removed), and the CyberHygiene Project drive
  - All other USB mass storage force-ejected and logged to `/var/log/usb-guard.log`
  - LaunchDaemon: `org.diwai.usb-guard`
- nginx 1.31.0 reverse proxy (Homebrew, ARM64) — HTTPS only, LAN interface ([LAN-IP-REDACTED]:443) 
  - Proxies Open Web UI at https://ai.[DOMAIN.ORG]; WAN interface (en0) excluded
  - TLS: *.[DOMAIN.ORG] wildcard certificate (`/etc/ssl/diwai/[DOMAIN.ORG].crt`); TLSv1.2/1.3 only; HSTS enforced (max-age=31536000; includeSubDomains)
  - WebSocket proxying enabled (required for streaming AI responses)
  - LaunchDaemon: `org.diwai.nginx`; config: `/opt/homebrew/etc/nginx/servers/ai.[DOMAIN.ORG].conf`
- Open Web UI 0.11.4 (Python venv: `/opt/local/open-webui-venv`; updated from 0.9.5 under `DIWAI-CR-2026-10-03`) — bound to 127.0.0.1:3000 (localhost only); ENABLE_SIGNUP=false; single admin account ([USERNAME]); LaunchAgent: `org.diwai.open-webui`
- AI knowledge base: may contain `CUI_`-marked documents; on this system that marking is applied in advance and the documents are company-proprietary, not CUI (see §4.8)
- **AI model runtime: LM Studio 0.4.25+1** — the single model server since 2026-10-03 (`DIWAI-CR-2026-10-01`); LaunchAgent `org.diwai.lmstudio`, bound to **127.0.0.1:1234 only**; prompt logging off (`logSensitiveData` false); updates are applied manually by a person (decision register row 11)
  - Models (checked against the publisher's checksums): **Devstral Small 2 (24B, MLX 4-bit) — primary**; nomic-embed-text v1.5 f16 — embeddings; Gemma 4 E4B — fallback; Magistral Small 2509 (MLX 4-bit) — general questions and writing, via the Open WebUI assistant "Magistral (general)" (`DIWAI-CR-2026-10-08`). Gemma 4 26B (QAT, MLX 4-bit) is also installed (previously unrecorded; weights identical to the Mac Studio copy). gpt-oss-20b, which followed an injected instruction in testing and was barred from checks, was **deleted 2026-10-18** (`DIWAI-CR-2026-10-13`)
  - Retired 2026-10-03: Ollama, mlx-lm/Magistral and LiteLLM (launch files renamed `.disabled`; ports 11434, 8081 and 4000 verified silent). Their model files were removed 2026-10-03 (`DIWAI-CR-2026-10-05`), except the retired Magistral MLX model (13 GB), which remains on disk
- **DIWAI document library** (`DIWAI-CR-2026-10-02`, approved 10-03-2026): a local search index of runbooks, runbook cards and vendor guides chosen by the owner
  - Read-only search server for the AI (MCP), LaunchAgent `org.diwai.rag-mcp`, **127.0.0.1:8767 only**; it offers search tools and no write tool, so the AI cannot add to or change its own library; passages are passed to the model as marked data, and a planted "ignore your instructions" document was tested and ignored
  - Library manager (`DIWAI Sysadmin Library.app`), started on demand by the owner, **127.0.0.1:8766 only**; documents are added only by a person
- **Compliance library** (`DIWAI-CR-2026-10-13`): a second index of the same design for standards, policies and assessment papers, now also diwai's own SSP, POA&M, SBOM and change records and NIST's Rev 2 to Rev 3 mapping (175 documents), so that they are not mixed with system-administration guides; read-only search server `org.diwai.rag-mcp-compliance`, **127.0.0.1:8769 only**, with a read-only exact lookup of NIST requirements (`requirement_lookup`, Rev 2 to Rev 3); all libraries also read spreadsheets and, for scanned PDFs, OCR text that is labelled machine-read and refused when too uncertain (`DIWAI-CR-2026-10-16`); manager `DIWAI Compliance Library.app`, **127.0.0.1:8768 only**, started by the owner. Each manager shows its library's name in a banner, the browser tab and above the drop box, to prevent misfiling
- **Contract Library, RFPShred and contract tools** (`DIWAI-CR-2026-10-13`): brought from the owner's Mac Studio on 2026-10-18 after every file was checked against the drive's manifest (62,431 of 62,431). `~/rag-library` (manager `Contract Library.app`, **127.0.0.1:8765 only**; search tool `contract-rag` for LM Studio), `~/RFPShred` and the `contract-tools` server, which asks a person to confirm before CUI is processed. LM Studio's tool-call confirmation stays on; web tools stay off. Embeddings use the Q4_K_M build the index was made with
- **Repair library `diwai-repair`** (`DIWAI-CR-2026-10-07`): runs only repairs the ISSO approved with the YubiKey (PIN + touch, signature over the exact code, re-checked every run with root-owned tools); installed root-owned in `/usr/local/lib/diwai-repair`; each run shows the planned change and needs a typed yes, keeps a backup and can be undone. VM sudo now asks for the password (`DIWAI-CR-2026-10-06`; was `NOPASSWD: ALL`)
- **Diagnosis tool `diwai-diagnose`** (`DIWAI-CR-2026-10-09`): run on demand by a person; reads the VM monitor's report and checks the Mac, then shows each problem as a plain-words form naming the approved repair, if any. It never uses sudo and never runs a repair; the local model only explains and chooses among repairs approved for that problem
  - Aider (coding assistant, LM Studio model) drafts runbooks, repairs and tests on the build side. It never edits a live configuration file on its own judgment; it may run an ISSO-approved repair only after a person types yes to the exact command (decision register row 13). It is started through the `aider-leashed` launcher, which refuses project-level Aider settings (`DIWAI-CR-2026-10-04`)
- **Nextcloud 32.0.11.1 private-cloud CUI/FCI document repository** (`/opt/local/nextcloud`, data dir `/opt/local/nextcloud/data` — FileVault-encrypted at rest) — the canonical store for CUI/FCI documents (SSP, POA&M, SBOM, evidence) 
  - Served at `https://cloud.[DOMAIN.ORG]` via the nginx reverse proxy on the LAN interface ([LAN-IP-REDACTED]:443) and loopback only — **never exposed to WAN**, no public DNS record (local resolution only)
  - Runtime: Homebrew PHP-FPM 8.3 + local Redis (127.0.0.1:6379) cache/locking
  - Identity: 389-DS via **LDAPS** (`ldaps://services.[DOMAIN.ORG]:636`, base `dc=diwai,dc=org`); database: MariaDB on the VM
  - **MFA: TOTP two-factor authentication (**`twofactor_totp`**) enforced instance-wide** (operator enrolled with TOTP + backup codes, confirmed 06/11/2026); `admin_audit` enabled; `session_lifetime=1800`, `remember_login_cookie_lifetime=0`
  - Group-based access control via 389-DS groups (`cn=cui-users` restricts the CUI groupfolder; `cn=users` for Operations/AI-Knowledge-Base)
  - Office editing: Collabora Online (`richdocuments` 9.1.0) bound to loopback (127.0.0.1:9980), reached only by Nextcloud's PHP backend over the WOPI protocol — never exposed through nginx or the LAN; the nginx reverse proxy remains the sole CUI-bearing TLS boundary
- Time Machine backup to dedicated SSD with auto-mount LaunchAgent (`org.diwai.mount-tm-drive`, script `/usr/local/sbin/mount-tm-drive.sh`) — RunAtLoad, fires 5 seconds after login; resolved a FileVault-encrypted-volume auto-mount failure that caused a 17-day backup gap (2026-04-28 to 2026-05-14)
- mSCP compliance baseline: `diwai_phase1.yaml` — **130/135 rules passing (96.30%)**, measured 2026-08-01; weekly automated scan **restored 2026-08-01** after being found non-functional since ~June (POA&M-015). POA&M-003 tracks the **5** failing rules

**MFA Status (Mac Host) — UPDATED 10/09/2026:**
YubiKey Nano 5C FIPS PIV hardware-token authentication was attempted twice (lockout incidents 2026-04-15 and 2026-05-15; both recovered via sysadmin break-glass, certs unpaired both times). Following the second incident, the approach was judged too technically fragile for reliable production use and **abandoned on 2026-06-06**. The Mac host's MFA strategy now follows the same path as the VM and the CyberInABox Linux systems: **TOTP via Authenticator app (RFC 6238)**. **Current state (2026-10-09):** SSH to the Mac requires a public key, the account password and a TOTP code (`/etc/ssh/sshd_config.d/50-diwai-mfa.conf` and `/etc/pam.d/sshd`; `DIWAI-CR-2026-08-17`, POA&M-007 closed). A macOS update removed the PAM TOTP line on 2026-09-03; it was restored and proven on 2026-10-09 (`DIWAI-CR-2026-10-11`), and an hourly check with a control-health alert now guards it. After every macOS update the Patch Review Procedure (DIWAI-PR-001 §4.7) requires the check to be read at once, through step 5 of `fix-mscp-regression.sh`, without waiting for the hourly run. Local console logon remains password only. POA&M-001 (YubiKey re-pairing) is **closed — superseded**.

#### Component 2: services.[DOMAIN.ORG] — Rocky Linux 9.7 UTM VM

**Role:** Server services — SIEM, identity, web, email, network, monitoring

| Attribute    | Value                                                                                                   |
|:-------------|:--------------------------------------------------------------------------------------------------------|
| Hostname     | services.[DOMAIN.ORG]                                                                                      |
| IP           | [LAN-IP-REDACTED]/24                                                                                           |
| OS           | Rocky Linux 9.7 (Blue Onyx)                                                                             |
| Architecture | aarch64 (ARM64 — UTM VM on Apple M4 Pro)                                                                |
| FIPS Mode    | Enabled (`fips-mode-setup --check`: FIPS mode is enabled)                                                 |
| OpenSCAP CUI | **101/101** (weekly automated scan, tailored profile) — one documented deviation tailored out, Appendix E.3 |

**Services running on VM:**

| Service                  | Version      | Purpose                                                                                                                                                                                                                       |
|:-------------------------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 389-DS LDAP              | dirsrv@diwai | Identity directory (dc=diwai,dc=org)                                                                                                                                                                                          |
| Apache httpd + PHP-FPM   | 2.4.x / 8.x  | Dashboard (securemac.[DOMAIN.ORG]) with LDAP auth                                                                                                                                                                                |
| MariaDB                  | 10.5         | Database backend for web services                                                                                                                                                                                             |
| Wazuh Manager            | 4.14.5       | SIEM — security monitoring, FIM, alerts                                                                                                                                                                                       |
| Wazuh Dashboard          | 4.14.5       | SIEM UI (HTTPS on VM)                                                                                                                                                                                                         |
| Wazuh Indexer            | 4.14.5       | Search/analytics backend                                                                                                                                                                                                      |
| Suricata IDS             | 7.0.13       | Network intrusion detection                                                                                                                                                                                                   |
| Prometheus               | 3.11.2       | Metrics collection                                                                                                                                                                                                            |
| ~~Grafana~~                  | ~~13.1.1~~       | Metrics visualization — **decommissioned 2026-08-02** (`DIWAI-CR-2026-08-04`)                                                                                                                                                       |
| Prometheus Node Exporter | —            | Host metrics                                                                                                                                                                                                                  |
| OpenVPN Server           | —            | Remote access VPN (diwai config)                                                                                                                                                                                              |
| Unbound DNS              | —            | Recursive DNS resolver                                                                                                                                                                                                        |
| Postfix                  | 3.5.25       | SMTP email server (TLS)                                                                                                                                                                                                       |
| Dovecot                  | 2.3.16       | IMAP/POP3 email server                                                                                                                                                                                                        |
| Roundcube                | —            | Webmail (AES-256-CBC cipher config + FPM pool fix applied for FIPS compatibility)                                                                                                                                             |
| YARA                     | 4.5.2        | Malicious-code pattern scanner — 5,972 rules, Wazuh-integrated on FIM events + weekly full-system scan (SI-3 primary, FIPS-native). *ClamAV 1.4.3 decommissioned 06/12/2026 — non-functional under FIPS; see DIWAI-EV-SI3-002.* |
| fapolicyd                | 1.4.5        | File access policy / application whitelisting; enforcing (`permissive = 0`), trust from the package database and a local file (checked 2026-10-23) |
| USBGuard                 | —            | USB device control                                                                                                                                                                                                            |
| auditd                   | —            | System call auditing                                                                                                                                                                                                          |
| firewalld                | —            | Host firewall                                                                                                                                                                                                                 |
| rsyslog                  | —            | Log forwarding                                                                                                                                                                                                                |
| chronyd                  | —            | NTP time synchronization                                                                                                                                                                                                      |
| diwai-control-health     | local script | Control-health monitor every 15 min (`DIWAI-CR-2026-08-20`); mails the owner on a change of state and, since `DIWAI-CR-2026-10-09`, also writes its results to `/var/lib/diwai-control-health/latest.json` for `diwai-diagnose`; checks 13 (Mac) and 16 (VM) watch the two inactivity-enforcement jobs (`DIWAI-CR-2026-10-18`) |

**Malicious-code protection (SI-3):** Provided by **YARA 4.5.2** (5,972 rules), integrated with Wazuh active-response on FIM rules 550/554 (new/modified files) and supplemented by a **weekly full-system YARA scan** (`yara-fullscan.timer`). Layered with **VirusTotal** reputation lookups, **fapolicyd** application allow-listing, **SELinux** enforcing, and **Suricata** network IDS — all FIPS-native. *ClamAV 1.4.3 was decommissioned on 06/12/2026: under FIPS it could neither download nor load any signature database (OpenSSL verification failure), so it provided no detection. The control substitution is documented in* `Compliance/Evidence/SI-3_Control_Substitution_ClamAV_Decommission_2026-06-12.md` *(DIWAI-EV-SI3-002), which supersedes RISK-2026-004. POA&M-002 is closed.*

#### Component 3: Synology NAS (nas.[DOMAIN.ORG])

**Role:** Supporting infrastructure — CUI storage, log archival, backup target

| Attribute  | Value                                                                 |
|:-----------|:----------------------------------------------------------------------|
| Hostname   | nas.[DOMAIN.ORG]                                                         |
| IP         | [LAN-IP-REDACTED]/24                                                        |
| Device     | Synology 8-bay NAS                                                    |
| Encryption | Folder-level AES-256/SHA-256 (non-FIPS second layer)                  |
| Shares     | DataStore (SMB; LDAP-authenticated against services.[DOMAIN.ORG] 389-DS) |

**Note:** Synology folder encryption is not FIPS 140-2 validated. Data arriving from the VM (Wazuh alert archives) is pre-encrypted by FIPS-validated OpenSSL (AES-256-CBC + PBKDF2/SHA-256) before transfer over SSH (AES-256-CTR). The NAS encryption is a defense-in-depth second layer, not a FIPS claim. NAS is classified as **supporting infrastructure** within the physical security boundary — not as part of the FIPS cryptographic boundary itself.

### 3.2.1 Role concentration and the daily-driver question (added 2026-08-04)

**This system is a reference model**, intended for adoption by very small
businesses in either of two configurations: a secure single-operator system, or a
domain controller serving a VSB of roughly fifteen users or fewer. Design
decisions are therefore recorded with that adoption in mind, not only with this
instance in mind.

**One such decision is recorded here as a caution against the present
configuration.** The Mac mini currently carries: perimeter firewall, hypervisor
for the service VM, the Nextcloud CUI document store, the local AI inference
stack, **and the operator's day-to-day working environment**. §3.2 describes its
role as including "management workstation," and in practice it is the machine the
operator works on.

**The system owner's guidance for adopters is that this should not be done** —
that even a one-person business would be well advised to place a separate
workstation on the network as the daily driver, rather than working on the
appliance itself. That guidance is sound and **this deployment does not currently
follow it.**

**Why it matters technically, not just tidily.** Nextcloud stores CUI as
**plaintext files** on this host (server-side encryption is disabled; see
POA&M-023). Any process running as the operator's account reads the entire CUI
store without passing through Nextcloud's authentication, 2FA, group ACLs or
audit log. Daily-driver activity — browsing, mail, general software — is exactly
what widens the population of such processes. The concentration also means a
single host compromise reaches the firewall, the hypervisor and the CUI store
together.

**Planned remediation.** Introduce the **existing SCAP-hardened laptop** to the
LAN as the model daily driver, moving routine work off the appliance. This
doubles as reference-model evidence: it demonstrates the separation the guidance
recommends, in the architecture adopters are being asked to copy. Recorded as a
planned architectural change; **not yet scheduled**.

**Connection policy for that device.** Wired Ethernet is the required default in
the office, enforced by network design rather than instruction — the CUI segment
is delivered over wired interfaces and governed by the `pf` ruleset. Wireless is
permitted **only away from the office**, where no wired connection is available,
subject to WPA2/WPA3 with authentication, VPN access to the boundary rather than
direct service exposure, and a prohibition on processing CUI over open or
untrusted networks (`DIWAI-PE-MP-001` v1.1).

> **Scoring dependency — act before deployment, not after.** Requirement 3.1.16
> (*authorise wireless access prior to allowing such connections*) was assessed
> as **met on 2026-08-03**, recovering 5 points, on the specific basis that
> wireless is **not permitted**: `en1` is powered off, nothing re-enables it, and
> `pf` bars CUI egress by that path (§2.5.2). **Introducing a device that uses
> wireless away from the office changes that basis.** The requirement can still
> be met — authorised wireless with adequate protection satisfies it — but the
> authorisation, the conditions above and §2.5.2 must be updated **in advance of
> the laptop being deployed**. Deploying first and documenting afterwards would
> reproduce, deliberately, the pattern this assessment exists to correct.

---

### 3.3 Network Topology

```
Internet
    |
Mac Mini M4 Pro (pf firewall)
  WAN: en0 ([WAN-IP-REDACTED]/29 -- [ISP-REDACTED])
  LAN: en6 ([LAN-IP-REDACTED]/24 -- Thunderbolt USB Ethernet)
  MGMT: en1 (Wi-Fi, [HOME-LAN-REDACTED] -- never blocked, not in CUI path)
    |
    +-- services.[DOMAIN.ORG] ([LAN-IP-REDACTED]) -- Rocky Linux 9.7 aarch64 VM
    +-- nas.[DOMAIN.ORG] ([LAN-IP-REDACTED])     -- Synology 8-bay NAS

DNS ([DOMAIN.ORG] zone):
  [DOMAIN.ORG] / www         -> [WAN-IP-REDACTED]
  ai.[DOMAIN.ORG]            -> [LAN-IP-REDACTED]   (LAN only, via nginx reverse proxy)
  cloud.[DOMAIN.ORG]         -> [LAN-IP-REDACTED]   (LAN only, via nginx reverse proxy; Nextcloud)
  mail.[DOMAIN.ORG]          -> [WAN-IP-REDACTED]
  vpn.[DOMAIN.ORG]           -> [WAN-IP-REDACTED]
  securemac.[DOMAIN.ORG]     -> [LAN-IP-REDACTED]  (VM dashboard, LDAP-authenticated)
```

> **Figure 3.3 — Network & Software-Stack Schematic:** see `Compliance/Architecture/RS2_Network_Schematic.svg` (editable source `RS2_Network_Schematic.drawio`) for the full device-level topology, per-node software stack, trust boundaries, and the LAN-only AI egress control.

**Physical co-location note:** The Mac Mini M4 Pro shares a locked rack enclosure with CyberInABox ([DOMAIN.ORG]) systems. These are architecturally and logically independent, standalone systems — no shared network, no shared services, no CA-3 interconnection beyond physical-boundary acknowledgment, and no shared policy set. The rack's physical security controls (PE-2, PE-3, PE-11) for the [DOMAIN.ORG] system are documented independently in DIWAI-PE-MP-001.

### 3.4 Malware Protection Architecture

| Layer                                | Technology                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Status                    |
|:-------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| Network IDS/IPS                      | Suricata 7.0.13 (VM)                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Operational               |
| File Integrity Monitoring            | Wazuh FIM with VirusTotal integration (VM)                                                                                                                                                                                                                                                                                                                                                                                                                            | Operational               |
| Application Whitelisting             | fapolicyd (VM) + Gatekeeper (Mac)                                                                                                                                                                                                                                                                                                                                                                                                                                     | Operational               |
| Host AV — Mac                        | XProtect + MRT (Apple native, auto-updated)                                                                                                                                                                                                                                                                                                                                                                                                                           | Operational               |
| Malicious-code scanning — VM         | **YARA 4.5.2** (5,972 rules) — Wazuh active-response on FIM 550/554 + **weekly full-system scan** (`yara-fullscan.timer`)                                                                                                                                                                                                                                                                                                                                                       | **Operational** (FIPS-native) |
| Reputation                           | VirusTotal (hash lookup on FIM events)                                                                                                                                                                                                                                                                                                                                                                                                                                | Operational               |
| *(retired)* Host AV — VM               | ~~ClamAV 1.4.3~~ — **decommissioned 06/12/2026**; **incompatible with FIPS 140** (could neither download nor load a signature database), replaced by the YARA stack (DIWAI-EV-SI3-002). **Packages removed from the VM 08/01/2026** (`DIWAI-CR-2026-08-01` C14), closing the inventory-vs-reality gap **F-2026-08-06**                                                                                                                                                                      | Retired                   |
| *(retired)* Metrics visualization — VM | ~~Grafana 13.1.1~~ — **decommissioned 08/02/2026** (`DIWAI-CR-2026-08-04`); **not patchable** — `rpm.grafana.com` failed GPG verification on `repomd.xml`, and the failing repository also broke `dnf check-update` system-wide — against limited operational use. **Prometheus + node-exporter retained**, so metrics collection is unaffected; only visualization was retired. No control named Grafana as its sole mechanism (AU-6 / 3.3.3 and 3.14.7 rest on Wazuh, Suricata, and auditd) | Retired                   |

> **Figure 3.4 — CUI Data-Flow:** see `Compliance/Architecture/RS2_CUI_DataFlow.svg` (editable `.drawio`) — how CUI is received over encrypted channels, authenticated at 389-DS with MFA, processed in-boundary (incl. the air-gapped AI), stored encrypted at rest, continuously monitored, and backed up.

---

## 4. SECURITY CONTROL IMPLEMENTATION

**Control Status Legend:**

- **IMPLEMENTED** — Control fully operational and verified
- **ENHANCED** — Control exceeds baseline requirements
- **NOT MET** — Control not implemented; SPRS deficit applies
- **PARTIAL** — Partially implemented; compensating controls documented
- **N/A** — Not applicable to this system

### 4.1 Access Control (AC)

| Control | Name                                                     | Status      | Implementation                                                                                                                                                                                                                                                                                                                                           |
|:--------|:---------------------------------------------------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.1.1   | Limit access to authorized users                         | IMPLEMENTED | 389-DS LDAP directory (dc=diwai,dc=org) manages user identities for VM services. macOS account management for the Mac host. SSH key-based access only. nginx proxy restricts the AI and Nextcloud interfaces to LAN-authorized users. Nextcloud authenticates against 389-DS over LDAPS and enforces TOTP 2FA on every login (see 3.5.3).                |
| 3.1.2   | Limit access to authorized functions                     | IMPLEMENTED | 389-DS group-based RBAC (cn=admins group required for dashboard access). Nextcloud groupfolder access is group-restricted (cn=cui-users for the CUI groupfolder; cn=users for Operations/AI-Knowledge-Base). sudo on the VM for privileged operations. macOS standard user + sudo for host admin. fapolicyd enforces application whitelisting on the VM. |
| 3.1.3   | Control flow of CUI                                      | IMPLEMENTED | pf firewall (Mac host) enforces WAN/LAN/MGMT boundaries. firewalld on the VM restricts inter-service traffic. nginx proxies the AI interface — no direct WAN exposure. TLS/SSH for all data in transit.                                                                                                                                                  |
| 3.1.4   | Separation of duties                                     | N/A         | Single-person organization. Separation enforced via audit logging, the break-glass account, and external review processes.                                                                                                                                                                                                                               |
| 3.1.5   | Least privilege                                          | IMPLEMENTED | Named user ([USERNAME]) with sudo elevation for privileged operations; sudo asks for the password except for three read-only diagnostic scripts on the VM and two on the Mac (`DIWAI-CR-2026-10-21`, `-10-22`). No service accounts hold unnecessary privileges. fapolicyd limits application execution on the VM.                                                                                                                                                                                  |
| 3.1.6   | Non-privileged accounts                                  | IMPLEMENTED | Administrative tasks require explicit sudo. No direct root SSH. All elevated actions logged.                                                                                                                                                                                                                                                             |
| 3.1.7   | Prevent non-privileged execution of privileged functions | IMPLEMENTED | fapolicyd application whitelisting on the VM. macOS SIP + Gatekeeper on the host. SELinux enforcing on the VM.                                                                                                                                                                                                                                           |
| 3.1.8   | Limit unsuccessful logon attempts                        | IMPLEMENTED | PAM faillock on the VM (3 failed attempts within a 5-minute window lock the account for 15 minutes: `deny = 3`, `fail_interval = 300`, `unlock_time = 900`). The 389-DS directory locks after 3 failed binds for 3600 seconds. macOS: 5 consecutive failed attempts lock the account until 900 seconds after the last failure (`diwai.authentication.lockout`). Aligned to the DoD Rev 3 values and proven by refusal on 2026-10-09 (`DIWAI-CR-2026-10-11`).                                                                                                                                                                                                                                                               |
| 3.1.9   | Privacy and security notices                             | IMPLEMENTED | Login banner confirmed on the VM ("AUTHORIZED USE ONLY — [DOMAIN.ORG] SecureMac Reference System"). macOS login banner configured on the host.                                                                                                                                                                                                              |
| 3.1.10  | Session lock                                             | IMPLEMENTED | SSH `ClientAliveInterval` 900s (15 min) on the VM. macOS screen lock configured on the host.                                                                                                                                                                                                                                                               |
| 3.1.11  | Session termination                                      | IMPLEMENTED | SSH `ClientAliveCountMax` enforced; sessions terminate after the idle period. GUI sessions lock automatically.                                                                                                                                                                                                                                             |
| 3.1.12  | Monitor/control remote access                            | IMPLEMENTED | All SSH sessions logged to rsyslog + Wazuh. Failed login attempts generate Wazuh alerts.                                                                                                                                                                                                                                                                 |
| 3.1.13  | Cryptographic mechanisms for remote access               | IMPLEMENTED | FIPS-approved SSH ciphers on the VM (FIPS mode enforces cipher restriction). TLS 1.2/1.3 for all HTTPS services. nginx enforces TLSv1.2/1.3 with HSTS.                                                                                                                                                                                                   |
| 3.1.14  | Route remote access via managed access control points    | IMPLEMENTED | All external access via the pf firewall (Mac host). The VPN (vpn.[DOMAIN.ORG]) is switched off since 2026-10-25 (`DIWAI-CR-2026-10-51`); there is no remote way in until it is re-enabled by a recorded change.                                                                                                                                                                                                                                    |
| 3.1.15  | Authorize remote access prior to connection              | IMPLEMENTED | SSH requires key-based authentication; no anonymous access. VPN requires client certificates.                                                                                                                                                                                                                                                            |
| 3.1.16  | Authorize wireless access                                | N/A         | Wi-Fi (en1/MGMT) used for management only — never blocked, not in the CUI data path. No wireless APs in the CUI network.                                                                                                                                                                                                                                 |
| 3.1.17  | Protect wireless access                                  | N/A         | As above.                                                                                                                                                                                                                                                                                                                                                |
| 3.1.18  | Control mobile device connections                        | IMPLEMENTED | USBGuard daemon active on the VM; custom USB Guard (mode: on) on the Mac host.                                                                                                                                                                                                                                                                           |
| 3.1.19  | Encrypt CUI on mobile devices                            | IMPLEMENTED | LUKS AES-256-XTS on VM storage (FIPS 140-2). FileVault / Apple Secure Enclave on the Mac host.                                                                                                                                                                                                                                                           |
| 3.1.20  | Control portable storage devices                         | IMPLEMENTED | USBGuard allowlist on the VM. Custom USB Guard on the Mac host with the Time Machine SSD UUID allowlisted; all other USB storage force-ejected and logged. The guard is switched off only by the owner for a stated transfer: 2026-10-18 09:10–10:48 (1 h 39 min; `DIWAI-CR-2026-10-13` §5.1), when the monitor writes no log.                                                                                                                                                                                               |
| 3.1.21  | Limit portable storage on external systems               | IMPLEMENTED | **DIWAI-AUP-001 §5.1 and §2.6** (corrected 2026-09-15, **F-2026-09-03**: the prior citation "§4.2" resolved to nothing — the AUP has no §4.2) prohibit storing CUI on unencrypted media and require authorised, encrypted drives. USB Guard (Evidence/USBGuard_Configuration_Evidence.md) enforces device-level authorization for portable storage connected to SPN systems.                                                                    |
| 3.1.22  | Control CUI on publicly accessible systems               | IMPLEMENTED | No CUI on public-facing systems. The AI interface (Open Web UI) is bound to localhost — no WAN exposure.                                                                                                                                                                                                                                                 |

### 4.2 Awareness and Training (AT)

| Control | Name                                         | Status  | Implementation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:--------|:---------------------------------------------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.2.1   | Ensure personnel are aware of security risks | **PARTIAL** | DIWAI-ATP-001 (Security Awareness and Training Policy, v1.0, 02/15/2026) is approved and establishes the training program (§3.2, AT-2). However, no [DOMAIN.ORG]-specific training delivery/completion record has been produced. The SSP's prior citation of "TCC-SAT-FY2026" was a CyberInABox/CPN-specific training record and has been removed (06/11/2026) per the determination that [DOMAIN.ORG] is an independent, standalone system that does not share evidence with CyberInABox. **POA&M-008** opened to deliver and document [DOMAIN.ORG]-specific initial training. |
| 3.2.2   | Security awareness training on threats       | **PARTIAL** | Same gap as 3.2.1 — DIWAI-ATP-001 §3.2 defines annual refresher training requirements, but no [DOMAIN.ORG]-specific delivery/completion record exists yet. **POA&M-008**.                                                                                                                                                                                                                                                                                                                                                                                                 |
| 3.2.3   | Security training before access and annually | **PARTIAL** | Same gap as 3.2.1/3.2.2 — DIWAI-ATP-001 establishes the requirement; [DOMAIN.ORG]-specific completion documentation is pending. **POA&M-008**.                                                                                                                                                                                                                                                                                                                                                                                                                            |

### 4.3 Audit and Accountability (AU)

**Status:** All AU controls **IMPLEMENTED**. The VM runs a full Wazuh SIEM stack (Manager 4.14.5 + Dashboard + Indexer) providing centralized, searchable audit logging. auditd captures system calls; rsyslog forwards logs to the Wazuh indexer. All audit data is stored on encrypted VM storage.

- **AU-2 / 3.3.1:** auditd (system calls), rsyslog (application/system events), Wazuh (security events, FIM, vulnerability data) — comprehensive audit-record coverage.
- **AU-3 / 3.3.2:** All records include timestamp, source, event type, outcome, and user identity. The Wazuh indexer provides long-term searchable retention.
- **AU-6 / 3.3.3:** The Wazuh Dashboard provides real-time audit review. The ISSO reviews Wazuh alerts daily. (Grafana previously provided supplementary metrics dashboards; it was decommissioned 2026-08-02 per `DIWAI-CR-2026-08-04`. Audit review has never depended on it — Wazuh is the audit-review mechanism, and Prometheus retains metrics collection.)
- **AU-9 / 3.3.8:** Wazuh indexer data is restricted to the wazuh-indexer service account. auditd logs are root-owned. FIPS-encrypted VM storage protects the audit partition.
- **Nextcloud:** the `admin_audit` app is enabled, logging authentication, sharing, and file-access events to `/opt/local/nextcloud/data/nextcloud.log` (JSON). Forwarding this log into Wazuh (decoder + rule) is a pending deployment task, not a control gap — the audit data is captured locally on the FileVault-encrypted host volume in the interim.

### 4.4 Configuration Management (CM)

**Status:** All CM controls **IMPLEMENTED**.

- **3.4.1 (CM-6):** Configuration baselines enforced via the tailored OpenSCAP CUI profile on the VM (**101/101**, one documented deviation tailored out — Appendix E.3) and mSCP on the Mac host (**134/136**; 3 rules remediated 2026-08-02, 2 remain and neither ships mSCP remediation code — POA&M-003). Weekly automated scans publish results to the compliance dashboard.
- **3.4.3 (CM-3):** Wazuh FIM monitors critical paths (`/etc`, `/usr/bin`, `/usr/sbin`, `/boot`) for unauthorized changes; auditd captures file-level system calls.
- **3.4.6–3.4.8:** fapolicyd provides deny-by-default application execution on the VM. macOS SIP + Gatekeeper enforces application signing on the host.
- **3.4.9:** fapolicyd (VM) is enforcing and refuses to execute a binary that is not in the package database or the local trust file (final rule `deny_audit perm=execute all : all`; read 2026-10-23, amendment 30). **Exceptions by rule:** shell scripts are allowed for every user; Python, Java and JavaScript are denied unless trusted, except when run by root; root running a trusted program is allowed everything. In summary: fapolicyd (VM) blocks execution of software that is not in the package database or the local trust file; Gatekeeper (Mac) enforces application signing. Neither prevents a user with administrative rights from installing software; installation is governed by change control (3.4.3). **Limit:** fapolicyd integrity checking is off (`integrity = none`), so a modified trusted file would still run; such changes are detected by Wazuh file-integrity monitoring. **User-installed add-ons:** the ONLYOFFICE "AI Tools (beta)" add-on (command execution, MCP, web search) is **not approved**: its trial on 2026-10-22 showed it runs commands with no approval step (`DIWAI-CR-2026-10-19` §2D; amendment 27). It stays uninstalled; any reconsideration needs a vendor approval step and a new trial.

### 4.5 Identification and Authentication (IA)

| Control      | Name                            | Status      | Implementation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-------------|:--------------------------------|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.5.1        | Identify system users           | IMPLEMENTED | 389-DS LDAP (dc=diwai,dc=org) manages all VM user identities. macOS directory services manage the host.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3.5.2        | Authenticate before access      | IMPLEMENTED | SSH key authentication on the VM. macOS password authentication on the host. LDAP authentication for the web dashboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3.5.3        | Multi-factor authentication     | **PARTIALLY IMPLEMENTED** | **Remote and privileged access is multifactor on both hosts and at the CUI repository.** **VM (services.[DOMAIN.ORG]):** SSH requires a public key and a TOTP code (`AuthenticationMethods publickey,keyboard-interactive:pam`, `pam_google_authenticator`, no `nullok`), proven by positive and negative test (`DIWAI-CR-2026-08-12`; POA&M-004 closed). **Mac host (securemac.[DOMAIN.ORG]):** SSH requires a public key, the account password and a TOTP code (`DIWAI-CR-2026-08-17`; POA&M-007 closed). **A macOS update removed the Mac's PAM TOTP line on 2026-09-03; it was restored and proven on 2026-10-09** (`DIWAI-CR-2026-10-11`, finding 7). The Mac now verifies the line hourly and at every boot, and the control-health monitor fails if it disappears (check 15). **Nextcloud CUI repository (cloud.[DOMAIN.ORG]):** TOTP enforced instance-wide (`twofactor_totp`) over LDAPS-backed identity. **Exemption:** the VM ([LAN-IP-REDACTED]) reaches the Mac with a key alone, for two production jobs (`DIWAI-CR-2026-08-17` §3.2). **Not covered:** local console logon on either host remains single-factor (password). **Status rationale:** MFA covers remote and privileged access but not every logon path, so the methodology's partial credit applies. **SPRS deficit: −3 points.** The YubiKey approach was abandoned 06/06/2026 (see 3.2, Component 1, "MFA Status"). |
| 3.5.4        | Replay-resistant authentication | IMPLEMENTED | SSH uses ephemeral key exchange (replay-resistant by design). TLS session tokens are not reusable. FIPS-approved algorithms on the VM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 3.5.5–3.5.11 | Password management controls    | IMPLEMENTED | 389-DS enforces password complexity, history, aging, and lockout policies. FIPS-compliant password hashing on the VM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

> **Note on IA Policy version:** The June 6 strategy change required the [DOMAIN.ORG] Identification and Authentication Policy (**DIWAI-IAP-001**, v1.0, 02/15/2026 — corrected from this SSP's earlier "TCC-IAP-001" citation, which refers to a different, CyberInABox/CPN-scoped document) to be updated to reflect the unified TOTP-everywhere approach, replacing the prior text that described YubiKey PIV as the Mac-host MFA mechanism. **DIWAI-IAP-001 v1.1 has been issued (effective 06/06/2026)**: §3.2.3 now documents MFA as NOT MET pending POA&M-004/POA&M-007, and the YubiKey approach is recorded as superseded.

### 4.6 Incident Response (IR)

| Control | Name                            | Status      | Implementation                                                                                                                                                                                                                                                                                  |
|:--------|:--------------------------------|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.6.1   | IR capability                   | IMPLEMENTED | DIWAI-IRP-001 (Incident Response Policy and Procedures) approved and effective 11/02/2025. Wazuh provides automated incident detection and alerting.                                                                                                                                            |
| 3.6.2   | Track/document/report incidents | IMPLEMENTED | Incidents are tracked in the Incident Register, `DIWAI-INCREG-001` v1.0 (approved by the owner 2026-10-23): seven incidents, each with how it was found, cause, recovery, who it was reported to and whether external reporting applied (none so far). The designated official is the IR Coordinator / ISSO (`DIWAI-IRP-001` §2.1); with one operator, reporting is self-reporting. **INC-003 to INC-007 were reconstructed on 2026-10-23, not written at the time.** The register also shows detection is weak (two of five found by no control, one flagged but unread). The Wazuh Dashboard provides an incident timeline. |
| 3.6.3   | Test IR capability              | IMPLEMENTED     | The IR capability was tested by the annual tabletop exercise required by DIWAI-IRP-001, **conducted and signed 2026-08-03** (`DIWAI-IR-TTX-001`; scenario R-02, compromise of an internet-published service reaching the CUI data tier; single participant, the owner, recorded as a limitation in `DIWAI-RAR-001` R-12). It identified ten gaps; two new POA&M items were opened (POA&M-056, -057). POA&M-006 closed 2026-08-03. |

### 4.7 Maintenance (MA)

| Control     | Name                       | Status      | Implementation                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:------------|:---------------------------|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.7.1       | Perform maintenance        | IMPLEMENTED | **Maintenance is reviewed and applied deliberately, not automatically.** `dnf-automatic` is **download-only** (`apply_updates = no`) on the VM — it stages updates and applies nothing (accepted deviation, Appendix E.3). Updates are applied at the **monthly patch review** `DIWAI-PR-001` (and on return after any gap over 30 days; PATCH-class CRITICAL within 72 hours of detection), logged in `DIWAI-PR-LOG`. macOS Software Update and Homebrew on the host, likewise applied at review. Identification: `diwai-cve-scan` (VM) and `diwai-cve-scan-mac` (host), plus Wazuh vulnerability detection. |
| 3.7.2       | Control maintenance tools  | IMPLEMENTED | Maintenance activities are logged. No remote maintenance tools other than SSH.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 3.7.3–3.7.4 | Sanitize/check media       | IMPLEMENTED | DIWAI-PE-MP-001 §4.5 (Media Sanitization, MP-6) procedures. Wazuh FIM monitors diagnostic tools.                                                                                                                                                                                                                                                                                                                                                                                          |
| 3.7.5       | MFA for remote maintenance | IMPLEMENTED     | Remote (nonlocal) maintenance is performed over SSH, which requires multifactor authentication on both hosts: a public key plus a TOTP code on the VM (`DIWAI-CR-2026-08-12`), and a public key, the account password and a TOTP code on the Mac (`DIWAI-CR-2026-08-17`; the +5 is recorded under `DIWAI-CR-2026-08-18`). The Mac's TOTP line was absent from 2026-09-03 to 2026-10-09 after a macOS update, and was restored and proven on 2026-10-09 (`DIWAI-CR-2026-10-11`, finding 7); it is now verified hourly and by control-health check 15. The VM-to-Mac key-only exemption for two production jobs is recorded in `DIWAI-CR-2026-08-17` §3.2. **SPRS deficit: none.** |
| 3.7.6       | Supervise maintenance      | IMPLEMENTED | Single-operator system. All maintenance actions logged via auditd + Wazuh.                                                                                                                                                                                                                                                                                                                                                                                                                |

### 4.8 Media Protection (MP)

**Status:** All MP controls **IMPLEMENTED**.

- Storage encrypted: LUKS AES-256-XTS (VM); FileVault / Apple Secure Enclave (Mac host) — covers the Nextcloud CUI/FCI data directory (`/opt/local/nextcloud/data`) at rest
- Removable media: USBGuard on the VM; custom USB Guard on the Mac host
- Media disposal: DIWAI-PE-MP-001 §4.5 (cryptographic erase / shred)
- Media transport: all CUI transmitted via encrypted channels (TLS/SSH)
- **CUI marking is applied in advance (owner determination 2026-10-03).** Documents on this system that carry a CUI marking or a `CUI_` filename prefix are company-proprietary information of [SYSTEM-OWNER] LLC while they are held here. They become CUI only when held by the U.S. Government. They are marked ahead of time because they may be shared with a Government or third-party assessor, and marking them at creation avoids a later marking step that could be missed. Consequently, `CUI_`-marked files in the local AI knowledge base (Open Web UI collections and the DIWAI document library, both loopback-only on the Mac host) are **not** a CUI-handling violation: the local AI reading them is reading proprietary company information. This is consistent with the Distribution Notice at the head of this plan.

### 4.9 Personnel Security (PS)

**Status:** 3.9.2 **IMPLEMENTED** (procedure exercised, scope below). 3.9.1 **IMPLEMENTED as interpreted** (sole-owner basis; no investigation claimed).

- 3.9.1: The sole user is the system owner. By owner decision of 2026-10-23 (`DIWAI-CR-2026-10-27`, `DIWAI-APP-001` v1.1, `DIWAI-PS-001` sole-owner paragraph), the owner is not screened by a third party; his access rests on ownership and control of the company, a signed attestation of eligibility, and his Joint Certification Program certification (DD Form 2345, cited by existence and expiry only; expires 2026-11-09). **Every other person is screened in full before access.** The attestation (`DIWAI-EV-PS-2026-10-23-S`) was signed 2026-10-23 and is filed in `Compliance/Evidence/Personnel/`; the objective-level determination is satisfied as interpreted. [PERSONNEL-SCREENING-NOTE-REDACTED]
- 3.9.2: `DIWAI-PS-001` documents the termination (PS-4) and transfer (PS-5) procedures. The termination procedure was exercised on 2026-10-23 on a disposable account (`DIWAI-EV-PS-2026-10-23`): access to the directory and the VM ended within 1 second of the lock, refusals were enforced by the systems, and later attempts were logged. The same drill on a Mac local account refused the correct password after the lock (positive control passed, 0 seconds). A second drill with a positive control (`DIWAI-EV-PS-2026-10-23-N`) found that locking the directory entry did **not** stop a Nextcloud app password; it was refused only after `occ user:disable`, so PS-4 now includes the Nextcloud step (`DIWAI-CR-2026-10-31`). The browser login with two-factor was not exercised. Transfers do not apply to a single-owner system.

### 4.10 Physical Protection (PE)

**Status:** All PE controls **IMPLEMENTED**. Evidenced 2026-08-02 —
`DIWAI-EV-PE-2026-08-02`.

**Facility characterisation.** The facility is a **private residence** in
[LOCATION-REDACTED]. CUI processing occurs in a dedicated home office within
that residence. This is stated explicitly because earlier revisions of this plan
described only "a secured home-office facility with controlled access," which
invites the reader to assume a commercial or controlled space. It is not one.
The controls below are assessed against what the facility actually is.

**Layered controls, outermost to innermost:**

| \# | Layer              | Control                                                                                                                                                                                                                |
|:--|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Property perimeter | **Nine wired cameras**, 360° coverage (Front Gate, Street View, Front Door, Courtyard, Garage, Back Yard, Back North, Back South, side). Wired, not Wi-Fi — no dependence on the wireless interface addressed by POA&M-024 |
| 2 | Residence          | **Professionally monitored intrusion alarm** (DSC panel; third-party monitoring service). Burglar, fire and perimeter zones                                                                                                |
| 3 | Room               | Dedicated home office, **separate room with doors that close** for privacy and security during work sessions                                                                                                               |
| 4 | **Rack**               | Enclosed rack, mesh front door with swing-handle lock, **habitually kept locked**                                                                                                                                          |
| 5 | Host               | **Mac mini inside the locked cabinet on a repurposed shelf** — corrected 2026-09-15 (**F-2026-09-01**); the 2U tray was repurposed. Access to ports and the power button is restricted by the locked cabinet (layer 4), not by the mounting |
| 6 | Data at rest       | FileVault (host and backup USB), LUKS (VM image), USBGuard                                                                                                                                                             |

> **Correction 2026-09-15 (F-2026-09-01).** Layer 5 previously read "Mac mini
> rack-mounted in a 2U tray". The tray was repurposed and the host now rests on a
> shelf within the same locked cabinet. **No security effect** — the enforcing
> control is layer 4 — but the evidence photograph `CUI_PE_03_macmini_rackmount.png`
> depicts the superseded mounting. See `CUI_EV_PE_Physical_Protection_2026-08-02.md`
> §4.6. **Nothing in this system verifies physical configuration against this plan**;
> this was found only because the owner said so.

**The rack lock is the enforcing control.** Layers 1–3 protect the residence;
layer 4 is the only layer that excludes people otherwise legitimately inside the
building — household members, guests, a repair visitor. This distinction is what
makes the 3.10.1 claim defensible rather than aspirational.

**3.10.2 (protect *and monitor*)** is satisfied by third-party alarm monitoring
in addition to camera coverage — monitoring is not performed solely by the system
owner, which is the element small facilities most commonly lack.

**3.10.3 / 3.10.4.** Very few outsiders visit the physical office; those who do
are logged and remain in the owner's presence. There is no unescorted access.
Physical access is recorded by three independent mechanisms: camera recording,
alarm arm/disarm history held by the monitoring service, and the visitor log.

**Alarm posture during working hours.** The alarm is normally **disarmed while
the premises are occupied**. Working hours are therefore covered by owner
presence, the closable office door and the locked rack rather than by the alarm.
This is recorded so the alarm is not over-claimed as a continuous control.

**Open items** (see `DIWAI-EV-PE-2026-08-02` §4–§5, tracked as POA&M-039): camera
timestamp inconsistency across the NVR and against the alarm panel; camera
retention period unestablished; no written physical access device inventory; NVR
network placement and client-software location unconfirmed.

**Physical co-location:** The rack also contains CyberInABox (Reference System #1) components. As noted in §3.3, the two systems remain architecturally and logically independent, standalone systems with no shared policy set. PE controls — PE-2 (Physical Access Controls), PE-3 (Physical Access), PE-11 (Emergency Power) — for the [DOMAIN.ORG] system are documented independently in DIWAI-PE-MP-001.

**Note:** Physical co-location does not create a logical or network interconnection. The two systems remain fully independent (see 2.5–2.6).

### 4.11 Risk Assessment (RA)

| Control | Name                      | Status      | Implementation                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------|:--------------------------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.11.1  | Periodic risk assessment  | **NOT MET**     | DIWAI-RA-001 (Risk Management Policy) is approved with NIST SP 800-30 methodology. The first formal [DOMAIN.ORG]-specific risk assessment has not been conducted. **Target: overdue. SPRS deficit: -3 points.** POA&M-005.                                                                                                                                                                                                                     |
| 3.11.2  | Vulnerability scanning    | IMPLEMENTED | Wazuh vulnerability detection module (continuous, 60-minute feed updates). OpenSCAP CUI weekly automated scan on the VM. mSCP weekly automated scan on the Mac host.                                                                                                                                                                                                                                                                    |
| 3.11.3  | Remediate vulnerabilities | IMPLEMENTED | Remediation is **operator-applied at the monthly review** (`DIWAI-PR-001`, log `DIWAI-PR-LOG`) — `dnf-automatic` is **download-only** and applies nothing. Timeframes: CRITICAL PATCH-class within **72 h**, IMPORTANT within **7 days** (`DIWAI-PR-001 §6`; Appendix E.3). Identification by `diwai-cve-scan`/`-mac` and Wazuh; the scan report distinguishes **actionable PATCH-class** findings from NO-CODE, STREAM-MIGRATION and THIRD-PARTY (`DIWAI-CR-2026-08-21`). |

### 4.12 Security Assessment (CA)

**Status:** All CA controls **IMPLEMENTED**.

- **3.12.1:** Tailored OpenSCAP CUI profile, automated weekly scans on the VM (**101/101**). mSCP automated weekly scans on the Mac host (**134/136**) — the scan was found non-functional and restored 2026-08-01 (POA&M-015); it remains **un-invocable on demand** (POA&M-038). CVE-level scanning added on the VM 2026-08-02 (`diwai-cve-scan`, weekly — POA&M-022); the Mac host still has none. Results published to the compliance dashboard at securemac.[DOMAIN.ORG].
- **3.12.2:** The [DOMAIN.ORG] POA&M documents all deficiencies with remediation plans and target dates.
- **3.12.3:** Wazuh provides continuous security monitoring; Suricata provides continuous network monitoring. Weekly compliance scans supplement automated monitoring.
- **3.12.4:** This SSP constitutes the system security plan per 3.12.4.

### 4.13 System and Communications Protection (SC)

**Status:** All SC controls **IMPLEMENTED**.

- **3.13.1 (SC-7):** The pf firewall (Mac host) provides boundary protection between WAN, LAN, and MGMT interfaces. firewalld provides host-level boundary protection on the VM. Suricata provides network IDS/IPS on the VM.
- **3.13.5:** The LAN ([LAN-IP-REDACTED]/24) is segregated from the WAN by pf. The VM and NAS are not directly reachable from the WAN. nginx is the sole WAN-accessible endpoint for internal services (and even it listens only on the LAN interface and loopback).
- **3.13.6:** pf implements default-deny inbound on the WAN. firewalld implements default-deny on the VM.
- **3.13.8 (SC-8):** All data in transit is protected by TLS 1.2/1.3 or SSH. nginx enforces HSTS on both ai.[DOMAIN.ORG] and cloud.[DOMAIN.ORG] (Nextcloud). FIPS-approved cipher suites are enforced on the VM. Nextcloud↔389-DS identity traffic uses LDAPS (port 636); the Nextcloud↔Collabora editing hop stays on host loopback and never independently terminates TLS, so the nginx reverse proxy remains the sole CUI-bearing TLS boundary.
- **3.13.10:** 389-DS provides PKI and key management for identity credentials. The Apple Secure Enclave manages cryptographic keys on the Mac host.
- **3.13.11 (SC-13):** FIPS 140-2 mode is enabled on the Rocky Linux 9.7 VM (verified via `fips-mode-setup --check`). The Apple Secure Enclave (FIPS 140-2 Level 1) protects the Mac host.
- **3.13.16:** TLS encryption is enforced on all CUI transmission paths.

**Note — FIPS boundary at the NAS:** Data leaving the FIPS boundary (VM → NAS) is pre-encrypted using FIPS-validated OpenSSL (AES-256-CBC + PBKDF2/SHA-256), then transferred over SSH (AES-256-CTR). The NAS applies a second AES-256/SHA-256 encryption layer (not FIPS 140-2 validated). The FIPS artifact is the encrypted `.enc` file produced inside the boundary — the NAS layer is defense-in-depth, not a FIPS claim. The NAS is classified as supporting infrastructure within the physical security boundary, not as part of the cryptographic (FIPS) boundary.

### 4.14 System and Information Integrity (SI)

| Control | Name                                    | Status                | Implementation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:--------|:----------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3.14.1  | Flaw remediation                        | **PARTIALLY IMPLEMENTED** | **Identify:** `diwai-cve-scan` (VM, weekly) and `diwai-cve-scan-mac` (host), Wazuh vulnerability detection with CVE correlation, OpenSCAP/mSCP baselines. **Report:** `DIWAI-PR-LOG` and `diwai-control-health` (state-change alerting, `DIWAI-CR-2026-08-20`). **Correct:** monthly review under `DIWAI-PR-001`; `dnf-automatic` is **download-only** and applies nothing (Appendix E.3). Evidence of adherence: two reviews logged 2026-08-02/-03, ~40 CVEs closed on the host, and the deferred VM kernel now **running 5.14.0-687.33.1** with no reboot pending. **Residual:** `wazuh-manager` **is version-pinned at 4.14.6 and receives no security updates — POA&M-051.** That is an uncorrected flaw in a security control, and it is why this requirement is not scored as met. |
| 3.14.2  | Malware protection                      | **IMPLEMENTED**           | **Verified end to end 2026-09-13 on both hosts:** EICAR → FIM 554 → YARA `SUSP_Just_EICAR` → Wazuh alert 100200; VM in 2 s, Mac on the hourly scheduled scan. Before that date the Wazuh YARA rules had never loaded, so no YARA detection had ever alerted (`DIWAI-CR-2026-09-06`; POA&M-075 closed). **Mac host:** XProtect + MRT + Gatekeeper (Apple native, always active, auto-updated). **VM:** **YARA 4.5.2** (5,972 rules) provides malicious-code scanning — run by Wazuh active-response on FIM rules 550/554 (new/modified files) and by a **weekly full-system scan** (`yara-fullscan.timer`). Corroborated by **VirusTotal** reputation lookups and layered with **fapolicyd** application allow-listing, **SELinux** enforcing, and **Suricata** network IDS — all FIPS-native. *(ClamAV was decommissioned 06/12/2026 — non-functional under FIPS; see DIWAI-EV-SI3-002, superseding RISK-2026-004.)* **POA&M-002 CLOSED — resolved by control substitution. SPRS deficit: 0.**                                                                                             |
| 3.14.3  | Security alerts, advisories, directives | IMPLEMENTED           | Wazuh alerts and Suricata IDS signatures auto-update. OS security advisories are **ingested and reported** by `diwai-cve-scan` against Rocky errata (`dnf-automatic` downloads but **applies nothing**); advisories requiring action are dispositioned at the monthly review. Third-party advisories outside Rocky errata (Remi PHP) are flagged as THIRD-PARTY and tracked under POA&M-041.                                                                                                                                                                                                                                                                                                                                                             |
| 3.14.4  | Update malicious code protection        | IMPLEMENTED           | YARA rulesets are refreshed nightly (verified: 9 updates, 80 already-current runs since 2026-04-20). Suricata rules were **not** updating from 2026-04-20 to 2026-10-23 (cron could not find the command; then a rule-load failure) — repaired 2026-10-23, `DIWAI-CR-2026-10-28`, first scheduled run due 2026-10-24 03:15. XProtect is auto-updated by Apple.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 3.14.5  | Periodic/real-time scans                | IMPLEMENTED           | Wazuh FIM operates in real time on critical paths. OpenSCAP and mSCP scan weekly. Suricata performs real-time network scanning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 3.14.6  | Monitor for anomalous activity          | IMPLEMENTED           | Wazuh behavioral analytics + Suricata network IDS detect failed logins, USB policy violations, and anomalous traffic patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 3.14.7  | Identify unauthorized use               | IMPLEMENTED           | Wazuh + Suricata correlation; auditd system-call auditing. (Grafana decommissioned 2026-08-02, `DIWAI-CR-2026-08-04`; it visualized anomalies but detected none — identification rests on Wazuh correlation, Suricata, and auditd, all unchanged.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

## 5. CONTINGENCY PLANNING (CP)

### CP-9 (System Backup)

**Status:** IMPLEMENTED

**Mac Host (securemac.[DOMAIN.ORG]):**

- Time Machine backup to dedicated encrypted SSD (partition UUID: [HW-UUID-REDACTED]; replacement drive, first backup 2026-10-18 10:47)
- LaunchAgent (`org.diwai.mount-tm-drive`) ensures the SSD auto-mounts at login
- RPO: continuous (Time Machine hourly snapshots)

**VM (services.[DOMAIN.ORG]):**

- Wazuh alert archives: daily encrypted push to the NAS (nas.[DOMAIN.ORG])
- Archives encrypted via FIPS-validated OpenSSL before transfer
- VM configuration: documented and reproducible via UTM snapshot + kickstart

**NAS (nas.[DOMAIN.ORG]):**

- Primary long-term archive target for encrypted log data (DataStore share)
- Synology folder-level encryption (AES-256/SHA-256) as a second layer

### CP-10 (System Recovery)

**Status:** IMPLEMENTED

- Mac host: Time Machine full-system restore + macOS bootable installer
- VM: UTM snapshot restore, or rebuild from the Rocky Linux 9.7 FIPS kickstart
- RTO: < 4 hours; RPO: < 24 hours

---

## 6. SECURITY POLICIES AND PROCEDURES

All policies below apply to the [DOMAIN.ORG] SecureMac Reference System as part of the single-operator organization [SYSTEM-OWNER] LLC. The same policy set covers both CyberInABox and [DOMAIN.ORG] as **organizational common controls** (not system-specific) — see 2.6 and 4.10.

| Policy                                      | Document ID          | Effective Date                                                                                                                                                                                                                                    |
|:--------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Incident Response Policy and Procedures     | DIWAI-IRP-001        | 11/02/2025                                                                                                                                                                                                                                        |
| Risk Management Policy                      | DIWAI-RA-001         | 11/02/2025                                                                                                                                                                                                                                        |
| Personnel Security Policy                   | DIWAI-PS-001         | 11/02/2025                                                                                                                                                                                                                                        |
| Physical and Media Protection Policy        | DIWAI-PE-MP-001      | 11/02/2025                                                                                                                                                                                                                                        |
| System and Information Integrity Policy     | DIWAI-SI-001         | 11/02/2025                                                                                                                                                                                                                                        |
| Acceptable Use Policy                       | DIWAI-AUP-001        | 11/02/2025                                                                                                                                                                                                                                        |
| Audit and Accountability Policy             | DIWAI-AAP-001        | 02/15/2026                                                                                                                                                                                                                                        |
| Configuration Management Policy             | DIWAI-CMP-001        | 02/15/2026                                                                                                                                                                                                                                        |
| Security Awareness and Training Policy      | DIWAI-ATP-001        | 02/15/2026                                                                                                                                                                                                                                        |
| **Identification and Authentication Policy**    | **DIWAI-IAP-001 — v1.1** | **02/15/2026 (orig. v1.0); v1.1 effective 06/06/2026 — unified TOTP MFA strategy** *(both dates verified against the policy document 2026-08-02; the v1.0 date previously stated 04/10/2026 and the v1.1 date 06/11/2026 — neither matched the policy)* |
| System and Communications Protection Policy | DIWAI-SCP-001        | 02/15/2026                                                                                                                                                                                                                                        |

---

## 10. PLAN OF ACTION AND MILESTONES (POA&M)

The complete [DOMAIN.ORG] POA&M is maintained as a standalone document and **that document is the single source of truth**: `CUI_[DOMAIN.ORG]_Unified_POAM_v1.32.md` (2026-09-13, in `Compliance/POAM/`; see Appendix D, "Companion Documents").

> **This section no longer embeds a copy of the register (changed in v2.18).**
> It previously carried a summary table described as "kept in sync with the
> standalone document." It was not kept in sync: the table was frozen at
> **2026-06-06** and listed only POA&M-001 through -010, while the register had
> advanced to POA&M-073. A reader comparing the two documents would have found
> two different answers to the same question, with this one asserting its own
> currency. **Duplicating a register inside the document that cites it is the
> mechanism by which the two drift**, so the copy has been removed rather than
> refreshed. Per-item detail, milestones, status and history live in the
> standalone POA&M.

### POA&M Status Summary (as of 2026-08-12)

Counts only. **Per-item detail is deliberately not reproduced here** — see
`CUI_[DOMAIN.ORG]_Unified_POAM_v1.32.md`.

| Measure          |                 Value |
|:-----------------|----------------------:|
| Tracked items    |                    **63** |
| Identifier range | POA&M-001 – POA&M-073 |
| Closed           |                    **39** |
| Open             |                    **24** |

Identifiers are not contiguous: some numbers were issued and later merged or
withdrawn, so the highest identifier (073) exceeds the item count (63).

**Current SPRS:** **101/110** — evidence-strict, 2026-10-22 (see §11); 3.5.6 awarded 2026-10-22 (POA&M-076). 3.14.2 is scored **MET** (POA&M-002 closed). Its YARA alert path, which had never fired, was repaired and **proven on both hosts 2026-09-13** (`DIWAI-CR-2026-09-06`; POA&M-075 closed).\

> **RESOLVED 2026-09-13 — the discrepancy this block recorded is closed.** The two
> blockers it named are both removed: the **owner determination** was made on
> 2026-09-13, and the **`DIWAI-VS-001` §4 dispute** is settled. The figure of record
> is **93/110**, applying the owner's standing rule that a disputed value is reported
> at the lower, more conservative reading. This SSP previously stated **87/110** — the
> 2026-08-03 recompute — in five live locations while the POA&M had moved on through
> **3.7.5 recovered (+5,** `DIWAI-CR-2026-08-18`**)** and **3.5.3 reduced (+2)** on
> 2026-08-07, reaching 94 by arithmetic; the determination withholds one further point.
> Those locations are corrected in this revision. The prior reasoning is retained in
> the revision history rather than deleted. Companion register:
> `CUI_[DOMAIN.ORG]_Unified_POAM_v1.32.md`.
>
> **RE-DETERMINED LATER 2026-09-13 — the figure of record is 94/110.** The withheld point
> rested on the credential policies being configured but not demonstrated. Negative tests
> the same day found two of them **not enforced** — the Mac password-history rule was
> malformed and silently skipped, and the 389-DS minimum length was disabled by
> `passwordCheckSyntax: off` — repaired both in session, and then proved 3.1.8, 3.5.7 and
> 3.5.8 **by refusal on both hosts** (`DIWAI-CR-2026-09-03`). With nothing left in dispute,
> the owner re-determined the score at the arithmetic figure, 110 − 16 = **94/110**.
>
> **RECOMPUTED LATER 2026-09-13 — 101/110.** Three recoveries, each proven by test before it was
> claimed: **3.14.1 +5** (Wazuh manager unpinned and upgraded, POA&M-051 closed, `DIWAI-CR-2026-09-04`);
> **3.3.4 +1** (Mac audit-failure warning received in the owner's inbox, `DIWAI-CR-2026-09-07`);
> **3.10.3 +1** (visitor nil attestation, `DIWAI-PE-LOG-001` §6). Open deductions −9: 3.5.3 −3,
> 3.13.5 −5, 3.10.4 −1 (withheld by owner decision). Companion register: POA&M v1.32 (amended 2).
>
> **WITHHELD THE SAME DAY — 100/110.** The evidence-strict basis was then applied to 3.5.6. Appendix E.4
> defines a 90-day inactivity disable, but testing found **no enforcement**: the 389-DS Account Policy plugin is
> off, and neither the VM's local accounts nor the Mac have an inactivity mechanism. A defined but unenforced
> control earns no point. Open deductions −10. **POA&M-076.**

---

## 11. IMPLEMENTATION METRICS

### SPRS Score Breakdown

#### Scoring basis and evidence standard — owner determination 2026-09-13

**The SPRS figure is scored on an evidence-strict basis.** A requirement earns its points only when
the security capability is implemented **and shown to work by evidence** — including a negative test
(a refusal, a lockout, an alert that arrives) wherever a positive observation could have been produced
by a broken system. The standard is the one adopted by `DIWAI-VS-001` (2026-08-07):

> *What evidence closed this, and could that evidence have been produced by a broken system?*

Configuration read-back, a document's existence, or a component's own success message is **not**
evidence under this standard. A point claimed on such a basis is withheld until tested.

**Two figures, deliberately reported side by side:**

| Figure | Basis | Current |
|:---|:---|---:|
| **SPRS score** | Evidence-strict capability: implemented **and** proven working (DoD Assessment Methodology weights) | **101/110** |
| **Strict 800-171A objectives met** | Every assessment objective satisfied **or not applicable**, **including definition and documentation** (Control Family Status table below) | **99/110** |

They measure different properties and are not in conflict. The gap between them is **working controls
that are not yet fully defined, enumerated or documented** — tracked under **POA&M-027** — and is the
exposure in any Medium or High assessment, where objectives are tested as written. Closing that
documentation gap raises the second figure without changing the system's security.

**Score: 101/110** (evidence-strict, 2026-10-22 — open deductions below; recomputed 2026-08-03; was 56/110). Weights **verified 2026-08-02** against the *NIST SP 800-171
DoD Assessment Methodology, Version 1.2.1 (24 June 2020)*, Annex A and §(d).

> **The 98/110 published in v2.11–v2.14 was never correct.** Two errors
> compounded: **3.7.5 was weighted −3 when the methodology assigns it −5**, and
> the **11 points for POA&M-008 were acknowledged as pending but never
> subtracted**. The corrected June 2026 baseline was **85/110**.

| Score as of 2026-08-02 (historical)                | Score |
|:---------------------------------------------------|------:|
| Corrected June 2026 baseline                       |    **85** |
| Deficiencies found by the 2026-08 assessment       |   **−29** |
| Points recovered by remediation applied 2026-08-01 |   **+13** |
| **At 2026-08-02 (historical)**                                            |    **56** |
| Had no remediation been applied                    |    43 |

**Score history of record:**

| Date | Score | Change | Basis |
|:---|---:|---:|:---|
| 2026-08-02 | 56 | — | Weights verified; baseline 85 (SSP amendment 2.15, corrected) |
| 2026-08-03 | 87 | +31 | Eight requirements recovered on evidence of 2026-08-03 (SSP amendment 2.16) |
| 2026-09-13 | 93 | +6 | Owner determination at the lower value: register 94 less one point withheld pending negative tests |
| 2026-09-13 | 94 | +1 | Negative tests on both hosts (`DIWAI-CR-2026-09-03`) |
| 2026-09-13 | 101 | +7 | 3.14.1 +5, 3.3.4 +1, 3.10.3 +1 |
| 2026-09-13 | **100** | −1 | 3.5.6 withheld, defined but not enforced (POA&M-076) |
| 2026-10-09 | **100** | 0 | No change (`DIWAI-CR-2026-10-11`; documentation corrections only) |
| 2026-10-22 | **101** | +1 | 3.5.6 awarded on owner decision: enforced on the directory, the Mac and the VM's local accounts, proven, first scheduled runs observed 10-20 to 10-22 (`DIWAI-CR-2026-10-17`, `-10-18`; POA&M-076) |


#### Open deductions (−9)

*Rebuilt 2026-10-09 to the 100/110 determination and updated 2026-10-22 (3.5.6 awarded, now 101/110). The rows below are the only open deductions; every other row of the 2026-08 table is kept under "Recovered" with the date and evidence of its recovery. No weight and no determination is changed.*

| Req    | Weight | Deficiency                                                                                                                                                                                                                                                            | POA&M          |
|:-------|-------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| 3.5.3  |     −3 | **Partial credit (was −5; +2 recorded before 2026-09-13).** MFA is not implemented for every user: the methodology's −3 applies where it covers remote and privileged users only (see the 3.5.3 row and Partial-credit requirements below) | 004/007        |
| 3.13.5 |     −5 | Internet-published services share a host with the CUI data tier                                                                                                                                                                                                       | 023            |
| 3.10.4 |     −1 | **Remains −1 — owner decision 2026-09-13: rack openings not logged during development.** No physical access log (as above)                                                                                                                                                                                                                                     | 027            |

#### Deductions recovered since the 2026-08 assessment (+46)

*44 points on the rows below, plus the 2 points of 3.5.3 partial credit; 55 gross (54 in the 2026-08 table plus the 1 point withheld for 3.5.6) − 9 open = 46 recovered.*

| Req    | Weight | Deficiency                                                                                                                                                                                                                                                            | POA&M          |
|:-------|-------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| 3.7.5  |     −5 | **RECOVERED — `DIWAI-CR-2026-08-18` (+5), recorded in the register before 2026-09-13.** No MFA for nonlocal maintenance | 004/007        |
| 3.5.6  |     −1 | **RECOVERED 2026-10-22 — owner decision.** Withheld 2026-09-13 (defined, not enforced). Directory (`DIWAI-CR-2026-09-08`), Mac (`DIWAI-CR-2026-10-17`) and VM local accounts (`DIWAI-CR-2026-10-18`) enforced by daily jobs, proven by refusal on disposable accounts; first scheduled runs observed 2026-10-20 to -22. No real account has yet aged out; never-logged-in directory entries not yet covered | 076            |
| 3.2.1  |     −5 | **RECOVERED 2026-08-03 — POA&M-008 closed (DoD IF141.16 certificate; `DIWAI-PAF-001`, `DIWAI-TRR-001`, `DIWAI-RAM-001`, `DIWAI-CRC-001` signed).** Security awareness — no delivery/completion records | 008            |
| 3.2.2  |     −5 | **RECOVERED 2026-08-03 — POA&M-008 closed (as 3.2.1).** Role-based training — no records | 008            |
| 3.2.3  |     −1 | **RECOVERED 2026-08-03 — POA&M-008 closed (as 3.2.1).** Insider-threat awareness not provided | 008            |
| 3.5.10 |     −5 | **RECOVERED 2026-08-03 — `nsslapd-require-secure-binds: on` (`DIWAI-CR-2026-08-10`).** NAS binds the directory in cleartext as `cn=Directory Manager` | 020/021        |
| 3.11.2 |     −5 | **RECOVERED 2026-08-03 — CVE scanning operational (`diwai-cve-scan`, last run 08-03 07:47).** No CVE-level vulnerability scanning | 022            |
| 3.1.16 |     −5 | **RECOVERED 2026-08-03 — wireless powered off, pf-enforced, verified live.** Wireless active but not authorised in this plan | 024            |
| 3.14.1 |     −5 | **RECOVERED 2026-09-13 — POA&M-051 closed, manager on 4.14.7 (`DIWAI-CR-2026-09-04`).** **Adherence is now evidenced (POA&M-025 closed 2026-08-07)** — cadence defined *and operating*, deviation tailored with justification, deferred kernel discharged. **The deduction now rests solely on POA&M-051:** `wazuh-manager` pinned at 4.14.6 receives no security updates | **051**            |
| 3.11.1 |     −3 | **RECOVERED 2026-08-03 — POA&M-005 closed; `DIWAI-RAR-001` v1.1 accepted and signed.** No risk assessment conducted | 005            |
| 3.6.3  |     −1 | **RECOVERED 2026-08-03 — tabletop `DIWAI-IR-TTX-001` conducted and signed; POA&M-006 closed.** IR capability never tested | 006            |
| 3.3.4  |     −1 | **RECOVERED 2026-09-13 — alert proven to the owner's inbox (`DIWAI-CR-2026-09-07`).** No alert on audit-logging failure (`audit_settings_failure_notify` fails)                                                                                                                                                                                               | 029            |
| 3.3.7  |     −1 | **RECOVERED — POA&M-010 closed on an observed episode 2026-08-08 (POA&M v1.30); no score movement at that date.** Clock synchronisation not durable | 010 (reopened) |
| 3.10.3 |     −1 | **RECOVERED 2026-09-13 — visitor nil attestation (`DIWAI-PE-LOG-001` §6).** No visitor log (procedure defined v2.15, not yet operating)                                                                                                                                                                                                           | 027            |

#### Recovered by remediation, 2026-08-01 (+13)

| Req    | Weight | Fix                                                          |
|:-------|-------:|:-------------------------------------------------------------|
| 3.3.1  |     +5 | Audit retention raised from ~1 hour to ~6.4 GB               |
| 3.12.3 |     +5 | Control-health check deployed — the single highest-value fix |
| 3.1.8  |     +1 | Account lockout enabled                                      |
| 3.5.7  |     +1 | Password minimum raised from 4 to 12 characters              |
| 3.5.8  |     +1 | Password history enabled                                     |

#### Partial-credit requirements

The methodology allows two requirements to score partially:

- **3.5.3 (MFA)** — −3 if implemented for remote and privileged users only; **−5 if not implemented for any users**. Currently **−3** (the 2 points for remote and privileged coverage were recorded before 2026-09-13). Extending MFA to every user, including local console logon, would recover the remaining 3.
- **3.13.11 (FIPS)** — −3 if encryption is employed but not FIPS-validated; −5 if none. FIPS-validated encryption **is** in use throughout, so this scores **0**.

#### Methodology note

The DoD methodology states that an assessment **cannot be conducted** where the
system security plan does not describe how each requirement is met — the absence
of such a plan yields a finding that the assessment could not be completed.
Accuracy of this document is therefore a scoring prerequisite rather than a
presentational concern, which is the principal argument for **POA&M-027**.

### Control Family Status

**Replaced in v2.15.** The previous table asserted whole families fully
implemented (AU 9/9, CM 9/9, MP 9/9, PE 6/6, SC 16/16, SI 7/7). Objective-level
assessment does not support that. Figures below are derived from
`CUI_800-171A_Self_Assessment_2026-08.md`, where a requirement counts as **Met**
only when **every** assessment objective is satisfied.

| Family                                  | Total | Met | Not Met | Unverified |
|:----------------------------------------|------:|----:|--------:|-----------:|
| AC — Access Control                     |    22 |  20 |       2 |          0 |
| AT — Awareness & Training               |     3 |   3 |       0 |          0 |
| AU — Audit & Accountability             |     9 |   9 |       0 |          0 |
| CM — Configuration Management           |     9 |   9 |       0 |          0 |
| IA — Identification & Authentication    |    11 |   9 |       2 |          0 |
| IR — Incident Response                  |     3 |   3 |       0 |          0 |
| MA — Maintenance                        |     6 |   6 |       0 |          0 |
| MP — Media Protection                   |     9 |   8 |       1 |          0 |
| PS — Personnel Security                 |     2 |   2 |       0 |          0 |
| PE — Physical Protection                |     6 |   4 |       2 |          0 |
| RA — Risk Assessment                    |     3 |   3 |       0 |          0 |
| CA — Security Assessment                |     4 |   3 |       1 |          0 |
| SC — System & Communications Protection |    16 |  13 |       3 |          0 |
| SI — System & Information Integrity     |     7 |   7 |       0 |          0 |
| **TOTAL**                                   |   **110** |  **99** |      **11** |          **0** |

**Revised 2026-10-23 (assessment revision 1.20): 78 → 81.** Access Control 13 → 16 of 22: **3.1.5, 3.1.8 and 3.1.10** re-determined on current evidence. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.19): 77 → 78.** Audit and Accountability 8 → 9 of 9: **3.3.1** recovered on the Mac audit retention change. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.18): 76 → 77.** Audit and Accountability 7 → 8 of 9: **3.3.2** recovered. The services that used the owner's directory account as their bind now have their own read-only accounts. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.17): 75 → 76.** Audit and Accountability 6 → 7 of 9: **3.3.5** recovered on the correlation procedure and an exercise across sources. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.16): 74 → 75.** Media Protection 6 → 7 of 9: **3.8.3** recovered on the rewritten procedure, the opened log and an exercise with positive controls. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.15): 73 → 74.** Maintenance 5 → 6 of 6: **3.7.2** recovered on `DIWAI-MNT-001`. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.14): 72 → 73.** Maintenance 4 → 5 of 6: **3.7.3** not applicable on the owner's statement that no equipment leaves for off-site maintenance. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.13): 70 → 72.** Maintenance 3 → 4 of 6 (**3.7.5**) and Audit and Accountability 5 → 6 of 9 (**3.3.7**), both on current evidence. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.12): 68 → 70.** Configuration Management 5 → 7 of 9. **3.4.3** recovered (POA&M-048 closed on the owner's acceptance of the publish gate) and **3.4.5** recovered (`DIWAI-CMA-001`). SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.11): 67 → 68.** Personnel Security 1 → 2 of 2. **3.9.2** recovered on the Nextcloud lockout drill, which also found and closed a gap in the termination procedure. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.10): 66 → 67.** Security Assessment 2 → 3 of 4. **3.12.2** recovered: four overdue POA&M items fixed and verified and seven re-dated with reasons on the owner's approval (`DIWAI-CR-2026-10-29`). Re-dating is plan management, not remediation. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.9): 65 → 66.** Incident Response 1 → 2 of 3. **3.6.2** recovered: the Incident Register `DIWAI-INCREG-001` v1.0 was issued and approved by the owner; INC-003 to INC-007 are reconstructed and say so. 3.6.1 stays partial (detection). SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.8): 64 → 65.** Personnel Security 0 → 1 of 2. **3.9.1** recovered, as interpreted: the owner's approved sole-owner screening basis (`DIWAI-CR-2026-10-27`, `DIWAI-APP-001` v1.1) with the attestation of eligibility signed and filed (`DIWAI-EV-PS-2026-10-23-S`). A tailoring decision, not an investigation; any other person is screened in full before access. SPRS unchanged (101/110).

**Revised 2026-10-23 (assessment revision 1.7): 55 → 64.** The definitions approved by the owner on 2026-10-23 were written (Appendix E.9 to E.14), the first audit-event review was run, and the VM password settings were hardened and proven. **Now met:** 3.1.2, 3.1.12, 3.1.15, 3.1.16, 3.3.3, 3.3.9, 3.4.4, 3.5.8 and 3.7.4. Moved without recovery: 3.3.1 (Mac keeps its audit trail only 7 days), 3.13.2 (publication tier not separated), 3.8.5 (no custody record produced yet).

**Revised 2026-10-23 (assessment revision 1.6): 52 → 55.** Identification and Authentication re-walked: **3.5.1, 3.5.2 and 3.5.5** are now met (IA 2 → 5 of 11); 3.5.3, 3.5.7, 3.5.8 and 3.5.9 moved up without recovering, each with a stated reason and a "what it takes" line in the assessment.

**Revised 2026-10-23 (assessment revision 1.5): 48 → 52.** The full re-walk began with System and Information Integrity: **3.14.1, 3.14.3, 3.14.6 and 3.14.7** are now met (SI 2 → 6 of 7). The August determinations were stale: Appendix E.3 now defines the flaw timeframes (and now states a reporting time), vendor advisories are ingested automatically, the monitor detects a stopped SIEM or IDS, and `DIWAI-AUP-001` defines authorized use. Only **3.14.4** (evidence that the YARA and Suricata rules update) stays open.

**Revised 2026-10-23 (assessment revision 1.4): 47 → 48.** **3.11.2** is now met: `DIWAI-PR-001` v1.4 §6.2 defines the trigger (scan on demand when a new vulnerability is reported) and it was exercised the same day, finding and closing a real critical (`DIWAI-PR-LOG`). Risk Assessment is now 3 of 3.

**Revised 2026-10-23 (assessment revision 1.3): 45 → 47.** Two requirements, **3.1.18** and **3.1.19** (mobile devices), are **not applicable** on the written applicability statement `DIWAI-APP-001`; no security change. AC is now 9 of 22.

**Revised 2026-10-23 (assessment revision 1.2): 42 → 45.** Three requirements re-determined on evidence verified that day (Tier A of `DIWAI-ORW-001`): **3.4.9** (the unattended-install basis is closed: update application is operator-run), **3.11.1** (risk assessment conducted 2026-08-02, accepted and signed 2026-08-03, annual) and **3.11.3** (remediation tied to severity and the risk register, operating). Objectives moved without a recovery: **3.4.3** [b][c], **3.5.6** [a][b], **3.11.2** [b][c], **3.12.3** [a], **3.13.1** [a]. Eight Tier A requirements were **not** recovered, each for a stated reason (assessment §0 and the notes under each requirement); in particular 11 open POA&M items are past their "Q3 2026" targets, which keeps 3.12.2 unmet.

**Revised 2026-09-15 (assessment revision 1.1): 35 → 42.** Seven requirements
re-determined on evidence produced between 08-03 and 09-15 — **3.2.1, 3.2.2, 3.2.3**
(training records, role assignment, competency), **3.3.4** (audit-failure alert
proven end to end, twice), **3.4.1** (baseline maintenance restored and evidenced;
attached storage added to the inventory), **3.6.3** (tabletop conducted and signed),
**3.10.3** (visitor log operating with nil attestations). AT is now complete at 3/3.
The evidence existed for weeks; **the assessment had simply not been re-walked**,
which is why the figure is now revised as evidence changes rather than annually.

**Reading this correctly.** "Not Met" here spans two very different situations,
and conflating them misrepresents the system in opposite directions:

- **Controls that are absent or broken** — roughly a third. Genuine risk. Examples: no CVE-level vulnerability scanning (3.11.2); no separation of the internet-facing tier from the CUI data tier (3.13.5); the NAS cleartext privileged bind (3.5.10).
- **Controls that function but are not defined, enumerated or evidenced** — roughly two thirds. Real compliance failures nonetheless, because 800-171 requires the definition as well as the implementation, and because an undocumented control cannot be verified, maintained, or transferred to a successor. Tracked collectively as **POA&M-027**.

**257 objective determinations** (revision 1.1, 2026-09-15): **123 satisfied**, 79
partially satisfied, 44 other than satisfied, 6 unverified, 5 not applicable.
*(August revision 1.0 recorded 249 determinations — 107 / 80 / 50 / 6 / 5. The count
rose because re-determination decomposed several combined objective cells.)*

**Assessor independence:** this is a self-assessment. The system owner is also
the assessor and the implementer of the remediation recorded in
`DIWAI-CR-2026-08-01`. No independent review has been performed.

---

## 12. CONCLUSION

The [DOMAIN.ORG] SecureMac Reference System demonstrates that NIST 800-171 / CMMC Level 2 compliance is achievable on Apple Silicon hardware using macOS and ARM64 Linux virtualization.

**Revised conclusion, v2.15** *(figures below are as at 2026-08-01 and are retained as written; current figures are **42/110 objectives met** and **SPRS 101/110** — see the Executive Summary)***.** The full SP 800-171A objective-level assessment of 2026-08-01 materially changed the picture the earlier conclusion described. **35 of 110 requirements have every assessment objective satisfied**, and the SPRS score is **56/110** against verified weights — the 98/110 published since June was never correct, and the properly computed June baseline was 85/110. The technical foundation remains genuinely strong — full FIPS mode on the VM, 100% OpenSCAP CUI compliance, a full Wazuh SIEM stack, Suricata IDS, a pf firewall, and comprehensive audit logging — with a small number of tractable, well-understood gaps remaining. **(Caveat, 06/11/2026: this 98/110 figure is the last-confirmed score and does not yet reflect the 3.2.1/3.2.2/3.2.3 PARTIAL finding opened as POA&M-008 — see §11.)**

**What the rebaseline established.** Four security controls were found
believed-running but inert — the SIEM (down ~21 h), a monitoring agent
(previously ~12 days), the weekly compliance scan (executing a zero-byte script
for roughly two months) and clock synchronisation (24 minutes adrift while
reporting itself synchronised). Two of the four had previously been closed as
fixed. Nineteen remediation changes were applied and verified the same day, and
a control-health check now verifies continuously that controls are actually
running (POA&M-019).

**The honest position.** This system's engineering is sound — FIPS throughout,
encryption at rest everywhere including backups, deny-by-default firewalls,
application-layer MFA over the CUI repository, and a working malicious-code
substitution. What it lacked was assurance that those controls stayed running,
and documentation sufficient for anyone other than its author to verify them.
The first is now addressed. The second is tracked as POA&M-027 and is the
largest remaining body of work.

**This remains a self-assessment** performed by the system owner, who is also
the implementer. Independent assessment should be obtained before any
attestation is relied upon by a third party.

The June 6, 2026 decision to abandon the YubiKey PIV approach (after two lockout incidents) and standardize on **TOTP via Authenticator app** across both the Mac host and the VM **simplifies** — rather than complicates — the path to 110/110: it consolidates what had been two separate, partially-failed MFA efforts into one coordinated rollout that recovers all 8 MFA-related points (3.5.3 -5, 3.7.5 -3) at once. Combined with the overdue annual risk assessment (+3) and the IR tabletop exercise (+1), these three actions account for all 12 of the remaining known SPRS deficit points — the 13th (3.14.2's -1) was recovered 06/12/2026 by closing POA&M-002 via the YARA control substitution. POA&M-008 (3.2.1/3.2.2/3.2.3, weight TBD) is additional and not yet included in that count.

### Priority Action Items

| Priority | Item                                                             | SPRS Recovery               | Target              |
|:---------|:-----------------------------------------------------------------|:----------------------------|:--------------------|
| 1        | Unified TOTP MFA rollout — VM (POA&M-004) + Mac host (POA&M-007) | +8 pts (3.5.3 + 3.7.5)      | Q3 2026             |
| 2        | Annual risk assessment (POA&M-005)                               | +3 pts                      | OVERDUE — immediate |
| 3        | IR tabletop exercise (POA&M-006)                                 | +1 pt                       | 06/30/2026          |
| ✓        | SI-3 malware protection — YARA stack (POA&M-002)                 | **+1 recovered**                | **DONE 06/12/2026**     |
| 5        | [DOMAIN.ORG]-specific security awareness training (POA&M-008)       | TBD pts (3.2.1/3.2.2/3.2.3) | Q3 2026             |
| —        | mSCP 8 failing rules remediation — Mac host (POA&M-003)          | (no direct SPRS weight)     | Q3 2026             |

---

## AUTHORIZATION

**Full Authorization Granted:** June 5, 2026\
**Authorization Period:** 3 years (through June 4, 2029)\
**Authorizing Official:** /s/ [SYSTEM-OWNER], System Owner/ISSO\
**[SYSTEM-OWNER] LLC dba [ORGANIZATION]**\
**Date:** \____\_ (pending re-signature for v2.14)

---

## APPENDICES

### Appendix A: Acronyms

- **AC** — Access Control; **aarch64** — ARM64 architecture; **ATO** — Authorization to Operate
- **AU** — Audit and Accountability; **CA** — Security Assessment; **CM** — Configuration Management
- **CMMC** — Cybersecurity Maturity Model Certification; **CP** — Contingency Planning
- **CUI** — Controlled Unclassified Information; **CVE** — Common Vulnerabilities and Exposures
- **DFARS** — Defense Federal Acquisition Regulation Supplement; **FAR** — Federal Acquisition Regulation
- **FCI** — Federal Contract Information; **FIM** — File Integrity Monitoring
- **FIPS** — Federal Information Processing Standards; **IA** — Identification and Authentication
- **IDS/IPS** — Intrusion Detection/Prevention System; **IR** — Incident Response
- **ISSO** — Information System Security Officer; **LDAP** — Lightweight Directory Access Protocol
- **LUKS** — Linux Unified Key Setup; **MA** — Maintenance; **MFA** — Multi-Factor Authentication
- **MLX** — Machine Learning eXchange (Apple Silicon native inference framework)
- **MP** — Media Protection; **mSCP** — macOS Security Compliance Project
- **NIST** — National Institute of Standards and Technology; **PE** — Physical Protection
- **POA&M** — Plan of Action and Milestones; **PS** — Personnel Security
- **RA** — Risk Assessment; **SC** — System and Communications Protection
- **SIEM** — Security Information and Event Management; **SI** — System and Information Integrity
- **SIP** — System Integrity Protection (macOS); **SSH** — Secure Shell; **SSP** — System Security Plan
- **SPRS** — Supplier Performance Risk System; **TLS** — Transport Layer Security
- **TOTP** — Time-based One-Time Password (RFC 6238); **UTM** — Universal Turing Machine (virtualization)

### Appendix B: References

 1. NIST SP 800-171 Rev 2 — Protecting CUI in Nonfederal Systems and Organizations
 2. NIST SP 800-171A — Assessing Security Requirements for CUI
 3. FAR 52.204-21 — Basic Safeguarding of Covered Contractor Information Systems
 4. DFARS 252.204-7012 — Safeguarding Covered Defense Information
 5. FIPS 140-2 — Security Requirements for Cryptographic Modules
 6. CMMC Model Version 2.0 — Cybersecurity Maturity Model Certification
 7. 32 CFR Part 2002 — Controlled Unclassified Information
 8. macOS Security Compliance Project (mSCP) — github.com/usnistgov/macos_security
 9. Wazuh Documentation v4.14.5 — documentation.wazuh.com
10. Rocky Linux 9 SCAP Security Guide — access.redhat.com/documentation
11. NIST SP 800-88 Rev 1 — Guidelines for Media Sanitization
12. RFC 6238 — TOTP: Time-Based One-Time Password Algorithm

### Appendix C: Supporting Documentation

**Compliance Scanning:**

- VM OpenSCAP scan: `/usr/local/bin/oscap-scan.sh` (weekly, Sunday 02:00)
- Mac mSCP scan: `/usr/local/bin/run-mSCP-scan.sh` (weekly, Sunday 03:00)
- Compliance dashboard: https://securemac.[DOMAIN.ORG] (Apache, LDAP-authenticated)

**Infrastructure:**

- nginx config: `/opt/homebrew/etc/nginx/servers/ai.[DOMAIN.ORG].conf`
- USB Guard (Mac): `/usr/local/sbin/usb-guard`, `/usr/local/sbin/usb-guard-monitor`, `org.diwai.usb-guard` LaunchDaemon
- Time Machine auto-mount: `/usr/local/sbin/mount-tm-drive.sh`, `org.diwai.mount-tm-drive` LaunchAgent
- OpenVPN: `/etc/openvpn/server/diwai.conf`
- AI stack: `org.diwai.lmstudio` (LM Studio, 127.0.0.1:1234), `org.diwai.open-webui` (127.0.0.1:3000), `org.diwai.rag-mcp` (document library search, 127.0.0.1:8767), `org.diwai.nginx`; change records `DIWAI-CR-2026-10-01` and `DIWAI-CR-2026-10-02`; inventory in the current SBOM (`Compliance/SBOM/CUI_Software_Bill_of_Materials.md`)
- Malicious-code scanning (VM): YARA 4.5.2 (`/usr/local/yara/rules/index.yar`); Wazuh active-response `yara.sh` (FIM 550/554); weekly `yara-fullscan.timer` (`/usr/local/sbin/yara-fullscan.sh`)

**Architecture & Assessment (**`Compliance/`**):**

- Network/stack schematic: `Architecture/RS2_Network_Schematic.svg` (+ editable `.drawio`)
- CUI data-flow diagram: `Architecture/RS2_CUI_DataFlow.svg` (+ `.drawio`)
- Stack & tool reference: `Architecture/RS2_Stack_Reference.md`
- Independent gap assessment: `Assessment/RS2_Gap_Assessment_2026-06-12.md`
- SI-3 control substitution (malware protection): `Evidence/SI-3_Control_Substitution_ClamAV_Decommission_2026-06-12.md` (DIWAI-EV-SI3-002)

**Policies:** DIWAI-IRP-001, DIWAI-RA-001, DIWAI-PS-001, DIWAI-PE-MP-001, DIWAI-SI-001, DIWAI-AUP-001, DIWAI-AAP-001, DIWAI-CMP-001, DIWAI-ATP-001, DIWAI-IAP-001 (v1.1), DIWAI-SCP-001

### Appendix D: Document Maintenance

This SSP shall be reviewed and updated quarterly or upon significant system changes.

**Next Scheduled Review:** September 30, 2026

**Companion Documents (resolved 06/11/2026):**

- `CUI_[DOMAIN.ORG]_Unified_POAM_v1.32.md` — the standalone POA&M of record and **single source of truth for POA&M status** (64 tracked items, POA&M-001 through POA&M-074; **39 closed, 25 open**), 2026-09-13, in `Compliance/POAM/` (supersedes the v1.7 file, which carried internal Version 1.29 — see the filename/version realignment note in `DIWAI-MFR-2026-08-12`). §10 carries **counts only** and no longer duplicates the register; per-item detail, milestones and history live in the standalone POA&M.
- **DIWAI-IAP-001 v1.1** — Identification and Authentication Policy, effective **06/06/2026**, reflecting the unified TOTP MFA strategy (§4.5). This also corrects the Rev. 2.12 (06/06/2026) revision-history entry's reference to "TCC-IAP-001," which is a different, CyberInABox/CPN-scoped document (see Document ID correction in revision history above).

**Review Focus Areas:**

- POA&M-004 / POA&M-007 unified TOTP MFA deployment status
- POA&M-005 risk assessment completion (OVERDUE)
- POA&M-006 IR tabletop exercise (June 30 deadline)
- ~~POA&M-002 ClamAV daemon / YARA remediation~~ — **CLOSED 06/12/2026** (SI-3 substitution to YARA stack; DIWAI-EV-SI3-002)
- POA&M-003 mSCP 8 failing rules remediation progress
- **Document-ID audit (completed 06/11/2026):** All ten remaining `TCC-*-001` policy citations in §6 and Appendix C, plus ~9 inline citations throughout §3/§4, have been corrected to their `DIWAI-*-001` equivalents (v1.0; effective dates vary by policy — 11/02/2025 or 02/15/2026, verified against source 2026-08-02; the blanket 04/10/2026 previously stated here was incorrect. Canonical copies now in the CUI store, `Compliance/Policies/`). This was driven by a definitive determination that **[DOMAIN.ORG] is an independent, standalone system and does not share policies, controls, or evidence with the CyberInABox/CPN reference system** — see the "2.12 (corrected)" revision-history entry above for the full list of changes. The two prior "shared/common controls, inherited by both SSPs" notes (former §3.3, §4.10) have been rewritten to describe [DOMAIN.ORG]'s physical/media protection controls as documented solely in DIWAI-PE-MP-001, independent of any physical co-location with CyberInABox.
- **POA&M-008 / SPRS weight confirmation (opened 06/11/2026):** The Document-ID audit above surfaced a substantive gap — §4.2 (3.2.1/3.2.2/3.2.3) had relied solely on a CyberInABox-specific training record (now removed). These three controls are now PARTIAL pending [DOMAIN.ORG]-specific training delivery and records (POA&M-008, target Q3 2026). Their SPRS point weight is **TBD** — confirm against the official DoD NIST SP 800-171 Assessment Methodology and update §11/§12/the POA&M dashboard accordingly before the next self-assessment submission.
- Open Web UI, LM Studio and model currency (manual updates; new models checked against the publisher's checksums)
- macOS 26.x security updates
- Wazuh and Suricata signature updates
- Outstanding companion documents (above) — drafting and approval

---

**— END OF SYSTEM SECURITY PLAN —**

**Document Classification: CONTROLLED UNCLASSIFIED INFORMATION (CUI)**\
**System: [DOMAIN.ORG] SecureMac Reference System**\
**Version: 2.14 | Date: June 29, 2026**

---

### Appendix E: System Inventories and Defined Parameters (added v2.15)

Added to close the definition gaps identified by DIWAI-ASMT-2026-08 and tracked
as **POA&M-027**. Several 800-171 requirements ask the organization to *define*
a parameter, not merely to implement a capability; those definitions live here.

#### E.1 Account Inventory (3.1.1, 3.1.5, 3.5.1)

| Account                    | Location            | Type                     | Privilege                                     | Notes                                                                                                                                            |
|:---------------------------|:--------------------|:-------------------------|:----------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| `[USERNAME]`                   | 389-DS + both hosts | Interactive, human       | Administrative (`admin` on macOS, `%wheel` on VM) | Sole human operator. Also serves as the Apache LDAP bind account and the Nextcloud agent account — see E.6                                       |
| `sysadmin`                   | Mac host            | Interactive, **break-glass** | Administrative                                | Emergency recovery only. Used 2026-04-15 and 2026-05-15 during YubiKey PIV lockout recovery                                                      |
| `root`                       | Both hosts          | System                   | Full                                          | No interactive login; `permitrootlogin no` on the VM                                                                                               |
| `wazuh`                      | Both hosts          | Service                  | Scoped to agent/manager operation             | —                                                                                                                                                |
| `cn=Directory Manager`       | 389-DS              | Directory superuser      | Full directory                                | Used only by the administrator from the directory's local socket; the NAS now binds as its own scoped account `svc-nas` (checked 2026-10-23, `DIWAI-EV-AC-2026-10-23`). Credential rotated 2026-08-02 (POA&M-021, closed) |
| Per-daemon system accounts | Both hosts          | Service                  | Least privilege                               | `mysql`, `dirsrv`, `postfix`, `dovecot`, `suricata`, `_www` etc.                                                                                             |

**Groups governing access:** `cn=admins` (SecureMac Admin dashboard),
`cn=cui-users` (Nextcloud CUI group folder), `cn=mail-users`, `cn=vpn-users`.

#### E.2 Separation of Duties — Documented Limitation (3.1.4)

This system has **one human user**, who is simultaneously system owner,
operator, administrator, assessor and approving authority. Separation of duties
as described in 3.1.4 **cannot be implemented** and is not claimed.

Compensating controls: comprehensive audit logging with extended retention
(3.3.1); a maintained change record with backup and rollback for every change
(`DIWAI-CR-2026-08-01`); automated control-health verification independent of
the operator (POA&M-019); and immutable-by-default evidence retained in the CUI
repository. External independent assessment should be obtained where
practicable; none has been to date.

#### E.3 Flaw Remediation Timeframes (3.14.1)

Defined in v2.15; previously undefined, which was the basis of the 3.14.1
finding.

| Activity                                   | Timeframe                                                            |
|:-------------------------------------------|:---------------------------------------------------------------------|
| Identify available flaws/updates           | Daily, automated (`dnf-automatic` download-only; macOS `softwareupdate`) |
| Review pending updates                     | **Monthly**, and **on return to the system after any gap exceeding 30 days** (revised 2026-09-15 — see note below) |
| Apply Critical / security-relevant updates | **Within 7 days** of review                                              |
| Apply routine updates                      | **Within 30 days** of review                                             |
| Reboot to activate kernel/OS updates       | **Within 14 days**, scheduled — attended, see E.7                        |
| Report flaws                               | **An actionable CRITICAL: mailed to the owner within 30 minutes of the scan report** (`diwai-control-health` check 5c, every 15 minutes). **All findings: at each monthly review** in `DIWAI-PR-LOG`, and quarterly in the POA&M review |

**Review cadence revised 2026-09-15 — weekly → monthly, deliberately.** The weekly
cadence was set in v2.15 and **lapsed for five and a half weeks** (2026-08-07 to
2026-09-15) while the operator worked on other systems. The lapse was found by the
automated control-health check, not by the calendar.

The revision reflects how the system is actually operated: **it is worked in
concentrated sessions and may sit unattended for weeks.** What does *not* pause is
exposure — mail (port 25) is internet-published continuously (webmail and OpenVPN were until 2026-10-25, `DIWAI-CR-2026-10-51`) and the VM
runs whether or not the operator is present. The response is therefore split:

- **Detection stays continuous and automated** — daily scans on both hosts, with
  `diwai-control-health` mailing the owner on any actionable CRITICAL. This is the
  control that does not depend on human attendance, and on 2026-09-15 it was what
  surfaced three CRITICAL findings.
- **PATCH-class CRITICAL remains 72 hours from detection** (`DIWAI-PR-001` §6.1),
  unchanged and unaffected by the review cadence.
- **The human review moves to monthly**, plus a mandatory review on returning after
  any gap over 30 days.

**Why this is stronger, not weaker.** 3.14.1 requires the organization to *define*
remediation timeframes **and meet them**. A monthly cadence that is met is better
evidence than a weekly one that is not, and the deadline that actually protects the
system — 72 hours on criticals — is untouched. A **reminder to the owner** is to be
wired into the control-health path so the evidence obligation has the same automated
backstop the CVE findings have; until it exists, the cadence depends on memory.

**Accepted deviation:** `dnf-automatic` is configured **download-only**
(`apply_updates = no`) following an unattended upgrade that disabled the SIEM
for ~21 hours on 2026-07-31. The deviation is accepted deliberately: unattended
installation applies unapproved changes to a CUI baseline (3.4.3/3.4.4) and has
demonstrably disabled a security control.

**Tailoring (added 2026-08-02, POA&M-025).** The SSG CUI rule
`dnf-automatic_apply_updates` cannot pass and will not. Left as a standing
failure it trains the operator to ignore scan results — the failure mode this
rebaseline exists to correct. It is therefore **tailored out with the
justification recorded in the tailoring file itself**
(`/etc/diwai/scap/diwai-cui-tailoring.xml`), not silently suppressed. The VM now
reports **101/101** against profile
`xccdf_org.diwai_profile_cui_tailored`. An assessor reading the scan results
should read the tailoring file alongside them.

**The compensating control is the monthly patch review,** `DIWAI-PR-001`**.** If that
review does not happen, the deviation is not compensated — the system is simply
unpatched. Updates are downloaded and staged (`download_updates = yes`), so
review costs time, not availability.

#### E.4 Identifier Management Periods (3.5.5, 3.5.6)

| Parameter                             | Value                                                          |
|:--------------------------------------|:---------------------------------------------------------------|
| Identifier reuse prohibited for       | **Indefinitely** — identifiers are never reissued                  |
| Accounts disabled after inactivity of | **90 days.** **Directory (389-DS): ENFORCED 2026-09-13** — Account Policy Plugin, `accountInactivityLimit 7776000`, proven by refusal (`DIWAI-CR-2026-09-08`). **Mac local accounts: ENFORCED** by the daily job `diwai-inactivity-enforce` (90 days idle, warning from 80 days, `sysadmin` break-glass exempt by owner direction 2026-09-13; retested 2026-10-19 after its confirmation check was corrected, `DIWAI-CR-2026-10-17`). **VM local accounts: ENFORCED** by the daily job `diwai-inactivity-enforce-vm` (04:25; 90 days idle, warning from 80 days; `root` exempt as the console-only break-glass; at most one account disabled per run; does nothing if the clock is not synchronized; confirmed by reading the account's expiry back; proven 2026-10-19 by PAM refusing a disposable account, `DIWAI-CR-2026-10-18`; monitored by control-health check 16). Never-logged-in directory entries are not yet covered. The 3.5.6 point was **awarded 2026-10-22** on the owner's decision: both hosts were covered (the condition set on 2026-10-19) and the first scheduled runs were observed on 2026-10-20, -21 and -22; no real account has yet aged out; **POA&M-076**. Constraint: the `sysadmin` break-glass account                                                        |
| Password reuse prohibited for         | **6 generations**: directory `passwordInHistory: 6` (enforced from 2026-08-01); Mac `diwai.password.history`; **VM local accounts `pam_pwhistory remember = 6`** (enabled 2026-10-23, `DIWAI-CR-2026-10-25`) |
| Change of characters (3.5.7 [b])      | A new password must differ from each of the previous six (the history rule above); no further character-difference rule. Stated 2026-10-24 (`DIWAI-CR-2026-10-43`) |
| Temporary passwords (3.5.9)           | Must be changed at first login. **Directory: ENFORCED 2026-10-24** (`passwordMustChange` on; an administrator-set password returns "unwilling to perform" with the password-expired control until the user changes it; proven on a disposable account). Service accounts are unaffected (own policy, binds re-checked) |
| Account lockout threshold             | **3 failed attempts** (`passwordMaxFailure: 3`)                      |
| Lockout duration                      | **3600 s**, auto-clearing (`passwordUnlock: on`)                     |
| Account lockout, VM operating system (PAM faillock) | **3 failed attempts within 300 s; locked 900 s** (`/etc/security/faillock.conf`; `DIWAI-CR-2026-10-11`) |
| Account lockout, Mac host             | **5 consecutive failed attempts; auto-releases 900 s after the last failure** (`diwai.authentication.lockout`; `DIWAI-CR-2026-10-11`). macOS has no separate counting window; the rule is at least as strict as a 5-minute window. |
| Minimum password length               | **16** on all three — **the VM's own accounts too (`pwquality.conf` `minlen = 16`, raised from 15 on 2026-10-23)** — Mac `diwai.minimum.length` (rule text `.{16,}+`); 389-DS `passwordMinLength: 16` with `passwordCheckSyntax: on`. **Raised from 14 and negatively tested 2026-10-09** (`DIWAI-CR-2026-10-11`). The 14-character alignment was made and negatively tested 2026-09-13 (`DIWAI-CR-2026-09-03`); until that date the 389-DS minimum was configured but **not enforced** |
| Password change interval              | **At least every three years, and after any incident or evidence of compromise, for every password** (`DIWAI-IAP-001` §3.3; Rev 3 03.05.12.e; replaces 90 days, `DIWAI-CR-2026-10-26`). Every password on this system has a login path without a second factor (consoles, webmail and mail, break-glass, service and recovery accounts), so none is exempt. **Enforced by the system:** Mac `[USERNAME]` per-user policy `diwai.password.expiry` **1095 days**; VM local `[USERNAME]` `chage -M 1095` (next change 2029-10-08); directory `passwordMaxAge` **94,608,000 s**, warning 14 days, `[USERNAME]` stored expiry 2029-10-08. **Tracked in the credential register `DIWAI-CRR-001`** (checked by monitor check 18): VM `root` (last 2026-10-19), Mac `sysadmin` (2026-08-07), `svc-nas` (2026-08-02). `demo_user` is locked. Proven on 2026-10-23: a VM account last changed 1,000 days ago is accepted by the account stack, one last changed 1,100 days ago is refused. |

#### E.5 Key Management (3.13.10)

| Key material             | Generation                 | Storage                                                     | Rotation            | Escrow            |
|:-------------------------|:---------------------------|:------------------------------------------------------------|:--------------------|:------------------|
| `*.[DOMAIN.ORG]` TLS (ECDSA)  | certbot, Cloudflare DNS-01 | `/etc/letsencrypt`, distributed to 4 consumers by deploy hook | Automatic, ~60 days | None (reissuable) |
| LUKS volume key (VM)     | Install time               | Single keyslot, passphrase only                             | Never rotated       | **NONE — POA&M-026**  |
| FileVault (Mac)          | Install time               | Secure Enclave                                              | —                   | Recovery key      |
| SSH host + user keys     | `ssh-keygen`                 | `/etc/ssh`, `~/.ssh`                                            | On compromise       | None              |
| 389-DS Directory Manager | Install time               | Directory config                                            | Rotated 2026-08-02 (POA&M-021, closed); on exposure thereafter | None              |
| Wazuh agent keys         | `manage_agents`              | `/var/ossec/etc/client.keys`                                  | On re-enrolment     | Backed up         |

**Procedure (added 2026-10-23, 3.13.10).** *Generation:* keys are generated on the host that uses them with the platform tool (certbot, `ssh-keygen`, the Secure Enclave, `manage_agents`, `cryptsetup`). *Storage:* in the locations in the table, readable by root or the owning service only, and never committed to a repository. *Rotation:* TLS certificates automatically about every 60 days; SSH keys on compromise or when a device is retired; the directory superuser credential on exposure; Wazuh agent keys on re-enrolment. *Escrow:* as in the table, with the LUKS passphrase as the exception below. *Destruction:* a retired key is removed from every location in the table and the end of its use is confirmed; destroying a drive's key is the way to sanitize it (3.8.3).

**Known deficiency:** the LUKS volume has a single keyslot and no escrow. Loss
of the passphrase is unrecoverable data loss, and the VM cannot boot
unattended — see E.7. Tracked as POA&M-026.

#### E.6 External System Dependencies (3.1.20)

| External system                   | Purpose                                             | Data exposed                         | Control                          |
|:----------------------------------|:----------------------------------------------------|:-------------------------------------|:---------------------------------|
| Cloudflare                        | DNS for `[DOMAIN.ORG]`; apex/www hosting; certbot DNS-01 | DNS records, ACME challenges         | API token scoped to DNS edit     |
| Let's Encrypt                     | TLS certificate issuance                            | Domain names only                    | ACME, automated                  |
| VirusTotal                        | FIM event enrichment                                | File hashes only — **not file contents** | API key, rate-limited            |
| `pool.ntp.org`                      | Time synchronisation                                | None                                 | Outbound only                    |
| Wazuh / EPEL / Rocky repositories | Package updates                                     | None                                 | GPG-verified, download-only      |
| GitHub (`securemac-site`)           | Public compliance site                              | **Redacted content only** — see 3.1.22   | Redaction gate, no `CUI` filenames |
| Wi-Fi network (`en1`)               | Secondary connectivity                              | Unassessed                           | WPA2/WPA3 Personal — **POA&M-024**   |

#### E.7 Alternate Work Sites and Media Custody (3.10.6, 3.8.5)

Established in v2.15 following the NCMA demonstration (2026-07-21 → 07-31), at
which the system was operated off-site with **no procedure, custody record or
authorisation record** — the finding that prompted this section.

**Before off-site operation:** record written authorisation from the system
owner; verify FileVault and LUKS are active; verify TOTP enrolment travels with
the operator; record an inventory of transported equipment and media.

**During:** CUI accessible only through the encrypted repository with MFA; no
CUI copied to unencrypted media; USBGuard remains active; host firewalls remain
enabled.

**On return:** reconcile the equipment/media inventory; verify no residual CUI
on transient media; return the system to the documented baseline and verify
(`demo-down.sh` and the control-health check).

**Scope (owner statement 2026-10-24):** CUI is not handled anywhere other than the controlled rack site; the safeguards above apply only if that changes.

**Media custody record:** maintained for any CUI-bearing media leaving the
controlled area, recording date out, custodian, encryption state, date returned,
and verification performed.

**Unattended boot limitation:** the VM requires an interactive LUKS passphrase
at every boot (single keyslot, no TPM2/clevis). Consequently the system cannot
self-recover from power loss and kernel patching requires physical presence.
This constrains E.3 and is tracked as POA&M-026.

#### E.8 Physical Access Records (3.10.3, 3.10.4)

Established in v2.15; previously no visitor or physical-access log existed.

- **Visitor log** — date, name, organization, purpose, escort, in/out times. All visitors escorted; the site is single-occupant with no unescorted access.
- **Physical access log** — entries recorded for maintenance of, or physical access to, the rack enclosure.
- **Physical access devices** — keys to the rack enclosure and premises inventoried, holder recorded, reconciled at each quarterly review.

#### E.9 Audit Records: Retention, Review and Who May Manage Them (3.3.1, 3.3.3, 3.3.9)

*Defined 2026-10-23 (owner approval in chat, `DIWAI-APP-001` and the re-walk).*

| Parameter | Value |
|:---|:---|
| **Retention, VM `auditd`** | Rotated at 64 MB, 100 files kept (about 6.4 GB) on its own 10 GB volume. Measured 2026-10-23: **83 days held** (oldest 2026-08-01), 19% of the volume used. The cap is reached at roughly 270 days at the current rate |
| **Retention, Wazuh alerts** | **90 days** online (the `wazuh-alerts-*` index policy, rebuilt 2026-09-25); alert files are also kept by month on disk |
| **Retention, Mac** | The BSM audit trail is kept **90 days** locally (`expire-after:90d`, set 2026-10-23, `DIWAI-CR-2026-10-39`; was 7 days). About 0.5 GB a day, about 46 GB at 90 days. **It takes 90 days to accumulate: verify on 2027-01-21.** The Mac trail is held locally only; Wazuh does not collect it |
| **Review of what is logged** | **Monthly, with the patch review** (`DIWAI-PR-001` §4.8): the audit rule set (113 rules on the VM, Mac flags `lo,aa,ad,-ex,-fm,-fr,-fw`) and the Wazuh rules are read against the services and changes of the month, and the outcome is recorded in `DIWAI-PR-LOG` ("audit-event review"), including "no change needed". The first review is 2026-10-23 |
| **Who may manage audit logging** | **One person: the system owner ([SYSTEM-OWNER]).** Audit files are root-only (VM `/var/log/audit` 0700, Mac `/var/audit` 0700). Any additional administrator needs the owner's written authorization first |

**Result of the first review (2026-10-23).** The 113 VM audit rules are the hardened baseline and record privileged commands, authentication and unsuccessful file access by user sessions. They do **not** record every successful write to a configuration file (a probe file written and removed under `/etc/security` produced no `auditd` event). Those changes are caught instead by **Wazuh file-integrity monitoring** in real time on `/etc`, `/var/www`, `/usr/bin`, `/usr/sbin`, `/bin`, `/sbin` and `/boot` (the probe produced alerts 554 *added*, 550 *checksum changed* and 553 *deleted* within seconds), and **sudo records who ran each command**. Together they answer *what changed* and *who*. No rule change is needed now; explicit `auditd` path watches on `/etc/sudoers.d`, `/etc/pam.d` and `/usr/local/sbin` are a possible later addition.

#### E.10 Roles and Permitted Functions (3.1.2)

| Role | Permitted functions |
|:---|:---|
| **System owner and administrator** (one person) | Everything: administration of both hosts, the directory, Nextcloud, mail, the firewall and the records |
| **Additional user** (a provision only; none exists, `DIWAI-APP-001` §5) | Read and write in the `cui-users` folders of the file store, mail and VPN as a user; **no** administration, no sudo, no change to logs, accounts or security settings |
| **Service accounts** | Only what their daemon needs (E.1); no interactive login |

#### E.11 Remote Access: Permitted Types and Authorized Privileged Commands (3.1.12, 3.1.15)

**Permitted remote access (published):** mail from other servers (SMTP on port 25; §2.5.1). **Switched off since 2026-10-25 (`DIWAI-CR-2026-10-51`):** OpenVPN, internet access to webmail, and mail-client ports 465, 587, 993, 995 (future enabled enhancements). **Not published:** SSH and every administrative interface; SSH is reached from the LAN or through the VPN, with a public key and a TOTP code (E.1, `DIWAI-CR-2026-08-12`, `-08-17`).

**Privileged commands authorized for remote execution:** (1) administration by the owner over SSH with `sudo`, all commands; (2) two automation keys with a **forced command** and no shell: the dashboard-figures key (read-only figures) and the archive-push key (`scp` to one destination). **Security-relevant information accessible remotely:** the Wazuh dashboard and the SecureMac dashboard (LAN, directory `cn=admins` group), and the logs, over SSH.

#### E.12 Wireless (3.1.16)

The Mac's Wi-Fi interface (`en1`) is an **authorized break-glass uplink** that gives the host a route to the internet if the carrier circuit fails. It is **normally off**; the radio was set **Off on 2026-10-23** (it had been found On and unassociated). The only access point is the household Wi-Fi network (the out-of-boundary residential network, §2.5.2), used with WPA2 or WPA3 Personal. The owner turns it back off after any use.

#### E.13 Architectural Principles Employed (3.13.2)

1. **Defense in depth:** a perimeter firewall (default deny), host firewalls, SELinux, fapolicyd, file-integrity monitoring, intrusion detection, FIPS cryptography and encrypted storage.
2. **Least functionality and least privilege:** services removed when not needed (Grafana, ClamAV), per-daemon accounts, read-only diagnostic scripts, and passwordless sudo only for named read-only scripts (`DIWAI-CR-2026-10-21`, `-22`).
3. **Default deny and allow by exception:** firewall rules, application allow-listing, an allow-listed USB policy.
4. **Separation of concerns:** a management plane (LAN, `cn=admins`) apart from user access; **the internet-facing tier is not yet separated from the CUI data tier** (3.13.5, POA&M-023), which is the main structural weakness and is planned.

#### E.14 Security Impact of Changes and Diagnostic Media (3.4.4, 3.7.4)

**Security impact.** Before any change to either host, its security impact is analysed and written in the change record (a "Security analysis" or "Risks" section, as in `DIWAI-CR-2026-09-05` §3, `-10-21` §3 and `-10-23` §4), together with a backup, a rollback and a verification. A change without that section is not made.

**Diagnostic and test media.** Any diagnostic or test program, and any media that carries one, is checked before use: scanned with YARA and VirusTotal, assessed by Gatekeeper on the Mac, allowed by USBGuard (allow-listed devices only) and by fapolicyd on the VM.


#### E.15 Separation of User Functionality from System Management Functionality (3.13.3)

**User functionality** is what people do with the data: Nextcloud (the CUI repository, on the Mac), webmail (`webmail`, on the VM), the AI chat and the document libraries (loopback services on the Mac). Access is by the group `cn=cui-users`.

**Management functionality** is what administers the system: the admin portal (`securemac`), the directory manager interface (`ldap`), the SIEM dashboard (`wazuh`), SSH to either host, and the directory's own tools. Access is by the group `cn=admins`, by source network, or by SSH key plus TOTP.

**How they are separated**

| Separation | By what |
|:---|:---|
| Different interfaces | Each function has its own host name and virtual host; management is not reachable through a user URL |
| Network | The directory manager and the SIEM dashboard accept only the CUI network ([LAN-IP-REDACTED]/24) and the host itself; they are not published to the internet. The SIEM dashboard and its indexer listen on loopback only |
| Authorization | The admin portal requires `cn=admins`; the user services require `cn=cui-users`. The two groups are different |
| Remote administration | SSH to the VM needs key plus TOTP; to the Mac, key, password and TOTP; Cockpit is disabled |
| Service identities | The services bind to the directory as their own scoped accounts (`svc-apache`, `svc-dovecot`, `svc-nextcloud`, `svc-nas`, `DIWAI-CR-2026-10-38`), not as a person's account; the directory superuser is used only from the host's local socket |
| Host split | The user repository (Nextcloud) runs on the Mac and the management portal and SIEM on the VM, so the two are not on one operating system instance |

**Limits, stated.** One person holds both roles (owner and administrator), so the separation is of interfaces, networks and authorization, not of people. The VM carries both webmail (user) and the management virtual hosts. The Mac carries the Nextcloud repository and the host administration.

The stale `uid=drilldbg61ff` member of `cn=cui-users` was removed on 2026-10-24 (`DIWAI-CR-2026-10-47`); no other group member lacks an entry. Approved by the owner 2026-10-24.

#### E.16 Separation of Duties: Not Applicable on a Stated Fact (3.1.4)

The organization has one individual with any access to the system, so there is no second individual to separate duties from. Compensating controls remain in force: every change is described, approved by the owner and only then run; privileged actions are logged on both hosts; every change is recorded in a signed change record; an outside reviewer can be asked. If a second individual is given any access, the requirement applies in full and the determination is re-walked that day (`DIWAI-APP-001` v1.3). Owner decision 2026-10-24.

#### E.17 Nonsecurity Functions and the Role Rule (3.1.6)

**Nonsecurity functions** are the everyday tasks that need no administrative power: reading and writing email (webmail and the mail client), web browsing, working with documents and spreadsheets, using the AI chat and document libraries, and reading dashboards.

**Rule.** Those tasks run in the owner's ordinary session without administrative power. Any privileged action (installing or changing software, changing configuration, controlling a service, reading protected files) is done by elevating with `sudo`, which asks for the password: on the Mac again after 5 minutes in a terminal, on the VM again after 2 minutes (read 2026-10-24). A separate daily account is not used (owner decision 2026-10-24).

**Temporary exception, recorded.** From 2026-10-23 to 2026-10-26 13:33 (Mac) and 13:36 (VM) the owner granted passwordless `sudo` for a maintenance round (`DIWAI-CR-2026-10-23`, extended 2026-10-24). The password rule resumes when it ends; the first check after it ends is on 2026-10-26.


#### E.18 NAS Management Port 5000 and Protection of CUI on the NAS (3.13.8, 3.5.10)

The Synology NAS is shared infrastructure that serves other clients, so its HTTP management port (5000) stays open; closing it is not possible without breaking them (owner decision 2026-10-24, option A of the POA&M-066 options). The basis is the owner's consistent position that **the information on the NAS is encrypted by its owner before it arrives and is not readable by anyone else**, which matches what was verified: the Wazuh alert archives are FIPS-encrypted before the push and the VM image archive is a LUKS image (`CUI_Backup_Procedures_v2.0.md` §4, §5), and the rule is that any writer of CUI to the NAS encrypts first.

Consequences stated: (1) no CUI reaches the NAS in the clear, so a cleartext management session on port 5000 exposes no CUI; (2) none of this system's components uses port 5000: administration uses HTTPS on 5001, files move over SMB, SSH on the NAS is disabled, and the NAS's directory bind uses LDAPS (TLS 1.3, read from the directory log 2026-10-24); (3) the DSM API requires multifactor authentication for the accounts that use it (owner statement). **Port 5000, as read on 2026-10-24:** it is plain HTTP, not HTTPS (HTTPS to port 5000 fails). A browser that opens it receives a page whose script sends it to `https://<NAS>:5001` before any login form appears, so a person's password goes over HTTPS on 5001; the owner states port 5000 is used only by people, never by scripts, and that sign-in requires multifactor authentication. **Residual risk, accepted by the owner:** the DSM web API on port 5000 still answers in the clear, so a deliberately written script could send a password unencrypted on the local network; none exists, and the port is not published to the internet. The NAS's other shares were not inspected for this statement.


#### E.19 Media Containing CUI: Access and Transport (3.8.5)

**Access to media:** every medium that holds CUI is encrypted (FileVault on the two attached drives, LUKS on the VM disk and its image archives, FIPS-encrypted alert archives on the NAS) and sits in the locked cabinet (PE layer 4); the keys are not on the media.

**Transport:** **no medium containing CUI is transported outside the controlled area** (owner statement 2026-10-24). The attached drives are fixed storage (§2.5.0). A drive that is retired leaves only after its key is destroyed (3.8.3).

**If that ever changes** (a drive must travel, for a restore test elsewhere, for example): before it leaves, the owner authorizes it in writing; the drive must be encrypted and locked; the custody record of Appendix E.7 is opened (date out, custodian, encryption state, destination); on return the record is closed with the verification done. This is the same procedure E.7 defines for alternate work sites.

Owner confirmation of the fact F11 and approval: 2026-10-24. A dry-run custody record is `DIWAI-EV-MP-2026-10-24`.

---
