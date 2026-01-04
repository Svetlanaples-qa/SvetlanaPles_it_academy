import math

# вычисления
def calculate(num1, num2, operator):
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
        raise ValueError("Неизвестная операция")


# Основная программа
print("Добро пожаловать в калькулятор!")
print("Доступные операции: +, -, *, /, **")
print("Пример ввода: 10 + 5")
print('Чтобы закрыть калькулятор введите "q" или "выход"')

while True:
    user_input = input("Ввод: ")

    # Выход из программы
    if user_input.lower() in ("q", "exit", "выход"):
        print("Выход из калькулятора.")
        break

    parts = user_input.split()

    # Проверка формата
    if len(parts) != 3:
        print("Ошибка! Формат должен быть: 4 + 2")
        continue

    num1, operator, num2 = parts

    try:
        num1 = float(num1)
        num2 = float(num2)

        # Основное вычисление
        result = calculate(num1, num2, operator)

        print("Результат:", result)

    except ZeroDivisionError:
        # Деление на ноль
        print("Ошибка! Деление на ноль!")

    except ValueError as e:
        # Неизвестная операция
        print("Ошибка:", e)