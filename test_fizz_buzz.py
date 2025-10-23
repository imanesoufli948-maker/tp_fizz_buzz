import pytest

from fizz_buzz import fizz_buzz

@pytest.mark.parametrize("n",[1])
def test_fizz_buzz_1_return_fizz_buzz(n):
    assert fizz_buzz(n) == "fizz buzz"