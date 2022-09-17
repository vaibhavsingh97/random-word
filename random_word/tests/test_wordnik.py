from os.path import abspath, dirname, join
from unittest import TestCase, main

from random_word import Wordnik
from random_word.utils.utils import get_api_keys, get_random_api_key

# TODO: Retire demo keys
ROOT_DIR = dirname(dirname(abspath(__file__)))
CONFIG_PATH = join(ROOT_DIR, "config.yml")

API_KEYS_LIST = get_api_keys(CONFIG_PATH)["API_KEY"]
API_KEY = get_random_api_key(API_KEYS_LIST)


class TestRandomWord(TestCase):
    # using single instance for all tests
    r = Wordnik(api_key= API_KEY)

    def test_random_word(self):
        return self.r.get_random_word()

    def test_random_words(self):
        return self.r.get_random_words()

    def test_word_of_the_day(self):
        return self.r.word_of_the_day()


if __name__ == "__main__":
    main()
