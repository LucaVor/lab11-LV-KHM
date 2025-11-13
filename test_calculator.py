# https://github.com/LucaVor/lab11-LV-KHM
# Partner 1: Luca Voros
# Partner 2: Kiro Habib

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(3, 3), 6)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(add(60, 7), 67)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(70, 3), 67)
        self.assertEqual(subtract(20, 40), -20)

    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(3, 9), 3)
        self.assertAlmostEqual(div(2, 7), 3.5)
    # ##########################

    ####### Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1000), 3)

    def test_log_invalid_base(self):  # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.414213, places=5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), 1.414213, places=5)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()