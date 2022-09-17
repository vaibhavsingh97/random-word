from random_word.services.wordnik import Wordnik
from random_word.services.apininjas import ApiNinjas
from random_word.services.local import Local


class RandomWords(object):

    """Class for generating random words"""

    def __init__(self, api_key=None, service_name=None):
        if service_name == "apininja":
            self.service = ApiNinjas()
        elif service_name == 'wordnik':
            self.service = Wordnik(api_key)
        else:
            self.service = Local()


    def get_random_word(self, **kwargs):
        return self.service.get_random_word(**kwargs)

    def get_random_words(self, **kwargs):
        return self.service.get_random_words(**kwargs)

    def word_of_the_day(self, **kwargs):
        return self.service.word_of_the_day(**kwargs)
