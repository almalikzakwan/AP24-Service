@echo off

REM cd into current directory
cd /d %~dp0

REM import config
call app/config.bat 

REM Check if service exists/not 
sc query %service_name% >nul 2>&1

IF ERRORLEVEL 1060 (
	echo [ERROR] %service_name% service not hornies.
	echo [WARNING] Please Add service to make it  hornies.
)

REM Query service status
FOR /F "tokens=3 delims=: " %%H IN ('sc query %service_name% ^| findstr "STATE"') DO (
	SET "STATE=%%H"
)

REM Check if running
IF /I "%STATE%"=="RUNNING" ( 
	echo [INFO] %service_name% service is already RUNNING hornies.
) ELSE (
	echo [WARN] %service_name% service not running, probably rest after pace 2. 
	
	REM configure apache random port
	echo [INFO] configure apache random port 
	cd /d "%~dp0"
	python .\resources\main.py
	TIMEOUT /t 4

	REM start the %service_name% service.
	echo [INFO] start %service_name% service.
	net start %service_name% >nul 2>&1

	IF ERRORLEVEL 1 (
		echo [ERROR] failed to start %service_name%.
		TIMEOUT /t 44
	) ELSE (
		echo [SUCCESS] %service_name% service hornies successfully.
	)

)

REM Query database status
FOR /F "tokens=3 delims=: " %%H IN ('sc query %database_name% ^| findstr "STATE"') DO (
	SET "DBSTATE=%%H"
)

REM Check if running
IF /I "%DBSTATE%"=="RUNNING" ( 
	echo [INFO] %database_name% service is already RUNNING hornies.
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