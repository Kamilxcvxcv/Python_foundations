import os
# included within standard python library
# this let you cech if some file exists someplace on your computer
path = "/home/Corypheus/Desktop/folder"

if os.path.exists(path): # tell you if that location exists
    print('That location exists')  # if true prints this
    if os.path.isfile(path):  # check if is a file
        print('That is a file')
    elif os.path.isdir(path):  # check if is a directory
        print('That is a directory')

else:
    print('That location doesnt exists')  # if false prints this




