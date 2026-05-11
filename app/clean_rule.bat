@echo off

REM cd into current directory
cd /d "%~dp0"

REM read value from recent.default.port file
set "defaultportfilepath=%CD%\..\storage\recent.default.port"
for /f "usebackq delims=" %%A in (%defaultportfilepath%) do (
    netsh advfirewall firewall delete rule name="Apache Custom Port %%A"
    echo [INFO] Deleted Rule Apache Port %%A
)

set "sslportfilepath=%CD%\..\storage\recent.ssl.port"
REM read value from recent.ssl.port file
for /f "usebackq delims=" %%B in (%sslportfilepath%) do (
    netsh advfirewall firewall delete rule name="Apache Custom Port %%B"   
    echo [INFO] Deleted Rule Apache Port %%B
)   