import unittest
from trie import Trie

trie_test = Trie()
test_data = [1, 2, 1, 3, 1, 4, 1, 5]


class TestTrie(unittest.TestCase):
    def SetUp(self):
        self.trie = trie_test
        self.data = test_data

    # testataan, että ensimmäisen kerroksen jälkeläiset löytyy
    def test_insert_root(self):
        self.trie.insert(self.data)

        self.assertEqual(self.trie.root.children.items, 1)

    # tätä testiä pitää hioa, testataan toisen polven jälkeläisiä
    def test_root_children(self):
        self.trie.insert(self.data)

        # self.assertEqual(self.trie.root.chidren(1), [2,3,4,5])
