"""Engine module."""
# This Python file uses the following encoding: utf-8
import prompt


def engine(game, game_rule, name_player):
    """Engine function.

    Gets game function and starts it 3 times
    If user's answer is right continue to next round,
    else turns out.

    Args:
        game: game to play
        game_rule: rule of the game
        name_player: user's
    """
    init_game = 1
    correct_answer = 'yes'
    user_answer = 'no'
    intent_number = 1

    print(game_rule)

    while (user_answer == correct_answer or init_game) and intent_number <= 3:
        question, correct_answer = game()
        print('Question:', question)
        user_answer = prompt.string(
            ''.join(['Enter your answer, ', name_player, ': ']),
        )

        if (user_answer == correct_answer):
            print('Correct!')

            if (intent_number == 3):
                print('Congratulations, ', name_player, '!')
        else:
            print(
                user_answer,
                ' is wrong answer :(. Correct answer was ',
                correct_answer,
            )

        intent_number += 1
        init_game = 0
