#!/usr/bin/env bash
set -e
MYDIR="$(cd "$(dirname "$0")" && pwd)"
export PYVER="${1:-3.6}"
if [ "$2" = "--build" ]; then
    docker-compose -f "$MYDIR/docker/compose.yaml" kill py
    docker-compose -f "$MYDIR/docker/compose.yaml" build py
fi
docker-compose -f "$MYDIR/docker/compose.yaml" run py pytest tests
