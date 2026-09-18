import unittest

def to_uppercase(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.upper()
def to_lowercase(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.lower()
class TestStringCaseConverter(unittest.TestCase):

    def test_uppercase(self):
        self.assertEqual(to_uppercase("ai coding"), "AI CODING")
    def test_lowercase(self):
        self.assertEqual(to_lowercase("TEST"), "test")
    def test_uppercase_empty(self):
        self.assertEqual(to_uppercase(""), "")
    def test_lowercase_empty(self):
        self.assertEqual(to_lowercase(""), "")
    def test_uppercase_mixed_case(self):
        self.assertEqual(to_uppercase("Ai Coding"), "AI CODING")
    def test_lowercase_mixed_case(self):
        self.assertEqual(to_lowercase("Ai Coding"), "ai coding")
    def test_uppercase_invalid_input(self):
        with self.assertRaises(TypeError):
            to_uppercase(None)
    def test_lowercase_invalid_input(self):
        with self.assertRaises(TypeError):
            to_lowercase(None)

if __name__ == "__main__":
    unittest.main()