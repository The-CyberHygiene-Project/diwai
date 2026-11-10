> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# DIWAI-EV-MAC-2026-08-01 — Technical Scrub: Mac Host

**System:** [DOMAIN.ORG] SecureMac Reference System
**Component:** [USERNAME]s-Mac-mini.local (securemac / ai / cloud.[DOMAIN.ORG]), macOS **26.5.1** build 25F80
**Evidence type:** Technical control verification (Phase 2)
**Collected by:** [SYSTEM-OWNER] (system operator), 2026-08-01 15:10 MDT
**Method:** Test / Examine — live interrogation + fresh mSCP audit (`--check`, audit-only)
**Raw capture:** `evidence/mac-scrub-raw-20260801-151027.txt`

---

## 1. Controls verified as operating

| Control | Observed | Requirement |
|:---|:---|:---|
| FileVault | **On** | 3.13.16 |
| System Integrity Protection | **enabled** | 3.4.2 |
| Gatekeeper | assessments enabled; override disallowed | 3.4.8, 3.14.2 |
| Application firewall | enabled, **stealth mode on** | 3.13.1 |
| pf | enabled, uptime 22h44m, 222 state entries | 3.13.1 |
| USBGuard | `org.diwai.usb-guard` **running** (`/usr/local/sbin/usb-guard-monitor`) | 3.8.7, 3.8.8 |
| Wazuh agent | 5 daemons running; **reconnected to [LAN-IP-REDACTED]:1514 at 14:30:20** after the manager was restored | 3.3.1, 3.14.6 |
| TLS certificate | `CN=[DOMAIN.ORG]`, Let's Encrypt YE2, valid to **Sep 9 2026** | 3.13.11 |
| Audit (BSM) | `flags:lo,aa,ad,-ex,-fm,-fr,-fw`, `policy:ahlt,argv`, **`expire-after:7d`** | 3.3.1 |
| Nextcloud CUI repo | 32.0.11.1, not in maintenance; **TOTP 2FA enabled**; `admin_audit`, `files_accesscontrol`, `files_automatedtagging`, `twofactor_backupcodes` all installed | 3.1.1, 3.5.3 |
| SSH hardening (mSCP) | FIPS-compliant client and server; timeouts enforced (900s) | 3.13.11 |

The Wazuh agent reconnection at 14:30:20 independently confirms the Phase 0
manager restoration worked end to end.

## 2. mSCP compliance audit — FRESH RESULT

Baseline `diwai_phase1`, 15 configuration profiles installed (mSCP-generated,
2026-04-02, installed 2026-04-24). Audit script run with `--check` only.

```
PASSED: 130   FAILED: 5   96.30 percent compliant
```

Results written to `/Library/Preferences/org.diwai_phase1.audit.plist`
(136 rules recorded).

**This supersedes the documented figure of 126/134 (94%).** Current posture is
**130/135, 96.30%** — better than documented, but the documented figure could
not have been current (see finding M1).

### The five failing rules

| Rule | Concern |
|:---|:---|
| `os_firewall_default_deny_require` | Firewall is **not default-deny** — see M3 |
| `audit_settings_failure_notify` | No notification on audit subsystem failure (3.3.4) |
| `os_home_folders_secure` | Home folder permissions not hardened (3.1.1) |
| `os_recovery_lock_enable` | Firmware recovery lock not enabled (3.4.2) |
| `os_unlock_active_user_session_disable` | Active user session may be unlocked by another user (3.1.10) |

**POA&M-003 currently describes "8 failing rules" and must be rewritten against
this list of 5.** Note `audit_settings_failure_notify` pairs with the VM audit
retention finding (`DIWAI-EV-VM-2026-08-01` F-2026-08-19) — audit failures are
neither retained long nor announced on either host.

## 3. FINDING M1 — the weekly mSCP scan has not been running

`/usr/local/bin/run-mSCP-scan.sh` is a **zero-byte file** (0 bytes, dated
2026-06-12 17:29). The `org.diwai.mSCP-scan` LaunchDaemon (Sundays 03:00) has
been executing an empty script. `/var/log/mscp-scan.log` is likewise 0 bytes,
last touched 2026-06-07. Newest published mSCP artifacts predate this at
**2026-04-24**.

The SSP states: *"weekly automated scan, results published to compliance
dashboard (POA&M-003 tracks the 8 failing rules)"*. The scan was not running and
the published figure was ~3.5 months stale.

The working audit script exists and functions — it is at
`~/Documents/SecureMac Project Docs/USB Reference/mSCP_diwai_phase1_compliance.sh`
(574 KB, generated 2026-04-10) and produced the results in §2 on demand. Only
the wrapper that the LaunchDaemon calls is empty.

**Pattern:** this is the third control found believed-running but inert
(Wazuh manager 2026-07-31; Wazuh Mac agent, closed POA&M-009; this). The common
factor is that **no control verifies that controls are running**.

**Remediation:** populate the wrapper to invoke the real script with `--check`,
write results to `/var/log/mscp-scan.log`, and publish. Not done unilaterally —
it re-arms an automated job.

## 4. FINDING M3 — latent internet exposure (characterised precisely)

The Mac holds **four public, routable addresses** on `en0`:

```
en0: [WAN-IP-REDACTED], .146, .147, .149   (netmask 0xfffffff8 = /29)
default gateway: [WAN-IP-REDACTED] via en0
```

pf explicitly permits inbound from **any** source:

```
pass in on en0 inet proto tcp from any to [WAN-IP-REDACTED] port = 80  flags S/SA keep state
pass in on en0 inet proto tcp from any to [WAN-IP-REDACTED] port = 443 flags S/SA keep state
```

**What is NOT true:** CUI services are not currently exposed. Verified:

- Nothing is bound to any `[WAN-IP-REDACTED]` address — nginx binds `[LAN-IP-REDACTED]` and
  `127.0.0.1` only.
- Connection tests to `[WAN-IP-REDACTED]` on 443, 80 and 22 are all **refused**.
- pf ends with `block drop all`; only 80/443 are passed inbound on `en0`.

**What is true:** a standing `pass in from any` rule sits in front of a host
that stores CUI, with no service behind it. Six services bind **all**
interfaces — `*.22`, `*.5000`, `*.7000`, `*.8080`, `*.8081` (Magistral AI),
`*.54303` — and are kept off the internet **solely** by that single pf ruleset.
Any future change that binds a service to `0.0.0.0:443`, or any pf failure or
flush, makes it internet-reachable immediately with no other misconfiguration
required.

That mSCP independently fails `os_firewall_default_deny_require` on this host
corroborates the concern from a second direction.

**Severity: medium — latent, not active.** Recommendation: remove the two
inbound rules if nothing is intended to be published; bind `*`-bound services
to specific interfaces (defence in depth rather than relying on one ruleset);
and reconcile the SSP.

## 5. FINDING M4 — SSP boundary description is inaccurate

SSP §3.2 describes: *"pf firewall — stateful packet inspection, **NAT**, inbound
port restrictions / WAN (en0): restricted inbound; **NAT outbound**"*.

There is no NAT for these addresses — `en0` carries four **public** IPs with a
public default gateway. The host is directly on the internet, not behind a
translating boundary. The SSP's characterisation should be corrected in v2.15,
and Figure 3.3 (`RS2_Network_Schematic`) re-checked against it.

Related drift: `en1` is now **[HOME-LAN-REDACTED]**; prior documentation records it as
[LAN-IP-REDACTED] (NetGear hotspot uplink). The network documentation should be
re-verified as a whole.

## 6. FINDING M5 — pending OS update

`softwareupdate --list` reports **macOS Tahoe 26.6** (3.8 GB, `Recommended: YES`,
`Action: restart`) pending. Relevant to 3.14.1. Note `system_settings_
softwareupdate_current` passes in mSCP, so the baseline does not treat this as
non-compliant, but an uninstalled recommended update is a flaw-remediation item.
Scheduling is an owner decision (requires a restart of the CUI host).

## 7. Accounts observed

Local: `[USERNAME]`, `sysadmin`, `root`, `wazuh`, plus `daemon`/`nobody`.
`admin` group membership: **root, sysadmin, [USERNAME]** — two interactive
administrative accounts. `sysadmin` is the documented break-glass account (used
in the 2026-04-15 and 2026-05-15 YubiKey lockout recoveries). Expected, but
should be explicitly documented in the SSP account inventory for 3.1.1/3.1.5.

## 8. Method note — a limitation in this collection

The capture truncated the mSCP output at `tail -60`, so only 59 of 136 rule
results appear in the raw file. The failure list in §2 was recovered from
`/Library/Preferences/org.diwai_phase1.audit.plist`, which is authoritative.
Future collections should retain full scan output.

## 9. Verification commands

```
sudo fdesetup status; csrutil status; spctl --status
sudo pfctl -s rules
ifconfig en0 | grep 'inet '
sudo /Library/Ossec/bin/wazuh-control status
/bin/zsh "~/Documents/SecureMac Project Docs/USB Reference/mSCP_diwai_phase1_compliance.sh" --stats
python3 -c "import plistlib;d=plistlib.load(open('/Library/Preferences/org.diwai_phase1.audit.plist','rb'));print([k for k,v in d.items() if v.get('finding')])"
```
