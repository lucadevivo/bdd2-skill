#!/usr/bin/env bash
# Crea e popola i due database di esempio del corso nel container bdd2pg.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DB="$ROOT/corpus/database"

docker start bdd2pg >/dev/null 2>&1 || \
  docker run -d --name bdd2pg -e POSTGRES_HOST_AUTH_METHOD=trust -p 55432:5432 postgres:16-alpine

echo "attendo che PostgreSQL accetti connessioni..."
until docker exec bdd2pg pg_isready -U postgres >/dev/null 2>&1; do sleep 1; done

for db in accademia cielo; do
  docker exec bdd2pg psql -U postgres -q -c "drop database if exists $db;"
  docker exec bdd2pg psql -U postgres -q -c "create database $db;"
done

# l'ordine conta: domini e tabelle, poi i vincoli/trigger, poi i dati
docker exec -i bdd2pg psql -U postgres -d accademia -q < "$DB/accademia 3/domains-tables.sql"
docker exec -i bdd2pg psql -U postgres -d accademia -q < "$DB/accademia 3/constraints.sql"
docker exec -i bdd2pg psql -U postgres -d accademia -q < "$DB/accademia 3/data.sql"
docker exec -i bdd2pg psql -U postgres -d cielo     -q < "$DB/cielo/domains-tables.sql"
docker exec -i bdd2pg psql -U postgres -d cielo     -q < "$DB/cielo/data.sql"

echo
echo "Verifica:"
docker exec bdd2pg psql -U postgres -d accademia -c "\dt"
docker exec bdd2pg psql -U postgres -d cielo -c "\dt"
