# This Python file uses the following encoding: utf-8

"""Prime Brain Game."""
import random

RULE = """"Answer 'yes' if given number is prime.
Otherwise answer 'no'."""


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
    """Check prime function.

    Checks if given number is prime.

    Args:
        number(int): number

    Returns:
        True - if number is prime,
        False - if number is not prime.
    """
    check_number = 2
    if number > 1:
        while check_number < number / 2:
            if check_multiplicity(number, check_number):
                return False
            check_number += 1
        return True
    return False


def generate_round():
    """One round function of brain_progression game.

    Ask user if given number is prime.

    Returns:
        question(str),
        correct_answer(str)
    """
    number = random.randint(0, 100)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = str(number)

    return (question, correct_answer)
