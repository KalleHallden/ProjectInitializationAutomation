#!/bin/bash

function git-create() {
    source .env

    path=$1
    repo_name=`echo $path |sed 's/.*\///'`

    # You may need to change python3 to python depending on your setup.
    url=$(python3 create.py $path $repo_name 2>&1)
    echo "URL: ${url}"

    git clone $url $path
}

cd "$(dirname "$0")" || exit

git-create $1
