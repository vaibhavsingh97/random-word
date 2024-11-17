import secrets
from json import load
from os.path import abspath, dirname, join


class Local(object):
    def __init__(self):
        self.source = join(dirname(__file__), "..", "database", "words.json")
        with open(self.source) as word_database:
            self.valid_words = load(word_database)

    def get_random_word(self):
        return secrets.choice(list(self.valid_words.keys()))
