# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "rher rurowski!"

# if(name[0].islower()):  # check if first letter in the name is capitalize
#     name = name.capitalize()  # if the letter is not capitalize it capitalize it

first_name = name[:4].upper()  # creates a substring from name string, and capitalize it
last_name = name[5:].lower()  # creates a substring from name string, and  lower it
last_character = name[-1]  # get access to last character of integer


print(first_name)
print(last_name)
print(last_character)






