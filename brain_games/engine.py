"""Engine module."""
# This Python file uses the following encoding: utf-8
import prompt


def engine(game, name_player):
    """Engine function.

    Gets game function and starts it 3 times
    If user's answer is right continue to next round,
    else turns out.

    Args:
        game: game to play
        game_rule: rule of the game
        name_player: user's
    """
    max_intent = 3
    intent_number = 1

    print(game.RULE)

    while intent_number <= max_intent:
        question, correct_answer = game.generate_round()
        print('Question:', question)
        user_answer = prompt.string(
            ''.join(['Enter your answer, ', name_player, ': ']),
        )

        if (user_answer == correct_answer):
            print('Correct!')

            if (intent_number == max_intent):
                print('Congratulations, ', name_player, '!')
        else:
            print(
                user_answer,
                ' is wrong answer :(. Correct answer was ',
                correct_answer,
            )
            break

        intent_number += 1
