# Logical operators (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

# if temp >= 0 and temp <= 30: # in order to this condition to be true, BOTH of them MUST be true
#     print("the temperature is good today!")
#     print("Go outside!!!")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad today!") # with or logical operator as long one is true whole condition is true
#     print("Stay inside!!")

# if Condition is true not operator will flip it to false, same with false.
if not (temp >= 0 and temp <= 30):  # used to ONE or more conditional
    print("The temperature is bad today!")
    print("Stay inside!!")
elif not (temp < 0 or temp > 30):
    print("the temperature is good today!")
    print("Go outside!!!")




