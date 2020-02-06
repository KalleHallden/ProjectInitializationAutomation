@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    if "%2"=="" (
        python local.py %fn%
        ) else (
            python remote.py %fn% %flag%
        )
    )
