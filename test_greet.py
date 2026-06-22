import unittest
from greet import greet, shout


class TestGreet(unittest.TestCase):
    def test_greet_normal(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_another_name(self):
        self.assertEqual(greet("Claude"), "Hello, Claude!")

    def test_greet_empty_string(self):
        self.assertEqual(greet(""), "Hello, World!")

    def test_greet_none(self):
        self.assertEqual(greet(None), "Hello, World!")

    def test_greet_whitespace(self):
        self.assertEqual(greet("  "), "Hello,   !")

    def test_greet_single_char(self):
        self.assertEqual(greet("A"), "Hello, A!")

    def test_greet_numeric_string(self):
        self.assertEqual(greet("123"), "Hello, 123!")

    def test_greet_special_chars(self):
        self.assertEqual(greet("O'Brien"), "Hello, O'Brien!")


class TestShout(unittest.TestCase):
    def test_shout_normal(self):
        self.assertEqual(shout("Alice"), "HELLO, ALICE!")

    def test_shout_empty_string(self):
        self.assertEqual(shout(""), "HELLO, WORLD!")

    def test_shout_none(self):
        self.assertEqual(shout(None), "HELLO, WORLD!")

    def test_shout_already_upper(self):
        self.assertEqual(shout("BOB"), "HELLO, BOB!")

    def test_shout_lowercase(self):
        self.assertEqual(shout("alice"), "HELLO, ALICE!")

    def test_shout_mixed_case(self):
        self.assertEqual(shout("aLiCe"), "HELLO, ALICE!")


if __name__ == "__main__":
    unittest.main()
