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
