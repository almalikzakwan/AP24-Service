@echo off

:loop
CLS
ECHO START (S)
ECHO STOP (T)
ECHO RESTART (R)
ECHO STATUS (U)
ECHO.

CHOICE /C 1234 /N /M "Start, Stop, Restart and Status?"

IF errorlevel 4 goto :four
if errorlevel 3 goto :three
if errorlevel 2 goto :two
if errorlevel 1 goto :one

:four
echo four

:three
echo three

:two
echo two

:one
echo one

pause

goto loop




