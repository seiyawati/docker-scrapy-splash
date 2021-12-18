#!/usr/bin/env bash
#wait for the MySQL Server to come up
#sleep 90s

#run the setup script to create the DB and the schema in the DB
mysql -u buyma -p buyma < "/docker-entrypoint-initdb.d/001-create-tables.sql"

if [ $? -eq 0 ]; then
  echo "Successfully created table."
else
  echo "Failed to create the table."
fi
