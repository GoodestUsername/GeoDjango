#!/bin/bash
set -e

# Run these commands as the postgres user
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Create extensions
    CREATE EXTENSION IF NOT EXISTS postgis;
    CREATE EXTENSION IF NOT EXISTS postgis_topology;
    CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
    CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder;
    CREATE EXTENSION IF NOT EXISTS pgrouting;

    -- Grant privileges
    ALTER DATABASE $POSTGRES_DB SET search_path TO public, topology, tiger;

    -- Optional: create a separate schema for your routing data
    CREATE SCHEMA IF NOT EXISTS routing;
    GRANT ALL ON SCHEMA routing TO $POSTGRES_USER;

    -- Log the PostGIS version
    SELECT PostGIS_full_version();

    -- Log the pgRouting version
    SELECT pgr_version();
EOSQL

echo "PostGIS and pgRouting have been initialized."
