#can compare, copying or making a reference
#assignment ,referencing to the same data,change in one shows up in another
letters = ['a', 'b', 'c']
letters_copy = letters  # This creates a reference to the same list
letters.pop()
letters_copy.append('z')
print('Original:',letters)
print('Copy:', letters_copy)

# shallow copy,play with data without affecting original list
letters = ['a', 'b', 'c']
letters_copy = letters.copy() # a separate list in memory
letters.pop()
letters_copy.append('z')
print('Original:',letters)
print('Copy:', letters_copy)

#shallow copy top, level complete independent, deeper level children shared.
# only copy for the top level , shallow copy, change in deeper level aggect both original and copy

matrix = [
    ['a', 'b'], # row 0
    ['c', 'd'], # row 1
]

matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')  # This modifies the inner list of the copy
print('Original:', matrix)
print('Copy:   ', matrix_copy)

# deep copy , copy module , copy() , deepcopy() , copy all levels of data, changes in copy do not affect original
# for deepocopy copy everything, including nested objects, so that the original and the copy are completely independent of each other.
#  import module, funtion name deepcopy
# creates true independent copy for all levels, connection between copies and original values
import copy
matrix = [
    ['a', 'b'], # row 0
    ['c', 'd'], # row 1
]

matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')  # This modifies the inner list of the copy
print('Original:', matrix)
print('Copy:   ', matrix_copy)

#justcopy funtion isinde of copy module, only copy top level
#affects child
import copy
matrix = [
    ['a', 'b'], # row 0
    ['c', 'd'], # row 1
]

matrix_copy = copy.copy(matrix)
# matrix.pop()
matrix_copy[0].append('z')  # This modifies the inner list of the copy
print('Original:', matrix)
print('Copy:   ', matrix_copy)

import copy
original = [
    ['a', 'b'], # row 0
    ['c', 'd'], # row 1
]

#Assignment
copy1= original
print("Same object?",original is copy1,"\n")

#Shallow , # each value pointing to different object
# not sharing same object but deeply they are sharing the same list
copy2 = original.copy()
print("Same object?",original is copy2,"\n")
print("Shared Lists?", original[0] is copy2[0],"\n")

#deep copy
#not sharing same object , deeply not sharing same list
#python storing rows in different objects
copy3 = copy.deepcopy(original)
print("Same object?",original is copy3,"\n")
print("Shared Lists?", original[0] is copy3[0],"\n")

# use operator to see if they are refeenced to same object
# assignment is very confusing and risky
#method copy for simple list one dimension, no nesting, flat list
#deppcopy for nesting,matrix, dont eed any shared references.
# ================================================================================
# COPYING LISTS (REFERENCE • SHALLOW • DEEP)
# ----------------------------------------
# In Python, assigning a list to another variable
# does NOT create a new list.
#
# We must understand the difference between:
# - Assignment (reference)
# - Shallow copy
# - Deep copy
# ================================================================================


# ---------------------------------------
# Assignment (Reference Copy)
# ---------------------------------------
# Both variables point to the same object.

letters = ['a', 'b', 'c']

letters_copy = letters
letters_copy.append('z')

print('Original:', letters)      # -> ['a', 'b', 'c', 'z']
print('Copy:', letters_copy)     # -> ['a', 'b', 'c', 'z']
# Both changed (same memory reference)


# ---------------------------------------
# Shallow Copy with copy()
# ---------------------------------------
# Creates a new outer list.

letters = ['a', 'b', 'c']

letters_copy = letters.copy()
letters_copy.append('z')

print('Original:', letters)      # -> ['a', 'b', 'c']
print('Copy:', letters_copy)     # -> ['a', 'b', 'c', 'z']
# Only copy changed


# ---------------------------------------
# Shallow Copy with Nested Lists
# ---------------------------------------
# Inner lists are still shared.

matrix = [
    ['a', 'b'],   # Row 0
    ['c', 'd']    # Row 1
]

matrix_copy = matrix.copy()

matrix.pop()                     # remove last row
matrix_copy[0].append('z')       # modify inner list

print('Original:', matrix)
print('Copy:', matrix_copy)
# Inner list modified in both (shared reference)


# ---------------------------------------
# Deep Copy
# ---------------------------------------
# Deep copy duplicates everything,
# including inner lists.

import copy

matrix = [
    ['a', 'b'],  # Row 0
    ['c', 'd'],  # Row 1
]

matrix_copy = copy.deepcopy(matrix)

matrix.pop()
matrix_copy[0].append('z')

print('Original:', matrix)
print('Copy:', matrix_copy)

# Completely independent


# ---------------------------------------
# Identity Comparison
# ---------------------------------------
# Using "is" to check memory identity.

import copy

original = [
    ['a', 'b'],  # Row 0
    ['c', 'd'],  # Row 1
]

# Assignment
copy1 = original
print("Same Object?", original is copy1)        # -> True

# Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2)        # -> False
print("Shared Lists?", original[0] is copy2[0]) # -> True

# Deep Copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)        # -> False
print("Shared Lists?", original[0] is copy3[0]) # -> False
