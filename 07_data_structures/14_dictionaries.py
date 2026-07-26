# other data types store one piece of infomation at a time
# info stores in different variables, but are describing one entity


# dictionary let you store different types of informations in key value pairs, where the key describes what the data means and the value holds your actual data
my_dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a': 40
}

print(my_dict) # dictionaries are ordered
#keys must be unique, if you use the same key again, it will overwrite the previous value
# values allows duplicates
# print(my_dict[1]) # dicionaries are not indexed
# we use keys to access values in dictionaries, not indexes or position numbers
print(my_dict['b']) # this will print 20
# is it mutable?
my_dict['c'] = 80
print(my_dict) # yes, we can change the value of a key in a dictionary
#ordered, keys unique allow duplicate values, keys to acces values, ,mutable

# dictionaries methods
user = { "id":1, "age":30, "city": "berlin"}

# access
print(user["city"])

#missing key , or not part of dictionary
# print(user["name"]) #error
# get returns the values and give nothing if missing
print(user.get("name")) # None
print(user.get("name", "Unknown")) #default value passed

# field checks
print("age" in user)
print("name" not in user)

#view objects
print(user.keys()) # get all keys of dictionary
print(user.values()) # get all values of dictionary
print(user) # print the dictionary
print(user.items()) # get all key value pairs of dictionary
# with .items we get list of tuples , easier to loop, to unpack, do transformations

# looping
for u in user:
    print(u) # prints only keys

for u in user:
    print(user[u]) # prints only values

for u in user:
    print(u, user[u]) # prints key and value

#cleaner way
for key, value in user.items():
    print(key, value) # prints key and value

# add value pairs
user["name"] = "John"
print(user)

# update value of existing key
user["age"] = 35
print(user)

user.update({"age": 40, "city": "Paris"}) # update multiple values at once
print(user)

# remove
user.pop("age") # remove key value pair by key
print(user)

city = user.pop("city")
print(user)
print("Removed Item:", city)

# targeting wrong key
# city = user.pop("salary")
# print(user)
# print("Removed Item:", city) #error

city = user.pop("salary", "Not Found") # default value if key not found, instead of breaking the whole code
print(user)
print("Removed Item:", city)

# user.pop() # error cannot leave empty, must pass a key to remove

#remove item without specifying a key
user.popitem()
print(user) # removes the last item in the dictionary


# creation
# define dictionary , without knowing the values
user = { "id":None,
         "name":None,
         "age":None,
         "city": None
         }

# have list of keys want them all to start with the same values

user = dict.fromkeys(["id", "name", "age", "city"], None)
# user = dict.fromkeys(["id", "name", "age", "city"], 0)
print(user)
user["age"] = 40
print(user)

#real world use case
# query database and in return retrieve for example recors ,we use dictionaries in oder to fill those information
#sql cloumnn keys and values inside colunms
#return records stored as dictionaries where colunm are keys and row values are dictionariy values.
row = {"id": 1,
       "name": "John",
       "age": 30,
       "city":
       "Berlin"}
# another use case is mapping, great for converting codes into friendly labels
# most systems stores data in very short way in order to make to make evrything fast, companies might not understand
# use dictionaries in order to do the mapping between the technical hard values to the friendly easy values, like statues of ordering something
status_map = {"01": "Pending",
              "02": "Shipped",
              "03": "Delivered",
              "04": "Cancelled"}
# mapping abreviations to full names of countries
country_map = {"DE": "Germany",
               "FR": "France",
               "IT": "Italy",
               "ES": "Spain"}

# store environment variables and configurations, config.py file, connect our system to multiple external systems, and we need to store connection information,server name ,port,user,password
# store system setting like host ,port, usernames in one clean place
system_conn ={"DB_HOST": "prod-db.company.com",
              "DB_PORT": 5432,
              "DB_USER": "admin",
              "DB_PASSWORD": "secret"}

# ETL and pipeline settings, great for storing run parameters and controlling  how your ETL  pipeline loads data
# a lot of parameters in order to control the run, the patch of the ETL pipeline,
# configurations to tell ETL how toload data from a to B
etl_config = {"DEBUG_MODE": False,
              "SOURCE_PATH": "/data/source/",
              "DESTINATION_PATH": "/data/destination/",
              "BATCH_SIZE": 1000,
              "RETRY_COUNT": 3}

# store metadata, data about your data
#store the structure of your data, SQL tables for the JSON files,data about data
# we dont see any customers , just describing the structure ,used later in order to process the data correctly in our data platforms
table_metadata = {"table_name": "customers",
                  "columns": {
                  "id": {"type": "integer", "nullable": False},
                   "name": {"type": "string", "nullable": False},
                   "email": {"type": "string", "nullable": False},
                   "age": {"type": "integer", "nullable": True},
                   "city": {"type": "string", "nullable": True}
                  },
                  "row_count": 105320,
                  "file_format": "parquet",
                  "last_updated": "2024-06-15T10:30:00Z",
                  "partition_by": ["country"],
                  "tags": ["pii", "customer_data"],
                 }

# store multiple relaced info
#ordered, key unique , values allow duplicates, keyed "not indexed, mutable"
# methods keys(), values(), items(), get(), update(), pop(), popitem(), fromkeys()
#use for mapping, storing configurations, metadata, ETL settings, and more things want to grouped together in one place

# create new dict
#keep only pairs with string values
#convert values to uppercase
#elegant and short solutions

user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}
# dict comprehension to filter and covert, 3 components: key value expression, a loop, and an optional condition

# user_str = {
#     k:v # Expression
#     for k, v in user.items()# Loop
#     if isinstance(v, str)# Filter
# }

user_str = {
    k: v.upper() # Expression
    for k, v in user.items() # Loop
    if isinstance(v, str) # Filter
}

print(user_str)

user_str = {
    k.upper(): v.lower() # Expression
    for k, v in user.items() # Loop
    if isinstance(v, str) # Filter
}

print(user_str)

# ================================================================================
# DICTIONARIES (KEY • VALUE • LOOKUPS • COMPREHENSION)
# ----------------------------------------
# Dictionaries are:
# - Ordered (Python 3.7+)
# - Mutable
# - Keys must be unique
# - Accessed using keys (not index)
# ================================================================================


# ---------------------------------------
# Basic Dictionary Behavior
# ---------------------------------------
# Dictionaries are: Ordered (Python 3.7+), Mutable, Keys are unique, Accessed by key
my_dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a': 40   # Duplicate key overrides previous
}

print(my_dict)       # -> {'a': 40, 'b': 20, 'c': 20}
print(my_dict['b'])  # -> 20  (key-based access)
my_dict['c'] = 80    # Update value
print(my_dict)       # -> {'a': 40, 'b': 20, 'c': 80}

# ---------------------------------------
# Access & Checks
# ---------------------------------------

user = {"id": 1, "age": 30, "city": "berlin"}

print(user.get("name", "Unknown"))  # -> Unknown (safe access)

print("age" in user)        # -> True
print("name" not in user)   # -> True

# keys(): Returns a view of all dictionary keys.
print(user.keys())

# values(): Returns a view of all dictionary values.
print(user.values())

# items(): Returns key-value pairs as tuples.
print(user.items())

# ---------------------------------------
# Looping Through Dictionary
# ---------------------------------------
# We can loop by keys or key-value pairs.

user = {"id": 1, "age": 30, "city": "berlin"}

# Loop using keys
for u in user:
    print(u, user[u])

# Loop using items()
for key, value in user.items():
    print(key, value)


# ---------------------------------------
# Add • Update • Remove
# ---------------------------------------

user = {"id": 1, "age": 30, "city": "berlin"}

user["name"] = "John"     # Add new key
user["age"] = 35          # Update value

user.update({"age": 40, "city": "Paris"})  # Update multiple keys
print(user)


# pop(): # Remove a key and return its value.
age = user.pop("salary", "Not Found")
print(user)
print("Removed Item:", age)

# popitem(): Remove and return the last inserted pair.
user.popitem()
print(user)


# ---------------------------------------
# Creating Dictionaries
# ---------------------------------------
# Create dictionary with default values.
user = {
    "id": None,
    "name": None,
    "age": None,
    "city": None
}

# fromkeys(): Create dictionary from a list of keys with same default value.
user = dict.fromkeys(["id", "name", "age", "city"], None)
print(user)

# ---------------------------------------
# Dictionary Comprehension Challenge
# ---------------------------------------
# Goal:
# 1. Keep only pairs where value is a string
# 2. Convert keys to UPPERCASE
# 3. Convert values to lowercase

user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

user_str = {
    k.upper(): v.lower()        # Expression (transform)
    for k, v in user.items()    # Loop
    if isinstance(v, str)       # Filter
}

print(user_str)

# Data Structure Review
# list are flexible, ordered, have duplicates, index number, youcan change them, add and remove
# tuple are ordered, have duplicates, index number, you cannot change them, add and remove
# set are unordered, no duplicates, no index number, you can change them, add and remove
# dictionary are ordered, keys unique, values allow duplicates, keyed "not indexed, mutable

# choosing the right ds type
# By default choose list,
# if the data must be protected , no changes allowed, go with tuple
# if the data must be unique , you want some performance use set ,especially to compare multiple datasets together.
# for mapping , multiple info, and mpping things together use dictionaries instead of list
# for dictionaries, whenever data has label,value
# frozen tuple,unique set, mapping dictionary
