# task 1.1 json
#import json

#results = {'test_suite': 'api_tests' , 'total': 10,'passed': 8,
#'failed': 2
#}

#with open('test_results.json', 'w', encoding='utf-8') as f:
#    json.dump(results, f, indent=2, ensure_ascii=False)

# task 1.2 json
#import json

#results = [{'id': 1 , 'name': 'Sasha', 'role': "admin"}]

#with open('user.json', 'w', encoding='utf-8') as f:
#    json.dump(results, f, indent=2, ensure_ascii=False)

# task 1.3 json
#import json


#with open('test_results.json', 'r', encoding='utf-8') as f:
#    new = json.load(f)
#    perc = 100 * new["passed"] / new["total"]
#    print(perc)

# task 1.4 json
#import json


#with open('user.json', 'r', encoding='utf-8') as f:
#    users = json.load(f)

#users.append({"id": 2, "name": "Svetlana", "role": "user"})

#with open('user.json', "w", encoding="utf") as f:
#    json.dump(users, f, indent=2, ensure_ascii=False)

#task 2.1  yaml
#import yaml

#results = {
#    "test_suite": "api_tests",
#    "total": 10,
#    "passed": 8,
#    "failed": 2
#}

#with open("test_results.yaml", 'w', encoding="utf") as f:
#    yaml.safe_dump(results, f, default_flow_style=False, sort_keys=False )

#task 2.2  yaml
#import yaml

#users = [{'id': 1 , 'name': 'Sasha', 'role': "admin"}]

#with open('user.yaml', 'w', encoding='utf-8') as f:
#    yaml.safe_dump(users, f, default_flow_style=False, sort_keys=False )

#task 2.3 yaml
#import yaml


#with open('test_results.yaml', 'r', encoding='utf-8') as f:
#    new = yaml.safe_load(f)
#    perc = 100 * new["passed"] / new["total"]
#    print(perc)


#task 2.4 yaml

#import yaml


#with open('user.yaml', 'r', encoding='utf-8') as f:
#    users = yaml.safe_load(f)

#users.append({"id": 2, "name": "Svetlana", "role": "user"})

#with open('user.yaml', "w", encoding="utf") as f:
#    yaml.safe_dump(users, f, default_flow_style=False, sort_keys=False )


# task 3.1 xml

#import xml.etree.ElementTree as ET

#tree = ET.parse("employees.xml")
#root = tree.getroot()

#total_employees = 0
#total_salary = 0

#for employee in root.findall("employee"):
#    total_employees += 1
#    salary = int(employee.find("salary").text)
#    total_salary += salary

#print("Employees:", total_employees)
#print("Total salary:", total_salary)

# task 3.2








