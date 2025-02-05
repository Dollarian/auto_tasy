# Caminho de origem do arquivo
$origem = "C:\Tasy AutoLogon\tasy.py"

# Caminho de destino (usando $env:AppData para expandir a variável de ambiente)
$destino = "$env:AppData\Microsoft\Windows\Start Menu\Programs\Startup"

# Verifica se o arquivo de origem existe
if (Test-Path $origem) {
    # Copia o arquivo para o destino
    Copy-Item -Path $origem -Destination $destino -Force
    Write-Host "Arquivo copiado com sucesso para $destino."
} else {
    Write-Host "Arquivo de origem não encontrado: $origem"
}