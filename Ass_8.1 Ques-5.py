import unittest
def is_valid_username(username):
    if len(username) < 5:
        return False
    if not username.isalnum():
        return False
    return True

class TestUsernameValidator(unittest.TestCase):
    def test_valid_username(self):
        self.assertTrue(is_valid_username("user01"))
    def test_short_username(self):
        self.assertFalse(is_valid_username("ai"))
    def test_username_with_spaces(self): 
        self.assertFalse(is_valid_username("user name"))
    def test_username_with_special_character(self): 
        self.assertFalse(is_valid_username("user@123"))
    def test_valid_mixed_case_username(self): 
        self.assertTrue(is_valid_username("User123"))
    def test_minimum_length_username(self):
        self.assertTrue(is_valid_username("abc12"))

if __name__ == "__main__":
    unittest.main()