import re

# Define regex pattern for validating email
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Function to check email validity
def validate_email(email):
    if re.match(pattern, email):
        return True
    else:
        return False

# Test cases
emails = [
    "user@example.com",
    "hello.world@domain.co.in",
    "invalid-email@.com",
    "noatsign.com",
    "username@domain",
    "name@domain.c"
]

# Checking emails
for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")
