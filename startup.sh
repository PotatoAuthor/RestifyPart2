#!/bin/bash

RED='\033[0;31m'
GRN='\033[0;32m'
NC='\033[0m'

# Check if running linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo -e "${GRN}Good!${NC} This is running linux"
  echo -e "${RED}Ensure you are running Ubuntu 20.04 LTS${NC}"

  sudo apt install python3.10-venv

  python3 -m venv ./venv/
  source ./venv/bin/activate

  if [[ "$VIRTUAL_ENV" != "" ]]
    then
      python3 -m pip install --upgrade pip
      python3 -m pip install django
      python3 -m pip install django-filter
      python3 -m pip install djangorestframework
      python3 -m pip install --upgrade Pillow
      python3 -m pip install djangorestframework-simplejwt

    else
      echo -e "${RED}ERROR: FAILED TO INSTALL VIRTUAL ENV"
    fi


  python3 ./restify/manage.py makemigrations
  python3 ./restify/manage.py migrate


# Give error if running script on MacOS
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo -e "${RED}ERROR: This is MacOS - Please run on Ubuntu 20.04 LTS${NC}"

  python3 -m venv ./venv/
  source ./venv/bin/activate
  python3 -m pip install --upgrade pip
  python3 -m pip install django
  python3 -m pip install django-filter
  python3 -m pip install djangorestframework
  python3 -m pip install --upgrade Pillow
  python3 -m pip install djangorestframework-simplejwt

  python3 ./restify/manage.py makemigrations
  python3 ./restify/manage.py migrate
fi
