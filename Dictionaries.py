# dictionaries =    a changeable, unordered collection of unique key:value pairs
#                   Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

# dictionaries are changeable and mutable after the program is running
capitals.update({'Germany':'Berlin'})  # append new key:value pair
capitals.update({'USA':'Las Vegas'})  # updates key of USA
capitals.pop('China')  # removes the china key
capitals.clear()  # removes everything
# methods
# print(capitals['Russia'])  # prints value that is associated with key of Russia
# it is not a safe way to access dictionary because when you enter key that doesn't exist the program will crash
# much safer way is to check is the certain key is there or not
# print(capitals.get('Germany'))  # return is none because Germany key is not there (it's a safe way)
# print(capitals.keys())  # Method to print only the keys
# print(capitals.values())  # method to print only the values
# print(capitals.items())  # method to print everything

# other way to display all the value of dictionaries is to use for loop

for key,value in capitals.items(): # iterates for each key:value pair
    print(key,value)  # prints every value


