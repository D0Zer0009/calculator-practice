# multiply.py
# 곱셈 연산 계산기 모듈 | 작성자: D0Zer0009 | 2026-04-18

def multiply(a, b):
    """두 수의 곱을 반환합니다.
    Args: a, b (float): 곱할 두 수
    Returns: float: a * b"""
    return a * b

def test_multiply_float(self):
    """소수점 곱셈"""
    self.assertAlmostEqual(multiply(0.1, 0.2), 0.02, places=5)
