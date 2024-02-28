class Car:

    # important thing is that we need a special method that will create object for us (constructor?)
    # init is a special method, we can pass in some arguments and assign these arguments to each object attributes and then we can reuse this class
    # is reusable
    def __init__(self, make, model, year, color):  # in theory to this work you would need to pass 5 arguments but python pass self argument automatically
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):  # defines a method, self refers to the object that is using this method
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
