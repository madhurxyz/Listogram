#!python


from __future__ import division, print_function
from listogram import Listogram
import unittest

class ListogramTest(unittest.TestCase):

    # test fixtures
    text_str = 'one fish two fish red fish blue fish'
    text_list = text_str.split()
    hist_list = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    hist_dict = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

    def test_items(self):
        hist_list = Listogram(self.text_list)
        assert len(hist_list) == 5
        self.assertItemsEqual(hist_list, self.hist_list)

        hist_dict = dict(hist_list)
        assert len(hist_dict) == 5
        self.assertItemsEqual(hist_dict.items(), self.hist_list)

    def test_count(self):
        hist_list = Listogram(self.text_list)
        assert hist_list.types == 5
        assert hist_list.tokens == 8
        assert hist_list.count('one') == 1
        assert hist_list.count('two') == 1
        assert hist_list.count('red') == 1
        assert hist_list.count('blue') == 1
        assert hist_list.count('fish') == 4
        assert hist_list.count('food') == 0

    def test_update(self):
        hist_list = Listogram(self.text_list)
        hist_list.update(['two', 'blue', 'fish', 'food'])
        assert hist_list.types == 6
        assert hist_list.tokens == 12
        assert hist_list.count('one') == 1
        assert hist_list.count('two') == 2
        assert hist_list.count('red') == 1
        assert hist_list.count('blue') == 2
        assert hist_list.count('fish') == 5
        assert hist_list.count('food') == 1

    def test_contains(self):
        hist_list = Listogram(self.text_list)
        for word in self.text_list:
            assert word in hist_list
        for word in ['fishy', 'food']:
            assert word not in hist_list


if __name__ == '__main__':
    unittest.main()
