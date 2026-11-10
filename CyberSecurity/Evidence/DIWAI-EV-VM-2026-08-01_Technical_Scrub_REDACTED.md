> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# DIWAI-EV-VM-2026-08-01 — Technical Scrub: services.[DOMAIN.ORG]

**System:** [DOMAIN.ORG] SecureMac Reference System
**Component:** services.[DOMAIN.ORG] ([LAN-IP-REDACTED]), Rocky Linux 9.7 aarch64
**Evidence type:** Technical control verification (Phase 2)
**Collected by:** [SYSTEM-OWNER] (system operator), 2026-08-01
**Method:** Test / Examine (live system interrogation + fresh SCAP scan)

---

## 1. Controls verified as operating

| Control area | Observed | Requirement |
|:---|:---|:---|
| FIPS mode | `/proc/sys/crypto/fips_enabled = 1` | 3.13.11 |
| SELinux | **Enforcing** | 3.1.2, 3.4.2 |
| Application control | `fapolicyd` active | 3.4.8 |
| IDS | `suricata` active | 3.14.6 |
| Audit daemon | `auditd` active, `backlog_limit 8192`, **`lost 0`** | 3.3.1 |
| Malware (SI-3 substitute) | `yara_rules.xml` present; `yara-fullscan.timer` **enabled** | 3.14.2 |
| Host firewall | `firewalld` active | 3.13.1 |
| Time sync | `chronyd` active; system time 0.4 µs off NTP | 3.3.7 |
| Disk encryption | LUKS2 + LVM; all volumes mounted post-reboot | 3.13.16 |
| Kernel currency | `5.14.0-687.31.1` running (patched 2026-08-01) | 3.14.1 |
| Cockpit | `disabled`, not listening | 3.4.6 (least functionality) |

Demo-period configuration delta confirmed **still in place and as documented**:
`/etc/my.cnf.d/99-skip-name-resolve.cnf` present; 4 [DOMAIN.ORG] entries in
`/etc/hosts`; NM `ipv4.dns-options = timeout:1,attempts:1` on `enp0s1`.

## 2. OpenSCAP — CUI profile, fresh scan

Content `ssg-rl9-ds.xml`, profile `xccdf_org.ssgproject.content_profile_cui`.
Artifacts: `/var/log/oscap/oscap-{scan,services,cui}-2026-08-01.*`

| Scan | Pass | N/A | Informational | **Fail** |
|:---|---:|---:|---:|---:|
| 2026-07-31 16:28 (pre-change) | 102 | 36 | 1 | **0** |
| 2026-08-01 15:02 (post-change) | 101 | 36 | 1 | **1** |

Base score 99.84.

### FINDING F-2026-08-18 — baseline regression, self-inflicted and authorised

The single failure is:

```
Title  Configure dnf-automatic to Install Available Updates Automatically
Rule   xccdf_org.ssgproject.content_rule_dnf-automatic_apply_updates
Result fail
```

This is a **direct consequence of change C3** (setting `apply_updates = no`),
made today at the system owner's direction after unattended updates disabled the
SIEM for ~21 hours (`DIWAI-EV-AU-2026-08-01`).

The documented figure "VM CUI 102/102" is therefore now **101/102**.

This is a genuine conflict between two requirements, not an error:

- **3.14.1 (flaw remediation)** — the SSG CUI baseline expects updates to install
  automatically, and this rule encodes that expectation.
- **3.4.3 / 3.4.4 (change control)** — unattended installation applies
  unapproved changes to a CUI baseline, and demonstrably disabled a security
  control on 2026-07-31.

**Disposition: documented deviation with compensating control.** Updates are
still downloaded daily and reported (`download_updates = yes`); the deviation is
the *application* step, which now requires operator action. Recommend recording
this as an accepted, justified deviation in SSP v2.15 rather than remediating
the SCAP rule, and pairing it with a defined patch-review cadence so 3.14.1 is
satisfied by procedure instead of automation.

**Owner confirmation required.** The alternative — reverting to auto-apply to
recover 102/102 — reinstates the exact condition that caused today's outage.

## 3. FINDING F-2026-08-19 — audit retention is approximately one hour

`/etc/audit/auditd.conf`:

```
max_log_file = 8          # MB
num_logs = 5
max_log_file_action = ROTATE
space_left_action = SYSLOG
```

Effective cap: **40 MB total**, rotating (oldest overwritten).

Measured retention window on 2026-08-01:

| | |
|:---|:---|
| Oldest retained record | 14:02:45 MDT |
| Newest record | 15:04:49 MDT |
| **History retained** | **~1 hour** |
| Partition | `/dev/mapper/vg0-var_log_audit`, **10 GB, 141 MB used (2%)** |

The audit partition is dedicated and 9.8 GB free, yet policy discards records
after roughly an hour. This materially undermines 3.3.1 and 3.3.2 (create and
**retain** audit records to enable monitoring, analysis, investigation and
reporting of unlawful or unauthorised activity) and 3.3.6 (audit reduction and
report generation for after-the-fact investigation).

**Compounding:** during the 2026-07-31 → 08-01 Wazuh outage there was no
central aggregation, and local audit records from that window have already
rotated away. That telemetry is unrecoverable — this finding is why.

**Recommendation:** raise `max_log_file` and `num_logs` to use the provisioned
partition (e.g. 64 MB × 100 ≈ 6.4 GB, months of history), and set
`max_log_file_action = ROTATE` with `space_left_action = EMAIL`/`SYSLOG` plus
`admin_space_left_action` so exhaustion is alerted rather than silent. Not
changed unilaterally — audit configuration is a controlled setting.

## 4. FINDING F-2026-08-20 — cleartext mail authentication permitted

`doveconf`:

```
auth_mechanisms = plain login
disable_plaintext_auth = no
ssl = yes
```

Listening: `0.0.0.0:143` (IMAP), `0.0.0.0:110` (POP3), `0.0.0.0:25` (SMTP),
alongside the TLS variants 993/995/465/587.

firewalld permits services: `cockpit dhcpv6-client http https imap imaps smtp
smtps ssh` — so **143 (IMAP) and 25 (SMTP) are reachable across the zone**.
110 (POP3) is listening but not permitted by the firewall.

`ssl = yes` makes TLS *available*; `disable_plaintext_auth = no` means it is not
*required*. A client may therefore authenticate over an unencrypted channel,
placing mail credentials on the wire in cleartext — the same defect class as the
NAS LDAP bind (`DIWAI-EV-SC-2026-08-01`). Relevant to 3.5.10 (protect
authenticators), 3.13.8 (transmission confidentiality), 3.13.11.

**Recommendation:** set `disable_plaintext_auth = yes`, and remove the `imap`
and `smtp` firewalld services in favour of `imaps`/`smtps`/submission. Requires
confirming Roundcube and any mail clients use TLS first — not changed
unilaterally.

## 5. FINDING F-2026-08-21 — Prometheus bound to all interfaces

`*:9090` is held by **`prometheus`** (pid 1566), not cockpit. It is bound to all
interfaces rather than loopback. It is **not** permitted by firewalld (absent
from both the services and ports lists), so it is not externally reachable —
defence in depth held. Best practice is nonetheless to bind loopback and proxy
if remote access is needed. Low severity; 3.13.1 / 3.4.6.

## 6. Not yet assessed (pending access)

| Area | Blocker |
|:---|:---|
| Mac host mSCP baseline, pf, USBGuard, FileVault, Wazuh agent | Requires Mac `sudo` |
| NAS DSM configuration, accounts, patch level, share ACLs, encryption at rest | Requires DSM access |

## 7. Verification commands

```
sudo systemctl start oscap-scan.service
sudo awk '/^Result/{print $2}' /var/log/oscap/oscap-scan-$(date +%F).log | sort | uniq -c
sudo grep -E '^max_log_file|^num_logs' /etc/audit/auditd.conf
sudo doveconf | grep -E '^disable_plaintext_auth|^ssl ='
sudo firewall-cmd --list-all
```
