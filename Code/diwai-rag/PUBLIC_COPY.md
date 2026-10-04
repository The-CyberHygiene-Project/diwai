# diwai-rag — public reference copy

> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

Snapshot of the `diagnosis-loop` branch, 2026-10-04 (no git history). Because names and addresses are replaced, some tests that check them will not pass as published.

- **Document library** (`ingest.py`, `mcp_server.py`, `webapp/`): read-only search over the system's own documents for a local AI model.
- **Runbook cards** (`runbooks/`): plain-words problem descriptions, ISSO-reviewed; `DECISIONS.md` holds the owner's decision register.
- **Repair library** (`repairkit/`, `repairs/`, `bin/diwai-repair`): runs only repairs the ISSO approved with a YubiKey (PIN + touch, signature over the exact code).
- **Diagnosis loop** (`diagnose/`, `bin/diwai-diagnose`): read-only; turns monitor results into findings and decision forms; names the approved repair, never runs one.
- **Evaluations** (`evals/`): live model checks, including planted-instruction tests. The diagnosis check's current honest result is 12 of 15 cases (see the change record).

Left out on purpose: the live-system facts file for the diagnosis loop (it names a current, unpatched finding).
