# create packing, unpacking
#use case ,list of personal information each item diffrent variables and operations
person = ['John', 30, 'Engineer', 'England']
# name = person[0]
# age = person[1]
# profession = person[2]
# country = person[3]

#order of variable must match list
name, age , profession, country = person
print(name)
print(age)

#unpacking asterisk,left over details will be stored in a list
person = ['John', 30, 'Engineer','Worchester', 'England']
# person = [1,'John', 30, 'Engineer','Worchester', 'England']
name, *details, country = person
print(name)
print(details)
print(country)

name, *details = person
print(name)
print(details)

*details, country = person
print(details)
print(country)

# rules of using unpacking
# 1. number of variables must match the number of values in the list
#you can unpact any sequence lists tuples, strings, sets, dictionaries

number = [1, 2, 3, 4]
first, *middle, fourth = number
first,*rest = number
print(first)
print(rest)

greet= "Hello"
first, *middle, last = greet
print(first)

#underscore in space you do not need the values, not extracting
person = ['John', 30, 'Engineer','Worchester', 'England']

name, _, profession, _ , country = person
print(name)
print(profession)

#asterics and underscore
#only want first and last value
number = [1, 2, 3, 4]
first, *_, last = number
print(first)
print(last)

person = ['John', 30, 'Engineer','Worchester', 'England']
name, *_, country = person
print(name)
print(country)
print(_)

# ================================================================================
# LIST UNPACKING
# ----------------------------------------
# List unpacking allows us to assign list elements
# to multiple variables in a single line.
#
# The * (asterisk) collects remaining values.
# The _ (underscore) is commonly used to ignore values.
# ================================================================================


# ---------------------------------------
# Basic Unpacking with *
# ---------------------------------------
# * collects remaining middle values.

person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']

name, *details, country = person

print(name)      # -> Maria  (first element)
print(details)   # -> [29, 'Data Engineer', 'city']  (middle values)
print(country)   # -> Spain  (last element)


# Star at the Beginning
# * can also collect values from the start.

person = ['Maria', 29, 'Data Engineer', 'city', 'Spain']

*details, city, country = person

print(details)   # -> ['Maria', 29, 'Data Engineer']  (first values)
print(city)      # -> city
print(country)   # -> Spain


# Strings are iterable.
# * collects remaining characters.

numbers = 'Hi'

first, *rest = numbers

print(first)   # -> H
print(rest)    # -> ['i']


# the * variable becomes an empty list, if nothing to be collected

numbers = 'H'

first, *rest = numbers

print(first)   # -> H  (only character)
print(rest)    # -> []  (no remaining characters)


# ---------------------------------------
# Ignoring Values with _
# ---------------------------------------
# _ is used when we want to skip values.

person = ['Maria', 29, 'Data Engineer', 'Spain']

name, _, role, _ = person

print(name)   # -> Maria
print(role)   # -> Data Engineer


# ---------------------------------------
# Ignoring Multiple Values
# ---------------------------------------
# *_ ignores everything except the last element.

person = ['Maria', 29, 'Data Engineer', 'Spain']

*_, country = person

print(country)   # -> Spain
