"""
Lab 03 shim implementing required functions for tests.

This provides `generate_mad_lib` and `guessing_game` expected by the
test suite. The implementation is simple and test-focused so it can be
imported by pytest without requiring interactive input during tests
(tests mock `input()` and `random.randint`).
"""

import random


def generate_mad_lib(adjective, noun, verb):
    """Generate a short story using the three provided words."""
    return (
        f"Once upon a time, a {adjective} {noun} {verb} through the valley, "
        f"meeting curious travelers and learning unexpected lessons along the way."
    )


def guessing_game():
    """Interactive guessing game; prints prompts and feedback."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Enter your guess: ")
        try:
            guess = int(user_input)
        except Exception:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break


if __name__ == '__main__':
    guessing_game()
