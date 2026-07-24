#how to explore and analyze data in our list
#max(),min(),sum(),len() are some of the functions that can be used to analyze data in a list
# all(),any()), completeness uniqueness
#count,index, for search and count
#true or false, to check if a value is present in the list
#comparison operators, to compare values in the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Max:", max(numbers))  # -> 10
print("Min:", min(numbers))  # -> 1
print("Sum:", sum(numbers))  # -> 55 #  would not work if stings values were in list
print("Length:", len(numbers))  # -> 10

#All and Any functions
print("All:", all(numbers))  # -> True (all values are non-zero)
print("All:", all([1, 0, 2])) # -> False (0 is considered False)
print("All:", all(['a','','b']))  # -> false ('' is considered False)
print("All:", all(['a','c','b']))

print("Any:", any(numbers))  # -> True (at least one value is non-zero)
print("Any:", any([1, 0, 2])) # -> True (1 is considered True)
print("Any:", any(['a','','b']))  # -> True (at least one non-empty string is considered True)
print("Any:", any(['0','0','0']))  # -> False (all strings are considered False)


# count and index functions
print("Count:", numbers.count(5))  # -> 1 (5 appears once)
print("Index:", numbers.index(5))  # -> 4 (5 is at index 4), function for first occurence of value in list

#in and is operators

numbers = [1, 5, 5, 4, 3]

print(4 in numbers)
print(8 not in numbers)

list1 = [1, 5, 5, 4, 3]
list2 = [1,2,3]
print(list1 == list2)

#first elements compared then next elements
list1 = [1,2,3]
list2 = [5,2,3]
print(list1 < list2)

list1 = [5,8,3]
list2 = [5,8,3]
print(list1 is list2) #do not check values but same memory address
print(list1 == list2)

# ================================================================================
# EXPLORING & ANALYZING LISTS
# ----------------------------------------
# Python provides many built-in functions to analyze lists.
# These help us inspect values, check conditions,
# and compare lists efficiently.
# ================================================================================


# ---------------------------------------
# Basic Analysis Functions
# ---------------------------------------

numbers = [1, 5, 5, 4, 3]

print("Max:", max(numbers))        # -> 5  (largest value)
print("Min:", min(numbers))        # -> 1  (smallest value)
print("Sum:", sum(numbers))        # -> 18 (total of elements)
print("Length:", len(numbers))     # -> 5  (number of elements)


# ---------------------------------------
# all()
# ---------------------------------------
# Returns True if all elements are truthy.

print("All:", all(numbers))            # -> True  (no zero values)
print("All:", all([1, 0, 2]))          # -> False (0 is falsy)
print("All:", all(['a', '', 'b']))     # -> False (empty string is falsy)
print("All:", all(['a', 'c', 'b']))    # -> True  (all non-empty)

# ---------------------------------------
# any()
# ---------------------------------------
# Returns True if at least one element is truthy.

print("Any:", any(numbers))            # -> True  (non-zero values exist)
print("Any:", any([1, 0, 2]))          # -> True  (1 and 2 are truthy)
print("Any:", any(['a', '', 'b']))     # -> True  (non-empty string exists)
print("Any:", any([0, 0, 0]))          # -> False (all values are falsy)

# ---------------------------------------
# count() and index()
# ---------------------------------------

print("Count:", numbers.count(5))   # -> 2  (5 appears twice)
print("Index:", numbers.index(5))   # -> 1  (first occurrence position)

# ---------------------------------------
# Membership Operators
# ---------------------------------------

print(8 in numbers)        # -> False
print(8 not in numbers)    # -> True

# ---------------------------------------
# Equality Comparison
# ---------------------------------------
# == compares values.

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]

print(list1 == list2)      # -> False (different length)

# ---------------------------------------
# Lexicographical Comparison
# ---------------------------------------
# Lists are compared element by element.

list1 = [1, 2, 3]
list2 = [5, 2, 3]

print(list1 < list2)       # -> True (1 < 5)


# ---------------------------------------
# Identity Comparison
# ---------------------------------------
# is checks memory identity, not value.

list1 = [5, 8, 3]
list2 = [5, 8, 3]

print(list1 is list2)      # -> False (different objects in memory)
# ================================================================================
