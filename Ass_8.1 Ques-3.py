import unittest

def sum_list(numbers):
    total = 0
    for item in numbers:
        if isinstance(item, (int, float)):
            total += item
    return total

class TestSumList(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)
    def test_empty_list(self):
        self.assertEqual(sum_list([]), 0)
    def test_negative_numbers(self):
        self.assertEqual(sum_list([-1, 5, -4]), 0)
    def test_non_numeric_values(self):
        self.assertEqual(sum_list([2, "a", 3]), 5)
    def test_zero(self):
        self.assertEqual(sum_list([10, 0, 5]), 15)

if __name__ == "__main__":
    unittest.main()