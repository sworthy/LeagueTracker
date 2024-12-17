import requests
import sys
import python.utils.PostgreSQL
import python.utils.Cassandra
import datetime

from dotenv import load_dotenv
from python.utils.api_utils import get_url, test_endpoint
from python.utils.logger import get_logger

logger = get_logger("test_riot_api.log", namespace="test_riot_api")
# Load environment variables
load_dotenv()


# Example usage
if __name__ == "__main__":
    # Test the Summoner endpoint
    summoner_name = "Ballanor"
    summoner_tag = "Jedi"
    region = "americas"
    summoner_url = get_url(
        "Account_Name", gameName=summoner_name, tagLine=summoner_tag, region=region
    )
    summoner_data = test_endpoint(summoner_url)

    if summoner_data:
        logger.info("Summoner Data Exists")
        summoner_puuid = summoner_data["puuid"]
        print("Summoner Name:", summoner_data["gameName"])
        print("Summoner Tag:", summoner_data["tagLine"])
        print("Summoner puuid:", summoner_data["puuid"])

        # Get match URL
        match_url = get_url("Account_Matches", puuid=summoner_puuid, region=region)

        # Set Query Parameters
        query_params = {
            "type": None,
            "start": 0,
            "count": 5,  # Max 100
            "startTime": None,
            "endTime": None,
            "queue": None,
        }

        filtered_params = {k: v for k, v in query_params.items() if v is not None}
        # Get Match Data IDs
        match_data = test_endpoint(match_url, filtered_params)

        if match_data:
            logger.info("Match Data Exists")
            print("Match Data:", match_data)
            for match in match_data:
                match_id = match
                print("Match ID:", match_id)
                match_url = get_url("Match", matchId=match_id, region=region)
                match_data = test_endpoint(match_url)
                if match_data:
                    logger.info("Match Data Exists")
                    # print("Match Data:", match_data)
                    timestamp_ms = match_data["info"]["gameStartTimestamp"]
                    timestamp_s = timestamp_ms / 1000
                    normalized_timestamp = datetime.datetime.fromtimestamp(timestamp_s)
                    print("Match Timestamp:", normalized_timestamp)
        else:
            logger.error("Match Data Does Not Exist")
            print("Match Data Does Not Exist")
