# This Python file uses the following encoding: utf-8

"""Prime Game module."""
import random


def brain_prime():
    """One round function of brain_progression game.

    Ask user if given number is prime.

    Returns:
        rule(str) - rule of the game,
        question(str),
        correct_answer(str)
    """
    number = random.randint(0, 100)
    check_number = 2
    correct_answer = 'yes'
    while check_number < number:
        if (number % check_number == 0):
            correct_answer = 'no'
            break
        check_number += 1

    rule = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
    question = str(number)

    return (rule, question, correct_answer)
