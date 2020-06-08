#!/usr/bin/env bash
set -e
MYDIR="$(cd "$(dirname "$0")" && pwd)"
export BNUM="${BUILDNUMBER:-2112}"
cp "$MYDIR/../config" "$MYDIR/../version.py"
mkdir -p "$MYDIR/../xtelligent_serial"
VERFILE="$MYDIR/../xtelligent_serial/version.py"
cp "$MYDIR/../config" "$VERFILE"
echo "BUILDNUMBER=$BNUM" >> "$VERFILE"
