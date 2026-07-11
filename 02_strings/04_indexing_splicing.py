## Transformations
# hello
# positive 0,1,2,3,4 and negative index -5,-4,-3,-2,-1

#[start:end] # start included, end not included
# do not get character of end position,but the character before
# h 0,-5
# e 1,-4
# l 2,-3
# l 3,-2
# o 4,-1
# hello [0:5] # hello
# hello [0:3] # hel
# hello [0:4] # hell

# [1:] # ello
# [:4] # hell
# [1] # e

# [start:end:step] # step is optional, default step is 1,python will take every step character from start to end-1
# hello [0:4:2] # hl

text = "Python"

print(text[-6]) # -> P
print(text[-1]) # -> n

print(text[3]) # -> h

date = "2023-06-15"
print(date[0:4])  # -> 2023
print(date[:4])   # -> 2023

print(date[5:7])  # -> 06

print(date[8:])  # -> 15
print(date[8:10])  # -> 15
print(date[-2:])  # -> 15 , extract from end easier negative number

# ================================================================================
# STRING INDEXING & SLICING
# ----------------------------------------
# Strings are ordered sequences of characters.
# This means:
# - Each character has a position (index)
# - Indexing starts at 0
# - Negative indexing starts from the end
# ================================================================================

# ---------------------------------------
# Basic Indexing
# ---------------------------------------
# Access characters by position.

text = "Python"

print(text[0]) # -> P  (first character)
print(text[-6]) # -> P  (same as index 0)
print(text[5]) # -> n  (last character)
print(text[-1]) # -> n  (last character using negative index)
print(text[3]) # -> h

# ---------------------------------------
# Slicing
# ---------------------------------------
# Format: string[start:stop]
# Stop index is excluded.

date = "2026-09-20"

print(date[0:4]) # -> 2026  (year)
print(date[:4]) # -> 2026  (from start to index 4)
print(date[5:7]) # -> 09  (month)
print(date[8:]) # -> 20  (from index 8 to end)
print(date[-2:]) # -> 20  (last two characters)
