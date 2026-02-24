"""
Top-level implementation of contact book utilities for Lab 07 tests.

Provides `save_contacts_to_json` and `load_contacts_from_json`.
"""

import json


def save_contacts_to_json(contacts, filename):
    """Save list of contact dicts to filename in JSON format."""
    with open(filename, "w", encoding="utf-8") as fh:
        json.dump(contacts, fh, indent=4, ensure_ascii=False)


def load_contacts_from_json(filename):
    """Load and return contacts list from filename, or [] if missing."""
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
    save_contacts_to_json(my_contacts, contacts_file)
    print("Saved contacts to disk.")
