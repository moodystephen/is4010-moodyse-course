users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
]


def calculate_average_age(users_list):
    """Calculate the average age for users with valid integer ages.

    Parameters
    ----------
    users_list : list of dict
        List of user dictionaries which may contain an 'age' field.

    Returns
    -------
    float
        The average age of users with integer ages. Returns 0.0 on error
        or when no valid ages are available.
    """
    if not users_list:
        print("error: cannot calculate average age of an empty list.")
        return 0.0

    total_age = 0
    count = 0
    for user in users_list:
        try:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                count += 1
        except Exception as exc:
            # Skip malformed user entries but continue processing
            print(f"warning: skipping user due to error: {exc}")

    if count == 0:
        print("error: no valid ages found to calculate average.")
        return 0.0

    try:
        return total_age / count
    except Exception:
        print("error: unexpected error when calculating average.")
        return 0.0


def get_active_user_emails(users_list):
    """Return a list of emails for users that are active.

    Parameters
    ----------
    users_list : list of dict
        List of user dictionaries which may contain 'is_active' and 'email'.

    Returns
    -------
    list
        A list of email strings for users where 'is_active' is truthy and an
        'email' field exists. Returns an empty list on error or when no
        matching users are found.
    """
    if not users_list:
        return []

    emails = []
    for user in users_list:
        try:
            if user.get("is_active") and user.get("email"):
                emails.append(user.get("email"))
        except Exception as exc:
            print(f"warning: skipping user due to error: {exc}")
            continue

    return emails


if __name__ == '__main__':
    avg = calculate_average_age(users)
    print(f"average user age: {avg:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
