
text = "Appended text \nappended text\nappended text\n"  # if run again it will overwrite whole file in w mode

with open('test2.txt','a') as file:  # second argument is by default r for read, w is write
    file.write(text)  # indicates what to write in the file
# if you want to append to the file change the mode to a for append

