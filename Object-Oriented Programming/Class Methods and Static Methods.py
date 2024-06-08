class Employee:
    num_employees = 0

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        Employee.num_employees += 1

    @classmethod
    def get_num_employees(cls):
        return cls.num_employees

    @staticmethod
    def validate_employee_id(employee_id):
        return employee_id.isdigit()
          
# Example usage
emp1 = Employee('122', 'Janu')
emp1 = Employee('134', 'Raju')
print("Number of Employees:", Employee.get_num_employees())  
# Output: Number of Employees: 2

print("is Valid Id :", Employee.validate_employee_id('ABC'))  # Output : is Valid Id : False
print("is Valid Id :", Employee.validate_employee_id('156'))  # Output : is Valid Id : True