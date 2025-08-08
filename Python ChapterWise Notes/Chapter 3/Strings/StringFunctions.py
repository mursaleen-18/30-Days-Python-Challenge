# Strings are immutable, meaning they cannot be changed after creation.

name = "magnetic"
print(len(name)) # Output: 8, length of the string

print(name.endswith("tic"))  # Output: True, checks if string ends with 'tic'

print(name.startswith("Mag"))  # Output: True, checks if string starts with 'Mag'

Caps = name.upper()  # Converts to uppercase
print(Caps)  # Output: MAGNETIC
Lower = name.lower()  # Converts to lowercase
print(Lower)  # Output: magnetic

print(name.capitalize())  # Capitalizes the first letter, Output: Magnetic