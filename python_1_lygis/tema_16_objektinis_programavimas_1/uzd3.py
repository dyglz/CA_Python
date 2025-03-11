# Nauji darbuotojai

class Employee:
    def __init__(self, first_name: str, last_name: str):
        self.fullname = f"{first_name} {last_name}"
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"

employee_1 = Employee(first_name="John", last_name="Doe")
employee_2 = Employee(first_name="David", last_name="Coen")

print(f"Full name: {employee_1.fullname}")
print(f"Email: {employee_1.email}")
print(f"Full name: {employee_2.fullname}")
print(f"Email: {employee_2.email}")

