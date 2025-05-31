# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n == 2:
        return True   # 2 is the only even prime number
    if n % 2 == 0:
        return False  # eliminate even numbers > 2

    # Check for factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Take input from the user
try:
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
