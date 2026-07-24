#sort,rearranging ,change order
letters = ['c', 'a', 'b']
letters.sort() # empty asorting order
print(letters)

letters.sort(reverse=True)
print(letters)

matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix.sort()
print(matrix)  # Sorts by first element of each row, if starts are the same ,the next item

#sort item in a row
matrix = [
    ['d', 'e', 'f'],  # Row 0
    ['a', 'z', 'i'],  # Row 1
    ['a', 'a', 'c']   # Row 2
]

matrix[1].sort()
print(matrix)  # Sorts by first element of each row, if starts are the same ,the next item

#temporary copy of the list sorted, a new list
letters = ['c', 'a', 'b']
new_lists = sorted(letters)
print('Original list:', letters)  # Original list remains unchanged
print('Sorted list:', new_lists)  # New sorted list

letters = ['c', 'a', 'b']
new_lists = sorted(letters, reverse=True)
print('Original list:', letters)
print('Sorted list:', new_lists)

# reversing list
# do not care about data ,flip the list around
letters = ['c', 'a', 'b']
letters.reverse()  # Reverses the list in place
print(letters)

letters = ['c', 'a', 'b']
# new_list = reversed(letters) # Returns an iterator that yields elements in reverse order, we need list
new_list = list(reversed(letters))
print('Original list:', letters)
print('Reversed list:', new_list)

# ================================================================================
# SORTING & REVERSING LISTS
# ----------------------------------------
# Python provides multiple ways to sort and reverse lists.
# Some methods modify the original list.
# Others return a new list without changing the original.
# ================================================================================

# ---------------------------------------
# sort() – Ascending
# ---------------------------------------
# sort() modifies the original list.

letters = ['c', 'a', 'b']
letters.sort()
print(letters)   # -> ['a', 'b', 'c']  (sorted ascending)


# ---------------------------------------
# sort() – Descending
# ---------------------------------------
# reverse=True sorts in descending order.

letters = ['c', 'a', 'b']
letters.sort(reverse=True)
print(letters)   # -> ['c', 'b', 'a']  (sorted descending)


# ---------------------------------------
# Sorting Nested Lists
# ---------------------------------------
# Lists are compared element by element.

matrix = [
    ['d', 'e', 'f'],
    ['a', 'z', 'i'],
    ['a', 'a', 'c']
]

matrix.sort()
print(matrix)


# ---------------------------------------
# Sorting Only One Row
# ---------------------------------------
# We can sort individual rows.

matrix = [
    ['d', 'e', 'f'],
    ['a', 'z', 'i'],
    ['a', 'a', 'c']
]

matrix[1].sort()
print(matrix)


# ---------------------------------------
# sorted() – Returns New List
# ---------------------------------------
# Does NOT modify the original list.

letters = ['c', 'a', 'b']

new_list = sorted(letters, reverse=True)
print('Original List:', letters)   # -> ['c', 'a', 'b']
print('Sorted List:', new_list)    # -> ['c', 'b', 'a']


# ---------------------------------------
# reversed() – Reverse Order
# ---------------------------------------
# reversed() returns an iterator.
# We convert it to list.

letters = ['c', 'a', 'b']

new_list = list(reversed(letters))
print('Original List:', letters)    # -> ['c', 'a', 'b']
print('Reversed List:', new_list)   # -> ['b', 'a', 'c']
