#!/bin/bash

# Develop Grind Log API Locally

echo 'Starting Grind Log API server...'
fuser -k 5001/tcp
gnome-terminal -e 'sh -c "echo ''Grind Log server...''; export FLASK_APP=grind_log_api.py; flask run -h localhost -p 5001;"'