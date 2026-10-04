> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Local-AI Tooling: Test Results (October 2026)

**System:** [DOMAIN.ORG] SecureMac Reference System #2 · **As of:** 2026-10-04 · **Owner/ISSO:** [SYSTEM-OWNER]

All results below come from the change records in `CyberSecurity/Change_Records/`, where each one is set out in full with its evidence, rollback and approval. This page summarises them.

## What was built (Oct 3–4, 2026)

| Change record | What it did |
|:---|:---|
| CR-2026-10-01 | LM Studio became the single local model server (loopback only); Ollama, mlx-lm and LiteLLM retired |
| CR-2026-10-02 | DIWAI document library: an offline, read-only search library for the local AI (no write tool) |
| CR-2026-10-03 | Open WebUI 0.9.5 → 0.11.4 (security fixes) |
| CR-2026-10-04 | Aider on a leash: a launcher that refuses project-level settings that could run code without approval |
| CR-2026-10-05 | Retired Ollama models removed (90 GB) |
| CR-2026-10-06 | VM `sudo` asks for the password again (it had been passwordless) |
| CR-2026-10-07 | Repair library v1: repairs run only if the ISSO approved their exact code with a YubiKey (PIN + touch) |
| CR-2026-10-08 | Magistral Small 2509 back in service through LM Studio for general questions |

## Test results

| Area | Result |
|:---|:---|
| Automated tests, whole project | **325 pass** (repair library 107, document library and runbook cards the rest) |
| Approach | Test-first: each test was seen to fail before the code that makes it pass was written |
| Independent code review of the repair library (before install) | 1 critical and 7 important findings, **all fixed**, each with a test that failed first; 8 minor findings, **all fixed** in a follow-up batch |
| Critical finding, for the record | `undo` accepted any folder as a "run", which would have let an approved repair's undo write unapproved content into a root-owned setting with no typed yes. Fixed: undo accepts only real run names, checks the record matches, and asks for a typed yes |
| Approval signatures | Real YubiKey signature verified with root-owned tools; a one-byte change to the signed data is rejected; the key's own flags show both PIN and touch |
| Changed code refused until re-approved | Shown live twice: after each reinstall, the runner refused both repairs until they were approved again |
| Open WebUI repair, live | Run → undo → run again. Final state: other web sites can no longer read Open WebUI's answers; its own site still works; the document-library assistant still answers |
| Wazuh repair, live | Correctly reports "nothing to do" (the rules block is present); apply and undo proven by 13 unit tests (owner decision: not broken on purpose on the live system) |
| Aider leash, live (8 checks against real Aider and the local model) | **8/8 pass**: a planted project settings file is refused; a command the model proposes never runs without a typed yes; drafting still works |
| Aider as a drafter (6 runs) | Wrote only the file it was given; ignored a planted "ignore your instructions" line 3/3; **but none of 6 cards cited a fitting 800-171A objective**, so its drafts need ISSO review, which decision 13 requires |
| Local model consistency on drift checks | 6/9 → **30/30** after one prompt rule was made explicit |
| Open WebUI upgrade | 8 of 9 retrieval spot checks identical; the 9th differs only in places 4–5, consistent with the release's search-recall fix; stored vectors unchanged |

## Problems found along the way (and fixed)

- Backups would have corrupted carriage returns: found by a test, fixed by handling backups as raw bytes.
- The Open WebUI key would have been visible in the process list: fixed.
- A VM file read echoed a settings file to the screen: fixed.
- The VM's password prompt was invisible: fixed and confirmed live.
- The VM had passwordless `sudo` since April, never recorded: fixed under CR-2026-10-06.

## Owner decisions recorded in this period

Decision register rows 13 (Aider on a leash, option B: may run an approved repair after a typed yes) and 14 (repairs run only with an ISSO YubiKey approval over their exact contents).
