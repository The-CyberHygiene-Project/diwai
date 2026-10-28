> **REDACTED PUBLIC COPY.** Identifiers (IPs, owner, organization, ISP, domain, contact, CAGE/DUNS) replaced with placeholders for public release. Authoritative unredacted copy held in the RS2 access-controlled store.

# CHANGE RECORD — MAIL PORT 25 CLOSED TO THE INTERNET
## [DOMAIN.ORG] SecureMac Reference System

| Field | Value |
|-------|-------|
| **Document ID** | **DIWAI-CR-2026-10-61** |
| **Date** | October 28, 2026 |
| **Status** | **IMPLEMENTED AND VERIFIED. Owner approved 2026-10-28 ("close port 25 for now").** |
| **System** | Mac host firewall (`/etc/pf_diwai.conf`) |
| **Addresses** | 3.13.5 and 3.13.2 [b] (exposure removed; count claim held, see §3) |

## 1. What changed

The redirect and the WAN pass rule for TCP 25 to the VM were removed. Nothing is now forwarded from the internet to any host (`pfctl -s nat` lists no redirect on the internet interface; `pfctl -s rules` lists no WAN pass rule for mail). The VM firewall was not changed: the VM still accepts mail on port 25 from the CUI network, which the alert mail uses. Outbound mail (alerts to the owner's Gmail account) is unchanged. Rollback is the backup file named in the script output, `/etc/pf_diwai.conf.bak-20261028-*-cr61`; re-enabling is a recorded change.

## 2. Why

Inbound mail never arrived. Over three 5–10 minute watches and earlier tests (two Gmail sends, one business-address send, and an outside SMTP test from a public diagnostic site that timed out) the Mac's internet interface captured **zero** port-25 packets while thousands of other packets arrived for the same address block. DNS at Cloudflare was verified correct (MX `mail.[DOMAIN.ORG]` to the mail address; no proxy on it). The Mac firewall counters stayed at zero. The owner called the carrier: the account is residential, support reported no block but could not act on a static address block, and the fault stays upstream of this system. Residential accounts commonly have port 25 filtered by policy. The owner has a hosted provider available for non-CUI mail if it is needed. CUI is never carried by outside mail (SSP E.22).

## 3. Effect on the requirements

The one publicly accessible component is removed from the internet. The owner is still looking at a relay or an upgraded account, so **no count change is claimed yet** (strict count stays 103/110, SPRS unchanged); if the owner confirms that nothing will be published, 3.13.5 and 3.13.2 [b] are reconsidered as not applicable on the fact that no component is accessible from the internet. Cloudflare still advertises the mail record; the owner removes it if mail is not to be published.

## 4. Verification

Read-only check after the change (2026-10-28): no redirect from the internet interface, no WAN pass rule for mail, and port 25 on the VM answers from the CUI network.
