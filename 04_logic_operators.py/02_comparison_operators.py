#comparison operators
# ==, !=, >, <, >=, <=
print(3 > 2) # true

x = 5
print (x == 5) # true
print (x < 6) # true
print (2-1 != 1) # false
print(10 == 10) # true
print(10 != 10) # false
print(10 >= 10) # true
print(10 <= 10) # true

print("a" > "b") # false
print("a" < "b") # true
print("a" == "a") # true
print("a" == "A") # false

print (1 < 4 < 6) # true because 1 is less than 4 and 4 is less than 6
print (1 > 4 < 5 ) # false because 1 is not greater than 4 but 4 is less than 5

# I s age btween 18 and 30?
age = 20
print(18 <= age <= 30) # true because age is between 18 and 30

age = 36
print(18 <= age <= 30) # false because age is not between 18 and 30

# ================================================================================
# COMPARISON OPERATORS
# ----------------------------------------
# Comparison operators are used to compare values and return Boolean results.
# These include equality, inequality, greater/less than, and range comparisons.
# ================================================================================

# ---------------------------------------
# Basic Comparison Operators
# ---------------------------------------
print(10 == 10)   # ➜ True  (equal to)
print(10 != 10)   # ➜ False (not equal to)
print(7 > 3)      # ➜ True  (greater than)
print(7 >= 3)     # ➜ True  (greater than or equal to)
print(3 < 7)      # ➜ True  (less than)
print(7 <= 7)     # ➜ True  (less than or equal to)

# ---------------------------------------
# String Comparison: Case Sensitivity
# ---------------------------------------
print("a" == "A")                     # ➜ False (case-sensitive)
print("a".lower() == "A".lower())     # ➜ True  (case-insensitive comparison)

# ---------------------------------------
# Alphabetical Comparison
# ---------------------------------------
print("a" < "b")  # ➜ True — "a" comes before "b" in ASCII order

# ---------------------------------------
# Common Mistake: Using = Instead of ==
# ---------------------------------------
# print("a" = "A")  # SyntaxError: cannot use = in comparisons
# Correct usage:
print("a" == "A")  # ➜ False

# ---------------------------------------
# Assignment vs Comparison
# ---------------------------------------
x = "a"            # Assignment
print(x == "a")    # ➜ True  (comparison)

# ---------------------------------------
# Chained Comparison (Range Check)
# ---------------------------------------
age = 18
print(18 <= age <= 30)  # ➜ True (age is between 18 and 30)

age = 35
print(18 <= age <= 30)  # ➜ False (35 is outside the range)
