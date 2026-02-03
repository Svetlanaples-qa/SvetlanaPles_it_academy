import unittest
from calculator3 import calculate


class TestCalculator(unittest.TestCase):
    def test_addition(self):                                      # один пример с дополнительным error message если тест падает
        print("Выполняю сложение")
        result = calculate(10, "+", 6)
        expected = 15
        self.assertEqual(result, expected, msg=f"Результат {result}, должен быть {expected}")

    def test_subtraction(self):
        print("Выполняю вычитание")
        self.assertEqual(calculate(10, "-", 5), 4)

    def test_muliplication(self):
        print("Выполняю умножение")
        self.assertEqual(calculate(10, "*", 5), 50)

    def test_division(self):
        print("Выполняю деление")
        self.assertEqual(calculate(10, "/", 5), 2)

    def test_exponentiation(self):
        print("Выполняю возведение в степень")
        self.assertEqual(calculate(2, "**", 3), 8)

    def test_unknown_operator(self):
        print("Выполняю негативный тест с неопознаным оператором")
        with self.assertRaises(ValueError):
            calculate(1, "%", 2)

    def test_division_by_zero(self):
        print("Выполняю негативный тест с делением на ноль")
        with self.assertRaises(ZeroDivisionError):
            calculate(1, "/", 0)

