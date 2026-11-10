> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# DIWAI-EV-CM-2026-08-02 — Compliance Citation Sweep

**System:** [DOMAIN.ORG] SecureMac Reference System
**Evidence type:** Documentation integrity audit
**Collected by:** [SYSTEM-OWNER] (system operator), 2026-08-02
**Method:** Automated resolution of every citation in the compliance document
set, followed by host-side verification of every absolute path
**Related requirements:** 3.12.4 (SSP accuracy), 3.8.9 (backup CUI), 3.4.1 (baseline/inventory), 3.11.1

---

## 1. Why this was done

Three broken references surfaced by accident during the 2026-08 rebaseline:
all eleven policies cited as `DIWAI-*-001` while declaring `TCC-*-001`;
`DIWAI-ATP-002` cited but never written; and the SBOM citing
`/root/oscap-report.html`, which never existed. Finding those by chance implied
others were present, so the whole set was swept systematically.

## 2. Method and coverage

Every `.md` file in the Nextcloud `Compliance/` tree, the 2026-08 assessment
working set, and the local `~/diwai/*.md` documents. Five citation classes
resolved: document filenames, policy document IDs, evidence IDs, Nextcloud
paths, and absolute host paths. Host paths were then tested for existence on
both the Mac and the VM.

| Class | Result |
|:---|:---|
| Document/ID citations resolved | **660** |
| Document/ID citations broken | **2** (one deliberate) |
| Absolute host paths cited | **114** |
| Host paths verified present | **93** |
| Host paths absent from both hosts | **21** |

**Tooling caveat:** the first run reported five evidence IDs as unresolved.
That was a defect in the checker — it validated evidence IDs against only one
of the two forms in which IDs are declared. Corrected; those five are properly
self-declared. Recorded here because an auditing tool that produces false
positives is worse than none.

## 3. Document-level findings

### 3.1 `[DOMAIN.ORG]_Unified_POAM_v1.1.md` — cited, does not exist

Cited by POA&M v1.2 and SSP v2.13/v2.14. POA&M v1.2 contains a live pointer:

> *"ITEM DETAIL (new / changed items — **see v1.1 for unchanged 001, 003–008**)"*

An assessor following that instruction to find the detail of six POA&M items
finds nothing. **The detail for those items exists in no current document.**
Not merely a stale path — a gap in the POA&M record.

### 3.2 `DIWAI-ATP-002` — cited, never written

Expected and deliberate. Annotated in place as `NOT YET ISSUED, see POA&M-008`
during the 2026-08-01 policy re-identification, precisely so it would not be
concealed. Retained as a visible marker of the missing training procedure.

## 4. Host-path findings

The 21 absent paths sort into three categories that must not be conflated.

### 4.1 Deliberate citations of things that do not exist (4) — no action

`/usr/bin/zsh`, `/root/Maildir`, `/root/oscap-report.html`, and
`/var/log/account-reviews/YYYY-QN.log`. The first three are cited *because* they
are absent — they document defects found and fixed. The fourth is a filename
template, not a path.

### 4.2 Assessor's own errors (2) — corrected 2026-08-02

The change record cited two rollback backups that were never created:
`run-mSCP-scan.sh.bak-20260801` (the backup step was guarded by `[ -s ... ]`
and correctly declined to preserve a zero-byte file) and
`nas-archive-push.bak-20260802` (the backup command was offered but not run).
Both entries corrected to state the true rollback position.

### 4.3 Genuine documentation defects (15)

| Path(s) | Finding |
|:---|:---|
| **7 × `/usr/local/bin/backup-*.sh`** | See §5 — the whole documented backup regime |
| `/etc/ipa/`, `/var/lib/ipa/` | FreeIPA paths. This system uses 389-DS; FreeIPA is CyberInABox technology and is not installed |
| `/etc/pki/tls/certs/wildcard.[DOMAIN.ORG].crt`, `…/private/wildcard.[DOMAIN.ORG].key` | Wrong filenames — the certificate is `[DOMAIN.ORG].crt` / `.key`. Cited as the TLS material location |
| `/var/lib/clamav/dl` | ClamAV, decommissioned 2026-06-12 and packages removed 2026-08-01 |
| `/Users/[USERNAME]/macos_security/` | mSCP toolchain directory, not present (related to POA&M-015) |
| `/var/log/change-management/`, `…/changes.log` | A change log the documentation says is maintained. It does not exist |

## 5. FINDING — the Backup Procedures document describes a different system

**`Compliance/Procedures/CUI_Backup_Procedures_v1.0_WITHDRAWN.md`** (renamed on
withdrawal 2026-08-02; was `CUI_Backup_Procedures_v1.0.md`) specifies a backup
regime built on **seven scripts, none of which exist** on either host:

```
backup-all-systems.sh   backup-system.sh      backup-databases.sh
backup-verify.sh        backup-offsite-sync.sh  backup-monthly-test.sh
backup-graylog-elasticsearch.sh
```

It is not merely unimplemented — it describes **another system's
infrastructure**:

| Technology referenced | Mentions | Present on [DOMAIN.ORG]? |
|:---|---:|:---|
| Graylog | 9 | **No** — `systemctl is-active graylog` → inactive |
| Elasticsearch | 8 | **No** — inactive |
| FreeIPA / IPA | 14 | **No** — this system uses 389-DS |

It contains operations such as `rsync -avz admin@${HOSTNAME}:/etc/graylog/` and
`mongodump --db graylog`, against services that have never run here.

**This is the same lineage defect as the `TCC-*-001` policy identifiers, but
more serious.** The policies had been rewritten in substance and only the
identifier was stale. This procedure was inherited from the CyberInABox system
and **never adapted at all**.

**Consequence.** The backups that actually protect this system — Time Machine to
the USB drive, and the FIPS-encrypted Wazuh archive to the NAS — are **described
nowhere**. SSP §5 (Contingency Planning) points at this procedure. An assessor
testing 3.8.9 or contingency planning against it would find that the documented
regime does not exist and the real one is undocumented.

**Recommendation:** rewrite against what actually runs. The real regime is now
well understood: Time Machine to a FileVault-encrypted USB destination with a
verified retention set; `wazuh-log-archive` producing FIPS-encrypted daily
archives; `nas-archive-push` delivering them with checksum verification; and the
control-health check confirming both still operate.

## 6. Disposition

| Finding | Action |
|:---|:---|
| §3.1 POA&M v1.1 missing | **POA&M-035** — recover or restate items 001, 003–008 detail |
| §3.2 DIWAI-ATP-002 | No action — deliberate marker, closes with POA&M-008 |
| §4.2 assessor's errors | **Corrected** 2026-08-02 |
| §4.3 stale paths | **POA&M-036** — correct in the next document revision |
| §5 backup procedures | **POA&M-037** — rewrite against the real regime |

## 7. Repeatability

The sweep tool is retained at
`~/diwai/assessment-2026-08/sweep-citations.py`. It should be run before issuing
any SSP or POA&M revision — broken citations are cheap to find automatically and
expensive to find during an assessment.
