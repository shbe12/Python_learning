# Rounding numbers
# Round half to even is the default rounding method in Python, also known as "bankers' rounding". This means that when a number is exactly halfway between two integers, it will round to the nearest even integer.
#1.5 → 2
#2.5 → 2
#3.5 → 4
import math # for functions like floor, ceil, and trunc
price = 35.54879865
print(round(price)) # Output: 36, rounds to nearest whole number, When the number is exactly halfway between two integers (ends in .5), Python rounds to the nearest even number.
print(math.floor(price))  # Output: 35
print(round(price, 2))  # Output: 35.55 , 2 decimal places
print(round(price, 1))  # Output: 35.5 , 1 decimal place
print(math.ceil(price))   # Output: 36
print(math.trunc(price))  # Output: 35, strictly removes the decimal part without rounding
print(int(price))  # Output: 35, converts to integer, effectively truncating the decimal part
# if you are not using math already, just use int() it's simple and built in
# if you have already imported math use trunc() it  makes your intent clearer
# ================================================================================
# ABSOLUTE VALUE & ROUNDING FUNCTIONS
# ----------------------------------------
# Python provides built-in tools to:
# - Remove negative signs
# - Round numbers
# - Control decimal precision
#
# These are extremely common in financial,
# analytics, and data processing tasks.
# ================================================================================


# ---------------------------------------
# Absolute Value
# ---------------------------------------
# abs() removes the negative sign.
# It always returns a positive number.

print(abs(2 - 10))   # -> 8

# ---------------------------------------
# Rounding Numbers
# ---------------------------------------
# round() rounds to nearest value.
# You can control decimal places.

price = 35.54879865

print(round(price))      # -> 36    (nearest whole number)
print(round(price, 2))   # -> 35.55 (2 decimal places)
print(round(price, 1))   # -> 35.5  (1 decimal place)

# ---------------------------------------
# Math Module (Advanced Rounding Control)
# ---------------------------------------
# The math module provides more specific control.

import math

print(math.floor(price))  # -> 35 (always round down)
print(math.ceil(price))   # -> 36 (always round up)
print(math.trunc(price))  # -> 35 (remove decimal part)

print(int(price))         # -> 35 (similar to trunc)
