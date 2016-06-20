#!/bin/bash

# Generate site and fork the process to background. -r is auto-reload if changes are made.
pelican -r content -o output -s pelicanconf.py &

# Sleep for 2 seconds to ensure that initial site generation is done before trying to change directory
sleep 2

# Serve site
cd output && python -m pelican.server 8000
