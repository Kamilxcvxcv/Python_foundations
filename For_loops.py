import time


#  for loop =        a statement that will execute it's block of code a limited amount of times
#                    while loop = unlimited
#                    for loop = limited
# for i in range (10):  # i is short for index (remember that computers count from 0)
#     print(i+1)

# for i in range(50,100+1): # starting point is inclusive and last is exclusive
#     print(i)  # will print all number from 50 to 100


# for i in range(50,100+1,2):
#     print(i) # this will count up numbers by two
# # you can add a third number that counts as a step, how much you want to count up or down by
#
# for i in "Bro Code":
#     print(i) #  this will print every letter in the string

# countdown program

for seconds in range(10,0,-1):  # we are setting the range so it starts at then end at 0 and counts down
    print(seconds)
    time.sleep(1) # prints every second
print("Happy new year!")
