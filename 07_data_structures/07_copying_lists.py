#can compare, copying or making a reference
#assignment ,referencing to the same data,change in one shows up in another
letters = ['a', 'b', 'c']
letters_copy = letters  # This creates a reference to the same list
letters.pop()
letters_copy.append('z')
print('Original:',letters)
print('Copy:', letters_copy)

# shallow copy,play with data without affecting original list
letters = ['a', 'b', 'c']
letters_copy = letters.copy() # a separate list in memory
letters.pop()
letters_copy.append('z')
print('Original:',letters)
print('Copy:', letters_copy)

#deep copy
matrix = [
    ['a', 'b'], # row 0
    ['c', 'd'], # row 1
]

matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')  # This modifies the inner list of the copy
print('Original:', matrix)
print('Copy:   ', matrix_copy)
