# This Python file uses the following encoding: utf-8

"""Progression Game module."""
import random

NAME = 'brain_progression'
RULE = 'What number is missing in the progression?'


def generate_round():
    """One round function of brain_progression game.

    Ask user missing number in the progression.

    Returns:
        question(str),
        correct_answer(str)
    """
    consequence = []
    first_number = random.randint(0, 100)
    diff = random.randint(0, 10)
    lenght_of_consequence = 10
    consequence = list(map(
        lambda el:
        first_number + el * diff,
        range(0, lenght_of_consequence),
        ),
    )

    secret_number = random.randint(0, lenght_of_consequence - 1)
    secret_consequence = consequence[:]
    secret_consequence[secret_number] = '..'

    question = str(secret_consequence)
    correct_answer = consequence[secret_number]

    return (question, str(correct_answer))
