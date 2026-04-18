# test_multiply.py | 곱셈 연산 계산기 테스트 | 작성자: D0Zer0009

import unittest
from multiply import multiply

class TestCalculator(unittest.TestCase):
    # ── 곱셈 테스트 ──────────────────────────
    def test_multiply_positive(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-4, 5), -20)

    def test_multiply_zero(self):
        self.assertEqual(multiply(100, 0), 0)

if __name__ == '__main__':
    unittest.main()