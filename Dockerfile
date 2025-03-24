FROM postgres:17

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB gis

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-17-postgis-3 \
        postgresql-17-postgis-3-scripts \
        postgresql-17-pgrouting \
        gdal-bin \
        wget \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY ./init-db.sh /docker-entrypoint-initdb.d/

EXPOSE 5432

WORKDIR /var/lib/postgresql

# Use the default entrypoint and command from the postgres image
