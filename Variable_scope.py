# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = 'Rher'  # global scope (available inside & outside function)
def display_name():  # if local version of variable is not present it will take the global version
    name = 'Code'  # this variable has a local scope (local scope) because it is created inside a function
    print(name)  # outside of this function you cannot access the function

display_name()  # calls display_name function
print(name)
