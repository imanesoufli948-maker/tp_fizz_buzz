import pytest

from fizz_buzz import fizz_buzz

@pytest.mark.parametrize("n",[1,2,4])
def test_fizz_buzz_other_number_return_fizz_buzz(n):
    assert fizz_buzz(n) == "fizz buzz"

@pytest.mark.parametrize("n",[3,6,5,9])
def test_fizz_buzz_multiples_3_return_fizz(n):
    assert fizz_buzz(n) == "fizz"