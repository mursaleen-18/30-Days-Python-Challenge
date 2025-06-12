def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Example: Print first 10 Fibonacci numbers
for num in fibonacci_generator(10):
    print(num)
