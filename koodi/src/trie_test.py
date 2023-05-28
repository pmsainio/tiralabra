import unittest
from trie import Trie

trie_test = Trie()
test_data = [1, 2, 1, 3, 1, 4, 1, 5]


class TestTrie(unittest.TestCase):
    def SetUp(self):
        self.trie = trie_test
        self.data = test_data

    def test_insert(self):
        self.trie.insert(self.data)

        self.assertEqual(self.trie.root.children.items, 1)
