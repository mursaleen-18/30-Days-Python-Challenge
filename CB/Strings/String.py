# Strings are used to strore text data.
text = "Hello, World!"  # String with double quotes
text2 = 'Hello, World!'  # String with single quotes
text3 = """Hello, World!"""  # String with triple quotes
text4 = '''Hello, World!'''  # String with triple single quotes
print(text)
print(text2)
print(text3)
print(text4)

# text[0] = "t"  # This will raise an error because strings are immutable


title = 'Ice Cream'

print(title[4:9])  # This will print 'Cream'. from index 4 to 8 (9 is not included)
print(title[4:])  # This will print 'Cream'. from index 4 to the end
print(title[:4])  # This will print 'Ice '. from the start to index 3 (4 is not included)
print(title[-1])  # This will print 'm'. last character


address = '''123 mani street
New York, NY 10001'''
print(address)

# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"  # Concatenating strings
print(full_greeting)  # This will print 'Hello, Alice!'

# concatinate string with number
age = 30
full_greeting_with_age = full_greeting + " You are " + str(age) + " years old."
print(full_greeting_with_age)  # This will print 'Hello, Alice! You are