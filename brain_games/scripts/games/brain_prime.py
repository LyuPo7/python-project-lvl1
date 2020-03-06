"""Brain-prime function."""
# This Python file uses the following encoding: utf-8
import random
import prompt


def ask_user_prime(name_player):
    """Ask user and return user's and correct answers."""
    number = random.randint(0, 100)

    print('Question: ', number)
    user_answer = prompt.string(' '.join(['Enter your answer,', name_player, ': ']))

    check_number = 2
    correct_answer = 'yes'
    while check_number < number:
        if (number % check_number == 0):
            correct_answer = 'no'
            break
        check_number += 1

    return (str(correct_answer), str(user_answer))


def brain_prime(name_player):
    """Ask user if given number is prime."""
    print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    init_game = 1
    correct_answer = 0
    user_answer = 1
    intent_number = 1

    while (((user_answer == correct_answer) or init_game) and intent_number <= 3):
        correct_answer, user_answer = ask_user_prime(name_player)

        if (user_answer == correct_answer):
            print('Correct!')
            if (intent_number == 3):
                print('Congratulations, ', name_player, '!')
        else:
            print(user_answer, ' is wrong answer ;(. Correct answer was ', correct_answer)
            print("Let\'s try again, ", name_player, '!')

        init_game = 0
        intent_number += 1
