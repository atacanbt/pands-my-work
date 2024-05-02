# messingwith_files
# author: atacan

FILENAME = "data.txt" # this is the file name that we will be working on
'''
with open(FILENAME, 'r') as f: # 'r' is for reading the file
    for data in f: # f is a file object
       # print(data, end='') # end='' is used to remove the newline character at the end of each line
        print(data.strip()) # strip() is used to remove the newline character at the end of each line / Preferred way of doing it
       # print(data[:-1]) # this is to remove the last two characters of each line
'''
with open("data2.txt", 'w+') as f: # 'wt' is for writing the file, if the file doesn't exist, it will be created
    # if we change the below message, it will overwrite the existing file, because of the 'w' mode
    # if we want to append the file, we should use 'a' mode
    f.write('Hello, World!\n')
    f.write('How are you?\n')
    f.seek(0) # this is to move the cursor to the beginning of the file
    data = f.read()
    print(data)



print('Data written to file')