def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Example usage:
num = 5
print(f"The factorial of {num} is {factorial(num)}")
