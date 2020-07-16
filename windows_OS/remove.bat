@echo off

cd /d %~dp0
setlocal

rem pyParams variable to contain python script's parameters
rem Helper flag for parameter presence. default to 0/FALSE.
set prmOk=0

rem Variable to contain python script name to use. default is remote.
set pyName=remove

rem Process batch parameters
:getParam

set pyParams=%pyParams% %1
set prmOk=1

shift
rem After SHIFT, %0 is replaced by %1, %1 replaced by %2, %2 replaced by %3, etc.
if "%~1" neq "" goto getParam

rem Check python script's parameter presence
if %prmOk% == 0 (
  echo Batch parameter is missing.
  goto :eof
)

python %pyName%.py%pyParams%

:eof