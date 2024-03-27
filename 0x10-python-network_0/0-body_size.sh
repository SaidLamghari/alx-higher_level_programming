#!/bin/bash
# This script takes in a URL
# Sends a request to URL
# The size of the body
# Autor : Said LAMGHARI

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
