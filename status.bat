@echo off  

REM cd into current directory
cd /d %~dp0

REM automatic get your current path here
set "filepath=%CD%\service_name.txt"

for /f "usebackq delims=" %%i in (%filepath%) do (
    set "service_name=%%i"
)

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
echo [INFO] Here all the list. hope you know what the status of the service right now. 
echo [WARN] this program will exit after timeout
timeout /t 44

