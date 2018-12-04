"""Application-level Options."""
from functools import partial
import os

path = partial(os.path.join, os.path.dirname(__file__))
path.__doc__ = 'Full path relative to the directory of this file.'

class options():
    """options available."""

    def __init__(self, application_debug, demo_payment_website_url,
                 demo_payment_https, demo_payment_port, db_host, db_port,
                 db_database, db_schema, db_user, db_password):
        self.application_debug = False
        self.demo_payment_website_url = 'http://localhost:8889'
        self.demo_payment_https = True
        self.demo_payment_port = 8889
        self.db_host = 'localhost'
        self.db_port = 5432
        self.db_database = 'demo_payment'
        self.db_schema = 'demo_payment'
        self.db_user = 'postgres'
        self.db_password = 'password'

# define(
#     'application_debug', default=False,
#     help='Dangerous option that shows debug information for any error.'
# )
# define(
#     'demo_payment_website_url', default='http://localhost:8889',
#     help='The URL of this instance of the demo payment server.'
# )
# define('demo_payment_https', default=True)
# define('demo_payment_port', default='8889')
# define('db_host', default='localhost')
# define('db_port', default=5432)
# define('db_database', default='demo_payment')
# define('db_schema', default='demo_payment')
# define('db_user', default='postgres')
# define('db_password', default='password')
