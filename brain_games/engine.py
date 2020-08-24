"""Engine module."""
# This Python file uses the following encoding: utf-8
import prompt

MAX_INTENT = 3


def engine(game, name_player):
    """Engine function.

    Gets game function and starts it 3 times
    If user's answer is right continue to next round,
    else turns out.

    Args:
        game: game to play
        name_player: user's
    """
    counter = 1

    print(game.RULE)

    while counter <= MAX_INTENT:
        question, correct_answer = game.generate_round()
        print('Question:', question)
        user_answer = prompt.string(
            'Enter your answer, {arg}: '.format(arg=name_player),
        )

        if (user_answer == correct_answer):
            print('Correct!')
        else:
            print(
                "'{arg1}' is wrong answer :(.Correct answer was '{arg2}'".format(
                    arg1=user_answer,
                    arg2=correct_answer,
                ),
            )
        counter += 1
    else:
        print('Congratulations, ', name_player, '!')
