#!/usr/bin/env python
"""Create the initial administrator for the application."""
import os
import sys
from sqlalchemy import func
from sqlalchemy.exc import OperationalError, InternalError
from time import sleep

sys.path.insert(1, os.path.join(sys.path[0], '..'))


def main():
    """Supply the administrator's e-mail."""
    from demo_payment import server
    from demo_payment import models
    from demo_payment.options import options
    session = server.create_session(ensure=True)
    try:
        users = session.query(func.count(models.User.user_id)).scalar()
    except OperationalError:
        print('Database connection failed... trying again in 2 seconds.')
        sleep(2)
    users = session.query(func.count(models.User.user_id)).scalar()
    if users:
        print('At least one user already exists. Log in as that user.')
        sys.exit(1)
    with models.transaction(session) as tx_session:
        tx_session.add(models.User(email=options.admin_email))
    print('Created initial user with e-mail', options.admin_email)


if __name__ == '__main__':
    main()
