import pytest
import pytest_check as check
import scr_calc.calc as calc


@pytest.mark.parametrize("num1, num2, exp", [(3, 16, 19), (-3, -16, -19)], ids=["positive_nums", "negative_nums"])
def test_sum_numbers(num1: int | float, num2: int | float, exp: int | float) -> None:
    assert calc.sum_numbers(num1, num2) == exp


def test_div_zero_error() -> None:
    with pytest.raises(ZeroDivisionError):
        calc.div_numbers(num1=5, num2=0)

@pytest.mark.parametrize("num1, num2, exp", [(10, 2, 5), (9, 3, 3)], ids=["exampl1", "example2"])
def test_division(num1: int | float, num2: int | float, exp: int | float) -> None:
    assert calc.div_numbers(num1, num2) == exp

def test_sum_with_fixture(data):
    result = data[0] + data[1]
    assert result == 3

def test_fixture_data(data):
    assert data == [1, 2]