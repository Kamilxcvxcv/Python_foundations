# multiple inheritance = when a child is derived (pochodny) from more than one parent class
# in this example we want to either inherit only one of these or both of them depending on example
class Prey:
    def flee(self):
        print("this animal flees")


class Predator:

    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()

