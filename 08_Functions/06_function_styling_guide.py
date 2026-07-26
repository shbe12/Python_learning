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
# start cheking the logic
# 5. do not print inside function
# replace prints wih return to send data back to the program
# if need to print do it in the main code not inside the functions
# 6.do not modify the values of the parameters, leave it as is, use local variables instead
# don't change parameter values directly, create local variables for any processing
# if you have one line calculation without extra steps inside tou can skip using any assignment.
# put ismple calculations directly inside the return statement instead of storing them in extra variables

# extra rules
# 7. Use data type hints for the function parameters and their return values
# Always add type hints to parameters and return to make the function easier to understand
# def add(a: str) -> int:
# most bugs come from wrong data types
# hints does not convert, they are for humans
# 8. description for the input and output inside the docstring
# explain args and return in docstring
# always describe what goes in and what comes out of the function in the docstring
def DiscPrint(p,r):
    print("calculating discount")
    p = p - (p * r/100)
    print(p)

DiscPrint(80,20)



def calculate_discount(price: float, rate: float) -> float: # original price inside parameter,hints
    """
    Calculate the final price after applying a discount.
    Args:
        price (float): Original Product Price.
        rate (float): Discount Rate as numbers(e.g 20 for 20%)
    Returns:
        final_price (float): Final price after applying discount.
    """
    # modified  inside a local variable so we do not lose values - final_price
    return price - (price * rate/100) # here we have to start using our parameters , here it is price

help(calculate_discount)
