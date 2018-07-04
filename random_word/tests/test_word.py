from unittest import TestCase, main
from random_word import RandomWords

class TestRandomWord(TestCase):
	# using single instance for all tests
    r = RandomWords()
    def test_random_word(self):
        return self.r.get_random_word()
    def test_random_words(self):
        return self.r.get_random_words()
    def test_word_of_the_day(self):
        return self.r.word_of_the_day()
    def test_word_meaning(self):
       	return self.r.get_word_definitions()
if __name__ == '__main__':
    main()