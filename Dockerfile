FROM python:3.7.1
COPY . /demo_payment
WORKDIR /demo_payment
RUN set -x \
  && pip install --no-cache-dir -r requirements.txt \
  && useradd -r -d /demo_payment -s /sbin/nologin demo_payment \
  && chown -R demo_payment:demo_payment .
USER demo_payment
CMD ["(cd demo_payment && ./run.sh)"]
EXPOSE 8889
