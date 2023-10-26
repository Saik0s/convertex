install:
	poetry install

test:
	python -m unittest test.py

publish:
	poetry build
	poetry publish
	rm -rf dist

.PHONY: install test publish
