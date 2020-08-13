# This Python file uses the following encoding: utf-8

"""Prime Game module."""
import random

RULE_BRAIN_PRIME = """"Answer \"yes\" if given number is prime.
Otherwise answer \"no\"."""


def check_multiplicity(dividend, divisor):
    """Check multiplicity function.

    Checks if given divisor evenly divides given dividend.

    Args:
        dividend(int): dividend
        divisor(int): divisor

    Returns:
        True - if divisor evenly divides given dividend,
        False - if divisor does not evenly divide given dividend.
    """
    if dividend % divisor == 0:
        return True
    return False


def is_prime(number):
    """Check multiplicity function.

    Checks if given number is prime.

    Args:
        number(int): number

    Returns:
        'yes' - if number is prime,
        'no' - if number is not prime.
    """
    check_number = 2
    while check_number < number:
        if check_multiplicity(number, check_number):
            return 'no'
        check_number += 1
    return 'yes'


def play_round_brain_prime():
    """One round function of brain_progression game.

    Ask user if given number is prime.

    Returns:
        question(str),
        correct_answer(str)
    """
    number = random.randint(0, 100)
    correct_answer = is_prime(number)
    question = str(number)

    return (question, correct_answer)
