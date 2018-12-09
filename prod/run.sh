#!/usr/bin/env sh
uwsgi -s 0.0.0.0:8889 \
  --logdate="%d/%m/%Y-%H:%M:%S" \
  --uid 1001 \
  --protocol=http -w demo_payment.wsgi \
  --mount /demo-payment-server=demo_payment.server:app

# --logto=logs/uwsgi.log \
