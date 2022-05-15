from .services.wordnik import Wordnik


class RandomWords(object):

    """Class for generating random words"""

    def __init__(self, api_key=None):
        self.wordnik_service = Wordnik(api_key)

    def get_random_word(self, **kwargs):
        return self.wordnik_service.get_random_word(**kwargs)

    def get_random_words(self, **kwargs):
        return self.wordnik_service.get_random_words(**kwargs)

    def word_of_the_day(self, **kwargs):
        return self.wordnik_service.word_of_the_day(**kwargs)
