# functions = a block of code which is executed only when it is called.

def hello(first_name, last_name, age):  # in order to function being able to receive information it needs
    print('Hello! ' + first_name + ' ' + last_name)  # a matching set of parameters
    print('You are '+str(age)+' years old!') # remember about casting integer to string
    print('Have a  nice day!')


hello("Rher", "Rurowski", 23)  # you can send 3 values
# my_name = 'rher'   # !! they do not need to be the same
#
# hello(my_name)

# hello('Rher') # you can sent information to your function, they are called arguments
# in short function hello receives an information of string, we give it a temporary nickname of name, and
# then we can use this value for whatever we want within our function
# you can also send variables
