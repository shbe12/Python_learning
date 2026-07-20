#lambda
#custom logic annymous  function,data structure functions
# result= lambda input:expression
# variable multiple is holding a formula, when used we specify value
multiple = lambda x: x*2
print(multiple(2))

#2 inputs
add = lambda x, y: x + y
print(add(1,2))

#contain expressions, including condition
check = lambda i: i in "python"
print(check('z'))

#previously map(function,iterable)
#map(lambda,iterable)
#price in string values , convert from string to float
prices = ['$12.50', '$9.99', '$100.00']
p = '$12.50'
print(list(map(lambda p: float(p.replace('$','')), prices)))
# map(lambda p: float(p.replace('$','')) # 3. map the function to iterator to manipulate my data
# (lambda p: float(p.replace('$','')) # 2. put it in lambda
# print(float(p.replace('$',''))) # 1.data transformation
#print(p.replace('$',''))
# print(type(float(p.replace('$',''))))

#lambda + filter
#reove prices lower than 100
prices = [120, 30, 300,80]
# p >= 100 # filter logic
# lambda p: p >= 100 # in lambda
# (filter(lambda p: p >= 100, prices)) #filter to apply the function to filter all your data in list
# list(filter(lambda p: p >= 100, prices))
print(list(filter(lambda p: p >= 100, prices)))


#kee only students with scores higher than 70
students = [['Maria',90], # row 0
            ['Kumar',90], # row 1
            ['Max',60]] # row 2

print(list(filter(lambda row: row[1] > 70, students)))
# lambda row: row[1] > 70 # check the score of each student
# students [0][1] > 70 # check the score of first student
# print(students [2][1] > 70)

#keep only students with names starting with M
students = [['Maria',85], # row 0
            ['Kumar',90], # row 1
            ['Max',60]] # row 2

# print(students[1][0].startswith('M')) # check the name of the second student
# lambda row: row[0].startswith('M') # check the name of each student
# filter(lambda row: row[0].startswith('M')
# filter(lambda row: row[0].startswith('M'),students) # filter to apply the function to filter all your data in list
print(list(filter(lambda row: row[0].startswith('M'),students)))
#create quick and custom logic
#one line function
#assist others: map(lambda), filter(lambda), sorted(lambda), reduce(lambda)
#add dynamic and flexibility

# ================================================================================
# LAMBDA FUNCTIONS
# ----------------------------------------
# A lambda function is a small anonymous function.
# It is useful when we need a quick function
# without formally defining it using def.
# ================================================================================


# ---------------------------------------
# Basic Lambda Examples
# ---------------------------------------

# Multiply a number by 2
# We create a short function in one line.

multiple = lambda x: x * 2
print(multiple(2))

# Add two numbers
add = lambda x, y: x + y
print(add(1, 2))

# Check membership in a string
check = lambda i: i in "python"
print(check('z'))

# Convert price string to float
prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))

# ---------------------------------------
# Lambda with filter() & sorted ()
# ---------------------------------------

# Example 6: Keep only prices >= 100
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))

students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]
# Keep students with score > 70
print(list(filter(lambda row: row[1] > 70, students)))

# Keep only students with names starting with 'M'
print(list(filter(lambda row: row[0].startswith('M'), students)))

# Sort students by their scores (ascending)
print(sorted(students, key=lambda row: row[1]))



# Go over
# Step 1: What does sorted() normally do?

# Without a key:

# print(sorted(students))

# Python compares the entire lists.

# It first compares:

# "John"
# "Maria"
# "Ali"

# because those are the first elements.

# Result:

# [
#     ["Ali", 95],
#     ["John", 90],
#     ["Maria", 85]
# ]

# It sorted alphabetically by the names.

# Step 2: What is key?

# key is a parameter of the built-in sorted() function.

# You didn't invent it.

# Python already defines sorted() like this (simplified):

# sorted(iterable, key=None, reverse=False)

# So you can pass:

# the list to sort
# an optional key
# an optional reverse
# What does the key do?

# The key tells Python:

# "Before comparing two items, extract this value from each item."

# Instead of comparing

# ["John", 90]

# Python compares

# 90

# because the key returns the second element.

# Step 3: What does this lambda do?
# lambda row: row[1]

# means

# Take each row
# Return row[1]

# Let's apply it.

# First row:

# ["John", 90]

# returns

# 90

# Second row:

# ["Maria", 85]

# returns

# 85

# Third row:

# ["Ali", 95]

# returns

# 95

# Python sorts using

# 90
# 85
# 95

# instead of

# John
# Maria
# Ali
# Step 4: The result
# students = [
#     ["John", 90],
#     ["Maria", 85],
#     ["Ali", 95]
# ]

# becomes

# [
#     ["Maria", 85],
#     ["John", 90],
#     ["Ali", 95]
# ]

# because

# 85 < 90 < 95
