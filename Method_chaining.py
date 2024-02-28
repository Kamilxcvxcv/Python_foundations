# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()
# example, I would like my car object to use its turn on method immediately followed by a drive method
# car.turn_on()
# car.drive()  # this will print two lines of code
# with using method chaining
# ! important to remember is that when you use method chaining you need to return self because otherwise it won't work
car.turn_on().drive()
car.brake().turn_off()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()  # when you are using a lot of method chaining hit enter after every method, it'll be more readable
