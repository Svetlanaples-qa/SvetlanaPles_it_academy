# task 1
def est_info(author, component):
    def decorator(cls):
        cls.author = author
        cls.component = component
        return cls
    return decorator

@est_info(author="Иван", component="Auth")
class TestLogin:
    pass

print(TestLogin.author) # Иван
print(TestLogin.component) # Auth

# task 2

PAGES = []

def register_page(cls):
    PAGES.append(cls)
    return cls

@register_page
class LoginPage:
    pass

@register_page
class DashboardPage:
    pass

print([cls.__name__ for cls in PAGES])

#task 3

class Tag():
    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, cls):
        cls.tag_name = self.tag_name
        return cls
@Tag("smoke")
class SmokeTests:
    pass

@Tag("regression")
class RegressionTests:
    pass

print(SmokeTests.tag_name)
print(RegressionTests.tag_name)

# task 4

from enum import Enum

class Environment(Enum):
    DEV = 1
    STAGE = 2
    PROD = 3

URLS = {
    Environment.DEV: "https://dev.example.com",
    Environment.STAGE: "https://stage.example.com",
    Environment.PROD: "https://example.com",
}

def get_base_url(env: Environment):
    return URLS[env]


print(get_base_url(Environment.DEV))
print(get_base_url(Environment.PROD))


# task 5

from enum import Enum

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


tasks = [
("Починить тест логина", Priority.HIGH),
("Обновить документацию", Priority.LOW),
("Настроить CI", Priority.MEDIUM),
]
# Сортировка по значению enum
tasks_sorted = sorted(tasks, key=lambda item: item[1].value)
for name, prio in tasks_sorted:
    print(prio.name, "-", name)

# task 6
from enum import Enum

class TestType(Enum):
    API = 1
    UI = 2
    UNIT = 3

tests = [
    ("test_login_api", TestType.API),
    ("test_login_ui", TestType.UI),
    ("test_sum", TestType.UNIT),
    ("test_profile_api", TestType.API),
]

def filter_tests_by_type(tests, test_type: TestType):
    result = []
    for name, ttype in tests:
        if ttype == test_type:
            result.append(name)
    return result

# Проверка
print(filter_tests_by_type(tests, TestType.API))
print(filter_tests_by_type(tests, TestType.UI))

# task 7

def parse_int_list(strings):
    nums = []
    for s in strings:
        try:
            nums.append(int(s))
        except ValueError:
            print(f"'{s}' не является целым числом, пропускаем")
    return nums

raw = ["11", "20", "abc", "30", "4.5", "40"]
nums = parse_int_list(raw)
print(nums)

# task 9

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float


p1 = Point(1.0, 2.0)
p2 = Point(-3.5, 4.2)

print(p1)
print(p2)

# task 10

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1

    def total(self):
        return self.price * self.quantity

p1 = Product("Keyboard", 50.0, 2)
p2 = Product("Mouse", 25.0)

print(p1, "total:", p1.total())
print(p2, "total:", p2.total())

# task 11

from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    authors: list[str] = field(default_factory=list)
    year: int | None = None

    def formatted(self):
        if self.year is None:
            year_part = ""
        else:
            year_part = f" ({self.year})"

        if len(self.authors) == 0:
            authors_part = "—"
        else:
            authors_part = ", ".join(self.authors)

        return f"{self.title}{year_part} — {authors_part}"

b1 = Book("Python 101", ["John Doe"], 2020)
b2 = Book("Безымянная книга")
b3 = Book("Совместный труд", ["Alice", "Bob"], 2009)

for b in (b1, b2, b3):
    print(b.formatted())