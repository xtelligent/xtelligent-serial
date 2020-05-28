#!/usr/bin/env bash
set -e
MYDIR="$(cd "$(dirname "$0")" && pwd)"
export PYVER="${1:-3.6}"

set +e
docker-compose -f "$MYDIR/docker/compose.yaml" run py pylint tests
RC1=$?
docker-compose -f "$MYDIR/docker/compose.yaml" run py pylint json_unmasked
RC2=$?

set -e
test $RC1 -eq 0 && test $RC2 -eq 0
