import os
import requests

from python.utils.logger import get_logger
from python.config import BASE_URLS

# Create logs directory if it doesn't exist
logger = get_logger("api_utils.log", namespace="api_utils")
api_key = os.getenv("RIOT_API_KEY")


def get_url(endpoint_key, **kwargs):
    url_template = BASE_URLS.get(endpoint_key)
    if not url_template:
        logger.error(f"Endpoint '{endpoint_key}' not found in BASE_URLS.")
        raise ValueError(f"Endpoint '{endpoint_key}' not found in BASE_URLS.")
    return url_template.format(**kwargs)


def call_endpoint(url, params=None):
    api_key = os.getenv("RIOT_API_KEY")
    if not api_key:
        print("Error: RIOT_API_KEY is missing. Ensure it's set in the .env file.")
        logger.error(
            "Error: RIOT_API_KEY is missing. Ensure it's set in the .env file."
        )
        return None

    headers = {"X-Riot-Token": api_key}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        logger.info(f"API call to {response.url} successful.")
        return response.json()
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
        print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Request Error: {e}")
        print(f"Request Error: {e}")
    return None
