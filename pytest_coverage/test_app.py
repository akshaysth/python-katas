import pytest

from app import factorial, fibonacci


@pytest.mark.parametrize("n, expected_fibonacci", [(1, 1), (10, 89), (30, 1346269)])
def test_multiple_fibonacci(n: int, expected_fibonacci: int) -> None:
    assert fibonacci(n) == expected_fibonacci


@pytest.mark.parametrize("n, expected_factorial", [(0, 1), (1, 1), (10, 3)])
def test_multiple_factorials(n: int, expected_factorial: int):
    assert factorial(n) == expected_factorial
