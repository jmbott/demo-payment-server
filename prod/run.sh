#!/usr/bin/env sh
python demo_payment/config_create.py --url 0.0.0.0:8889
uwsgi --yaml wsgi_config.yaml \
  --log-date='%d/%m/%Y-%H:%M:%S' \
  --logto=logs/uwsgi.log
