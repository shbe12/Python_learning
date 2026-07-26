# an outut from the function, so data goes outside the function , useing the keyword return
# transformation function- raw values to the function,data goes in,somthings happens to data, data comes out and return to the program in order to do something else with it
# if you want the result of your function to be reused in the program use return instead of print
# can return expression, variable,parameter,logic, another function
f = 2 # f is a global variable
def multiply_factor(x): # x is a parameter
    y = x * f      # y is a local variable
    return y # return local variable

z = multiply_factor(3) #store return value,whatever the function returns back is stores in this variable z
print(z) # print the return value stored in z

# if you do not specify return,still python send something back to the program. It sends None
# None is not a real values, something unknown,missing.

def clean_name(name): #parameter
    cleaned = name.strip().lower() # cleaned is a local variable
    return cleaned

# clean_name(" MariA ") # print the cleaned name, but it is not stored anywhere, so it cannot be reused in the program
cln_name = clean_name(" MariA ") # assign the function call to a variable to store the result
print(cln_name) # print the stored result, now it can be reused in the program

def clean_name(name): #parameter
    cleaned = name.strip().lower() # cleaned is a local variable
    # return cleaned # without the return we get None

# clean_name(" MariA ") # print the cleaned name, but it is not stored anywhere, so it cannot be reused in the program
cln_name = clean_name(" MariA ") # assign the function call to a variable to store the result
print(cln_name) # print the stored result, now it can be reused in the program

# function use multiple returns statements
def clean_name(name):
    cleaned = name.strip().lower()
    return cleaned

cln_name = clean_name("")
print(cln_name) # print empty string, because the function returned an empty string, not None

# if value empty, convert to None, otherwise clean it
# return multiple values separated by commas

def clean_name(name):
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
        return cleaned

cln_name = clean_name("")
print(cln_name) # print empty string, because the function returned an empty string, not None

print('-----------------------------')

# return multiple values separated by commas, they are returned as a tuple
def get_name():
    return "John", "Smith"

name = get_name() # returns a tuple with two values, first name and last name
print(name)

print('-----------------------------')

# return 2 numbers, store them in 2 variables, print them
def calculate():
    return 15, 8

a, b = calculate()

print(a)
print(b)

print('-----------------------------')

#returns multiple values, store them in 2 variables, print them
def clean_name(name):
    cleaned = name.strip().title()
    length = len(cleaned)

    return cleaned, length

name, letters = clean_name("   maria   ")

print(name)
print(letters)

print('-----------------------------')

#return the value in both upper and lower case

def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned

# cln_name = clean_name("   Maria   ")
# print(cln_name) # print the tuple with both lower and upper case values

lo_name, up_name = clean_name("   Maria   ")
print(lo_name)
print(up_name)

# no input/output, only input, input and output, multi-input/output
# ================================================================================
# RETURN STATEMENT
# ----------------------------------------
# The return statement sends a value back
# from a function.
#
# Unlike print(), return allows us to:
# - Store the result in a variable
# - Reuse it later
# - Pass it to other functions
# ================================================================================


# ---------------------------------------
# Multiple Returns
# ---------------------------------------
# If the input is empty, we return None.
# Otherwise, we clean the name and return it.

def clean_name(name):
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
        return cleaned

cln_name = clean_name(" MariA ")
print(cln_name)


# ---------------------------------------
# Returning Multiple Values
# ---------------------------------------
# A function can return more than one value.
# Python automatically packs them into a tuple.

def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned

lo_name, up_name = clean_name(" MariA ")

print(lo_name)
print(up_name)
