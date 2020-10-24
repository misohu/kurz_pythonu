# Video https://youtu.be/ZeTobU9tomc
# Vlastna funkcia na scitanie dvoch cisel. Uistite sa ze ste pridali return
def addition(a, b):
    result = a + b
    return result

addition(5,4)
addition("Michal" , "Hucko")

# Funkciu vieme aj retazit
# x = 5 + 4 +3 
addition(addition(5, 4), 3)
addition(addition(addition(addition("Michal" , "Hucko"), "is"), "the"), "best")

# Funkcia na scitanie 2 stringov s vyuzitim delimiteru
def string_addition_with_delimiter(string1, string2, delimiter):
    return string1 + delimiter + string2

string_addition_with_delimiter("Michal" , "Hucko", ", ")
# Ak vyuzijeme pomenovane atributy mozme ich ulozit v roznom poradi
string_addition_with_delimiter(delimiter=" ", string2="Hucko", string1="Michal")

# Optional parametre funkcie. Musia byt definovane vzdy za  vynutenymi parametrami inac nastane chyba !! 
def string_addition_with_delimiter(string1, string2, delimiter=" "):
    return string1 + delimiter + string2

string_addition_with_delimiter("Michal" , "Hucko")
string_addition_with_delimiter("Michal" , "Hucko", ", ")

# Podme si definovat funkciu ktora vrati sucet pola
numbers = list(range(7))
print(numbers)

# Funkciu nemozme pomenovat sum lebo je to vyhradene slovo 
def sum_list(numbers):
    total = 0 
    for number in numbers:
        total += number
    return total

sum_list(numbers)
sum(numbers) # build in python function 

# sum_list(["M", "i", "c", "h", "a", "l"]) # Preco je toto chyba ? 

# Funkcie vieme pouzit kde kilvek v kode napr v podmienke 
def simple_sum(a, b):
    return a+b

if simple_sum(4,3) > simple_sum(5,2):
    print("First is bigger")
else:
    print("Second is bigger")

# Alebo v poli 
[simple_sum(3,4), simple_sum(simple_sum(1,2), 3)]