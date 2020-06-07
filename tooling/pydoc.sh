#!/usr/bin/env bash
set -e
MYDIR="$(cd "$(dirname "$0")" && pwd)"
export PYVER="3.8"
if [ "$1" = "--build" ]; then
    docker-compose -f "$MYDIR/docker/compose.yaml" kill py
    docker-compose -f "$MYDIR/docker/compose.yaml" build py
fi
PROJDIR="$(cd "$MYDIR/.." && pwd)"
DOCDIR="$PROJDIR/docs"
rm -rf "$DOCDIR" || true
mkdir -p "$DOCDIR"

function makedoc {
    docker-compose \
        -f "$MYDIR/docker/compose.yaml" \
        run \
        -v "$DOCDIR:/var/doc" \
        -e "PYTHONWARNINGS=error::UserWarning" \
        py \
        pdoc \
        --html --output-dir /var/doc \
        "$@"
}
makedoc xtelligent_serial examples
