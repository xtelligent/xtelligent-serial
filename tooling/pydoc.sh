#!/usr/bin/env bash
set -e
MYDIR="$(cd "$(dirname "$0")" && pwd)"
export PYVER="3.8"
if [ "$1" = "--build" ]; then
    docker-compose -f "$MYDIR/docker/compose.yaml" kill py
    docker-compose -f "$MYDIR/docker/compose.yaml" build py
fi
PROJDIR="$(cd "$MYDIR/.." && pwd)"
TEMPDIR="$PROJDIR/.tmp/doc"
rm -rf "$TEMPDIR" || true
mkdir -p "$TEMPDIR"

function makedoc {
    # docker-compose -f "$MYDIR/docker/compose.yaml" run py pydoc-html "$1" > "$TEMPDIR/$1.html"
    docker-compose \
        -f "$MYDIR/docker/compose.yaml" \
        run \
        -v "$TEMPDIR:/var/doc" \
        -e "PYTHONWARNINGS=error::UserWarning" \
        py pdoc --html --output-dir /var/doc "$@"
}
makedoc xtelligent_serial examples
# makedoc xtelligent_serial.json