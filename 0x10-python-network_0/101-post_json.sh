#!/bin/bash
# Autor: Said LAMGHARI
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
