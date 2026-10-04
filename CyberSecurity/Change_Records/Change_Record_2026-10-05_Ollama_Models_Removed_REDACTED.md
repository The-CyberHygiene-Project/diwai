> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — RETIRED OLLAMA MODELS REMOVED
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-05** |
| **Date opened** | October 3, 2026 |
| **Status** | **APPROVED 10-04-2026** — implemented and verified, all checks pass (§6); signed by the System Owner / ISSO (typed at the owner's direction) |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host only. The VM is not touched |
| **Addresses** | **3.4.3** (change control); **3.4.6/3.4.7** (least functionality: unused software removed) |
| **Authority** | Owner direction 2026-10-03: "let's clean up the old Ollama models" |
| **Builds on** | `DIWAI-CR-2026-10-01` (Ollama retired; its models kept on disk for rollback) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

`DIWAI-CR-2026-10-01` made LM Studio the single model runtime and kept Ollama's models on disk in case of rollback. That change is complete, and its reboot test passed. The models are no longer needed; they took 90 GB.

## 2. Scope

Delete `~/.ollama/models` (7 models, 26 files):

| Model | Size |
|:---|---:|
| gemma4:31b-it-q8_0 | 33.8 GB |
| gemma4:26b-a4b-it-q8_0 | 28.1 GB |
| gemma4:26b-a4b-it-qat | 15.6 GB |
| devstral:latest | 14.3 GB |
| devstral-agent:latest | 14.3 GB (same weights as devstral) |
| mistral:latest | 4.4 GB |
| nomic-embed-text:latest | 0.3 GB |

**Not changed:** the Ollama program (`/opt/homebrew/bin/ollama`), its disabled launcher, the `~/.ollama` key pair, and the retired Magistral MLX model (13 GB, `/opt/local/models`).

## 3. Before the change

- **Nothing in use:** no Ollama process was running, nothing listened on port 11434, and the launcher was disabled. Every remaining mention of Ollama in an active script is a comment, or the post-reboot check confirming that port 11434 stays silent.
- **Restore source:** Time Machine includes `~/.ollama/models`; the latest backup is `2026-10-03-164817`.
- **Inventory kept:** model names, file hashes and sizes, and the manifests, in `~/diwai/backups/20261003-ollama-models-removed/`.

## 4. Rollback

Restore `~/.ollama/models` from the Time Machine backup `2026-10-03-164817`. Each model can also be downloaded again with `ollama pull <name>` while the system still has internet access.

## 5. Execution log

1. Inventory written and manifests copied (§3).
2. `~/.ollama/models` deleted.
3. Free space did not change at once. Time Machine's local snapshots still hold the deleted files; macOS removes those snapshots after about 24 hours, and the 90 GB is freed then. The snapshots were deliberately left in place as a second restore path.

## 6. Verification

| Check | Result |
|:---|:---|
| `~/.ollama/models` gone; key pair and cache untouched | **Pass** |
| LM Studio, Open WebUI and the library unaffected | **Pass** (none used Ollama since `DIWAI-CR-2026-10-01`) |
| SBOM v3.9 records the removal; doc-freshness IN SYNC | **Pass** |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — \_[SYSTEM-OWNER] *(typed at the owner's direction, 2026-10-04)* |
| **Date** | 10-04-2026 |

---

**Distribution:** Limited to authorized personnel
