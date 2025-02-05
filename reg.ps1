# Caminho da chave no Registro
$regPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

# Altera o valor de AutoAdminLogon para 1
Set-ItemProperty -Path $regPath -Name "AutoAdminLogon" -Value "1"

# Verifica se a chave DefaultUserName já existe
if (-not (Get-ItemProperty -Path $regPath -Name "DefaultUserName" -ErrorAction SilentlyContinue)) {
    # Cria a chave DefaultUserName com o valor especificado
    Set-ItemProperty -Path $regPath -Name "DefaultUserName" -Value "corp\paineltasy"
} else {
    Write-Host "A chave DefaultUserName já existe. Nenhuma alteração foi feita."
}

# Verifica se a chave DefaultPassword já existe
if (-not (Get-ItemProperty -Path $regPath -Name "DefaultPassword" -ErrorAction SilentlyContinue)) {
    # Cria a chave DefaultPassword com o valor especificado
    Set-ItemProperty -Path $regPath -Name "DefaultPassword" -Value "hospital@102030"
} else {
    Write-Host "A chave DefaultPassword já existe. Nenhuma alteração foi feita."
}