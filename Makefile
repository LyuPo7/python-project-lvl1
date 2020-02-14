install:
	poetry install

lint:
	poetry run flake8 --show-source brain_games
 	
selfcheck:
	poetry check

check: selfcheck test lint
