"""Even game module"""
# This Python file uses the following encoding: utf-8
import random

def brain_even():
    """One round of brain_even game.
        Ask user if the number is even.
        Return rule of the game, question and correct answer.
    """
    number = random.randint(0, 100)
    correct_answer = 'yes'

    if (number % 2):
        correct_answer = 'no'
    
    rule = 'Answer \"yes\" if number even otherwise answer \"no\"'
    question = str(number)
    return (rule, question, correct_answer)