> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — LOCAL-AI TOOLS BROUGHT FROM THE MAC STUDIO; DOCUMENT LIBRARY SPLIT INTO THREE
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-13** |
| **Date opened** | October 18, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§6) EXCEPT the LM Studio first-launch check, which needs the owner (§6, row 12); owner approved 2026-10-18** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host only (the services VM is untouched) |
| **Addresses** | **3.4.3** (change control); **3.4.1** (baseline inventory kept accurate: SBOM v3.15); **3.4.8/3.4.9** (software on the system is known and controlled); **3.1.20** (removable media: USB guard window, §5.1) |
| **Authority** | Owner instruction 2026-10-18: bring the tools built on the Mac Studio onto this system for production use; keep the existing LM Studio; merge the new sysadmin documents into the existing library; end with a Contract RAG and a Sysadmin RAG (the owner then asked for a third, Compliance, library); delete gpt-oss; label the upload pages so documents are not misfiled |
| **Related** | `DIWAI-CR-2026-10-01` (LM Studio), `-10-02` (document library), `-10-05` (Ollama models removed), `DIWAI-CR-2026-10-14` (Time Machine drive and USB guard, same day) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

The owner built a set of local-AI tools on the Mac Studio (a contracting document library, a solicitation shredder, contract scripts and a tool server). They were carried here on a transfer drive named `AI-TRANSFER` (its encryption was not confirmed, §5.4) with a hand-off note written by the Mac Studio's Claude Code session. The goal was to bring this system in line with that reference where it made sense, while keeping what already works here.

## 2. Scope

**Brought over (from `AI-TRANSFER`, checksum-verified first):**

1. `~/rag-library` — the **Contract Library** (contracting profile only), with its data (chroma_db, collection `rag_library`; 145,684 chunks after this change) and 72 source documents.
2. `~/RFPShred` — solicitation shredder (clause pass, amendments, tables); OCR language data `eng` and `osd` in `~/RFPShred/tessdata`.
3. `~/contract-tools` and `~/contract-tools-mcp` — contract scripts and the `contract-tools` tool server (asks a person to confirm before CUI is processed).
4. Offline Python 3.12.15 environments (Homebrew Python already on the host) built from the drive's wheels with `--no-index`; nothing was downloaded.
5. Tool servers `contract-rag` and `contract-tools` added to `~/.lmstudio/mcp.json` (backup `mcp.json.bak-20261018`).
6. `/Applications/Contract Library.app` (the drive's launcher, renamed from "RAG Library").

**Deliberately not brought over:**

- LM Studio 0.4.26 and the 43,026 runtime files. This host keeps **LM Studio 0.4.25+1** (owner decision; an update is a later, separate change).
- The drive's `sysadmin-rag` tool server and its `sysadmin_db` (see item 8: merged by documents, not by vectors).
- `gpt-oss-20b` (item 9).
- The drive's Devstral Small 2 weights. They differ from this host's copy (shard sizes and checksums); this host's copy is kept. Which is newer was not determined.
- Four credential or private files found in the drive's "sysadmin" folder (two sets of authenticator/back-up codes, a signed non-disclosure agreement, a licence). Their names were seen; they were **not opened, copied or indexed**, and are untouched on the drive.
- Three assessment results/sweep records and two Windows Server documents (owner: not wanted).

**Changed on this host:**

7. **Embedding model pinned for the Contract Library.** The drive's index was built with `nomic-embed-text-v1.5` **Q4_K_M**. Here the unsuffixed model name resolves to the **f16** build (measured: different vectors), which would make every contract search return wrong passages with no error. `EMBED_MODEL` in `~/rag-library/config.py` is pinned to `…@q4_k_m`. LM Studio's bundled Q4_K_M file is byte-identical to the drive's (SHA-256 `d4e38889…1295ac`).
8. **Sysadmin library merged by document, not by vector.** Vectors from the two embedding builds are not interchangeable (cosine 0.93). The drive's "sysadmin" folder held 209 files. Compared by content (SHA-256): 74 were already here; 2 duplicated contract files; 9 were excluded (four credential/private files, three assessment results, two Windows Server documents); 13 were contracting material (sent to the Contract Library; 5 of them were already in its index); 23 were compliance material (item 10); and 88 were sysadmin documents, of which **87 were indexed** here with the f16 model and 1 was skipped as a near-duplicate of a file already in the library.
9. **`gpt-oss-20b` deleted** from `~/.lmstudio/models` (11 GB). It was already barred from checks (it followed an injected instruction in testing). Its catalog entry under `~/.lmstudio/hub` remains (metadata only).
10. **Three libraries instead of one** (the compliance profile existed in `config.py` but was never built):

| Library | Documents / chunks | Index | Manager (on demand) | Search server |
|---|---|---|---|---|
| **Sysadmin** | 239 / 5,112 | `~/diwai-rag/data/chroma_db` | 127.0.0.1:**8766**, `DIWAI Library.app` | MCP 127.0.0.1:**8767**, `org.diwai.rag-mcp`; LM Studio `diwai-rag` |
| **Compliance** (new) | 118 / 8,403 | `~/diwai-rag/data/chroma_db_compliance` | 127.0.0.1:**8768**, `DIWAI Compliance Library.app` | MCP 127.0.0.1:**8769**, `org.diwai.rag-mcp-compliance`; LM Studio `diwai-compliance` |
| **Contract** | ≈145,684 chunks | `~/rag-library/data/chroma_db` | 127.0.0.1:**8765**, `Contract Library.app` | LM Studio `contract-rag` (stdio) |

    95 policy, NIST, SPRS, SSP, TCC and Rev 3 documents were **moved** from the sysadmin library to the compliance library (removed from the sysadmin index, re-indexed in compliance); 23 further compliance files from the drive were added. All search tools are read-only; the network ones bind to 127.0.0.1 only.
11. **Upload pages made unmistakable** (the owner reported two documents had been misfiled earlier because all the pages looked alike). Each manager now shows a full-width banner, a browser-tab prefix, a distinct icon and colour, the port, and the words **"ADDS TO: SYSADMIN / COMPLIANCE / CONTRACTS LIBRARY"** above the drop box. Code change: per-profile names and a `ui` block in `~/diwai-rag/config.py`, `webapp/main.py` and `webapp/templates/page.html`; the drive's `base.html` and `add.html` for the Contract Library.

**Local changes to the Mac Studio's code (to be reported back to the Studio session):** the embedding pin (item 7); `APP_NAME` "RAG Library" → "Contract Library"; the banner/drop-label template edits; one test updated to the new name. The drive's originals are kept as `*.drive-original` and `config.py.bak-20261018-b`. The drive's own `sysadmin` profile remains in that code but nothing here launches it (its port, 8766, belongs to this host's Sysadmin Library).

## 3. Rollback

- Contract tools: delete `~/rag-library`, `~/RFPShred`, `~/contract-tools`, `~/contract-tools-mcp`, `/Applications/Contract Library.app`; restore `~/.lmstudio/mcp.json` from `mcp.json.bak-20261018`.
- Compliance library: delete `/Applications/DIWAI Compliance Library.app` and `~/Library/LaunchAgents/org.diwai.rag-mcp-compliance.plist` (`launchctl bootout gui/501/org.diwai.rag-mcp-compliance`); restore the sysadmin index from `~/diwai/backups/20261018-pre-compliance-split/chroma_db` and move the files from `~/diwai-rag/documents-compliance` back to `documents/2026-10`.
- Sysadmin merge: restore `~/diwai/backups/20261018-pre-library-merge/chroma_db`.
- `config.py`, `webapp/main.py`, `page.html`: `*.bak-20261018` copies beside each.
- `gpt-oss-20b`: Time Machine, or the drive's copy (checksums identical).

## 4. Execution log (2026-10-18)

1. Read the hand-off note and the installer; ran its read-only plan after stopping the running library server (the installer refuses to run beside one).
2. Compared models: Magistral identical; Gemma 4 26B weights identical (only a tokenizer file differs); Devstral differs; gpt-oss identical to the drive's copy, then deleted (owner).
3. Compared embedding files: drive Q4_K_M = LM Studio's bundled Q4_K_M; this host's library uses f16.
4. Inventoried document **names and counts only** and hash-compared sysadmin files; bucketed by the owner's rules.
5. Verified every file on the drive against `MANIFEST.sha256`: **62,431 of 62,431 match** (3 min 8 s).
6. Copied the tools (excluding the drive's sysadmin data), built three offline environments, ran the test suites, pinned the embedding model, registered the tool servers.
7. Backed up the index; stopped the search server (single writer); indexed 87 sysadmin documents and 13 contract documents; backed up again; split the compliance library; created the launcher, the LaunchAgent and the tool-server entry; labelled the pages; restarted the services.

## 5. Observations

1. **USB guard window.** The guard blocked and ejected `AI-TRANSFER` when it was first plugged in (08:06:35–08:06:38, `usb-guard.log`). The owner then switched the guard **off at 09:10:04** for the transfer and it was switched back **on at 10:48:57**: a window of **1 hour 39 minutes** during which any USB storage would have been accepted. `AI-TRANSFER` and the replacement Time Machine drive (`DIWAI-CR-2026-10-14`) were attached in that window; after the guard came back on, `AI-TRANSFER` was ejected again. The monitor writes nothing while the guard is off, so the log cannot show what else was attached in that window; the owner reports only those two drives.
2. **Document contents were not read into the cloud assistant session**, with **one exception to report:** to prove the Contract Library answers, one test question was run through `query.py`, whose output (a generic paragraph about fixed-price and cost-reimbursement contracts, assembled by the local model from the library) was displayed in this session. It contained no solicitation or CUI text that the assistant could identify, but the Mac Studio hand-off note forbids printing library output. Later checks printed only file names, scores and counts.
3. **Misfiled material found at the source.** The drive's "sysadmin" folder held contracting, compliance and private files. It is the likely origin of the earlier misfiling the owner described. The page labels (item 11) address how new files are added; the drive itself was not cleaned.
4. **`AI-TRANSFER` encryption was not checked** before it was ejected. `DIWAI-CR-2026-09-09` requires attached storage that holds CUI-bearing material to be encrypted. **Open: the owner should confirm whether the drive is encrypted, and encrypt or wipe it if not.**
5. **Entity ownership is unsettled for some compliance files.** Files named `TCC_…` and `Rev3_TCC-…`, the `Chapter_…` documents and several SPRS/SSP drafts may describe the other organisation ([DOMAIN.ORG]) rather than [DOMAIN.ORG]. They were placed in the Compliance library by subject only. Open: the owner to say which, if any, must be separated.
6. **Contract Library re-ingest.** Indexing the contract documents folder re-processed 80 files, replacing existing entries (the "delete-before-write" weakness noted in the Studio hand-off). The chunk count rose by only 563, nothing was lost.
7. **Compliance staging.** 23 compliance files from the drive were placed in `~/diwai-rag/documents-compliance` and indexed in the Compliance library; the two executive reports are among them.
8. **gpt-oss-20b** was barred from checks but remained installed until today; the SSP wording ("on disk but barred") is now out of date (SSP amendment 22).
9. **Tool-call confirmation.** `contract-tools` must keep LM Studio's tool-call confirmation switched on and must never be added to its "don't ask" list; the web tools stay off. The first launch with the owner has not yet been done.

## 6. Verification

| # | Check | Result |
|--:|:---|:---|
| 1 | All files on the drive match the manifest (62,431) | **Pass** |
| 2 | Embedding: bundled Q4_K_M identical to the drive's; unsuffixed name proved to resolve to f16, pin applied | **Pass** |
| 3 | RFPShred tests | **Pass** (94 passed, 1 skipped, as predicted) |
| 4 | contract-tools-mcp tests | **Pass** (17 passed) |
| 5 | Contract Library tests | **Pass** (170 passed; the drive predicted 149 + 21 skipped, Ghostscript being present here) |
| 6 | DIWAI library tests after the config and template changes | **Pass** (400 passed) |
| 7 | Contract search returns a sourced answer | **Pass** (see §5.2) |
| 8 | Sysadmin and Compliance searches return the expected sources (pam_faillock → the Rocky man page; Kanidm sshd → the Kanidm example; 800-171A → NIST SP 800-171A) | **Pass** |
| 9 | Each manager answers on its port with its own banner, tab title and drop label (8765, 8766, 8768) | **Pass** (page text checked; appearance on screen not yet confirmed by the owner) |
| 10 | Both search servers running (`launchctl list`) | **Pass** |
| 11 | `gpt-oss-20b` absent from LM Studio's model list (`lms ls`) | **Pass** |
| 12 | LM Studio shows `contract-rag`, `contract-tools`, `diwai-compliance`; contract-tools confirmation prompt appears | **Partly passed 2026-10-18 (owner present).** All four servers listed in LM Studio; a `contract-rag` `search_regulations` call asked for approval before running and the answer cited FAR 15.204-1, Table 15-1 (the owner relayed the source line; the tool-result panel was not inspected). **Still open:** the `contract-tools` confirmation prompt has not been exercised. |
| 13 | SBOM v3.15 published; freshness check 0 unsafe | **See SBOM v3.15** |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — **[SYSTEM-OWNER]** *(entered by Claude at the owner's explicit instruction, 2026-10-18)* |
| **Date** | 10-18-2026 |

---

**Distribution:** Limited to authorized personnel
