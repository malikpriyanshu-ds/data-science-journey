# Mini Project: Simple Login System
# Concepts:
# - Boolean logic
# - Conditional statements
# """

username = "admin"
password = "1234"

user = input("Enter your username: ")
your_pass = input("Enter your password: ")

if user == username and your_pass == password:
    print("Access Granted ✅")
else:
    print("Invalid Credentials ❌")