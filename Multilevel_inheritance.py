# multi-level inheritance = when a derived (child) class inherits another derived (child) class
# think of it as a family tree
class Organism:  # grand-parent

    alive = True


class Animal(Organism):  # parent

    def eat(self):
        print("This animal is eating")


class Dog(Animal):   # child

    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
