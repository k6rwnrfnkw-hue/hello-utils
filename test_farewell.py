import unittest
from greet import farewell, whisper


class TestFarewell(unittest.TestCase):
    def test_farewell_normal(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")

    def test_farewell_empty_string(self):
        self.assertEqual(farewell(""), "Goodbye, World!")

    def test_farewell_none(self):
        self.assertEqual(farewell(None), "Goodbye, World!")

    def test_farewell_single_char(self):
        self.assertEqual(farewell("A"), "Goodbye, A!")

    def test_farewell_spaces(self):
        self.assertEqual(farewell("  "), "Goodbye,   !")

    def test_farewell_unicode(self):
        self.assertEqual(farewell("世界"), "Goodbye, 世界!")

    def test_farewell_number_string(self):
        self.assertEqual(farewell("42"), "Goodbye, 42!")


class TestWhisper(unittest.TestCase):
    def test_whisper_normal(self):
        self.assertEqual(whisper("Alice"), "goodbye, alice!")

    def test_whisper_empty_string(self):
        self.assertEqual(whisper(""), "goodbye, world!")

    def test_whisper_none(self):
        self.assertEqual(whisper(None), "goodbye, world!")

    def test_whisper_already_lowercase(self):
        self.assertEqual(whisper("bob"), "goodbye, bob!")

    def test_whisper_mixed_case(self):
        self.assertEqual(whisper("BoBo"), "goodbye, bobo!")

    def test_whisper_single_char(self):
        self.assertEqual(whisper("Z"), "goodbye, z!")

    def test_whisper_unicode(self):
        self.assertEqual(whisper("世界"), "goodbye, 世界!")


if __name__ == "__main__":
    unittest.main()
