"""
Simple JSON-backed contact book utilities for Lab 07.

Provides:
- `save_contacts_to_json(contacts, filename)`
- `load_contacts_from_json(filename)`

The loader returns an empty list when the file doesn't exist.
"""

import json


def save_contacts_to_json(contacts, filename):
    """
    Saves a list of contacts (dictionaries) to a file in JSON format.

    Parameters
    ----------
    contacts : list
        A list of contact dictionaries.
    filename : str
        The name of the file to save the contacts to.
    """
    with open(filename, "w", encoding="utf-8") as fh:
        json.dump(contacts, fh, indent=4, ensure_ascii=False)


def load_contacts_from_json(filename):
    """
    Loads a list of contacts from a JSON file.

    Returns an empty list if the file does not exist.
    """
    try:
        with open(filename, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    contacts_file = 'contacts.json'
    my_contacts = load_contacts_from_json(contacts_file)
    print(f"Loaded {len(my_contacts)} contact(s).")

    new_contact = {"name": "Charles Babbage", "email": "charles@computers.org"}
    my_contacts.append(new_contact)
    print(f"Added a new contact for {new_contact['name']}.")

    save_contacts_to_json(my_contacts, contacts_file)
    print("Saved contacts to disk.")
