#!/bin/sh
# Assemble the GitHub Pages site into _site/, exactly as the Pages workflow does.
#   sh scripts/build-site.sh          build only
#   sh scripts/build-site.sh serve    build, then serve at http://localhost:8000
set -e
cd "$(dirname "$0")/.."

rm -rf _site
mkdir -p _site/clock _site/docs
cp -R site/index.html site/site.css site/site.js site/fonts _site/
cp app/src/main/assets/index.html _site/clock/index.html
cp docs/*.png _site/docs/
touch _site/.nojekyll
echo "Built _site/"

if [ "$1" = "serve" ]; then
  echo "Serving at http://localhost:8000 (Ctrl+C to stop)"
  cd _site && python3 -m http.server 8000
fi
