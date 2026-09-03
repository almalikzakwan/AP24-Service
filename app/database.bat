@echo off

REM cd into current directory
cd /d %~dp0

REM import config
call config.bat 

REM Query database status
FOR /F "tokens=3 delims=: " %%H IN ('sc query %database_name% ^| findstr "STATE"') DO (
	SET "DBSTATE=%%H"
)

REM Check if running
IF /I "%DBSTATE%"=="RUNNING" ( 
	echo [INFO] %database_name% service is already RUNNING hornies.
    REM stop database
    echo [INFO] Stopping %database_name% service
    net stop %database_name%`

    echo %database_name% also cumming......
) ELSE (
	echo [WARN] %database_name% service not running, probably rest after pace 2. 

	REM start the %database_name% service.
	echo [INFO] start %database_name% service.
	net start %database_name% >nul 2>&1

	IF ERRORLEVEL 1 (
		echo [ERROR] failed to start %database_name%.
		TIMEOUT /t 44
	) ELSE (
		echo [SUCCESS] %database_name%	service hornies successfully.
	)

)

echo [WARNING] This program will exit after the timeout. Please be alert.
TIMEOUT /t 44