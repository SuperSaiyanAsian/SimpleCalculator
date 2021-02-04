import unittest
import simple_calculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(simple_calculator.add(6,9), 15)
        self.assertEqual(simple_calculator.add(3.6,2), 5.6)
        self.assertEqual(round(simple_calculator.add(-4.20,13.37), 2), 9.17)

    def test_subtract(self):
        self.assertEqual(simple_calculator.subtract(6,9), -3)
        self.assertEqual(simple_calculator.subtract(3.6,2), 1.6)
        self.assertEqual(simple_calculator.subtract(-4.20,13.37), -17.57)

    def test_multiply(self):
        self.assertEqual(simple_calculator.multiply(6,9), 54)
        self.assertEqual(simple_calculator.multiply(3.6,2), 7.2)
        self.assertEqual(round(simple_calculator.multiply(-4.20,13.37), 3), -56.154)

    def test_divide(self):
        self.assertEqual(round(simple_calculator.divide(6,9), 2), 0.67)
        self.assertEqual(simple_calculator.divide(3.6,2), 1.8)
        self.assertEqual(round(simple_calculator.divide(-4.20,13.37), 3), -0.314)
        self.assertRaises(ZeroDivisionError, simple_calculator.divide, 6, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)