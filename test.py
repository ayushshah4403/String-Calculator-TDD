import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)
        
    def test_single_number(self):
        self.assertEqual(add("6"), 6)
        
    def test_two_numbers_comma_seperated(self):
        self.assertEqual(add("5,7"), 12)
        
if __name__ == "__main__":
    unittest.main()
