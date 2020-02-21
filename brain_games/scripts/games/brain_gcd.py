"""Brain-even function."""
# This Python file uses the following encoding: utf-8
import random, math


def ask_user_gcd(name_player):
    """Ask user and return user's and correct answers."""
    number_1 = random.randint(0, 100)
    number_2 = random.randint(0, 100)
    print('Question: ', number_1, number_2)
    user_answer = input('Enter your answer,' + name_player + ': ')
    correct_answer = math.gcd(number_1, number_2)
    return (correct_answer, user_answer)


def brain_gcd(name_player):
    """Ask user the GCD of two numbers."""
    print('Find the greatest common divisor of given numbers.')
    init_game = 1
    correct_answer = 0
    user_answer = 1
    intent_number = 1

    while (((int(user_answer) == int(correct_answer)) or init_game) and intent_number <= 3):
        correct_answer, user_answer = ask_user_gcd(name_player)

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
