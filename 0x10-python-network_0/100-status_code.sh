#!/bin/bash
# Autor : Said LAMGHARI

curl -so /dev/null -w "%{http_code}" "$1"
