#!/usr/bin/env sh
uwsgi -s 127.0.0.1:8080 \
  --logdate="%d/%m/%Y-%H:%M:%S" \
  --protocol=http -w wsgi \
  --mount /demo_payment=server:app

#   --logto=logs/uwsgi.log \
