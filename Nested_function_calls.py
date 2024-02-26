# nested functions calls =  functions calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

# # the harder way without nested function calls
# num = input('Enter a whole positive number: ')  # asks user for a whole positive number
# num = float(num)  # convert number to a float because at first it'll be a string
# num = abs(num)  # Finds absolute value of num
# num = round(num)  # # Rounds the value of num
# print(num) # prints value of num

print(round(abs(float(input('Enter a whole positive number: ')))))  # first function accepts some user input
# then it is casted as float, then  finds absolute value, then rounds the value and then prints it
# and all of this in one line of code

