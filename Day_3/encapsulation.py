class employee:
    def __init__(self,name ,salary):
        self.name = name
        self.__salary = salary  # Private variable
        self._dept = "IT"  # Protected variable
    def get_salary(self):
        return self.__salary
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")
emp = employee("Harsha", 50000)
print(emp.name)  # Output: Harsha
print(emp.get_salary())  # Output: 50000
emp.set_salary(55000)
emp.set_salary(-1000)  # Output: Invalid salary amount
