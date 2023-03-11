#!/bin/bash

python3 -m venv ./venv/
source ./venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install django
python3 -m pip install djangorestframework
python3 -m pip install --upgrade Pillow
python3 -m pip install djangorestframework-simplejwt