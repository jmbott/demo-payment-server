#!/usr/bin/env sh
uwsgi --json wsgi_config.json:app

# uwsgi -s 127.0.0.1:8889 \
#   --logdate="%d/%m/%Y-%H:%M:%S" \
#   --protocol=http -w demo_payment.wsgi \
#   --mount /demo-payment-server=demo_payment.server:app

# --logto=logs/uwsgi.log \
