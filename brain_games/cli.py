# This Python file uses the following encoding: utf-8

"""Functions of project."""
import prompt
from brain_games.games.brain_even import play_round_brain_even
from brain_games.games.brain_even import Rule_Brain_Even
from brain_games.games.brain_calc import play_round_brain_calc, Rule_Brain_Calc
from brain_games.games.brain_gcd import play_round_brain_gcd, Rule_Brain_Gcd
from brain_games.games.brain_progression import play_round_brain_progression
from brain_games.games.brain_progression import Rule_Brain_Progression
from brain_games.games.brain_prime import play_round_brain_prime
from brain_games.games.brain_prime import Rule_Brain_Prime
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
	name = welcome_user()
	user_choice = request_choice()

	if (user_choice == '0'):
		engine(play_round_brain_even, Rule_Brain_Even, name)
	elif (user_choice == '1'):
		engine(play_round_brain_calc, Rule_Brain_Calc, name)
	elif (user_choice == '2'):
		engine(play_round_brain_gcd, Rule_Brain_Gcd, name)
	elif (user_choice == '3'):
		engine(play_round_brain_progression, Rule_Brain_Progression, name)
	elif (user_choice == '4'):
		engine(play_round_brain_prime, Rule_Brain_Prime, name)
