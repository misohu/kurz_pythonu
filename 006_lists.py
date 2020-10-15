# List definition
number_list=[0,1,2,3,4,5,6,7]
type(number_list)
string_list=["Michal", "Felipe", "John"]
combined_list=[1,"Michal", "John", True, 1.5]

# List indexing (same as strings)
print(number_list[0])
print(number_list[2:4]) # [2;3>
print(number_list[0:3])
print(number_list[-1])
print(number_list[-2:])

# Concatenation
print(number_list + [8, 9, 10])

# Mutability string vs list 
best_teacher="Michal Hucko"
numbers=[0,1,2,3,4,5]

numbers[0]=10 # Mutable = can be changed
# best_teacher[0]="N"
print(numbers)
print(best_teacher) # Immutable cannot be changed

# Slice assignment
numbers[1:3] # is <1;3)
numbers[1:3] = [11, 12]
print(numbers)
numbers[1:3] = [11, 12 ,13]
print(numbers)
numbers[1:3] = []
print(numbers)

# In place operation vs not in place 
numbers=[0,1,2,3,4,5]
numbers + [1, 2]
print(numbers)
numbers_new=numbers + [1, 2]
print(numbers_new)
numbers+=[1, 2] # the same as numbers=numbers + [1, 2]
print(numbers)
number_of_rooms=0 
number_of_rooms += 1 # the same syntax can be applied to numbers
print(number_of_rooms)

numbers=[0,1,2,3,4,5]
numbers.append(10)
print(numbers)

# The len function 
numbers=[0,1,2,3,4,5]
len(numbers)
len("Michal")

# The remove method
numbers=[0,1,2,3,4,5,0]
numbers.remove(0)
print(numbers)

# Pointers
numbers=[0,1,2,3,4,5,0]
the_same_numbers=numbers # nowm numbers the_same_numbers points to numbers (the_same_numbers -> numbers)
print(the_same_numbers)
the_same_numbers[0] = 10
print(the_same_numbers)
print(numbers)

# Copy of list
numbers=[0,1,2,3,4,5,0]
other_numbers=numbers.copy()
other_numbers[0] = 10 
print(numbers)

# Lists of lists 
numbers_and_lists=[0, 1, 2, 3, 4, 5, 0, [1, 2], [3, 4, [5]]]
print(numbers_and_lists[-1])
print(numbers_and_lists[-1][0])
# try to get only the number 5

# Other list functions 
letters = ['m', 'i', 'c', 'h', 'a', 'l', 'h', 'u', 'c', 'k', 'o']
letters.count('c') 
letters.extend([1, 2]) # appends list element to end
letters.append([1, 2]) # appends list to the end
letters.index('i') # position in list
letters.insert(3, "x") # add elemet to position
print(letters)
letters.remove("c") # removes the element from list
print(letters)
letters.reverse()
print(letters)
letters.pop()
letters.clear() # clears the list

numbers=[8,4,5,1,2,7,8,9,0]
numbers.sort()
print(numbers)