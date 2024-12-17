import os

from python.utils.logger import get_logger
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

logger = get_logger("Cassandra.log", namespace="Cassandra")


def get_cassandra_session(keyspace):
    try:
        auth_provider = PlainTextAuthProvider(
            username=os.getenv("CASSANDRA_USER"),
            password=os.getenv("CASSANDRA_PASSWORD"),
        )
        cluster = Cluster(["localhost"], auth_provider=auth_provider)
        session = cluster.connect()
        session.set_keyspace(keyspace)
        return session
    except Exception as error:
        logger.error(f"Error connecting to Cassandra: {error}")
        raise
