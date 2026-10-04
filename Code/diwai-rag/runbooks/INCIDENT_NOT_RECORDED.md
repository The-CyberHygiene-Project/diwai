default_repair: none
decisions:
objectives: 3.6.2[a], 3.6.2[b], 3.6.2[f]
user_sees: Something unusual happened, such as an unexpected sign-in warning, a lost key or device, a strange message, or files changed that nobody changed.
means: Some incidents must be reported to the Defense Department within 72 hours of being noticed. The clock starts when it is noticed, not when it is written down.
evidence: Something unusual was noticed, and there is no incident record for it yet.
repair: No automatic repair. Write down what was seen and when, then tell the owner at once. A note on paper is enough to start.
if_wrong: Little harm. A report that turns out to be nothing is closed with a note.
rollback: An incident record is never deleted. A false alarm is closed with a dated note.
say_no_if: Someone suggests waiting to see whether it happens again before telling anyone.
---
Status per DIWAI-IRP (Incident_Response_Plan) and POA&M v1.32. DFARS 252.204-7012: report to DoD via DIBNet (https://dibnet.dod.mil) within 72 hours of discovery; the admin portal has pre-populated DoD, GSA and FBI report forms. Filed incidents: DIWAI-INC-001, -002; the POA&M is the tracking register. Open: POA&M-056 (the reporting tooling is hosted on the VM, the asset contained during an incident, so paper is the fallback) and POA&M-057 (no DoD medium assurance certificate for DIBNet yet).
