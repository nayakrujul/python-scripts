print("")
print("Welcome to RN Delete File")
print("")
import os
filename = raw_input("Please enter the filename. ")
print("")
if(os.path.isfile(filename)):
    os.remove(filename)
    print("File '" + filename + "' cleared.")
else:
    print("File '" + filename + "' not found.")
print("")