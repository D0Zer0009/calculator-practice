# test_divide.py | 나눗셈 연산 계산기 테스트 | 작성자: D0Zer0009

import unittest
from divide import divide

class TestCalculator(unittest.TestCase):
    # ── 나눗셈 테스트 ────────────────────────
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_float(self):
        self.assertAlmostEqual(divide(1, 3), 0.333, places=3)

    def test_divide_large(self):
        self.assertEqual(divide(1000000, 1000), 1000.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_divide_by_zero_msg(self):
        with self.assertRaises(ValueError) as ctx:
            divide(5, 0)
        self.assertIn(
            "Cannot divide by zero",
            str(ctx.exception)
        )

if __name__ == '__main__':
    unittest.main()