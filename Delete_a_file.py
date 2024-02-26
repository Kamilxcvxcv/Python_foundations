import os
import shutil


path = "Folder_to_delete"
try:
    # os.remove(path)  # removes a file, that path is stored in a variable called path
    # # this function does not remove empty folders
    # os.rmdir(path)  # removes a directory (empty)
    shutil.rmtree(path)  # be careful  this function is considered dangerous because it deletes everything
except FileNotFoundError:
    print("That file was not found")
except OSError:
    print("Folder is not empty, use different module (shutil")
except IsADirectoryError as e:
    print("This is not a file dumbass")
else:
    print(path+" was deleted")
