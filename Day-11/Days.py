from datetime import datetime

# Input two dates as strings
date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert strings to datetime objects
date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

# Calculate difference in days
difference = abs((date2 - date1).days)

print(f"The number of days between the two dates is: {difference}")
