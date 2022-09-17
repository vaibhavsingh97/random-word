# random-word

![Build](https://github.com/vaibhavsingh97/random-word/workflows/Build/badge.svg)
[![PyPI version](https://badge.fury.io/py/Random-Word.svg)](https://badge.fury.io/py/Random-Word)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://pypi.org/project/random-word/)
[![PyPI - Status](https://img.shields.io/pypi/status/Django.svg)](https://pypi.org/project/random-word/)
[![Downloads](https://pepy.tech/badge/random-word)](https://pepy.tech/project/random-word)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://vaibhavsingh97.mit-license.org/)

This is a simple python package to generate random English words.
If you need help after reading the below, please find me on Twitter at [@vaibhavsingh97](https://twitter.com/vaibhavsingh97).

If you love the package, please :star2: the repo.

## Installation

You should be able to install using `easy_install` or `pip` in the usual ways:

```sh
$ easy_install random-word
$ pip install random-word
```

Or clone this repository and run:

```sh
$ python3 setup.py install
```

Or place the `random-word` folder that you downloaded somewhere where your scripts can access it.

## Basic Usage

> 👋 This package will now, by default, fetch the random word from local [database](https://github.com/vaibhavsingh97/random-word/blob/master/random_word/database/words.json)

```python
from random_word import RandomWords
r = RandomWords()

# Return a single random word
r.get_random_word()
```

Different services are available as a part of the random word package, which fetches random words from various API providers. Please check the `Services` section for more details.

## Services

- [Wordnik][wordnikDocLink]
- [API Ninjas][apiNinjasDocLink]

## Development

Assuming that you have [`Python`](https://www.python.org/) and [`pipenv`](https://docs.pipenv.org) installed, set up your environment and install the required dependencies like this instead of the `pip install random-word` defined above:

```sh
$ git clone https://github.com/vaibhavsingh97/random-word.git
$ cd random-word
$ make init
```

Add API Key in `random_word` directory defining API Key in `config.yml`. If you don't have an API key, then request your API key [here][wornikWebsiteLink]

```sh
API_KEY = "<API KEY>"
```

To check your desired changes, you can install your package locally.

```sh
$ pip install -e .
```

## Issues

You can report the bugs at the [issue tracker](https://github.com/vaibhavsingh97/random-word/issues)

## License

Built with ♥ by Vaibhav Singh([@vaibhavsingh97](https://github.com/vaibhavsingh97)) under [MIT License](https://vaibhavsingh97.mit-license.org/)

You can find a copy of the License at <https://vaibhavsingh97.mit-license.org/>

[wordnikDocLink]:https://github.com/vaibhavsingh97/random-word/blob/master/docs/wordnik.md
[apiNinjasDocLink]:https://github.com/vaibhavsingh97/random-word/blob/master/docs/apininjas.md
