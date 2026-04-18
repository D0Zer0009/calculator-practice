# divide.py
# 나눗셈 연산 계산기 모듈 | 작성자: D0Zer0009 | 2026-04-18

def divide(a, b):
    """두 수의 나눗셈 결과를 반환합니다. 0 나누기 시 ValueError 발생.
    Args: a (float): 피제수 / b (float): 제수
    Returns: float: a / b
    Raises: ValueError: b가 0일 때"""
    if b == 0:
        raise ValueError(
            f"Cannot divide by zero: divisor was {b}"
        )
    return a / b

def test_divide_negative(self):
    """음수 나눗셈"""
    self.assertEqual(divide(-10, 2), -5.0)

def test_divide_by_zero_msg(self):
    """에러 메시지에 divisor 값 포함 확인"""
    with self.assertRaises(ValueError) as ctx:
        divide(5, 0)
    self.assertIn(
        "divisor was 0",
        str(ctx.exception)
    )