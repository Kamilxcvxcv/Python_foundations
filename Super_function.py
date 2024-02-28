# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

# used to reduce lines of code, so you do not need to define lenght and width two times in square and rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length   # because you wrote this code in parent you no longer need it in children
        self.width = width  # use super function to access

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)  # ask to access the init method in parent class

    def area(self):
        return self.length*self.width
class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width*self.height


square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())

# Conclusion
# Super function is used to give access to the methods of a parent class it return a temporary object of a parent class when used
# in order to access the methods of the parent class also known as super class and in this example within init methods of both square
# and cube we immediately called the init method of the parent class to pass in some arguments that both of these classes have in common




