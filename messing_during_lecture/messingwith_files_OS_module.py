# messingwith_files_OS_module.py
# author: atacan

import os

FILENAME = "messingwith_files.py" # this is the file name that we will be working on

if os.path.exists(FILENAME): # check if the file exists
    with open(FILENAME, 'r') as f: # 'r' is for reading the file
        for line in f: # f is a file object
            print(line.strip()) # strip() is used to remove the newline character at the end of each line / Preferred way of doing it
else:
    print(f"{FILENAME} does not exist") # if the file does not exist, print this message

# os.remove("data2.txt") # this is to remove the file