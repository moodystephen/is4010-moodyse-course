"""
Simple API client for Week 07 (file-local implementation).

Provides `get_api_data(url)` which returns parsed JSON or None on error.
"""

import requests
from typing import Optional, Dict


def get_api_data(url: str) -> Optional[Dict]:
    """Fetch JSON data from `url` and return a dictionary or None on error.

    Parameters
    ----------
    url : str
        The API endpoint to fetch.
    """
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as exc:
        print(f"Error making request: {exc}")
        return None
    except ValueError:
        print("Error: Failed to decode JSON from response.")
        return None


if __name__ == '__main__':
    # Demo using PokéAPI
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    data = get_api_data(url)
    if data:
        print(f"Name: {data.get('name')}")
