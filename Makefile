install:
	pip install -r requirements.txt
	python setup.py install

test:
	python -m unittest test.py

sdist:
	python setup.py sdist

.PHONY: install test sdist
