#!/usr/bin/env bash

echo "BUILD START"
python3 -m pip install --upgrade pip
rm -rf staticfiles_build 
mkdir staticfiles_build  
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput 
echo "BUILD END"



