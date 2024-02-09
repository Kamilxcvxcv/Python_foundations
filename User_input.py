name = input("What is your name?: ")  # this function asks user for input and stores it in a variable called name
# age = input("How old are you?: ")  # you cannot do math with these input because it is a string
age = int(input("How old are you?: "))  # in order to use math, you need to typecast the input into int or float
height = float(input("How tall are you?: "))  # Height is often measured with decimals so typecast it into a float

print("Hello "+name)
print("Your are "+str(age)+" years old")  # you cannot display strings with integer, typecast into a string
print("Your height is "+str(height)+" cm tall")  # again cannot display strings with float, typecast into a string



