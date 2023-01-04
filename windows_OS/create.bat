@echo off

rem Check for required arguments
if "%1"=="" (
    echo "error: folder name is required"
    goto usage
)
if "%2"=="" (
    echo "error: mode is required"
    goto usage
)

rem Set variables from command line arguments
set foldername=%1
set mode=%2

rem Change to the script's directory
cd /d %~dp0

rem Run the appropriate script based on the mode
if "%mode%"=="local" (
    python local.py %foldername%
) else if "%mode%"=="remote" (
    python remote.py %foldername% %mode%
) else (
    echo "error: invalid mode"
    goto usage
)

goto end

:usage
echo "Usage: create.bat <folder_name> <mode>"
echo "       where <mode> is one of 'local' or 'remote'"

:end
