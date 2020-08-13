# This Python file uses the following encoding: utf-8

"""Functions of project."""
import prompt
from brain_games.games.brain_even import play_round_brain_even
from brain_games.games.brain_even import RULE_BRAIN_EVEN
from brain_games.games.brain_calc import play_round_brain_calc, RULE_BRAIN_CALC
from brain_games.games.brain_gcd import play_round_brain_gcd, RULE_BRAIN_GCD
from brain_games.games.brain_progression import play_round_brain_progression
from brain_games.games.brain_progression import RULE_BRAIN_PROGRESSION
from brain_games.games.brain_prime import play_round_brain_prime
from brain_games.games.brain_prime import RULE_BRAIN_PRIME
from brain_games.engine import engine


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
	print('For play brain_even enter: 0')
	print('For play brain_calc enter: 1')
	print('For play brain_gcd enter: 2')
	print('For play brain_progression enter: 3')
	print('For play brain_prime enter: 4')
	return prompt.string('Make your choice: ')


def play_brain_games():
	"""Choice the game.

	Call welcome_user() for welcoming user.
	Ask user which game would like to play.
	Call brain_games.engine for choosen game.
	"""
	games_dict = {
		'0': (play_round_brain_even, RULE_BRAIN_EVEN),
		'1': (play_round_brain_calc, RULE_BRAIN_CALC),
		'2': (play_round_brain_gcd, RULE_BRAIN_GCD),
		'3': (play_round_brain_progression, RULE_BRAIN_PROGRESSION),
		'4': (play_round_brain_prime, RULE_BRAIN_PRIME),
	}
	name = welcome_user()
	user_choice = request_choice()
	game, game_rule = games_dict[user_choice]
	engine(game, game_rule, name)
