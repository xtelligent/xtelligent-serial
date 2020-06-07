#!/usr/bin/env bash
set -e
MYDIR="$(cd "$(dirname "$0")" && pwd)"
PROJDIR="$(cd "$MYDIR/.." && pwd)"
TEMPDIR="$PROJDIR/.tmp/doc"

SOURCE_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# get on the branch we want.
git checkout gh-pages
git pull || true
git reset --hard origin/gh-pages
git merge --strategy theirs "$SOURCE_BRANCH"

# start recording changes
cd "$PROJDIR"
rmdir "doc" 2>/dev/null || true
cp -r ".tmp/doc" ./
git add --all
git commit -m "Generated documentation published."
git push
