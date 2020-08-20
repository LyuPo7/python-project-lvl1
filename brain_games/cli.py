# This Python file uses the following encoding: utf-8

"""Functions of project."""
import prompt

from brain_games.games import even, calc, gcd
from brain_games.games import progression, prime
from brain_games.engine import engine


def generate_games_dict():
	"""Generate dictionary of the games.

	Returns:
		dictionary(dict) - dictionary of the games,
	"""
	return {
		'0': even,
		'1': calc,
		'2': gcd,
		'3': progression,
		'4': prime,
	}


def welcome_user():
	"""Welcoming user.

	Returns:
		user_name(str)
	"""
	print('Welcome to the Brain Games!')
	return prompt.string('May I have your name? ')


def request_choice():
	"""Request choice function.

	Asc which game would like to play.

	Returns:
		user_choice(str): number of game
	"""
	print('Choice the game: ')
	games_dict = generate_games_dict()
	for number, game in games_dict.items():
		print('For play {arg1} enter: {arg2}'.format(
			arg1=game.__name__,
			arg2=str(number),
			),
		)
	return prompt.string('Make your choice: ')


def play_brain_games():
	"""Choice the game.

	Call welcome_user() for welcoming user.
	Ask user which game would like to play.
	Call brain_games.engine for choosen game.
	"""
	name = welcome_user()
	games_dict = generate_games_dict()
	user_choice = request_choice()
	game = games_dict[user_choice]
	engine(game, name)
