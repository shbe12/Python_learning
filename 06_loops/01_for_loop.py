#Loop tool use to control flow of code repeaat clock of code till stoped
# for and why loops main types of loop
#for loop go though item one by one to do something with each item
#for ,loop variable plus operator in,then the sequence
#python iterator reposible for knowing wherewe are in the loop and the next item,lets you go through items
# () -tuple, [] -list, {} -dictionary, "" -string
for i in (1,2,3):
    print(i)
# ask if each item is the last item, if false, it does action then goes back to the start to ask again, if true it stops the loop
#needs variable to assign value we get from iterator, then we can use that variable to do something with the item
# once last item processed, loop stops and goes to next line of code after the loop
print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")
#or
for i in (1,2,3,4,5):
    print("Round:", i)

for i in (1,2,3,4,5):
    print("Round:1")

for i in (1,2,3,4,5):
    print(f"Round:{i}")

items = (1,2,3,4,5)
for item in items:
    print(f"Round:{item}")

#for loop in sequences
items = [1, 2, 3, 4, 5]
for item in items:
    print(f"Round:{item}")

items = [1, 2, 3, 4, "Hi"]
for item in items:
    print(f"Round:{item}")


# string value is a sequence of characters, so we can use a for loop to go through each character in the string
items = "Python"
for item in items:
    print(f"Round:{item}")

#range
#for i in range(5)
# range (stop) used to tell we must stop generating numbers
#range(5) you get 0,1,2,3,4
for item in range(100):
    print(f"Round:{item}")

#range(start, stop) used to tell we must start generating numbers from start and stop at stop
# start is optional, default is 0, when range start at 1 , it incldes 1 and excludes 5, so you get 1,2,3,4
for item in range(1,5):
    print(f"Round:{item}")

#step is optional, used to define or specify an icrementation, if not used incrementation is always 1
# range (start, stop, step) used to tell we must start generating numbers from start and stop at stop and increment by step
#range(0,10,2) you get 0,2,4,6,8
for item in range(1,10,2):
    print(f"Round:{item}")

# for loop use cases
# we have 100 tables , we writing code for 100 tables
# , we can use loop to do the same thing for all tables, instead of writing code for each table, we can use a loop to do the same thing for all tables
# for filename in [file]:
#     df = pd.read_csv(src)
#     df.to_csv(tgt, index=False)
# we can iterate through colunms in tabel
# for col in df.columns:
#     df[col] = df[col].str.strip()

# use for loops to go through values, aggregate data, like summing,cunting,averaging
scores =[80, 50,60,75]
total = 0
for score in scores:
    total += score # use loop variable not sequence
    print("Current Total:", total)
print("Final Total:", total)

# use loops totransform data like cleaning data vefore processing
files = [' Report.csv ', 'DATA.csv ', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv') #cleaning data then tranform
    print(f"Processing {file}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    number_result = number * 7
    print(f" 7 x {number} = {number_result}")

star = "*"
for
