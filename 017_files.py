# Video https://youtu.be/fb0x0YwInVM
# Kazdy subor je tvoreny znakmi s znakom konca riadku
# Fkazdy subor je ulozeny na mieste v pocitaci ku ktoremu vedie cesta
# Riadky suboru koncia CR LF, \r\n (WINDOWS :'())  alebo len LF \n (MAC, LINUX)
# CR - carriage return
# Line feed

# Takto sa otvori subor. Je potrebne ho vzdy zavriet !!
file_reader = open('FileFolder/data_file.txt')
print(file_reader)
file_reader.close() # Dont forget to close PLEASE 

# Specialna syntac kde python mimo blocku sam zavrie subor. Pismeno r znamena ze k suboru pristupujeme na citanie
with open("FileFolder/data_file.txt", "r") as file:
    print(file) 
    print(type(file))

# Ine sposoby pristupu su r-read, w-write, rb-read in binary mode, wb-write in binary mode 
with open("FileFolder/data_file.txt", "r") as file:
    print(file.readline(1))
    print(file.readline(1)) # Guess the output
    print(file.readline(2)) # Guess the output 

with open("FileFolder/data_file.txt", "r") as file:
    print(file.readlines())


with open("data_file.txt", "r") as file:
    for line in file.readlines():
        print(line, end='')

# Zapis do suboru
with open("new_data_file.txt", "w") as file:
    for word in ["Michal", "HUcko", "is", "good", "teacher"]:
        file.write(word)

# Priklad
# otvorte subor data_file a prepiste ho do suboru backwards_data_file od zadu 
with open("FileFolder/data_file.txt", "r") as file:
    data = file.readlines()

with open("FileFolder/backwards_data_file.txt", "w") as file:
    for line in reversed(data):
        file.write(line)

# Do suboru mozme aj zapisaovat na jeho koniec pomocou pristupu a - append
with open("FileFolder/backwards_data_file.py", "a") as file:
    for number in [10, 9]:
        file.write(str(number))

# Pristup w vzdy prepisuje obsah suboru 
with open("FileFolder/backwards_data_file.py", "w") as file:
    for number in [10, 9]:
        file.write(str(number))

