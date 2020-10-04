#!/bin/zsh
if [ $# = 0 ]
then
    STAGE='dev'
else
    STAGE=$1
fi

cd terraform && terraform workspace select $STAGE && terraform apply && cd ..


