'''Engine module'''
# This Python file uses the following encoding: utf-8
import prompt

def engine(game, name_player):
    """Engine.
    """
    init_game = 1
    correct_answer = 'yes'
    user_answer = 'no'
    intent_number = 1

    while (((user_answer == correct_answer) or init_game) and intent_number <= 3):
        rule, question, correct_answer = game()
        print(rule)
        print('Question:', question)
        user_answer = prompt.string('Enter your answer, ' + name_player + ':')
        
        if (user_answer == correct_answer):
            print('Correct!')

            if (intent_number == 3):
                print('Congratulations, ', name_player, '!')
        else:
            print(user_answer, ' is wrong answer ;(. Correct answer was ', correct_answer)

        intent_number += 1
        init_game = 0
