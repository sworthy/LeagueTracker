#!/bin/bash

echo "Starting Cassandra initialization..."

# Wait for Cassandra to be ready
for i in {1..12}; do
  echo "Checking if Cassandra is ready..."
  if cqlsh cassandra -e 'DESCRIBE KEYSPACES'; then
    echo "Cassandra is ready!"
    break
  fi
  echo "Cassandra is not ready, retrying in 5 seconds..."
  sleep 5
done

# Exit if Cassandra is still not ready
if ! cqlsh cassandra -e 'DESCRIBE KEYSPACES'; then
  echo "Cassandra did not become ready in time. Exiting."
  exit 1
fi

# Execute initialization scripts
echo "Loading Cassandra keyspaces and data..."
cqlsh cassandra -f /cql_init/01_create_keyspaces.cql
cqlsh cassandra -f /cql_init/02_seed_data.cql

echo "Cassandra initialization completed successfully."
