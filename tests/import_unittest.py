import unittest

from app import buzz

class BuzzTest(unittest.TestCase):
    def test_select_single_word(self):
        l = ('foo', 'bar', 'foobar')
        word = buzz.select_word(l)
        self.assertTrue(word in l)

    def test_select_multiple_words(self):
        l = ('foo', 'bar', 'foobar')
        words = buzz.select_word(l, 2)
        self.assertEqual(2, len(words))
        self.assertTrue(words[0] in l)
        self.assertTrue(words[1] in l)
        self.assertNotEqual(words[0], words[1])

    def test_generate_buzz_of_at_least_five_words(self):
        phrase = buzz.generate_buzz()
        self.assertTrue(len(phrase.split()) >= 5) 
