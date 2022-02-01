#The OS module in Python provides functions for
# interacting with the operating system.
import os
#to  know the cwd
print(os.getcwd())
# to get the list of all the files in cwd
print(os.listdir())
#to rename a file
#os.rename('enumerate.py','go.py')
#to check in a directory
print(os.path.exists('de22.py'))
#to get the size of the file
print(os.path.getsize('hello.txt'))
