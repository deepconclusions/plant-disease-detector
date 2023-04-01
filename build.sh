#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip

pip install tensorflow

pip install --upgrade Pillow

poetry install

python manage.py collectstatic --no-input
python manage.py migrate

pip install --force-reinstall -U setuptools