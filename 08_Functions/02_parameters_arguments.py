# Parameters and Arguments in Functions
# how data flows through functions
#parameters,arguments,return,types,chapes,and purposes of functions.
# not all functions work the same way ,some functions do not take data.
# another function take data, has input, can perform action,it stops, with no output, no data going outside
# another funtion accepts input ,takes data, tranform it, then returns the result, as an output,data goes out transformed.
# another takes multiple inputs, multiple data, then calcuculations and transformations,then you could have multiple outputs data going outside
# DATA THAT GOES IN INPUT PARAMETERS AND ARGUMENTD AND DATA THAT COMES OUT RETURN VALUE

# parameters named used in function definition that describe what data the function expects
# arguments real values passed in a function call that are assigned to parameters

# def function_name(parameter):

# function_name(argument)

def multiple_two(x):
    print(x*2)

multiple_two(3)

#funtion to normalize string
#harcoded
# def clean_name():
#     name = " MariA "
#     print(name.strip().lower())

# clean_name()

def clean_name(name):
    print(name.strip().lower())

# more generic
clean_name(" MariA ")
clean_name("  JOhN  ")
clean_name("")

#parameters look like variables
# in python 3 type of variables, parametrs,local variables, global variables
# how long does it live, where is it accesssible

#global variable is created outside of a function and can be accessed anywhere in the file
#local variable is created inside a function and can only be accessed inside that function

f = 2 # f is a global variable
def multiply_factor(x): # x is a parameter
    y = x * f      # y is a local variable
    print(y)

multiply_factor(3)
# python exute the call before the function definition, so if you call the function before it is defined, you will get an error.
# python knows the global variable, the parameter but not yet the local variable
# only after the function is called, the local variable is created and can be accessed inside the function.
#afterwards python remove argument from parameter,unassign the value
# then destoys the local variable, and the function is done executing, and the local variable is no longer accessible.
# global variable live from program strt to end, local variable live from function start to end, parameter live from function start to end, argument live from function call to function end.
#global variable acessable anywhere in the file, local variable only accessible inside the function, parameter only accessible inside the function, argument only accessible inside the function.
# local variable not accessible outside the function, parameter not accessible outside the function, argument not accessible outside the function.
# the parameter cannot be accessed outside the function, but the argument can be accessed outside the function, but only if it is assigned to a variable outside the function.

# variable scope examples
# usually paremeter holds raw data,keeps the raw valu to be reused
# store the processed data inside a new variable, local variable holds the processed version
def clean_name(name): #parameter
    cleaned = name.strip().lower() # cleaned is a local variable
    print("Raw:", name)
    print("Cleaned:", cleaned)


clean_name(" MariA ")
# print("Raw:", name)
# print("Cleaned:", cleaned)



case_rule = "n/a" #'lower' # global variable contols behavior without changing the function
def clean_name(name): #parameter
    cleaned = name.strip() # cleaned is a local variable
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Cleaned:", cleaned)


clean_name(" MariA ")
print("The Rule is:", case_rule)

# positional vs keyword arguments
#multiple parameters, multiple arguments, order matters, positional arguments, keyword arguments, order does not matter
# first send first name then last name, then merged into full name
def clean_name(first_name, last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print( full_name)

clean_name(" MariA ", "  LOPEZ  ")


# def clean_name(first_name, last_name = "n/a", country=): # put parameter with default value at the end after parameters without default values, otherwise you will get a syntax error.

def clean_name(first_name, last_name, country="n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print( full_name, "From", country)

# positional arguments values pass to the funtion based on their Order
# keyword arguments values pass to the function based on their Names

clean_name(" MariA ", "  LOPEZ  ", "USA") # positional arguments values pass to the funtion based on their Order
#clean_name("  USA  ", " MariA ", "LOPEZ  ") # positional arguments
clean_name(country="USA", last_name="  LOPEZ  ", first_name=" MariA ") # keyword arguments values pass to the function based on their Names

# keyword easier to read,safer with clear names, more time to write and maintain
# how to choose, positional arguments if 2-3 arguments, keyword arguments if more than 3 arguments.
# mixed arguments
clean_name(" MariA ", last_name="  LOPEZ  ", country="USA") # mixed arguments, positional first then keyword arguments
#clean_name(first_name=" MariA ","  LOPEZ  ", country="USA")
# main reason to mmix - primary values ,secondary values helps the context
#  primary values positional arguments, secondary values keyword arguments
# tip don't mix it .

# default parameters
#parameters that already have a values, if you don't pass anthing in python, python uses that value automatically.makes parameter optional

# default
clean_name(" john ", "  smith  ") # default parameter country="n/a" is used

# ================================================================================
# FUNCTION PARAMETERS & SCOPE
# ----------------------------------------
# Functions can accept inputs (parameters).
# These inputs allow the function to behave dynamically.
#
# We will explore:
# - Simple parameter usage
# - Global vs local variables
# - Positional arguments
# - Keyword arguments
# - Default parameters
# ================================================================================


# Adding Input
# We pass a name and clean it before printing.

def clean_name(name):
    print(name.strip().lower())

clean_name(" MariA ")   # -> maria
clean_name("KUMAR ")    # -> kumar
clean_name("")          # ->  (empty string remains empty)


# ---------------------------------------
# Parameters vs Global vs Local Variable
# ---------------------------------------
# Global variables exist outside the function.
# Local variables exist only inside the function.

case_rule = "n/a"  # Global variable

def clean_name(name):  # Parameter
    cleaned = name.strip()  # Local variable

    if case_rule == "lower":
        cleaned = cleaned.lower()

    print("Cleaned:", cleaned)

# print(name) -> Parameters can be accessed only inside functions
# print(cleaned) -> local variables can be accessed only inside functions
clean_name(" MariA ")
print("The Rule is:", case_rule)


# -----------------------------------------------------------
# Positional, Keyword, mixed Arguements | Default Parameters
# -----------------------------------------------------------
# Functions can accept multiple inputs.

def clean_name(first_name, last_name, country="n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "From", country)


# Positional Arguments (Access based on order)
clean_name(" MariA ", "SMITH ", "DE")

# Keyword Arguments (Access based on parameter name)
clean_name(country="DE", first_name=" MariA ", last_name="SMITH ")

# Mixed Arguments (Positional first, then keyword)
clean_name(" MariA ", "SMITH ", country="DE")

# Default Parameter (If country not provided, default is used.)
clean_name("Kumar", "Suresh")
