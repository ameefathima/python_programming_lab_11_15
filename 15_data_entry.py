# Program to Validate Email, Phone Number and Extract Transaction IDs Using Regex

import re

# Validate email
email = input("Enter email address: ")

if re.match(r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$', email):
    print("Valid Email")
else:
    print("Invalid Email")

# Validate phone number
phone = input("Enter phone number: ")

if re.match(r'^[6-9][0-9]{9}$', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

# Extract transaction IDs
log = input("Enter log message: ")

ids = re.findall(r'TXN\d+', log)

print("Transaction IDs:", ids)