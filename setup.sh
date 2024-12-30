#!/bin/bash

# Update package lists
apt-get update

# Install dependencies for pillow (libjpeg, zlib, freetype, etc.)
apt-get install -y libjpeg-dev zlib1g-dev libfreetype6-dev

# Install pip and dependencies
pip install --upgrade pip
pip install -r requirements.txt
