"""Main file of project."""
# This Python file uses the following encoding: utf-8
from brain_games.cli import welcome_user, game_choice
from brain_games.scripts.games.brain_even import brain_even
from brain_games.scripts.games.brain_calc import brain_calc
from brain_games.scripts.games.brain_gcd import brain_gcd
from brain_games.scripts.games.brain_progression import brain_progression
from brain_games.scripts.games.brain_prime import brain_prime


def main():
    """Run project."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    choice = game_choice()
    if (choice == '0'):
        brain_even(name)
    elif (choice == '1'):
        brain_calc(name)
    elif (choice == '2'):
        brain_gcd(name)
    elif (choice == '3'):
        brain_progression(name)
    elif (choice == '4'):
        brain_prime(name)


if __name__ == '__main__':
    main()
