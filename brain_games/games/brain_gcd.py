# This Python file uses the following encoding: utf-8

"""GCD Game module."""
import random
import math


def brain_gcd():
    """One round function of brain_gds game.

    Ask user the GCD of two numbers.

    Returns:
        rule(str) - rule of the game,
        question(str),
        correct answer(str)
    """
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    correct_answer = math.gcd(number_1, number_2)

    rule = 'Find the greatest common divisor of given numbers.'
    question = ' '.join([str(number_1), ' and ', str(number_2)])

    return (rule, question, str(correct_answer))
