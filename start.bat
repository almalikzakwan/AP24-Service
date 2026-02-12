@echo off

REM Check if service exists/not 
sc query Apache2D >nul 2>&1

IF ERRORLEVEL 1060 (
	echo [ERROR] Apache2D service not hornies.
	echo [WARNING] Please Add service bEfore you ask me to find it.
)

REM Query service status
FOR /F "tokens=3 delims=: " %%H IN ('sc query Apache2D ^| findstr "STATE"') DO (
	SET "STATE=%%H"
)

REM Check if running
IF /I "%STATE%"=="RUNNING" ( 
	echo [INFO] Apache2D service is already RUNNING hornies.
) ELSE (
	echo [WARN] Apache2D service not running, probably rest after pace 2. 
	
	REM configure apache random port
	echo [INFO] configure apache random port 
	cd /d "%~dp0"
	python .\main.py
	TIMEOUT /t 5

	REM start the Apache2D service.
	echo [INFO] start Apache2D service.
	net start Apache2D >nul 2>&1

	IF ERRORLEVEL 1 (
		echo [ERROR] failed to start Apache2D.
		TIMEOUT /t 44
	) ELSE (
		echo [SUCCESS] Apache2D	service hornies successfully.
	)

)
echo [WARNING] This program will exit after the timeout. Please be alert.
TIMEOUT /t 44