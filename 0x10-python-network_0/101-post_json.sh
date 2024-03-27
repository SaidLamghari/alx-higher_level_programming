#!/bin/bash
# Autor: Said LAMGHARI
jq . "$2" >/dev/null 2>&1 && curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1" || echo "Not a valid JSON" >&2
