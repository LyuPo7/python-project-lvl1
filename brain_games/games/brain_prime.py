"""Prime Game module"""
# This Python file uses the following encoding: utf-8
import random
import math


def brain_prime():
    """One round of brain_progression game.
        Ask user if given number is prime.
        Return rule of the game, question and correct answer.
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