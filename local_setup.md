# demo-payment-server

## Running locally
### Native

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ ./dev/run.sh
03/12/2018-22:34:03 - *** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 22:34:03 2018] ***
```

### Docker

* First make sure the Docker daemon is running

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

You may need to run `docker-machine start default`, `docker-machine env`,
and/or `eval $(docker-machine env)` to start docker.

* If rebuilding container then,

```
$ docker-compose -f dev/docker-compose.yml build
```

* Then start the containers

```
$ docker-compose -f dev/docker-compose.yml up -d
$ docker-compose -f dev/docker-compose.yml ps
       Name                     Command               State           Ports
------------------------------------------------------------------------------------
dev_db_1             docker-entrypoint.sh postgres    Up      5432/tcp
dev_demo_payment_1   ./demo_payment/run.sh --db ...   Up      0.0.0.0:8889->8889/tcp            
```

* You should be able to [access containers](https://github.com/docker/for-win/issues/221#issuecomment-260028907)
from your container host using the container IP. You can use
`docker inspect <container ID>` to get your container's IP address.

```
$ docker inspect dev_demo_payment_1 | grep '"IPAddress":'
"IPAddress": "",
    "IPAddress": "172.21.0.3",
```

* Access container logs of the form,

```
docker exec -it -u root dev_demo_payment_1 tail -f /demo-payment-server/logs/uwsgi.log
```

## Adding an initial user locally

For manual edits use, `docker exec -it dev_demo_payment_1 /bin/bash`

### Native

* To launch postgres locally `pg_ctl -D /usr/local/var/postgres start` on OSX
  or `pg_ctl -D /var/lib/postgres/data -l logfile start` on arch
  * Follow [this guide](https://linuxhint.com/install-postgresql-10-arch-linux/)
    from install.
* [Create postgres user](https://www.postgresql.org/docs/current/sql-createrole.html),

```
$ psql -c 'create role postgres with login superuser' # only on OSX
$ psql -c 'create database demo_payment;' -U postgres
```

* To remove the database (in case of structure change)

```
$ psql -c 'drop database demo_payment;' -U postgres
```

* create user and stripe key,

```
(venv) [user@machine dir]$ python
>>> from dev import commands
>>> commands.createdb(True)
Created schema demo_payment
<sqlalchemy.orm.session.Session object at 0x105fe5710>
>>> commands.create_user('test@test')
Created user with e-mail test@test
>>> commands.create_stripe_key('sk_test_xxxxxxxxxx')
Added stripe key sk_test_xxxxxxxxxx
```

* To remove the demo_payment schema,

```
$ python
>>> commands.killdb()
You definitely want to kill the schema demo_payment? y/N y
Dropped schema
```

* login to postgres, `psql -U postgres`.
* Once logged in, list databases `\list`, connect to a database
  `\connect database_name`, list tables `\dt`, list users `\du`, list schemas
  `\dn`.

* To add your schema to the search path,

```
$ psql -U postgres
postgres=# \connect demo_payment
You are now connected to database "demo_payment" as user "postgres".
demo_payment=# SET search_path TO demo_payment;
SET
demo_payment=# \dt
List of relations
Schema    |    Name     | Type  |  Owner
--------------+-------------+-------+----------
demo_payment | key         | table | postgres
demo_payment | twilio_info | table | postgres
demo_payment | user        | table | postgres
(3 rows)
```

* To explore database contents,

```
demo_payment-# select column_name, data_type, character_maximum_length from
demo_payment-# INFORMATION_SCHEMA.COLUMNS where table_name = 'user';
 column_name | data_type | character_maximum_length
-------------+-----------+--------------------------
 user_id     | uuid      |
 email       | text      |
(2 rows)
demo_payment=# \d+ user
                                     Table "demo_payment.user"
 Column  | Type | Collation | Nullable |      Default       | Storage  | Stats target | Description
---------+------+-----------+----------+--------------------+----------+--------------+-------------
 user_id | uuid |           | not null | uuid_generate_v4() | plain    |              |
 email   | text |           | not null |                    | extended |              |
Indexes:
    "user_pkey" PRIMARY KEY, btree (user_id)
    "user_email_key" UNIQUE CONSTRAINT, btree (email)
Check constraints:
    "user_email_check" CHECK (email ~ '.*@.*'::text)
demo_payment=# SELECT * FROM demo_payment.user;
               user_id                |   email
--------------------------------------+-----------
 5abccab9-8538-4ac5-b8bd-6a14c922293e | test@test
(1 row)
```

### Docker

```
$ docker exec -it dev_demo_payment_1 chmod +x /demo-payment-server/prod/create_initial_user.py
$ docker exec -it dev_demo_payment_1 /demo-payment-server/prod/create_initial_user.py --dbhost dev_db_1 --email example@example.com
Created schema demo_payment
Created initial user with e-mail example@example.com
```
