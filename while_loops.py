#  while loop = a statement that will execute it's block of code, as long as it's condition remains true
# used to prompt user for an input and this input is needed to be added in order to continue
# while 1==1:
#     print("help! I'm stuck in a loop!")  # that's an infinite loop, normally you want a way to escape a loop
# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
# # You're stuck in this loop as long as you enter your name
# print("Hello "+name)

name = None

while not name:
    name = input("Enter your name: ")
print("Hello "+name)