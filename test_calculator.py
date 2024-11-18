import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    # add 10 test cases
    def test_add1(self):
        self.assertEqual(self.calc.add(2, 1), 3)
    def test_add2(self):
        self.assertEqual(self.calc.add(-1000,0),-1000)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
    def test_substract2(self):
        self.assertEqual(self.calc.subtract(2, 10), -8)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-5, 2), -10)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(5, 5), 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()