> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — REPAIR LIBRARY v1 (`diwai-repair`)
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-07** |
| **Date opened** | October 4, 2026 |
| **Status** | **APPROVED 10-04-2026** — implemented and verified, all checks pass (§6); signed by the System Owner / ISSO (typed at the owner's direction) |
| **System** | SecureMac — [DOMAIN.ORG] Reference System #2 (RS2) |
| **Hosts affected** | Mac mini host (installed library); VM reached only through the owner's SSH session |
| **Addresses** | **3.4.3** (change control); **3.4.5** (access restrictions for change); **3.14.1** (flaw remediation, with approval) |
| **Authority** | Owner decision 13, option B (2026-10-03): a live problem is fixed by an ISSO-approved repair, which Aider may run after a typed yes. Design approved 2026-10-03; build 2026-10-03/04 |
| **Builds on** | `DIWAI-CR-2026-10-04` (Aider leash), `DIWAI-CR-2026-10-06` (VM sudo asks for the password) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

Decision 13 lets Aider run code only when it comes from a trusted source and a person approves it first. This library makes "approved" something code can check. Each repair is a small program: check, back up, make one change, verify, undo. It runs only if the ISSO's YubiKey signed its exact contents.

## 2. Scope

| Part | Where |
|:---|:---|
| Runner, two repairs, shared code (Python standard library only, `/usr/bin/python3` 3.9.6) | Installed root-owned in `/usr/local/lib/diwai-repair/`; command `/usr/local/bin/diwai-repair` |
| Run records and backups | `/var/db/diwai-repair/runs/` (root only, mode 700) |
| Source, tests, design, plan | `~/diwai-rag` (git), branch `repair-library` |

**Approval:**
1. The ISSO's YubiKey signs a list of SHA-256 fingerprints of every file a repair runs, with `fido2-assert`, needing the PIN and a touch every time.
2. Every run checks the signature with root-owned tools only (`/usr/bin/python3`, `/usr/bin/openssl`): the signature, that it covers this exact list, that it was made for repair approvals, and that the key recorded both the PIN and the touch.
3. A repair changed after approval cannot run, nor can its undo, until it is approved again.

**Approver key:** P-256, created on the YubiKey on 2026-10-04 (standard YubiKey 5, not the FIPS model; FIPS validation is not required for an approval, see the design §2). On first install it had to sign a fresh challenge before it was trusted. Its public key SHA-256 is `42ca390a6a3235075d5630de900e2647bc3513a190a482be23017bed424e104f`.

**v1 repairs:**

| Repair | Host | Runbook card |
|:---|:---|:---|
| `owui-cors-any-origin`: Open WebUI lets only `https://ai.[DOMAIN.ORG]` read its answers | Mac | `OPEN_WEBUI_ACCEPTS_ANY_ORIGIN` |
| `wazuh-ruleset-missing`: restores Wazuh's custom-rules block and proves a custom rule fires | VM | `WAZUH_CUSTOM_RULES_NOT_LOADED` |

**Safeguards a person sees:**
- the runner shows the planned change and asks for the exact word `yes`, typed at a keyboard (not piped);
- `undo` also asks;
- Mac steps ask for the Mac password;
- a VM repair asks for the VM password once, which the VM forgets afterwards;
- the runner signs `sudo` out when it ends;
- spoken prompt: "Type your YubiKey PIN, then touch the key when it blinks."

## 3. Testing

- **Tests:** 96 unit tests for the library, test-first; 314 in the whole project, all passing.
- **Live signing check:** the real YubiKey signature verified, a one-byte change was rejected, and the PIN and touch flags were set.
- **Independent review** of the whole branch before installing. It found 1 critical and 7 important problems, all fixed with a test that failed first:
  - undo could be pointed at a forged run folder;
  - unchecked repair names;
  - a cached `sudo` sign-in;
  - a yes that could be piped in;
  - the approver key trusted without proof;
  - install of uncommitted code;
  - a needless undo when nothing had changed;
  - symlinks published.
- **Found during the build and fixed:**
  - backups would have corrupted carriage returns;
  - the Open WebUI key would have appeared in the process list;
  - VM file reads echoed `ossec.conf`;
  - the VM password prompt was invisible.
- **Found and handled separately:** passwordless `sudo` on the VM (→ `DIWAI-CR-2026-10-06`).

## 4. Rollback

1. Run `sudo rm -rf /usr/local/lib/diwai-repair /usr/local/bin/diwai-repair`. The run records in `/var/db/diwai-repair/runs/` are kept as evidence.
2. To restore Open WebUI's setting, first run `diwai-repair undo 20261004-085625-owui-cors-any-origin` (§5).

## 5. Execution log (2026-10-04)

1. **08:45 install** from commit `9dea450`, after the approver key proved itself (PIN + touch).
2. **08:50 approvals:** both repairs approved with the YubiKey. One approval attempt failed when the PIN was typed before its prompt appeared. That cost one try, reset by the next correct PIN.
3. **`owui-cors-any-origin`, live:**
   - run `20261004-085245`: done;
   - `undo`, after a typed yes: original restored, and a foreign origin was echoed again;
   - run again `20261004-085625`: done. **Final state: fixed.**
4. **`wazuh-ruleset-missing`, live:** `check` reports "Not present: nothing to do" (the block has been present since 2026-09-13), so it declined correctly. Owner decision: the decline, plus 13 unit tests covering apply, configuration-test failure, restart failure, no alert, undo and a planted instruction, stand as the v1 evidence. The block was not broken on purpose.
5. **The VM password prompt was invisible** (a display bug). Fixed in commit `70fd4ef`, reinstalled, and both repairs **re-approved**. The runner refused both until then, as designed. The fix was confirmed live: the prompt shows.

## 6. Verification

| Check | Result |
|:---|:---|
| Installed files root-owned; owner's account cannot write | **Pass** (`touch` refused) |
| Unapproved repair refused, even for `check` | **Pass** (exit 2) |
| Changed code refused until re-approved | **Pass** ("has changed since it was approved", live after reinstall) |
| Approver key fingerprint matches the YubiKey enrollment | **Pass** |
| Open WebUI repair: foreign site refused, own site allowed, launcher owner/mode kept, warning gone, library assistant answers | **Pass** |
| Open WebUI undo restores the original | **Pass** |
| Wazuh repair declines when the block is present | **Pass** |
| VM password asked once, prompt visible | **Pass** |

## 7. Observations and known limits

1. **Plain `aider` and anything running as the owner** can still run any command the owner approves at a prompt. The library guarantees only that `diwai-repair` runs approved code.
2. **The 8 minor review points were fixed on 2026-10-04** (commit `06826fd`), each with a test that failed first; 325 tests pass. The library was reinstalled (with `tools/repair-install`) and both repairs re-approved with the YubiKey. The fixes:
   - `undo` re-checks and says whether the original problem is back;
   - Ctrl-C at a yes prompt is a cancel (exit 2);
   - a refused password at the lock is no longer reported as "another repair is running", and `status` shows a lock left by a killed run and how to clear it;
   - the approval now covers `bin/diwai-repair` too;
   - VM settings are written through a copy and swapped in (atomic; owner and mode kept);
   - `fido2-assert` and `libfido2` are fingerprinted at install (`fido-tools.sha256`), and `approve` refuses if either has changed, so a Homebrew upgrade of libfido2 needs one reinstall;
   - the command runs the real interpreter `/Library/Developer/CommandLineTools/usr/bin/python3`, so `DEVELOPER_DIR` can no longer redirect it (confirmed live);
   - a literal `*` CORS answer counts as "any site allowed".
3. **Wazuh apply and undo** have not been exercised on the live VM (owner decision, §5).
4. **The two runbook cards** were approved without change by the ISSO on 2026-10-04 (review record in `runbooks/README.md`). The approval method is recorded as decision register row 14 (owner, 2026-10-04).
5. **During testing,** 3 characters of the YubiKey FIDO2 PIN appeared in the build conversation. **Owner decision 2026-10-04: PIN not changed.** The risk is low in this test environment: the PIN is useless without the physical key, and 8 wrong tries lock it.

## 8. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — \_[SYSTEM-OWNER] *(typed at the owner's direction, 2026-10-04)* |
| **Date** | 10-04-2026 |

---

**Distribution:** Limited to authorized personnel
