def square(num: int) -> int:
    return num * num


def is_adult(age: int) -> bool:
    return age >= 18


def employee_info(name: str, salary: int = 500000):
    print(f"Name: {name}")
    print(f"Salary: {salary}")


print(square(5))
print(is_adult(23))
employee_info("Sakshi")
