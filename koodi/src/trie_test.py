import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.t = Trie(1)
        self.tune_1 = [1, 2, 1, 3, 1, 4]
        self.tune_2 = [1, 3, 1, 5, 1, 6, 1, 7]
        self.tune_3 = [1, 3]

    def test_setter_and_getter(self):
        self.t.insert(self.tune_1)

        result = self.t.get([1])
        self.assertEqual(result[0], [2, 3, 4])

    def test_multiple_inserts(self):
        self.t.insert(self.tune_1)
        self.t.insert(self.tune_2)
        self.t.insert(self.tune_3)

        result = self.t.get([1])
        self.assertEqual(result[0], [2, 3, 4, 5, 6, 7])

    def test_weights(self):
        self.t.insert(self.tune_1)

        result = self.t.get([1])
        self.assertEqual(result[1], [1, 1, 1])

    def test_weight_growth(self):
        self.t.insert(self.tune_1)
        self.t.insert(self.tune_2)
        self.t.insert(self.tune_3)

        result = self.t.get([1])
        self.assertEqual(result[1], [1, 3, 1, 1, 1, 1])

    def test_path_too_long(self):
        with self.assertRaises(ValueError) as context:
            self.t.get([1, 2, 3])

        self.assertEqual(
            str(context.exception),
            "Key must be shorter than degree. Current degree is 1.")

    def test_getter(self):
        self.t.insert(self.tune_1)
        root = self.t.get([])
        self.assertEqual(root, ([1, 2, 3, 4], [3, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
