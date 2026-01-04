import time
import functools

# task 1
def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            attempt = 0
            while attempt < times:
                attempt += 1
                result = func(*args)
                if result == "FAILURE":
                    print(f"Not successful! Attempt number: {attempt}")
                else:
                    return result
            print("No more attempt")
            return result
        return wrapper
    return decorator


@retry(times=1)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
    return "PASSED"

print(flaky_test())



# task 2

def require_role(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            current_role = args[0]
            if current_role != required_role:
                print(f"Ошибка: Требуется роль {required_role}, текущая: {current_role}")
                return  None
            return func(*args)
        return wrapper
    return decorator

user_one = 'user'
user_two = 'admin'

@require_role("admin")
def admin_test(*args):
    print("Выполняется админский тест")
    return "Success"

#print(admin_test(user_two))
print(admin_test(user_one))



# task 3

def timer(func):
    @functools.wraps(func)
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        exec_time = end - start
        print(f"{func.__name__} выполнился за {exec_time} сек.")
        return result
    return wrapper


@timer
def slow_test():
    time.sleep(1)
    return "OK"

print(slow_test())



# task 4

def wait_with_retry_until(timeout=10, interval=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(**kwargs):
            attempt = 1
            while True:
                result = func(**kwargs)
                if result:
                    print(f"Попытка {attempt}: успешно \n Элемент найден")
                    return "Элемент найден"

                else:
                    print(f"Попытка {attempt}: неуспешно")
                    attempt += 1
                time.sleep(interval)
        return wrapper
    return decorator


@wait_with_retry_until(timeout=7, interval=0.5)
def element_visible():
    return time.time() % 3 > 2


element_visible()

# task 5 Не получилось сделать сделать рабочий cache

def cache_results(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@cache_results
def expensive_calculation(n):
    print(f"Вычисляем для {n}")
    time.sleep(1)
    return n * n

#print(expensive_calculation(5))
print(expensive_calculation(5))
#print(expensive_calculation(5))
#print(expensive_calculation(6))
#print(expensive_calculation(6))
#print(expensive_calculation(5))

#task 5.1

def count_exec_time(func):
    @functools.wraps(func)
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        execution_time = time.time() - start
        print(f"Время выполнения: {execution_time} сек.")
        return result
    return wrapper

def cache_results(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Быстро возвращаем из кэша {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_results
@count_exec_time
def expensive_calculation(n):
    print(f"Вычисляем expensive_calculation с аргументом {n}")
    time.sleep(2)
    return n * n

#print(expensive_calculation(5))
#print(expensive_calculation(6))
#print(expensive_calculation(5))
#print(expensive_calculation(6))
print(expensive_calculation(6))
#print(expensive_calculation(5))
