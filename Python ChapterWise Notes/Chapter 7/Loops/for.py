# printing values from 1 to 10
# for i in range(1, 11):
#     print(i)

# ============================================================

# print("for loop with step of 2:")

# # syntax => for i in range(start, stop, step_size)
# # printing values from 1 to 10 with a step of 2

# for i in range(0, 11, 2):
#     print(i)

# ==============================================================

# printing all elements of the list using a for loop
# list = [1, "Magnetic", 3.14, True, "This", "Python", 4, "computer"]

# print("Using for loop to print all elements of the list:")

# for item in list:
#     print(item)

# =====================================================================

# for loop with else clause.

# print("Using for loop with else clause:")

# for item in list:
#     print(item)
# else:
#     print("All items have been printed from the list.")
# # the else block executes after the for loop completes normally,
# # not when it is terminated by a break statement.

# =================================================

# table of any number using for loop
# n = int(input("Enter a number to print its table: "))

# print(f" Table of {n} using for loop:")

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# =================================================
# Table of any number using for loop with step size

# for i in range(4, 40, 4):
#     print(i)


# =================================================

# find prime numbers using for loop

# n = int(input("Enter a number: "))
# for i in range(2, n):
#     if (n % i) == 0:
#         print(f"{n} is not a prime number.")
#         break
# else:
#     print(f"{n} is a prime number.")

# ================================================

# sum of first n natural numbers using for loop

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
#     i += 1
# print(f"The sum of first {n} natural numbers is: {sum}")

# ================================================

# Factorial of a number using for loop

# n = int(input("Enter a number to find its factorial: "))

# factorial = 1

# for i in range(1, n+1):
#     factorial *= i
#     i += 1
# print(f"The factorial of {n} is: {factorial}")

# =================================================

# star pattern using for loop

n = int(input("Enter the number of rows for the star pattern: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")
