""""
class women:

    def __init__(self,age,cm,kg):
        self.age = age
        self.cm = cm
        self.kg = kg

    def get_info(self):
        return f"{self.age},{self.cm},{self.kg}"


women1 = women(18,155,45)

print(women1.get_info())

women2 = women(19,158,56)
print(women2.get_info())
"""

class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_deparment):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_deparment = emp_deparment



    def cal_emp_salary(self,hours):
        if hours > 50:
            ot = hours-50
            self.emp_salary = self.emp_salary + (ot * (self.emp_salary/50))
        print(f"total salary: {self.emp_salary}")
        return self.emp_salary

    def emp_assign_deparment(self,new_deparment):
        self.deparment = new_deparment

    def emp_details(self):
        print(f"employee id:{self.emp_id}")
        print(f"name:{self.emp_name}")
        print(f"salary:{self.emp_salary}")
        print(f"deparment:{self.emp_deparment}")

emp1 = Employee("ak47","humyai",23000,"hr")

print("Initial Details:")

emp1.emp_details()
print("-" * 20)

emp1.cal_emp_salary(70)

emp1.emp_assign_deparment("it")

print("Updated Details:")
emp1.emp_details()
