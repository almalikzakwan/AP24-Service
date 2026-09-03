@echo off

REM cd into current directory
cd /d %~dp0

REM import config
call config.bat 

REM Query redis status
FOR /F "tokens=3 delims=: " %%H IN ('sc query %redis_name% ^| findstr "STATE"') DO (
	SET "DBSTATE=%%H"
)

REM Check if running
IF /I "%DBSTATE%"=="RUNNING" ( 
	echo [INFO] %redis_name% service is already RUNNING hornies.
    REM stop redis
    echo [INFO] Stopping %redis_name% service
    net stop %redis_name%

    echo %redis_name% ahhhhhhhh ...... cumming last round.....

) ELSE (
	echo [WARN] %redis_name% service not running, probably rest after pace 2. 

	REM start the %redis_name% service.
	echo [INFO] start %redis_name% service.
	net start %redis_name% >nul 2>&1

	IF ERRORLEVEL 1 (
		echo [ERROR] failed to start %redis_name%.
		TIMEOUT /t 44
	) ELSE (
		echo [SUCCESS] %redis_name%	service hornies successfully.
	)

)


echo [WARNING] This program will exit after the timeout. Please be alert.
TIMEOUT /t 44