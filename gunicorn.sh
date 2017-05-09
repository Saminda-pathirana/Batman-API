#!/bin/bash
. venv/bin/activate
#gunicorn api:app -D --bind=0.0.0.0:5000 --reload
gunicorn api:app -w 2 --threads 4 -D --bind=0.0.0.0:5000 --reload