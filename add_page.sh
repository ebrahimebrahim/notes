#!/bin/bash

set -e

# This should export the requested jupyter notebook to HTML and add the html file to the pages branch,
# for the purpose of github pages

JNB=$1.ipynb

if ! [[ -f $1.ipynb ]]
then
        echo "File $JNB does not exist."
        exit -1
fi

jupyter nbconvert --execute --to html $JNB

echo "Now you should do the following:"
echo "git checkout pages"
echo "git checkout master $1.html"
echo "vim index.md"
echo "git add $1.html"
echo "git commit -a"
echo "git push"
echo "git checkout master"
echo "rm $1.html"
