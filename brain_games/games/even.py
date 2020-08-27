# This Python file uses the following encoding: utf-8

"""Even brain game."""
import random

RULE = "Answer 'yes' if number even otherwise answer 'no'"


def is_even(number):
    """Check even function.

    Checks if given number is even.

    Args:
        number(int): number

    Returns:
        'yes' - if number is even,
        'no' - if number is not even.
    """
    return number % 2 == 0


def generate_round():
    """One round function of brain_even game.

    Ask user if the number is even.

    Returns:
        question(str),
        correct answer(str)
    """
    number = random.randint(0, 100)

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = str(number)
    return (question, correct_answer)
