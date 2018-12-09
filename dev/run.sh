#!/usr/bin/env sh
python demo_payment/config_create.py --schema demo_payment_dev --debug
uwsgi --yaml wsgi_config.yaml --log-date='%d/%m/%Y-%H:%M:%S'
