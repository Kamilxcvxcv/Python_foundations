class Car:
            wheels = 4  # class variable
            # Can have a default unique value

            def __init__(self, make, model, year, color):
                self.make = make  # instance variable
                self.model = model  # in1stance variable
                self.year = year  # instance variable
                self.color = color  # instance variable


# Summary
# Instance variable is declared inside constructor, they can be given unique values
# class variables are declared within a class but outside the constructor
# and you can set a default value for all instances of these class, for all unique
# objects that are created, You can change those values later

