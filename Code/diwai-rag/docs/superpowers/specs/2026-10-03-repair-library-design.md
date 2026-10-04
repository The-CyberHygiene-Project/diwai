# DIWAI repair library: design

*2026-10-03. Agreed with the owner/ISSO section by section in chat; this document records it for review.*

## 1. Purpose

A live problem on this system is fixed by an **ISSO-approved repair**: a small program that checks the problem is really there, backs up what it will change, makes one change, verifies the result, and can undo it. This implements owner decision 13 (option B): Aider drafts repairs on the build side and never edits a live configuration file itself; it may run an **approved** repair only after a person types yes to the exact command. The library makes "approved" something code can check, not just a promise.

**Success means:** only repairs the ISSO approved with the YubiKey can run; a repair changed after approval cannot run; every run leaves a backup, a record and a working undo; and the two v1 repairs work end to end on the live system, including undo.

## 2. Decisions taken (owner, 2026-10-03)

| Question | Decision |
|:---|:---|
| Where repairs run | **Mac and VM from v1.** VM repairs go through the owner's interactive SSH session, so they work only while the owner is logged in |
| How approval is recorded | **Fingerprint + approval list:** approval covers the repair's exact contents; any later edit makes it unrunnable until re-approved |
| What proves the ISSO approved | **YubiKey signature, PIN + touch** (as on the Mac Studio). The YubiKey is out of the owner's line of sight, so the touch request is **spoken aloud** and shown in large text; a missed touch times out harmlessly and can be retried |
| v1 repairs | **A** Open WebUI cross-site setting (Mac) and **C** Wazuh custom-rules block (VM) |
| Implementation approach | **Python, inside `~/diwai-rag`**, one runner; Ansible reconsidered at about a dozen repairs |

The key is a standard YubiKey 5 (FIDO 2.0), not the FIPS Nano. Its FIDO2 application was reset and a new PIN set by the owner on 2026-10-03. FIPS validation is not required here: 3.13.11 applies to cryptography protecting CUI confidentiality, and this signature proves a person's approval.

## 3. Parts and trust boundaries

| Part | Where | Who can change it |
|:---|:---|:---|
| Repair drafts, tests | `~/diwai-rag/repairs/`, `~/diwai-rag/tests/` | The owner's account, so Aider too |
| Installed runner, repairs, shared helpers | `/usr/local/lib/diwai-repair/` (root-owned) | Only an install step that needs the administrator password |
| Command | `/usr/local/bin/diwai-repair` (root-owned) → the installed runner | Same |
| YubiKey public key | `/usr/local/lib/diwai-repair/approver.pem` + `approver.credid` (root-owned; set on first install after a YubiKey proof) | Same |
| Approvals | `/usr/local/lib/diwai-repair/approvals/<repair>.manifest` + `.assertion` | Written by `approve`, which needs the YubiKey (PIN + touch) and the administrator password |
| Run records and backups | `/var/db/diwai-repair/runs/<timestamp>-<repair>/` (root-only, mode 700) | The runner via `sudo` |

- The runner and repairs use **only the Mac's built-in Python (`/usr/bin/python3`) and its standard library**. They never run from `~/diwai-rag/venv`, which the owner's account (and so Aider) can modify.
- The runner runs **as the owner's account**, never wholly as root. A step that needs administrator rights calls `sudo` for that one command, so the person types the password. VM steps run through the owner's shared session (`~/.ssh/cm/`): a VM repair asks the VM password once (`ssh -tt services sudo -v`, kept at most 2 minutes, DIWAI-CR-2026-10-06), quiet steps use `sudo -n`, and `sudo -K` ends it.
- Aider can propose `diwai-repair run <repair>`; Aider's own "Run shell command?" yes starts it. **The runner then asks its own yes** after showing the exact change its check found, because that plan exists only once the check has run.

## 4. A repair

One Python file per repair in `repairs/`, defining:

- `ID`, `TITLE`, `HOST` (`mac` or `vm`), `CARD` (the runbook card it fixes)
- `check(ctx)` → `None` if the problem is absent, else a finding with the plan in plain words. Read-only.
- `backup(ctx)` → copies what `apply` will change into the run folder.
- `apply(ctx)` → one change.
- `verify(ctx)` → proves the change worked.
- `undo(ctx)` → restores from the run folder.

`ctx` gives the run folder, a `sudo` runner for the Mac, an SSH runner for the VM, and logging. Anything a check reads from the system is **data**: shown to the person, never acted on as an instruction.

## 5. The runner: `diwai-repair`

| Command | Does |
|:---|:---|
| `list` | Installed repairs, each with its approval state |
| `check <repair>` | Read-only check; prints the finding or "not present" |
| `run <repair>` | Approval check → `check` → show plan → typed yes → `backup` → `apply` → `verify` → record. A failure in `apply` or `verify` triggers `undo`, then `check` again to confirm the system is back |
| `undo <run>` | Restore from that run's backup, then re-check |
| `status` | Recent runs, including any left unfinished |
| `approve <repair>` | ISSO only: fingerprint (SHA-256 of the installed repair file plus the shared helpers) signed with the YubiKey. Spoken prompt: "Touch the YubiKey now" |
| `install` | Copies drafts from `~/diwai-rag/repairs/` into the root-owned folder (administrator password). Installing a changed repair invalidates its approval |

**As built (2026-10-04):** OpenSSH could not be used. Apple's `ssh-keygen` has no FIDO support, and this YubiKey (FIDO 2.0) rejects OpenSSH's `verify-required`. Instead, an approval is a FIDO2 assertion made with `fido2-assert -G -p -v` (touch + PIN, every time) over the SHA-256 of the manifest, using a credential created with `fido2-cred` (rp `diwai-repair`). Each run checks it with root-owned tools only (`/usr/bin/python3`, `/usr/bin/openssl`): the rp hash, the client data hash = SHA-256(manifest), the UP and UV flags, and the ECDSA P-256 signature. On first install the approver key must prove it is the YubiKey by signing a fresh challenge. Install takes the committed tree only (`git archive HEAD`), and approve shows that commit.

## 6. v1 repairs

### `owui-cors-any-origin` (Mac) — card `OPEN_WEBUI_ACCEPTS_ANY_ORIGIN`

Today Open WebUI echoes back **any** requesting site and marks the answer as allowed to carry credentials (checked 2026-10-03), because `CORS_ALLOW_ORIGIN` is not set and defaults to `*`.

- **check:** request with `Origin: http://evil.example`; problem present if the reply allows it.
- **backup:** `/usr/local/sbin/open-webui-start` (it holds the session key; the run folder is root-only).
- **apply:** add `export CORS_ALLOW_ORIGIN=https://ai.[DOMAIN.ORG]` to the launcher; restart the LaunchAgent.
- **verify:** health 200 within 60 s; a foreign origin is not allowed; `https://ai.[DOMAIN.ORG]` is allowed; the "CORS … '*'" startup warning is gone; the DIWAI Library assistant still answers.
- **undo:** restore the launcher; restart.
- **say no if:** someone is in the middle of a conversation in Open WebUI (the restart interrupts it).

### `wazuh-ruleset-missing` (VM) — new card `WAZUH_CUSTOM_RULES_NOT_LOADED`

Before 2026-09-13 `ossec.conf` had no `<ruleset>` block, so every custom rule (YARA 100200–209, audit 100220, incident 100230) was silently never loaded.

- **check:** read `/var/ossec/etc/ossec.conf`; problem present if the `<ruleset>` block does not include the custom rules and decoders folders.
- **backup:** `ossec.conf` on the VM, plus a copy in the Mac run folder.
- **apply:** restore the approved `<ruleset>` block stored with the repair; run Wazuh's configuration test; restart only if it passes.
- **verify:** configuration test passes **and** a tagged test event makes a custom rule fire. The configuration test alone is not proof (lesson of 2026-09-13).
- **undo:** restore `ossec.conf`; restart Wazuh.
- **needs:** the owner's SSH session open, and the owner's VM `sudo` password.

The exact block, rule to fire and test event are confirmed against the live VM during the build.

## 7. Failure handling

- **Refusals:** a plain reason, nothing changed, when:
  - the approval is missing, invalid or signed by another key;
  - the repair is not installed;
  - `allowed_signers` is missing;
  - the VM session is not open;
  - the check finds no problem (the decline case);
  - another run holds the lock.
- **Part-way failure:** automatic undo, then re-check; the run is recorded "failed, rolled back". If undo fails, the runner stops, states the system's state plainly and prints the manual restore steps. It never guesses.
- **Interruption** (Ctrl-C, lost SSH session): the run is marked "interrupted"; `status` lists it, and `undo` still works.

## 8. Testing

- **Unit, test-first.** Every runner rule, with stand-ins: fake files, a fake `sudo`, a fake SSH, and a throwaway software signing key in place of the YubiKey.
- **Signatures.** An approved repair runs; a repair edited after approval is refused; a wrong signer is refused; a missing approval is refused.
- **Per repair.** Problem present (runs); already fixed (declines); planted instruction in what it reads (ignored); forced failure part-way (rolls back cleanly).
- **Live acceptance, with the owner present.** Each repair runs for real once, including the YubiKey approval, the typed yes and the passwords. It is then undone and run again, so undo is proven live.

## 9. Records

- **A change record** for the build.
- **SBOM update.**
- **Cards:** `OPEN_WEBUI_ACCEPTS_ANY_ORIGIN` written from the repair's code (README rule 2); `WAZUH_CUSTOM_RULES_NOT_LOADED` new. Both with `default_repair` set to the repair ID, after ISSO review.
- **Decision register:** a row recording the approval method, if the owner wants it.

## 10. Out of scope for v1

More repairs (the mSCP regression rules are next); Ansible; a repair that runs without the owner present; an allow-list check inside Aider itself (the runner is the enforcement point).
