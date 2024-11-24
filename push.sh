pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git push origin gh-pages