#!/bin/sh
export FLASK_DEBUG=1
export FLASK_APP=./create-kvm-on-host/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0 -p 5000
