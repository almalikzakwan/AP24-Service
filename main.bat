@echo off

:loop
CLS
cd /d %~dp0
ECHO START (1)
ECHO STOP (2)
ECHO RESTART (3)
ECHO STATUS (4)
ECHO.

CHOICE /C 1234 /N /M "Start, Stop, Restart and Status?"

IF errorlevel 4 goto :status
if errorlevel 3 goto :restart
if errorlevel 2 goto :stop
if errorlevel 1 goto :start

:status
call app/status.bat
goto end

:restart
call app/restart.bat
goto end

:stop
call app/stop.bat
goto end

:start
call app/start.bat
goto end

:end
pause
goto loop




