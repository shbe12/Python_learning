## Validation

country = "USA"
print(country.isalpha())  # -> True (only letters, no spaces or numbers)

phone = "01761234587"
print(phone.isnumeric())  # -> True (only numbers, no letters or special characters)

# ================================================================================
# STRING VALIDATION METHODS
# ----------------------------------------
# Python provides built-in string methods
# to validate the content of text.
#
# These are extremely useful in:
# - User input validation
# - Form processing
# - Data cleaning
# - ETL pipelines
# ================================================================================

# ---------------------------------------
# isalpha()
# ---------------------------------------
# Returns True if ALL characters are letters.
# No spaces, no numbers, no symbols allowed.

name = "Michael"
print(name.isalpha()) # -> True

name = "Michael123"
print(name.isalpha()) # -> False

name = "Michael Scott"
print(name.isalpha()) # -> False  (space is not a letter)


# ---------------------------------------
# isnumeric()
# ---------------------------------------
# Returns True if ALL characters are numeric.
# Includes special numeric characters.

age = "25"
print(age.isnumeric()) # -> True

age = "25.5"
print(age.isnumeric()) # -> False  (decimal point is not numeric)

age = "25a"
print(age.isnumeric()) # -> False

# ---------------------------------------
# isdigit()
# ---------------------------------------
# Similar to isnumeric() but slightly stricter.
# Used mostly for digit-only strings.

code = "12345"
print(code.isdigit()) # -> True

code = "123a"
print(code.isdigit()) # -> False


# isdigit()	Digits and digit-like characters	"123", "²"
# isnumeric()	Everything isdigit() accepts plus other numeric characters like fractions and numerals	"123", "²", "½", "Ⅳ"#


print("123".isdigit())      # True
print("123".isnumeric())    # True

print("²".isdigit())        # True
print("²".isnumeric())      # True

print("½".isdigit())        # False
print("½".isnumeric())      # True

print("Ⅳ".isdigit())        # False
print("Ⅳ".isnumeric())      # True

print("-5".isdigit())       # False
print("-5".isnumeric())     # False

print("3.14".isdigit())     # False
print("3.14".isnumeric())   # False

# ---------------------------------------
# isalnum()
# ---------------------------------------
# Returns True if string contains
# only letters and numbers (no spaces).

username = "User123"
print(username.isalnum()) # -> True

username = "User 123"
print(username.isalnum()) # -> False

# ---------------------------------------
# Python Challenge
# ---------------------------------------

data = "968-Maria, (D@t@ Engineer );; 27yr    "
new_data =(data.lower()
      .replace('@', 'a')
      .replace('968-','name: ')
      .replace (',','')
      .replace (';;', '')
      .replace (')', '')
      .replace ('(', '')
      .replace ('yr', '')

)  # -> "968-maria, (d@t@) engineer );; 27yr    "
print(new_data)
new_data = new_data.split()  # -> ["name:maria", "data", "engineer", "27"]
print(new_data)
new_data = f"{new_data[0]} {new_data[1]} | role: {new_data[2]} {new_data[3]} | age: {new_data[4]}"  # -> "name:maria data engineer age:27"
print(new_data)
################################################################

data = "968-Maria, (D@t@ Engineer );; 27yr"

clean_data = (
    data.lower()
        .replace("968-", "")
        .replace("@", "a")
        .replace(",", "")
        .replace("(", "")
        .replace(")", "")
        .replace(";;", "")
        .replace("yr", "")
)

parts = clean_data.split()

name = parts[0]
role = parts[1] + " " + parts[2]
age = parts[3]

print(f"name: {name} | role: {role} | age: {age}")

# unpacking####################################################
data = "968-Maria, (D@t@ Engineer );; 27yr"

clean_data = (
    data.lower()
        .replace("968-", "")
        .replace("@", "a")
        .replace(",", "")
        .replace("(", "")
        .replace(")", "")
        .replace(";;", "")
        .replace("yr", "")
)

name, first_role, second_role, age = clean_data.split()

print(f"name: {name} | role: {first_role} {second_role} | age: {age}")
