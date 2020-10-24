# Video https://youtu.be/AFTZeCB6WEk
# Definicia tuple. Tuple je ako imutable list 
number_tuple = (1, 2, 3)
print(type(number_tuple))
number_tuple[0]
number_tuple[0] = 10 

# Tuples su ovela rychlejsie ako polia a vyuzivaju sa hlavne v slovnikoch (dictionaries), ktore predstavime v dalsej lekcii
# Ina definicia tuple
x = 1,2,3
print(x)

# Tuple ako navratova hodnota z funkcie
def funciton_returning_tupple(elemnt1, element2):
    return elemnt1, element2
funciton_returning_tupple(1, 2)

# Tuple vieme potom rozbalit do premennych
e1, e2 = funciton_returning_tupple(1, 2)
print(e1)
print(e2)

# Zamlcanie prvku tuple 
x = (1,2,3)
a,b,_ = x # Bez podtrnika to vracia value error VYSKUSAJ
print(a,b)

# No brain syntax Toto nie je touple ale to druhe je tuple 
not_a_tuple = (2)
a_tuple = (2,) # with only one element !!! 
print(type(not_a_tuple))
print(type(a_tuple))

# Bonusove tuples 
sneaky_tupe = 2,
print(sneaky_tupe)
pack_tuple = "Michal", "Hucko", "Is", "Amazing"
print(pack_tuple)
name, surname, word, another_word = pack_tuple 
print(name, surname, word, another_word) 
name, surname, _, _ = pack_tuple # unpack important and forget other (lazy to make up variable names)
print(name, surname)