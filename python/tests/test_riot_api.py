import os
import requests
import sys

from dotenv import load_dotenv
from python.utils.api_utils import get_url, test_endpoint
from python.utils.logger import get_logger

logger = get_logger("test_riot_api.log", namespace="test_riot_api")
# Load environment variables
load_dotenv()
api_key = os.getenv("RIOT_API_KEY")

# Example usage
if __name__ == "__main__":
    if not api_key:
        print("Error: RIOT_API_KEY is missing. Ensure it's set in the .env file.")
        logger.error("Error: RIOT_API_KEY is missing. Ensure it's set in the .env file.")
        sys.exit(1)

    # Test the Summoner endpoint
    summoner_name = "Ballanor"
    summoner_tag = 'Jedi'
    region= 'americas'
    summoner_url = get_url("Account_Name", gameName=summoner_name, tagLine=summoner_tag, region=region)
    summoner_data = test_endpoint(summoner_url, api_key)
    
if summoner_data:
    logger.info("Summoner Data Exists")
    summoner_puuid = summoner_data["puuid"]
    print("Summoner Name:", summoner_data["gameName"])
    print("Summoner Tag:", summoner_data["tagLine"])
    print("Summoner puuid:", summoner_data["puuid"])
    
    
    
    