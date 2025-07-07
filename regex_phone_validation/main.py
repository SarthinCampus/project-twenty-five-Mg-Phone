import re

phone = input()

# Pattern: starts with 09, followed by 7 to 9 digits → total 9–11 digits
pattern = r'^09\d{7,9}$'

if re.match(pattern, phone):
    print("Valid")
else:
    print("Invalid")
