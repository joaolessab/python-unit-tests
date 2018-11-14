import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_greater_than_zero(self):
        value = fizzbuzz.is_fizzbuzz(1)
        self.assertTrue(value)

    def test_lower_than_a_hundred(self):
        value = fizzbuzz.is_fizzbuzz(100)
        self.assertTrue(value)

    def test_valid_interval(self):
        value = fizzbuzz.is_fizzbuzz(0)
        self.assertFalse(0)