# Lab 05 — Notes on Refactor and Error Handling

Summary
-------
This lab refactors a procedural script into two single-purpose functions and adds error handling so the program is robust against missing or malformed data.

Files changed
-------------
- `week05/lab05.py`: contains the original `users` data, two functions, and a main block.

Key functions
-------------

1. `calculate_average_age(users_list)`
   - Purpose: Compute the average age across users that have a valid integer `age` value.
   - Behavior:
     - Skips users whose `age` is missing or not an `int` (e.g., the string "unknown").
     - If `users_list` is empty or contains no valid ages, the function prints an error message and returns `0.0`.
     - Catches unexpected exceptions during per-user processing and continues processing other users.
   - Return type: `float` (average age) or `0.0` as a safe default on error.

2. `get_active_user_emails(users_list)`
   - Purpose: Return a list of `email` strings for users where `is_active` is truthy and an `email` value exists.
   - Behavior:
     - Preserves the order of users as given in the input list.
     - If a user is missing required keys or is malformed, the function logs a warning and skips that user.
     - Returns an empty list for empty input or when no active users with emails are found.
   - Return type: `list` of `str`.

Error handling decisions
------------------------
- Avoid crashing the program: functions return safe defaults (`0.0` or `[]`) instead of raising exceptions for common edge cases.
- Use `user.get(...)` to access dictionary fields safely rather than direct indexing.
- Use `isinstance(..., int)` to validate `age` before arithmetic to avoid `TypeError`.
- Print short, user-friendly messages for key error conditions (empty input or no valid ages).

Examples / Expected output
--------------------------
Running `python3 week05/lab05.py` prints the average age and the active user emails, e.g.:

average user age: 30.00
active user emails: ['alice@example.com', 'charlie@example.com']

Testing
-------
- Tests are in `week05/tests/test_lab05.py` and cover:
  - Normal calculation of average age (skipping invalid ages)
  - Handling of an empty list for average age (returns `0.0`)
  - Collecting active user emails, skipping users without emails
  - Behavior on empty input
- Run tests from repository root (example):
```bash
export PYTHONPATH="${PYTHONPATH}:week05"
python3 -m pytest week05/tests/test_lab05.py -q
```

Notes for maintainers
---------------------
- Functions are intentionally conservative: they favor predictable return types for testability and downstream use.
- If different behavior is desired (e.g., raising exceptions instead of returning default values), adapt the error handling accordingly.
