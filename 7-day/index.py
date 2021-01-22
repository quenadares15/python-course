# 7 DAY

# Loop is need to check, that password or nick in login system isn't empty

# I started by making variables with empty string.
# Then variable content is changing to input
name = ""
while not name:
    name = input("\nName: ")

password = ""
while not password:
    password = input("Password: ")

# Next I checking, that the names and passwords are in the database (this file).
# You can manage database (this file) manually.

if name == "admin" and password == "admin":
    print("Welcome, " + name)
elif name == "test" and password == "test":
    print("\nWelcome, " + name)
else:
    print("\nAccess denied.")

# 7 day complete!