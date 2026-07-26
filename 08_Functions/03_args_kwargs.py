# some scenarios where we don't know in advance how many values we're going  pass to the function
# for that we have *args and **kwargs
# *args and **kwargs allow functions to accept a unkown number of arguments,flexiblility
# * args for positional arguments, **kwargs for keyword arguments

# calculate total of values
def total(a, b):
    print(a + b)
total(1, 2)
# total(1, 2, 3) #error because we have only 2 parameters in the function

def total(a=0, b=0, c=0): #default values for parameters, if we don't pass any value, it will use the default value
    print(a + b + c)
total(1, 2)
total(1, 2, 3)
#total(1, 2, 3, 4) #error because we have only 3 parameters in the function

# more values
def total(*args): # *args allows the function to accept a variable number of positional arguments
    # print(type(args)) # tuple
    print(sum(args))

total(1, 2)
total(1, 2, 3)
total(1, 2, 3, 4)

#when to use *args - when you pass similar values, (1,2,3,4), (alex, john, maria), (True, False, True)
# for different types of values use the **kwargs, for example, name="alex", age=30, country="USA"

#create the user profile
def create_user(**kwargs): # **kwargs allows the function to accept a variable number of keyword arguments
    print(type(kwargs)) # dictionary, we are using the key words arguments, this is key value pairs, only data that can hold key value pairs is dictionary
    print(kwargs)

create_user(first_name="alex",
            last_name="smith",
            age=30,
            country="USA")

create_user(first_name="maria",
            country="Mexico")

# *args, positional arguments, "only values", same type of information, stored in a tuple
# **kwargs, keyword arguments, "key value pairs/ names + values", different types of information, stored in a dictionary
# ================================================================================
# VARIABLE ARGUMENTS (*args • **kwargs)
# ----------------------------------------
# Sometimes we don’t know how many inputs
# a function will receive.
#
# Python allows flexible arguments using:
# - *args  → multiple positional arguments
# - **kwargs → multiple keyword arguments
# ================================================================================


# ---------------------------------------
# *args (Multiple Positional Arguments)
# ---------------------------------------
# Here we want to calculate the total of an unknown number of values.
def total(*args):
    print(type(args))     # args is a tuple
    print(sum(args))

total(1, 2)
total(1, 2, 3)
total(1, 2, 3, 4)

# ---------------------------------------
# **kwargs (Multiple Keyword Arguments)
# ---------------------------------------
# Here we want to build a flexible user profile.
# We don’t know which fields the user will provide.

def create_user(**kwargs):
    print(type(kwargs))   # kwargs is a dictionary
    print(kwargs)

create_user(
    first_name="Mo",
    last_name="Salah",
    age=33,
    country="Egypt"
)
create_user(
    name="Ronaldo",
    country="Portugal"
)
