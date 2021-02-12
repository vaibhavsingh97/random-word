help:
	@echo '    init'
	@echo '        install pipenv and all project dependencies'
	@echo '    test'
	@echo '        run all tests'

init:
	@echo 'Install python dependencies'
	pip install pipenv
	pip install autopep8
	pipenv install
	pipenv shell
	python setup.py install

test:
	@echo 'Run all tests'
	nosetests

build:
	python setup.py sdist bdist_wheel

test_upload:
	python -m twine upload -r testpypi dist/*

upload:
	python -m twine upload dist/*

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
