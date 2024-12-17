import os
import psycopg2
from python.utils.logger import get_logger
from psycopg2 import sql

logger = get_logger("PostgreSQL.log", namespace="PostgreSQL")


def get_postgres_connection(database):
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database=database,
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )
        return connection
    except Exception as error:
        logger.error(f"Error connecting to PostgreSQL: {error}")
        raise
