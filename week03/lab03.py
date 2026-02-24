"""
Lab 03 solutions: Mad Libs generator and Number Guessing Game

Contains:
- `generate_mad_lib(adjective, noun, verb)` -> returns a story string
- `guessing_game()` -> interactive number guessing game (prints output)

This file is written to be testable by the provided pytest tests in
`week03/tests/test_lab03.py` (they mock `input()` and `random.randint`).
"""

import random


def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story
    noun : str
        A noun to use in the story
    verb : str
        A past-tense verb to use in the story

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.
    """
    # Create a short, testable story using all parameters and f-strings
    story = (
        f"Once upon a time, a {adjective} {noun} {verb} through the valley, "
        f"meeting curious travelers and learning unexpected lessons along the way."
    )
    return story


def guessing_game():
    """
    Plays a number guessing game with the user.

    The function prints prompts and feedback and returns None. It's written so
    that tests can mock `random.randint` and `builtins.input` to simulate play.
    """
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
