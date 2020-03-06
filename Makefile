install:
	poetry install

lint:
	poetry run flake8 --show-source brain_games --ignore=T001,DAR101,S311,WPS210,E501,DAR201,I002,WPS114,WPS221,W191,S001,WPS223,WPS232,WPS231,E117,D104 --statistics

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

.PHONY: install lint selfcheck check build