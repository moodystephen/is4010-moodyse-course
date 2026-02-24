import pytest
from week02.lab02 import factorial, is_prime, reverse_string


def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (1, False),
    (0, False),
    (25, False),
])
def test_is_prime_cases(n, expected):
    assert is_prime(n) is expected


def test_reverse_string():
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("hello") == "olleh"
