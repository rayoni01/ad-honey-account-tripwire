# AD Honey Account Tripwire — Active Directory Deception

**Problem:** Attackers love AD — BloodHound enumeration, Kerberoasting. EDR often misses enumeration.

**Design (Lab Simulation):**
This is a lab-safe simulation. It does NOT create a real domain user — it creates a decoy credential file to simulate a honey account. In production you would use `New-ADUser svc_finance_backup` with no logon rights.

**Flow:**
1. Create honey account name `svc_finance_backup` (attractive name, no real access)
2. Plant decoy file `AD_Credentials.txt` on Desktop with fake password
3. Simulate detection: Windows Event ID 4768 (Kerberos TGT Request) or 4625 (Failed Logon) for that user
4. Detection: `Detect-HoneyLogon.py` parses sample JSON with TargetUserName, IpAddress, EventID and logs alert

**What this repo contains:**
- `Create-HoneyADUser.ps1` — Lab-safe script that creates decoy credential file (not real AD)
- `Detect-HoneyLogon.py` — Parses sample honey logon JSON and formats alert for SOAR
- `sample_honey_event.json` — Sample Event ID 4768 payload

**MITRE:**
- T1087 Account Discovery
- T1558 Kerberoasting (4768)
- T1003 Credential Dumping (4625)

Author: Brian Rayoni
