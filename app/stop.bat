@echo off

REM cd into current directory
cd /d %~dp0

REM import config
call app/config.bat

echo "bitch %service_name% stopping.........."
REM configure apache random port

REM import clean firewall rule
call clean_rule.bat
REM import clean port forwarfing function
call clean_port_forwarding.bat

net stop %service_name%
echo "yeah dude, %service_name% cumming......." 

REM stop database
echo [INFO] Stopping %database_name% service
net stop %database_name%

echo %database_name% also cumming......

pause

REM make if else with error level for stoping service