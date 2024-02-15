# tuple =       collection which is ordered and unchangeable
#               used to group together related data, works similar to lists

student = ("rher",23,"male")
# methods with tuples
print(student.count("rher"))  # how many times the value appears
print(student.index("male"))  # finds an index of a certain value (index of value male is at 2)
# you can display all of the contents within a tuple using a for loop
for x in student: # iterates through all the values found within our tuple of student
    print(x)
# check is a certain value exists within our tuple using an if statement
if "rher" in student:
    print("rher is here")

