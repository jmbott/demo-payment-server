#!/usr/bin/env sh
# Demo Payment Server installer for version 0.0.2
set -e

# Do you have docker installed?
if ! command -v docker > /dev/null; then
  printf "You need to install docker\n"
  exit 1
fi

# Do you have sed installed?
if ! command -v sed > /dev/null; then
  printf "You need to install sed\n"
  exit 1
fi

# Do you have curl installed?
if command -v curl > /dev/null; then
  CURL=curl
else
  CURL="docker run tutum/curl curl"
fi

# Do you have docker-compose installed?
if command -v docker-compose > /dev/null; then
  DOCKER_COMPOSE=docker-compose
else
  DOCKER_COMPOSE=./docker-compose
  if ! [ -f ./docker-compose ]; then
    printf "========================================\n"
    printf " Installing docker-compose in this      \n"
    printf " directory                              \n"
    printf "========================================\n"
    $CURL -L https://github.com/docker/compose/releases/download/1.23.2/run.sh > docker-compose \
      && chmod +x docker-compose
    ./docker-compose -v
  fi
fi

# Ask for domain(s)
printf "========================================\n"
printf " Please enter your domain name(s) (space\n"
printf " separated)                             \n"
printf "                                        \n"
printf " Hint: for www include both             \n"
printf " >>> www.your.domain your.domain        \n"
printf "                                        \n"
printf " For a subdomain just give              \n"
printf " >>> subdomain.your.domain              \n"
printf "========================================\n"
printf "Domain(s):\n>>> "
read DOMAINS
LETSENCRYPT_DIR=$(echo $DOMAINS | cut -d' ' -f1)
DOMAIN_ARGS=$(echo $DOMAINS | sed -r s/\([^\ ]+\)/-d\ \\1/g)

# Add ...
# Run letsencrypt

# Add ...
# Run openssl dhparam

# Download the configuration files
printf "========================================\n"
printf " Generating configuration               \n"
printf "========================================\n"
$CURL -L https://raw.githubusercontent.com/jmb2341/demo-payment-server/0.0.2/prod/docker-compose.yml > docker-compose.yml
$CURL -L https://raw.githubusercontent.com/jmb2341/demo-payment-server/0.0.2/prod/nginx.conf > nginx.conf

# Add ...
#sed -i s/www.example.com/$LETSENCRYPT_DIR/g docker-compose.yml
#sed -i s/www.example.com/$LETSENCRYPT_DIR/g nginx.conf

printf "\n"
printf "Please enter an e-mail address for the  \n"
printf "administrator. This will be the only    \n"
printf "account that can log in at first.       \n"
printf "Administrator e-mail address:\n>>> "
read ADMIN_EMAIL

# Bring up the server
printf "========================================\n"
printf " Starting demo-payment server.          \n"
printf "                                        \n"
printf " You can view the status of the         \n"
printf " containers by running:                 \n"
printf " $DOCKER_COMPOSE ps\n"
printf "========================================\n"
$DOCKER_COMPOSE up -d
DEMO_PAYMENT_CONTAINER_NAME=$($DOCKER_COMPOSE ps | grep _demo_payment_ | cut -d' ' -f1)
sleep 1
docker exec $DEMO_PAYMENT_CONTAINER_NAME ""prod/create_initial_user.py --db-host=db --email=$ADMIN_EMAIL""
NGINX_CONTAINER_NAME=$($DOCKER_COMPOSE ps | grep _nginx_ | cut -d' ' -f1)

# Let's Encrypt auto-renew (for now this is a cron job).
printf "========================================\n"
printf " Adding twice-daily cron job to renew   \n"
printf " SSL certificate.                       \n"
printf "========================================\n"

printf "Not all stages complete..."
# Add ...
