#!/bin/bash

set -e

# This should export the requested jupyter notebook to HTML and add the html file to the pages branch,
# for the purpose of github pages

HTML=$1.html
JNB=$1.ipynb

if ! [[ -f $HTML ]]
then
        echo "File $HTML does not exist; just a warning."
fi

rm $HTML
git checkout master $JNB
jupyter nbconvert --execute --to html $JNB
rm $JNB

echo "Now you should do the following:"
echo "git add $HTML"
echo "vim index.md"
echo "git commit -a"
echo "git push --all origin"
echo "git checkout master"
