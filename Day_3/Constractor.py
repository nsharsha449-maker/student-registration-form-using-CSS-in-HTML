class Student:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.courese = course
    def display_info(self):
        
        print("My name is", self.name)
        print("My age is", self.age)
        print("I am pursuing", self.courese)
s1 = Student("Harsha", 21, "MCA")
s2 = Student("Jayanth", 22, "MCA")
s1.display_info()
s2.display_info()