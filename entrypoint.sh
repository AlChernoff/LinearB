#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver 127.0.0.1:8001