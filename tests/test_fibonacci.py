"""fibonacci関数のテスト"""

import unittest

from utils.fibonacci import fibonacci
from utils.exceptions import InvalidInputException


class FibonacciTestCase(unittest.TestCase):
    """fibonacci関数のテスト"""

    def test_fibonacci_with_n_1(self):
        """nが1の場合"""
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_fibonacci_with_n_2(self):
        """nが2の場合"""
        result = fibonacci(2)
        self.assertEqual(result, 1)

    def test_fibonacci_with_n_3(self):
        """nが3の場合"""
        result = fibonacci(3)
        self.assertEqual(result, 2)

    def test_fibonacci_with_n_10(self):
        """nが10の場合"""
        result = fibonacci(10)
        self.assertEqual(result, 55)

    def test_fibonacci_with_negative_n(self):
        """nが負の場合"""
        with self.assertRaises(InvalidInputException):
            fibonacci(-1)

    def test_fibonacci_with_float_n(self):
        """nが小数の場合"""
        with self.assertRaises(InvalidInputException):
            fibonacci(3.5)


if __name__ == "__main__":
    unittest.main()
