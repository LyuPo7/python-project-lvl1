# This Python file uses the following encoding: utf-8

"""Functions of project."""
import prompt


def welcome_user():
	"""Welcoming user.

	Returns:
		user_name(str)
	"""
	return prompt.string('May I have your name? ')


def game_choice():
	"""Choice the game.

	Ask user which game would like to play.

	Returns:
		user's choice(str)
	"""
	print('Choice the game: ')
	print('For play brain_even enter: 0')
	print('For play brain_calc enter: 1')
	print('For play brain_gcd enter: 2')
	print('For play brain_progression enter: 3')
	print('For play brain_prime enter: 4')
	user_choice = prompt.string('Make your choice: ')

	return str(user_choice)
