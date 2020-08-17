# This Python file uses the following encoding: utf-8

"""Even game module."""
import random

NAME = 'brain_even'
RULE = 'Answer \"yes\" if number even otherwise answer \"no\"'


def is_even(number):
    """Check even function.

    Checks if given number is even.

    Args:
        number(int): number

    Returns:
        'yes' - if number is even,
        'no' - if number is not even.
    """
    if (number % 2):
        return False
    return True


def bool2word(sign):
    """Convert bool value to word.

    Converts bool value to word.

    Args:
        sign(str): sign

    Returns:
        'yes' - if sign is True,
        'no' - if sign is False.
    """
    if sign:
        return 'yes'
    return 'no'


def generate_round():
    """One round function of brain_even game.

    Ask user if the number is even.

    Returns:
        question(str),
        correct answer(str)
    """
    number = random.randint(0, 100)
    correct_answer = bool2word(is_even(number))

    question = str(number)
    return (question, correct_answer)
