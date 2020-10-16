# Video: https://youtu.be/MMxxnj5aP8Y
# String vieme definovat pomocou dvojitych uvodzoviek
string="This is string"

# String, hocijaky datovy typ ale aj premennu vieme vypisat pomocou funkcie print
print(string)
print(1)
print(1.5)
print(True)
jablka = 4
print(jablka)
print("Priamy vypis stringu")

# String vieme definovat aj jednoduchymi uvodzovkami
string='This is string with single quotes'
print(string)

# Takto vieme napisat uvodzovku v stringu definovanom uvodzovkami.
string='This is single quote \' in single quote string'
print(string)

# Takto vieme napisat dvojtu uvodzovku v stringu definovanom uvodzovkami.
string='This is double quote " in single quote'
print(string)

# Takto vieme napisat uvodzovku v stringu definovanom dvojtymi uvodzovkami.
string="This is single quote ' in double quote"
print(string)

# \n je symbol noveho riadku, ktory vidime len pomocou funkcie print
string="This is string with \nnew line"
print(string)

# \t je symbol tabulatoru, ktory vidime len pomocou funkcie print
string="This is string with \n\tnew line and tab"
print(string)

# Co ak nechceme vypisat novy riadok ? Pouzijeme r pred definiciou stringu
tricky_string_path="C:\documents\notes"
print(tricky_string_path)
tricky_string_path_fixed=r"C:\documents\notes"
print(tricky_string_path_fixed)

# String vieme definovat aj na viac riadkov
string="""
This is  
multiline 
string.
"""
print(string)

# a takto sa zbavime zbytocnych mnovych riadkov
string="""\
This is  
multiline 
string. Empty lines fixed\
"""
print(string)