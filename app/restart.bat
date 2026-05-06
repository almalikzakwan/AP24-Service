@echo off

REM cd into current directory
cd /d %~dp0

REM import config
call app/config.bat 

REM import clean firewall rule
call clean_rule.bat
REM import clean port forwarding function
call clean_port_forwarding.bat

REM stop service 
echo [INFO] Restarting bitch %service_name% service.....
net stop %service_name%

REM configure random port
echo [INFO] configure apache random port 
cd /d "%~dp0"
python .\resources\main.py
TIMEOUT /t 4

REM start service
net start %service_name%
echo [INFO] %service_name% successfully fucking restart

REM stop database service
echo [INFO] Restarting %database_name% service.....
net stop %database_name%

REM start database service
echo [INFO] Starting %database_name% service......
net start %database_name%

pause