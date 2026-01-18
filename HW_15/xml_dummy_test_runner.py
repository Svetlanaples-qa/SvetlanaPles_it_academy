import xml.etree.ElementTree as et


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
            "actual": result
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
      "persentage": persentage
}

root = et.Element("test_report")
# решила оформить каждый элемент по отдельности, может есть более красивый способ
et.SubElement(root, "total").text = str(report["total"])
et.SubElement(root, "passed").text = str(report["passed"])
et.SubElement(root, "failed").text = str(report["failed"])
et.SubElement(root, "persentage").text = str(report["persentage"])

errors_el = et.SubElement(root, "errors")

for err in report["errors"]:
    error_el = et.SubElement(errors_el, "error")

    et.SubElement(error_el, "test_id").text = str(err["test_id"])
    et.SubElement(error_el, "expected").text = str(err["expected"])
    et.SubElement(error_el, "actual").text = str(err["actual"])

tree = et.ElementTree(root)
tree.write("dummy_report.xml", encoding="utf-8", xml_declaration=True)

# мой xml file был не красивый, в одну строку, mindom писала с chatGPT
from xml.dom import minidom

xml_str = et.tostring(root, encoding="utf-8")
parsed = minidom.parseString(xml_str)
pretty_xml = parsed.toprettyxml(indent="  ")

with open("dummy_report.xml", "w", encoding="utf-8") as f:
    f.write(pretty_xml)