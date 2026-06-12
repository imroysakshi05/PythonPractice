employees = [
    {"name": "Sakshi", "salary": 900000},
    {"name": "Rahul", "salary": 400000},
    {"name": "Priya", "salary": 700000}
]

employee_names = [employee["name"] for employee in employees]

high_salary_employees = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 500000
]

print(employee_names)
print(high_salary_employees)
