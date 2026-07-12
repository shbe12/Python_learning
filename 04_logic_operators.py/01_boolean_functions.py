#control flow
#conditional statements, loops,
#control flow statements tools,- conditional statements, loops,
# control flow boolean expressions- values,functions,comparison operators, logical operator,,membership operators and identity operatord
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("Hi")) # true we have a value
print(bool()) # false we have no value
print(bool(0)) # false considered as nothing no quantity
print(bool("")) #false blank empty
None # there is no value, it is not a boolean value, it is a special value that represents the absence of a value
print(bool(None)) # false , in order to check if  function has real value inside
#functions
#any , if one of the value is true then it will return true
#all every value should be true then it will return true

email = ""
phone = "0176-123456"
username = ""

#allow,if any field is filled

print(any([email, phone, username])) # true because phone is filled

#allow,if all field is filled
print(all([email, phone, username])) # false because email and username are empty

print(isinstance(123, int))
print(isinstance(True, str))

print("Hello".endswith("o")) # true
print("Hello".startswith("o")) # false

# ================================================================================
# BOOLEAN VALUES
# ----------------------------------------
# Booleans are either True or False. They're often used for logic, conditions,
# validations, and control flow. Python also allows checking "truthiness" of values.
# ================================================================================

# ---------------------------------------
# Basic Boolean Values
# ---------------------------------------
print(True)         # ➜ True
print(False)        # ➜ False
print(type(True))   # ➜ <class 'bool'>

# ---------------------------------------
# bool() Function: Truthiness of Values
# ---------------------------------------
print(bool(123))     # ➜ True  (non-zero number)
print(bool("Hi"))    # ➜ True  (non-empty string)

print(bool(()))      # ➜ False (empty tuple)
print(bool(0))       # ➜ False (zero)
print(bool(""))      # ➜ False (empty string)
print(bool(None))    # ➜ False (None is always considered False)

# ---------------------------------------
# Using any() and all() for Field Validation
# ---------------------------------------
email    = ""
phone    = "017-1234"
username = "baraa123"

# Allows registration if at least one field is filled
print(any([email, phone, username]))  # ➜ True

# Allows registration only if all fields are filled
print(all([email, phone, username]))  # ➜ False

# ---------------------------------------
# Type Checking with isinstance()
# ---------------------------------------
print(isinstance(123, int))     # ➜ True
print(isinstance(True, str))    # ➜ False

# ---------------------------------------
# String Start/End Checks
# ---------------------------------------
print("Hello".endswith("o"))    # ➜ True
print("Hello".startswith("o"))  # ➜ False
