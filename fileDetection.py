#  python file detection 

import os    # very import to add


# file_path ="test.txt"                     # relative file path        # dont forget .extensionnnn

# file_path = "try/test.txt"                   # relative file in folder  # dont forget .extensionnnn

#file_path = "C:/Users/hp/OneDrive/Desktop/test1.txt"     # absolute file  # dont forget .extensionnnn

file_path = "C:/Users/hp/OneDrive/Desktop/dbms"     # absolute file in folder  # dont forget .extensionnnn

# check for is file or is folder by meothod

if os.path.exists(file_path):
    print("file exist")
    if os.path.isfile(file_path):
        print('is a file')
    elif os.path.isdir(file_path):
        print("is a directory ")
else :
    print('File does not exist')
