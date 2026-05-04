@echo off
REM cd into current directory
cd /d %~dp0

REM automatic get your current path here
set "servicefilepath=%CD%\..\config\service.conf"

for /f "usebackq delims=" %%i in (%servicefilepath%) do (
    set "service_name=%%i"
)

REM automatic get your current path here
set "databasefilepath=%CD%\..\config\database.conf"

for /f "usebackq delims=" %%i in (%databasefilepath%) do (
    set "database_name=%%i"
)