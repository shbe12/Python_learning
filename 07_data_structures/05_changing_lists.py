# adding,removing,updating lists
letters = ['a', 'b', 'c']
letters.append('x') #add to the end of the list
letters.append('y')
print(letters)

#specify position number, and value to insert
letters.insert(0,'x') #insert at index 0
print(letters)
letters.insert(3,'y') #insert at index 3
print(letters)

matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]
matrix.append(['j', 'k', 'l']) #add new row to the end of the matrix
print(matrix)
matrix.insert(0,['a', 'a', 'a'])
print(matrix)
# matrix.append('x')
matrix[1].append('x')
matrix[0].insert(0,'z')
print(matrix)


#removing elements from a list
#duplicate, bad ,old
#remove everything from the list
letters = ['a', 'b', 'c']
letters.clear() #remove all elements from the list
print(letters)
# remove by value, the first match
letters = ['a', 'b', 'a']
letters.remove('a') #remove first match of 'a'
letters.remove('a') # removes next a
print(letters)

#remove by position, pop defaults to the last item, pops removes and return
letters = ['a', 'b', 'c']
letters.pop() #remove last item
print(letters)
removed = letters.pop()
print('Removed Item:', removed)
print(letters)

matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]
# matrix.remove(['a', 'b', 'c']) #remove first match of the row
# print(matrix)
# matrix.pop() #remove last row
# print(matrix)
# matrix.remove('e') # error have to specify the row first, then remove the value
matrix [1].remove('e') #remove value from the row
matrix[-1].pop(0) #remove firstvalue from the row by index
matrix[0].pop() #remove last value from the row
print(matrix)

#updating values in a list

letters = ['a', 'b', 'c']
letters[0] = 'x' #update first value
print(letters)
# letters= 'z'
# print(type(letters)) #string

matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix[-1] = ['x', 'y', 'z'] #update last row
print(matrix)

matrix[0][0] = '-' #update first value in the first row
print(matrix)
matrix[1][1] = '-' #update middle value in the second row
print(matrix)

# ================================================================================
# MODIFYING LISTS (ADD • REMOVE • UPDATE)
# ----------------------------------------
# Lists are mutable.
# This means we can add, remove, and update elements.
# Python provides several built-in methods to do that.
# ================================================================================

# ================================================================================
# Adding Items to Lists
# ================================================================================

# ---------------------------------------
# append()
# ---------------------------------------
# Adds element to the end of the list.

letters = ['a', 'b', 'c']

letters.append('x')
letters.append('y')
print(letters)   # -> ['a', 'b', 'c', 'x', 'y']  (added at end)


# ---------------------------------------
# insert()
# ---------------------------------------
# Adds element at a specific index.

letters = ['a', 'b', 'c']

letters.insert(0, 'x')
letters.insert(3, 'y')
print(letters)   # -> ['x', 'a', 'b', 'y', 'c']


# ---------------------------------------
# Adding to Matrix
# ---------------------------------------
# Adding Rows to a Matrix

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix.append(['x', 'y', 'z'])
matrix.insert(0, ['a', 'a', 'a'])
print(matrix)


# Adding One Item to Matrix

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix[1].append('x')
matrix[0].insert(0, 'z')
print(matrix)


# ================================================================================
# Removing Items From Lists
# ================================================================================

# ---------------------------------------
# clear()
# ---------------------------------------
# Removes all elements.

letters = ['a', 'b', 'c']

letters.clear()
print(letters)   # -> []  (list is now empty)


# ---------------------------------------
# remove()
# ---------------------------------------
# Removes first occurrence of value.

letters = ['a', 'b', 'a']

letters.remove('a')
letters.remove('a')
print(letters)   # -> ['b']


# ---------------------------------------
# pop()
# ---------------------------------------
# Removes element by index and returns it.

letters = ['a', 'b', 'c']
removed = letters.pop(1)
print(letters)           # -> ['a', 'c']
print('Removed Item:', removed)   # -> b


# ---------------------------------------
# Removing Inside Nested Lists
# ---------------------------------------

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix[1].remove('e')   # remove specific value
matrix[-1].pop(0)       # remove by index
matrix[0].pop()         # remove last element
print(matrix)


# ================================================================================
# Updating Items in Lists
# ================================================================================

# Direct assignment changes values.

letters = ['a', 'b', 'c']

letters[0] = 'x'
letters[1] = 'y'
letters = 'z'   # variable now points to a string
print(letters)        # -> z
print(type(letters))  # -> <class 'str'>



# Updating Nested Lists

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix[-1] = ['x', 'y', 'z']   # replace entire row
matrix[0][0] = '-'             # update specific element
matrix[1][1] = '-'
matrix[-1][-1] = '-'
print(matrix)
