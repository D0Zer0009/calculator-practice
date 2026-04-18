# divide.py
# 나눗셈 연산 계산기 모듈 | 작성자: D0Zer0009 | 2026-04-18

def divide(a, b):
    """두 수의 나눗셈 결과를 반환합니다. 0 나누기 시 ValueError 발생.
    Args: a (float): 피제수 / b (float): 제수
    Returns: float: a / b
    Raises: ValueError: b가 0일 때"""
    if b == 0:
        raise ValueError(
            "Cannot divide by zero / 0으로 나눌 수 없습니다."
        )
    return a / b