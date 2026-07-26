# Function Styling Guide
# Goal is to write fucntionsthat are easy to read and understand.
# PEP8- style guide

# bad style
# First look at the Function name
# 1. follow the naming convention, the snake
# lowercases sperated by underscores
#2. use clear descriptive function names
# describe clearly what the function does
# start with a verb
# use full words, avoid abbreviations
# 3. Parameter names describe their values
# use full meaningful words
# avoid abbreviations and single letters
#4. always use docstring to describe what the function does
# help teammates understand your code
# help future you remember the logic
# doctring is a string on the first line inside a function that explains what the function does.
# why not comments instead of docstrings, the comments lost ignored, the program , the code, don't know about the comment at all
# Python can use docstring as description for function
# docstrings stored inside the function as documentation, so it is not lost
# something that is attached to the function
# we are using the string aas a value for our function , but it is inside the program and can be called
# docstring can be used by functions,tools,IDEs
# python can return documentation of function with help()


def DiscPrint(p,r):
    print("calculating discount")
    p = p - (p * r/100)
    print(p)

DiscPrint(80,20)


# def disc_print():

def calculate_discount(price, rate):
    """ Calculate the final price after applying a discount."""
    return 1

help(calculate_discount)
