# Video: https://youtu.be/pUyZLSJHxZc
# Stringy vieme scitavat. Toto sa nazyva konkatenacia alebo retazenie.
string_concatenation="Hello" + "world"
print(string_concatenation)

# String vieme nascitat aj priamo do printu
string_hello="Hello"
string_world="World"
print(string_hello + string_world)

# Alebo aj takto
print("Hello" "World") 

# Avsak nemozme nappisat string a premennu stringu bez ciarky. Toto sposoby chybu
print("Hello" string_world) 

# Aby sme sa zbavili chyby staci napisat +. Scitavam string a premennu stringu
print("Hello" + string_world) # OK

# String vieme aj nasobit. Vsimnite si ze som pridal medzeru pre krasu.
string_multiplication=3*"Hi "
print(string_multiplication)

# Ak chceme vieme spajat string a cislo pomocou funkcie str, ktora premeni cislo na string
"Number is" + str(6)

# Alebo pomocou funkcie print
print("Number is", 6, "aditional string")

# Ak strig a cislo spocitame mimo funkcie str dostaneme chybu
print("Number is" + 6)

# Takto je to spravne
print("Number is" + str(6))
print(type(6))
print(type(str(6)))

# Do stringu vieme pristupovat pomocou indexu, ktory zacina od nuly
instructor="Michal Hucko"
print(instructor[0])
print(instructor[3])

# -1 je posledny prvok, -2 je predposledny atd.
print(instructor[-1])

# Ak pristupime na neexistujuci prvok dostaneme chybu
print(instructor[16])

# pristupovat vieme aj cez zlozeny index
print(instructor[0:6])
print(instructor[:6])
print(instructor[:-1]) # tricky
print(instructor[:2] + instructor[2:])
print(instructor[-4:])

# Specialne pripady 
print(instructor[2:103]) 
print(instructor[104:])
print(instructor[45])