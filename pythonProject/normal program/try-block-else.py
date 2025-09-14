import os
try:
    os.rename("old file.txt","new file.txt")
    print("change")
except FileNotFoundError:
    print("File is absent")
else:
    print("Not exception error occeer")