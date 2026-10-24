> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — LIBRARY DE-CONFLICTION, SYSTEM RECORDS AND NIST MAPPING LOADED, REQUIREMENT LOOKUP TOOL, XLSX AND OCR READERS
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-16** |
| **Date opened** | October 19, 2026 |
| **Status** | **IMPLEMENTED; tests pass (§6). Owner approved 2026-10-23. Four items open (§5)** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host only (the services VM was not changed) |
| **Addresses** | **3.4.1** (inventory: SBOM v3.16); **3.4.3** (change control); **3.4.9** (user-installed software: one Python package added by the administrator at the owner's direction). All servers still listen on 127.0.0.1 only |
| **Authority** | Owner instructions of 2026-10-19: de-conflict the library apps; sort the sysadmin library; load the system records; add the NIST mapping; build the lookup tool; add XLSX and OCR to all libraries |
| **Related** | `DIWAI-CR-2026-10-13` (the three libraries), `DIWAI-CR-2026-10-15` (same week) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

After the Studio transfer (`DIWAI-CR-2026-10-13`) the three document libraries were hard to tell apart and partly mixed, and an offline test of the local AI models on 2026-10-19 showed what that costs: asked how diwai disables inactive accounts, the models could not find diwai's own records, could not map a Revision 2 requirement to Revision 3, and repeated out-of-date wording. The changes below address the library layout, the content the models can read, one deterministic lookup for NIST requirements, and the file types the libraries can read.

## 2. Scope

**A. Library apps renamed and given distinct icons.**
1. `/Applications/DIWAI Library.app` is now **`DIWAI Sysadmin Library.app`** (green icon, wrench and screwdriver). The Compliance app has a purple icon (shield with check). The Contract Library is unchanged (blue). The old sysadmin app and the Compliance app had the same icon file until this change.
2. Source: `~/diwai-rag/packaging/` (renamed app folder, `icon/make_icon.swift` and `icon/build_icns.sh` now take a colour, symbol and label; originals saved as `*.bak-20261019`). `install_app.sh` and one test (`tests/test_launcher.py`) were updated for the new name; the original app folder is saved at `~/diwai/backups/DIWAI-Library.app.pre-rename-20261019`.
3. **Not changed on purpose:** the internal name `APP_NAME = "DIWAI Library"`, the service names (`diwai-rag`, `diwai-compliance`) and all ports. A test and a repair check depend on that name, and LM Studio's configuration points at the service names.

**B. Sysadmin library sorted.** 27 documents were removed from the sysadmin index (239 documents / 5,112 chunks → **212 / 4,571**). 24 CyberInABox/dc1 and Phase II installer documents (Chapter 33 to 38, the CyberHygiene specifications, hardware sheets, the February 2026 evidence reports, eight `GH_*` files) were moved, un-indexed, to `~/diwai-rag/documents-cyberinabox-holding` (the technical-evidence separation of the two projects). Three were taken out of the library at the owner's direction (an old multi-system SBOM v2.4, a Grafana README, and one unidentified PDF); their files are kept in `documents-cyberinabox-holding/removed-from-library` and not deleted. The runbook cards and RB-00 to RB-18 were not touched. Index backup: `~/diwai/backups/20261019-pre-sysadmin-sort`.

**C. System records loaded into the Compliance library.** 57 files were copied from the canonical Nextcloud copies and indexed: the SSP v2.18, the Unified POA&M v1.32, the SBOM and 54 change records (staging folder `~/diwai-rag/documents-compliance-records`). The 800-171A self-assessment was **deliberately not loaded**, because it is the answer key for the 800-171A local-AI test. The records are CUI-marked and are read by the local AI under the owner's standing ruling (2026-10-03). Index backup: `~/diwai/backups/20261019-pre-records-ingest`.

**D. NIST Rev 2 to Rev 3 mapping loaded.** NIST's public change-analysis spreadsheet was converted to text (130 requirements) and indexed (114 chunks; `~/diwai-rag/documents-compliance-refs`). Index backup: `~/diwai/backups/20261019-pre-mapping-ingest`. The Compliance library now holds **175 documents / 9,644 chunks**.

**E. New read-only tool `requirement_lookup`.** Semantic search buries a popular identifier such as 3.5.6 under the SSP and POA&M text that mentions it, so the models never saw NIST's statement that Revision 3 withdrew it. The tool is an exact lookup (identifier in either revision, or one to four keywords) over `reference/requirements_r2_r3.json`, built from NIST's spreadsheet and OSCAL catalog; the file records both sources' SHA-256. New code: `requirements.py`; changed: `mcp_server.py` (registers the tool for the **compliance profile only**). The tool says only what NIST's data says; it does not say where a withdrawn requirement went. The Compliance search server (`org.diwai.rag-mcp-compliance`, port 8769) was restarted to load it.

**F. XLSX and OCR readers in all three libraries.** New module `extra_readers.py` (an identical copy in `~/diwai-rag` and `~/rag-library`); `ingest.py` changed in both (backups `ingest.py.bak-20261019`).
1. **XLSX:** each sheet becomes plain text, one line per row with its column headings, sheet names kept, hidden sheets marked. A sheet over 20,000 rows is refused, not truncated.
2. **OCR** for PDFs with no text layer: Ghostscript draws the pages and Tesseract reads them (both already installed, offline). The text starts with a "machine-read, verify against the original" warning and each page carries its confidence. A scan is **refused with a reason** (status "empty", nothing indexed) when it has more than 200 pages, yields no text, or reads below 40% mean confidence. The limits can be changed with `DIWAI_OCR_MAX_PAGES` and `DIWAI_OCR_MIN_CONFIDENCE`.
3. **A deliberate earlier design is reversed.** The Contract Library's PDF reader said there was deliberately no OCR, so that a scan would never be quietly half-read. The owner directed OCR for all libraries. The refusal rules in item 2 keep that design's intent. Four tests that asserted the old behaviour were updated.
4. **New dependency:** `openpyxl` 3.1.5 (and its `et_xmlfile` 2.0.0) installed with pip into both library environments (`~/diwai-rag/venv`, `~/rag-library/venv`), the same version already recorded for RFPShred.
5. The three web managers (ports 8765, 8766, 8768) were stopped and restarted so that they load the new code (all were idle at the time).

## 3. Rollback

1. Restore the index backups named in B, C and D; delete `documents-compliance-refs` and `documents-compliance-records` if the added documents are to go.
2. Reinstall the old sysadmin app from `~/diwai/backups/DIWAI-Library.app.pre-rename-20261019`; restore the `*.bak-20261019` files (`ingest.py` and `mcp_server.py` in `~/diwai-rag`, `ingest.py` in `~/rag-library`, the icon scripts, `test_launcher.py`); delete `extra_readers.py`, `requirements.py` and `reference/requirements_r2_r3.json`.
3. `pip uninstall openpyxl et_xmlfile` in each environment.
4. Restart the three web managers and `org.diwai.rag-mcp-compliance`.

## 4. Execution log (2026-10-19)

1. Compared the three apps' icons (identical hash for sysadmin and Compliance), regenerated icons, renamed and installed the apps, removed the old one from `/Applications`.
2. Listed the sysadmin library, grouped the doubtful files, got the owner's rulings, ran a dry run, then moved and de-indexed 27 files.
3. Scanned the 57 records for secrets. **Disclosure:** the first scan printed the matching lines to this session (they were file hashes and key fingerprints, no credentials). The owner stopped the ingest and corrected the method; the rescan reported counts only (no private keys; one text match that proved to be ordinary prose). The rule is recorded in the assistant's notes.
4. Ingested the 57 records, then converted and ingested the NIST mapping.
5. Built `requirements.py` and the lookup data, registered the tool, ran the tests, restarted the Compliance search server.
6. Added the XLSX and OCR readers, installed `openpyxl`, ran the tests of both projects, restarted the three web managers. Checked afterwards that each server started after the last code change (11:20 against 11:17) and that the Contract page now accepts `.xlsx`.

## 5. Observations and open items

1. **Open: `requirement_lookup` has not been exercised through LM Studio's own tool connection.** It was tested in code and used by the offline test runner, and the search server restarted and answers; LM Studio has not yet been restarted to list the new tool.
2. **Open: the library's wording about Mac inactivity enforcement is out of date** (found by the offline test and a read-only audit on 2026-10-19). The SSP, the POA&M and a runbook card say the Mac is not covered; a daily Mac job has run since 2026-09-13. A review draft of the corrections was prepared; **no document has been changed**. When corrected documents are published they must be re-ingested.
3. **Open: the offline model test is not finished.** Results of 2026-10-19: Gemma 26B answers more carefully and says when it cannot find something; Devstral twice attributed a statement to a document that did not contain it. Gemma's reasoning length varies from about 2,000 to over 12,000 tokens on the same prompt (not a repetition loop; not explained by temperature or by tools in the nine runs made). A recommended setting is not yet chosen.
4. **Open: OCR and XLSX were tested on generated files only.** A real scanned contract and a real workbook have not been tried. English text only (the installed language data are `eng` and `osd`). Spreadsheet formulas that were never calculated have no stored value and read as empty.
5. The records loaded into the Compliance library are copies; the canonical copies remain in Nextcloud, so the library copies go out of date whenever a record is revised unless re-ingested.

## 6. Verification

| # | Check | Result |
|--:|:---|:---|
| 1 | `~/diwai-rag` tests | **Pass**, 427 (15 new for the readers, 12 new for the lookup tool) |
| 2 | `~/rag-library` tests | **Pass**, 187 (the new reader tests plus the updated old ones) |
| 3 | OCR of a generated image-only PDF; a blank scan, an over-length scan and a low-confidence scan are refused with a reason | **Pass** (real Ghostscript and Tesseract) |
| 4 | XLSX: headings kept with every row; hidden sheets marked; over-limit refused | **Pass** |
| 5 | Index sizes after the changes: sysadmin 212 / 4,571; Compliance 175 / 9,644; Contract 145,684 chunks (unchanged) | **Pass** |
| 6 | Three web managers healthy after restart; started after the last code change; the Contract upload page lists `.xlsx` | **Pass** |
| 7 | `requirement_lookup` returns 3.5.6 as "WITHDRAWN in Rev 3" with NIST's stated reason, and a keyword search for "inactive" finds 03.01.01 item f.02 | **Pass** (in code) |
| 8 | `requirement_lookup` visible and working in LM Studio | **Not yet tested** (§5.1) |
| 9 | A real scan and a real workbook ingested from the browser managers | **Not yet tested** (§5.4) |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-23)* |
| **Date** | 10-23-2026 |

---

**Distribution:** Limited to authorized personnel
