import time

from concurrent.futures import ThreadPoolExecutor
from cassandra.cluster import Cluster
from python.utils.api_utils import get_url, test_endpoint
from python.utils.logger import get_logger

# Connect to Cassandra
cluster = Cluster(["localhost"])
session = cluster.connect("raw_league_data")

# Log Information
logger = get_logger("match_crawler.log", namespace="match_crawler")


def get_most_recent_puuid(region):
    try:
        # Correctly formatted query
        query = "SELECT puuid, DateAdded FROM puuids WHERE region = %s"

        # Pass parameter as a tuple with a trailing comma
        results = session.execute(query, (region,))
        sorted_results = sorted(results, key=lambda row: row.DateAdded, reverse=True)
        if sorted_results:
            result = sorted_results[0].puuid if sorted_results else None
            print(f"Most Recent PUUID in {region}: {sorted_results[0].puuid}")

        if result:
            print(
                f"Most Recent PUUID in {region}: {result.puuid}, DateAdded: {result.DateAdded}"
            )
            return result.puuid
        else:
            print(f"No PUUID found for region: {region}")
            return None
    except Exception as e:
        print(f"Error querying PUUID for region {region}: {e}")
        return None


def add_puuid(puuid, region):
    try:
        # Correctly formatted query
        query = """INSERT INTO puuids (puuid, region, DateAdded) VALUES (%s, %s, toTimestamp(now()))
                    IF NOT EXISTS"""

        # Pass parameters as a tuple
        session.execute(query, (puuid, region))
        print(f"PUUID {puuid} added for region {region}")
    except Exception as e:
        print(f"Error adding PUUID {puuid} for region {region}: {e}")


if __name__ == "__main__":
    default_puuid = (
        "HHk7hueAv-6OIn3vv7xOVPxIB_ARB2z9IAf7p5w14pbRN1COH0bCY5jZEXYioHKIaf3AMj3Ntuhvvg"
    )

    summoner_puuid = get_most_recent_puuid("americas") or default_puuid

    if summoner_puuid:
        print(f"Using summoner puuid: {summoner_puuid}")
        add_puuid(summoner_puuid, "americas")

        # Fetch and display all PUUIDs for the region
        results2 = session.execute(
            "SELECT puuid, region, DateAdded FROM puuids WHERE region = %s",
            ("americas",),
        )
        print("Inserted PUUIDs for region 'americas':")
        for row in results2:
            print(
                f"PUUID: {row.puuid}, Region: {row.region}, DateAdded: {row.dateadded}"
            )
