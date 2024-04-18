# test_simple_math.py
import unittest
from simple_math import SimpleMath


class SimpleMathTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = SimpleMath()

    def test_somme(self):
        self.assertEqual(SimpleMath().somme(1, 1), 2)

    def test_soustraction(self):
        self.assertEqual(self.instance.soustraction(2, 1), 1)

    def test_somme_liste(self):
        self.assertEqual(self.instance.somme_liste([1, 2, 3, 4]), 10)


if __name__ == '__main__':
    unittest.main()
