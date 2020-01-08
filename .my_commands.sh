#!/bin/bash

function create() {
    cd
    python create.py $1
    cd ~/Documents/Projects/MyProjects/$1
    git init
    git remote add origin git@github.com:$2/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}

function remove() {
    cd ~/Documents/Projects/MyProjects
    read -p "Are you sure?[y/n]" confirm
    if [ "$confirm" = "n" ] || [ "$confirm" = "N" ]; then
        return
    fi
    rm -rf $1
    python remove.py $1
}
