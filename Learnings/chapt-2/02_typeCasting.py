# type function and type casting
# type() & type casting
# type() function returns the type of an object
a = 10
print(type(a))  # <class 'int'>

b = 10.5
print(type(b))  # <class 'float'>

c = "Hello"
print(type(c))  # <class 'str'>

# type casting

# converting int to float

d = "31.5"

e = float(d) # converting float to int

f = type(e)
print(f)  # <class 'float'> 

int("10")  # converting string to int
float(31)  # converting int to float