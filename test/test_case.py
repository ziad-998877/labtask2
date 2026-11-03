import unittest

from calculator import calculate


class TestCalculator(unittest.TestCase):

    
    def test_addition_positive_numbers(self):
        self.assertEqual(calculate(5, 3, "+"), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(calculate(-5, -3, "+"), -8)

    def test_addition_positive_and_negative(self):
        self.assertEqual(calculate(-5, 3, "+"), -2)

    def test_addition_with_zero(self):
        self.assertEqual(calculate(5, 0, "+"), 5)

    def test_addition_decimal_numbers(self):
        self.assertAlmostEqual(calculate(1.5, 2.5, "+"), 4.0)