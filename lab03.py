"""
Top-level shim for Lab 03 so tests can import `lab03` directly.

This duplicates the implementation in `week03/lab03.py` so pytest discovery
can import `lab03` as a top-level module (the tests expect that).
"""

import random


def generate_mad_lib(adjective, noun, verb):
    """See week03/lab03.py for full documentation."""
    story = (
        f"Once upon a time, a {adjective} {noun} {verb} through the valley, "
        f"meeting curious travelers and learning unexpected lessons along the way."
    )
    return story


def guessing_game():
    """See week03/lab03.py for full documentation."""
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
