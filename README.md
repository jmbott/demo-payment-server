# demo-payment-server

Web server exploring different payment platforms and their security methodology

## Setup

For full setup follow the `docs/launch_aws_server.md` guide.

## Overview

Web server to demo different payment platforms. Uses the
[Flask](http://flask.pocoo.org/) microframework for Python,
[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) to contain the application,
[Docker](https://www.docker.com/) to containerize the project, and Travis CI
for continuous integration and testing.

Docker containers for [NGINX](https://nginx.org/),
[PostgreSQL](https://www.postgresql.org/), and the Flask Python application.

Shows tests for `M-Pesa`, `Stripe`, and `Bitpay`.

Uses email-based password-less authentication service `Portier`.

**server.py**

Main Flask application file.

**wsgi.py**

[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
entry point for Flask application.

**requirements.txt**

Set of Python requirements listed with version numbers.

**Dockerfile**

A text document that contains all the commands a user could call on the command
line to assemble a Docker image.

**.travis.yml**

[YAML](https://en.wikipedia.org/wiki/YAML) configuration file for
[Travis CI](https://travis-ci.org/); a Continuous Integration tool.

**.gitignore & .dockerignore**

Files that indicate what to ignore when using `git` and `docker` respectively.

**/demo_payment**

Web server code base.

**/prod**

Production code install scripts and setup.

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
