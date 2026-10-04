default_repair: none
decisions:
objectives: 3.4.3[d], 3.12.4[h]
user_sees: The document check warns that your copy of a compliance document is older than the official one.
means: Editing or publishing the old copy would silently wipe out newer work in the official copy.
evidence: The official copy has changed since this copy was last brought up to date.
repair: No automatic repair. Do not edit or publish this copy. Bring it up to date from the official copy first, then make the change.
if_wrong: Publishing an old copy over the official one erases every change made since.
rollback: An overwritten document can be restored from backup, but only if someone notices it happened.
say_no_if: Someone proposes copying the old version over the official one to make the warning go away.
---
Status as of 2026-10-03. Canonical store: Nextcloud CUI groupfolder; working copies in ~/diwai/assessment-2026-08/. Tool: `scripts/doc-freshness.py` (status / check <file> / adopt <file> / publish <file> / accept <file>), then `occ groupfolders:scan 1` after a publish. STALE and DIVERGED are unsafe; the tool fails closed if canonical cannot be read. POA&M-048 (detection implemented 2026-08-03, enforcement pending). On 2026-10-03 two working copies showed STALE: CUI_Policy_Acknowledgment_2026-08-04.md and CUI_Session_Record_2026-07-30_to_2026-08-04.md. The SSP and POA&M versions pin each other; repoint live pointers on a version bump.
