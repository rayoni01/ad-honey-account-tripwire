# AD Honey Account Tripwire — Active Directory Deception

**Problem:** Attackers love AD — BloodHound, Kerberoasting. EDR misses enumeration.

**Flow:**
1. Create honey user svc_finance_backup (attractive name, no real access)
2. Plant decoy doc AD_Credentials.txt on Desktop
3. Attacker tries logon/Kerberoast -> Event ID 4768/4625 -> Triggers
4. Python -> SentinelOne isolate + alert

**Value:**
- Detects T1087, T1558, T1003
- Placement: 2 honey users per OU, no logon rights
- Zero false positives — legit users never touch it

Author: Brian Rayoni
