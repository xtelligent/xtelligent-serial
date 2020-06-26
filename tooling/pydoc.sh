#!/usr/bin/env bash
set -e
MYDIR="$(cd "$(dirname "$0")" && pwd)"
export PYVER="3.8"
if [ "$1" = "--build" ]; then
    docker-compose -f "$MYDIR/docker/compose.yaml" kill py
    docker-compose -f "$MYDIR/docker/compose.yaml" build py
fi
PROJDIR="$(cd "$MYDIR/.." && pwd)"
DOCDIR="$PROJDIR/.tmp/docs"
rm -rf "$DOCDIR" || true
mkdir -p "$DOCDIR"

docker-compose \
    -f "$MYDIR/docker/compose.yaml" \
    run --rm \
    -v "$DOCDIR:/var/doc" \
    -v "$PROJDIR/tooling/docker/scripts/pydoc-html.sh:/usr/project/pydoc-html.sh" \
    py \
    ./pydoc-html.sh xtelligent_serial examples
