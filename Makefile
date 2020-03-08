help:
	@echo '    init'
	@echo '        install pipenv and all project dependencies'
	@echo '    test'
	@echo '        run all tests'

init:
	@echo 'Install python dependencies'
	pip install pipenv
	pipenv install
	python setup.py install

test:
	@echo 'Run all tests'
	nosetests

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .tox
	rm -rf .pytest_cache .coverage

lint:
	autopep8 random_word --recursive --in-place --pep8-passes 2000 --verbose
