# Video https://youtu.be/DdemSIz-MpQ
# Slovnik alebo dictionari je datovy typ zalozeny na klucoch a ich hodnotach
# Je to tzv json v pythone :D 
# Definicia
mixed_dict = {
    "Michal" : 23,
    "Felipe" : 32,
    True: "True",
    False: True,
}
print(mixed_dict)
print(type(mixed_dict))

# Pristup k prvkom
mixed_dict['Michal']
mixed_dict['Felipe']
mixed_dict[True]
# mixed_dict['John'] # Error

# Dict je mutable sam o sebe vieme teda menit hodnoty a aj ich vymazavat juchuu
mixed_dict['John'] = 40
mixed_dict['Felipe'] = 33
print(mixed_dict)
del mixed_dict['John']
print(mixed_dict)

# Polia nemozu byt klucami slovnika ale mozu byt hodnotami. Slovink moze byt hodnotou v slovniku
person = { # DONT FORGET THE ciarky na konci riadku !!!
    "name" : "Michal", 
    "surname": "Hucko", 
    "languages": ["Python", "JavaScript", "Java"],
    "instagram": "@misohucko",
    "address": {
        "city": "New York",
        "street": "stret_name",
        "street_number": 45
    }
}

# Ukazka vnoreneho pristupu
person['languages'][-1]
person['address']['street']

# Klucom dictu moze byt len imutable objekt (cize nemoze to byt pole ale moze to byt tuple )
touple_dict={
    (1,2): "touple",
    # [1,2]: "array" # this is an error 
}
print(touple_dict[(1,2)])


# Operacie spojene so slovnikom 
person = { # DONT FORGET THE COMMAS
    "name" : "Michal", 
    "surname": "Hucko", 
    "languages": ["Python", "JavaScript", "Java"],
    "instagram": "@misohucko",
    "address": {
        "city": "New York",
        "street": "stret_name",
        "street_number": 45,
    }
}

# Pristupn na zaklade klucu, ktory nevracia chybu pri neexistujucom kluci!! Moze zadefinovat hodnotu ktora sa vrati ked kluc neexistuje 
person.get("name")  
person.get("not_existing_key", "PLESE NO") 

# . items vrati vsetky kluc-hodnoty slovnika ako list of tuples 
list(person.items()) 

# Potom cez ne vieme takto iterovat. PORIADNE SI TOTO NASTUDUJTE 
for key, value in person.items():
    print(f"Key: {key}, Value {value}")

# . keys vrati list klucov
person.keys() 

# . values vrati list hodnot
person.values() # list of values,  recommend to cast like list(person.keys())

# . pop vrati hodnotu kluca a nasledne kluc vymaze zo slovnika
person.pop("name") # returns the item and removes from dict. Raise error if not presented
print(person) # name is no longer in dict 

# Vrati tuple key-value a vymaze ho zo slovnika 
person.popitem() # removes the last key-value pair added from d and returns it as a tuple



