## Proof — Lab Simulation (Why 0 events is expected)

This is a lab-safe simulation. On this standalone Windows 11 laptop (non-domain), the Security log filtered for Event ID 4768 shows 0 events — expected behavior.

![Event Viewer - 4768 - 0 events](event-viewer-4768-zero.png)

**Why 0 events:**
- Event ID 4768 = Kerberos TGT Request — only generated on a Domain Controller with Kerberos auditing
- This laptop is not a domain controller, so no real 4768 for `svc_finance_backup`
- In production: Enable auditing on DC, create real AD user `New-ADUser -SamAccountName svc_finance_backup`

**What this lab shows instead:**
- `sample_honey_event.json` — sample Event ID 4768 payload for parser testing
- `Detect-HoneyLogon.py` — parses sample JSON and formats alert for SOAR workflow
- Parser output:
  `[ALERT] Honey account Kerberos TGT Request — Possible Kerberoasting`
  `User: svc_finance_backup | Source: 192.168.56.101 | Event: 4768`
