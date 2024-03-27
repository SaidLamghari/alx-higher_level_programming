#!/bin/bash
# Autor : Said LAMGHARI 
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
