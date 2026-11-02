# Create-HoneyADUser.ps1 — Lab-safe honey account simulation
# This does NOT create a real AD user — it creates a decoy file for testing
# In production: New-ADUser -SamAccountName svc_finance_backup -Description "Finance Backup - Do not disable"

$HoneyUser = "svc_finance_backup"
$FakePassword = "XXXX-FAKE-PASSWORD-XXXX"

Write-Host "[*] Simulating honey account: $HoneyUser"

$DecoyContent = @"
Username: $HoneyUser
Password: $FakePassword
Description: Finance Backup - DO NOT DISABLE
Note: This is a decoy file for deception lab — not a real credential
"@

$DesktopPath = [Environment]::GetFolderPath("Desktop")
$DecoyPath = Join-Path $DesktopPath "AD_Credentials.txt"
$DecoyContent | Out-File -FilePath $DecoyPath -Encoding utf8

Write-Host "[+] Decoy file created at $DecoyPath"
Write-Host "[*] To test detection: Try runas /user:$HoneyUser cmd — should generate Event ID 4625"
