# complex 2 + 3j
x = 5
y = 5.7
z = 2+ 3j
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

x = "24"
print(type(x))  # <class 'str'>
print(x * 3)

x = int(x)
print(type(x))  # <class 'int'>
print(x * 3)

x = 3.14
print(int(x))

x = 3
print(float(x))

x = "3.14"
print(float(x))

x = 3 #real
y = 4 #imaginary
print(complex(x, y))  # (3+4j)

print (2 + 3)
print(7 / 2)
print(7 // 2)
print(7 % 2) # left over after division
print(2 ** 3) # 2 to the power of 3

# x = 2
# x = x + 3
# print(x)  # 5
x = 2
x += 3 # x = x + 3
print(x)  # 5

r = 5
r *=2 # r = r * 2
print(r)  # 10

# ================================================================================
# NUMERIC DATA TYPES & BASIC NUMBER TOOLS
# ----------------------------------------
# Python supports different numeric types:
# - int      → Whole numbers
# - float    → Decimal numbers
# - complex  → Numbers with imaginary part
#
# We can convert between types and perform arithmetic operations.
# ================================================================================


# ---------------------------------------
# Numeric Types
# ---------------------------------------

x = 5
y = 5.7
z = 2 + 3j

print(type(x))  # -> <class 'int'>
print(type(y))  # -> <class 'float'>
print(type(z))  # -> <class 'complex'>


# ---------------------------------------
# Type Conversion
# ---------------------------------------
# Convert values between numeric types.

x = "24"
print(type(x))  # -> <class 'str'>

x = int(x)      # Convert string to integer
print(type(x))  # -> <class 'int'>
print(x * 3)    # -> 72

x = 3.14
print(int(x))   # -> 3 (decimal part removed)

x = 3
print(float(x)) # -> 3.0

x = 3
y = 4
print(complex(x, y))  # -> (3+4j)


# ---------------------------------------
# Basic Arithmetic Operations
# ---------------------------------------

print(2 + 3)     # -> 5   (Addition)
print(5 - 3)     # -> 2   (Subtraction)
print(4 * 2)     # -> 8   (Multiplication)
print(7 / 2)     # -> 3.5 (True division → float)
print(7 // 2)    # -> 3   (Floor division → integer result)
print(9 % 2)     # -> 1   (Modulus → remainder)
print(2 ** 3)    # -> 8   (Exponentiation)


# ---------------------------------------
# Compound Assignment Operators
# ---------------------------------------
# Shorter way to update a variable.

x = 2

x += 3
print(x)  # -> 5

x -= 1
print(x)  # -> 4

x *= 2
print(x)  # -> 8

# ---------------------------------------
# Useful Built-in Numeric Functions
# ---------------------------------------

print(abs(-10))   # -> 10  (Absolute value)
print(pow(2, 3))  # -> 8   (Power function)
print(divmod(7, 2))  # -> (3, 1) (Quotient, Remainder)
print(2-10)
print(abs(2-10))

# pow()

# The pow() function raises a number to a power.

# Syntax
# pow(base, exponent)
# Example
# print(pow(2, 3))

# Output:

# 8

# This is the same as:

# print(2 ** 3)

# Output:

# 8
# Three-argument version

# pow() has a special version with three arguments:

# pow(base, exponent, modulus)

# It calculates:

# (base ** exponent) % modulus

# Example:

# print(pow(2, 5, 3))

# Steps:

# 2 ** 5 = 32
# 32 % 3 = 2

# Output:

# 2

# This version is commonly used in cryptography because it's much faster than calculating the power first.

# More examples
# print(pow(5, 2))

# Output:

# 25
# print(pow(10, 3))

# Output:

# 1000
# print(pow(9, 0.5))

# Output:

# 3.0

# Since raising to the power 0.5 means taking the square root.

# divmod()

# divmod() performs division and modulus at the same time.

# It returns two values:

# Quotient
# Remainder
# Syntax
# divmod(a, b)
# Example
# print(divmod(17, 5))

# Output:

# (3, 2)

# Because

# 17 ÷ 5 = 3 remainder 2
# Without divmod()

# Normally you'd write:

# quotient = 17 // 5
# remainder = 17 % 5

# print(quotient)
# print(remainder)

# Output

# 3
# 2

# divmod() combines both operations into one.

# Using unpacking
# quotient, remainder = divmod(17, 5)

# print(quotient)
# print(remainder)

# Output

# 3
# 2

# This is the most common way to use divmod().

# More examples
# print(divmod(20, 6))

# Output

# (3, 2)
# print(divmod(25, 5))

# Output

# (5, 0)

# No remainder because 25 is divisible by 5. #
