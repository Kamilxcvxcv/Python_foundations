# str.format() =    optional method that gives users
#                   more control when displaying output


# animal = "cow"
# item = "moon"

# print("The "+animal+" jumped over the "+item)
# there is a more elegant way of previous code
# {} are the placeholders, knows as format fields. First one will insert in first location and so on.
# print("The {} jumped over the {}".format('cow','moon')) # you cannot use them alternately
# print("The {} jumped over the {}".format(animal,item))  # you can also replace previous one with names of variables
# additional way of inserting values to a given placeholder would be to use positional argument
# print("The {1} jumped over the {0}".format('cow','moon'))  # you need to insert index of a value
# last way of inserting values at a given format field would be keyword argument
# print("The {animal} jumped over the {animal}".format(animal='cow', item='moon'))  # keyword argument
# keyword argument could be reused, as well as positional argument
# but there is even more elegant way of previous code

# text = 'The {} jumped over the {}'
# print(text.format(animal,item))

# how to add some padding to a string when we display it using string format method
name = "Rher"

# print('Hello, my name is {}'.format(name)) # you can add some name before, after a name or even to the left or right
# print('Hello, my name is {:10}. Nice to meet you'.format(name))  # add some padding to the right hand side of my name
# print('Hello, my name is {:>10}. Nice to meet you'.format(name))  # Right align your name
# print('Hello, my name is {:<10}. Nice to meet you'.format(name))  # Left align your name (default)
# print('Hello, my name is {:^10}. Nice to meet you'.format(name))  # Center your name
# What if we need to add a positional argument or keyword argument to our format field
# just precede the colon in your format with your keyword/positional argument
# print('Hello, my name is {name:10}. Nice to meet you'.format(name))
# How can we format some numbers
# number = 3.14159  # let's say i want to display only first two digits after the decimal
#
# # print('The number pi is {}'.format(number))  # prints the whole number
# print('The number pi is {:.2f}'.format(number))  # prints first two digits after the decimal
# # f is for floating point numbers

number = 1000

print('The number is {:,}'.format(number))  # adds a coma to all 1000s places
print('The number is {:b}'.format(number))  # displays number as binary
print('The number is {:o}'.format(number))  # displays number as octal
print('The number is {:x}'.format(number))  # displays number as hexadecimal (X for all uppercase)
print('The number is {:e}'.format(number))  # displays in scientific notations (E for all uppercase)
