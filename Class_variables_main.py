from Class_variables import Car

car_1 = Car("Chevy","Corvette","2021","blue")
car_2 = Car("Ford","Mustang","2022","red")


car_1.wheels = 2  # affects only car 1

Car.wheels = 2  # affects all instances of our class


print(car_1.wheels)
print(car_2.wheels)


print(Car.wheels)  # also gets access to variable






