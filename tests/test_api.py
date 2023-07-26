"""APIのテスト"""

import unittest

from app import app


class FibonacciAPITestCase(unittest.TestCase):
    """APIのテスト"""

    def test_fibonacci_with_valid_n(self):
        """正常なリクエストの場合。n=10"""
        tester = app.test_client(self)
        response = tester.get("/fib?n=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 55})

    def test_fibonacci_with_missing_n(self):
        """nがない場合のエラーテスト"""
        tester = app.test_client(self)
        response = tester.get("/fib")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json,
            {
                "status": 400,
                "message": "Missing query parameter 'n'. Please provide 'n' as a positive integer.",
            },
        )

    def test_fibonacci_with_non_integer_n(self):
        """nが数字でない場合のエラーテスト"""
        tester = app.test_client(self)
        response = tester.get("/fib?n=abc")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json,
            {"status": 400, "message": "Invalid input. n must be a positive integer."},
        )


if __name__ == "__main__":
    unittest.main()
