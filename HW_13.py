# task 1
def even_numbers(iterable):
    for i in iterable:
        if i % 2 == 0:
            yield i


print(list(even_numbers([1, 2, 3, 4, 5, 6])))

# task 2
def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")          # код из лекции, что такое open?

def filter_lines(path, keyword):
    for line in read_lines(path):
        if keyword in line:
            yield line


for line in filter_lines("readme.md", "ERROR"):
    print(line)

# task 3
def chain(iter1, iter2):
    for i in iter1:
        yield i
    for n in iter2:
        yield n

print(list(chain([1, 2, 7], [3, 4])))

# task 4
def counter(start=0):
    current = start
    while True:
        yield current
        current += 1


c = counter(10)
print(next(c))  # 10
print(next(c))  # 11
print(next(c))

# task 5
def counter(start = 0):
    current = start
    while True:
        yield current
        current += 1

def take(n, iterable):
    count = 0
    for i in iterable:
        if count >= n:
            break
        yield i
        count += 1


c = counter(1567)
print(list(take(77, c)))

# task 6
import re

a = "one two three\tfour"
res = re.sub(r"\s" ,",", a)

print(res)

# task 7
emails = ["a@test.com", "b@mail.ru", "user@sub.example.org"]
domains = []
for email in emails:
    parts = email.split("@")
    domain = parts[1]
    domains.append(domain)

print(domains)

# task 8
import re

def is_valid_date(date) -> bool:
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return re.match(pattern, date) is not None


assert is_valid_date("2025-12-23")
assert not is_valid_date("25-12-23")

print(is_valid_date("2025-12-23"))
print(is_valid_date("25-12-23"))

# task 9 по положению, если статус всегда на 7 месте
log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
status = []
for l in log:
    parts = log.split(" ")
    status = parts[6]

print(status)

# task 9 если статус это всегда перводе вхождение 3 цифр
import re

log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
status = re.search(r'\d{3} ', log).group().strip()
print(status)

# task 10
import re


def is_strong_password(passw):
    a = re.search(r'\d', passw) is not None
    b = re.search(r"[A-Z]", passw) is not None

    if len(passw) >= 8 and a and b:
        print("Password is accepted")
        return True
    else:
        print("Invalid password")
        return False


assert is_strong_password("Abcdef12")
assert not is_strong_password("abcdef12")
assert not is_strong_password("Abcdefgh")

# task 11
import re

s = "<p>Hello <b>world</b>!</p>"
new = re.sub(r'<[^>]+>', "", s)  #[] класс символов
print(new)

# task 12
import re


s = "name=John; age=30; city=London;"

pairs = re.findall(r"(\w+)=([^;]+)", s)
result = dict(pairs)

print(result)

# task 13
import re


def find_phones(text):
    pattern = r"((\+7-\d{3}-\d{3}-\d{2}-\d{2})|(8\s*\(\d{3}\)\s*\d{3}-\d{2}-\d{2}))"
    return re.findall(pattern, text)

text = "Мой телефон: +7-999-123-45-67, офис: 8 (812) 555-66-77."
print(find_phones(text))

# task 14
import re


s = "one,two;three four"
words = re.split(r"[,\s;]+", s)
print(words)

# task 15
import re


url = "/api/v1/users/123/orders/456"

match = re.search(r"users/(\d+)/orders/(\d+)", url)
result = match.groups()

print(result)

