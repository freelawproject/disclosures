#!/bin/bash
gunicorn disclosures.wsgi:application --bind 0.0.0.0:5050 --timeout 3600
exec "$@"