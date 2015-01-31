#!/bin/sh

nohup python ./manage.py runserver 0.0.0.0:8000 &> /dev/null &

