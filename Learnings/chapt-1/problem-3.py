# write a python program to print the contents of a directory using the os module
import os

# Specify the directory (you can change this to any path you want)
directory = input("Enter the path of the directory: ")

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory)
    
    print(f"\nContents of '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
except Exception as e:
    print(f"An error occurred: {e}")
