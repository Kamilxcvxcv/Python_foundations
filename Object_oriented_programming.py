
# What are object in OOP? Object is an instance of a class, by using programming we can create representations of real life objects
# It can mimic real world objects by assigning a combination of attributes = is/has ex. name,age, height
# and methods = actions ex. eat, sleep, make
# class works as a blueprint to create objects, we can assign attributes what describe an object is or has and methods what each object can do
# class Car:  # names of the classes should be capital
#     pass
# if you have a small program it may be better to write your class within your main module
# if the class is fairly large you may consider to create a separate module for you class

# to import class
from Car import Car  # name of the file, and then name of the class


# to create and object

car_1 = Car("Chevy","Corvette","2021","Blue")  # in order to make a car object we need to pass set of arguments
# you can use a class as a blueprint to create other cars
car_2 = Car("Ford","Mustang","2022","Red")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_1.stop()