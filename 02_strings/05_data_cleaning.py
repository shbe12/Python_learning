## cleaning
text = " Engineering".lstrip()
print(text)  # -> "Engineering" (leading whitespace removed)

text = "Engineering ".rstrip()
print(text)  # -> "Engineering" (trailing whitespace removed)

text = " Engineering ".strip()
print(text)  # -> "Engineering" (both leading and trailing whitespace removed)
# removes tabs and multiple spaces not within the string, but at the beginning and end of the string

text = "   Data Engineering   ".strip()
print(text)  # -> "Data Engineering" (leading and trailing whitespace removed)

text = "###Abc###".strip("#")
print(text)  # -> "Abc" (leading and trailing '#' characters removed)

text = " Engineering"
print(len(text))
print(len(text.strip()))  # -> 11 (length after removing leading whitespace,can see how many whites spaces are in the string )

print(len(text) == len(text.strip()))  # -> False (lengths are not equal, indicating leading whitespace was present)
nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print("Number of leading spaces:", nr_of_spaces)  # -> 1 (number of leading whitespace characters)
print("Is my data clean?", is_clean)  # -> False (string has leading whitespace)

# Case Conversions
text = "python PROGRAMMING"
print(text.lower())  # -> "python programming" (all characters to lowercase)
print(text.upper())  # -> "PYTHON PROGRAMMING" (all characters to uppercase

# search = "Email"
# data = "email"

# print(search == data)  # -> False (case-sensitive comparison)

# search = "Email ".lower()
# data = " eMAil".lower()

# print(search == data) # false (case-insensitive comparison after converting both to lowercase)


search = "Email ".lower().strip()
data = " eMAil".lower().strip()

print(search == data)

# ================================================================================
# WHITESPACE CLEANUP & CASE NORMALIZATION
# ----------------------------------------
# In real-world data, text is often messy.
# We need to:
# - Remove extra spaces
# - Normalize case (lower / upper)
#
# These operations are essential in data cleaning.
# ================================================================================


# ---------------------------------------
# Whitespace Cleanup
# ---------------------------------------
# lstrip()  → remove spaces from the left
# rstrip()  → remove spaces from the right
# strip()   → remove spaces from both sides

text = " Engineering".lstrip()
print(text) # -> Engineering

text = "Engineering ".rstrip()
print(text) # -> Engineering

text = "  Engineering ".strip()
print(text) # -> Engineering

text = "Data Engineering".strip()
print(text) # -> Data Engineering

# strip() can also remove specific characters.
text = "###Abc###".strip("#")
print(text) # -> Abc

# ---------------------------------------
# Case Conversion
# ---------------------------------------
# lower() → convert to lowercase
# upper() → convert to uppercase

text = "python PROGRAMMING"

print(text.lower()) # -> python programming
print(text.upper()) # -> PYTHON PROGRAMMING

# ---------------------------------------
# Why Normalization Matters
# ---------------------------------------
# When comparing user input, always normalize first.

search = "Email ".lower().strip()
data = " emAil".lower().strip()

print(search == data) # -> True
