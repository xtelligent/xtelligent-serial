#!/usr/bin/env bash
set -e
MYDIR="$(cd "$(dirname "$0")" && pwd)"
export PYVER="3.8"
if [ "$1" = "--build" ]; then
    docker-compose -f "$MYDIR/docker/compose.yaml" kill py
    docker-compose -f "$MYDIR/docker/compose.yaml" build py
fi
PROJDIR="$(cd "$MYDIR/.." && pwd)"
docker-compose \
    -f "$MYDIR/docker/compose.yaml" \
    run \
    -v "$PROJDIR/setup.py:/usr/project/setup.py" \
    -v "$PROJDIR/README.md:/usr/project/README.md" \
    --rm py python setup.py  sdist bdist_wheel
