# task 1.1

class Product():
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Отрицательную цену задать нельзя")
        else:
            self._price = value

p = Product(100)
print(p.price)

p.price = 250
print(p.price)

p.price = -10
print(p.price)


# task 1.2

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rectangle(3, 4)
print(rect.area)

rect.width = 10
print(rect.area)

#task 1.3

class TestStats():
    def __init__(self, passed, total):
        self.passed = passed
        self.total = total

    @property
    def success_rate(self):
        return 100 * self.passed / self.total


stats = TestStats(8, 10)
print(stats.success_rate)

# task 2.1

class PermissionMixin:
    def has_permission(self, user_role):
        return user_role == "admin"


class SecureAction(PermissionMixin):
    def execute(self, role):
        if self.has_permission(role):
            print("Админ. Метод запущен")
        else:
            print("Нет прав.")


action = SecureAction()
action.execute("user")
action.execute("admin")

# task 2.2

class Logger:
    def log(self, message):
        print(f"[Log] {message}")


class Service:
    def __init__(self):
        self.logger = Logger()

    def process(self):
        self.logger.log("Начал обработку")
        print("Обрабатываю")
        self.logger.log("Закончил обработку")


s = Service()
s.process()

# task 2.3

class Admin:
    def create_user(self, name):
        print(f"Создан пользователь: {name}")


class Support:
    def create_ticket(self, text):
        print(f"Создан тикет: {text}")


class SuperUser(Admin, Support):
    pass


su = SuperUser()
su.create_user("Ivan")
su.create_ticket("Падает сервис")


# task 2.4

class A:
    def who_am_i(self):
        print("A")


class B(A):
    def who_am_i(self):
        print("B")


class C(A):
    def who_am_i(self):
        print("C")


class D(B, C):
    pass


d = D()
d.who_am_i()
print(D.mro())

# task 2.5

class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class RetryMixin:
    def retry(self, attempts):
        for i in range(1, attempts + 1):
            print(f"Попытка {i}")
            self.run()


class Job(LoggingMixin, RetryMixin):
    def run(self):
        self.log("Выполняем задачу")
        print("Job что-то делает...")


j = Job()
j.retry(2)

# task 3.1

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return f"Прямоугольник. Площадь: {self.w * self.h}"


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        value = math.pi * self.r * self.r
        text = f"{value:.2f}".replace(".", ",")
        return f"Круг. Площадь: {text}"


shapes = [Rectangle(3, 4), Circle(2)]
for s in shapes:
    print(s.area())

# task 3.2

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    def go(self):
        print("Начинаем движение")
        self.move()


class Car(Transport):
    def move(self):
        print("Едем по дороге на машине")


class Bike(Transport):
    def move(self):
        print("Едем на велосипеде")


for t in (Car(), Bike()):
    t.go()

#task 3.3

from abc import ABC, abstractmethod


class BaseTestCase(ABC):
    @abstractmethod
    def prepare_data(self):
        pass

    @abstractmethod
    def run_test(self):
        pass

    def run(self):
        print(f"=== {self.__class__.__name__} ===")
        self.prepare_data()
        self.run_test()


class LoginTest(BaseTestCase):
    def prepare_data(self):
        print("Готовим пользователя для логина")

    def run_test(self):
        print("Проверяем успешный логин")


class PaymentTest(BaseTestCase):
    def prepare_data(self):
        print("Готовим данные и баланс")

    def run_test(self):
        print("Проверяем успешный платеж")


tests = [LoginTest(), PaymentTest()]
for t in tests:
    t.run()

# task 4.1

from abc import ABC, abstractmethod


class BaseTest(ABC):
    @abstractmethod
    def run(self):
        pass


class APITest(BaseTest):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def run(self):
        print(f"API тест: проверяем эндпоинт {self.endpoint}")


class UITest(BaseTest):
    def __init__(self, page_name):
        self.page_name = page_name

    def run(self):
        print(f"UI тест: проверяем страницу {self.page_name}")


def run_all(tests):
    for t in tests:
        t.run()


tests = [
    APITest("/login"),
    UITest("LoginPage"),
    APITest("/users"),
]

run_all(tests)

# task 4.2

def print_length(obj):
    print(len(obj))


class TestCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


print_length("Python")
print_length([1, 2, 3])
print_length({"a": 1, "b": 2})
print_length(TestCollection([10, 20, 30, 40]))

# task 5.1

class TestResults:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)


results = TestResults()
results["test_login"] = "passed"
results["test_payment"] = "failed"

print(results["test_login"])
print(len(results))

# task 5.2

class Duration:
    def __init__(self, seconds):
        self.seconds = float(seconds)

    def __add__(self, other):
        return Duration(self.seconds + other.seconds)

    def __str__(self):
        return f"{self.seconds:.2f} sec"


d1 = Duration(1.5)
d2 = Duration(2.7)
d3 = d1 + d2

print(d1)
print(d2)
print(d3)

# task 5.3

class TestRunner:
    def __init__(self, test_names):
        self.test_names = test_names

    def __call__(self):
        print("Запускаем тесты:")
        for name in self.test_names:
            print(f"- {name}")
        print(f"Всего тестов: {len(self.test_names)}")


runner = TestRunner(["test_login", "test_signup", "test_payment"])
runner()