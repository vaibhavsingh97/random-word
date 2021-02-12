import datetime
import json
import os

from random_word.utils.utils import (
    request_url,
    check_payload_items,
    get_api_keys,
    get_random_api_key,
)

from random_word.utils.retry_generator import Retry

from urllib.parse import urlencode, quote_plus


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, "config.yml")

API_KEYS_LIST = get_api_keys(CONFIG_PATH)["API_KEY"]
API_KEY = get_random_api_key(API_KEYS_LIST)


class RandomWords(object):
    """ Class for genrating random words"""

    def __init__(self, api_key=None):
        if api_key:
            self.__api_key = api_key
        else:
            self.__api_key = API_KEY
        self.issue_url = "https://github.com/vaibhavsingh97/random-word/issues"
        if self.__api_key == "" or self.__api_key is None:
            raise Exception("API key not found")

    @Retry(3)
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
        allParams = [
            "hasDictionaryDef",
            "includePartOfSpeech",
            "excludePartOfSpeech",
            "minCorpusCount",
            "maxCorpusCount",
            "minDictionaryCount",
            "maxDictionaryCount",
            "minLength",
            "maxLength",
        ]
        params = locals()
        payload = params["kwargs"]
        check_payload_items(payload, allParams)
        payload["api_key"] = self.__api_key
        del params["kwargs"]
        try:
            url += urlencode(payload, quote_via=quote_plus)
        except TypeError:
            url += urlencode(payload)
        response = request_url(url)
        result = response.json()
        if response.status_code == 200:
            return result["word"]
        else:
            if len(API_KEYS_LIST) == 0:
                raise Exception(
                    "Error occured, No result found. If you think this was a mistake than raise issue at {}".format(
                        self.issue_url
                    )
                )
            else:
                if self.__api_key in API_KEYS_LIST:
                    API_KEYS_LIST.remove(self.__api_key)
                self.__api_key = get_random_api_key(API_KEYS_LIST)

    @Retry(3)
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
        allParams = [
            "hasDictionaryDef",
            "includePartOfSpeech",
            "excludePartOfSpeech",
            "minCorpusCount",
            "maxCorpusCount",
            "minDictionaryCount",
            "maxDictionaryCount",
            "minLength",
            "maxLength",
            "sortBy",
            "sortOrder",
            "limit",
        ]
        params = locals()
        payload = params["kwargs"]
        check_payload_items(payload, allParams)
        payload["api_key"] = self.__api_key
        del params["kwargs"]
        if "sortBy" in payload:
            value = ["alpha", "count"]
            if payload["sortBy"] not in value:
                raise ValueError("Got an unexpected value to argument sortBy")
        if "sortOrder" in payload:
            value = ["asc", "desc"]
            if payload["sortOrder"] not in value:
                raise ValueError(
                    "Got an unexpected value to argument sortOrder")
        try:
            url += urlencode(payload, quote_via=quote_plus)
        except TypeError:
            url += urlencode(payload)
        response = request_url(url)
        result = response.json()
        word_list = []
        if response.status_code == 200:
            for word in result:
                word_list.append(word["word"])
            return word_list
        else:
            if len(API_KEYS_LIST) == 0:
                raise Exception(
                    "Error occured, No result found. If you think this was a mistake than raise issue at {}".format(
                        self.issue_url
                    )
                )
            else:
                if self.__api_key in API_KEYS_LIST:
                    API_KEYS_LIST.remove(self.__api_key)
                self.__api_key = get_random_api_key(API_KEYS_LIST)

    @Retry(3)
    def word_of_the_day(self, **kwargs):
        """Returns a specific WordOfTheDay
        Args:
            date, str: Fetches by date in yyyy-MM-dd (optional)

        Returns: Json(WordOfTheDay)
        """

        url = "https://api.wordnik.com/v4/words.json/wordOfTheDay?"
        allParams = ["date"]
        params = locals()
        payload = params["kwargs"]
        check_payload_items(payload, allParams)
        payload["api_key"] = self.__api_key
        del params["kwargs"]
        if "date" in payload:
            try:
                datetime.datetime.strptime(payload["date"], "%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        try:
            url += urlencode(payload, quote_via=quote_plus)
        except TypeError:
            url += urlencode(payload)
        response = request_url(url)
        result = response.json()
        if response.status_code == 200:
            word = result["word"]
            definitions = result["definitions"]
            return json.dumps({"word": word, "definations": definitions})
        else:
            if len(API_KEYS_LIST) == 0:
                raise Exception(
                    "Error occured, No result found. If you think this was a mistake than raise issue at {}".format(
                        self.issue_url
                    )
                )
            else:
                if self.__api_key in API_KEYS_LIST:
                    API_KEYS_LIST.remove(self.__api_key)
                self.__api_key = get_random_api_key(API_KEYS_LIST)
