@echo off  

REM cd into current directory
cd /d %~dp0

REM import config
call app/config.bat 

REM cd into root path
cd /d %~dp0

REM read value from recent.default.port file
for /f "usebackq delims=" %%A in ("storage/recent.default.port") do (
    echo [INFO] %service_name% running in DEFAULT port : %%A    
)

REM read value from recent.ssl.port file
for /f "usebackq delims=" %%B in ("storage/recent.ssl.port") do (
    echo [INFO] %service_name% running in SSL port : %%B 
)

echo [INFO] Checking %service_name% status..
sc query %service_name%

echo [INFO] Checking %database_name% status.. 
sc query %database_name%

echo [WARN] this program will exit after timeout !
timeout /t 48

