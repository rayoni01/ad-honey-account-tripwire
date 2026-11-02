import json
def handle(j):
    d=json.loads(j)
    print(f"🚨 AD HONEY TRIGGERED: {d.get('TargetUserName')}\nSource: {d.get('IpAddress')}\nAction: Isolate host + Hunt SharpHound")
handle('{"TargetUserName":"svc_finance_backup","IpAddress":"192.168.56.101"}')
