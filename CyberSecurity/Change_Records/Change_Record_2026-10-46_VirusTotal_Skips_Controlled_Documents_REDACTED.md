> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — VIRUSTOTAL INTEGRATION SKIPS THE CONTROLLED DOCUMENTS
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-46** |
| **Date** | October 24, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED (§3). Owner approved 2026-10-24.** |
| **System** | services VM: `/var/ossec/integrations/custom-virustotal` |
| **Addresses** | 3.14.2 and 3.14.4 (malicious-code protection working as stated); the "hashes only" statement in `DIWAI-EXT-001` |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Finding

The manager log showed `custom-virustotal` errors ("Unable to run integration", exit status 4) at 09:14 and 10:14 on 2026-10-24, the hourly Mac file-integrity scans. Exit status 4 is "no usable response from VirusTotal". The account is healthy (key valid; 218 of 500 daily and 5 of 240 hourly lookups used; the service answered a test lookup from the VM). The cause is rate: the free API allows about **4 lookups a minute**, and each scan reports a burst of file events (mostly the compliance documents, changed by publishing). The first few succeed and the rest fail.

## 2. Change

The wrapper now exits quietly for any alert whose path is under `/opt/local/nextcloud/data/__groupfolders/`. Everything else is looked up as before. File-integrity alerts are unaffected. Backup `/root/custom-virustotal.bak-20261024-1215-cr46`. The wrapper keeps its `custom-` name, so package upgrades do not overwrite it.

## 3. Verification (`scripts/vt/vm-vt-skip-groupfolders.sh`, output kept beside it)

A synthetic alert for a group-folder path: exit 0, no query. A synthetic alert for another path: queried VirusTotal as normal. The test lookup used the hash of an empty file. The second test may have produced one harmless test event at the manager.

## 4. Limits and follow-up

- Bursts outside the group folders (an app update in `apps`, for example) can still exceed 4 a minute; those lookups fail as before. If it recurs, a short pause between lookups would be the next step.
- Not re-verified end to end on a real event; the next hourly scan with a non-group-folder change will show it. The weekly review step (`DIWAI-SCH-001` W1) reads the integration errors.
- `DIWAI-EXT-001` updated: no lookups for the controlled documents.

## 5. Rollback

`sudo cp -p /root/custom-virustotal.bak-20261024-1215-cr46 /var/ossec/integrations/custom-virustotal && sudo restorecon -v /var/ossec/integrations/custom-virustotal`

---

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | [SYSTEM-OWNER], System Owner / ISSO — approved 2026-10-24 |
