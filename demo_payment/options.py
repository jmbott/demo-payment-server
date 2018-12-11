"""Application-level Options."""
import argparse
from functools import partial
import os

path = partial(os.path.join, os.path.dirname(__file__))
path.__doc__ = 'Full path relative to the directory of this file.'

parser = argparse.ArgumentParser(description='Process Application Options.')
parser.add_argument('-d', '--debug', dest='application_debug',
                    action='store_true', help='enter debug mode')
parser.add_argument('-u', '--url', dest='demo_payment_website_url',
                    default='localhost:8889', help='set website url')
# set demo_payment_https default true set false when certbot is setup
parser.add_argument('-s', '--https', dest='demo_payment_protocol',
                    action='store_true', help='https set')
parser.add_argument('-p', '--port', dest='demo_payment_port', type=int,
                    default='8889', help='port for demo payment server')
parser.add_argument('-b', '--dbhost', dest='db_host',
                    default='localhost', help='set database host')
parser.add_argument('-o', '--dbport', dest='db_port', type=int, default=5432,
                    help='port for postgres database')
parser.add_argument('-a', '--db', dest='db_database',
                    default='demo_payment', help='set database name')
parser.add_argument('-c', '--schema', dest='db_schema', default='demo_payment',
                    help='set database schema')
parser.add_argument('-r', '--dbuser', dest='db_user', default='postgres',
                    help='set database user')
parser.add_argument('-w', '--dbpass', dest='db_password', default='password',
                    help='set database password')
parser.add_argument('-e', '--email', dest='admin_email',
                    help='set admin email')

options = parser.parse_args()
