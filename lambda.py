# lambda functions = function written in 1 line using lambda keyword
#                    accepts any number of arguments, but only has one expression
#                    (think of it as a shortcut)
#                    (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression


# def double(x):
#     return x * 2
#
#
# print(double(5))


# let's write these function as lambda function
double = lambda x:x * 2  # lambda <parameter>:<expression>
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False
print(double(5))
print(multiply(2,5))
print(add(1,2,3))
print(full_name("Rher","Rurowski"))
print(age_check(18))