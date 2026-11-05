> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — ADMIN PORTAL: CONTROL-HEALTH ALERTS PAGE
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-65** |
| **Date** | November 4, 2026 |
| **Status** | **IMPLEMENTED. Page verified to load for an administrator; four negative tests still to run (§6). Owner approval pending (§7).** |
| **System** | SecureMac Admin Portal, `securemac.[DOMAIN.ORG]` on services.[DOMAIN.ORG] (VM), DocumentRoot `/var/www/securemac` |
| **Addresses** | **3.3.1** (audit trail of administrator actions); **3.3.2** (actions traceable to a named user); **3.14.6** (monitoring is only useful if reviewed); **3.4.3** (change control) |
| **Authority** | Owner request 2026-11-04; spec and plan in `~/diwai/drafts/2026-11-04-admin-portal-alerts-page-*.md` |
| **Related** | `DIWAI-CR-2026-10-64` (previous record in sequence); the control-health monitor (not changed) |
| **Classification** | Controlled Unclassified Information (CUI) |

---

## 1. Reason

The control-health monitor (`diwai-control-health`, every 15 minutes) detects failures, but its mail goes to a VM mailbox that is rarely read. The Admin Portal had no place to see the monitor's results or to record that a failure had been seen. The owner asked for a separate portal page for this.

## 2. What changed

1. **New files in `/var/www/securemac/`** (owner and group `apache`, mode 644, SELinux `httpd_sys_content_t`):
   - `alerts.html`: the page. Failing checks first, each with an Acknowledge button and an optional note; passing checks collapsed; warnings if the report is more than 30 minutes old, unreadable, or the ledger has unreadable lines.
   - `alerts.php`: the endpoint (JSON). Takes the user name from the authenticated `REMOTE_USER` and the time from the server clock.
   - `alerts_lib.php`: the logic (report reading, ledger, acknowledgment rules).
2. **Edited `index.html`:** one new card, "Control-Health Alerts", linking to `alerts.html`. Backup: `index.html.bak-20261104-alerts`. The edit was made to the **live** copy; the Mac source had drifted and was refreshed from the live file afterwards (Mac backups `~/diwai/securemac-site/index.html.bak-20261104-alerts` and `.bak-20261104-tab`).
   - **Alerts tab (second edit, installed 15:29):** a fourth tab, "Alerts", was added to the tab bar after "Policies & Docs" on `index.html`, `compliance.html` and `docs/index.html`; `alerts.html` carries the same bar with its own tab highlighted (it replaces the earlier "Admin Portal" link). Each of the four files was backed up first as `<name>.bak-20261104-tab`. Each existing file was overwritten in place, so owner, mode and SELinux label were kept (checked in the installer listing). The home-page card remains, so the page is reachable both ways.
3. **New ledger** `/var/log/diwai/alert-acks.log` (apache, mode 640, `httpd_sys_rw_content_t`), append-only, one JSON line per acknowledgment.
4. **Installed** with `sudo` by the owner: `~/alerts-stage/install-alerts.sh` at 12:30 (page, endpoint, card) and `~/alerts-stage-tab/install-tab.sh` at 15:29 (tab); each wrote a file listing as its output.
5. **Not changed:** the monitor, its timer and `latest.json`; `duties.php`; the other tabs' content; Apache configuration; `fapolicyd` rules and trust database; Wazuh rules.

## 3. How it behaves

- **Access:** the whole portal sits under one LDAP rule (`cn=admins`); the new files add no exception. Unauthenticated requests are refused with 401.
- **What counts as failing:** `ok` is the only passing status. Any other value (`fail`, `warn`, or one added later) is shown as failing, verbatim.
- **Acknowledge means record only.** It writes who, when, the check, the status and detail seen, and an optional note (500 characters, control characters removed). The monitor still sends its 24-hour reminders.
- **Writes:** POST only, with a per-session CSRF token. Only a check that is currently failing in `latest.json` can be acknowledged. If `latest.json` is unreadable or malformed, the page shows an error and offers no Acknowledge button. If the ledger cannot be written, the acknowledgment is refused.
- **Expiry:** an acknowledgment stops counting after 24 hours, or when the check's detail text changes. Future-dated ledger lines are ignored.
- **Audit copy:** each recorded acknowledgment is also written to syslog as program `diwai-alert-ack`, so Wazuh's log collection can see it. **No Wazuh rule alerts on it** (owner decision: collect only).
- **Row identity:** several checks share an id (3, 5, 5b, 5c, 6, 7, 10 at the time of writing; the report has 35 checks). A row is identified by id, name and its position among rows with the same id and name.

## 4. Rollback

To remove the tab only: restore each `<name>.bak-20261104-tab` over `index.html`, `compliance.html`, `docs/index.html` and `alerts.html`. To remove the page entirely: restore `index.html.bak-20261104-alerts` over `index.html` and `compliance.html.bak-20261104-tab` / `docs/index.html.bak-20261104-tab` over their files; delete `alerts.html`, `alerts.php`, `alerts_lib.php`. The ledger may stay (it is evidence) or be moved aside. Nothing else depends on these files.

## 5. Known limits and observations

1. **Recover-then-refail gap.** If a check recovers and fails again within 24 hours with identical detail text, it still shows as acknowledged. The monitor keeps no history, so the page cannot see the recovery. Closing it needs a background recorder, which was left out of scope.
2. **Acknowledgments are not alerts.** Because no Wazuh rule watches the syslog line, nobody is notified of an acknowledgment. The ledger is for audit, not for alerting.
3. **A failing check could not be acknowledged on the live page**, because no check was failing at test time (35 passing). That path is covered by the unit tests only (§6, row 6).
4. **Row order across runs.** The repeated ids appeared grouped in the one report read (§6, row 9). Whether their order is stable from run to run has not yet been compared across two reports. If the monitor reorders rows, an acknowledgment could attach to the wrong row of a repeated id until it expires or the detail changes.
5. **`fapolicyd` and new PHP files.** The trust database has no entry for the portal files, yet Apache ran the new `alerts.php`. Why `fapolicyd` allows Apache to run PHP here was not determined. No trust change was made. If a later change (for example a content change under trust) blocks it, the page shows "Could not load alerts".
6. **Unit tests run on the Mac, not on the VM.** `fapolicyd` stops an interactive user running PHP files on the VM (PHP 8.2); the tests ran on the Mac (PHP 8.3). The deployed code ran under the VM's PHP 8.2 only through Apache, which loaded the page.
7. **Phone-width layout** has not been checked on a real phone.
8. **Leftovers on the VM, not yet cleaned:** `~/alerts-preflight` (contains an old credential line copied from a backup configuration file), `~/alerts-build/tests/run.php`, and the preflight scripts. Owner decision pending on deleting them.

## 6. Verification

| # | Check | Result |
|--:|:---|:---|
| 1 | Unit tests (42 checks: report parsing, ledger, concurrency, CSRF, expiry, hostile note, status vocabulary) | **Pass**, 0 failed (Mac, PHP 8.3.36) |
| 2 | Files present with the intended owner, mode and SELinux label | **Pass** (installer listing) |
| 3 | No login: `alerts.html`, `alerts.php`, `index.html` | **Pass**, 401 for each |
| 4 | Administrator login: page loads, shows report time, monitor version, 0 failing, 35 passing | **Pass** (owner's screenshot, 13:49 MST) |
| 5 | Apache runs the new PHP under `fapolicyd` and SELinux | **Pass** (the page's data call succeeded) |
| 6 | Acknowledge a failing check on the live page; ledger line and syslog line appear | **Not tested live** (nothing failing); covered by unit tests only |
| 7 | POST without or with a wrong CSRF token refused (403), ledger unchanged | **Not yet run live** (unit tests pass) |
| 8 | GET cannot write to the ledger | **Not yet run live** (unit test passes) |
| 9 | Repeated ids keep a stable order between reports | **Partly:** grouped in one report; two-report comparison pending |
| 10 | A login outside `cn=admins` is refused | **Not tested** (no such account is available) |
| 11a | Tab installed on four pages; no login still gives 401 on all of them | **Pass** (installer listing; 401 from `curl`) |
| 11b | Tab shows and works when signed in; Alerts tab highlighted on its own page | **Not yet confirmed** (owner to look) |
| 11 | Monitor, timer and `latest.json` untouched | **Pass** (none of them was edited by this work; the monitor's report was still current at 13:45) |

## 7. Approval

| | |
|:---|:---|
| **Prepared by** | Claude (AI assistant), for the system owner |
| **Approved** | *Pending — [SYSTEM-OWNER], System Owner / ISSO* |
| **Date** | |

---

**Distribution:** Limited to authorized personnel
