> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — WEB PORTS 80 AND 443 CLOSED; MAIL PORT 25 KEPT
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-60** |
| **Date** | October 26, 2026 |
| **Status** | **IMPLEMENTED AND TESTED. Owner approved 2026-10-26.** |
| **System** | Mac host firewall (`/etc/pf_diwai.conf`) |
| **Addresses** | 3.13.5 and 3.13.2 [b] (narrowed; both stay partial) |

## 1. What changed

The redirect and the WAN pass rule for TCP 80 and 443 to the VM were removed. The owner's reason: no legitimate use; they are re-enabled by a recorded change if a use appears. Port 25 (inbound and outbound mail) is unchanged. Webmail, the admin portal and `cloud.[DOMAIN.ORG]` still answer on the CUI network. Backup: `/etc/pf_diwai.conf.bak-20261026-0949-cr60`.

## 2. Evidence

The pf counters for the three redirects showed zero packets and zero connections over about 26 hours (since 2026-10-25 07:53); the web logs show no hits from outside the house; the current mail log shows no inbound connection from outside. The window is short, so this is "nothing reached them", not "nothing ever has". Ten tests passed with the automatic revert armed; the revert was cancelled.

## 2A. Why port 25 stays (owner, 2026-10-26)

The mail service is for a business email address aligned with the domain name and is set up for FIPS-validated encryption. The system's alert mail, forwarded to the owner's Gmail account, also uses it. A business that prefers an external email provider should block port 25; the system would then publish nothing. Recorded as adopter guidance in SSP Appendix E.22 and `DIWAI-PORTS-001`.

## 2B. Inbound delivery not proven (2026-10-26)

Two inbound test messages (from a Gmail account and from a second business address) produced **no connection on port 25** at the Mac's internet interface within several minutes, and the pf counters stayed at zero. In the same period the interface saw about 100 connection attempts in two minutes to the /29 block from internet scanners, on ports including 23, 443 and 995 but none on 25. Outbound mail works (a webmail test reached Gmail through Gmail's relay). The likely cause is that the ISP filters inbound port 25 on this circuit; this is **not confirmed**. Until inbound delivery is proven, "external email can be received" is the intent, not an established fact. Next steps: ask the ISP whether inbound port 25 is blocked and can be unblocked; if it cannot, mail receipt is not possible and Option A (publish nothing) applies.

## 3. Effect on the requirements

The one publicly accessible component is the mail server, on the same VM as the directory, the Nextcloud database and the SIEM manager. 3.13.5 stays not met and 3.13.2 [b] partial. Options for separating the mail server were discussed with the owner (a small VM on its own subnet inside the Mac, a separate firewall appliance, or not publishing mail); none is chosen. Strict count 103/110; SPRS unchanged.
