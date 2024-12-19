import os
from dotenv import load_dotenv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from python.utils.logger import get_logger  # Assuming this is your custom logger

load_dotenv()


class CassandraClient:
    """
    A class to handle Cassandra database connections.
    """

    def __init__(self, keyspace, contact_points=None, port=9042):
        """
        Initialize the Cassandra client with the provided keyspace, contact points, and port.

        Args:
            keyspace (str): The keyspace to connect to.
            contact_points (list, optional): List of Cassandra nodes to connect to. Defaults to ["localhost"].
            port (int, optional): The port number for Cassandra connections. Defaults to 9042.
        """
        self.keyspace = keyspace
        self.contact_points = contact_points or ["localhost"]
        self.port = port
        self.cluster = None
        self.session = None
        self.logger = get_logger("Cassandra.log", namespace="Cassandra")

    def connect(self):
        """
        Establishes a connection to the Cassandra cluster and sets the keyspace.

        Raises:
            Exception: If connection to Cassandra fails.
        """
        try:
            self.logger.info("Initializing Cassandra cluster connection...")
            cassandra_user = os.getenv("CASSANDRA_USER")
            cassandra_password = os.getenv("CASSANDRA_PASSWORD")

            if not cassandra_user or not cassandra_password:
                missing_vars = []
                if not cassandra_user:
                    missing_vars.append("CASSANDRA_USER")
                if not cassandra_password:
                    missing_vars.append("CASSANDRA_PASSWORD")
                raise ValueError(
                    f"Missing required environment variables: {', '.join(missing_vars)}"
                )

            auth_provider = PlainTextAuthProvider(
                username=cassandra_user,
                password=cassandra_password,
            )
            self.cluster = Cluster(
                self.contact_points, auth_provider=auth_provider, port=self.port
            )
            self.session = self.cluster.connect()
            self.session.set_keyspace(self.keyspace)
            self.logger.info(
                f"Successfully connected to Cassandra keyspace: {self.keyspace}"
            )
        except Exception as error:
            self.logger.error(f"Error connecting to Cassandra: {error}")
            raise

    def get_session(self):
        """
        Returns the Cassandra session.

        Returns:
            cassandra.cluster.Session: The active Cassandra session.

        Raises:
            Exception: If the session is not established.
        """
        if not self.session:
            self.logger.error("Session is not initialized. Call 'connect()' first.")
            raise Exception("Session is not initialized. Call 'connect()' first.")
        return self.session

    def close(self):
        """
        Closes the Cassandra cluster connection gracefully.
        """
        if self.cluster:
            try:
                self.logger.info("Closing Cassandra cluster connection...")
                self.cluster.shutdown()
                self.session = None  # Reset session to None after closing
                self.logger.info("Cassandra cluster connection closed.")
            except Exception as error:
                self.logger.error(f"Error closing connection to Cassandra: {error}")
                raise
