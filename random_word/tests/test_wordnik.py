from os.path import abspath, dirname, join
from unittest import TestCase, main

from random_word import Wordnik
from random_word.utils.utils import get_api_keys, get_random_api_key

ROOT_DIR = dirname(dirname(abspath(__file__)))
CONFIG_PATH = join(ROOT_DIR, "config.yml")

# Ensure that the config.yml file contains valid API keys
API_KEYS_LIST = get_api_keys(CONFIG_PATH)["API_KEY"]
API_KEY = get_random_api_key(API_KEYS_LIST)


class TestRandomWord(TestCase):
    # using single instance for all tests
    r = Wordnik(api_key=API_KEY)

    def test_random_word(self):
        word = self.r.get_random_word()
        self.assertIsNotNone(word)

    def test_random_words(self):
        words = self.r.get_random_words()
        self.assertIsInstance(words, list)

    def test_word_of_the_day(self):
        word_of_the_day = self.r.word_of_the_day()
        self.assertIsNotNone(word_of_the_day)


if __name__ == "__main__":
    main()
