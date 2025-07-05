import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)
        
    def test_single_number(self):
        self.assertEqual(add("6"), 6)
        
    def test_two_numbers_comma_separated(self):
        self.assertEqual(add("5,7"), 12)
        
    def test_multiple_numbers_comma_separated(self):
        self.assertEqual(add("1,2,3,4,5"), 15)
    
    def test_newline_as_delimiter(self):
        self.assertEqual(add("1\n2,3\n4,5"), 15)
        
    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2;3;4;5"), 15)
        
    def test_negative_numbers_raise_exception(self):
        with self.assertRaises(Exception) as context:
            add("1, -2, 3, 4, -5")
        self.assertEqual(str(context.exception), "Negatives not allowed: -2,-5")
        
    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(add("6,1001"), 6)
        self.assertEqual(add("5,1000"), 1005)
        
    def test_delimiter_of_custom_length(self):
        self.assertEqual(add("//[***]\n1***2***3***4***5"), 15)
        
if __name__ == "__main__":
    unittest.main()
