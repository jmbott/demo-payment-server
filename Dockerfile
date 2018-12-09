FROM python:3.7.1
COPY . /demo-payment-server
WORKDIR /demo-payment-server
RUN set -x \
  && pip install --no-cache-dir -r requirements.txt \
  && useradd -r -d /demo-payment-server -s /sbin/nologin demo_payment \
  && chown -R demo_payment:demo_payment .
USER demo_payment
CMD ["./prod/run.sh"]
EXPOSE 8889
