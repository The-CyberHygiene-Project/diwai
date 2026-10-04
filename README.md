# diwai
The SecureMac Project Repository: Do It With AI

Public, redacted documentation for the **[DOMAIN.ORG] SecureMac Reference System #2**: a small-business NIST SP 800-171 reference system built on a Mac mini (host, firewall, local AI) and a Rocky Linux FIPS virtual server, documented as it is built. Identifiers (owner, organization, domain, IP addresses, ISP, contact details, serial numbers) are replaced with placeholders. The authoritative, unredacted copies are held in the system's access-controlled store.

## What is here

| Folder | Contents |
|:---|:---|
| `CyberSecurity/SSP/` | System Security Plan (current version only) |
| `CyberSecurity/POAM/` | Plan of Action and Milestones (current version only) |
| `CyberSecurity/Software_Inventory/` | Software Bill of Materials (current version only) |
| `CyberSecurity/Change_Records/` | Change records for the local-AI tooling (October 2026) |
| `CyberSecurity/Testing/` | Test results for that tooling |
| `Policies/`, `Procedures/` | The system's policies and procedures |
| `Training/`, `Assessments/` | Training material and earlier assessments |

## Status (2026-10-04)

- **System Security Plan** v2.18 (amendment 17), **POA&M** v1.32, **SBOM** v3.11.
- **Local AI, fully offline-capable:**
  - LM Studio is the single model server;
  - an offline, read-only document library for the AI;
  - Aider (coding assistant) runs on a leash;
  - a **repair library** in which a fix runs only if the ISSO approved its exact code with a hardware key (YubiKey, PIN + touch), shows the planned change, needs a typed yes, keeps a backup and can be undone.
- See `CyberSecurity/Testing/AI_Tooling_Test_Results_2026-10.md` for the evidence.
