#!/usr/bin/env bash
# Exit on error
set -o errexit

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements/production.txt

# Make sure we're in the correct directory
cd $RENDER_PROJECT_DIR

# Convert static asset files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate 