#!/bin/bash

source /etc/flash-hunters/database_env.sh
# source etc/database_env.sh

cd "$SCRAPING_PATH" || exit 1

mkdir -p out

if ! venv/bin/python -m src.scrape; then
  echo "Error while scanning data from web."
  exit 1
fi
echo "Scan completed."

if [ -n "$DB_USER" ]; then
  uri_prefix="$DB_USER@"
else
  uri_prefix=""
fi

if [ -n "$DB_PASSWORD" ]; then
  password_option="--password \"$DB_PASSWORD\""
else
  password_option=""
fi

if [ -n "$DB_AUTHENTICATION_DB" ]; then
  authentication_option="--authenticationDatabase $DB_AUTHENTICATION_DB"
else
  authentication_option=""
fi

mongoimport --uri "mongodb://$uri_prefix$DB_SERVER:$DB_PORT" $password_option \
  --db invaders --collection mosaic --mode merge --upsertFields id \
  --file out/mosaic.json --jsonArray

rm out/mosaics.json
