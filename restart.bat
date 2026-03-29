@echo off

REM set your service_name file path here
set "filepath=E:\Apache\httpd-2.4.66-260223-Win64-VS18\AP24-Service\service_name.txt"

for /f "usebackq delims=" %%i in (%filepath%) do (
    set "service_name=%%i"
)

echo "Restarting bitch Apache2D service....."
net stop %service_name%
net start %service_name%
echo "Apache2D successfully fucking restart"
pause