class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        return f"{self.name} is eating."

    def speak(self):
        return f"{self.name} says: Make some noise!"
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

    def speak(self):
        return f"{self.name} barks: Woof!"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name) 
        self.color = color

    def speak(self):
        return f"{self.name} meows: Meow!"
    
dog = Dog("Tommy", "Golden Retriever")
cat = Cat("Whitey", "Tabby")

print(dog.eat())  
print(dog.speak())  
print(cat.eat())  
print(cat.speak())  
