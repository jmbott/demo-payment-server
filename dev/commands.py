#!/usr/bin/env python
"""Commands useful during development."""

import os
import sys

from sqlalchemy.orm import sessionmaker

sys.path.insert(1, os.path.join(sys.path[0], '..'))


def createdb(ensure=True):
    """Create the schema and tables and return a Session."""
    from demo_payment import models
    engine = models.create_engine()
    if ensure:
        models.Base.metadata.create_all(engine)
        print(f'Created schema {models.Base.metadata.schema}')
    return sessionmaker(bind=engine)()


def create_user(email):
    """Create a user with the given e-mail."""
    from demo_payment import models
    session = createdb(ensure=False)
    with models.transaction(session) as tx_session:
        tx_session.add(models.User(email=email))
    print('Created user with e-mail ' + email)


def create_stripe_key(key):
    """Add a new Stripe api_key to the DB."""
    from demo_payment import models
    session = createdb(ensure=False)
    with models.transaction(session) as session:
        # See your keys here: https://dashboard.stripe.com/account/apikeys
        session.add(models.Stripe(api_key=key))
    print('Added stripe key ' + key)


def create_twilio_info(sid, token, dest, orig):
    """Add new Twilio info to the DB."""
    from demo_payment import models
    session = createdb(ensure=False)
    with models.transaction(session) as session:
        # Your Account SID and Auth Token from twilio.com/console
        session.add(models.Twilio(account_sid=sid))
        session.add(models.Twilio(aauth_token=token))
        session.add(models.Twilio(dest_num=dest))
        session.add(models.Twilio(orig_num=orig))
    print('Added twilio sid ' + sid)
    print('Added twilio token ' + token)
    print('Added twilio dest ' + dest)
    print('Added twilio orig ' + orig)


def killdb():
    """Drop the schema."""
    from demo_payment import models
    answer = input('You definitely want to kill the schema demo_payment? y/N ')
    if not answer.lower().startswith('y'):
        print('Not dropping the schema')
        return
    engine = models.create_engine()
    engine.execute('DROP SCHEMA demo_payment CASCADE')
    print('Dropped schema')
