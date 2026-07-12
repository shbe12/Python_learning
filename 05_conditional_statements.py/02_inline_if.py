#ternary operator, inline if, conditional expression
# syntax: value_if_true if condition else value_if_false
# "A" if score >= 90 else "F"
#must iclude both if and else,cannot use elif, cannot use without else, cannot use without if, cannot use without condition, cannot use without value_if_true and value_if_false, cannot use without colon, cannot use without parentheses, cannot use without indentation, cannot use without line break, cannot use without whitespace, cannot use without comments, cannot use without docstring, cannot use without function, cannot use without class, cannot use without module, cannot use without package, cannot use without import statement, cannot use without from statement, cannot use without as statement, cannot use without try statement, cannot use without except statement, cannot use without finally statement, cannot use without raise statement, cannot use without assert statement, cannot use without with statement, cannot use without yield statement, cannot use without return statement
# can be store in variable

score = 100
if score >= 90:
    print("A")
else:
    print("F")

print("A" if score >= 90 else "F")

grade = "A" if score >= 90 else "F"
print(grade)


score = 90
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)

# ================================================================================
# INLINE CONDITIONAL EXPRESSION (TERNARY OPERATOR)
# ----------------------------------------
# Python allows writing simple if-else logic
# in a single line.
#
# Syntax:
# value_if_true if condition else value_if_false
# ================================================================================


# ---------------------------------------
# Standard If-Else (Multi-line)
# ---------------------------------------
score = 50

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"

print(grade) # -> F

# ---------------------------------------
# Inline Version (Single Line)
# ---------------------------------------
# Same logic, written more compactly.

score = 50

grade = "A" if score >= 90 else "B" if score >= 80 else "F"

print(grade) # -> F


# Decide user access level.
is_admin = True

access_level = "Full Access" if is_admin else "Limited Access"

print(access_level) # -> Full Access


# Discount Eligibility
cart_total = 120

discount_status = "Discount Applied" if cart_total >= 100 else "No Discount"

print(discount_status) # -> Discount Applied
