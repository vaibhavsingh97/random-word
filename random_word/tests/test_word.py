from unittest import TestCase, main
from random_word import RandomWords


class RandomWordTest(TestCase):
    def set_up(self):
        r = RandomWords()

        def random_word(self):
            return r.get_random_word()

        def random_words(self):
            return r.get_random_words()

        def word_of_the_day(self):
            return r.word_of_the_day()


if __name__ == '__main__':
    main()
