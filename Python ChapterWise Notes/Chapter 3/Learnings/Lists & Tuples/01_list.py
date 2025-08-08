# A list contains items separated by commas and enclosed within square brackets [].lists are almost similar to arrays
# in C. One difference is that all the items belonging to a list can be of different data type.


Friends = ["apple", "orange", 5, 10.5, True, "magnetic"]

print(Friends)  # Output: ['apple', 'orange', 5, 10.5, True, 'magnetic']

# Lists are mutable, unlike strings.

Friends[0] = "banana"
print(Friends)  # Output: ['banana', 'orange', 5, 10.5, True, 'magnetic']

# Common operations on lists

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")      # Add at the end
fruits.insert(1, "mango")    # Insert at index
fruits.remove("banana")      # Remove by value
fruits.pop()                 # Remove last item
fruits[0] = "kiwi"           # Modify element

# accessing elements
print(fruits[0])     # First element
print(fruits[-1])    # Last element

# Looping through.
print("looping fruits")
for fruit in fruits:
    print(fruit)

print(fruits)
print(fruits.remove("kiwi")) 
print(fruits)