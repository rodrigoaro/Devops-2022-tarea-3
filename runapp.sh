#!/bin/bash

echo "RUN SERVER"

# bash ./wait-for-it.sh -h db -p 5432 -t 120

sleep 10

python initdb.py

python main.py
