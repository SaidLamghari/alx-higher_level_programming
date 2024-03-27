#!/bin/bash
# Autor : Said LAMGHARI
curl -sL -w "%{http_code}" -o /dev/null "$1" | {
    read -r status_code
    if [ "$status_code" -eq 200 ]; then
        curl -sL "$1"
    fi
}
