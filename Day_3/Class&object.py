class Dog:
    Species = "Canis familiaris"
    
    def bark(self):
        return "Woof!"

dog1 = Dog()
dog2 = Dog()
print(dog1.Species) # Output: Canis familiaris
print(dog2.Species)
print(dog1.bark())  # Output: Woof!
dog1.bark()  # Output: Woof!
def __init__(self):
    self.name = "Harsha"
    self.age = 21
    self.courese = "MCA"
    print("My name is", self.name)
    print("My age is", self.age)
    print("My course is", self.courese)