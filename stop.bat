@echo off

REM cd into current directory
cd /d %~dp0

REM import config
call app/config.bat

echo "bitch %service_name% stopping.........."
REM configure apache random port
cd /d "%~dp0"

net stop %service_name%

netsh interface portproxy delete v4tov4 listenport=80 listenaddress=0.0.0.0
netsh interface portproxy delete v4tov4 listenport=443 listenaddress=0.0.0.0

echo [INFO] Port forwarding deleted successfully.

REM read value from recent.default.port file
for /f "usebackq delims=" %%A in ("storage/recent.default.port") do (
    netsh advfirewall firewall delete rule name="Apache Custom Port %%A"
    echo [INFO] Deleted Rule Apache Port %%A
)
REM read value from recent.ssl.port file
for /f "usebackq delims=" %%B in ("storage/recent.ssl.port") do (
    netsh advfirewall firewall delete rule name="Apache Custom Port %%B"   
    echo [INFO] Deleted Rule Apache Port %%B
)

echo "yeah dude, %service_name% cumming......." 

REM stop database
echo [INFO] Stopping %database_name% service
net stop %database_name%

echo %database_name% also cumming......

pause

REM make if else with error level for stoping service