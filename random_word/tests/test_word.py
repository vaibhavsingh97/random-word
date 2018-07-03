from unittest import TestCase, main
from random_word import RandomWords


class TestRandomWord(TestCase):

    # tests should be independent of each other
    
    def test_random_word(self):
        return RandomWords().get_random_word()

    def test_random_words(self):
        return RandomWords().get_random_words()

    def test_word_of_the_day(self):
        return RandomWords().word_of_the_day()
    

if __name__ == '__main__':
    main()
