"""Application-level Options."""
from functools import partial
import os
import secrets

path = partial(os.path.join, os.path.dirname(__file__))
path.__doc__ = 'Full path relative to the directory of this file.'


define(
    'application_debug', default=False,
    help='Dangerous option that shows debug information for any error.'
)
define(
    'demo_payment_website_url', default='http://localhost:8889',
    help='The URL of this instance of the demo payment server.'
)
define('demo_payment_https', default=True)
define('demo_payment_port', default='8889')
define('db_host', default='localhost')
define('db_port', default=5432)
define('db_database', default='demo_payment')
define('db_schema', default='demo_payment')
define('db_user', default='postgres')
define('db_password', default='password')
define('redis_url', default='redis://localhost:6379/0')
