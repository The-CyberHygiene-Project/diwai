> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# Admin Portal: overview

Date: 2026-11-04. Status: describes the portal as it stands after the Control-Health Alerts page (change record DIWAI-CR-2026-10-65).

## What it is

The SecureMac Admin Portal is the administrator's start page for the reference system. It is a small set of static pages and a few PHP endpoints served by Apache from the virtual server. It is not a general web application: it links to the system's other tools (monitoring dashboard, file store, webmail, local AI chat) and holds the administrator's routine duties, a compliance summary, and now the control-health alerts.

## Access

- One blanket rule for the whole site: the administrator signs in with a directory (LDAP over TLS) account and must be in the administrators group. There are no per-page exceptions; only the site icon files are open.
- No account outside that group can read any page. An unauthenticated request to any page or endpoint returns 401.
- The portal does not hold its own accounts and stores no passwords.

## Pages

| Page | What it does |
|:---|:---|
| Home | Status tiles and a list of action cards linking to the system's tools |
| Compliance | The compliance summary |
| Policies & Docs | Index of policies, procedures and reports; the documents themselves live in the file store |
| Routine Duties | Daily, weekly and monthly checks: what is due, and a place to record that it was done |
| Alerts | Current results of the control-health monitor, failing checks first, with an Acknowledge button and optional note (design: `Alerts_Page_Design_Spec`; change record: `Change_Record_2026-10-65`) |

Navigation is a tab bar (Home, Compliance, Policies & Docs, Alerts) repeated at the top of each page. Routine Duties and Alerts are also reachable from cards on the Home page.

## The Alerts page in one paragraph

The control-health monitor runs every 15 minutes and writes its latest report to one world-readable file. The Alerts page reads that file and shows each check. Only `ok` counts as passing; any other status is shown as failing, word for word. Acknowledging a failing check records who, when, what was seen and a note in an append-only log, and copies the line to the system log so the monitoring system can collect it. An acknowledgment lapses after 24 hours or when the check's detail text changes. Acknowledging changes nothing in the monitor, which keeps sending its own reminders. The page cannot repair anything and holds no repair button.

## Safeguards built into the endpoint

- Writes only by POST with a per-session token; any other method cannot write.
- The user name comes from the authenticated session and the time from the server's clock; the browser supplies only which check and an optional note.
- Only a check that is failing right now can be acknowledged. If the report is missing or malformed the page says so and offers nothing to acknowledge.
- Notes are length-limited, stripped of control characters, stored as data and shown as text only.
- If the log cannot be written, the acknowledgment is refused and nothing is shown as recorded.
- Known gap, stated in the change record: if a check recovers and fails again within 24 hours with identical text, it still shows as acknowledged, because the monitor keeps no history.

## How changes are made

- The live files on the server are the authoritative copy. A working copy on the administrator's Mac drifts and is not trusted; before any edit the live file is pulled and compared.
- Every modified file is backed up first with a dated suffix (for example `index.html.bak-20261104-tab`).
- Installation is by a short script that the owner reads and runs with elevated rights; it backs up, copies, sets owner, mode and SELinux label, and writes what it did to a file.
- New files follow the same owner, mode and label as existing portal files. The system's application allow-listing and SELinux policy stayed unchanged and did not block the new endpoint; why the allow-listing lets the web server run new script files was not determined, and no trust change was made.
- Each change has a change record. Unit tests for the endpoint's logic run on a development machine; they do not run on the server because the allow-listing stops an interactive user running script files there.

## What the portal deliberately does not do

- It does not run commands on the system, and it does not approve or run repairs. Repairs stay at the console with a hardware-key approval (see the Automated_Compliance design note on diagnosis and repair).
- It does not notify anyone. A failing check is visible only when someone opens the Alerts page; a badge showing the count of unacknowledged failures has been proposed and not built.
