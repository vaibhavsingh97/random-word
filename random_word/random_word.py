from random_word.services.local import Local


class RandomWords(object):

    """Class for generating random words"""

    def __init__(self):
        self.service = Local()

    def get_random_word(self):
        return self.service.get_random_word()
