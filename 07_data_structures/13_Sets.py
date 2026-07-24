#Set speacial methods and operators
a = {10, 20, 30, 40}
# How to add values to sets
a.add(50) #add item somewhere in set,only if value does not exist, if it exists it will not be added
print(a)
# add multiple values to set , merges another group values (iteraple) into the set
# a.update("Hi")
# a.update({1,2})
# print(a)
# use operators as a shortcut instead of using the method name
a |= {1, 2} # union operator, adds values to set, like update
print(a)
#remove by value
a.remove(10)
print(a)
# if you try to remove a value that is not part of the set
#a.remove(100) # will throw an error
# a python savior in order to remove values, remove items if it exists and does nothing if not
a.discard(100) # will not throw an error
print(a)
a.pop() # removes a random value from the set, since set is unordered, you cannot specify which value to remove
print(a)

#set math operations
# overlapping values between two sets
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
#Math operations
print(a.union(b)) # union returns a new set with all unique values from both sets
#not changing original sets, does not show values twice even if it is in both sets, or is shown twice in one set, only unique values are shown
print(a | b) # union operator, also returns a new set with all unique values from both

#returns only shared items
print(a.intersection(b)) # intersection returns a new set with only the values that are in both sets
print(a & b) # intersection operator, also returns a new set with only the values that

# only items in a but not in b
print(a.difference(b)) # difference returns a new set with only the values that are in a but not in b
print(a - b) # difference operator, also returns a new set
print(b - a) # difference operator, also returns a new set

# values not overlapping at all, non-shared values
print(a.symmetric_difference(b)) # symmetric difference returns a new set with only the values that are in a or b but not in both
print(a ^ b) # symmetric difference operator, also

# set relationships
# not creating anything new just ask questions and getting false or true
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a.issubset(b)) # returns True if all values in a are also in b, otherwise False
print(b.issubset(a)) # returns True if all values in b are also in a, otherwise False
print(a.issuperset(b)) # returns True if all values in b are also in a, otherwise False
#customers and vip customers

# do two sets share any items
#is the sets are completely separated so zero values is true
print(a.isdisjoint(b)) # returns True if the two sets have no elements in common, otherwise False
#
# ================================================================================
# SETS (UNIQUE • MATHEMATICAL OPERATIONS • RELATIONSHIPS)
# ----------------------------------------
# Sets are:
# - Unordered
# - Mutable
# - Unique values only
# - Not indexed
# ================================================================================


# ---------------------------------------
# Basic Set Behavior
# ---------------------------------------
my_set = {10, 30, 20, 10}
print(my_set)       # -> {10, 20, 30}  (duplicates removed)
# print(my_set[1])  # ❌ Error (not indexed)
my_set.remove(20)   # Remove specific value
print(my_set)       # -> {10, 30}


# ---------------------------------------
# Basic Set Operations
# ---------------------------------------
a = {10, 20, 30, 40}
a.add(50)       # Add one value
a |= {1, 2}     # Add multiple values (union assignment)
a.discard(100)  # Safe remove (no error if not found)
print(a)

# ---------------------------------------
# Mathematical Operations
# ---------------------------------------
# Sets support mathematical set theory operations.

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}


# Union (combine all unique elements)
print(a.union(b))   # -> {10, 20, 30, 40, 50, 60}
print(a | b)        # Same as union

# Intersection (common elements)
print(a.intersection(b))   # -> {30, 40}
print(a & b)               # Same as intersection

# Difference (elements in a but not in b)
print(a.difference(b))   # -> {10, 20}
print(a - b)             # Same as above
print(b - a)             # -> {50, 60}

# Symmetric Difference (elements in either but not both)
print(a.symmetric_difference(b))   # -> {10, 20, 50, 60}
print(a ^ b)                       # Same as above


# ---------------------------------------
# Relationship Operations
# ---------------------------------------
# Check subset, superset, and disjoint relationships.

a = {10, 20}
b = {30, 40, 50, 60}

print(a.issubset(b))     # -> False  (a not fully inside b)
print(b.issuperset(a))   # -> False  (b does not contain 10, 20)

print(a.isdisjoint(b))   # -> True   (no common elements)
