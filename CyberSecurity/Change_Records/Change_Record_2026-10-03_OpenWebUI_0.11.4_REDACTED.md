> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — OPEN WEBUI 0.9.5 → 0.11.4
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-03** |
| **Date opened** | October 3, 2026 |
| **Status** | **APPROVED 10-04-2026** — implemented and verified, all checks pass (§6); signed by the System Owner / ISSO (typed at the owner's direction) |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host only. The VM is not touched |
| **Addresses** | **3.4.3** (change control); **3.14.1** (flaw remediation: the release carries security fixes) |
| **Authority** | Owner direction 2026-10-03 ("open web UI update"), under decision register row 11 (updates are manual, applied by a person) |
| **Builds on** | `DIWAI-CR-2026-10-01` (LM Studio), `DIWAI-CR-2026-10-02` (DIWAI document library) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

Open WebUI 0.11.4 (released 2026-09-21) was offered during `DIWAI-CR-2026-10-02` and not applied. The releases between 0.9.5 and 0.11.4 include security fixes relevant here:

- Knowledge search now applies the list of collections a user may read (0.11.1).
- Knowledge directory traversal prevention, token revocation on logout, and blocking of external resources in diagrams and SVG (0.11.4).
- The API-key permission is enforced on every key endpoint (0.10.0).

They also fix knowledge-search recall where several knowledge bases share one store, which is how this instance stores them (0.11.4).

The changelog was read for breaking changes before the update. Two applied in principle; neither affects this instance:

- **Model IDs containing spaces are rejected** (0.11.4). The three workspace models (`diwai-library`, `log-analysis-agent`, `securemac-compliance-assistant`) have none.
- **Embedding prefix markers** (0.11.0) apply only when a query or content prefix is configured. None is configured here, so the stored vectors and new queries stay consistent.

## 2. Scope

1. Upgrade the `open-webui` package in `/opt/local/open-webui-venv` from 0.9.5 to 0.11.4, with the dependencies pip selects.
2. Let Open WebUI apply its database migrations on first start.
3. No configuration change: same launcher (`/usr/local/sbin/open-webui-start`), same LaunchAgent (`org.diwai.open-webui`), same listener (127.0.0.1:3000).

## 3. Pre-change backup (taken 2026-10-03)

`~/diwai/backups/20261003-pre-owui-0114/`. Open WebUI was stopped before copying, so the database was at rest.

| Item | How | Check |
|:---|:---|:---|
| Data folder `~/.open-webui` (database, vector store, uploads), 750 MB | APFS clone `open-webui-data/` | `PRAGMA integrity_check` = ok |
| Software `/opt/local/open-webui-venv`, 2.2 GB | APFS clone `open-webui-venv/` | — |
| Package list before and after | `pip-freeze-0.9.5.txt`, `pip-freeze-0.11.4.txt` | 260 lines before |
| Baseline: search results, vector counts, assistant answer | `before.json`, `vector-counts-before.txt`, `assistant-before.txt` | — |

## 4. Rollback

Written to `ROLLBACK.txt` in the backup folder. Stop the LaunchAgent, put both clones back in place, and start it again. **The 0.11.x database migrations are one-way: 0.9.5 must never be run against the upgraded database.** Restore the data clone together with the software clone.

## 5. Execution log

1. Baseline taken with Open WebUI 0.9.5 running (§3).
2. 16:56: LaunchAgent stopped (`launchctl bootout`), both clones made, database integrity checked.
3. `pip install open-webui==0.11.4`: 56 packages updated or newly installed, 11 of them new, none removed. Notable: chromadb 1.5.2 → 1.5.9, SQLAlchemy 2.0.48 → 2.0.50, fastapi 0.135.1 → 0.136.3, sentence-transformers 5.4.0 → 5.5.1. `pip check`: no broken requirements.
4. LaunchAgent started (`launchctl bootstrap`). Health 200 after about 21 s. 16 database migrations ran, ending at revision `d4c1a8e37b62`, with no errors.
5. Verification (§6).

## 6. Verification

| Check | Result |
|:---|:---|
| Version reported by `/api/version` | **Pass**: 0.11.4 |
| Listener bound to 127.0.0.1:3000 only | **Pass** |
| Database migrations | **Pass**: 16 applied, no errors in the log |
| Stored vectors unchanged (no re-embedding, no duplication) | **Pass**: 28,364 before and after; the three knowledge collections 4,891 / 1,984 / 129 |
| Retrieval spot check (9 fixed queries, top 5) | **Pass**: 8/9 identical. In the 9th ("VM will not boot LUKS passphrase", runbook collection) the top 3 are unchanged and places 4–5 differ. The new result repeats across runs, so it comes from the new search code (the recall fix in §1), not chance |
| Embedding and search settings survived the settings-storage migration | **Pass**: engine openai → LM Studio 127.0.0.1:1234, model `text-embedding-nomic-embed-text-v1.5@f16`, top_k 15, hybrid search on, reranker top 8 |
| Workspace models and LM Studio models listed | **Pass**: `diwai-library`, `log-analysis-agent`, `securemac-compliance-assistant`, plus the LM Studio models |
| Tool server "DIWAI Library (read-only)" still registered | **Pass**: 127.0.0.1:8767 |
| DIWAI Library assistant answers from the library and cites | **Pass**: patching question answered "monthly; criticals within 72 hours of detection", citing the runbook card, same as before |
| Admin API key still valid (used by the Nextcloud sync) | **Pass** |

## 7. Observations (not changed by this record)

These were already true before the update. They are recorded so they are not lost; each needs its own decision.

1. **`CORS_ALLOW_ORIGIN` is `*`.** Open WebUI warns about this on every start. The listener is loopback-only and reached through nginx, which limits the exposure, but the setting should be narrowed to `https://ai.[DOMAIN.ORG]`.
2. **The session-signing key is short.** The JWT library warns that `WEBUI_SECRET_KEY` is 30 bytes, below the recommended 32. Changing it signs everyone out and makes stored tool-server sign-ins unreadable (they are encrypted with it), so it needs its own change.
3. **That key is stored in plain text** in `/usr/local/sbin/open-webui-start`, which every local account can read (mode 755).
4. **The launcher still sets `OLLAMA_BASE_URL`** to the retired Ollama port 11434. It is harmless while Ollama is off, but stale.

## 8. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — \_[SYSTEM-OWNER] *(typed at the owner's direction, 2026-10-04)* |
| **Date** | 10-04-2026 |

---

**Distribution:** Limited to authorized personnel
