import json
import requests
import datetime
from . import config

API_KEY = config.API_KEY

class RandomWords(object):
    """ Class for genrating random words"""

    def __init__(self):
        self.__api_key = API_KEY
        self.issue_url = "https://github.com/vaibhavsingh97/random-word/issues"
        if self.__api_key == "" or None:
            raise "API key not found"
        url = "https://api.wordnik.com/v4/account.json/apiTokenStatus?api_key=" + self.__api_key
        response = requests.get(url)
        if response.status_code == 200 and response.json()['valid'] == True:
            pass
        else:
            raise "API key either expired or not working. Please raise issue at {}".format(self.issue_url)

    def get_random_word(self, **kwargs):
        """Returns a single random word

        Args:
            hasDictionaryDef, str: Only return words with dictionary definitions (optional)
            includePartOfSpeech, str: CSV part-of-speech values to include (optional)
            excludePartOfSpeech, str: CSV part-of-speech values to exclude (optional)
            minCorpusCount, int: Minimum corpus frequency for terms (optional)
            maxCorpusCount, int: Maximum corpus frequency for terms (optional)
            minDictionaryCount, int: Minimum dictionary count (optional)
            maxDictionaryCount, int: Maximum dictionary count (optional)
            minLength, int: Minimum word length (optional)
            maxLength, int: Maximum word length (optional)

        Returns: String, Random words
        """

        url = "https://api.wordnik.com/v4/words.json/randomWord?"
        allParams = ['hasDictionaryDef', 'includePartOfSpeech', 'excludePartOfSpeech', 'minCorpusCount', 'maxCorpusCount', 'minDictionaryCount', 'maxDictionaryCount', 'minLength', 'maxLength']
        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_random_word" % key)
            params[key] = val
        del params['kwargs']

        if ('hasDictionaryDef' in params):
            url += "&hasDictionaryDef=" + str(params['hasDictionaryDef'])
        if ('includePartOfSpeech' in params):
            url += "&includePartOfSpeech=" + str(params['includePartOfSpeech'])
        if ('excludePartOfSpeech' in params):
            url += "&excludePartOfSpeech=" + str(params['excludePartOfSpeech'])
        if ('minCorpusCount' in params):
            url += "&minCorpusCount=" + str(params['minCorpusCount'])
        if ('maxCorpusCount' in params):
            url += "&maxCorpusCount=" + str(params['maxCorpusCount'])
        if ('minDictionaryCount' in params):
            url += "&minDictionaryCount=" + str(params['minDictionaryCount'])
        if ('maxDictionaryCount' in params):
            url += "&maxDictionaryCount=" + str(params['maxDictionaryCount'])
        if ('minLength' in params):
            url += "&minLength=" + str(params['minLength'])
        if ('maxLength' in params):
            url += "&maxLength=" + str(params['maxLength'])
        url += "&api_key=" + self.__api_key
        response = requests.get(url)
        result = response.json()
        if response.status_code == 200:
            return result['word']
        else:
            raise Exception("Error occured, No result found. If you think this was a mistake than raise issue at {}".format(self.issue_url))

    def get_random_words(self, **kwargs):
        """Returns a list of random words

        Args:
            includePartOfSpeech, str: CSV part-of-speech values to include (optional)
            excludePartOfSpeech, str: CSV part-of-speech values to exclude (optional)
            hasDictionaryDef, str: Only return words with dictionary definitions (optional)
            minCorpusCount, int: Minimum corpus frequency for terms (optional)
            maxCorpusCount, int: Maximum corpus frequency for terms (optional)
            minDictionaryCount, int: Minimum dictionary count (optional)
            maxDictionaryCount, int: Maximum dictionary count (optional)
            minLength, int: Minimum word length (optional)
            maxLength, int: Maximum word length (optional)
            sortBy, str: Attribute to sort by (optional)
            sortOrder, str: Sort direction (optional)
            limit, int: Maximum number of results to return (optional)

        Returns: list[Random Words]
        """

        url = "https://api.wordnik.com/v4/words.json/randomWords?"
        allParams = ['hasDictionaryDef', 'includePartOfSpeech', 'excludePartOfSpeech', 'minCorpusCount', 'maxCorpusCount', 'minDictionaryCount', 'maxDictionaryCount', 'minLength', 'maxLength', 'sortBy', 'sortOrder', 'limit']
        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_random_word" % key)
            params[key] = val
        del params['kwargs']

        if ('hasDictionaryDef' in params):
            url += "&hasDictionaryDef=" + str(params['hasDictionaryDef'])
        if ('includePartOfSpeech' in params):
            url += "&includePartOfSpeech=" + str(params['includePartOfSpeech'])
        if ('excludePartOfSpeech' in params):
            url += "&excludePartOfSpeech=" + str(params['excludePartOfSpeech'])
        if ('minCorpusCount' in params):
            url += "&minCorpusCount=" + str(params['minCorpusCount'])
        if ('maxCorpusCount' in params):
            url += "&maxCorpusCount=" + str(params['maxCorpusCount'])
        if ('minDictionaryCount' in params):
            url += "&minDictionaryCount=" + str(params['minDictionaryCount'])
        if ('maxDictionaryCount' in params):
            url += "&maxDictionaryCount=" + str(params['maxDictionaryCount'])
        if ('minLength' in params):
            url += "&minLength=" + str(params['minLength'])
        if ('maxLength' in params):
            url += "&maxLength=" + str(params['maxLength'])
        if ('sortBy' in params):
            value = ['alpha', 'count']
            if params['sortBy'] not in value:
                raise  ValueError("Got an unexpected value to argument sortBy")
            url += "&sortBy=" + str(params['sortBy'])
        if ('sortOrder' in params):
            value = ['asc', 'desc']
            if params['sortOrder'] not in value:
                raise  ValueError("Got an unexpected value to argument sortOrder")
            url += "&sortOrder=" + str(params['sortOrder'])
        if ('limit' in params):
            url += "&limit=" + str(params['limit'])
        url += "&api_key=" + self.__api_key
        response = requests.get(url)
        result = response.json()
        word_list = []
        if response.status_code == 200:
            for word in result:
                word_list.append(word['word'])
            return word_list
        else:
            raise Exception("Error occured, No result found. If you think this was a mistake than raise issue at {}".format(self.issue_url))

    def word_of_the_day(self, **kwargs):
        """Returns a specific WordOfTheDay
        Args:
            date, str: Fetches by date in yyyy-MM-dd (optional)

        Returns: Json(WordOfTheDay)
        """

        url = "https://api.wordnik.com/v4/words.json/wordOfTheDay?"
        allParams = ['date']
        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get_random_word" % key)
            params[key] = val
        del params['kwargs']

        if ('date' in params):
            try:
                datetime.datetime.strptime(params['date'], '%Y-%m-%d')
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
            url += "&date=" + str(params['date'])
        url += "&api_key=" + self.__api_key
        response = requests.get(url)
        result = response.json()
        if response.status_code == 200:
            word = result['word']
            definitions = result['definitions']
            return json.dumps({
                'word': word,
                'definations': definitions
            })
        else:
            raise Exception("Error occured, No result found. If you think this was a mistake than raise issue at {}".format(self.issue_url))
