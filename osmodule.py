import os
#to know current working directory
print(os.getcwd())
# Get the list of all files and directories
# in the root directory
print(os.listdir())
# A file old.txt can be renamed to new.txt, using the function os.rename()
os.rename('main.py','notmain.py')
#to check whether a file exists or not by passing the name of the file as a parameter
print(os.path.exists('hello.txt'))
#to get the size of the file
print(os.path.getsize('notmain.py'))