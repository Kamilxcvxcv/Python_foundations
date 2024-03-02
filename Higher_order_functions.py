# Higher order Functions = a function that either
#                          1. accepts a function as an argument or
#                          2. returns a function
#                           (In python, functions are also treated as objects)

# def loud(text):
#     return text.upper()
#
#
# def quiet(text):
#     return text.lower()
#
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(loud)
# hello(quiet)

# second part

def divisor(x):  # divisor is a higher order function because it returns dividend
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))

# in short what happened program starts at divide we are passing to divisor
# 2 that means x equals 2. it will stay that way until we finish this program
# or until we reassign x. X equals 2. We're skipping divided function because
# we did not call it yet. we are returning dividend and assigning it to a variable
# we can call a variable if it has the memory address of a function
# we are calling a dividend and passing in 10 so y equals 10 and x still equals 2
# we are returning 10 divided by 2 and returning it to console


