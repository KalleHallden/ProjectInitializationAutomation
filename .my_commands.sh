#!/bin/bash
source ./.env

CREDINTIALS=$USERNAME
if [[ "$PASSWORD" != "" ]]; then
    CREDINTIALS="$USERNAME:$PASSWORD"
fi
function project(){
    DELETE_FLAG='false'
    DELETE_VALUE=''
    if [[ "$1" == "-d" ]]; then
        DELETE_FLAG='true'; DELETE_VALUE=$2
    fi
    if [ "$DELETE_FLAG" = "true" ]; then
        cd $PROJECTS_PATH
        rm -rf $PROJECTS_PATH$DELETE_VALUE
        GH_CREATE=$(curl -u $CREDINTIALS -X DELETE https://api.github.com/repos/$USERNAME/$DELETE_VALUE)
        if [[ $GH_CREATE == *"message"* ]]; then
            echo -e "\033[1;31mMay be there is something wrong please check the curl response."
            echo $GH_CREATE
        fi
        echo -e "\033[1;32mFinished! \033[0m"
        return;
    fi
    mkdir $PROJECTS_PATH$1
    cd $PROJECTS_PATH$1
    GH_DELETE=$(curl -u $CREDINTIALS -X POST https://api.github.com/user/repos --data '{"name":"'$1'"}')
    if [[ "$GH_DELETE" == *"message"* ]]; then
        echo -e "\033[1;31mMay be there is something wrong please check the curl response."
        echo $GH_DELETE
    fi
    git init
    git remote add origin git@github.com:$USERNAME/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
    echo -e "\033[1;32mFinished! \033[0m"
}
