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

if [ -z "$DB_USER" ]; then
  uri_prefix=""
else
  if [ -n "$DB_PASSWORD" ]; then
    uri_prefix="$DB_DB_USER:$DB_PASSWORD"
  else
    uri_prefix="$DB_DB_USER"
  fi
fi

mongoimport --uri "mongodb://$uri_prefix@$DB_SERVER:$DB_PORT" \
  --db invaders --collection mosaic --mode merge --upsertFields id \
  --file out/mosaic.json --jsonArray

rm out/mosaics.json
