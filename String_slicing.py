# Slicing = create a substring by extracting elements from another string
#                       indexing[] or slice()
#                       [start:stop:step]   #arguments of slicing (index)
#  indexing []
# name = "Rher rurowski"  # Let's slice this string, so it only prints your name
#               Blank at the start means first letter
# first_name = name[:4]  # Remember that computers starts counting from 0, stopping index in exclusive
# last_name = name[5:]  # blank at the end means the last letter
# funky_name = name[::2]  # step index means it will only count every second character(by default is 1)
# reversed_name = name[::-1]  # prints whole string in reversed order


# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)


# Slice()
website1 = "https://www.google.pl/"   # lets exclude http and .pl portion
website2 = "https://www.wikipedia.pl/"
# negative index means that slicing will start from left
slice = slice(12,-4)  # slicing object, servers as the information on the way of slicing

print(website1[slice])  # to apply slice object type name of the string, index operator and place slicing object
print(website2[slice])  # you can reuse the slice object
