#!/usr/bin/env sh
python demo_payment/config_create.py --url 'www.example.com'
uwsgi --yaml wsgi_config.yaml \
  --log-date='%d/%m/%Y-%H:%M:%S' \
  --logto=logs/uwsgi.log
