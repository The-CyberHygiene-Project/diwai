> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Admin Portal: Control-Health Alerts Page — Design Spec

Date: 2026-11-04
Status: APPROVED by owner 2026-11-04 (no code written, nothing deployed)
Host: services.[DOMAIN.ORG] (VM), portal `securemac.[DOMAIN.ORG]`, DocumentRoot `/var/www/securemac`

## 1. Purpose

The control-health monitor (`diwai-control-health`, every 15 minutes, 25 checks) detects
failures correctly, but its mail lands in a VM Maildir that is rarely read. The portal
needs a page where the administrator can see the monitor's current results and record
that a failing check has been seen.

Success: the administrator opens one portal page, sees which checks fail, acknowledges
them with an optional note, and every acknowledgment is recorded in an audit trail that
Wazuh can see.

## 2. Scope

In scope
- Control-health monitor results only (the contents of `latest.json`).
- Viewing current check results; acknowledging a failing check ("record only").
- An append-only acknowledgment ledger and a syslog copy for Wazuh.

Out of scope
- Wazuh alerts, backup, certificate and patch alerts, and any other source.
- Silencing or changing the monitor's mail reminders. The monitor is not modified.
- History of past alerts, including the unread mail in the Maildir.
- A background recorder that detects recover-then-re-fail (see 5.3, the known gap).

## 3. Decisions already made by the owner

- Scope is the control-health monitor only (2026-11-04).
- Acknowledge means "record only" (2026-11-04): who, when, optional note. The monitor
  keeps sending its 24-hour reminders.

## 4. Data source

`/var/lib/diwai-control-health/latest.json`: root-owned, world-readable, rewritten every
15 minutes. Shape: `host`, `time`, `monitor_version`, `checks[]`, each with `id`, `name`,
`status`, `detail`. Several checks share an id (for example 3, 5, 5b appear more than
once), so a row's identity is `id` + `name` + its position among entries with the same
`id` and `name`. The page does not hard-code the monitor's status vocabulary (resolved
O-1): `ok` is the only passing value, every other value is treated as failing and
shown verbatim, so a status the monitor adds later appears without a page change. The
status value is stored in each ledger line, so the audit trail shows what was seen.

## 5. Design

### 5.1 Page (`alerts.html` + `alerts.php`)

- Shows report time and monitor version at the top, and a warning if `latest.json` is
  older than 30 minutes (monitor stalled) or unreadable.
- Failing checks first, each with name, detail, and either an Acknowledge control or the
  existing acknowledgment (who, when, note). Passing checks follow, collapsed.
- `alerts.php` serves the data as JSON to `alerts.html` and accepts acknowledgments.
  Pattern follows the existing `duties.html/duties.php` conventions (not its code, which
  could not be read).

### 5.2 Acknowledgment

- POST only, with a CSRF token tied to the session; any other method cannot write.
- The server takes the user name from the authenticated `REMOTE_USER` and the time from
  its own clock. The client supplies only the check identity and an optional note
  (length-limited, stored as data, escaped on output).
- Only a check that is currently failing in `latest.json` can be acknowledged.
- Access is limited to the same LDAP group as the rest of the portal (`cn=admins`).

### 5.3 Expiry

An acknowledgment stops counting when either:
1. 24 hours have passed (equal to the monitor's reminder interval), or
2. the check's `detail` text differs from the text recorded at acknowledgment.

Known gap: if a check recovers and fails again within 24 hours with identical detail
text, it stays shown as acknowledged. The monitor holds no history, so the page cannot
see the intervening recovery. Closing this needs a background recorder, which is
deliberately out of scope.

### 5.4 Storage and audit trail

- One append-only ledger: `/var/log/diwai/alert-acks.log`, one JSON object per line
  (`ts`, `user`, `check_id`, `check_name`, `detail`, `note`, `report_time`).
- Current acknowledgment state is computed from the ledger on each request. No second
  state file exists, so none can drift.
- Each acknowledgment is also written to syslog with program name `diwai-alert-ack`, so
  the existing Wazuh log collection sees it. Whether a Wazuh rule alerts on it is a
  separate decision (open item O-2).
- The ledger is never edited or deleted by the page. `/var/log/diwai` is apache-owned
  (0750) and is already written by `ir-log.php`, so permissions and SELinux context have
  a working precedent.

### 5.5 Failure handling

- `latest.json` missing, unreadable or malformed: the page says so plainly and offers no
  acknowledge controls. It does not fall back to old data.
- Ledger unwritable: the acknowledgment is refused with an error; nothing is shown as
  acknowledged unless it was recorded.
- Malformed ledger line: skipped, and the page shows a count of skipped lines.

## 6. Deployment

1. Pull the live `index.html` from the VM first. The live copy is canonical; the Mac
   copy drifts silently and is gitignored.
2. Diff live against the Mac source before editing anything.
3. Make a dated backup of every file modified (`.bak-<stamp>`).
4. Add `alerts.html` and `alerts.php` as new files; add one link card to the live
   `index.html`.
5. Copy the deployed `index.html` back over the Mac source after deployment.
6. The monitor, its timer and `latest.json` are not touched.

## 7. Testing

Negative tests come first, in line with the evidence-strict scoring rule:
- No credentials returns 401.
- A valid login outside `cn=admins` is denied.
- A GET request cannot write to the ledger.
- A missing, wrong or reused CSRF token is rejected.
- Acknowledging a passing check is rejected.
- Acknowledgment lapses after 24 hours, and lapses when the detail text changes.
- Unwritable ledger: acknowledgment refused, nothing shown as recorded.
- Malformed `latest.json`: no controls, clear error.
- An unknown status value (for example `warn`) is shown as failing, verbatim.
- Each acknowledgment appears in the ledger and in syslog, and reaches Wazuh.

Tests run against a copy of `latest.json` (a test-only data path), never by faking a
failure in the real monitor. The test hook must not exist in the deployed page.

## 8. Paperwork

- One change record in the usual numbering, placed in Nextcloud with
  `doc-freshness.py accept`.
- SBOM unchanged (no new software). SSP: add a note beside the existing alert-review and
  audit-review controls.
- Cross-reference sweep (`xref-sweep.py`) after any version bump.

## 9. Open items

- O-1: RESOLVED 2026-11-04 by design: no status list is needed (see section 4). The
  plan should still check, against a real `latest.json`, that repeated ids keep a
  stable order from run to run.
- O-2: RESOLVED 2026-11-04: collect only. Acknowledgments go to the ledger and syslog;
  no Wazuh rule alerts on them. A rule can be added later as a separate change.
- O-3: `duties.php` could not be read (Operation not permitted). If it is protected on
  purpose, the new files must not rely on copying its protection scheme.
