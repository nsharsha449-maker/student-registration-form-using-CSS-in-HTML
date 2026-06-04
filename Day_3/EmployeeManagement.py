class Employee:
    
    def __init__(self, emp_id, name, department, salary):   # Constructor
        self.__emp_id     = emp_id        # Encapsulation (name mangling)
        self.__name       = name
        self.__department = department
        self.__salary     = salary

    # Getters & Setters (Encapsulation)
    def get_emp_id(self):     
        return self.__emp_id
    def get_name(self):      
        return self.__name
    def get_department(self): 
        return self.__department
    def get_salary(self):      
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    # Method — overridden in subclasses (Polymorphism)
    def display_info(self):
        print(f"  Emp ID     : {self.__emp_id}")
        print(f"  Name       : {self.__name}")
        print(f"  Department : {self.__department}")
        print(f"  Salary     : Rs.{self.__salary}")

    def calculate_bonus(self):
        return self.__salary * 0.10       # 10% default bonus


# ════════════════════════════════════════════
# SUBCLASS 1 — Inheritance (Manager)
# ════════════════════════════════════════════
class Manager(Employee):                  # Inheritance

    def __init__(self, emp_id, name, dept, salary, team_size):
        super().__init__(emp_id, name, dept, salary)  # calls Employee constructor
        self.__team_size = team_size

    def get_team_size(self): 
        return self.__team_size

    # Polymorphism — Method Overriding
    def display_info(self):
        super().display_info()
        print(f"  Team Size  : {self.__team_size}")
        print(f"  Role       : Manager")

    def calculate_bonus(self):
        return self.get_salary() * 0.20 + self.__team_size * 5000


# ════════════════════════════════════════════
# SUBCLASS 2 — Inheritance (Developer)
# ════════════════════════════════════════════
class Developer(Employee):                # Inheritance

    def __init__(self, emp_id, name, dept, salary, tech_stack):
        super().__init__(emp_id, name, dept, salary)
        self.__tech_stack = tech_stack

    def get_tech_stack(self): 
        return self.__tech_stack

    # Polymorphism — Method Overriding
    def display_info(self):
        super().display_info()
        print(f"  Tech Stack : {self.__tech_stack}")
        print(f"  Role       : Developer")

    def calculate_bonus(self):
        return self.get_salary() * 0.15   # 15% for developers


# ════════════════════════════════════════════
# MAIN — Polymorphism Demo
# ════════════════════════════════════════════
if __name__ == "__main__":

    # Parent reference holds child objects (Polymorphism)
    employees = [
        Manager(101, "Anusha", "Operations", 77000, 6),
        Developer(102, "Thejas", "Engineering", 78000, "Python"),
        Employee(103, "Pavan", "HR", 56000),
    ]

    for emp in employees:
        print("==========================================")
        emp.display_info()                # Runtime Polymorphism
        print(f"  Bonus      : Rs.{emp.calculate_bonus():.2f}")
        print()