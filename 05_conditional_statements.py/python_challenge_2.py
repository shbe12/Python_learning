# password must not be empty,
# must be at least 8 characters,
# must contain at least one uppercase letter,
# must contain at least one lowercase letter,
# must not be the same as email,
# must not contain spaces,
# and must start and end with a letter or a digit.

password = "password123"
email = "user@example.com"
password = password.strip()
if password == "":
    print("Password cannot be empty")
elif len(password) < 8:
    print("Password must be at least 8 characters")
elif not any(c.isupper() for c in password):
    print("Password must contain at least one uppercase letter")
elif not any(c.islower() for c in password):
    print("Password must contain at least one lowercase letter")
elif password == email:
    print("Password cannot be the same as email")
elif " " in password:
    print("Password cannot contain spaces")
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or a digit")
else:
    print("Password is valid")

password = "password123"
email = "user@example.com"
valid = True
password = password.strip()
if password == "":
    print("Password cannot be empty")
    valid = False
if len(password) < 8:
    print("Password must be at least 8 characters")
    valid = False
if not any(c.isupper() for c in password):
    print("Password must contain at least one uppercase letter")
    valid = False
if not any(c.islower() for c in password):
    print("Password must contain at least one lowercase letter")
    valid = False
if password == email:
    print("Password cannot be the same as email")
    valid = False
if " " in password:
    print("Password cannot contain spaces")
    valid = False
if password and not (password[0].isalnum() and password[-1].isalnum()): #Here, if password: means "if the string is not empty."
    print("Password must start and end with a letter or a digit")
    valid = False
if valid:
    print("Password is valid")


# if password and not (password[0].isalnum() and password[-1].isalnum()):
#     print("Password must start and end with a letter or a digit")
#     valid = False

# if password != "" and not (password[0].isalnum() and password[-1].isalnum()):
#     print("Password must start and end with a letter or a digit")
#     valid = False

# if password != "" and not (password[0].isalnum() and password[-1].isalnum()):
#     print("Password must start and end with a letter or a digit")
#     valid = False
