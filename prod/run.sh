#!/usr/bin/env sh
uwsgi -s 127.0.0.1:8888 \
  --log-prefix=log/demo_payment.log \
  --protocol=http -w wsgi \
  --mount /=server:app
