# Lists = used to store multiple items in a single variable

food = ["pizza", "Hamburbur", "Hotdog", "Spaghetti"]  # each item of list is referred as element
# if you want to print certain element of the list you need to implement [] and number of the element
# REMEMBER that computer starts counting from 0


# # important feature with lists is that you can always update and change the elements within a list
# food[1] = "sushi"  # it changed 1 element from Hamburbur to sushi
# print(food[1])

# useful functions with lists
# food.append("ice cream")  # adds an element
# food.remove("Hotdog") # removes an element
# food.pop()  # removes the last element
# food.insert(0,"cake") # adds element on certain index
# food.sort()  # sorts the list alphabetically
# food.clear() # removes all elements

# if you want to display all the element found within a list you can do it with standard for loop
for x in food:
    print(x)





