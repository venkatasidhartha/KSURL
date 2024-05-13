#!/bin/bash

# Create Database folder if not exists in the current directory
if [ ! -d "Database" ]; then
    mkdir Database
    echo "Database folder created."
fi

# Create logs folder if not exists in the current directory
if [ ! -d "logs" ]; then
    mkdir logs
    echo "logs folder created."
fi