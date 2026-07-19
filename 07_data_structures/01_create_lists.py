   # data structure a way of organizing and storing data so it can be used efficiently
   # 4 built in data structure in python: list, tuple, set, dictionary
#list collection of items in a particular order, can be changed, allows duplicate members
# tuple collection of items in a particular order, cannot be changed, allows duplicate members
#set collection of items in no particular order, cannot be changed, no duplicate members
# dictionary collection of items in a particular order, can be changed, no duplicate members
#list -brackets, tuple - parentheses, set - curly braces, dictionary - curly braces with key value pairs
#function vs methods meyhod no output , function output, method is a function that is associated with an object
# list methods
# ordered collection of items,changeable , allows duplicate members
# H ow to create a list
empty = []
print (empty)
print (type(empty))

empty = []
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
mixed = ['1', 2, 3.0, True]
print (numbers)
print (type(numbers))
print (letters)
print (type(letters))
print (mixed)
print (type(mixed))

empty = list()
print(empty)

letters = 'Python'
print(letters)

letters = list('Python')
print(letters)

numbers = list(range(5))
print(numbers)

#nested lists

empty = []
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
mixed = ['1', 'a', True, None]

matrix = [['a','b','c'],
          ['d','e','f']]

mixed_matrix = [['a','b'],
          [1,2,3],
          [True]]
print(matrix)
print(type(matrix))

print(mixed_matrix)
print(type(mixed_matrix))

# empty list bracket nothing inside or function list without specifying  , x = list (), in order to create and plan
#manual creation
# nested or matrix list is a list inside a list, can be used to represent 2D data, can be used to represent a table of data
# create by converting to list "cat" to list ['c', 'a', 't']
# ================================================================================
# CREATING LISTS
# ----------------------------------------
# Lists are ordered, mutable collections in Python.
# They can store multiple values inside square brackets [].
# Lists can contain any data type, even mixed types.
# ================================================================================


# ---------------------------------------
# Empty Lists
# ---------------------------------------
# There are two common ways to create an empty list.

empty1 = []
print(empty1)

empty2 = list()
print(empty2)

# ---------------------------------------
# Creating a List from a String
# ---------------------------------------
# The list() function splits the string into individual characters.

letters = list('Python')
print(letters)


# ---------------------------------------
# Creating a List from range()
# ---------------------------------------
# range() generates numbers. list() converts them into a list.

numbers = list(range(5))
print(numbers)


# ---------------------------------------
# Nested List (Matrix)
# ---------------------------------------
# A list can contain other lists. This is commonly called a matrix.

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f']
]

print(matrix)
print(type(matrix))


# ---------------------------------------
# Mixed Data Types
# ---------------------------------------

mixed_matrix = [
    ['a', 'b'],
    [1, 2, 3],
    [True]
]

print(mixed_matrix)
