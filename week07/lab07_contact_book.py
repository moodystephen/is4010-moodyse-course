"""
Contact book utilities for Week 07 (file-local implementation).

Provides `save_contacts_to_json` and `load_contacts_from_json` and
accepts either `str` or `pathlib.Path` for filenames to match tests.
"""

from pathlib import Path
import json
from typing import List, Dict, Union

Filename = Union[str, Path]


def save_contacts_to_json(contacts: List[Dict], filename: Filename) -> None:
    """Save a list of contact dicts to `filename` in JSON format.

    Parameters
    ----------
    contacts : list
        A list of contact dictionaries.
    filename : str | Path
        Path or filename to write to. Parent directories will be created
        if necessary.
    """
    path = Path(filename)
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as fh:
        json.dump(contacts, fh, indent=4, ensure_ascii=False)


def load_contacts_from_json(filename: Filename) -> List[Dict]:
    """Load contacts from `filename` and return them as a list.

    Returns an empty list if the file does not exist.
    """
    path = Path(filename)
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    # Quick manual demo when run directly
    contacts_file = Path("contacts.json")
    contacts = load_contacts_from_json(contacts_file)
    print(f"Loaded {len(contacts)} contact(s).")
    contacts.append({"name": "Ada Lovelace", "email": "ada@example.com"})
    save_contacts_to_json(contacts, contacts_file)
    print("Saved contacts to disk.")
