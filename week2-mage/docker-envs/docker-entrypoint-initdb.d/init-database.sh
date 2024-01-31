#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" <<-EOSQL
    CREATE USER mage WITH PASSWORD 'mage';
    CREATE DATABASE mage;
    GRANT ALL PRIVILEGES ON DATABASE mage TO mage;
 
EOSQL

psql -v ON_ERROR_STOP=1 --username "${POSTGRES_USER}" -d "mage" <<-EOSQL
   GRANT ALL ON SCHEMA public TO mage;
EOSQL
