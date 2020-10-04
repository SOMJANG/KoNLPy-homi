#!/bin/zsh
if [ $# = 0 ]
then
    echo "can not find tag"
else
    version=$1
    img="gcr.io/konlpy/konlpy_homi:$version"
    docker build  -t $img . && docker push $img
fi


