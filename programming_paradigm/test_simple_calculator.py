import unittest
from simple_calculator import SimpleCalculator
class test_simple_calculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""
    def setUp(self):
        """Set up the SimpleCalculator instance for testing."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    def test_subtraction(self):
        
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    def test_multiplication(self):
       
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)
    def test_division(self):
       
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 0), None)