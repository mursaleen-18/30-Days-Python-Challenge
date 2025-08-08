a = (1,2,45, 3343, False, "hello", )
print(a) 
print(type(a))

no = a.count(45)
print(no)

i = a.index(3343)
print(i)

i2 = a.index("123")
print(i2)  # This will raise a ValueError since "123" is not in the tuple