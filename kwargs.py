# **kwargs =    parameter that will pack all arguments into a dictionary
#               useful so that a function can accept a varying amount of keyword arguments

# def hello(first, last):  # function that accepts two keyword arguments
#     print('Hello '+first+' '+last)
#
# hello(first='Rher',last='Rurowski')  # you can only pass two arguments because function accepts only 2
# what if someone has 3 thats what for you would use kwargs parameter, so will function accept varying amount of keyword

# def hello(**kwargs):
#     print('Hello ' + kwargs['first'] + ' '+ kwargs['middle'] +' ' + kwargs['last'] )  # in order to access a value
#     # within a dictionary type the name of it [] and list of the key
#
#
# hello(first='rher',middle='ruror',last='rurowski')

# how to do this but let's say we would like to display somebody's full name on the amount of keywords arguments that
# they pass into this function

def hello(**kwargs):
    print('Hello', end=" ")  # now we need to iterate each key value pair within this dictionary
    for key,value in kwargs.items():  # iterates through each key value pair
        print(value, end=" ")  # prints only the value and end makes it printed in one line with spaces

hello(title='Mr.',first='rher',middle='ruror',last='rurowski')



