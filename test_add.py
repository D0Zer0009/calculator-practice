# test_add.py | 덧셈 연산 계산기 테스트 | 작성자: D0Zer0009

import unittest
from add import add


class TestCalculator(unittest.TestCase):

    # ── 덧셈 테스트 ──────────────────────────
    def test_add_positive(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative(self):
        self.assertEqual(add(-3, -5), -8)

    def test_add_mixed(self):
        self.assertEqual(add(10, -3), 7)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


if __name__ == '__main__':
    unittest.main()