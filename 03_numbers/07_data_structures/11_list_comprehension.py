#List Comprehension
#Data transformation
#loop
#filter
# p*2 p for pices if p>50
#inside loop first filter, then data transformation,then back to start of loop, if condtiotion not met not tranformed
#filter is optional, python will iterate through all item
domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.DATAWITHBARAA.COM']
# normalize and tranform to standard format
cleaned = [
    d.lower().replace('www.', '')  # Data transformation
    for d in domains
    if '.' in d # Data filtering
]

print(cleaned)

cleaned = [
    d.lower().replace('www.', '')  # Data transformation
    for d in domains
]

print(cleaned)

# filter data without changing values
cleaned = [
    d
    for d in domains
    if '.' in d
]

print(cleaned)

# ================================================================================
# LIST COMPREHENSIONS
# ----------------------------------------
# List comprehension allows us to create lists
# in a clean and compact way.
#
# It combines:
# - Iteration
# - Optional filtering
# - Optional transformation
# In a single readable expression.
# ================================================================================



# Task:
# 1. Keep only valid domains (must contain a dot)
# 2. Convert everything to lowercase

domains = [
    'www.google.com',
    'openai.com',
    'localhost',
    'WWW.DATAWITHBARAA.COM'
]
# one line -> cleaned = [d.lower() for d in domains if '.' in d]

cleaned = [
    d.lower()
    for d in domains
    if '.' in d
]
-
print(cleaned)

#indexing  using parantehesis and specifying the index of the item in the list
#  slicing get multiple items , start and end
#unpacking split items to multiple variables to hold their values

#max() , min(), len(), all() , any(), .count, .index, in ,
# .append(),.insert(), .remove(),.clear(), .pop()
#.sort(), .reverse(),
# assignment,.copy(), deepcopy()
# +, .extend(), .zip(), enumerate(), map(), filter()
#comprehension =filet + tranformation/map
