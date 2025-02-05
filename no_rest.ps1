# Caminho de origem do arquivo Preferences
$origem = "C:\Tasy AutoLogon\Preferences"

# Caminho de destino
$destino = "C:\Users\paineltasy\AppData\Local\Google\Chrome\User Data\Default\Preferences"

# Verifica se o arquivo de origem existe
if (Test-Path $origem) {
    # Verifica se o arquivo Preferences já existe no destino
    if (Test-Path $destino) {
        # Renomeia o arquivo existente para Preferences.old
        Rename-Item -Path $destino -NewName "Preferences.old" -Force
        Write-Host "Arquivo renomeado para Preferences.old."
    }

    # Copia o novo arquivo Preferences para o destino
    Copy-Item -Path $origem -Destination $destino -Force
    Write-Host "Arquivo Preferences copiado com sucesso para $destino."
} else {
    Write-Host "Arquivo de origem não encontrado: $origem"
}