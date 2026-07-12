# ================================================================================
# LOGICAL OPERATORS & IDENTITY CHECKS
# ----------------------------------------
# Python provides logical operators to combine multiple conditions:
# `and`, `or`, `not` — which return Boolean results based on truth tables.
# This section also covers `in`, `not in`, `is`, and `is not`.
# ================================================================================

# ---------------------------------------
# Basic Logical Operators: and / or
# ---------------------------------------
print(3 > 1 and 5 < 1)   # ➜ False: first is True, second is False
print(3 > 1 and 5 > 1)   # ➜ True: both are True

print(3 > 1 or 5 < 1)    # ➜ True: first is True, second is False
print(3 > 1 or 5 > 1)    # ➜ True: both are True

print(3 > 5 and 5 != 5)  # ➜ False: first is False, second is False

cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)  # ➜ True: memory usage exceeds threshold

email = True
password = False
print(email and password)  # ➜ False: email is True but password is False

print(3 > 2)  # ➜ True
print(not 3 > 2)  # ➜ False
print(not False)  # ➜ True
print(not True)  # ➜ False
print( not not True)  # ➜ True
print( not not False)  # ➜ False

name = ""
print (not name)  # ➜ True: empty string is considered False, so not False is True
print (not not name)  # ➜ False: double negation returns the original truthiness
print(not 10)          # ➜ False: 10 is truthy


# and hass higher precedence than or, so it is evaluated first. Parentheses can be used to clarify order of operations.
#5==5 or 8 > 5 and 6 < 4 # true because 5==5 is true, and the rest is false, but or only needs one true to return true
(5==5 or 8 > 5) and 6 < 4 # parantheses is calcualated first so here we start with or , false because the first part is true, but the second part is false, and and needs both to be true to return true

# allow if logged in or guest and not banned
is_logged_in = True
is_guest = False
is_banned = False

print(is_logged_in or is_guest and not is_banned)

#problem banned user is logged in, but he is banned, so he should not be allowed to log in, but the above statement will return true because the first part is true, and and has higher precedence than or, so it will be evaluated first, and not is also evaluated first, so the second part is false, and or only needs one true to return true, so the whole statement returns true, which is not what we want.
is_logged_in = True
is_guest = False
is_banned = True

print(is_logged_in or is_guest and not is_banned)

# solution
print((is_logged_in or is_guest) and not is_banned)

# 'a' not in 'Data' false because 'a' is in 'Data'
# 'a' not in ['b', 'c'] true because 'a' is not in the list

print('o' not in 'Hello')  # ➜ True: 'o' is in 'Hello', so not in returns False
print( 3 in [1, 2, 3])  # ➜ True: 3 is in the list

domain = "gmail.com"
banned_domains = ["spam.com", "baddomain.com"]
print(domain not in banned_domains)  # ➜ True: domain is not in the banned

#check if two variables point to the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]
print( a == b)  # ➜ True: values are equal, compare values
print( a is b)  # ➜ False: different objects in memory, not same id,compare ids

a = 5
b = 5
#simple value creates one object in memory, so both variables point to the same object
print( a is b) # ➜ True: same object in memory, compare ids

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print( x == y)  # ➜ True: values are equal, compare values
print( x is y)  # ➜ False: different objects in memory, not same id,compare ids

x = 10
y = 10
print( x == y)  # ➜ True: values are equal, compare values
print( x is y)  # ➜ True: same object in memory, compare ids


x = ['a', 'b', 'c']
y = x
print( x == y)  # ➜ True: values are equal, compare values
print( x is y)  # ➜ True: same object in memory, compare ids


email = ""
email != ""
print(email != "")  # ➜ False: email is empty, so not equal to empty string is False

email = None
print(email != "")  # ➜ True: email is None, so not equal to empty string is True

print(email != None)  # ➜ False: email is None, so not equal to None is False
print(email != None and email != "")  # ➜ False: email is None, so not equal to None is False, and not equal to empty string is True, but and needs both to be True to return True, so the whole statement returns False

# None is no value at all ,unkown, "" means empty but known,a string

# always use is None or is not None to check for None, because None is a singleton object, and using == or != can lead to unexpected results if the variable is not None but has a value that is equal to None.

# ---------------------------------------
# Real-World Example: System Monitoring
# ---------------------------------------
cpu_usage    = 70
memory_usage = 90

print(cpu_usage > 90 or memory_usage > 90)  # ➜ False: both values are within limits

# ---------------------------------------
# Login Validation
# ---------------------------------------
email    = True
password = False

print(email and password)  # ➜ False: both must be True to allow login

# ---------------------------------------
# Logical NOT
# ---------------------------------------
print(not 3 > 2)       # ➜ False
print(not True)        # ➜ False
print(not False)       # ➜ True
print(not not False)   # ➜ False

name = ""
print(not name)        # ➜ True: empty string is falsy
print(not 10)          # ➜ False: 10 is truthy

# ---------------------------------------
# Complex Access Control Logic
# ---------------------------------------
# Allow access if the user is logged in OR a guest,
# BUT they must not be banned.

is_logged_in = True
is_guest     = False
is_banned    = True

print(is_logged_in or is_guest and not is_banned)      # ➜ True (wrong logic)
print((is_logged_in or is_guest) and not is_banned)    # ➜ False (correct logic)

# ---------------------------------------
# Python Challenges
# ---------------------------------------
# 1. Name is not empty and age is >= 18
# 2. Password is at least 8 chars and has no spaces
# 3. Email is not empty, contains '@', and ends with '.com'
# 4. Username is a string, not None, and longer than 5 characters
# 5. User is admin or moderator, and not banned or email verified

# ---------------------------------------
# Membership Operators: in / not in
# ---------------------------------------
print("f" not in "python")      # ➜ True
print(3 not in [1, 2, 3])       # ➜ False

domain = "spam.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)  # ➜ False

# ---------------------------------------
# Identity Operators: is / is not
# ---------------------------------------
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)  # ➜ True: same content
print(x is y)  # ➜ False: different objects in memory

x = 10
y = 10

print(x == y)  # ➜ True: same value
print(x is y)  # ➜ True: same object (small integers are cached)

x = ['a', 'b', 'c']
y = x

print(x == y)  # ➜ True: same values
print(x is y)  # ➜ True: same object (same memory reference)

# ---------------------------------------
# Validate Email Exists and Is Not Empty
# ---------------------------------------
email = "b@gmail.com"
print(email != "")              # ➜ True

email = None
print(email is not None and email != "")  # ➜ False

# name is not empty and age is >= 18
username = ""
age = 20
print(username != "" and age >= 18)
#or using bool() to check truthiness of username,empty string is falsy, so bool(username) will be False, and the whole expression will be False
print(bool(username) and age >= 18)  # ➜ False: username is empty, so bool(username) is False

#password is at least 8 chars and has no spaces
password = "hbzsuhusrh "
# password != " " only checks whether the password is exactly one space
# print(len(password) >= 8 and password != " ")
print(len(password) >= 8 and " " not in password)  # ➜ False: password has a space

#Email is not empty, contains '@', and ends with '.com'
email = "b@gmail.com"
print(email != "" and "@" in email and email.endswith(".com"))

#Username is a string, is not None, and longer than 5 characters
username2 = "baraa123"
# wrong,syntax errors
# print(isinstance(username2 str and is not None and (len(username2)) > 5)
print(isinstance(username2, str)
       and username2 is not None
       and len(username2) > 5
)

# Admin or moderator, and (not banned or email verified)

is_admin = True
is_moderator = True
is_banned = True
email_verified = True
# syntax mistakes
# user = is_admin and is not is banned
# print( user is_moderator or is_admin and not is_banned or email_verified))
user = (is_admin or is_moderator) and (not is_banned or email_verified)
print(user)  # ➜ True: user is admin and email is verified, so access

# or
has_permission = is_admin or is_moderator
can_login = not is_banned or email_verified

print(has_permission and can_login)
