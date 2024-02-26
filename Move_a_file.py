import os

source = "folder_to_move"  # source of the file
destination = "/home/Corypheus/Desktop/folder_is_moved"  # destination of the file

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)  # takes files from the source and moves it into a destination
        print(source+" was moved")
except FileNotFoundError:
    print(source+"Was not found!")




