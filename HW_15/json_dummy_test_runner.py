import json

def dummy_test(data):
    if data <= 5:
        return True
    else:
        return False

tests = [
(dummy_test(5), True),
(dummy_test(7), True),
(dummy_test(6), False),
(dummy_test(2), True),
(dummy_test(4), False),
(dummy_test(8), True),
(dummy_test(1), False),
]

total = len(tests)
passed = 0
failed = 0
errors = []
index = 0


for result, expected in tests:
    try:
        assert result == expected
    except AssertionError as e:
        print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
              f"но фактический результат {result}")
        failed += 1
        errors.append({
            "test_id": index + 1,
            "expected": expected,
            "actusl": result
        })
        index += 1
        continue

    print("Тест прошёл!")
    passed += 1
    index += 1

persentage = round(passed / total * 100, 1)

report = {
      "total": total,
      "passed": passed,
      "failed": failed,
      "errors": errors,
      "presentage": persentage
}

with open("dummy_test_runner.json", 'w', encoding="utf") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)
