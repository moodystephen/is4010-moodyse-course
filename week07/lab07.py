"""
Week 07: Contact book and simple API client

This file provides:
- `save_contacts_to_json(contacts, filename)`
- `load_contacts_from_json(filename)`
- `get_api_data(url)`

The functions accept either `str` or `pathlib.Path` for filenames.
"""

from __future__ import annotations

import json
from typing import List, Dict, Optional, Union
import requests
from pathlib import Path


Filename = Union[str, Path]


def save_contacts_to_json(contacts: List[Dict], filename: Filename) -> None:
    """Save a list of contact dictionaries to `filename` as JSON.

    Parameters
    ----------
    contacts : list
        A list of dictionaries representing contacts.
    filename : str | Path
        Path to the file to write. If parent dirs don't exist, an error
        will be raised.
    """
    path = Path(filename)
    # Ensure parent exists
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as fh:
        json.dump(contacts, fh, indent=4, ensure_ascii=False)


def load_contacts_from_json(filename: Filename) -> List[Dict]:
    """Load contacts from `filename` and return a list of dictionaries.

    Returns an empty list if the file does not exist.
    """
    path = Path(filename)
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return []


def get_api_data(url: str) -> Optional[Dict]:
    """Fetch JSON data from `url` and return the parsed dict, or None on error."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as exc:
        print(f"Request error: {exc}")
        return None
    except ValueError:
        # JSON decoding error
        print("Error: failed to decode JSON from response")
        return None


if __name__ == '__main__':
    # Simple contact book demo
    contacts_file = Path("week07") / "contacts.json"

    contacts = load_contacts_from_json(contacts_file)
    print(f"Loaded {len(contacts)} contact(s) from {contacts_file}")

    contacts.append({"name": "Alan Turing", "email": "alan@code.org"})
    save_contacts_to_json(contacts, contacts_file)
    print(f"Saved {len(contacts)} contact(s) to {contacts_file}")

    # Simple API demo (PokéAPI)
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    data = get_api_data(url)
    if data:
        print(f"Fetched Pokémon: {data.get('name')}")
