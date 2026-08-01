import unittest

from greet import greet


class GreetTests(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greet_with_empty_name(self):
        self.assertEqual(greet(""), "Hello, stranger!")


if __name__ == "__main__":
    unittest.main()
