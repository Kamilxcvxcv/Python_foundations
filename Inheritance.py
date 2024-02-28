# classes can inherit something usually  attributes and methods from another class
# classes can form parent-child relationship where a child will receive everything that the parent class has

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):  # in order to create a child, in () insert name of the parent
    def running(self):  # each of these classes inherit methods from their parent and also can contain unique classes of their own
        print("This rabbit is running!")


class Fish(Animal):
    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


# create object from these classes
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)  # these class will have method alive because of inheritance even if the method isn't declared inside the class
# each child classes inherit everything of their parents
fish.eat()
hawk.sleep()

