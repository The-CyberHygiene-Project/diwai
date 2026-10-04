> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — AI MODEL SERVER: OLLAMA + MLX-LM → LM STUDIO
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-01** |
| **Date opened** | October 3, 2026 |
| **Status** | **COMPLETE** — reboot verification passed 2026-10-03 (host restarted 13:35; owner entered the VM's LUKS passphrase) |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host only. The VM is not touched |
| **Addresses** | **3.4.3** (change control), **3.4.6/3.4.7** (least functionality: one model runtime, loopback only) |
| **Authority** | Owner direction 2026-10-03: reconfigure the AI stack to mirror the Mac Studio's documented setup ("Local AI Stack and RAG Tools — Reference for RS#2"); plan approved the same day |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

Testing on the Mac Studio (RS#3 pathfinder) showed that its documented stack avoided problems seen on this host. That stack is LM Studio as the **single** model runtime, loopback only, with no web tools. Running the same model in two runtimes had filled swap.

RS2 currently runs two runtimes: Ollama (`org.diwai.ollama`) and mlx-lm (`org.diwai.magistral`, installed but not auto-started). This change makes LM Studio the only one.

This is Phase 1 of a re-scoped project: AI infrastructure first, then compliance tests and runbooks (positive, negative, and remediation with human approval).

## 2. Scope

1. Install LM Studio and bind its server to 127.0.0.1:1234.
2. Turn off prompt logging, plugins, LM Link and in-app auto-update.
3. Install the models devstral-small-2-2512, gpt-oss-20b and nomic-embed-text v1.5.
4. Repoint Open WebUI chat and embeddings to LM Studio, and re-embed its three knowledge collections.
5. Retire `org.diwai.ollama` and `org.diwai.magistral`. Their plists are renamed, and binaries and models stay on disk for rollback.
6. Repoint `~/diwai/drift/drift-run.py` and the LiteLLM shim.

## 3. Pre-change backup (taken 2026-10-03)

`~/diwai/backups/20261003-pre-lmstudio/`:

| Item | How | Check |
|:---|:---|:---|
| `webui.db` | `sqlite3 .backup` | `integrity_check` ok; 3 knowledge collections |
| `vector_db/` | APFS clone | 3,791 files, matching the source; `chroma.sqlite3` unchanged since 04:15 |
| LaunchAgents | copy | `org.diwai.ollama`, `org.diwai.magistral`, `org.diwai.open-webui` |
| Start scripts | copy | `open-webui-start`, `magistral-start` |
| LiteLLM | APFS clone | `~/diwai/litellm/` |
| State | `rollback-reference.txt` | `ollama list` / `ps`, listening ports |

## 4. Rollback

1. Rename each `*.plist.disabled` back to `.plist`, then `launchctl bootstrap gui/$(id -u)` it.
2. Restore `webui.db` and `vector_db/` from the backup.
3. Restore `open-webui-start`.
4. Restart `org.diwai.open-webui`.

## 5. Execution log

### 5.1 LM Studio installed and locked down (2026-10-03)
- `brew install --cask lm-studio` installed **0.4.25+1**: Notarized Developer ID, Element Labs Inc (`D65G88RHWN`).
- It bootstrapped headless from one background launch; the GUI was never needed. It runs as `LM Studio --run-as-service`.
- Settings changed. The originals are kept as `*.orig-20261003`.

| File | Setting | Default → set |
|:---|:---|:---|
| `.internal/http-server-config.json` | `logSensitiveData` | **true → false** |
| | `autoStartOnLaunch` | false → true |
| | `networkInterface` / `cors` / `port` | 127.0.0.1 / false / 1234 (confirmed) |
| `settings.json` | `developer.allowDevelopmentPlugins` | true → false |
| | `developer.autoUpdateExtensionPacks` (runtimes) | true → false |
| | `autoLoadBundledLLM` | true → false |
| | `enableLocalService` | false → true |
| | `defaultContextLength` | 8192 → 32768 |

- **Login start:** new LaunchAgent `org.diwai.lmstudio` (RunAtLoad) runs `lms server start --port 1234 --bind 127.0.0.1`. Loaded, exit 0.
- **Listening:** `127.0.0.1:1234` (API) and `127.0.0.1:41343` (internal); nothing on other interfaces.
- **Bundled plugins:** `lmstudio/js-code-sandbox` and `lmstudio/rag-v1` are present but pinned in no chat. `mcp.json` is empty. LM Link is not signed in (`credentials` type `none`).
- **Residual risk:** the app has no setting to stop it **checking for and staging its own updates**. A staged update installs only on restart, so the version is to be checked after every restart.

### 5.2 Models
- `text-embedding-nomic-embed-text-v1.5` is bundled with LM Studio (84 MB, Q4_K_M).
- `mistralai/devstral-small-2-2512` resolved to `mlx-community/Devstral-Small-2-24B-Instruct-2512-4bit` (15.1 GB).
- `openai/gpt-oss-20b` resolved to MXFP4 (12.1 GB).
- `nomic-embed-text-v1.5` **f16** GGUF was added (274 MB); see 5.3 for why.

### 5.3 Open WebUI embeddings
- **Measured:** Ollama's `nomic-embed-text` and LM Studio's nomic v1.5 give **cosine 0.930–0.948** on identical text. They are not interchangeable, so **every** vector must be regenerated: the 3 knowledge bases **and** the 948 per-file collections (21,357 vectors), which Open WebUI's reindex does not touch.
- **Before** (Ollama embedder):
  - SecureMac Project: 1,984 vectors
  - CyberHygiene Project History: 4,891
  - SecureMac Runbooks: 129
  - Retrieval spot check: `retrieval/before.json`
- `POST /api/v1/retrieval/embedding/update` set the engine to openai, `http://127.0.0.1:1234/v1`, `text-embedding-nomic-embed-text-v1.5`, batch size 32.
- **First attempt, reversed:** Open WebUI's `POST /api/v1/knowledge/reindex` returned `true`, but it **duplicated chunks**: Runbooks went from 129 to 258 vectors with 129 distinct texts, and the other two were also re-split. That store is kept as `vector_db.after-reindex-DUPLICATED`.
- **Second attempt, superseded:** the original store was restored and all 952 collections (28,453 vectors) were re-embedded in place with the bundled Q4_K_M model. Counts matched, but the spot check showed the same top result in only 4 of 9 queries. That store is kept as `vector_db.reembedded-q4-SUPERSEDED`.
- **Root cause:** quantization. LM Studio with **nomic f16** gives cosine **1.0000** against Ollama's vectors, while Q4_K_M gives 0.93.
- **Final state:**
  - embedder set to `text-embedding-nomic-embed-text-v1.5@f16`
  - **the original, untouched vector store restored** (byte-identical to the backup)
  - **9 of 9 spot-check queries return identical top-5 results**, and still 9 of 9 after Ollama was stopped
- **Observation:** opening the store with chromadb applied 89 logged chunks for two per-file collections whose processing failed on 2026-06-17. Those collections had been empty and now hold their own file's text. Knowledge-base counts are unchanged.

### 5.4 Open WebUI chat
- The OpenAI connection now points at `http://127.0.0.1:1234/v1`; the dead `:8081` (Magistral) connection is gone, and the Ollama API is disabled.
- `open-webui-start` (root-owned) is **unchanged**: its `OLLAMA_BASE_URL` is overridden by the saved configuration, so no sudo was needed.
- Custom assistants `securemac-compliance-assistant` and `log-analysis-agent` were rebased from Ollama `mistral:latest` to `mistralai/devstral-small-2-2512`, with params unchanged. Their original definitions are exported to `owui-custom-models-export.json`.
- End-to-end chat works. The pre-existing `'NoneType' … startswith` error (also logged 2026-06-13) occurs only on API calls made without a `chat_id`.
- **Observation for the record:** both assistants answered "what does 3.4.6 require" **wrongly** (3.4.6 is least functionality).

### 5.5 Ollama and mlx-lm retired
- `launchctl bootout` was run on `org.diwai.ollama` and `org.diwai.magistral`, and both plists were renamed `*.disabled`.
- Nothing listens on 11434, 8081 or 4000. Listeners are 1234 (LM Studio) and 3000 (Open WebUI), both on 127.0.0.1.
- Swap is 0 bytes with the VM, LM Studio and Devstral all resident.

### 5.6 Tools repointed
- **`claude-local.sh`:** LM Studio serves the **Anthropic Messages API natively** (`/v1/messages`), so Claude Code now points straight at `127.0.0.1:1234` and the LiteLLM shim is out of the path. Smoke test: "local-ok".
- **`drift-run.py`:**
  - moved to LM Studio with a strict `json_schema` response format
  - Devstral as the default model, temperature 0.2
  - `<DATA>`-delimited inputs with `<` escaped (the idm-assistant contract)
  - a prompt-size cap
- **New `--model-tests`**, run on synthetic fixtures only, so no CUI is sent:

| Model | injected instruction | decline when undecidable | flag clear drift |
|:---|:---|:---|:---|
| devstral-small-2-2512 | 3/3 pass | 2/3 pass | 1/3 pass |
| gpt-oss-20b | **0/3: marked a mismatched version SATISFIED, as instructed by text inside the evidence** | 0/3 | not run |

  **gpt-oss-20b is barred from drift checks.** Devstral's remaining failures are inconsistency, not obedience to injected text. They are an open item for the drift library, not for this change.
- **RC-002** (SBOM vs LM Studio inventory; new collector `lmstudio_inventory.py`):
  - against SBOM v3.4, VALID; it under-reported, marking everything UNVERIFIED, which is what led to the "flag clear drift" test
  - against **SBOM v3.5, 7 of 7 SATISFIED, VALID**, with every citation resolving
- RC-001's Ollama collector now **fails closed** ("connection refused"), which is the intended behaviour.

## 6. Verification

| Check | Result |
|:---|:---|
| 1234 bound to 127.0.0.1 only; 11434/8081/4000 absent | **Pass** |
| Open WebUI retrieval identical before/after (9 queries × top-5) | **Pass**: 9/9 |
| Open WebUI chat end-to-end on LM Studio | **Pass** |
| Prompt text not retained | **Pass**: `logSensitiveData` false; after ~40 test prompts, 0 hits for test strings in `server-logs/`; `api-prediction-history` empty (0 B); no conversations |
| Claude Code → LM Studio direct | **Pass** |
| drift-run self-test (16 fabrication cases) | **Pass** |
| RC-002 on SBOM v3.5 | **Pass**: VALID, 7/7 SATISFIED |
| SBOM v3.5 published, `doc-freshness` IN SYNC | **Pass** |
| **Reboot: LM Studio serves `/v1/models` with no GUI; Open WebUI works** | **Pass** (2026-10-03, host up since 13:35): `post-reboot-check.sh` 16/16 PASS, same as the 13:32 pre-reboot baseline; LaunchAgents loaded, ports loopback-only, retired ports 11434/8081/4000 silent, library 126 documents, VM web service 200. Open WebUI assistant "DIWAI Library" asked how often patches are applied: Devstral called the library search tool, and the answer (monthly; criticals within 72 h of detection, DIWAI-PR-001 v1.2 §6/§6.1) was correct and cited |
| Version check after restart (app self-update residual) | **Pass**: LM Studio still 0.4.25+1 after the restart |
