#!/usr/bin/env bash
set -e
echo "Opening bash in a container where pwd is the project root."
MYDIR="$(cd "$(dirname "$0")" && pwd)"
export PYVER="${1:-3.7}"
if [ "$2" = "--build" ]; then
    docker-compose -f "$MYDIR/docker/compose.yaml" kill py
    docker-compose -f "$MYDIR/docker/compose.yaml" build py
fi
docker-compose -f "$MYDIR/docker/compose.yaml" run --rm py /bin/bash
