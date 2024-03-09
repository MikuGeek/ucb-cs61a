#!/bin/bash

# Filter and remove __pycache__ folders
find . -type d -name "__pycache__" -exec rm -rf {} +

# Filter and remove files with .ok_history and .ok_storage in their names
find . -type f \( -name "*.ok_history" -o -name "*.ok_storage" \) -exec rm -f {} +