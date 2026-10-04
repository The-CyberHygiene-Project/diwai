# Owner decisions register ([DOMAIN.ORG])

**Confirmed by the owner 2026-10-03** (all 12 rows reviewed and agreed; compiled the same day). Each row is a standing ruling by the system owner
that runbook cards may cite by number (`decisions:`). Numbers are permanent: a withdrawn ruling is marked withdrawn,
never renumbered or reused. The source column names where the ruling was recorded.

| No. | Date | Decision | Source | Status |
| --- | --- | --- | --- | --- |
| 1 | 2026-09-13 | A disputed compliance figure is reported at the lower, conservative value. | Owner ruling, 2026-09-13 (SPRS 94 → 93, later 94 once negative tests removed the dispute) | Confirmed 2026-10-03 |
| 2 | 2026-09-13 | SPRS points are claimed only for controls proven working, including negative tests. The strict 800-171A objective count is tracked separately as a documentation gap and is never the score. | Owner ruling, 2026-09-13; DIWAI-VS-001 | Confirmed 2026-10-03 |
| 3 | 2026-09-15 | Patching is monthly. Critical vulnerabilities are fixed within 72 hours of detection, with the clock defined in SSP §6.1. | Owner ruling, 2026-09-15; F-2026-09-04 | Confirmed 2026-10-03 |
| 4 | 2026-09-15 | No interior cameras, ever (privacy). 3.10.4 cannot be met by video. | Owner ruling, 2026-09-15; restated in DIWAI-MFR-2026-09-24 | Confirmed 2026-10-03 |
| 5 | 2026-08-02 | Grafana stays removed. If it is ever restored, it comes from Rocky AppStream, never the vendor repository. | DIWAI-CR-2026-08-04 §5 | Confirmed 2026-10-03 |
| 6 | 2026-10-03 | Documents marked CUI are company-proprietary while held on this system; they become CUI only when held by the Government. The local AI may read them. | Owner ruling, 2026-10-03 | Confirmed 2026-10-03 |
| 7 | 2026-10-03 | gpt-oss models are barred from checks and are never selected automatically. | DIWAI-CR-2026-10-01 | Confirmed 2026-10-03 |
| 8 | 2026-10-03 | Every change to a system or to the AI's document library is approved by a person; the AI cannot add to its own library. | Reference doc rule; Phase 2 plan, 2026-10-03 | Confirmed 2026-10-03 |
| 9 | 2026-10-03 | [DOMAIN.ORG] and [DOMAIN.ORG] are separate systems. Only records about [SYSTEM-OWNER] himself (training, personnel, role designations) may serve both; technical evidence never crosses. | Owner ruling; dated 2026-10-03 at the owner's direction (earlier origin date not recorded) | Confirmed 2026-10-03 |
| 10 | 2026-09-24 | No door sensor on the rack. 3.10.4 rests on the written rack access log (DIWAI-PE-LOG-001) and its monthly nil-activity attestation; the rack, not the room, is the logged boundary. | DIWAI-MFR-2026-09-24 (signed 2026-10-03) | Confirmed 2026-10-03 |
| 11 | 2026-10-03 | Updates are manual only, applied by a person (ISSO direction). LM Studio's internet access is to be blocked once the stack is stable; new models are fetched separately, checked against the publisher's checksums, then added. | Owner ruling, 2026-10-03; signed 2026-10-03 | Confirmed 2026-10-03 |
| 12 | 2026-10-03 | Devstral is the primary model (faster, better at code); other models are fallbacks. gpt-oss stays barred (row 7). | Owner ruling, 2026-10-03; signed 2026-10-03 | Confirmed 2026-10-03 |
| 13 | 2026-10-03 | Aider is on a leash. It drafts runbooks, repairs and tests on the build side, and it never edits a live system configuration file on its own judgment. It may run code only when that code comes from a trusted source (an ISSO-approved repair, or the project's own reviewed code) and a person approves the exact command before it runs. That includes running an approved repair on the live system (option B, owner 2026-10-03). | Owner ruling, 2026-10-03; reference doc (Aider weakened a control 3/3 when it edited freehand in the repair path) | Confirmed 2026-10-03 |
| 14 | 2026-10-04 | A repair runs only if the ISSO approved its exact contents with the YubiKey, PIN and touch. Any change to a repair or to the shared repair code needs a new approval before it can run again. | Owner ruling, 2026-10-04; DIWAI-CR-2026-10-07 | Confirmed 2026-10-04 |
