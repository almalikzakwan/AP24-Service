@echo off

:loop
CLS
cd /d %~dp0
ECHO START ALL (1)
ECHO STOP ALL (2)
ECHO RESTART ALL (3)
ECHO STATUS ALL (4)
ECHO APACHE START/STOP (5)
ECHO DATABASE START/STOP (6)
ECHO REDIS START/STOP (7)
ECHO.

CHOICE /C 123456 /N /M "Start, Stop, Restart and Status?"

IF errorlevel 7 goto :redis
IF errorlevel 6 goto :database
IF errorlevel 5 goto :apache
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

:apache
call app/apache.bat
goto end

:database
call app/database.bat
goto end

:redis
call app/redis.bat
goto end

:end
pause
goto loop




