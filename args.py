# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments

# def add(num1,num2):  # function add accepts two numbers as arguments
#     sum = num1 + num2  # adds them together
#     return sum  # and return the sum

# print(add(1,2))  # gives two arguments to the sum and prints it
# if you would like to add 3 arguments you couldn't do that because it accepts only two
# that's where you can use args, it'll replace all arguments with args

def add(*args):  # args is short for arguments, in short we are packing all the arguments as tuple
    sum = 0  # sums equals 0
    args = list(args)  # tuples doesn't support item assignments so if you want to change something cast it into a list
    args[0] = 0  # change the item with index 0 to 0
    for i in args:  # we iterate the sum through the tuple because tuples are iterable
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8))
