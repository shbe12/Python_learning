# ================================================================================
# LOOP CONTROL STATEMENTS
# ----------------------------------------
#tools and addond to put on loops
# Sometimes we don’t want a loop to run normally.
# We may want to stop it early, skip an iteration,
# or simply leave a placeholder for future logic.
#
# In this file, we explore:
# break
# continue
# pass
# for-else
# ================================================================================


# ---------------------------------------
# break
# ---------------------------------------
# The break statement immediately stops the loop when a condition is met.
#the loops ends and goes to the next line of the code.

# for i in (1,2,3):
#     if i == 2:
#         break
#     print(i) # prints 1


names = ['john', 'maria', '', 'kumar']
for name in names:
    print(f'Name = {name}')


print('-----------------------------------')

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print('Empty value detected!')
        break
    print(f'Name = {name}')

# continue
# skips one loop cycle and continues with the next iteration of the loop.
# skip bad or empty data without stopping the loop
# for i in (1,2,3):
#     if i == 2:
#         continue
#     print(i) # prints 1, 3

print('-----------------------------------')

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print('Empty value detected!')
        continue
    print(f'Name = {name}')

# pass
# pass a placeholder where nothing happens, for now just keep going
# if pass true goes to block of code ,normal way of our loop
# for i in (1,2,3):
#     if i == 2:
#         pass
#     print(i) # prints 1, 3

#placeholder while planning next step ,checking for a situatiom, dont know what to do if contdition is true

print('-----------------------------------')

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        pass # todo: handle empty value
    print(f'Name = {name}')

print('-----------------------------------')
#replace pass with logic
names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        name = name.replace('', 'unknown')
    print(f'Name = {name}')

# my try
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# for day in days:
#     if day == 'Saturday', 'Sunday':
#         break
#     print(f'Day = {day}')


print('-----------------------------------')
#used continue because we want to skip the weekend and continue with the next iteration of the loop.
days = ['Mon', 'Sun', 'Wed', 'Tue']
for day in days:
    if day in ['Sat', 'Sun']:
        continue
    print(F'Workday: {day}')

print('-----------------------------------')

days = ['Mon', 'Sun', 'Wed', 'Tue']
weekend = ['Sat', 'Sun']
for day in days:
    if day in weekend:
        continue
    print(F'Workday: {day}')

print ('-----------------------------------')

#check wheter everything is safe , sql injection hacker attack,destroy datatabase or
# read info , do not tust the data at all then break
emails = ['john@example.com',
          'maria@example.com',
          '',
          'DROP TABLE USER;']

for email in emails:
    if ';' in email:
        print('Potential SQL injection detected!')
        break
    print(f'Processing email: {email}')

print('-----------------------------------')

for email in emails:
    if email == '':
        print('Empty email detected!')
        continue
    if ';' in email:
        print('Potential SQL injection detected!')
        break
    print(f'Processing email: {email}')

# break where we add condition if condition fulfilled , we execute the break and exit loop,emergency exit if something goes wrong
# break - all other values totally ignored and we exit immediately,used for high critical -cost,security,integrity.
# continue when condition fulfilled skip this iteration and go to the next one, dont stop loop
# continue- used for medium risk, like empty data ,bad draws, empty files
# pass- when condition fulfilled keep going, just excute the code and do the loop,dont skip or stop
# pass - used for placeholder , planning

# use else statement to run a block of code , only if the loop finishes naturally, without breaks, at the end do something extra
#action executed once loop complete
for i in (1, 2, 3):
    print(i)
else :
    print("End")

print('-----------------------------------')

# for else break
items = [1,3,4,7]
for item in items:
        print(i)
else: #useless
    print("Loop is completed")

#because

items = [1,3,4,7]
for item in items:
        print(item)
print("Loop is completed")

# else make sense once combined with break
#python does not execute the else statement, because the condtion last item was never fulfilled
for i in (1, 2, 3):
    if i == 2:
        break
    print(i)
else:
    print("End")

print('-----------------------------------')

#findif there are evennumbers
items = [1,3,4,7]
for i in items:
        if i % 2 == 0:
            print("Even number found",i)
            break
else:
    print("All numbers are odd")

print('-----------------------------------')

#all odd numbers

items = [1,3,5,7]
for i in items:
        if i % 2 == 0:
            print("Even number found",i)
            break
else:
    print("All numbers are odd")

print('-----------------------------------')
# even numbers without break
#The else is only useful when you're searching for something and using break.

#If you remove break, then the loop always finishes normally, so
# the else will always execute, which is not very useful.
# items = [1,3,4,8]
# for i in items:
#         if i % 2 == 0:
#             print("Even number found",i)
# else:
#     print("All numbers are odd")

# print('-----------------------------------')

#all even numbers
items = [1, 3, 4, 8]

found_even = False

for i in items:
    if i % 2 == 0:
        print("Even number found", i)
        found_even = True

if not found_even: #"If I have not found an even number..."
    print("All numbers are odd")

print('-----------------------------------')

# for else use cases real world applications
#used for search andd validate data

names = ['john', 'maria', None, 'kumar']
for name in names:
    if name is None:
        print('Found a missing name')
        break
else:
    print('All names are available')

print('-----------------------------------')

#only the first true dedtected is shown
files = ['data1.csv', 'report.csv','data.txt','report2.csv']
for file in files:
    if not file.endswith('.csv'):
        print(f' {file} is not a CSV file')
        break
else:
    print('All files are CSV files')

print('-----------------------------------')

files = ['data1.csv', 'report.csv','data.csv','report2.csv']
for file in files:
    if not file.endswith('.csv'):
        print(f' {file} is not a CSV file')
        break
else:
    print('All files are CSV files')

print('-----------------------------------')

files = ['data1.csv', 'report.pdf','data.txt','report2.csv']
for file in files:
    if not file.endswith('.csv'):
        print(f' {file} is not a CSV file')
        continue #cant combine continue with else
else:
    print('All files are CSV files')

print('-----------------------------------')

file_list = ['report.csv',
             'data.xlsx',
             'summary.docx',
             'report.csv',
             'data.csv',
]

# my try
# for file in file_list:
#     if file_list.count > 2:
#         print(f"Duplicate file found: {file}")
#         break
# else:
#     print("All files are unique")

for file in file_list:
    if file_list.count(file) > 1:
        print(f"Duplicate file found: {file}")
        break
else:
    print("All files are unique")

# ================================================================================
# LOOP CONTROL STATEMENTS
# ----------------------------------------
# Sometimes we don’t want a loop to run normally.
# We may want to stop it early, skip an iteration,
# or simply leave a placeholder for future logic.
#
# In this file, we explore:
# break
# continue
# pass
# for-else
# ================================================================================


# ---------------------------------------
# break
# ---------------------------------------
# The break statement immediately stops the loop when a condition is met.

names = ['john', 'maria', '', 'kumar']

for name in names:
    if name == '':
        print('Empty value detected!')
        break
    print(f'Name = {name}')


# ---------------------------------------
# continue
# ---------------------------------------
# The continue statement skips the current iteration and moves to the next one.

names = ['john', 'maria', '', 'kumar']

for name in names:
    if name == '':
        print('Empty value detected!')
        continue
    print(f'Name = {name}')


# ---------------------------------------
# pass
# ---------------------------------------
# The pass statement does nothing.
# It acts as a placeholder for future code.

names = ['john', 'maria', '', 'kumar']

for name in names:
    if name == '':
        pass  # TODO: Handle Empty Value
        name = name.replace('', 'unknown')
    print(f'Name = {name}')



# TASK
# Loop through a list of days and print. only the working days, skipping weekends.
days = ['Mon', 'Sun', 'Wed', 'Tue']
weekends = ['Sat', 'Sun']

for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')


# Real-World Example (Security Check)
# Stop processing if a suspicious input appears.
emails = [
    'data@gmail.com',
    'baraa@outlook.de',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break
    print(f'Processing Email: {email}')


# ---------------------------------------
# for-else
# ---------------------------------------
# The else block runs only if the loop completes without hitting break.

items = [1, 3, 4, 7]

for i in items:
    print(i)
else:
    print("Loop is completed")


# Task: Check for Even Number
# If no even number is found,
# the else block will execute.
items = [1, 3, 5, 7]

for i in items:
    if i % 2 == 0:
        print("Even Nr. Found:", i)
        break
else:
    print("All numbers are odd")


# TASK: Check for missing names in a list.
names = ['Kamara', 'Tuba', None, 'Mounika']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")

# TASK: Check if all files are CSV files.

files = ['data1.csv', 'report.pdf', 'data2.txt', 'report2.csv']

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} is not a CSV')
        break
else:
    print('All files are CSV')


# ---------------------------------------
# Python Challenge
# ---------------------------------------
# Check whether any filename appears more than once.
# Print "Duplicate found" if a duplicate exists,
# otherwise print "All files are unique".

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]

for file in file_list:
    if file_list.count(file) > 1:
        print(f"Duplicate found: {file}")
        break
else:
    print("All files are unique")
