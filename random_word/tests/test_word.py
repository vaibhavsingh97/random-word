from unittest import TestCase, main
from random_word import RandomWords


class RandomWordTest(TestCase):
	# using single instance for all tests
    r = RandomWords()

    def random_word(self):
        return self.r.get_random_word()

    def random_words(self):
        return self.r.get_random_words()

    def word_of_the_day(self):
        return self.r.word_of_the_day()


if __name__ == '__main__':
    main()
