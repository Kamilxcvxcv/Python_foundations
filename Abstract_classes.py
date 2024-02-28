# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have implementation
# abstract classes prevent a user from creating an object of that class
# additional feature is that they compel a user to override any abstract method within a child class, a method that is abstract
# has a declaration but does not have an implementation
# think of it as a template
from abc import ABC, abstractmethod  # ABC is abstract based class


class Vehicle(ABC):  # we want to prevent user from creating object form vehicle class because it is to generic
    # we want user to create object from a child class
    @abstractmethod  # now the vehicle class is abstract and we cannot give it aa physical form
    def go(self):  # go method is empty
        pass
    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):  # we write our own implementation of go method
        print("You drive the car")

    def stop(self):
        print("This car is stopped!")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped!")



# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()


car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

# in order to create car and motorcycle class we need to override the go method that they inherit from its parent class of vehicle
# and provide its own implementation

