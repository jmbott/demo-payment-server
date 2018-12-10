#!/usr/bin/env sh
python demo_payment/config_create.py
uwsgi --yaml wsgi_config.yaml --log-date='%d/%m/%Y-%H:%M:%S'
