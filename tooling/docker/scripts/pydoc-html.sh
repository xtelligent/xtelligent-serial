#!/usr/bin/env bash
OUTDIR="./docs"
mkdir -p "$OUTDIR"
pdoc --html --output-dir "$OUTDIR" xtelligent_serial examples || true
