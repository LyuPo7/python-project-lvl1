# This Python file uses the following encoding: utf-8

"""Progression Game module."""
import random


def brain_progression():
    """One round function of brain_progression game.

    Ask user missing number in the progression.

    Returns:
        rule(str) - rule of the game,
        question(str),
        correct_answer(str)
    """
    consequence = []
    first_number = random.randint(0, 100)
    diff = random.randint(0, 10)
    consequence = list(map(lambda el: first_number + el * diff, range(0, 10)))

    secret_number = random.randint(0, 9)
    secret_consequence = consequence[:]
    secret_consequence[secret_number] = '..'

    rule = 'What number is missing in the progression?'
    question = str(secret_consequence)
    correct_answer = consequence[secret_number]

    return (rule, question, str(correct_answer))
