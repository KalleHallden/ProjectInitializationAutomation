#!/bin/bash


function create() {
    cd 
    source .env #Type the path to your .env file here
    python create.py $1 #Type the path to the create.py path here
    cd $FILEPATH$1
    touch README.md
    git init       
    git add .
    git commit -m "Initial commit"
    git remote add origin git@github.com:$USERNAME/$1.git
    git push -u origin master
    cd ..
    subl $1
    cd $1
    
}


function delete() { 
    cd
    source /.env #Type the path to your .env file here     
    python /delete.py $1 #Type the path to the delete.py path here
    cd $FILEPATH    
    rm -r -f $1    

}
