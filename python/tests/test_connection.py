
import os
import psycopg2
from dotenv import load_dotenv
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

load_dotenv()

postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
cassandra_user = os.getenv("CASSANDRA_USER")
cassandra_password = os.getenv("CASSANDRA_PASSWORD")


def postgres_test():
    try: 
        # Connect to the postgres server
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="LeagueTracker",
            user=f"{postgres_user}",
            password=f"{postgres_password}"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        postgres_version = cursor.fetchone()
        print(f"PostgreSQL version: {postgres_version}")
        
    except Exception as error:
        print(f"Error connecting to postgres: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def cassandra_test():
    try:
        # connect to the cassandra server
        auth_provider = PlainTextAuthProvider({cassandra_user},{cassandra_password})
        cluster = Cluster(['localhost'], auth_provider=auth_provider)
        session = cluster.connect()
        
        # Set Keyspace
        keyspace = "leaguetracker"
        session.set_keyspace(keyspace)
        print(f"Connected to Cassandra Keyspace: {keyspace}")
        
        # Run a simple Query
        rows = session.execute("SELECT release_version FROM system.local;")
        for row in rows:
            print(f"Cassandra version: {row.release_version}")
            
        cluster.shutdown() 
    except Exception as error:
        print(f"Error connecting to Cassandra: {error}")
        
# Test Connections
if __name__ == "__main__":
    print("Testing postgres connection")
    postgres_test()
    print("Testing cassandra connection")
    cassandra_test()
        
