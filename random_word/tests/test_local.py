from unittest import TestCase, main
from random_word import RandomWords


class TestRandomWord(TestCase):
    # using single instance for all tests
    r = RandomWords()

    def test_random_word(self):
        return self.r.get_random_word()

if __name__ == "__main__":
    main()
