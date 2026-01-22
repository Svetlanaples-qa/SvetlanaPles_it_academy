import math
import argparse
import logging
import sys

# logger
logger = logging.getLogger("calculator")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("calculator.log", mode="a", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# вычисления
def calculate(num1, operator, num2):
    logger.info(f"Calculating: {num1} {operator} {num2}")

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/" or operator == ":":
        return num1 / num2

    elif operator == "^" or operator == "**":
        return math.pow(num1, num2)

    else:
        raise ValueError(f"Неизвестная операция: {operator}")

#парсер
parser = argparse.ArgumentParser(description="Calculator",
                                 epilog="Доступные операции: +, -, *, /, **.\n"
                                        "Пример ввода: 10 + 5.\n"
                                        'Чтобы закрыть калькулятор введите "q" или "выход."'
                                 )
parser.add_argument("num1", type=float, help="Первое число")
parser.add_argument("operator", help="Операция (+, -, *, /, **)")
parser.add_argument("num2", type=float, help="Второе число")

#валидация формата
try:
    args = parser.parse_args()
except SystemExit:
    print("Неверный формат ввода. Пример: 10.4 * 5")
    logger.error("Неверный формат ввода")
    sys.exit(1)

# Основная программа
try:
    result = calculate(args.num1, args.operator, args.num2)
    print("Результат:", result)
    logger.info(f"Result: {result}")

except ZeroDivisionError:
    print("Деление на ноль!")
    logger.error("Деление на ноль")

except ValueError as e:
        print("Ошибка:", e)
        logger.error(f"Error: {e}")
except Exception:
    print("Неожиданная ошибка! cмотри calculator.log")
    logger.exception("Unexpected error")