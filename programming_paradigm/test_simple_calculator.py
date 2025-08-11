import unittest
from simple_calculator import SimpleCalculator
class test_simple_calculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""
    def test_addition(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 0), 0)
    def test_subtraction(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(-1, -1), 0)
    def test_multiplication(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(0, 5), 0)
    def test_division(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(5, 0), None)