# Detect-HoneyLogon.py — Parses honey account logon events
# No real credentials — sample JSON only
# Simulates detection of Event ID 4768 (Kerberos TGT) and 4625 (Failed Logon)

import json
from datetime import datetime

def handle_honey_logon(event_json: str):
    try:
        data = json.loads(event_json)
    except json.JSONDecodeError:
        print("[!] Invalid JSON")
        return

    user = data.get("TargetUserName", "svc_finance_backup")
    src_ip = data.get("IpAddress", "192.168.56.101")
    event_id = data.get("EventID", 4768)
    time = data.get("Time", datetime.utcnow().isoformat())

    # Basic check — is this our honey user?
    if "svc_finance" not in user and "backup" not in user.lower():
        print(f"[-] Not a honey account: {user}")
        return

    if event_id == 4768:
        print(f"[ALERT] Honey account Kerberos TGT Request — Possible Kerberoasting")
    elif event_id == 4625:
        print(f"[ALERT] Honey account Failed Logon — Possible enumeration")
    else:
        print(f"[ALERT] Honey account activity — Event ID {event_id}")

    print(f"User: {user} | Source: {src_ip} | Event: {event_id} | Time: {time}")
    print(f"Next: Check {src_ip} for BloodHound/SharpHound, review LDAP queries")

    # Example SentinelOne workflow — commented, do NOT commit real API key
    # import requests
    # requests.post("https://XXXX.sentinelone.net/web/api/v2.1/agents/actions/disconnect",
    #               headers={"ApiToken": "XXXX"}, json={"filter": {"ip": src_ip}})

if __name__ == "__main__":
    sample = '{"TargetUserName":"svc_finance_backup","IpAddress":"192.168.56.101","EventID":4768,"Time":"2026-05-11 10:30:00"}'
    handle_honey_logon(sample)
