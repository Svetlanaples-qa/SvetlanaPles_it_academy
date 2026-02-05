def sum_numbers(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2


def sub_numbers(num1: int | float, num2: int | float) -> int | float:
    return num1 - num2


def mul_numbers(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2


def div_numbers(num1: int | float, num2: int | float) -> int | float:
    if num2 == 0:
        raise ValueError("Division by zero is not allowed")
    return num1 / num2