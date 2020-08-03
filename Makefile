install:
	poetry install

lint:
	poetry run flake8 --show-source brain_games --ignore=T001,S311,WPS210,I002,WPS114,WPS221,W191,S001,WPS223,WPS232,WPS231,E117 --statistics

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

.PHONY: install lint selfcheck check build