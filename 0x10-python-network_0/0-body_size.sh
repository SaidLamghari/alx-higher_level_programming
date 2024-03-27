#!/bin/bash
# Autor : Said LAMGHARI
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
