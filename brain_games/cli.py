"""Functions of project."""
# This Python file uses the following encoding: utf-8
import prompt


def welcome_user():
	"""Welcoming user."""
	name = prompt.string('May I have your name? ')

	return name

def game_choice():
	"""Choice the game."""
	print('Choice the game:\n')
	print('For play brain_even enter: 0\n')
	print('For play brain_calc enter: 1\n')
	print('For play brain_calc enter: 2\n')
	user_choice = prompt.string('Make your choice: ')

	return str(user_choice)	
