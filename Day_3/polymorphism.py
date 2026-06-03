class Duck:
    def sound(self):
        return "Quack!"
class person:
    def sound(self):
        return "Hello!"
class dog:
    def sound(self):
        return "Woof!"
class cat:
    def sound(self):
        return "Meow!"
def make_sound(obj):
    print(obj.sound())
make_sound(Duck())
make_sound(person())
make_sound(dog())
make_sound(cat())
print(len("Hello"))
print(len([1,2,3]))
print(3+5)
print("A" + "B")