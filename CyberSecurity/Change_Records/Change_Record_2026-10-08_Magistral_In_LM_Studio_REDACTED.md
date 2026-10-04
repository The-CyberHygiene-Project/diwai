> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MAGISTRAL BACK IN SERVICE THROUGH LM STUDIO
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-08** |
| **Date opened** | October 4, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED — all checks pass (§6); owner approval signature pending** |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host only |
| **Addresses** | **3.4.3** (change control); **3.4.1** (baseline inventory kept accurate: SBOM v3.11) |
| **Authority** | Owner decision 2026-10-04: keep Magistral for non-coding tasks and general questions, and make it usable |
| **Builds on** | `DIWAI-CR-2026-10-01` (LM Studio the single runtime; mlx-lm and Magistral retired) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

The owner kept `/opt/local/models/Magistral-Small-2509-MLX-4bit` (13 GB), which may be better than Devstral for non-coding tasks and general questions. Since `DIWAI-CR-2026-10-01` nothing could run it: its `mlx-lm` server is retired. LM Studio runs MLX models directly, so the model goes there rather than bringing `mlx-lm` back.

## 2. Scope

1. **Verify the files** against the publisher, `lmstudio-community/Magistral-Small-2509-MLX-4bit` (base `mistralai/Magistral-Small-2509`, Apache 2.0, revision `bb18789f03d9`). The 5 large files were checked by SHA-256 against Hugging Face's values; the 9 small files were downloaded and compared byte for byte. All 14 files on disk match.
2. **Copy into LM Studio:** an APFS clone (no extra disk space) to `~/.lmstudio/models/lmstudio-community/Magistral-Small-2509-MLX-4bit`. The original in `/opt/local/models` is unchanged.
3. **LM Studio** serves it as `magistral-small-2509-mlx`, loaded on demand like the other models.
4. **Open WebUI:** a new workspace assistant `magistral-general` ("Magistral (general)"), with `reasoning_tags` `[THINK]` / `[/THINK]` so the model's thinking is folded away, and temperature 0.3.
5. **No change** to `mlx-lm`: it stays retired.

## 3. Rollback

Delete the LM Studio copy folder and the Open WebUI assistant (`DELETE /api/v1/models/model/delete?id=magistral-general`, or in Workspace → Models). The original model is untouched.

## 4. Execution log

1. Verification: 5/5 SHA-256 OK and 9/9 byte-identical.
2. Clone made; `lms ls --json` lists `magistral-small-2509-mlx`. Loaded in 6.2 s (13.15 GiB, 125,696-token context).
3. Direct API test: "why does a pressure cooker cook faster?" was answered correctly after the `[THINK]` section.
4. Open WebUI's model list needed one refresh (`/api/models?refresh=true`) before the new assistant could find the base model. Test through Open WebUI: "what is a haiku?" was answered correctly.

## 5. Observations

1. **Thinking in the reply.** Magistral writes its reasoning in `[THINK]…[/THINK]` inside the reply. Open WebUI does not recognise those markers by default, hence the per-assistant `reasoning_tags`. Folding happens in the chat page; a direct API call still returns the markers.
2. **Not for drift checks or the library:** the decision register (row 12) keeps Devstral as the primary model for those.

## 6. Verification

| Check | Result |
|:---|:---|
| Files match the publisher (14/14) | **Pass** |
| LM Studio lists and loads the model | **Pass** |
| Direct LM Studio answer | **Pass** |
| Open WebUI assistant answers | **Pass** |
| Original model files unchanged; no extra disk used | **Pass** |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — \______________________ *(pending)* |
| **Date** | \______________________ |

---

**Distribution:** Limited to authorized personnel
