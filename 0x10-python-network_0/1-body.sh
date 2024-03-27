#!/bin/bash
# Autor : Said LAMGHARI
curl -sL -w "%{http_code}" -o /dev/null "$1" | { read -r c; [ $c -eq 200 ] && curl -sL "$1" ; }
