# This Python file uses the following encoding: utf-8

"""Calc Game module."""
import random

NAME = 'brain_calc'
RULE = 'What is the result of the expression?'


def generate_round():
    """One round function of brain_gds game.

    Ask user the result of the expression.

    Returns:
        question(str),
        correct answer(str)
    """
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = number_1 + number_2
    elif operator == '-':
        correct_answer = number_1 - number_2
    elif operator == '*':
        correct_answer = number_1 * number_2

    question = ' '.join([str(number_1), operator, str(number_2)])

    return (question, str(correct_answer))
