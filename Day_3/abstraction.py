from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def fuel_type(self):
        pass
    def drive(self):
        return "The vehicle is driving."
    def driving(self):
        return "The vehicle is Silently Moving."
class car(vehicle):
    def start_engine(self):
        return "Car engine started."
    def fuel_type(self):
        return "Car runs on petrol."
class ElectricCar(vehicle):
    def start_engine(self):
        return "Electric car is ready to go."
    def fuel_type(self):
        return "Electric car runs on electricity."
my_car = car()
my_electric_car = ElectricCar() 
print(my_car.start_engine())
print(my_car.fuel_type())
print(my_electric_car.start_engine())
print(my_electric_car.fuel_type())
print(my_car.drive())
print(my_electric_car.driving())
