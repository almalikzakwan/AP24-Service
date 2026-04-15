@echo off

REM cd into current directory
cd /d %~dp0

REM automatic get your current path here
set "filepath=%CD%\service_name.txt"

for /f "usebackq delims=" %%i in (%filepath%) do (
    set "service_name=%%i"
)

echo Restarting bitch %service_name% service.....
net stop %service_name%
net start %service_name%
echo %service_name% successfully fucking restart
pause