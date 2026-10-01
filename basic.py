
password = input("Enter your password:")

length = len(password)

if length >= 8:
    print("Valid Password")
else:
    print("Invalid Password")
    print("Password must contain at least 8 characters")