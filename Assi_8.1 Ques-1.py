import unittest
# Function to  check if a number is even
def is_even(n):
	if not isinstance(n, int):
		raise TypeError("Input must be an integer")
	return n%2==0

class TestIsEven(unittest.TestCase):

	def test_positive_even(self): 
		self.assertTrue(is_even(2))
	def test_positive_odd(self): 
		self.assertFalse(is_even(7))
	def test_zero(self):
		self.assertTrue(is_even(0))
	def test_negative_even(self): 
		self.assertTrue(is_even(-4))
	def test_negative_odd(self): 
		self.assertFalse(is_even(-5))
	def test_large_even_number(self):
		self.assertTrue(is_even(1000000))

if __name__ == "__main__":
	unittest.main()