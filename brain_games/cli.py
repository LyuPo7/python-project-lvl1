"""Functions of project."""
# This Python file uses the following encoding: utf-8
import prompt


def welcome_user():
	"""Welcoming user."""
	name = prompt.string('May I have your name? ')

	return name
