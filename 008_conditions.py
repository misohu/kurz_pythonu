# Video https://youtu.be/S7HWbBG-vy4
# Jednoduchá podmienka. Splní sa ak je výraz v podmienke pravda. Vzdy musime cast vykonania oddelit 4 medzerami alebo tabulatorom.
is_student=True
if is_student == True:
    print("He is a programmer")

# Ak vyraz nie je prava python vykona kod v casti else
is_programmer=True
if is_programmer == False:
    print("He is a programmer")
else:
    print("He is not a programmer")

# Takto jednoducho vieme retazit podmienky. Ak neplati prvy if python skusi vykonat druhy a ak neplati ani ten python vykona else  
if is_programmer == False:
    print("Is not a programmer")
elif is_student == True:
    print("Is student")
else:
    print("Is a programmer and is not a student")

# Porovnavat vieme aj retazce a polia.
number_list1=[1, 2, 3]
number_list2=[1, 2, 3]

number_list1 == number_list2

# Takto  vieme pouzit premennu s pravdivostnou hodnotou priamo v podmienke
is_programmer=True
if not is_programmer:
    print("He is not a programmer")
else: 
    print("He is a programmer")

# Samozrejme stale viem pouzit logicke operacie alebo boolovske operacie and a or
is_programmer = True 
is_student = True

if is_programmer and is_student:
    print("Is a student programmer")
else: 
    print("Is not a student programmer")

if is_programmer or is_student:
    print("Is either student or programmer or both")
else: 
    print("Is not a student nor a programmer")


# Kazde cislo != 0 ma implicitnu pravdivostnu hodnotu True
if 1:
    print("Its True")
else: 
    print("Its false")

if 0:
    print("Its True")
else: 
    print("Its false")

if 2:
    print("Its True")
else: 
    print("Its false")

if -2:
    print("Its True")
else: 
    print("Its false")

# Pozor toto neplati pri porovnani s boolmi okrem cisla 1 
print(1 == True)
print(0 == False)
print(2 == True) 
print(-2 == True)

# Pravdivostnu hodnotu nadobudaju aj polia. Prazdne pole je False a ple s aspon jednym prvkom je True
if []:
    print("Its True")
else: 
    print("Its false")

if [1,2,3]:
    print("Its True")
else: 
    print("Its false")

# Opat pozor toto neplati pre porovnania 
[] == False
[1] == True

# If vieme napisat aj do jedneho riadku ale vzdy musime napisat aj cast else
is_programmer = False
is_programmer_string = "Is a programmer" if is_programmer
is_programmer_string = "Is a programmer" if is_programmer else "is not a programmer"
print(is_programmer_string)

# Vrchny kod sa da prepisat nasledovne pomocou standardneho ifu
if is_programmer:
    is_programmer_string ="He is a programmer"
else:
    is_programmer_string ="He is not a programmer"
print(is_programmer_string)