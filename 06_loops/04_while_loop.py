#while loop
# repeats block of code as long as condition is true
# for always predefined sequence and condition in middle predefined from python cantvchange, about whether we are at the end of the sequence .
# while, as long as our condition is true do something , defined our condition, might end up infinite loop, when codition false end
# while condition, until condition false, end loop, if condition true, keep going, keep repeating block of code, until condition false, end loop
#while true can be infinite, add break statement in order to force the loop to stop

# while condition
#in while condion always assign i to a value before the loop
# if we do not give chance for i to change forever loop
i = 1 # inititialization
while i < 4: #condition
    print(i)
    i += 1 #update

print("--------------------------")
count = 1
while count <= 5:
    print(count)
    count += 1

print("--------------------------")

count = 1
while count <= 10:
    print(count)
    count += 2

print("--------------------------")

#ask user for input
# write a program user can only say yes
# looping variable answer
answer = ""
while answer != "yes":
   answer = input("Do you agree? (yes/no): ")
print("Thank You")


# while true
 # infinite loop
# while True:
#     print(i) #

print("--------------------------")

#if condition false goes to the top of the loop
# use break statement to exit the loop
while True:
    x = input ('type')
    if x == 'stop':
        break

print('-----------------------------------')

# while True:
#     print("I'm Unstopable")

print('-----------------------------------')

answer = ""
while answer != "yes":
   answer = input("Do you agree? (yes/no): ")
print("Thank You")

print('-----------------------------------')

while True:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        break
print("Thank You")

# while true vs. condition
# while condition we know when loop should stop, something that can end the loop naturally
# while loop forvever infinite until condition stops the loop
#while condition ,counter, limited retries
# whilte true, open-ended waiting, database, stream Api

#loops for vs while

#For need fixed sequence, predefined condition, if we know how many time we want to iterarate.simple clear hard to make infinite loop
# while loop, open-ended, waiting for something to happen, until condition false, infinite loop, until condition false, break statement to exit the loop

print('-----------------------------------')

# # Python challenge
# # my try
# # answer = ""
# # while answer == "yes" and input.count(not "yes") < 4:
# #     print("Glad we are on the same page")
# #     break
# # print("3 Strikes, You are Out!")

print('-----------------------------------')

#mising when 3 strike you are out
#ttempts = 0
#hile attempts < 3:
#   answer = input("Do you agree? (yes/no): ")
#   if answer == "yes":
#       print("Glad we are on the same page")
#       break
#   attempts += 1
# print("Thank You")

print('-----------------------------------')

# error print both same page and 3 strike you are attempts = 0
# while attempts < 3:
#     answer = input("Do you agree? (yes/no): ")
#     if answer == "yes":
#         print("Glad we are on the same page")
#         break
#     attempts += 1
# print("3 Strikes, You are Out!")

#print 3 strikes previously outside while loop
# after break the next line executed, but we want execution only if it did not break
#the else statement of the while loop, executed only if the loop was not broken out of

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we are on the same page")
        break
    attempts += 1
else:
    print("3 Strikes, You are Out!")

# ================================================================================
# WHILE LOOP
# ----------------------------------------
# A while loop runs as long as a condition is True.
# Unlike the for loop, we do not iterate over a collection.
# Instead, we control the loop using a condition.
#
# It is commonly used when:
# - We do not know how many times the loop should run
# - We wait for user input
# - We repeat until a condition changes
# ================================================================================


# ---------------------------------------
# Basic While Loop
# ---------------------------------------
# The loop runs while the condition is True.
# We must manually update the variable to avoid an infinite loop.

count = 1

while count <= 10:
    print(count)
    count += 2


# TASK: Keep asking the user "Do you agree?" until the user types "yes"
answer = ""

while answer != "yes":
    answer = input("Do you agree? (yes/no): ")

print("Thank You")


# ---------------------------------------
# While True + break
# ---------------------------------------
# Another common pattern.
# The loop runs forever until we explicitly break it.

while True:
    answer = input("Do you agree? (yes/no): ")

    if answer == "yes":
        break

print("Thank You")


# ---------------------------------------
# While Else Break
# ---------------------------------------
# The else block runs only if the loop
# finishes without hitting break.

attempts = 0

while attempts < 3:
    answer = input("Do you agree? (yes/no): ")

    if answer == "yes":
        print("Glad we're on the same page")
        break

    attempts += 1
else:
    print("3 strikes. You're out!")
