# This Python file uses the following encoding: utf-8

"""Even game module."""
import random


def brain_even():
    """One round function of brain_even game.

    Ask user if the number is even.

    Returns:
        rule(str) - rule of the game,
        question(str),
        correct answer(str)
    """
    number = random.randint(0, 100)
    correct_answer = 'yes'

    if (number % 2):
        correct_answer = 'no'

    rule = 'Answer \"yes\" if number even otherwise answer \"no\"'
    question = str(number)
    return (rule, question, correct_answer)
