# This Python file uses the following encoding: utf-8

"""GCD Brain Game."""
import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def generate_round():
    """One round function of brain_gds game.

    Ask user the GCD of two numbers.

    Returns:
        question(str),
        correct answer(str)
    """
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    correct_answer = math.gcd(number_1, number_2)

    question = '{arg1} and {arg2}'.format(
        arg1=str(number_1),
        arg2=str(number_2),
    )
    return (question, str(correct_answer))
