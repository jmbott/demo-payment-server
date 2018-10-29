#!/usr/bin/env sh
# Demo Payment Server installer for version 0.0.1
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
    $CURL -L https://github.com/docker/compose/releases/download/1.22.0/run.sh > docker-compose \
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

# Download the configuration files
printf "========================================\n"
printf " Generating configuration               \n"
printf "========================================\n"
$CURL -L https://raw.githubusercontent.com/jmbott/demo-payment-server/0.0.1/prod/docker-compose.yml > docker-compose.yml
$CURL -L https://raw.githubusercontent.com/jmbott/demo-payment-server/0.0.1/prod/nginx.conf > nginx.conf

printf "\n"
printf "Please enter an e-mail address for the  \n"
printf "administrator. This will be the only    \n"
printf "account that can log in at first.       \n"
printf "Administrator e-mail address:\n>>> "
read ADMIN_EMAIL
