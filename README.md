# demo-payment-server

Web server exploring different payment and messaging platforms and their
security methodology

[![Build Status](https://travis-ci.com/jmbott/demo-payment-server.svg?branch=master)](https://travis-ci.com/jmbott/demo-payment-server)

Demo Server: [https://demo-payment-server.duckdns.org](https://demo-payment-server.duckdns.org)

## Setup

For full setup follow the `docs/launch_aws_server.md` guide.

For local setup see the **local_setup.md** file.

## Overview

Web server to demo different payment and messaging platforms. Uses the
[Flask](http://flask.pocoo.org/) microframework for Python,
[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) to contain the application,
[Docker](https://www.docker.com/) to containerize the project,
[Let's Encrypt](https://letsencrypt.org/) and [certbot](https://certbot.eff.org/about/) 
for free ssl certificates, and Travis CI for continuous integration and testing.

Docker containers for [NGINX](https://nginx.org/),
[PostgreSQL](https://www.postgresql.org/), and the Flask Python application.

Currently shows tests for `Stripe` and `Twilio`. Plans to add additional tests
for `M-Pesa` and `Bitpay`.

Uses [flask sessions](http://flask.pocoo.org/docs/1.0/api/#sessions) to handle
authentication.

**requirements.txt**

Set of Python requirements listed with version numbers for consistent installs.

**Dockerfile**

A text document that contains all the commands a user could call on the command
line to assemble a Docker image. In this case for the demo_payment docker
container.

**.travis.yml**

[YAML](https://en.wikipedia.org/wiki/YAML) configuration file for
[Travis CI](https://travis-ci.org/); a Continuous Integration tool.

**.gitignore & .dockerignore**

Files that indicate what to ignore when using `git` and `docker` respectively.

**/demo_payment**

Web server code base.

**/prod**

Production code install scripts and setup files.

**/dev**

Development install scripts and setup files.

**/tests**

Folder for tests.

**/docs**

Contains server setup and design docs.

**/log**

Folder for log files.

## References

* [Docker Docs](https://docs.docker.com/)
* [Flask Docs](http://flask.pocoo.org/docs/1.0/)
* [Travis CI Docs](https://docs.travis-ci.com/)
* [NGINX Docs](https://nginx.org/en/docs/)
* [PostgreSQL docs](https://www.postgresql.org/docs/)
* [Portier Docs](https://portier.github.io/using.html)
* [Stripe API](https://stripe.com/docs/api)
* [Bitpay API](https://bitpay.com/api)
* [M-Pesa](https://developer.safaricom.co.ke/docs#m-pesa-apis)
* [EC2 Documentation](https://docs.aws.amazon.com/ec2/index.html#lang/en_us)
  * Could use EC2 API for auto setup in the future
