import math
import logging


# logger
logger = logging.getLogger("calculator3")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("calculator.log", mode="a", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# вычисления
def calculate(num1: float, operator: str, num2: float) -> float:
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

def main_progr() -> None:
    while True:
        user_input = input("Ввод: ").strip() # strip!!
        logger.info(f"User input: {user_input}")

        # Выход из программы
        if user_input.lower() in ("q", "exit", "выход"):
            print("Выход из калькулятора.")
            logger.info("Calculator closed by user")
            break

        parts = user_input.split()
        # Проверка вводных данных
        if len(parts) != 3:
            print("Ошибка! Формат должен быть с пробелами: 4 + 2")
            logger.warning(f"Invalid input format: {user_input}")
            continue

        num1, operator, num2 = parts
        # Преобразовываем num1 и num2
        try:
            num1 = float(num1)
            num2 = float(num2)

            result = calculate(num1, operator, num2)

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

