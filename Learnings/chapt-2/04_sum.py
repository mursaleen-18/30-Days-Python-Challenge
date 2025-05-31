a = input ("Enter a number: ")  # input() function takes input in the form of a string
b = input ("Enter another number: ")

# sum = a+b  # This will concatenate the strings
#  print("The sum is:", sum)  # prints the concatenated result, because both a and b are strings

# To perform arithmetic addition, we need to convert the inputs to integers or floats

a = int(a)  # converting string to int 
b = int(b)  # converting string to int
sum = a + b  # Now this will perform arithmetic addition

print("Actual The sum is:", sum)  # prints the arithmetic sum of a and b 
