"""Brain-progression function."""
# This Python file uses the following encoding: utf-8
import random, math


def ask_user_progression(name_player):
    """Ask user and return user's and correct answers."""
    consequence = []
    first_number = random.randint(0, 100)
    diff = random.randint(0, 10)
    consequence = list(map(lambda x : first_number + x * diff, range(0,10)))

    secret_number = random.randint(0, 9)
    secret_consequence = consequence[:]
    secret_consequence[secret_number] = '..'

    print('Question: ', secret_consequence)
    user_answer = input('Enter your answer,' + name_player + ': ')

    return (consequence[secret_number], user_answer)


def brain_progression(name_player):
    """Ask user missing number in the progression."""
    print('What number is missing in the progression?')
    init_game = 1
    correct_answer = 0
    user_answer = 1
    intent_number = 1

    while (((int(user_answer) == int(correct_answer)) or init_game) and intent_number <= 3):
        correct_answer, user_answer = ask_user_progression(name_player)

        if (int(user_answer) == int(correct_answer)):
            print('Correct!')
            if (intent_number == 3):
                print('Congratulations, ' + name_player + '!')
        else:
            print(user_answer, ' is wrong answer ;(. Correct answer was ', 
            correct_answer)
            print('Let\'s try again, ' + name_player + '!')
        
        init_game = 0
        intent_number += 1
