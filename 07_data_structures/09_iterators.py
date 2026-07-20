#iterables and iterators
#iterators do not store everything in memory produce values
# enumerate,reversed,zip,chain,filter,map,iter,range,sorted,zip
#1. in order to build loop
#2. in order to save memory
#3.speed and flexibility, data pipeline
#iterator t,an oject that can helpus to iteration
#proceesing machine
#iterable is the thing you can loop over, a list, sting value
# use iteration to tranform data
letters = ['a','b','c']
new_list = []
for l in letters:
    # print(l)
    new_list.append(l.upper())
    # print(l.upper())
    print(new_list)

#iterator examples
#enumrate accepts an iterable and returns an iterator that produces tuples containing the index and the value from the iterable.
#enumerate to find exact positionn of data in list
# letters = ['a','b','c']
letters = ['a','','c']
# print(enumerate(letters))
# print(list(enumerate(letters)))
print(list(enumerate(letters, start=1)))
for index, value in enumerate(letters):
    print(index,value)

# iterator that flips data order
letters = ['a','b','c']
# print(reversed(letters))
# print(list(reversed(letters)))
for l in reversed(letters):
    print(l)

# iterator that combines 2 or more sequences
letters = ['a','b','c']
numbers = [1,2,3]
# print(zip(letters,numbers))
# print(list(zip(letters,numbers)))
for l,n in zip(letters,numbers):
    print(l,n)

#map function
# you give the function you want to repeat for each item and the iterable, you get your list after transformation
#the output an object called map
letters = ['a','b','c']
# print(map(str.upper, letters))
print(list(map(str.upper, letters)))

numbers = ['1','2','3']
# print(map(int, numbers))
print(list(map(int, numbers)))

names = ['John', 'Jane ', ' Joe']
print(list(map(str.strip, names)))


names2 = ['John', 'Jane ', ' Joe']
# print(list(map(int, names2)))
for n in map(str.strip, names2):
    print(n)

# filter function
#specifies the rule how to filter data, needs funtion and iterable
letters = ['a','','b',None,'c',False] #remove falsy values
# filter(None, letters) # if you use none and the filter , python removes the falsy data, not only the None,but the empty and the false
print(list(filter(None, letters)))
print(list(filter(bool, letters))) # just keep the list of true values

#only letters
items = ['sql','123','python','42']
# print(list(filter(str.isalpha,items))) # only keep the items that are letters
for i in filter(str.isalpha,items):
    print(i)

# iterable,the cotainer,the data structure itself,like list
# iterator the process, the machine that is going to produce the next items
#function map, give it the data transformation,the function and your list,data.
#filter, rule,expection and data should be filter
# ================================================================================
# ITERATION TOOLS (ENUMERATE • REVERSED • ZIP • MAP • FILTER)
# ----------------------------------------
# Python gives us powerful tools to work with iterables.
# Instead of writing everything manually,
# we can transform, combine, and filter data more efficiently.
# ================================================================================


# ---------------------------------------
# Basic Iteration with Transformation
# ---------------------------------------

# Convert letters to uppercase manually
letters = ['a', 'b', 'c']
new_list = []

for l in letters:
    new_list.append(l.upper())
    print(new_list)

# ---------------------------------------
# enumerate()
# ---------------------------------------

# Get index and value together
letters = ['a', '', 'c']

for index, value in enumerate(letters):
    print(index, value)

# ---------------------------------------
# reversed()
# ---------------------------------------

# Iterate from the end to the beginning
letters = ['a', 'b', 'c']

for l in reversed(letters):
    print(l)

# ---------------------------------------
# zip()
# ---------------------------------------

# Combine two related lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

for l, n in zip(letters, numbers):
    print(l, n)

# ---------------------------------------
# map()
# ---------------------------------------

# Convert letters to uppercase automatically
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))

# Convert string numbers to integers
numbers = ['1', '2', '3']
print(list(map(int, numbers)))

# Clean extra spaces from names
names = [' Maria ', ' John ', ' Kumar']

for n in map(str.strip, names):
    print(n)

# ---------------------------------------
# filter()
# ---------------------------------------

# Remove falsy values
letters = ['a', '', 'b', None, 'c', False]
print(list(filter(bool, letters)))


# Task: Keep only alphabetic values
items = ['sql', '123', 'python', '42']

for i in filter(str.isalpha, items):
    print(i)
