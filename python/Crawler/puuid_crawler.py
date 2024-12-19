import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from python.utils.Cassandra import CassandraClient
from python.utils.api_utils import get_url, call_endpoint
from python.utils.logger import get_logger

"""Manages League of Legends match and player data retrieval and storage. Provides functionality to fetch player identifiers,
    match histories, and persist data in a Cassandra database.

    The module handles interactions with the Riot Games API, including retrieving player PUUIDs, fetching match histories, 
    and storing player and match information. It supports operations across different regions and provides logging and error handling.

Functions:
    get_most_recent_puuid(region): Retrieves the most recently added PUUID for a given region.
    get_matches(region, puuid): Fetches recent match identifiers for a specific player.
    add_puuid(puuid, region): Adds a new PUUID to the database.
    add_match(puuid, match_id, region): Stores a match identifier for a specific player.
"""

# Initialize Cassandra Client
cassandra_client = CassandraClient(keyspace="raw_league_data")
cassandra_client.connect()
session = cassandra_client.get_session()

# Log Information
logger = get_logger("match_crawler.log", namespace="match_crawler")

# Throttling Parameters
REQUESTS_PER_SECOND = 20
REQUESTS_PER_TWO_MINUTES = 100
SLEEP_INTERVAL = 1  # 1 second delay between requests if throttling is needed

# Global deque for tracking requests
requests_in_window = deque(
    maxlen=100
)  # Tracks up to 100 requests for 2-minute rate limiting

# Get Start Time
global_start_time = time.time()


def throttle():
    """
    Enforce throttling based on rate limits.
    """
    global requests_in_window

    # Remove timestamps older than 2 minutes from the deque
    current_time = time.time()
    while requests_in_window and (current_time - requests_in_window[0] > 120):
        requests_in_window.popleft()

    # Check if we are over the limit
    if len(requests_in_window) >= REQUESTS_PER_TWO_MINUTES:
        logger.info("Throttling: Waiting to respect rate limits.")
        print("Throttling: Waiting to respect rate limits.")

        time.sleep(SLEEP_INTERVAL)

    # Record the current request timestamp
    requests_in_window.append(current_time)


def get_most_recent_puuid(region):
    """Retrieves the most recently added player unique identifier (PUUID) for a specific region. Queries the database to
        find the latest PUUID based on the date added.

    Searches the puuids table for entries matching the given region, sorts them by date in descending order,
        and returns the most recent PUUID. Handles cases where no PUUID is found or an error occurs during the database query.

    Args:
        region (str): The server region to search for the most recent PUUID.

    Returns:
        str or None: The most recently added PUUID for the specified region, or None if no PUUID is found or an error occurs.

    Raises:
        Exception: Logs and handles any database query errors, returning None in such cases.

    Examples:
        >>> get_most_recent_puuid('americas')
        'example-puuid-123'
    """

    try:

        query = (
            "SELECT puuid, dateadded FROM puuids WHERE region = %s and dateadded < %s"
        )

        results = session.execute(query, (region,))
        if sorted_results := sorted(
            results, key=lambda row: row.dateadded, reverse=True
        ):
            result = sorted_results[0] if sorted_results else None

        if result:
            logger.info(
                f"Most Recent PUUID in {region}: {result.puuid}, DateAdded: {result.dateadded}"
            )
            return result.puuid
        else:
            logger.info(f"No PUUID found for region: {region}")
            return None
    except Exception as e:
        print(f"Error querying PUUID for region {region}: {e}")
        logger.info(f"Error querying PUUID for region {region}: {e}")

        return None


def get_matches(region, puuid, start=0, count=100, start_time=None):
    """Retrieves a list of recent match identifiers for a specific player.
        Fetches match data from the Riot Games API using the player's unique identifier and region.

        Queries the match history endpoint with configurable parameters to retrieve a limited set of
        recent matches. By default, it retrieves the 5 most recent matches without additional filtering.

    Args:
        region (str): The server region for the player's account.
        puuid (str): The player's unique identifier.

    Returns:
        list: A list of match identifiers or API response data.

    Examples:
        >>> get_matches('americas', 'player-puuid-123')
        ['match1', 'match2', 'match3', 'match4', 'match5']
    """
    try:
        throttle()  # Enforce throttling
        url = get_url("Account_Matches", region=region, puuid=puuid)
        query_params = {
            "type": None,
            "start": start,
            "count": count,
            "startTime": start_time,
            "endTime": None,
            "queue": None,
        }

        filtered_params = {k: v for k, v in query_params.items() if v is not None}

        matches = call_endpoint(url, filtered_params)
        return matches or []
    except Exception as e:
        print(f"Error fetching matches for PUUID {puuid}: {e}")
        logger.error(f"Error fetching matches for PUUID {puuid}: {e}")


def fetch_all_match_ids(region, puuid):
    """
    Fetch all match IDs for a given PUUID and store them in the database.
    """
    try:
        update_query = """
                UPDATE puuids
                SET lastprocessed = DateAdded
                WHERE lastprocessed IS NULL ALLOW FILTERING;
            """
        start_time_query = """
                SELECT lastprocessed as starttime
                FROM puuids
                WHERE puuid = %s
            """
        results = session.execute(start_time_query, (puuid,))
        start_time = results.one().starttime if results.one() else None
        logger.info(f"Most recent start time for PUUID {puuid}: {start_time}")
    except Exception as e:
        logger.error(f"Error fetching start time for PUUID {puuid}: {e}")
        start_time = None  # Default to None if there's an error
    start = 0
    count = 100  # Retrieve matches in larger batches if possible

    while True:
        try:
            matches = get_matches(
                region, puuid, start=start, count=count, start_time=start_time
            )
            if not matches:
                logger.info(f"All match IDs retrieved for PUUID {puuid}.")
                update_query = "UPDATE puuids SET lastprocessed = toTimestamp(now()) WHERE puuid = %s"
                session.execute(update_query, (puuid,))
                break

            for match_id in matches:
                try:
                    # Insert match_id into puuid_matches table if not already present
                    add_match(puuid, match_id, region)
                except Exception as e:
                    logger.error(
                        f"Error adding match ID {match_id} for PUUID {puuid}: {e}"
                    )

            # Increment the starting index for the next batch
            start += count

        except Exception as e:
            logger.error(f"Error fetching matches for PUUID {puuid}: {e}")
            break


def add_puuid(puuid, region):
    try:
        query = """INSERT INTO puuids (puuid, region, DateAdded) VALUES (%s, %s, toTimestamp(now()))
                   IF NOT EXISTS"""

        # Execute the query
        result = session.execute(query, (puuid, region))

        # Check if the row was actually added
        if result.one().applied:
            logger.info(f"PUUID {puuid} successfully added for region {region}")
        else:
            logger.info(f"PUUID {puuid} already exists for region {region}")
    except Exception as e:
        print(f"Error adding PUUID {puuid} for region {region}: {e}")


def add_match(puuid, match_id, region):
    try:
        # Check if the match has already been processed in puuid_matches
        check_query = "SELECT processed FROM puuid_matches WHERE match_id = %s and processed = True"
        if check_result := session.execute(check_query, (match_id,)).one():
            logger.info(f"Match {match_id} already processed for PUUID {puuid}.")
            return

        insert_query = """INSERT INTO puuid_matches (dateadded, match_id, puuid, processed) VALUES (toTimestamp(now()), %s, %s, false)
                   IF NOT EXISTS"""

        # Execute the query
        result = session.execute(insert_query, (match_id, puuid))

        # Check if the row was actually added
        if result.one().applied:
            logger.info(f"Match ID {match_id} for PUUID {puuid} successfully added")
        else:
            logger.info(f"Match ID {match_id} for PUUID {puuid} already exists")

    except Exception as e:
        print(f"Error adding Match Id {match_id} for PUUID {puuid}: {e}")
        return


if __name__ == "__main__":
    region = "americas"
    default_puuid = (
        "HHk7hueAv-6OIn3vv7xOVPxIB_ARB2z9IAf7p5w14pbRN1COH0bCY5jZEXYioHKIaf3AMj3Ntuhvvg"
    )

    if summoner_puuid := get_most_recent_puuid(region) or default_puuid:
        print(f"Using summoner puuid: {summoner_puuid}")
        add_puuid(summoner_puuid, region)
        fetch_all_match_ids(region, summoner_puuid)
