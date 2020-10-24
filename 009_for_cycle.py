# Video https://youtu.be/VH_YaAI-BKI
numbers = [1, 2, 3, 4, 5, 10]

# Pomocou for cyklu vieme prechadzat cez polia
for number in numbers:
    print(number)

# Alebo cez retazce.
for letter in "Michal Hucko":
    print(letter) 

# Funkcia range nam pomaha vytvorit pocitadlo, alebo pole cisel <dolnyny interval; horny interval)
counter = range(0, 5)
print(counter)

# Mozme definovat o kolko sa maju prvky v pcitadle zvysovat pomocou tretieho argumentu
range(0, 10, 2)
range(10, 1, -2)

# Pozor na nekonecne pole 
range(0, 10, -2)

# Funkcia range a cyklus for sa casto pouzivaju spolu
for number in range(0, 10, 2):
    print(number)

# Takti vieme iterovat cez akekolvek pole 
letters = ["M", "i", "c", "h", "a", "l", 7, 8.7, [4, 5]]
for item in letters:
    print(item)


# Do cyklu vieme pridat aj podmienky. Pozor na odsadenie (tabulator, 4 medzery)
letters = ["M", "i", "c", "h", "a", "l"]
for letter in letters:
    if letter != 'c':
        print(letter)