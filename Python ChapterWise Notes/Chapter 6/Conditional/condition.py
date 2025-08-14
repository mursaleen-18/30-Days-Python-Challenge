a = int(input("Enter your Age: "))


# if elif else ladder.
if a >= 18:
    print("you are eligible to vote")
    
elif a == 0:
    print("You have entered entered zero")

elif a <0:
    print("You are entering an invalid age")

else:
    print("you are not eligible to vote")

print("Thank you for using the program")