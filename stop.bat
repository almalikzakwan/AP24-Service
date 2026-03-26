@echo off

REM set your service_name file path here
set "filepath=E:\Apache\httpd-2.4.66-260223-Win64-VS18\AP24-Service\service_name.txt"

for /f "usebackq delims=" %%i in (%filepath%) do (
    set "service_name=%%i"
)

echo "bitch %service_name% stopping.........."
REM configure apache random port
cd /d "%~dp0"

net stop %service_name%

netsh interface portproxy delete v4tov4 listenport=80 listenaddress=0.0.0.0
netsh interface portproxy delete v4tov4 listenport=443 listenaddress=0.0.0.0

echo [INFO] Port forwarding deleted successfully.

REM read value from recent.default.port file
for /f "usebackq delims=" %%A in ("storage/recent.default.port") do (
    netsh advfirewall firewall delete rule name="%service_name% Port %%A"
    echo [INFO] Deleted Rule Apache Port %%A
)
REM read value from recent.ssl.port file
for /f "usebackq delims=" %%B in ("storage/recent.ssl.port") do (
    netsh advfirewall firewall delete rule name="%service_name% Port %%B"   
    echo [INFO] Deleted Rule Apache Port %%B
)

echo "yeah dude, %service_name% cumming......." 
pause

REM make if else with error level for stoping service