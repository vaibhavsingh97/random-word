# random-word

![Build](https://github.com/vaibhavsingh97/random-word/workflows/Build/badge.svg)
[![PyPI version](https://badge.fury.io/py/Random-Word.svg)](https://badge.fury.io/py/Random-Word)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://pypi.org/project/random-word/)
[![PyPI - Status](https://img.shields.io/pypi/status/Django.svg)](https://pypi.org/project/random-word/)
[![Downloads](https://pepy.tech/badge/random-word)](https://pepy.tech/project/random-word)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://vaibhavsingh97.mit-license.org/)

This is a simple python package to generate random english words by calling the Wordnik API.
If you need help after reading the below, please find me at [@vaibhavsingh97](https://twitter.com/vaibhavsingh97) on Twitter.

If you love the package, please :star2: the repo.

## Installation

You should be able to install using `easy_install` or `pip` in the usual ways:

```sh
$ easy_install random-word
$ pip install random-word
```

Or just clone this repository and run:

```sh
$ python3 setup.py install
```

Or place the `random-word` folder that you downloaded somewhere where it can be accessed by your scripts.

## Basic Usage

```python
# ⚠️ This will be soon deprecated in future versions of this package
from random_word import RandomWords
r = RandomWords()

# Return a single random word
r.get_random_word()
# Return list of Random words
r.get_random_words()
# Return Word of the day
r.word_of_the_day()
```

User can specify their own [api key][wornikWebsiteLink]
```python
r = RandomWords(api_key="<your api key>") 
```

In a future version, we will have different services similar to Wordnik that will provide random words.

```python
from random_word import Wordnik
wordnik_service = Wordnik()

# Return a single random word
wordnik_service.get_random_word()
# Return list of Random words
wordnik_service.get_random_words()
# Return Word of the day
wordnik_service.word_of_the_day()

```

## Advance Usage

1.  To generate single random word we can use these optional parameters

    - `hasDictionaryDef (string)` - Only return words with dictionary definitions (optional)
    - `includePartOfSpeech (string)` - CSV part-of-speech values to include (optional)
    - `excludePartOfSpeech (string)` - CSV part-of-speech values to exclude (optional)
    - `minCorpusCount (integer)` - Minimum corpus frequency for terms (optional)
    - `maxCorpusCount (integer)` - Maximum corpus frequency for terms (optional)
    - `minDictionaryCount (integer)` - Minimum dictionary count (optional)
    - `maxDictionaryCount (integer)` - Maximum dictionary count (optional)
    - `minLength (integer)` - Minimum word length (optional)
    - `maxLength (integer)` - Maximum word length (optional)

    ```python
    r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)

    # Output: pediophobia
    ```

2.  To generate list of random word we can use these optional parameters

    - `hasDictionaryDef (string)` - Only return words with dictionary definitions (optional)
    - `includePartOfSpeech (string)` - CSV part-of-speech values to include (optional)
    - `excludePartOfSpeech (string)` - CSV part-of-speech values to exclude (optional)
    - `minCorpusCount (integer)` - Minimum corpus frequency for terms (optional)
    - `maxCorpusCount (integer)` - Maximum corpus frequency for terms (optional)
    - `minDictionaryCount (integer)` - Minimum dictionary count (optional)
    - `maxDictionaryCount (integer)` - Maximum dictionary count (optional)
    - `minLength (integer)` - Minimum word length (optional)
    - `maxLength (integer)` - Maximum word length (optional)
    - `sortBy (string)` - Attribute to sort by `alpha` or `count` (optional)
    - `sortOrder (string)` - Sort direction by `asc` or `desc` (optional)
    - `limit (integer)` - Maximum number of results to return (optional)

    ```python
    r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10, sortBy="alpha", sortOrder="asc", limit=15)

    # Output: ['ambivert', 'calcspar', 'deaness', 'entrete', 'gades', 'monkeydom', 'outclimbed', 'outdared', 'pistoleers', 'redbugs', 'snake-line', 'subrules', 'subtrends', 'torenia', 'unhides']
    ```

3.  To get word of the day we can use these optional parameters

    - `date (string)` - Fetches by date in yyyy-MM-dd (optional)

    ```python
    r.word_of_the_day(date="2018-01-01")

    # Output: {"word": "qualtagh", "definations": [{"text": "The first person one encounters, either after leaving one\'s home or (sometimes) outside one\'s home, especially on New Year\'s Day.", "source": "wiktionary", "partOfSpeech": "noun"}, {"text": "A Christmas or New Year\'s ceremony, in the Isle of Man; one who takes part in the ceremony. See the first extract.", "source": "century", "partOfSpeech": "noun"}]}
    ```

## Development

Assuming that you have [`Python`](https://www.python.org/) and [`pipenv`](https://docs.pipenv.org) installed, set up your environment and install the required dependencies like this instead of the `pip install random-word` defined above:

```sh
$ git clone https://github.com/vaibhavsingh97/random-word.git
$ cd random-word
$ make init
```

Add API Key in `random_word` directory defining API Key in `config.yml`. If you don't have an API key than request your API key [here][wornikWebsiteLink]

```sh
API_KEY = "<API KEY>"
```

To check your desired changes you can install your package locally

```sh
$ pip install -e .
```

## Issues

You can report the bugs at the [issue tracker](https://github.com/vaibhavsingh97/random-word/issues)

## License

Built with ♥ by Vaibhav Singh([@vaibhavsingh97](https://github.com/vaibhavsingh97)) under [MIT License](https://vaibhavsingh97.mit-license.org/)

You can find a copy of the License at <https://vaibhavsingh97.mit-license.org/>

[wornikWebsiteLink]:https://developer.wordnik.com
