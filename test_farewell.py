import unittest
from farewell import farewell, shout_farewell


class TestFarewell(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")

    def test_empty_string(self):
        self.assertEqual(farewell(""), "Goodbye, World!")

    def test_none(self):
        self.assertEqual(farewell(None), "Goodbye, World!")

    def test_special_characters(self):
        self.assertEqual(farewell("O'Brien"), "Goodbye, O'Brien!")
        self.assertEqual(farewell("张三"), "Goodbye, 张三!")
        self.assertEqual(farewell("@user!"), "Goodbye, @user!!")

    def test_whitespace_name(self):
        self.assertEqual(farewell("  "), "Goodbye,   !")

    def test_shout_farewell_basic(self):
        self.assertEqual(shout_farewell("Alice"), "GOODBYE, ALICE!")

    def test_shout_farewell_empty(self):
        self.assertEqual(shout_farewell(""), "GOODBYE, WORLD!")


if __name__ == "__main__":
    unittest.main()
