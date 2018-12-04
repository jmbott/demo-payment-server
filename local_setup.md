# demo-payment-server

## Running locally
### Native

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ cd demo_payment && ./run.sh
03/12/2018-22:34:03 - *** Starting uWSGI 2.0.17.1 (64bit) on [Mon Dec  3 22:34:03 2018] ***
```

### Docker

* First make sure the Docker daemon is running

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
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


## Adding an initial user locally

Note that the login flow is quicker with a gmail.com e-mail address.

### Native

```
(venv) $ ./dev/commands.py create_user --kwarg email=<your_email_address>
Created user with e-mail your_email_address
```

### Docker

```
$ docker exec dev_minigrid_1 dev/commands.py create_user --db_host=db --kwarg email=<your_email_address>
Created user with e-mail your_email_address
```
