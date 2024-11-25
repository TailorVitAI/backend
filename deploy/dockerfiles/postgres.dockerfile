FROM postgres:14.7-alpine3.17

COPY deploy/entrypoints/postgres.sh /docker-entrypoint-initdb.d/

VOLUME /var/lib/postgresql/data/

# Replace `postgres` according to `POSTGRES_USER` variable in `./deploy/environments/postgres.env`
HEALTHCHECK --start-period=5s --interval=5s --timeout=5s --retries=5 CMD pg_isready -U postgres
