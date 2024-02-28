# method overriding is  the ability of an object-oriented programming language to allow a subclass also known as child
# to provide a more specific implementation of a method that is already provided by one of its parents

class Animal:  # parent

    def eat(self):  # eat(self) is a method signature
        print("This animal is eating")


class Rabbit(Animal):  # child

    def eat(self):
        print("This rabbit is eating a carrot")  # when executed this method will be used instead of inherited method from parent
# an object will use a method that is more closely associated with itself first before relying on  a method that it may inherit
# from a parent class


rabbit = Rabbit()
rabbit.eat()