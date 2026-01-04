import datetime
import math
import random

# task 1 DATETIME
now = datetime.datetime.now()
print(now)

# task 2 DATETIME
bday = datetime.date(1995, 9, 7)
print(f"My birthday is {bday}")

# task 5 DATETIME
formatted = datetime.datetime.strptime("31/12/2025 23:59:59", "%d/%m/%Y %H:%M:%S")
print(formatted)


# task 2 MATH
print(math.floor(9.8))

# task 7 MATH
print(math.factorial(8))

# task 10 MATH
def tang(degrees):
    radians = math.radians(degrees)
    return math.tan(radians)


angle = float(input("Enter an angle in degrees: "))
result = tang(angle)
print("Tangent:", result)


# task 2 RANDOM
import random

letters = "abcdefghijklmnopqrstuvwxyz"

password = "".join(random.choice(letters) for i in range(8))
print("Случайный пароль:", password)

# task 3 RANDOM
methods = ["GET", "POST", "PUT", "DELETE"]

def random_http_method():
    return random.choice(methods)

print("Случайный HTTP метод:", random_http_method())

# task 4 RANDOM
tests = ["test_login", "test_logout", "test_add_to_cart", "test_checkout"]

random.shuffle(tests)
print("Случайный порядок тестов:", tests)


