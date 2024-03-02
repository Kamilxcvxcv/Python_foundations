# walrus operator :=


# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

print(happy := True)  # you can assign a value to a variable and use it
# as a part of larger expression


# more practical example
# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# this program ask you for food and puts it in a list
# by using walrus operator you can do it more practically

foods = list()
while food := input("what food do you like?: ") != "quit":
    foods.append(food)



