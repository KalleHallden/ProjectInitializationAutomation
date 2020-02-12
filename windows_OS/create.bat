@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    if "%2"=="" (
        python remote.py %fn% %flag%
        ) else (
            if "%2"=="l" (
                python local.py %fn%
            )
        )
    )
