string_concatenation="Hello" + "world"
print(string_concatenation)
string_hello="Hello"
string_world="World"
print(string_hello + string_world)
print("Hello" "World") 
# print("Hello" string_world) # Error
print("Hello" + string_world) # OK

# Multiplication 
string_multiplication=3*"Hi " # notice the space
print(string_multiplication)

# String and numbers
print("Number is", 6, "aditional string")
print("Number is" + 6) # Error
print("Number is" + str(6))
print(type(6))
print(type(str(6)))

# Indexing strings
instructor="Michal Hucko"
print(instructor[0]) # Indexed from 0. Sorry mathlab fans :'(
print(type(instructor[0]))
print(instructor[3])
print(instructor[-1])
# print(instructor[16]) # Error
print(instructor[0:6])
print(instructor[:6])
print(instructor[:-1]) # tricky
print(instructor[:2] + instructor[2:])
print(instructor[-4:])

# Careful 
print(instructor[2:103]) 
print(instructor[104:])
print(instructor[45])