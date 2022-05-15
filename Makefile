help:
	@echo '    init'
	@echo '        install pipenv and all project dependencies'
	@echo '    test'
	@echo '        run all tests'
	@echo '    build'
	@echo '        package for distributing in pypi repository'
	@echo '    test_upload'
	@echo '        package for distributing in test pypi repository'
	@echo '    upload'
	@echo '        upload package to pypi (You will require credentials)'
	@echo '    clean'
	@echo '        clean temporary files created during build'
	@echo '    lint'
	@echo '        lint all the python files'


init:
	@echo 'Install python dependencies'
	pip install pipenv
	pip install autopep8
	pipenv install
	pipenv shell
	python setup.py install

test:
	@echo 'Run all tests'
	pytest

build:
	python3 -m build

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
	find . -name '*.egg-info' -exec rm -rf {} +
	rm -rf .tox
	rm -rf .pytest_cache .coverage
	rm -rf .eggs

lint:
	autopep8 random_word --recursive --in-place --pep8-passes 2000 --verbose
