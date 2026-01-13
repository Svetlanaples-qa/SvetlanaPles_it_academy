# task 2

with open("numbers.txt", "w", encoding="utf-8") as f:
    f.write("text\n\n")
    for i in range(6):
        f.write(f"{i}\n")

with open("numbers.txt", "r", encoding="utf-8") as f:
    a = f.read()

print(a)

# task 3

with open("numbers.txt", "w", encoding="utf-8") as f:
    f.write("text\n\n")
    for i in range(6):
        f.write(f"{i}\n")

def count_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines)


print(count_lines("numbers.txt"))

# task 4
with open("sours1.txt", "w", encoding="utf-8") as f:
    f.write("text\n\n")
    for i in range(6):
        f.write(f"{i}\n")


with open("sours1.txt", "r", encoding="utf-8") as f:
    with open("copy.txt", "w", encoding="utf-8") as c:
        for line in f:
            c.write(line)

with open("copy.txt", "r", encoding="utf-8") as c:
    print(c.read())


# task 5 не разобралась с выводом

def log_message(path, message):
    with open("app.log", "a", encoding="utf-8") as f:
        f.write(message + "\n")

with open("app.log", "r", encoding="utf-8") as f:
    print(f.read())

log_message("app.log", "Test started")
log_message("app.log",  "Test finished")

# task 6
with open("app.log", "w", encoding="utf-8") as f:
    f.write("text\n\n")
    for i in range(6):
        f.write(f"{i}\n")


def read_first_chars(path, n):
    with open("app.log", "r", encoding="utf-8") as f:
        return f.read(n)


print(read_first_chars("app.log", 7))

# task 7
with open("app.log", "w", encoding="utf-8") as f:
    f.write("line 1 ERROR\n\n")
    f.write("line 2 \n\n")
    f.write("line 3 ERROR \n\n")
    for i in range(6):
        f.write(f"{i}\n")


def filter_file(src, dst, keyword):
    with open(src, "r", encoding="utf-8") as f:
        with open(dst, "w", encoding="utf-8") as c:
            for line in f:
                if keyword in line:
                    c.write(line)

    with open(dst, "r", encoding="utf-8") as c:
        print(c.read())

filter_file("app.log", "errors.log", "ERROR")

# task 8
with open("nums.txt", "w", encoding="utf-8") as f:
    for i in range(8):
        f.write(f"{i}\n")


with open("nums.txt", "r", encoding="utf-8") as f:
    total = 0
    for line in f:
        number = int(line)
        total += number

print(total)

# task 9
def copy_binary(src, dst):
    with open(src, "rb") as f:
        data = f.read()

    with open(dst, "wb") as c:
        c.write(data)


copy_binary("a_2soctoQN7.png", "a_2soctoQN7_copy.png")

# task 10

def read_config(path):
    config = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            key, value = line.split("=")
            config[key] = value

    return config

result = read_config("config.txt")
print(result)
