# task 1
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Move with {self.speed} km/h")

class Car(Vehicle):
    def honk(self):
        print("bip bip!")

car = Car(200)
car.move()
car.honk()

# task 2

class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    salary = 8000


class Developer(Employee):
    salary = 10000


manager = Manager("Ivan")
developer = Developer("Alex")

print(manager.salary)
print(developer.name, developer.salary)

# task 3

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area
    print("rectangle area =")


class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        area = self.rad * self.rad * 3.14
        return area
    print("circle area =")


#rect = Rectangle(5, 3)
#print(rect.area())

cir = Circle(7)
print(cir.area())

# task 4

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств")

class SavingsAccount(Account):
    def add_interest(self):
        self.balance *= 1.05



account = SavingsAccount(0)
account.withdraw(500)
account.add_interest()
print(account.balance)