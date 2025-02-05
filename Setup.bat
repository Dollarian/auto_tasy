@echo off

:: Executa o script auto.ps1
powershell.exe -ExecutionPolicy Bypass -File "C:\Tasy AutoLogon\reg.ps1"
pause

:: Executa o script dir.ps1
powershell.exe -ExecutionPolicy Bypass -File "C:\Tasy AutoLogon\pip.ps1"
pause

:: Executa o script start.ps1
powershell.exe -ExecutionPolicy Bypass -File "C:\Tasy AutoLogon\start.ps1"
pause

:: Executa o script no_rest.ps1
powershell.exe -ExecutionPolicy Bypass -File "C:\Tasy AutoLogon\no_rest.ps1"
pause
