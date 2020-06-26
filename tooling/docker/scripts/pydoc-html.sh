#!/usr/bin/env bash
OUTDIR="/var/doc"
pdoc --html --output-dir "$OUTDIR" xtelligent_serial examples
