import math
# built-in functions,come with python ,can use them: Number, String, Data Structure
# print() , len() , type() , int() , str() , list() , dict() , set() , tuple()
# standard library functions, written by python team,improt then use
# math , random , datetime , os , sys , json , csv , re
# external library, written by community, install import use them
#Pandas , numpy , matplotlib , seaborn , sklearn , tensorflow , keras

# you do not have to deal with definition of the function ,just use them
# User-Defined functions: write your own desifintion, we define and then use them
#  How to choose your source
# 1. check if it exist, check built in functions
# 2. check the standard libraries
# 3. if not found,ask your team , then 4.if not then write your own

# function are small reusable block of code that does one specific job.
# why funtions
# you solve problem using the same code logic multiple times
# you can code can be outdates, inconsistent behaviours, hard to change, time consuming,hard to read , hard to understand
# instead of repeating sam logic , put logic in one place inside a function
# when needed just call the function
# now if you want to modify you only change one place,easier,faster,safer,smaller,cleaner,modular easier to read,collaboration
#code modularity , big complex problems in smaller pieces
# how function works
#user defined functions has 2 parts, funtion defition/declaration and call
#to execute write the function name followed by paranthesis.

def greet():
    print("Hello")

greet()
print("End")

# logic exist twice
print("Wake up")
print("Start Machine")
print("Make Coffee")
print("Add Milk")
print("Enjoy it")

print("Working for a while")

print("Start Machine")
print("Make Coffee")
print("Add Milk")
print("Enjoy it")

print("-------------------")

# solution
def make_coffee():
    print("Wake up")
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")
    print("Enjoy it")

print("Wake up")
make_coffee()
print("Working for a while")
make_coffee()
make_coffee()

# types of function
#built-in function
print(len("Python"))

# function from libraries, import math, at the top of file
number = 4.2
print(math.ceil(number))

# user-defined function
def greet():
    print("Hello")
greet()

# ================================================================================
# FUNCTIONS (WHY • BUILT-IN • USER-DEFINED)
# ----------------------------------------
# Functions help us avoid repetition.
# Instead of writing the same code again and again,
# we define it once and reuse it.
# ================================================================================


# ---------------------------------------
# Problem: Repetition
# ---------------------------------------
# Here we repeat the same coffee steps multiple times.

print("Wake up")
print("Start Machine")
print("Make Coffee")
print("Add Milk")
print("Enjoy it")

print("Working for a while")

print("Start Machine")
print("Make Coffee")
print("Add Milk")
print("Enjoy it")


# ---------------------------------------
# Solution: Create a Function
# ---------------------------------------
# We define the steps once, then call them whenever we need.

def make_coffee():
    print("Start Machine")
    print("Make Coffee")
    print("Add Milk")
    print("Enjoy it")


print("Wake up")
make_coffee()
print("Working for a while")
make_coffee()
make_coffee()


# ---------------------------------------
# Python Function Sources
# ---------------------------------------

import math


# Example 1: Built-in Function
# Already available in Python.
print(len("Python"))   # -> 6


# Example 2: Function from a Library
# We import first, then call it.
number = 4.2
print(math.ceil(number))   # -> 5


# Example 3: User-Defined Function
# We define it ourselves using def.

def greet():
    print("Hello")

greet()   # -> Hello
