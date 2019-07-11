#!/bin/bash

function create() {
    source .env
    python3 create.py $1
    cd $FILEPATH$1
    touch README.md
    git init
    git remote add origin git@github.com:$USERNAME/$1.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}