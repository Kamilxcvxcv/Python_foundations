# How to read contents of a file
try:
    with open('text.txt') as file:  # within brackets you need path to a file
        print(file.read())  # open after printing this file will automatically close it
    # if you do a typo in a path of a file, you can prevent it by using exception method
    print(file.closed) # checks if file is closed
except FileNotFoundError as e:
    print("Wrong file dumbass")
    print(e)


