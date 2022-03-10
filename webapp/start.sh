#!/bin/bash
python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
python -m pip install --upgrade pip&&
pip install uwsgi&&
uwsgi --ini /Eastridge/webapp/uwsgi.ini