# copyfile() = copies contents of a file
# copy() =     copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('text.txt','copy.txt')  # src  and destination
# it copied the file and changed it name to copy.txt
# same arguments for copy and copy2

