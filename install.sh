#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv dOsint

echo "Installing dependencies..."
dOsint/bin/pip install -r requirements.txt

echo "Setup complete."
