#!/bin/bash
SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
function create() {
    cd $SCRIPTPATH
    python3 create.py $1
}
