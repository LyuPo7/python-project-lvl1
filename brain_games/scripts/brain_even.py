"""Brain-even function."""
# This Python file uses the following encoding: utf-8
import random


def ask_user(name_player):
    """Ask user and return user's and correct answers."""
    number = random.randint(0, 100)
    print('Question: ', number)
    user_answer = input('Enter your answer,' + name_player + ': ')
    correct_answer = 'yes'
    
    if (number % 2):
        correct_answer = 'no'

    return (correct_answer, user_answer)


def brain_even(name_player):
    """Ask user if the number is even."""
    print('Answer \"yes\" if number even otherwise answer \"no\"')
    init_game = 1
    correct_answer = 'yes'
    user_answer = 'no'

    while ((user_answer == correct_answer) or init_game):
        correct_answer, user_answer = ask_user(name_player)

        if (user_answer == correct_answer):
            print('Correct!')
            init_game = 0
        else:
            print(user_answer, ' is wrong answer ;(. Correct answer was ', 
            correct_answer)
