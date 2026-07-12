#email must not be empty,
# must contain '@' and '.',
# must contain exactly one '@',
# must end with '.com', '.org', or '.net',
# must not be longer than 254 characters,
# and must start and end with a letter or a digit.

email = "example@gmail.com"
#clean the string
#first, remove leading and trailing whitespace using strip(), then check if the string is empty. If it is, print "Email cannot be empty". Otherwise, print "Email is valid".
email = email.strip()
#email must not be empty
if email == "":
    print("Email cannot be empty")
# email must contain '@' and '.'
elif not ('.' in email and '@' in email):
    print("Email must contain '@' and '.'")
#email must contain exactly one '@'
elif email.count('@') != 1:
    print("Email must contain exactly one '@'")
# email must end with '.com', '.org', or '.net'
elif not email.endswith(('.com', '.org', '.net')):
    print("Email must end with '.com', '.org', or '.net'")
# email must not be longer than 254 characters
elif len(email) > 254:
    print("Email must not be longer than 254 characters")
# email must start and end with a letter or a digit.
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or a digit")
else:
    print("Email is valid")

#want to see all conditions are evaluated , else if stops at first relevant condition, so we can use independent if statements instead of elif statements, but this will make the code less readable and less efficient, so use with caution.
#issue here the else is only for the last if statement, so if the email conatins 2 @, it will print "Email must contain exactly one '@'and then it will check the other conditions and print "Email is valid" even though the email is empty,
#first, remove leading and trailing whitespace using strip(), then check if the string is empty. If it is, print "Email cannot be empty". Otherwise, print "Email is valid".
email = "eexample@@gmail.com"
email = email.strip()
#email must not be empty
if email == "":
    print("Email cannot be empty")
# email must contain '@' and '.'
if not ('.' in email and '@' in email):
    print("Email must contain '@' and '.'")
#email must contain exactly one '@'
if email.count('@') != 1:
    print("Email must contain exactly one '@'")
# email must end with '.com', '.org', or '.net'
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with '.com', '.org', or '.net'")
# email must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters")
# email must start and end with a letter or a digit.
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or a digit")
else:
    print("Email is valid")

#solution with valid

email = "example@gmail.com"
valid = True
# clean the string
email = email.strip()
#email must not be empty
if email == "":
    print("Email cannot be empty")
    valid = False
# email must contain '@' and '.'
if not ('.' in email and '@' in email):
    print("Email must contain '@' and '.'")
    valid = False
#email must contain exactly one '@'
if email.count('@') != 1:
    print("Email must contain exactly one '@'")
    valid = False
# email must end with '.com', '.org', or '.net'
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with '.com', '.org', or '.net'")
    valid = False
# email must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters")
    valid = False
# email must start and end with a letter or a digit.
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or a digit")
    valid = False
if valid:
    print("Email is valid")
