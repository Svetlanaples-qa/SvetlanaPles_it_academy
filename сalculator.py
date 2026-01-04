import math

# Приветствие
print("Добро пожаловать в калькулятор!")
print("Доступные операции: +,  -,  *,  /, **(возведение в степень)")
print("Пример ввода: 10 + 5")
print('Чтобы закрыть калькулятор введите"q" или "выход"')

while True:
    user_input = input("Ввод: ")

    # Выход из программы
    if user_input.lower() == "q" or user_input.lower() == "exit" or user_input.lower() == "выход":
        print("Выход из калькулятора.")
        break

    parts = user_input.split()

    # Проверка вводных данных
    if len(parts) != 3:
        print("Ошибка! Формат должен быть с пробелами: 4 + 2")
        continue

    num1 = parts[0]
    operator = parts[1]
    num2 = parts[2]

    # Преобразовываем num1 и num2. isdigit() не подходит: возвращает False если число дробное.
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print("Ошибка! Введите правильные числа!")
        continue

    # Вычисления
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/" or operator == ":":
        if num2 == 0:             # Проверка деления на 0
            print("Ошибка! Деление на 0!")
            continue
        result = num1 / num2
    elif operator == "^" or operator == "**":
        result = math.pow(num1, num2)
    else:
        print("Ошибка! Неверный оператор.")
        continue

    print("Результат:", result)