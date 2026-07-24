# Data Structures Behavior
# ----------------------------------------
# Python provides multiple built-in collection types.
# 4 types of data structures in python
# list, tuple, set, dictionary
# Each one has different behavior regarding:
# - Ordered
# - Mutable
# - Duplicates
# - Indexed
# ================================================================================


# ---------------------------------------
# List
# ---------------------------------------
# Lists are: Ordered, Mutable, Allow duplicates, Indexed
# list in python stored in like an array , each item seated next to each other in memory,python can access any value using index number, mainstains same order
my_list = [10, 30, 20, 10] # allows duplicates
print(my_list) # ordered
print(my_list[1]) #  indexed- can acess value using position numebr
my_list[3] =40 # mutable-can change and update values
print(my_list)

# when storing data base info if list is used anything inside your code might change those values might lose connection to the database
# use tuple ordered collection that cannot change after creation, locked for safety reason
# protect data
# ---------------------------------------
# Tuple
# ---------------------------------------
# Tuples are: Ordered, Immutable, Allow duplicates, Indexed

my_tuple = (10, 30, 20, 10) # allows duplicates
print(my_tuple) # ordered
print(my_tuple[1]) #  indexed- can acess value using position/index number
# my_tuple[3] = 40 # immutable- cannot change and update values
# my_tuple.remove(10) # immutable- cannot change and update values
# my_tuple.pop() # immutable- cannot change and update values
print(sorted(my_tuple)) # the output is a list because tuple is immutable and cannot be changed, so it returns a new list with sorted values


# when cheking data see customers id apperaing twice, data not clean, remove duplicates, tokeep data unique use sets
# unordered collection of unique values, no duplicates, no indexing, no order, cannot access values using index number
# ---------------------------------------
# Set
# ---------------------------------------
# Sets are: Unordered, Mutable, Unique values only, Not indexed
# items placed based on hashed values, not by index , after set created mo chance to understand order of items,
# hash values for speed, Python can if a value exist fast, with hash values
my_set = {10, 30, 20, 10}
print(my_set) # unordered, unique values only, python do not sort data eithere
#print(my_set[1]) # no index number, cannot use hash , it is internally for python, not to access specific value
my_set.remove(20) # mutable- can change and update values
print(my_set)

# ---------------------------------------
# Dictionary
# ---------------------------------------
# Dictionaries are: Ordered (Python 3.7+), Mutable, Keys are unique, Accessed by key

my_dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a': 40   # Duplicate key overrides previous
}

print(my_dict)       # -> {'a': 40, 'b': 20, 'c': 20}
print(my_dict['b'])  # -> 20  (key-based access)
my_dict['c'] = 80    # Update value
print(my_dict)       # -> {'a': 40, 'b': 20, 'c': 80}
