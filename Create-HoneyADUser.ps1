$HoneyUser="svc_finance_backup"
"Username: $HoneyUser`nPassword: Canary_Honey_2024!Fake" | Out-File "$env:USERPROFILE\Desktop\AD_Credentials.txt"
Write-Host "[+] Honey decoy created — try runas /user:$HoneyUser cmd"
