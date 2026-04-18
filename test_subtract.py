# test_subtract.py | 덧셈 연산 계산기 테스트 | 작성자: D0Zer0009

import unittest
from subtract import subtract

class TestCalculator(unittest.TestCase):
 # ── 뺄셈 테스트 ──────────────────────────
    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -3), -2)

if __name__ == '__main__':
    unittest.main()