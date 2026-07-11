# ================================================================================
# DATA TYPES
# ----------------------------------------
# Python has multiple built-in data types to represent different kinds of values.
# Common types include integers, floats, strings, booleans, and NoneType.
# ================================================================================

# ---------------------------------------
# Examples of Different Data Types
# ---------------------------------------
from dbm.ndbm import library


a = 10        # int
b = 3.15      # float
c = "Hello"   # str (double quotes)
d = 'Hi'      # str (single quotes)
e = "1234"    # str (looks like a number, but it's a string)
f = True      # bool
g = False     # bool
h = None      # NoneType
i = ""        # str - empty string, blank string
j = " "       # str - contains a single space

'Hello'.upper() #function
print(2+3) #method
print("2" + "3")

# primitives types in python are: int, float, bool, str

# functions: Stand-alone functions-print(),type(), methods of class -upper(),lower(),capitalize(),title(),strip(),split(),join(),replace(),Operations: +, -, *, /, //, %, **, ==, !=, >, <, >=, <=, and, or, not
# user defined functions, third party library ,standard library with built in functions, methods of class, operations, and operators are all part of Python's functionality.

text = "Hello, World!"
number = 10

print (type(text))   # Output: <class 'str'>
print (type(number)) # Output: <class 'int'>

print(len(text))   # Output: 13
# print(len(number))  # error
print(text.upper())  # Output: "HELLO, WORLD!"
# number.upper()  # error, because int type does not have an upper() method
print(number.bit_length())  # Output: 4
# print(text.bit_length())  # error, because str type does not have a bit_length() method
# No value single value multiple value

age = 26
height = 5.6
name = "Sherline"
student = True
car = None
print("Age:", age, "Height:", height, "Name:", name, "Student:", student, "Car:", car)
print(type(age), type(height), type(name), type(student), type(car))
print(len(name))
# print(len(age), len(height), len(name), len(student), len(car)) # This will raise an error for age, height, and student because they are not iterable types. Only strings and collections have a length.

# Exploring Methods for Each Data Type
# ---------------------------------------
# Some methods are specific to certain types.
print(text.upper())           # "HI" (string method)
print(number.bit_length())    # 4   (integer method)
# print(text.bit_length())    # Error: str has no bit_length()

# ---------------------------------------
# Python Challenge
# ---------------------------------------
# Create 5 variables, each with a different data type:
# - Your age
# - Your height (with decimals)
# - Your name
# - Are you a student?
# - Something with no value yet

age        = 30            # int
height     = 1.75          # float
name       = "Maria"       # str
is_student = False         # bool
has_kids   = None          # NoneType
