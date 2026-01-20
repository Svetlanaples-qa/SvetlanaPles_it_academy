# task 1 basic logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Тест стартовал")
logging.error("Произошла ошибка")

#task 2 logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="test_results.log",
    filemode="a"
)

logging.info("Тест стартовал")
logging.error("Произошла ошибка")

# task 3 logging
import logging


logger = logging.getLogger("hw16")
logger.setLevel(logging.DEBUG)

# 1 Handler в файл: DEBUG
file_handler = logging.FileHandler("test_results.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# 2 Handler в консоль: INFO+
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Формат для обоих
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Подключаем хэндлеры
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("Только в файл")
logger.info("В консоль и файл")
logger.warning("WARNING тоже в консоль и файл")


# task 4 URL и expected status
import logging
import requests


logger = logging.getLogger("task 4 logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_results.log", mode="a", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def test_login(url, expected_status=200):
    logger.info(f"Starting test_login: url={url}, expected={expected_status}")

    try:
        r = requests.post(url)

        if r.status_code == expected_status:
            logger.info("PASSED")
        else:
            logger.error(f"FAILED: expected {expected_status}, got {r.status_code}")

    except Exception as e:
        logger.error(f"FAILED: {e}")



test_login("https://api.example.com/users", 200)

# task 5 URL и expected status
import logging
import requests

#задала логгер
logger = logging.getLogger("task 5 logger")
logger.setLevel(logging.DEBUG)
# задала хэндлер
file_handler = logging.FileHandler("test_results.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
#задала формат
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#соединяем
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def test_login_bad():
    url = "http://bad-url"
    logger.info(f"Starting test_login_bad with url={url}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.info("✅ Request succeeded")

    except requests.RequestException:
        logger.exception("❌ HTTP error occurred during test_login")


test_login_bad()


