# Video https://youtu.be/kTFkZDNLHt4
# While cyklus ma v sebe podmienku a funguje podobne ako if
counter=0
while counter< 5:
    print(counter)
    counter+=1

# Nekonecny cyklus vieme dosiahnut pomocou while True
counter = 0
while True:
    print(counter)

# Nezabudnite cyklus ukoncit inac pojde do nekonecna.
# Ukoncit cyklus vieme pomocou kluceoveho slova break
counter = 0
while True: 
    print(counter) 
    if counter >= 5:
        break
    counter += 1

# Break vieme pouzit aj na ukoncenie for cyklu
for i in [1,2,3,4]:
    print(i)
    if i == 2:
        break

# Klucove slove continue sa pouziva na predcasne ukoncenie iteracie nie vsak celeho cyklu
counter = 0
while True:  
    if counter == 2:
        counter += 1
        continue
    if counter >= 5:
        break
    print(counter)
    counter += 1

# Opat ho vieme pouzit vo for cikle
for i in [1,2,3,4]:
    if i == 2:
        continue
    print(i)

