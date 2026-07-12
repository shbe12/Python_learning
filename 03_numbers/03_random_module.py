import random #importing random module
print(random.random()) #generates a random float number between 0 and 1
print(random.randint(1,6)) #generates a random integer between 1 and 6
#random sampling, ids
# ================================================================================
# RANDOM MODULE (SIMULATION • SAMPLING • SHUFFLING)
# ----------------------------------------
# The random module allows us to generate
# unpredictable values.
#
# Used in:
# - Games
# - Simulations
# - Data Sampling
# - Testing
# - Machine Learning experiments
# ================================================================================


import random


# ---------------------------------------
# random()
# ---------------------------------------
# Returns a float between 0.0 and 1.0

print(random.random())

# ---------------------------------------
# randint()
# ---------------------------------------
# Returns an integer between two values (inclusive)

print(random.randint(1, 6))

# ---------------------------------------
# uniform()
# ---------------------------------------
# Returns a random float between two numbers

print(random.uniform(10, 20))
# -> Example: 14.8271


# ---------------------------------------
# choice()
# ---------------------------------------
# Select one random element from a sequence

colors = ["red", "blue", "green"]
print(random.choice(colors))

#A good analogy

# Imagine your list is a deck of cards.

# random.choice(deck) → Pick one card from the deck.
# random.shuffle(deck) → Shuffle the entire deck.

# When you shuffle a deck, you don't get a new deck back—the deck itself is now in a different order.

# Rule of thumb

# If a method or function modifies a mutable object (like a list), it often returns None.

# Some common examples are:

# numbers.sort()      # Returns None
# numbers.reverse()   # Returns None
# numbers.append(6)   # Returns None
# random.shuffle(numbers)  # Returns None

# ---------------------------------------
# shuffle()
# ---------------------------------------
# Shuffles a list in place (modifies original list)
#random.shuffle(numbers) shuffles the original list directly. Since it has already changed the list, it doesn't need to return a new one.

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)
print(numbers)

# ---------------------------------------
# sample()
# ---------------------------------------
# Select multiple unique random elements

students = ["Ali", "Sara", "John", "Maria", "Kumar"]

print(random.sample(students, 2))

# ---------------------------------------
# seed()
# ---------------------------------------
# you're telling Python:

# "Start the random number generator from this exact starting point."

# That starting point is called the seed.

# Because the seed is always the same (42), Python generates the same sequence of "random" numbers every time.
# Controls randomness for reproducibility.
# Same seed -> same results every run.

random.seed(42)
print(random.randint(1, 10))

# # import random

# students = ["Ali", "Sara", "John", "Maria", "Kumar"]

# # One random student
# random.choice(students)

# # Three students, no repeats
# random.sample(students, 3)

# # Three students, repeats allowed
# random.choices(students, k=3)

# A possible result from random.choices() is:

# ['Sara', 'Sara', 'John']

# because each selection is independent, just like calling random.choice() three times.

# That's the main difference:

# choice() → one pick.
# choices() → multiple picks with replacement (repeats allowed).
# sample() → multiple picks without replacement (no list element is selected twice).
