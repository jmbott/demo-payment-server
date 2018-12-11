"""Database Models."""

import sqlalchemy as sa

from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from contextlib import contextmanager

from demo_payment.options import options


metadata = sa.MetaData(schema=options.db_schema)
Base = declarative_base(metadata=metadata)


sa.event.listen(
    Base.metadata, 'before_create',
    sa.DDL(f"""
        ALTER DATABASE {options.db_database} SET TIMEZONE TO "UTC";
        CREATE SCHEMA IF NOT EXISTS public;
        CREATE SCHEMA IF NOT EXISTS {options.db_schema};
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA pg_catalog;
    """))


def create_engine():
    """Connect to the database using the application-level options."""
    connection_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        options.db_user, options.db_password, options.db_host,
        options.db_port, options.db_database)
    return sa.create_engine(connection_string)


@contextmanager
def transaction(session): # noqa
    """Provide a transactional scope around a series of operations.
    Taken from http://docs.sqlalchemy.org/en/latest/orm/session_basics.html
    #when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it
    """
    try:
        yield session
        session.commit()
    except BaseException:
        session.rollback()
        raise


def pk():
    """Return a primary key UUID column."""
    return sa.Column(
        pg.UUID, primary_key=True, server_default=func.uuid_generate_v4())


def fk(foreign_column):
    """Return a foreign key."""
    return sa.Column(
        pg.UUID, sa.ForeignKey(foreign_column))


class User(Base):
    """The model for a registered user."""

    __tablename__ = 'user'
    user_id = pk()
    email = sa.Column(
        pg.TEXT, sa.CheckConstraint("email ~ '.*@.*'"),
        nullable=False, unique=True)


class Stripe(Base):
    """The model for Stripe Key."""

    __tablename__ = 'key'
    key_id = pk()
    api_key = sa.Column(
        pg.TEXT, sa.CheckConstraint("api_key ~ 'sk_.*'"),
        nullable=False, unique=True)
