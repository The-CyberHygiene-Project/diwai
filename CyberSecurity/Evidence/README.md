# Evidence notes (redacted examples)

These are six redacted evidence notes from the reference system and, in `../Assessment_Records/`, the redacted
session record of the August 2026 sweep. They show what an evidence note looks like and how the sweep was recorded.
They are **examples, not the whole evidence set**: the reference system's evidence folder holds about a hundred files
(notes, raw output, scan reports, images), most of which are not published here.

## Naming

`DIWAI-EV-<AREA>-<YYYY-MM-DD>[-X]_<Title>.md` (a `CUI_` prefix in the private store is dropped here, and `_REDACTED`
is added). Areas seen: AU audit, CM configuration, MP media, PS personnel, SC communications, VM server, MAC host.
A note opens with the system, the evidence type, who collected it, the method and the requirements it supports.
Raw output is kept beside the note in the private store and is not published.

## Scripts and method

The scripts that produced or checked this kind of evidence, and a plain-language account of how evidence is
collected and how the SSP and POA&M are updated, are in the
[Automated_Compliance](https://github.com/The-CyberHygiene-Project/Automated_Compliance) repository under `evidence/`.

## The examples

| Note | What it shows |
|---|---|
| `DIWAI-EV-CM-2026-08-02_Citation_Sweep` | A sweep of every citation in the document set and the checker's own false-positive defect |
| `DIWAI-EV-VM-2026-08-01_Technical_Scrub`, `DIWAI-EV-MAC-2026-08-01_Technical_Scrub` | Host-level evidence for the August sweep |
| `DIWAI-EV-AU-2026-10-23-C_Audit_Correlation_Exercise` | One synthetic event traced across sources |
| `DIWAI-EV-MP-2026-10-23_Media_Sanitization_Exercise` | A drill on disposable images |
| `DIWAI-EV-PS-2026-10-23_Personnel_Action_Drill` | A personnel-action drill |
