import unittest
from index import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_numbers(3,7)
        self.assertEqual(result, 10)
        print("Test 'test_add_positive_numbers' passed.")
    
    def test_add_negative_numbers(self):
        result = add_numbers(-5, -3)
        self.assertEqual(result, -8)
        print("Test 'test_add_negative_numbers' passed.")

    def test_add_mix_numbers(self):
        result = add_numbers(10, -2)
        self.assertEqual(result, 8)
        print("Test 'test_add_mix_numbers' passed.")

if __name__ == '__main__':
    unittest.main()
