#!/usr/bin/env sh
# python demo_payment/config_create.py --url 'www.example.com'
python demo_payment/config_create.py --url '127.0.0.1:8889'
uwsgi --yaml wsgi_config.yaml \
  --logto=logs/uwsgi.log \
  --uid 1001
