# if
# one single condition
score = 100
if score >= 90:
    print("A")

# indentation is important in Python to define the scope of the block of code
# indentaion part of rule and syntax
score = 50
if score >= 90:
    print("A")

#else
#else comes at end ,optional, cannot standalone, only one else block is allowed, no condition is needed for else block
score = 50
if score >= 90:
    print("A")
else:
    print("F")

score = 95
if score >= 90:
    print("A")
else:
    print("F")

#Elif is the first result was false, then check the next condition, and so on, until one of the conditions is true, or else block is executed if all conditions are false. Elif can be used multiple times, but only one else block is allowed at the end.

#else fallback or backup, if all conditions are false, then else block is executed, if no else block is provided, then nothing is executed if all conditions are false.
#elif comes after if , multiple elif allowed, needs codition, optional, cannot standalone, cannot be used without if block, can be used with else block, but not required, can be used without else block, but not required, can be used with multiple elif blocks, but only one else block is allowed at the end.

score = 95
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

# nested if, another false condition inside the first if block, can be used to check multiple conditions, but can make the code less readable, so use with caution, can be used with else and elif blocks, but not required, can be used without else and elif blocks, but not required, can be used with multiple nested if blocks, but can make the code less readable.
score = 67
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# logical operators can be used to combine multiple conditions in if statements, and can be used with else and elif blocks, but not required, can be used without else and elif blocks, but not required, can be used with multiple logical operators, but can make the code less readable.

score = 92
submitted_project = False
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 100
submitted_project = False
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 100
submitted_project = True
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 50
submitted_project = False
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60  or submitted_project:
    print("D")
else:
    print("F")

#independent if statement
#question completely outside the scope of the first if statement, can be used to check multiple conditions, but can make the code less readable, so use with caution, can be used with else and elif blocks, but not required, can be used without else and elif blocks, but not required, can be used with multiple independent if statements, but can make the code less readable.

score = 50
submitted_project = False

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("Project submitted")
else:
    print("Project is not submitted")

# ================================================================================
# CONDITIONAL STATEMENTS (IF / ELSE / ELIF)
# ----------------------------------------
# Python uses `if`, `elif`, and `else` to control the flow of decisions.
# You can nest conditions or combine them using logical operators.
# ================================================================================

# ---------------------------------------
# Simple If Condition
# ---------------------------------------
score = 100
if score >= 90:
    print("A")

# ---------------------------------------
# If / Else
# ---------------------------------------
score = 50
if score >= 90:
    print("A")
else:
    print("F")

# ---------------------------------------
# If / Elif / Else
# ---------------------------------------
score = 50
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

# ---------------------------------------
# Full Grading Logic with Multiple Elif
# ---------------------------------------
score = 50
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# ---------------------------------------
# Nested If: Project Bonus
# ---------------------------------------
score = 50
submitted_project = True

if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# ---------------------------------------
# Combined Conditions with and/or
# ---------------------------------------
score = 50
submitted_project = True

if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")

# ---------------------------------------
# Independent Conditions
# ---------------------------------------
score = 50
submitted_project = True

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")
