"""Calc Game module"""
# This Python file uses the following encoding: utf-8
import random


def brain_calc():
    """One round of brain_gds game.
        Ask user the result of the expression.
        Return rule of the game, question and correct answer
    """
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = number_1 + number_2
    elif operator == '-':
        correct_answer = number_1 - number_2
    else:
        correct_answer = number_1 * number_2

    rule = 'What is the result of the expression?'
    question = str(number_1) + operator + str(number_2)

    return (rule, question, str(correct_answer))