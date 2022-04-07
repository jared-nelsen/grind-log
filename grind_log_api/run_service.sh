#!/bin/bash

# Start the Grind Log API server in Prod

echo 'Starting Grind Log API server...'
export FLASK_APP=grind_log_api.py
flask run -h localhost -p 5001
