#!/bin/bash

set -e
source ~/venv/bin/activate

# This should export the requested jupyter notebook to HTML and add the html file to the pages branch,
# for the purpose of github pages

HTML=$1.html
JNB=$1.ipynb

rm -f $JNB
git show master:$JNB > $JNB
jupyter nbconvert --execute --to html $JNB
rm $JNB
rm -rf .ipynb
git add $HTML

echo "Now you should do the following:"
echo "vim index.md"
echo "git commit -a"
echo "git push --all origin"
echo "git checkout master"
