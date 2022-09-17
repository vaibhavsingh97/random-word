# Wordnik Service

## Overview

Wordnik is the world's biggest online English dictionary, by number of words.


## Simple Usage

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

User can specify their own [api key][wornikWebsiteLink]
```python
r = Wordnik(api_key="<your api key>") 
```


## Advance Usage

1. To generate single random word we can use these optional parameters

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

2. To generate list of random word we can use these optional parameters

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

3. To get word of the day we can use these optional parameters

    - `date (string)` - Fetches by date in yyyy-MM-dd (optional)

    ```python
    r.word_of_the_day(date="2018-01-01")

    # Output: {"word": "qualtagh", "definations": [{"text": "The first person one encounters, either after leaving one\'s home or (sometimes) outside one\'s home, especially on New Year\'s Day.", "source": "wiktionary", "partOfSpeech": "noun"}, {"text": "A Christmas or New Year\'s ceremony, in the Isle of Man; one who takes part in the ceremony. See the first extract.", "source": "century", "partOfSpeech": "noun"}]}
    ```

[wornikWebsiteLink]:https://developer.wordnik.com
