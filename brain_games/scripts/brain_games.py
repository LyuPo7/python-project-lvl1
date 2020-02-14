"""Main file of project."""
# This Python file uses the following encoding: utf-8
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import brain_even

def main():
    """Run project."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    brain_even(name)


if __name__ == '__main__':
    main()
