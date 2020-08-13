# This Python file uses the following encoding: utf-8

"""Even game module."""
import random

RULE_BRAIN_EVEN = 'Answer \"yes\" if number even otherwise answer \"no\"'


def play_round_brain_even():
    """One round function of brain_even game.

    Ask user if the number is even.

    Returns:
        question(str),
        correct answer(str)
    """
    number = random.randint(0, 100)
    correct_answer = 'yes'

    if (number % 2):
        correct_answer = 'no'

    question = str(number)
    return (question, correct_answer)
